#!/usr/bin/env python3
"""Parse a stet run's three-part output into counts and rows. No dependencies.

The shape read here is specified in `skills/stet-hungarian/SKILL.md`, section `## Kimenet`.
**SKILL.md is authoritative.** If the two disagree, this script is the one that is wrong.

Why this exists: round 2 counted eighteen runs by hand, because the output shape varied enough
between runs that a line-range parser could not tell a change row from a suspect entry. Those
counts therefore rest on one person reading carefully, with no artefact anyone can re-derive
them from. See docs/validation.md, round 2 finding 4.

Usage:
    python3 scripts/parse_run.py tests/corpus/runs/*.md          # table of counts
    python3 scripts/parse_run.py --json tests/corpus/runs/x.md   # full parse
    python3 scripts/parse_run.py --strict tests/corpus/runs/*.md # exit 1 on shape violations

One judgment call is made here rather than buried: a change row may cite several patterns
(the catalogue's own worked example merges HU-R04 and HU-T15 into one row). Such a row counts
as SOFT if **any** cited pattern is SOFT, because the edit budget counts soft edits and the
strictest reading is the safe one. Rows are counted as rows, never as pattern mentions.
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from check import HEADER, TAG, ROOT  # single-source the header grammar  # noqa: E402

SECTIONS = [
    (0, "Nyelv és regiszter"),
    (1, "A javított szöveg"),
    (2, "Változástábla"),
    (3, "Gyanús, de nem javítottam"),
]
CHANGE_COLUMNS = ["ID", "Eredeti", "Új", "Indok"]
PROFILES = ["informal", "neutral", "formal", "legal"]
EMPTY = "nincs"

# [ \t]*$ and not \s*$: in the fence-masked text a fenced body is whitespace-only, and a
# greedy \s* swallows it whole, leaving section 1 apparently empty.
SECTION_RE = re.compile(r"^## (\d)\. (.+?)[ \t]*$", re.M)
PID_RE = re.compile(r"\bHU-[A-Z]\d{2}\b")
SUSPECT_RE = re.compile(r"^- \*\*(.+?)\*\*\s+–\s+(.*)$")


def severities():
    """Pattern ID -> severity, read from the catalogue itself."""
    out = {}
    for f in sorted((ROOT / "skills").glob("*/references/*.md")):
        for line in f.read_text(encoding="utf-8").splitlines():
            m = HEADER.match(line)
            if m:
                tags = TAG.findall(m["tags"])
                out[m["id"]] = tags[0].split(":")[0].strip() if tags else ""
    return out


def mask_fences(text):
    """Blank fenced blocks, preserving every offset, so that headings *inside* the corrected
    text are not mistaken for section boundaries.

    Not hypothetical: a real specimen's corrected text carried five `##` headings of its own,
    and an adversarial `## 2.` inside a fence split the run into `[0, 1, 2, 2, 3]`.
    """
    out, in_fence = [], False
    for line in text.split("\n"):
        if line.lstrip().startswith(("```", "~~~")):
            in_fence = not in_fence
            out.append(" " * len(line))
        else:
            out.append(" " * len(line) if in_fence else line)
    return "\n".join(out)


def split_sections(text):
    hits = list(SECTION_RE.finditer(mask_fences(text)))
    out = {}
    for i, m in enumerate(hits):
        end = hits[i + 1].start() if i + 1 < len(hits) else len(text)
        out[int(m.group(1))] = (m.group(2), text[m.end():end].strip())
    return out, [(int(m.group(1)), m.group(2)) for m in hits]


def parse_table(body):
    """Rows of a pipe table, as lists of stripped cells. Header and rule excluded."""
    rows = []
    for line in body.splitlines():
        line = line.strip()
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if all(set(c) <= set("-: ") for c in cells):
            continue  # the |---|---| rule
        rows.append(cells)
    return rows


def parse(text, sev=None):
    sev = severities() if sev is None else sev
    problems = []
    sections, order = split_sections(text)

    if [n for n, _ in order] != [n for n, _ in SECTIONS]:
        problems.append(f"section numbers/order: got {[n for n, _ in order]}, "
                        f"want {[n for n, _ in SECTIONS]}")
    for num, title in SECTIONS:
        if num not in sections:
            problems.append(f"missing section {num}. {title}")
        elif sections[num][0] != title:
            problems.append(f"section {num} title: {sections[num][0]!r}, want {title!r}")
    if re.search(r"^#{3,} ", mask_fences(text), re.M):
        problems.append("subsection heading present; sections must be flat")

    # 0. register
    register = None
    if 0 in sections:
        found = [p for p in PROFILES if f"`{p}`" in sections[0][1]]
        if len(found) == 1:
            register = found[0]
        else:
            problems.append(f"section 0 must name exactly one backticked profile, found {found}")

    corrected = sections.get(1, (None, ""))[1]
    if not corrected:
        problems.append("section 1 is empty; the corrected text is never optional")

    # 2. change table
    changes = []
    body2 = sections.get(2, (None, ""))[1]
    if body2 == EMPTY:
        pass
    elif 2 in sections:
        rows = parse_table(body2)
        if not rows:
            problems.append(f"section 2 is neither a table nor the single word {EMPTY!r}")
        else:
            if rows[0] != CHANGE_COLUMNS:
                problems.append(f"section 2 columns {rows[0]}, want {CHANGE_COLUMNS}")
            for cells in rows[1:]:
                if len(cells) != len(CHANGE_COLUMNS):
                    problems.append(f"change row has {len(cells)} cells: {cells[:2]}")
                    continue
                ids = PID_RE.findall(cells[0])
                if not ids:
                    problems.append(f"change row cites no pattern ID: {cells[0]!r}")
                unknown = [i for i in ids if i not in sev]
                if unknown:
                    problems.append(f"change row cites undefined pattern(s) {unknown}")
                kinds = {sev.get(i, "?") for i in ids}
                changes.append({
                    "ids": ids,
                    "original": cells[1], "new": cells[2], "reason": cells[3],
                    "kind": "SOFT" if "SOFT" in kinds else "FIX",
                })

    # 3. suspect list
    suspects = []
    body3 = sections.get(3, (None, ""))[1]
    if body3 == EMPTY:
        pass
    elif 3 in sections:
        items = [ln for ln in body3.splitlines() if ln.startswith("- ")]
        if not items:
            problems.append(f"section 3 is neither a bullet list nor the single word {EMPTY!r}")
        for item in items:
            m = SUSPECT_RE.match(item)
            if not m:
                problems.append(f"suspect item does not match "
                                f"`- **ID** – text`: {item[:60]!r}")
                continue
            label = m.group(1)
            ids = PID_RE.findall(label)
            if not ids and label != "nincs minta":
                problems.append(f"suspect item label must be a pattern ID or "
                                f"'nincs minta': {label!r}")
            suspects.append({"ids": ids, "note": m.group(2)})

    return {
        "register": register,
        "corrected": corrected,
        "changes": changes,
        "suspects": suspects,
        # Rows and distinct patterns are both reported, because they answer different questions
        # and the row count alone misleads. A text-wide orthographic habit becomes one row per
        # sentence, so "5 FIX" can mean one decision applied five times. The row unit is still
        # right — it is what reconciles with the sentence budget — but it is not the headline.
        #
        # Suspects split by whether a pattern was cited at all: a damaged specimen fills the list
        # with defects the catalogue has no pattern for (22 entries, 13 of them `nincs minta` on
        # one specimen here), and those are not comparable with blocked-pattern entries.
        "counts": {
            "fix": sum(1 for c in changes if c["kind"] == "FIX"),
            "soft": sum(1 for c in changes if c["kind"] == "SOFT"),
            "fix_patterns": len({i for c in changes if c["kind"] == "FIX" for i in c["ids"]}),
            "soft_patterns": len({i for c in changes if c["kind"] == "SOFT" for i in c["ids"]}),
            "suspect": len(suspects),
            "suspect_cited": sum(1 for s in suspects if s["ids"]),
            "suspect_nopattern": sum(1 for s in suspects if not s["ids"]),
        },
        "problems": problems,
    }


def main(argv):
    strict = "--strict" in argv
    as_json = "--json" in argv
    paths = [Path(a) for a in argv if not a.startswith("--")]
    if not paths:
        print(__doc__.strip().splitlines()[0])
        print("usage: parse_run.py [--json] [--strict] FILE...")
        return 2

    sev, bad = severities(), 0
    results = {}
    for p in paths:
        results[str(p)] = parse(p.read_text(encoding="utf-8"), sev)

    if as_json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
    else:
        print("rows/patterns for FIX and SOFT; suspects as cited/no-pattern\n")
        print(f"{'run':<40} {'reg':<9} {'FIX':>7} {'SOFT':>7} {'susp':>8}  shape")
        for name, r in results.items():
            c, n = r["counts"], len(r["problems"])
            print(f"{Path(name).name:<40} {r['register'] or '?':<9} "
                  f"{str(c['fix']) + '/' + str(c['fix_patterns']):>7} "
                  f"{str(c['soft']) + '/' + str(c['soft_patterns']):>7} "
                  f"{str(c['suspect_cited']) + '/' + str(c['suspect_nopattern']):>8}  "
                  f"{'ok' if not n else str(n) + ' problem(s)'}")
    for name, r in results.items():
        for prob in r["problems"]:
            bad += 1
            print(f"  ✗ {Path(name).name}: {prob}", file=sys.stderr)

    return 1 if (strict and bad) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
