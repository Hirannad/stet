---
title: Round 3 protocol — four-arm corpus measurement
type: spec
status: draft
updated: 2026-08-15
---

# Round 3 protocol — four-arm corpus measurement

Pre-registered. Written before any measurement was taken, so that the analysis decisions in
[§7](#7-pre-registered-analysis-decisions) cannot be chosen after seeing the numbers. Where the
executed round departs from this document, [validation.md](validation.md) records the departure
and the reason.

Rounds 1 and 2 are in [validation.md](validation.md). This one exists because of a gap both of
them state about themselves.

---

## 1. The missing arm

An `AI:` value asserts a **rate difference**: this form appears more often in machine-written
Hungarian than in human-written Hungarian.

Round 2 measured one side of that. Eighteen runs over nine machine-generated specimens established
how often the catalogue fires on machine Hungarian. There is no corresponding measurement on human
Hungarian — not in round 2, and not in round 1, whose "negative fixture" was part of one company's
playbook, unpublishable and partly written by the rater.

**A difference cannot be measured from one arm.** That is the whole reason
`measured_patterns` in [method/constants.yml](../method/constants.yml) is empty and every one of
the 47 soft patterns carries the estimate marker. The constants file says as much in its own
comment: the catalogue has citable linguistic sources, "but not one citable measurement of how
often a language model produces a given form."

This round builds the other arm.

### What this is not

It is tempting to read "sample good Hungarian writing" as an instruction to put exemplar sentences
into the catalogue. That would be wrong here, and three of this repository's own rules say so:

- [CONTRIBUTING.md](../CONTRIBUTING.md) — "Every example sentence must be invented. Do not copy,
  and do not translate, an example from a source."
- The density brake in [SKILL.md](../skills/stet-hungarian/SKILL.md) forbids inserting idiom or
  discourse particle where there was none. Style exemplars push in exactly that direction.
- [NOTICE.md](../NOTICE.md) has no provision for verbatim third-party text, and the licence story
  depends on it not acquiring one carelessly.

The corpus's role in this round is **evidence, not exemplar**. Nothing from it is quoted into a
pattern.

### One claim in the README that this protocol contradicts

[README.md](../README.md) currently says calibrating the cluster gate "needs seeded inputs, not
real text." That is half right and the half that is wrong matters.

Seeded inputs test **mechanics**: does the gate fire when a cluster is constructed? They cannot
**calibrate**, because the density of the seeded cluster is chosen by someone who already believes
3 is the right threshold. The reasoning is circular. Where the cut belongs is a question about the
distribution of paragraph scores in each arm, and only two arms of real text can answer it.

Seeded inputs and this round are complementary, not alternatives. The README sentence will be
corrected whether or not the rest of this round succeeds.

---

## 2. The central prediction

The catalogue states its own first premise in [SKILL.md](../skills/stet-hungarian/SKILL.md): the
model produces Hungarian from a latent English representation, so the sentence structure stays
English even when nothing was translated — and this is called the *louder* of the two signal
sources.

That premise makes a sharp, falsifiable prediction:

> **On the Pass 2 (translationese) features, LLM-generated Hungarian sits closer to translated
> Hungarian than to originally-composed Hungarian.**

If it holds, Pass 2 aims correctly and the translationese metric is the natural basis for the
`AI:` values. If it fails, the signal source the catalogue calls loudest is mis-aimed, and the
consequences reach every pattern in `02-translationese.md`.

**No round has tested it.** Round 2's own limitations section records that it had "no genuinely
translated source," and round 1 had none either. The loudest claimed signal is the least tested
thing in the repository. Testing it requires arms that neither previous round had, which is why
this round has four.

---

## 3. Corpus design

### 3.1 The four arms

| arm | content | what it isolates |
|---|---|---|
| **A1** | originally-composed human Hungarian | baseline; false-positive rate; what the norms look like in practice |
| **A2** | human-translated Hungarian (from English) | translationese without any machine involvement |
| **A3** | machine-translated Hungarian (from English) | translationese produced by a machine, without LLM rhetoric |
| **A4** | LLM-generated Hungarian (not a translation) | the target of measurement |

A3 exists to separate the two signal sources the catalogue claims are independent. If A3 shows the
Pass 2 signal but not the Pass 4 signal, that independence is demonstrated rather than asserted.

### 3.2 Stratification, and why it is the crux

Newspaper prose covers the `neutral` and `formal` profiles. It does not cover documentation,
product copy, contracts, or chat. Measure `-ásra kerül` (HU-H02) against a journalism-only baseline
and it looks like a machine tell — when in fact it is merely rare *in journalism* and normal in
administrative Hungarian. The register difference would be confounded with the human/machine
difference, and every officialese pattern would be systematically overstated.

**Every arm is stratified by register, and every comparison is made within a stratum. Pooled
comparisons are not reported.** The four profiles are defined in
[registers.md](../skills/stet-hungarian/references/registers.md), which is also the source for the
genre-to-profile mapping.

| profile | A1 | A2 | A3 / A4 |
|---|---|---|---|
| `informal` | MNSZ2 `személyes`; curated Hungarian blogs, esports and new-media writing | — | seeded continuation from the same stratum |
| `neutral` | MNSZ2 `sajtó` (news, reportage); MEK non-fiction | MEK public-domain literary translation | as above |
| `formal` | MNSZ2 `tudományos`; press commentary and analysis | EUR-Lex / DGT Hungarian (human-translated) | as above |
| `legal` | MNSZ2 `hivatalos`; njt.hu | EUR-Lex Hungarian legal | as above |

The Hungarian National Corpus (MNSZ2, `mnsz.nytud.hu`) is the backbone of A1. Its five style
subcorpora — `sajtó`, `szépirodalom`, `tudományos`, `hivatalos`, `személyes` — map almost
one-to-one onto this catalogue's four profiles. Roughly 1.5 billion words, CQL query support,
`doc.style` / `doc.type` / `doc.column` metadata, exportable frequency lists, free registration,
no bulk download. Tier A measurement against it is therefore a **documented, batched sequence of
manual queries**, not scraping. Every query string is published so the counts are re-derivable.

### 3.3 Contamination, and the cutoff the catalogue already defines

`references/06-rhythm.md` already names the boundary, in its list of features to preserve: text
written before 30 November 2022, the public launch of ChatGPT, cannot carry AI-origin signals even
in principle.

So the control stratum does not need inventing. **The primary A1 baseline is drawn exclusively
from material published before 2022-11-30.** MNSZ2 (v2.0.5, 2018) and Hungarian Webcorpus 2.0
satisfy this by construction.

This creates a real tension with contemporary informal Hungarian — slang, esports writing, current
new-media prose — which is a live register the `informal` profile targets and which MNSZ2's 2018
close does not reach. Resolution, in order of preference:

1. Where the outlet has a pre-2022 archive, sample from it. Hungarian gaming and esports media
   predate 2022. This material is baseline-eligible.
2. Post-2022 informal material is a **separate stratum, `A1-contemporary`, and is never baseline.**
   It serves as a contamination probe: has contemporary human Hungarian drifted toward the machine
   profile? That is a finding in its own right and costs nothing once the pipeline exists.
3. **The two never merge into one baseline.** If they did, contamination would compress the
   measured difference and real tells would present as non-tells. This is the failure mode most
   likely to go unnoticed, because it produces a plausible-looking null result.

### 3.4 Sourcing, licensing, and what ships

Openly-licensed material is preferred everywhere it suffices: MNSZ2 (query results), MEK
public-domain works, Hungarian Webcorpus 2.0, njt.hu, EUR-Lex. Where a source is openly licensed,
the text itself may be committed.

For material that is not, two things are separate and must stay separate:

- **Mining** is permitted. The Hungarian copyright act's general text-and-data-mining exception
  (Szjt. 35/A) covers lawfully accessed content for any purpose, unless the rightsholder has
  reserved rights in machine-readable form. That reservation is checked per outlet, per source,
  before anything is fetched, and the check is recorded in the manifest.
- **Redistribution** is not covered by it. Raw third-party text does not enter this repository.

What ships instead is a **manifest plus derived counts**: URL, outlet, publication date, genre,
word count, SHA-256, and the rights-reservation check. Raw material stays local and gitignored.

This shape has precedent here. `tests/corpus/prompt.md` plus `tests/corpus/results.md` is already
"the recipe and the numbers, so a stranger can re-derive them" — see
[tests/README.md](../tests/README.md). The manifest extends that pattern to material this
repository cannot host. [NOTICE.md](../NOTICE.md) gains a section naming each source and its terms.

The cost is stated rather than glossed: round 2 exists because round 1's corpus could not be
published and its numbers had to be taken on trust. Any part of A1 that ships as manifest-only
carries a weaker reproducibility guarantee than `tests/corpus/` does — a stranger can re-fetch,
but not diff against what we fetched.

### 3.5 Producing A3 and A4

**A4 follows the HAP-E construction** (`browndw/human-ai-parallel-corpus`, MIT). Take a ~500-word
chunk of human text, ask the model to continue it for 500 words, and compare against the *actual*
human continuation. Topic, genre and register are held constant by construction — which is exactly
the confound that a naive "generate on three topics" design fails to control, and which round 2's
corpus did not control.

Round 2's nine specimens are retained and re-measured, but they are no longer the main material.

At least one non-Anthropic model is required. Round 2's own limitations section makes the point:
three Claude models "is not 'language models'; it is three members of one vendor's family at one
point in time."

**A3** is English source text through two machine-translation systems.

Both A3 and A4 are output this repository produces, so both ship in full alongside their prompts,
in the established `tests/corpus/` shape.

---

## 4. Measurement tiers

The 119 patterns are not equally measurable. Across the six pass files (84 patterns):

| tier | count | share | requirement |
|---|---|---|---|
| **A** — decidable by regular expression | 42 | 50% | none; countable in every arm immediately |
| **B** — computable by script | 26 | 31% | sentence splitting, statistics, sometimes morphology |
| **C** — requires judgment | 16 | 19% | sampling plus adjudication |

Plus the 12 `HU-M` patterns in `registers.md` (6 of them soft) and the 23 `HU-B` entries in
`do-not-touch.md`. The latter are prohibitions rather than frequency claims, but they make an
excellent suppression test bed — see [§5.3](#53-phase-2--false-positives-and-calibration).

The distribution is sharply file-dependent. `05-llm-style.md` is 93% tier A, being largely lexical
lists, two of them explicitly closed. `06-rhythm.md` has **no** tier A patterns at all: every
rhythm pattern needs at minimum sentence splitting, and three need semantic judgment.

**Only tier A and validated tier B patterns are eligible for `measured_patterns`.** Tier C gets
sampled adjudication with an inter-rater agreement statistic, and its result stays an observation,
not a measurement. This is stated in advance because
[design-rationale.md](design-rationale.md) already rejected a numeric rubric on the grounds that
"a score looks like data when it is a judgement," and a corpus study is an easy place to reintroduce
that error.

### Two counting traps

**Bare-construction filtering.** Every left-hand cell in
[substitutions.md](../skills/stet-hungarian/references/substitutions.md) is a searchable string —
121 of them — but the file's own preamble sets two preconditions: the construction must be bare (no
preceding article or demonstrative) and the substitution must not change the argument frame. A
naive count of `döntést hoz` overcounts, because it includes determined instances such as
`ezt a döntést`. Without the determiner filter the baseline is inflated, in the direction that makes
patterns look *more* justified.

**Markup-dependent patterns.** HU-R08, HU-M09 and HU-M10 measure markup statistics: heading depth,
in-sentence bold runs, list-to-prose ratio, emoji. Most Hungarian reference corpora strip markup.
These patterns either get a markup-preserving source or they are reported as not measured. They are
not silently omitted.

---

## 5. Phases

Ordering follows the two-half rule established after round 2: a cheap, parallelisable, rater-free
counting half first; the expensive human ballot second, and only on what the first half surfaced.

### 5.1 Phase 0 — prerequisites

**The three-part output must acquire a machine-readable shape.** Round 2's finding 4 records that a
line-range parser could not reliably separate a change-table row from a suspect-list entry, and that
its eighteen runs were counted by hand. Phase 2 requires running the workflow over hundreds of human
texts. Hand counting does not scale to that, so phase 2 does not start until this is done.

- `SKILL.md` `## Kimenet`: fix the heading strings, the heading levels, and the table columns.
- `scripts/parse_run.py`: extract the three parts.

This is already an open issue in the repository, not new scope.

**The installed plugin, not the working copy, is what the Skill tool serves.** Measured, not
assumed: three independent format-validation runs each reported that invoking `stet:stet-hungarian`
loaded `~/.claude/plugins/cache/stet/stet/0.2.0/`, whose `SKILL.md` contains none of the fixed
output shape and whose catalogue lacks patterns that exist in the working copy. A measurement run
driven through the Skill tool therefore measures the *released* version, silently, and returns
plausible round-2-shaped output while doing it.

Every phase that runs the skill must state which copy it ran, and refresh or pin the plugin before
starting. This is the same lesson the `allowed-tools` finding taught in round 2, in a new place:
**a native mechanism is not a mechanism until you have measured it.**

Also in phase 0:

- **Dependency decision.** The repository is stdlib-only today, with no requirements file, and
  `scripts/check.py` hand-rolls a YAML subset parser specifically to stay that way. Tier B needs
  sentence splitting. Recommendation: a hand-written, published, auditable splitter, with its
  failure modes documented — the splitter is part of the result and must be inspectable. The
  alternative, `huspacy`, is more accurate and would be this repository's first dependency.
- `NOTICE.md`: source and licence section.
- `.gitignore`: `data/raw/`.

### 5.2 Phase 1 — counting, no rater

- **1a.** A1 and A2, tier A, via MNSZ2 CQL queries per subcorpus, producing frequency per million.
  Roughly 40 patterns across 5 subcorpora. Every query string published.
- **1b.** Produce and measure A3 and A4. Same counting script, same pattern definitions.
- **1c.** Discrimination per pattern per register: rate in each arm, ratio, confidence interval.
  Power is computed in advance; patterns whose expected counts are too low get **"underpowered"
  reported instead of a number**.
- **1d.** Tier B distributions: sentence length, paragraph length, connective density, demonstrative
  anaphora, concrete-detail density per paragraph.

### 5.3 Phase 2 — false positives and calibration

- **2a. False-positive rate.** Run the full workflow over N human texts per register. On
  professionally edited, pre-2022 human prose, every soft edit is a candidate false positive. No
  rater is needed to count them; adjudication applies only to what fired. Rounds 1 and 2 both state
  this rate is unestablished; this is the cleanest single quality number the project can publish.
- **2b. Threshold calibration.** From the recorded hits, sweep offline: `cluster_threshold` over
  {2,3,4,5}, `max_sentence_share` over {0.2…0.6}, `soft_per_paragraph` over {1,2,3}. Plot machine-arm
  firing rate against human-arm false-positive rate; choose an operating point. This is where
  `cluster_threshold: 3` stops being `[declared]`.
- **2c. Suppression test.** Human prose naturally contains the `HU-B` forms — `-va/-ve van`,
  sentence-initial `És`, double negation, discourse particles, `ami`. Any edit touching one is an
  automatic catch-trial failure, at a scale round 1's three hand-built decoys could not reach.
  **19 of the 23 are well tested this way.** The other four are recorded as not tested and why:
  HU-B04 and HU-B08 are too rare for rate estimation, HU-B09 needs a Transylvanian stratum, and
  HU-B10 is suppressed by professional editing, so an edited corpus understates it by construction.

### 5.4 Phase 3 — blind ballot, second rater

Only on what phases 1 and 2 surfaced. **The second rater is the binding constraint**, and no corpus
removes it — round 1's single interested rater is the limitation that both prior rounds name.

Two instrument defects from round 1 are inherited as rules: no key is published until that round's
retests are in, and **a decoy may differ from the original only in the forbidden operation, never in
lexical quality.**

### 5.5 Phase 4 — revision

Two decisions that must not be taken in one motion, because the repository has already been bitten
by conflating them:

1. **The evidence decision** — what was measured, what enters `measured_patterns`. A question about
   truth.
2. **The behaviour decision** — whether the now-unmarked pattern should be allowed to fire on its
   own score. A question about calibration.

Removing the estimate marker **re-arms a pattern**, because the marker is what closes the
score path. When the markers were added between rounds 1 and 2, that change silently disarmed a
working rule; the reverse move can silently arm a bad one.

---

## 6. Instrument validation

A corpus measurement is worth something only if the pipeline first answers questions whose answers
are already known. These are **canaries, not results.** If one fails, the instrument is broken, not
the language.

| canary | expected | what its failure indicts |
|---|---|---|
| HU-B05 double negation: `senki` / `semmi` / `soha` / `sehol` co-occurring with `nem` / `sem` | ~100% in every human arm | tokenisation or sentence splitting |
| Domonkosi replication: `Ön` / `Önök` in the `hivatalos` subcorpus | ≈78% (240 official letters, `real.mtak.hu/75699`) | the register stratification is wrong |
| HU-B01 `-va/-ve van` | abundant, every register | morphological matching |
| `ímél` — a form the orthographic rules accept | ≈0 | nothing; it demonstrates that "both are correct" is not "both are attested" |
| HU-T01: the Hungarian quotation mark in edited press | dominant | see below |

That last row is a side benefit worth stating. The 35 `FIX` and 12 `FIX-IF` patterns rest on the
codified orthographic norm, not on machine evidence, so they need no measurement of this kind. But
the same pipeline shows, at no extra cost, whether **published practice actually follows the norm**
the fix layer enforces. If it does not, that is a finding about the fix layer and belongs in the
write-up.

---

## 7. Pre-registered analysis decisions

Fixed before any number is seen.

**The statistic.** Per pattern, per register: occurrences per million words in each arm, with a
ratio and a 95% confidence interval. The ratio is the estimate an `AI:` value encodes; the interval
is what decides whether it may be reported at all.

**Earning measured status.** A pattern moves into `measured_patterns` only if all of:

1. it is tier A, or tier B with its operationalisation published as code;
2. its confidence interval excludes 1 in the register where it is claimed;
3. the register-matched comparison is powered — expected counts high enough that the interval is
   informative rather than merely wide;
4. the direction agrees with the catalogue's stated `AI:` value.

A pattern meeting 1–3 but failing 4 does not keep its marker quietly. Its `AI:` value is corrected.

**Retiring a pattern.** Where the interval contains 1 in every register, the pattern makes no
discriminative claim that survives measurement. It moves to `[jelöld]` or to `do-not-touch.md`, with
the measurement recorded as the reason. This would be the first mechanism in this repository that
retires a pattern on evidence rather than on argument, and it applies symmetrically: a pattern is
not spared because someone finds the linguistics persuasive.

**Where the interval crosses 1 in the other direction** — the form is *more* frequent in human
Hungarian — the pattern is actively harmful and moves to the suppression list.

**No marker is removed on a firing-rate result.** Round 2 established that a firing-rate measurement
is not evidence that an `AI:` value is right. That still holds; only the two-arm ratio bears on the
marker.

---

## 8. Two internal contradictions this round settles

**Paragraph length.** `06-rhythm.md` treats "every paragraph 3–5 sentences" as a machine tell.
`example-rewrite.md` and `SKILL.md` assert that a Hungarian prose paragraph is "typically 3–4
sentences" as the human norm, without a source. The ranges overlap, and this is not cosmetic: the
**entire edit budget is calibrated on the second claim** — the per-paragraph limit of 2 soft edits is
described as usually unreachable precisely because paragraphs run 3–4 sentences. One
sentences-per-paragraph distribution, stratified by register, settles both. It is the
highest-yield single measurement in this round.

**The light-verb split.** HU-B18 protects idiomatic light-verb constructions (`köszönetet mond`,
`házkutatást tart`); `substitutions.md` replaces 18 "terpeszkedő" ones. Both classes are
noun-plus-verb of the same surface shape. If human prose contains both at comparable rates across
registers, the distinction has no corpus basis and is lexical stipulation. If the replaceable set
concentrates in administrative Hungarian while the protected set spreads across genres, the
distinction is empirically real. This is a foundational catalogue decision that has so far rested on
argument.

---

## 9. What this round will not establish

- **Whether any edit is good.** That is phase 3, and the second rater is its bottleneck. A frequency
  difference does not show that acting on it improves the text.
- **Anything measured about the 16 tier C patterns**, beyond sampled observation. Four of the five
  cluster overrides have tier C gates; none of those can enter `measured_patterns`.
- **The generation-side prohibitions.** The `HU-B` entries that forbid *producing* a form
  (`-tatik/-tetik`, `kell menjek`, stigmatised dialect forms) can have their human baseline
  established, but a human corpus cannot show what the tool does not emit.
- **The markup-dependent patterns**, unless a markup-preserving source is found.
- **A single unified "human corpus."** MNSZ2 cannot be downloaded in bulk, so tier B full-text
  statistics run on Webcorpus 2.0 and MEK — *different material from the tier A baseline*. This
  distinction is carried through every table in the write-up and is not collapsed under one label.
- **Anything to ±1.** Round 2 saw the suspect list move 24% between two runs of the same specimen on
  the same catalogue.

---

## 10. Artefacts

| path | contents |
|---|---|
| `docs/round-3-protocol.md` | this file |
| `docs/validation.md` | round 3 write-up, after execution |
| `scripts/parse_run.py` | three-part output parser (phase 0) |
| `scripts/measure.py` | tier A/B counting over a corpus |
| `data/manifest.csv` | source register: URL, outlet, date, genre, word count, SHA-256, rights check |
| `data/raw/` | local only, gitignored |
| `tests/corpus/` | extended with A3 and A4 material plus generation prompts |

Placement note: `scripts/check.py` globs `docs/*.md`, not `docs/**/*.md`. A protocol filed under a
`docs/research/` subdirectory would be exempt from link-integrity and pattern-ID checking, which is
the kind of unenforced convention this repository tries not to accumulate. It is filed flat instead.
