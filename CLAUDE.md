# stet — project instructions

A prose linter for machine-written text, shipped as a Claude Code plugin. One skill
(`skills/stet-hungarian/`), no commands, no agents, no hooks, no MCP. Everything else in
the repo is build-time machinery around that one skill.

## Authority chain

- `method/constants.yml` is normative. `METHOD.md` explains the reasoning and loses any
  disagreement. Never restate a constant or a count in prose — link to the source instead;
  `scripts/check.py` asserts that prose and constants agree.

## The one command

- Run `make check` before every commit. It gates every `*.md` under root, `docs/`, `skills/`
  and `tests/` (quote glyphs, link integrity, pattern-ID resolution, count restatements),
  runs as the pre-commit hook (`.githooks/`, armed via `make hooks`) and in CI.
- Other targets (`runs`, `fixtures`, `cache`) are documented in the `Makefile` itself.

## Release discipline — the silent no-op trap

- The installed plugin cache is keyed by the **version string**, not the commit. Any change
  to skill content must bump the version in all three places — `.claude-plugin/plugin.json`,
  `.claude-plugin/marketplace.json`, `skills/stet-hungarian/SKILL.md` (`metadata.version`) —
  and get a git tag before push. Without the bump, `plugin update` succeeds and changes
  nothing, silently.
- The Skill tool reads the **installed** plugin, not this working copy. `make cache` tells
  you which copy a recorded run actually read. Never assume a live test exercised your edit.

## Content invariants

- Every example sentence in the catalogue is invented. Never translate or quote real text
  into an example (CC BY-SA boundary — see `NOTICE.md`).
- Validation records in `docs/validation.md` are frozen. Never edit a closed round to match
  the current code; new findings get their own section.
- The repo surface is English; skill content is Hungarian. `*.hu.md` files are gated as
  Hungarian prose (stricter typography rules apply to them).

## Where state lives

Volatile facts do not live in this file. What the project is and the 1.0 gate:
[docs/programme.md](docs/programme.md). Rejected rules:
[docs/design-rationale.md](docs/design-rationale.md). On the owner's machine there are
three untracked, gitignored Hungarian working documents — `docs/STATE.md` (current
assessment), `docs/DECISIONS.md` (decision log), `docs/GAPS.md` (publishing gaps) — read
them if present; a fresh clone will not have them.

## Traps for a fresh session

- Any `.md` you add is inside the `make check` gate set: close every Hungarian `„` with `”`,
  make every relative link resolve, only mention pattern IDs that exist (`HU-X99` is the
  one allowed placeholder), and restate catalogue counts either in a gated phrasing with
  the current number or not at all.
- In Hungarian prose, use the spaced en dash, never the em dash — the catalogue bans it,
  and the gate enforces this in `*.hu.md` files.
- `docs/STATE.md`, `docs/DECISIONS.md` and `docs/GAPS.md` are local-only working documents
  (untracked by owner decision, 2026-08-18). Do not `git add -f` them, and do not link to
  them from tracked files — the CI link gate would fail on a fresh clone.
