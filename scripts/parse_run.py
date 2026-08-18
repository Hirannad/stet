#!/usr/bin/env python3
"""Parse a stet run's four-part output into counts, rows and cluster scores. No dependencies.

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

Two things here are arithmetic rather than shape, and they are the reason a run is calibration
data at all. Section 3's reason code must come from the closed list in method/constants.yml —
`--strict` fails on an unknown one — and section 4's stated points must equal what the cited
patterns are worth in the catalogue. Neither can be checked by reading prose carefully.

One check is a *recording* requirement, not part of the output shape SKILL.md specifies: a file
under tests/corpus/runs/ must open with a provenance comment naming the skill copy that produced
it, because the Skill tool serves the installed plugin rather than the working tree and a run
that cannot say which copy it read is not evidence about either. A recorded hash that no longer
matches is reported as `stale`, not as a failure — a run measures the version it names, and that
is exactly why it names one.
"""
import hashlib
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from check import HEADER, TAG, ROOT, load_yaml  # single-source the grammar  # noqa: E402

CONSTANTS = load_yaml(ROOT / "method" / "constants.yml")
REASONS = CONSTANTS["shape"]["suspect_reasons"]
POINTS = CONSTANTS["skills"]["stet-hungarian"]["cluster_points"]

SECTIONS = [
    (0, "Nyelv és regiszter"),
    (1, "A javított szöveg"),
    (2, "Változástábla"),
    (3, "Gyanús, de nem javítottam"),
    (4, "Klaszterpontok"),
]
CHANGE_COLUMNS = ["ID", "Eredeti", "Új", "Indok"]
CLUSTER_COLUMNS = ["#", "Kezdet", "Pont", "Minták"]
PROFILES = ["informal", "neutral", "formal", "legal"]
EMPTY = "nincs"
NO_PATTERN = "nincs minta"

# [ \t]*$ and not \s*$: in the fence-masked text a fenced body is whitespace-only, and a
# greedy \s* swallows it whole, leaving section 1 apparently empty.
SECTION_RE = re.compile(r"^## (\d)\. (.+?)[ \t]*$", re.M)
PID_RE = re.compile(r"\bHU-[A-Z]\d{2}\b")
SUSPECT_RE = re.compile(r"^- \*\*(.+?)\*\*\s+\[([a-z-]+)\]\s+–\s+(.*)$")
PROVENANCE_RE = re.compile(
    r"^<!-- stet-run: source=(?P<source>\S+) sha256=(?P<sha>[0-9a-f]{8,}) "
    r"date=(?P<date>\d{4}-\d{2}-\d{2}) -->\s*$", re.M)


def digest(path):
    """Content hash of a skill copy: every markdown file under it, path and bytes.

    The whole directory rather than SKILL.md alone, because the installed plugin differed from
    the working tree in its *catalogue* as much as in its instructions — a run that read a
    catalogue without HU-R11 in it is not the run this file claims to record.
    """
    h = hashlib.sha256()
    files = sorted(path.rglob("*.md")) if path.is_dir() else [path]
    for f in files:
        h.update(f.relative_to(ROOT).as_posix().encode() + b"\0" + f.read_bytes())
    return h.hexdigest()


def catalogue():
    """Pattern ID -> {severity, points}, read from the catalogue itself.

    Points come from the AI: tag through the constants file's scale, so that section 4's
    arithmetic is checked against the same numbers the skill scores with. The estimate marker
    is stripped: it qualifies where the value came from, not what it is worth.
    """
    out = {}
    for f in sorted((ROOT / "skills").glob("*/references/*.md")):
        for line in f.read_text(encoding="utf-8").splitlines():
            m = HEADER.match(line)
            if m:
                tags = TAG.findall(m["tags"])
                ai = [t[3:].rstrip("?") for t in tags if t.startswith("AI:")]
                out[m["id"]] = {
                    "severity": tags[0].split(":")[0].strip() if tags else "",
                    "points": POINTS.get(ai[0], 0) if ai else 0,
                }
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


