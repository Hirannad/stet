# Changelog

All notable changes to this plugin. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/);
versions follow semver as far as a prose catalogue allows: a behaviour change in what the
skill may edit is a minor bump, wording and documentation are patches.

## [0.3.0] - 2026-08-18

### Changed

- HU-F01 (nominalisation and possessive chains), the largest pattern in the catalogue, now
  **marks instead of editing**. Verbalising an agentless nominal necessarily invents a person
  and a focus the source never marked, so the edit gate is permanently shut for it.
- Run output now has a fixed, machine-parseable shape: five numbered sections, a closed
  11-code vocabulary for declined edits, and a cluster-point section that
  `scripts/parse_run.py` recomputes from the catalogue.
- The catalogue gained HU-T16 (English-language heading left in Hungarian text).

### Added

- `README.hu.md` — a Hungarian README written for a different reader, not a translation.
- `scripts/parse_run.py`, `scripts/check_fixtures.py` and `scripts/plugin_cache.py`, with
  `make runs`, `make fixtures` and `make cache`; nine recorded corpus runs across three
  model families and three registers.
- `docs/round-3-protocol.md` (pre-registered before measurement) and `docs/programme.md`
  (what the project is, and what 1.0 waits on).
- `CLAUDE.md` project instructions, and this changelog.

### Fixed

- The marketplace description claimed 118 patterns while the catalogue defines 119.
- The repo-wide quote and dash gates now cover every markdown file, after the catalogue
  twice printed the very forms it bans.

## [0.2.0] - 2026-08-14

Initial public release: one skill (`stet-hungarian`) with 118 patterns behind a suppression
list, register profiles, a cluster gate and an edit budget; `method/constants.yml` as the
normative constants file with `scripts/check.py` asserting the prose agrees; validation
rounds 1 and 2 recorded in `docs/validation.md`.

[0.3.0]: https://github.com/Hirannad/stet/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/Hirannad/stet/releases/tag/v0.2.0
