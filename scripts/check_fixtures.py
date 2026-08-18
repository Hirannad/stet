#!/usr/bin/env python3
"""Check the tests/fixtures/ specifications, and compare recorded runs against them. No deps.

The fixtures declare what a run *should* do; `scripts/parse_run.py` reads what a run *did*. This
script is the join. Until it existed the two artefacts sat in the same repository without ever
meeting, which is what the README's last limitation said out loud.

Two arms, and the second one is often idle:

1. **The specifications against the catalogue.** Always runs, needs no recorded run. It catches the
   failure this repository has seen before in another place — a pattern being reclassified while
   the prose that depends on it keeps its old numbers. A fixture that declares `expect_no_soft` and
   then names a `SOFT` pattern is asking for two incompatible things.
2. **A recorded run against its fixture.** Runs when `tests/fixtures/runs/` has something in it.
   When it does not, the summary says so rather than printing a bare OK: an arm that cannot fire
   must not read the same as an arm that fired and found nothing.

The shape of a run, its reason codes and its cluster arithmetic are `parse_run.py`'s business and
are simply forwarded here. Two further requirements are this script's own, and both come from
somewhere the repository has already been bitten. A fixture run carries the same provenance
comment a corpus run does, because the Skill tool serves the installed plugin rather than the
working tree. And `expect_max_cluster_points` turns a claim two of the fixtures already made in
prose — *every paragraph should score 0* — into something section 4 can be held to.

One judgment call, made here rather than buried. The fixtures count **occurrences in the input**
(`8GB`, `4GB`, `21°C` is three). The output shape counts **rows**, and SKILL.md defines a row as one
pattern in one sentence, so those three merge into one row. The units are not the same and no
parser can convert between them. What is sound in both directions is the bound:

    1 <= rows citing a pattern <= its declared occurrences

A sentence with a hit contributes at least one occurrence, so rows can merge but never multiply.
Zero rows means the pattern did not fire at all; more rows than occurrences means it fired
somewhere the fixture does not account for. Both are defects; anything between them is a
formatting choice the fixture has no business policing.

What this script does not check: the `expect_noop` entries. Those name a construction and give a
reason in prose, for a reader. A count of them is printed so a green run cannot be mistaken for a
fully verified one.

Usage:
    python3 scripts/check_fixtures.py        # or: make fixtures
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from check import ROOT  # noqa: E402
from parse_run import PROFILES, catalogue, parse  # noqa: E402

FIXTURES = ROOT / "tests" / "fixtures"
RUNS = FIXTURES / "runs"
SUFFIX = "-expected.yml"

KEYS = {"register", "expect_patterns", "expect_change_count", "expect_noop",
        "expect_no_soft", "expect_max_cluster_points", "soft_reason"}
PATTERN_KEYS = {"id", "occurrences", "note", "where"}
WHERE = {"change", "change_or_suspect"}

FAIL = []


def fail(where, msg):
    FAIL.append(f"{where}: {msg}")


# ---------------------------------------------------------------- tiny YAML reader
# The fixture dialect only: nested maps, sequences of maps, folded `>-` scalars, inline `[]`.
# check.py has its own reader for constants.yml, which needs none of the sequence handling.
def load_yaml(path):
    lines = [(len(ln) - len(ln.lstrip()), ln.strip())
             for ln in path.read_text(encoding="utf-8").split("\n")
             if ln.strip() and not ln.lstrip().startswith("#")]
    return block(lines, 0, lines[0][0])[0]


def block(lines, i, indent):
    if lines[i][1].startswith("- "):
        seq = []
        while i < len(lines) and lines[i][0] == indent and lines[i][1].startswith("- "):
            lines[i] = (indent + 2, lines[i][1][2:])  # the item's first key, re-indented
            item, i = block(lines, i, indent + 2)
            seq.append(item)
        return seq, i
    out = {}
    while i < len(lines) and lines[i][0] == indent:
        key, _, rest = lines[i][1].partition(":")  # first colon only; values contain colons
        rest, i = rest.strip(), i + 1
        if rest == "":
            out[key], i = block(lines, i, lines[i][0])
        elif rest in (">-", ">"):
            buf = []
            while i < len(lines) and lines[i][0] > indent:
                buf.append(lines[i][1])
                i += 1
            out[key] = " ".join(buf)
        else:
            out[key] = scalar(rest)
    return out, i


def scalar(v):
    if v == "[]":
        return []
    if v in ("true", "false"):
        return v == "true"
    if len(v) > 1 and v[0] == v[-1] and v[0] in "\"'":
        return v[1:-1]
    try:
        return int(v)
    except ValueError:
        return v


# ---------------------------------------------------------------- arm 1: the specification
def check_spec(name, spec, cat):
    where = name + SUFFIX
    unknown = sorted(set(spec) - KEYS)
    if unknown:
        fail(where, f"unknown key(s) {unknown}")
    if not (FIXTURES / f"{name}-input.md").exists():
        fail(where, f"no matching {name}-input.md")
    if spec.get("register") not in PROFILES:
        fail(where, f"register {spec.get('register')!r} is not one of {PROFILES}")
    cap = spec.get("expect_max_cluster_points")
    if cap is not None and (not isinstance(cap, int) or cap < 0):
        fail(where, f"expect_max_cluster_points must be a non-negative integer, got {cap!r}")

    patterns = spec.get("expect_patterns", [])
    for p in patterns:
        pid = p.get("id")
        unknown = sorted(set(p) - PATTERN_KEYS)
        if unknown:
            fail(where, f"{pid}: unknown key(s) {unknown}")
        if pid not in cat:
            fail(where, f"{pid}: no such pattern in the catalogue")
            continue
        n = p.get("occurrences")
        if not isinstance(n, int) or n < 1:
            fail(where, f"{pid}: occurrences must be a positive integer, got {n!r}")
        if p.get("where", "change") not in WHERE:
            fail(where, f"{pid}: where must be one of {sorted(WHERE)}, got {p.get('where')!r}")
        # The gate this arm exists for: a reclassified pattern silently invalidating a fixture.
        if spec.get("expect_no_soft") and cat[pid]["severity"] == "SOFT":
            fail(where, f"{pid} is SOFT in the catalogue, but this fixture also declares "
                        f"expect_no_soft — the two cannot both hold")
    if spec.get("expect_change_count") == 0 and patterns:
        fail(where, "expect_change_count: 0 with a non-empty expect_patterns")


# ---------------------------------------------------------------- arm 2: a run against it
def check_run(name, spec, path, cat):
    where = path.name
    run = parse(path.read_text(encoding="utf-8"), cat)
    for problem in run["problems"]:
        fail(where, problem)  # the shape gate `make runs` applies to the corpus

    # The same recording contract the corpus runs carry, for the same reason: a run that cannot
    # say which skill copy produced it is not evidence about either copy.
    if run["provenance"] is None:
        fail(where, "no provenance comment: a recorded run must name the skill copy that "
                    "produced it")

    if run["register"] != spec.get("register"):
        fail(where, f"ran as {run['register']!r}, the fixture pins {spec.get('register')!r}")

    cap = spec.get("expect_max_cluster_points")
    if cap is not None:
        for c in run["clusters"]:
            if c["points"] > cap:
                fail(where, f"paragraph {c['n']} scored {c['points']} cluster points, the "
                            f"fixture caps it at {cap}: {', '.join(c['ids'])}")

    rows = {}
    for change in run["changes"]:
        for pid in change["ids"]:
            rows[pid] = rows.get(pid, 0) + 1
    on_suspect_list = {pid for s in run["suspects"] for pid in s["ids"]}
    declared = {p["id"]: p for p in spec.get("expect_patterns", []) if "id" in p}

    if "expect_change_count" in spec and len(run["changes"]) != spec["expect_change_count"]:
        fail(where, f"{len(run['changes'])} change row(s), the fixture expects "
                    f"{spec['expect_change_count']}")
    if spec.get("expect_no_soft"):
        for change in run["changes"]:
            if change["kind"] == "SOFT":
                fail(where, f"SOFT edit where the fixture forbids every one: "
                            f"{','.join(change['ids'])} on {change['original']!r}")

    for pid, p in declared.items():
        n = rows.get(pid, 0)
        if n == 0:
            if p.get("where") == "change_or_suspect":
                if pid not in on_suspect_list:
                    fail(where, f"{pid} appears in neither the change table nor the suspect "
                                f"list; the fixture accepts either, and silence is the one "
                                f"answer it does not accept")
            else:
                fail(where, f"{pid} expected but never cited in the change table")
        elif n > p.get("occurrences", 0):
            fail(where, f"{pid}: {n} change rows for {p['occurrences']} occurrence(s) in the "
                        f"input — a row is one pattern in one sentence, so rows may merge but "
                        f"never outnumber the hits")

    for pid in sorted(rows):
        if pid not in declared:
            fail(where, f"{pid} fired, the fixture does not declare it — either the catalogue "
                        f"or the expectation is wrong, and telling which apart is the finding")
    return run


def main():
    cat = catalogue()
    specs = sorted(FIXTURES.glob("*" + SUFFIX))
    if not specs:
        print(f"no fixtures in {FIXTURES.relative_to(ROOT)}/")
        return 1

    print(f"stet fixtures — {len(specs)} specification(s)\n")
    matched, noop_total, runs_total = set(), 0, 0
    for f in specs:
        name = f.name[: -len(SUFFIX)]
        spec = load_yaml(f)
        check_spec(name, spec, cat)
        runs = sorted(RUNS.glob(f"{name}-*.md")) if RUNS.exists() else []
        for run in runs:
            check_run(name, spec, run, cat)
        matched.update(runs)
        noop_total += len(spec.get("expect_noop", []))
        runs_total += len(runs)
        print(f"  {name:<16} {len(spec.get('expect_patterns', [])):>2} pattern(s), "
              f"{len(spec.get('expect_noop', [])):>2} noop note(s)   "
              f"{', '.join(r.name for r in runs) if runs else '— no recorded run'}")

    for stray in sorted(set(RUNS.glob('*.md')) - matched) if RUNS.exists() else []:
        fail(stray.name, "no fixture of that name; a run file is named <fixture>-<label>.md")

    if runs_total:
        print(f"\n{runs_total} run(s) compared.")
    else:
        print(f"\nNothing was compared: {RUNS.relative_to(ROOT)}/ is empty, so only the "
              f"specifications were checked.\nRecording a run is a manual step — "
              f"tests/README.md says how.")
    print(f"{noop_total} 'noticed but deliberately did not fix' notes are prose for a reader. "
          f"Nothing here checks them.")

    if FAIL:
        print(f"\n{len(FAIL)} problem(s):\n")
        for f in FAIL:
            print(f"  ✗ {f}")
        return 1
    print("\nOK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