def parse(text, cat=None):
    cat = catalogue() if cat is None else cat
    problems = []
    sections, order = split_sections(text)

    prov = PROVENANCE_RE.search(text)
    provenance = None
    if prov:
        src = ROOT / prov["source"]
        if not src.exists():
            problems.append(f"provenance names a file that does not exist: {prov['source']}")
        provenance = {
            "source": prov["source"], "sha256": prov["sha"], "date": prov["date"],
            "current": src.exists() and digest(src).startswith(prov["sha"]),
        }

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
                unknown = [i for i in ids if i not in cat]
                if unknown:
                    problems.append(f"change row cites undefined pattern(s) {unknown}")
                kinds = {cat[i]["severity"] if i in cat else "?" for i in ids}
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
                                f"`- **ID** [reason] – text`: {item[:60]!r}")
                continue
            label, reason = m.group(1), m.group(2)
            ids = PID_RE.findall(label)
            if not ids and label != NO_PATTERN:
                problems.append(f"suspect item label must be a pattern ID or "
                                f"{NO_PATTERN!r}: {label!r}")
            if reason not in REASONS:
                problems.append(f"unknown reason code {reason!r} on {label!r}; "
                                f"the list is closed: {REASONS}")
            # One direction only. "No pattern reaches it" is a claim the label already makes, so
            # the code may not make it where a pattern is cited — but the reverse is allowed: an
            # uncited entry can still have been stopped by something that says keep it.
            elif reason == "no-pattern" and label != NO_PATTERN:
                problems.append(f"reason {reason!r} contradicts the label {label!r}")
            suspects.append({"ids": ids, "reason": reason, "note": m.group(3)})

    # 4. cluster points. Every paragraph gets a row, so the denominator is visible, and the
    # points are recomputed here from the catalogue: a stated score that does not follow from
    # the patterns beside it is the one arithmetic error nobody catches by reading.
    clusters = []
    body4 = sections.get(4, (None, ""))[1]
    if body4 == EMPTY:
        pass
    elif 4 in sections:
        rows = parse_table(body4)
        if not rows:
            problems.append(f"section 4 is neither a table nor the single word {EMPTY!r}")
        else:
            if rows[0] != CLUSTER_COLUMNS:
                problems.append(f"section 4 columns {rows[0]}, want {CLUSTER_COLUMNS}")
            for n, cells in enumerate(rows[1:], 1):
                if len(cells) != len(CLUSTER_COLUMNS):
                    problems.append(f"cluster row has {len(cells)} cells: {cells[:2]}")
                    continue
                num, start, points, patterns = cells
                if num != str(n):
                    problems.append(f"cluster rows run 1..N in order: {num!r} in position {n}")
                ids = PID_RE.findall(patterns)
                if not ids and patterns != EMPTY:
                    problems.append(f"cluster row {num} pattern cell is neither IDs nor "
                                    f"{EMPTY!r}: {patterns!r}")
                if len(set(ids)) != len(ids):
                    problems.append(f"cluster row {num} counts a pattern twice: {ids}")
                unknown = [i for i in ids if i not in cat]
                if unknown:
                    problems.append(f"cluster row {num} cites undefined pattern(s) {unknown}")
                hard = [i for i in ids if i in cat and cat[i]["severity"] != "SOFT"]
                if hard:
                    problems.append(f"cluster row {num} scores non-SOFT pattern(s) {hard}")
                try:
                    got = int(points)
                except ValueError:
                    problems.append(f"cluster row {num} points not a number: {points!r}")
                    continue
                want = sum(cat[i]["points"] for i in ids if i in cat)
                if not unknown and got != want:
                    problems.append(f"cluster row {num}: {got} points, but {ids or 'no pattern'} "
                                    f"sum to {want}")
                clusters.append({"n": n, "start": start, "points": got, "ids": ids})

    # A SOFT pattern that produced an edit demonstrably survived every gate, so it must appear in
    # the cluster table. This does not check which paragraph — the parser cannot map a row to one —
    # but it catches the omission that reading cannot: a scored pattern silently missing from the
    # arithmetic. It found one on its first run over this corpus.
    if clusters:
        scored = {i for c in clusters for i in c["ids"]}
        edited = {i for c in changes for i in c["ids"] if cat.get(i, {}).get("severity") == "SOFT"}
        for pid in sorted(edited - scored):
            problems.append(f"{pid} was edited as SOFT but scores in no paragraph")

    return {
        "provenance": provenance,
        "register": register,
        "corrected": corrected,
        "changes": changes,
        "suspects": suspects,
        "clusters": clusters,
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
            # Which brake actually binds is the question the suspect list exists to answer, and
            # free prose could not answer it: round 2 could only report that the rule's named
            # reasons covered 5 of 15 entries on one run.
            "reasons": {r: sum(1 for s in suspects if s["reason"] == r)
                        for r in REASONS if any(s["reason"] == r for s in suspects)},
            "paragraphs": len(clusters),
            "paragraphs_scored": sum(1 for c in clusters if c["points"] > 0),
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

    cat, bad = catalogue(), 0
    results = {}
    for p in paths:
        r = parse(p.read_text(encoding="utf-8"), cat)
        # The recording contract, applied where recordings live. See the module docstring.
        if r["provenance"] is None and "corpus/runs/" in p.as_posix():
            r["problems"].append("no provenance comment: a recorded run must name the skill "
                                 "copy that produced it")
        results[str(p)] = r

    if as_json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
    else:
        print("rows/patterns for FIX and SOFT; suspects as cited/no-pattern; "
              "paragraphs as scored/all\n")
        print(f"{'run':<38} {'reg':<9} {'FIX':>7} {'SOFT':>7} {'susp':>8} {'par':>7} "
              f"{'skill':>6}  shape")
        for name, r in results.items():
            c, n, prov = r["counts"], len(r["problems"]), r["provenance"]
            print(f"{Path(name).name:<38} {r['register'] or '?':<9} "
                  f"{str(c['fix']) + '/' + str(c['fix_patterns']):>7} "
                  f"{str(c['soft']) + '/' + str(c['soft_patterns']):>7} "
                  f"{str(c['suspect_cited']) + '/' + str(c['suspect_nopattern']):>8} "
                  f"{str(c['paragraphs_scored']) + '/' + str(c['paragraphs']):>7} "
                  f"{('same' if prov['current'] else 'stale') if prov else '?':>6}  "
                  f"{'ok' if not n else str(n) + ' problem(s)'}")
        reasons = {}
        for r in results.values():
            for code, k in r["counts"]["reasons"].items():
                reasons[code] = reasons.get(code, 0) + k
        if reasons:
            print("\nwhat blocked the suspects: "
                  + ", ".join(f"{c}={k}" for c, k in sorted(reasons.items(), key=lambda x: -x[1])))
    for name, r in results.items():
        for prob in r["problems"]:
            bad += 1
            print(f"  ✗ {Path(name).name}: {prob}", file=sys.stderr)

    return 1 if (strict and bad) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
