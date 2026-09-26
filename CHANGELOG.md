# Changelog

All notable changes to this plugin. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/);
versions follow semver as far as a prose catalogue allows: a behaviour change in what the
skill may edit is a minor bump, wording and documentation are patches. A change to *when* the
skill is invoked — the description's routing surface — is a patch too, unless it also moves what
the skill may edit. 0.3.1 is the first release to test that clause.

## [0.3.2] - 2026-09-26

The catalogue is untouched, and so is when the skill is invoked: this release moves the machinery
and the record around them, which makes it a patch.

### Added

- `make cache` fails unless the installed copy and the marketplace clone both sit on the exact
  commit their version is tagged at, and neither is older than the latest release. `plugin install`
  delivers the clone's HEAD under whatever number it declares, so one version string could name two
  contents on two machines. The failure prints the commands that refresh both.
- `make check` fails on a version that disagrees across its three declaration sites, on a pattern
  count in the manifests that disagrees with the catalogue, and on a home-directory path or a
  credential-shaped string in any tracked file.
- One recorded run through each fixture, on Opus 5, so `make fixtures` compares behaviour and not
  only specifications. All three pass, including `02-clean`, where any edit at all fails.
- `NOTICE.md` states the rule for a measurement corpus of third-party Hungarian: mining under the
  text-and-data-mining exception, no redistribution. `data/raw/` is gitignored.

### Fixed

- `scripts/parse_run.py` raised on a run whose provenance names a copy outside the repository —
  the one case the provenance comment exists to report. It now reports `extern`.
- Two statements in the round 3 protocol's artefact section were false: a `.gitignore` line said to
  be missing that had been added, and a glob narrower than the one `check.py` uses.

## [0.3.1] - 2026-08-21

### Fixed

- The description excluded translation by saying the skill wants Hungarian text, which reads as a
  rule about the *input*. A request to translate into Hungarian has a non-Hungarian input and a
  Hungarian result, and the router took the result: asked to translate a German paragraph into
  Hungarian, the skill fired in three of four measured runs. The exclusion now names the direction
  — a Hungarian result is not a Hungarian source — and says that writing fresh Hungarian is out of
  scope for the same reason. The catalogue is untouched; only the routing surface moved.

  Measured on the installed 0.3.0 copy in 31 headless runs started outside the repository, on
  Opus 5. The same measurement found the five positive prompts firing five out of five when actual
  text accompanies the request; two of them fire only about half the time on the bare prompt, which
  is the prompts referring to absent text rather than a routing defect.

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

[0.3.2]: https://github.com/Hirannad/stet/compare/v0.3.1...v0.3.2
[0.3.1]: https://github.com/Hirannad/stet/compare/v0.3.0...v0.3.1
[0.3.0]: https://github.com/Hirannad/stet/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/Hirannad/stet/releases/tag/v0.2.0
