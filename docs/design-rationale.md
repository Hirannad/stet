# Design rationale — what was rejected, and why

A catalogue is defined as much by what it refuses to flag as by what it flags. This file records
the refusals, so a later review does not start from scratch and re-adopt a rule that was already
considered and dropped.

## Rules from English prose practice that we did not adopt

Two MIT-licensed English tools cover the same ground and were read while this catalogue was built:
`blader/humanizer` and `hardikpandya/stop-slop` (see `NOTICE.md`). Most of what they flag was
already covered here or is inapplicable.

Seven rules were rejected deliberately. **They are stated below as the rule we considered and
rejected, not as a quotation of either project.** Some are sharper than what those projects
actually say, some are composites of the two, and both are living repositories that have moved
since. Where the distinction matters, it is noted in the row. If you want to know what either
project prescribes, read it — do not read this table as a summary of it.

| Rule as we considered it | Why not |
|---|---|
| Active voice required — every sentence needs a human subject | Head-on collision with `HU-B06`: forbidding inanimate subjects is a Hungarian prescriptive myth. A "false agency" category would flag correct Hungarian sentences by the thousand (*a tanulmány kimutatja*, *döntés született*). **Note:** `humanizer`'s own rule is conditional — rewrite the passive *when* it makes the sentence clearer — which is defensible in English. It is the absolute form that breaks Hungarian, and the absolute form is what we rejected. |
| Ban all adverbs | An English `-ly` heuristic. Hungarian adverbs carry aspect and meaning; deleting them mechanically violates `HU-B14`/`HU-B15`. |
| Ban the em dash outright | Inverted here: the spaced en dash is the *correct* Hungarian form, and only the em dash is wrong. See `HU-T02`. This is the clearest inversion of the set, and it is genuinely prescribed in English practice. |
| Ban sentences opening with a wh-question | English-specific. The Hungarian equivalent — SEO question subheadings — is handled more narrowly by `HU-M09`. |
| Never use a list of three; use two or one | More dogmatic than anything the sources actually say — `humanizer` flags *overuse*, not the triple as such, and that is the more careful position. We rejected the strong form and kept the same conclusion: a triple is not on its own a machine tell (`HU-R03`). |
| Delete "lazy extremes" — *always*, *never*, *everyone* | Risks violating the quantifier invariant. Deleting *mindig* changes the meaning of the sentence. At most this belongs to the hedging cluster (`HU-L07`). |
| A 50-point numeric rubric across five dimensions | Pseudo-measurement: a score looks like data when it is a judgement. The falsifiable yes/no audit stays. The one dimension we were missing — *is anything cuttable?* — was adopted as a question, not a number (audit item 7). |

One convergence worth naming, because it is evidence rather than influence: `humanizer` independently
forbids synonym cycling — "elegant variation" — which is exactly what `HU-B13` forbids. Two
catalogues built separately reaching the same conclusion is the strongest support either has, and it
is worth more than a borrowed rule.

Six ideas **were** adopted, restated in our own terms with our own examples: the aphorism formula
and its quotability test (`HU-L14`); the empty-declarative form of `HU-R11`; the
responsibility-hiding sub-clause of `HU-H03`, narrowed to flag-only because `HU-B06` protects the
inanimate subject; the quick-test table in `SKILL.md`; the density question in the self-audit; and
the worked-example file.

## Rules we removed from our own catalogue

Four patterns were dropped or softened because the cited source did not support them — in one case
it argued the opposite. These are listed in `skills/stet-hungarian/references/sources.md`. The
general lesson is recorded in `CONTRIBUTING.md`: read the source, do not cite its title.

A larger finding from the same review: a first pass at the suppression list produced 45 entries
**with before/after example pairs**. That would have taught the transformation backwards — given a
pair, the tool starts producing the stigmatised forms it was supposed to leave alone. The
suppression file therefore has no example pairs at all, by design.

## Why the machinery is not novel, and why that is fine

The architecture is a re-derivation of linter design, and it is worth saying so plainly rather
than presenting it as invention:

| here | the established equivalent |
|---|---|
| severity levels | `error` / `warning` / `off` |
| evidence strength with an estimate marker | static-analysis confidence ranks |
| the suppression list | `nolint` / `eslint-disable` |
| the cluster gate | a firing threshold |
| register profiles | a checker's strictness mode |
| the edit budget | an autofix cap |

The consequence is practical, not deflating: the vocabulary is borrowed rather than invented, so
an English-speaking reader already knows what these mean, and a future config format has an
obvious shape to follow. What is genuinely specific here is the *content* — a Hungarian pattern
catalogue with a suppression list built from the prescriptive tradition — and the insistence that
over-correction is the primary failure mode rather than an edge case.
