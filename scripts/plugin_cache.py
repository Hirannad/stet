#!/usr/bin/env python3
"""Which catalogue does a Skill-tool run read — this working copy, or the installed plugin?

No dependencies. Run before anything that measures: `make cache`.

Round 3's format-validation runs reported independently that invoking `stet:stet-hungarian` loads
`~/.claude/plugins/cache/<marketplace>/<plugin>/<version>/`, not this tree, and that the two
catalogues had already diverged. A run driven through the Skill tool therefore measures the
*released* version, silently, and returns plausible round-2-shaped output while doing it — see
docs/validation.md, round 3. The protocol's answer was a sentence telling every phase to state
which copy it ran. A claim that can be turned into a mechanism has to be, so this is it.

Two questions, and they are not the same one:

  1. **Can the two copies disagree at all?** Byte-compare the skill trees. If they are identical,
     provenance is moot: either copy gives the same answer. Exit 1 when they have drifted, so a
     measurement phase can gate on it.

  2. **Which copy did *this* recorded run read?** A run's provenance comment names a source path
     and a content hash; `parse_run.py` checks that hash against the working copy and reports
     `stale` when it does not match. `stale` is one bit, and it conflates two different facts: the
     working copy moved on after the run, or the run read the installed plugin all along. Here the
     declared hash is resolved against **every copy on disk**, so the answer is a named copy.

     Its limit, stated rather than glossed: a hash matching nothing on disk resolves to `unknown`,
     not to a verdict. That is the honest reading — the copy that produced the run is gone, and no
     amount of hashing brings it back.

Usage:
    python3 scripts/plugin_cache.py                        # the copies, and whether they agree
    python3 scripts/plugin_cache.py tests/corpus/runs/*.md  # also resolve each run to a copy

Not wired to CI or to the pre-commit hook: neither has an installed plugin, and this is a fact
about one machine at one moment rather than a property of a commit.
"""
import hashlib
import json
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from check import ROOT  # noqa: E402
from parse_run import PROVENANCE_RE, digest as parser_digest  # noqa: E402

REGISTER = Path.home() / ".claude" / "plugins" / "installed_plugins.json"


def manifest():
    return json.loads((ROOT / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))


def installed(name):
    """Every installed copy of this plugin, from Claude Code's own install register.

    The register is keyed `<plugin>@<marketplace>`, and the path it names is the version-keyed
    cache extract — the copy the Skill tool actually serves. The intermediate marketplace clone
    under `marketplaces/<name>/` is not read at run time, so it is not compared here.
    """
    if not REGISTER.exists():
        return []
    reg = json.loads(REGISTER.read_text(encoding="utf-8")).get("plugins", {})
    return [e for key, entries in reg.items() if key.split("@")[0] == name for e in entries]


def digest(base, path):
    """`parse_run.digest`, but relative to an arbitrary plugin root instead of to this repository.

    The parser hashes each file's path relative to ROOT, which is what makes its digests
    comparable between runs — and what makes them uncomputable for a copy living outside the
    tree. Relativising to the copy's own root instead yields the same string for the same
    content wherever the copy sits, which is the whole point: it lets a hash recorded in a run
    be matched against the installed plugin. `check_agrees` keeps the two functions honest.
    """
    h = hashlib.sha256()
    for f in sorted(Path(path).rglob("*.md")):
        h.update(f.relative_to(base).as_posix().encode() + b"\0" + f.read_bytes())
    return h.hexdigest()


def check_agrees():
    """Two digest functions over the same bytes must never disagree. Loudly, if they ever do."""
    for d in sorted((ROOT / "skills").glob("*")):
        if d.is_dir() and digest(ROOT, d) != parser_digest(d):
            print(f"✗ digest disagrees with parse_run.digest on {d.relative_to(ROOT)} — "
                  f"the two hash the same bytes and must stay identical")
            return False
    return True


def sources(root):
    """`skills/<name>` -> content digest, for every skill a copy ships.

    Keyed by the path a run's provenance comment names, so a declared hash can be looked up.
    """
    root = Path(root)
    return {str(d.relative_to(root)): digest(root, d)
            for d in sorted((root / "skills").glob("*")) if d.is_dir()}


def tree(root):
    """Relative path -> sha256, over every file under skills/.

    Dot-paths and `__pycache__` are skipped: they are gitignored, so they exist in a working copy
    and never in an extract, and a stray `.DS_Store` reported as drift would train the reader to
    ignore this check.
    """
    root = Path(root)
    out = {}
    for f in sorted((root / "skills").rglob("*")):
        rel = f.relative_to(root)
        if not f.is_file() or any(p.startswith(".") or p == "__pycache__" for p in rel.parts):
            continue
        out[str(rel)] = hashlib.sha256(f.read_bytes()).hexdigest()
    return out


