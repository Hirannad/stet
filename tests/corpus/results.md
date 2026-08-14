# Round 2 — raw counts

Every number the round 2 write-up rests on. Method and interpretation:
[`../../docs/validation.md`](../../docs/validation.md). The specimens are in this directory and the
generation prompt is in [`prompt.md`](prompt.md), so this table is re-derivable rather than
asserted.

Each specimen was run twice, in a fresh isolated agent context, review mode, register pinned by the
operator before the run. `FIX` counts `FIX` and `FIX-IF` changes; `SOFT` counts `SOFT` changes;
`suspect` counts entries on the run's "noticed but deliberately did not fix" list.

| specimen | register | FIX ①→② | SOFT ①→② | suspect ①→② |
|---|---|---|---|---|
| `haiku-01-code-review` | informal | 11 → 15 | **0 → 0** | 22 → 20 |
| `haiku-02-devtool` | neutral | 10 → 8 | **4 → 2** | 32 → 20 |
| `haiku-03-onkormanyzat` | formal | 10 → 10 | **6 → 6** | 26 → 18 |
| `sonnet-01-code-review` | informal | 1 → 1 | **0 → 0** | 10 → 8 |
| `sonnet-02-devtool` | neutral | 8 → 8 | **0 → 0** | 11 → 8 |
| `sonnet-03-onkormanyzat` | formal | 3 → 5 | **0 → 0** | 18 → 12 |
| `opus-01-code-review` | informal | 9 → 10 | **0 → 0** | 11 → 9 |
| `opus-02-devtool` | neutral | 9 → 8 | **0 → 0** | 11 → 9 |
| `opus-03-onkormanyzat` | formal | 5 → 6 | **0 → 0** | 8 → 9 |
| **total** | | **66 → 71** | **10 → 8** | **149 → 113** |

## By generating model, both runs summed

| model | FIX | SOFT | suspect |
|---|---|---|---|
| Claude Haiku 4.5 | 64 | **18** | 138 |
| Claude Sonnet 5 | 26 | **0** | 67 |
| Claude Opus 5 | 47 | **0** | 57 |

Twelve runs on Sonnet- and Opus-generated Hungarian produced **zero** `SOFT` edits. All eighteen
came from Haiku, and from only two of its three specimens.

## By register, both runs summed

| register | FIX | SOFT | suspect |
|---|---|---|---|
| `informal` | 47 | 0 | 80 |
| `neutral` | 51 | 6 | 91 |
| `formal` | 39 | 12 | 91 |

`informal` enables every pass at full strength and produced no `SOFT` edits; `formal` switches
Pass 5 off except for three content patterns and produced the most. The register gate is therefore
not what drives the difference — the text is.

## Register-gate check

`HU-L07` must not fire in `formal` (`references/registers.md`, Pass 4 "teljes, HU-L07 nélkül"). It
appears in all three `formal` runs' output. In every case it sits in the run's opening
register declaration or on its suspect list, never in a change table. **No register-gate violation.**

Establishing that took hand inspection: the three-part output's shape varies between runs enough
that a line-range parser cannot reliably separate a change-table row from a suspect entry. Filed as
an issue.

## Model versions

`claude-haiku-4-5-20251001`, `claude-sonnet-5`, `claude-opus-5`. The measuring agent was
`claude-opus-5` for all eighteen runs, held constant so that only the specimen's origin varies.
