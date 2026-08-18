#!/usr/bin/env python3
"""Structural checks for stet skills. No dependencies.

method/constants.yml is authoritative; this script asserts the prose agrees with it.
Run before every commit: `make check`.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FAIL = []


def fail(where, msg):
    FAIL.append(f"{where}: {msg}")


# ---------------------------------------------------------------- tiny YAML reader
# Handles the subset constants.yml uses: nested maps, inline lists, inline dicts, scalars.
def load_yaml(path):
    root = {}
    stack = [(-1, root)]
    for raw in path.read_text(encoding="utf-8").split("\n"):
        line = raw.split(" #")[0].rstrip() if " #" in raw else raw.rstrip()
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        indent = len(line) - len(line.lstrip())
        key, _, val = line.strip().partition(":")
        val = val.strip()
        while stack and stack[-1][0] >= indent:
            stack.pop()
        parent = stack[-1][1]
        if val == "":
            node = {}
            parent[key] = node
            stack.append((indent, node))
        else:
            parent[key] = parse_scalar(val)
    return root


def parse_scalar(v):
    if v.startswith("[") and v.endswith("]"):
        items = [x.strip().strip('"').strip("'") for x in v[1:-1].split(",") if x.strip()]
        return [parse_scalar(i) if not i.startswith('"') else i for i in items]
    if v.startswith("{") and v.endswith("}"):
        out = {}
        for part in v[1:-1].split(","):
            k, _, x = part.partition(":")
            out[k.strip()] = parse_scalar(x.strip())
        return out
    if v.startswith('"') and v.endswith('"'):
        return v[1:-1]
    try:
        return int(v)
    except ValueError:
        pass
    try:
        return float(v)
    except ValueError:
        return v


# ---------------------------------------------------------------- header grammar
HEADER = re.compile(
    r"^### (?P<id>[A-Z]{2}-[A-Z]\d{2}) · (?P<name>.+?) · "
    r"(?P<tags>\[.+\])\s*$"
)
TAG = re.compile(r"\[([^\]]+)\]")


# ------------------------------------------------------- typography the catalogue got wrong itself
# Two gates, one defect shape: the catalogue printing a form it forbids. Validation round 1 found
# 69 half-fixed „…" quote pairs in its own examples, so a run matching the printed example emitted
# half-fixed output. Round 2 found one more that wrapped across two lines, and 271 em dashes in the
# catalogue's own Hungarian voice while HU-T02 calls the em dash "not used in modern Hungarian
# typography".
#
# Exemptions are narrow and mechanical:
#   - inline code spans, which is how a pattern file demonstrates a wrong glyph;
#   - in a skill file, Jelek: and ROSSZ: lines and substitution rows (→), which demonstrate
#     without backticks;
#   - YAML frontmatter, whose description is English prose read by an English-speaking router,
#     so English typography applies there — em dash included.
# Blanking a line rather than dropping it keeps the reported line numbers honest.
FRONTMATTER = re.compile(r"\A---\n.*?\n---\n", re.S)


def blank_out(text, spans_pattern):
    """Replace every match with the same number of newlines, so line numbers survive."""
    return spans_pattern.sub(lambda m: "\n" * m.group(0).count("\n"), text)


def check_quote_glyphs(rel, text, skill, hungarian=False):
    scannable = []
    for line in text.split("\n"):
        demonstrates = skill and (line.startswith(("Jelek:", "ROSSZ:")) or "→" in line)
        scannable.append("" if demonstrates else re.sub(r"`[^`]*`", "", line))
    body = blank_out("\n".join(scannable), FRONTMATTER)

    def report(pattern, message):
        for m in re.finditer(pattern, body):
            fail(rel, f"line {body[:m.start()].count(chr(10)) + 1}: {message}")

    report(r"„[^„”]*[\"“]", "Hungarian quote closed with the wrong glyph (want ”)")
    if hungarian:
        report(r"—", "em dash in Hungarian prose (want a spaced en dash)")


def check_skill(skill_dir, cfg, shape):
    name = skill_dir.name
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        fail(name, "no SKILL.md")
        return

    files = [skill_md] + sorted(skill_dir.glob("references/*.md"))
    seen, overrides_found, all_text, headers_by_id = {}, set(), {}, {}
    soft_ids = set()

    for f in files:
        rel = f.relative_to(ROOT)
        text = f.read_text(encoding="utf-8")
        all_text[str(rel)] = text
        if f.name == "SKILL.md":
            continue  # SKILL.md's headers are illustrative, not definitions

        headers = 0
        blocks = re.split(r"^(?=### )", text, flags=re.M)
        for block in blocks:
            m = HEADER.match(block.split("\n")[0])
            if not block.startswith("### "):
                continue
            headers += 1
            if not m:
                fail(rel, f"unparseable header: {block.split(chr(10))[0][:80]}")
                continue
            pid, tags = m["id"], TAG.findall(m["tags"])
            if pid in seen:
                fail(rel, f"duplicate pattern id {pid} (also in {seen[pid]})")
            seen[pid] = rel
            headers_by_id[pid] = block.split("\n")[0].strip()

            sev = tags[0].split(":")[0].strip() if tags else ""
            if sev not in shape["severity"]:
                fail(rel, f"{pid}: illegal severity {sev!r}")
            if sev == "SOFT":
                soft_ids.add(pid)

            ai = [t for t in tags if t.startswith("AI:")]
            stab = [t for t in tags if t == "kern" or re.fullmatch(r"\d{4}-\d{2}", t)]

            if sev != "NEVER":
                if not ai:
                    fail(rel, f"{pid}: missing AI: tag")
                if not stab:
                    fail(rel, f"{pid}: missing stability tag")
                for field in shape["required_fields_non_never"]:
                    if field not in block:
                        fail(rel, f"{pid}: missing '{field}' field")
            if ai:
                val = ai[0][3:]
                est = val.endswith("?")
                base = val.rstrip("?")
                if base not in shape["evidence"]:
                    fail(rel, f"{pid}: illegal evidence {base!r}")
                if sev == "SOFT" and not est and pid not in cfg["measured_patterns"]:
                    fail(rel, f"{pid}: SOFT pattern claims measured evidence "
                              f"but is not in measured_patterns")
            for field in shape["required_fields"]:
                if f"{field}:" not in block:
                    fail(rel, f"{pid}: missing '{field}' line")
            if "Klaszter-felülírás" in block:
                overrides_found.add(pid)

        srcs = len(re.findall(rf"^{shape['required_fields'][0]}:", text, flags=re.M))
        if headers != srcs:
            fail(rel, f"{headers} pattern headers but {srcs} "
                      f"'{shape['required_fields'][0]}' lines")

    # cluster overrides: declared == found
    declared = set(cfg["cluster_overrides"])
    if declared != overrides_found:
        fail(name, f"cluster overrides declared {sorted(declared)} "
                   f"but found {sorted(overrides_found)}")

    # every referenced pattern id must exist
    for rel, text in all_text.items():
        for pid in set(re.findall(r"\bHU-[A-Z]\d{2}\b", text)):
            if pid not in seen:
                fail(rel, f"reference to undefined pattern {pid}")

    # single-source constants: reference files must not restate the gate
    restatements = [
        (r"`eros`\s*=\s*2", "cluster point values"),
        (r"pontösszegnek el kell érnie", "cluster threshold"),
        (r"klaszterküszöb 3 helyett 4", "moderate threshold"),
        (r"^\| `informal`", "pass matrix"),
        (r"bekezdésenként legfeljebb \*\*2\*\*", "per-paragraph budget"),
        (r"legfeljebb 40%|40%-a?\b.*mondat", "text-level budget"),
    ]
    for rel, text in all_text.items():
        if rel.endswith("SKILL.md") or rel.endswith(cfg["pass_matrix_file"]):
            continue
        for pat, what in restatements:
            if re.search(pat, text, flags=re.M):
                fail(rel, f"restates {what} — it belongs in SKILL.md / "
                          f"{cfg['pass_matrix_file']} only")

    # SKILL.md invariants
    sm = all_text[str(skill_md.relative_to(ROOT))]
    audit_sec = re.search(r"^## Önellenőrzés\n(.*?)(?=^## )", sm, flags=re.M | re.S)
    n_audit = len(re.findall(r"^\d+\. \*\*", audit_sec.group(1), flags=re.M)) if audit_sec else 0
    if n_audit != cfg["audit_questions"]:
        fail("SKILL.md", f"constants say {cfg['audit_questions']} audit questions, "
                         f"found {n_audit} numbered items")
    if not re.search(r"^\s*method:\s*1\s*$", sm, flags=re.M):
        fail("SKILL.md", "frontmatter must declare 'method: 1'")
    # The suspect list's reason codes are a closed vocabulary, and the order is the resolution
    # rule rather than presentation — so the prose table must be the enum, in the enum's order.
    codetable = re.search(r"^\| kód \| mikor \|\n\|[-| ]+\|\n((?:\|.*\n)+)", sm, flags=re.M)
    codes = re.findall(r"^\| `([a-z-]+)` \|", codetable.group(1), flags=re.M) if codetable else []
    if codes != shape["suspect_reasons"]:
        fail("SKILL.md", f"suspect reason codes {codes} do not match the constants "
                         f"{shape['suspect_reasons']} (the order is the resolution rule)")
    if "Nyelvi kapu" not in sm:
        fail("SKILL.md", "missing language-guard section")
    found = re.findall(r"^\*\*Pass ([−-]?\d+) [—–-]", sm, flags=re.M)
    passes = sorted({int(p.replace("−", "-")) for p in found})
    if passes != sorted(cfg["passes"]):
        fail("SKILL.md", f"constants declare passes {sorted(cfg['passes'])} "
                         f"but the workflow defines {passes}")
    n_lines = len(sm.split("\n"))
    if n_lines > 500:
        fail("SKILL.md", f"{n_lines} lines exceeds the 500-line portability budget")

    # relative links resolve
    for rel, text in all_text.items():
        base = (ROOT / rel).parent
        for target in re.findall(r"\]\((?!https?:)([^)#]+)\)", text):
            if not (base / target).exists():
                fail(rel, f"broken link: {target}")

    for rel, text in all_text.items():
        check_quote_glyphs(rel, text, skill=True, hungarian=True)

    # SKILL.md prints three pattern headers as illustrations. They are not definitions — the
    # checker skips them above — but a stale illustration teaches the wrong tag set, which is the
    # HU-T01 defect shape. So each one must match its real header byte for byte.
    for line in sm.split("\n"):
        m = HEADER.match(line)
        if not m:
            continue
        pid = m["id"]
        real = headers_by_id.get(pid)
        if real is None:
            fail("SKILL.md", f"illustrative header cites undefined pattern {pid}")
        elif real != line.strip():
            fail("SKILL.md", f"illustrative header for {pid} does not match its definition\n"
                             f"      printed:    {line.strip()}\n"
                             f"      defined as: {real}")

    print(f"  {name}: {len(seen)} patterns "
          f"({len(soft_ids)} SOFT), {len(overrides_found)} cluster overrides")
    return set(seen), soft_ids


def check_repo_surface(known_ids):
    """Outside skills/: link integrity, quote glyphs, and pattern IDs that resolve.

    The README claims all three across the whole repository, and the round 2 audit found the
    flagship quote defect sitting in the README's own Hungarian example — the one place the
    skill-only scan could never reach.
    """
    files = (sorted(ROOT.glob("*.md")) + sorted(ROOT.glob("docs/**/*.md"))
             + sorted(ROOT.glob("tests/**/*.md")) + sorted(ROOT.glob("tests/**/*.yml")))
    for f in files:
        rel = f.relative_to(ROOT)
        text = f.read_text(encoding="utf-8")
        for target in re.findall(r"\]\((?!https?:)([^)#]+)\)", text):
            if not (f.parent / target).exists():
                fail(rel, f"broken link: {target}")
        # tests/ is data, not prose: the corpus specimens are the measured inputs and must stay
        # byte-identical to what was run, defects included, and the fixture notes quote the defect
        # in order to assert against it. The gate belongs on the repository's own prose.
        #
        # A *.hu.md file is Hungarian prose, so the em dash gate applies to it as well — the same
        # rule the catalogue enforces on itself. The English surface keeps English typography.
        if f.suffix == ".md" and not str(rel).startswith("tests/"):
            check_quote_glyphs(rel, text, skill=False, hungarian=".hu." in f.name)
        for pid in sorted(set(re.findall(r"\bHU-[A-Z]\d{2}\b", text))):
            # HU-X99 is CONTRIBUTING.md's template placeholder for a new pattern header.
            if pid not in known_ids and pid != "HU-X99":
                fail(rel, f"reference to undefined pattern {pid}")


COUNT_CLAIMS = [
    # (regex with one numeric group, which count it must equal)
    (r"(\d+) `SOFT` mintája", "soft"),
    (r"(\d+) stilisztikai minta", "soft"),
    # \s+ not a space: the README wraps "All 47 soft / patterns carry ...".
    # "N soft patterns" only — "2 soft edits" is the per-paragraph budget, a different number.
    (r"(\d+) soft\s+patterns?\b", "soft"),
    (r"\*\*Hungarian\*\* \((\d+) patterns\)", "total"),
    (r"\| Hungarian \| (\d+) \|", "total"),
    (r"The (\d+) patterns are not equally measurable", "total"),
]


def check_counts(total, soft):
    """Prose restatements of the catalogue size must match the catalogue.

    Adding one pattern invalidates every place that prints a count, and nothing here noticed:
    six restatements of "46 soft" survived a pattern being added, across the README, its
    Hungarian mirror, SKILL.md, sources.md and the round 3 protocol. That is the same shape as
    the quote-glyph defect — a printed number contradicting the thing it describes — so it gets
    the same treatment.

    docs/validation.md is exempt. Its numbers are historical: they record what a round measured
    at the time, and a validation record edited to match the current code is not a record.
    """
    want = {"total": total, "soft": soft}
    files = (sorted(ROOT.glob("*.md")) + sorted(ROOT.glob("docs/**/*.md"))
             + sorted(ROOT.glob("skills/*/SKILL.md"))
             + sorted(ROOT.glob("skills/*/references/*.md")))
    for f in files:
        rel = f.relative_to(ROOT)
        if str(rel) == "docs/validation.md":
            continue
        text = f.read_text(encoding="utf-8")
        for pattern, kind in COUNT_CLAIMS:
            for found in re.findall(pattern, text):
                if int(found) != want[kind]:
                    fail(rel, f"stale {kind} count: prose says {found}, "
                              f"catalogue has {want[kind]} (matched /{pattern}/)")


def main():
    cfgfile = ROOT / "method" / "constants.yml"
    data = load_yaml(cfgfile)
    shape = data["shape"]
    print(f"stet check — method version {data['version']}")
    known_ids, soft_ids = set(), set()
    for skill_name, cfg in data["skills"].items():
        ids, softs = check_skill(ROOT / "skills" / skill_name, cfg, shape)
        known_ids |= ids
        soft_ids |= softs
    check_repo_surface(known_ids)
    check_counts(len(known_ids), len(soft_ids))

    if FAIL:
        print(f"\n{len(FAIL)} problem(s):\n")
        for f in FAIL:
            print(f"  ✗ {f}")
        sys.exit(1)
    print("\nOK")


if __name__ == "__main__":
    main()