def commits_behind(sha):
    """How far HEAD is ahead of the commit a copy was installed from. None if git cannot say."""
    try:
        r = subprocess.run(["git", "-C", str(ROOT), "rev-list", "--count", f"{sha}..HEAD"],
                           capture_output=True, text=True, timeout=10)
        return int(r.stdout.strip()) if r.returncode == 0 else None
    except (OSError, ValueError):
        return None


def report(entry, here, version):
    """Print one installed copy against the working one. Returns 'same', 'drift' or 'missing'."""
    path = Path(entry["installPath"])
    where = f"version {entry.get('version', '?')}, scope {entry.get('scope', '?')}"
    sha = entry.get("gitCommitSha", "")
    if sha:
        n = commits_behind(sha)
        where += f", commit {sha[:7]}"
        if n == 0:
            where += " (the commit HEAD is on)"
        elif n:
            where += f" ({n} commit{'s' if n > 1 else ''} behind HEAD)"

    print(f"\n  installed  {path}")
    print(f"             {where}")
    if not path.exists():
        print("             ✗ the register names a path that is not on disk")
        return "missing"

    there = tree(path)
    differ = sorted(p for p in set(here) & set(there) if here[p] != there[p])
    only_here = sorted(set(here) - set(there))
    only_there = sorted(set(there) - set(here))
    total = len(set(here) | set(there))

    if not (differ or only_here or only_there):
        print(f"             skills/: {total} files, byte-identical")
        return "same"

    print(f"             skills/: {total} files — {len(differ)} differ, "
          f"{len(only_here)} only here, {len(only_there)} only there")
    for p in differ:
        print(f"               ~ {p}")
    for p in only_here:
        print(f"               + {p}")
    for p in only_there:
        print(f"               - {p}")

    # The trap is silent for this reason and no other: the cache path ends in the version, so an
    # unbumped version means a marketplace refresh finds the directory already there.
    if entry.get("version") == version:
        print(f"             ⚠ both copies declare version {version}, and the cache directory is")
        print("               keyed by version — refreshing the marketplace leaves this copy in")
        print("               place. Bump the version, or reinstall the plugin.")
    return "drift"


def resolve(runs, copies):
    """Name the copy each run's declared hash belongs to. `copies` is [(label, {source: sha})]."""
    print(f"\nrecorded runs ({len(runs)}):\n")
    tally, any_unknown = {}, False
    for p in runs:
        prov = PROVENANCE_RE.search(p.read_text(encoding="utf-8"))
        if not prov:
            verdict, why = "no provenance", "cannot say which copy it read"
        else:
            # A short declared hash is a prefix of the full digest, as parse_run.py matches it.
            hit = [label for label, src in copies
                   if src.get(prov["source"], "").startswith(prov["sha"])]
            if not hit:
                verdict, why = "unknown", f"{prov['sha']} matches no copy on disk"
                any_unknown = True
            elif len(hit) > 1:
                verdict, why = "indistinguishable", f"{' and '.join(hit)} are identical here"
            else:
                verdict, why = hit[0], f"{prov['source']} @ {prov['sha']}"
        tally[verdict] = tally.get(verdict, 0) + 1
        print(f"  {p.name:<40} {verdict:<19} {why}".rstrip())

    print("\n  " + ", ".join(f"{n} {k}" for k, n in tally.items()))
    if any_unknown:
        print("  An `unknown` run named a copy that is no longer on disk. It is not evidence about\n"
              "  either catalogue until the named hash can be produced again.")


def main(argv):
    if not check_agrees():
        return 2
    m = manifest()
    runs = [Path(a) for a in argv]
    print(f"stet plugin cache — {m['name']} {m['version']}, working copy {ROOT}")

    entries = installed(m["name"])
    copies = [("working copy", sources(ROOT))]
    states = set()
    if not entries:
        print(f"\n  installed  nothing: no {m['name']}@… entry in {REGISTER}")
    else:
        here = tree(ROOT)
        for e in entries:
            states.add(report(e, here, m["version"]))
            path = Path(e["installPath"])
            if path.exists():
                copies.append((f"installed {e.get('version', '?')}", sources(path)))

    if runs:
        resolve(runs, copies)

    if "drift" in states:
        print("\n✗ the installed catalogue is not this one. A Skill-tool run reads that copy, so\n"
              "  refresh or pin the plugin before measuring, and record which copy ran.")
        return 1
    if "missing" in states:
        print("\n✗ the install register names a copy that is not on disk. Nothing can be said about\n"
              "  what a Skill-tool run would read until the register and the disk agree.")
        return 1
    if not entries:
        print("\nOK — no installed copy can shadow the working one")
    else:
        print("\nOK — the copies are byte-identical, so which one a run read cannot change it")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
