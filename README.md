***English** · [Magyar](README.hu.md)*

# stet

**stet** *(proofreader's mark: "let it stand")* — the annotation that cancels a correction.

A prose linter for machine-written text, as an [Agent Skill](https://agentskills.io/specification)
for Claude Code. It finds the tells that mark a text as LLM-generated or machine-translated, and
then — this is the part that makes it different — decides which of them to leave alone.

Currently one language: **Hungarian** (119 patterns). English is planned, and open questions are
tracked as issues.

## Who it is for

You write Hungarian with an LLM's help, and the result goes in front of other people: customer
mail, documentation, product copy, a newsletter, a policy.

The usual case is this. You have it written, you read it back, it looks fine, you send it — and
somebody replies that it reads "machine-made". This tells you which sentence, and why.

If you are writing notes for yourself, or the text is only going to be a prompt for something
else, it is not worth the round trip.

## What you actually get

The last measurement ran nine LLM-written Hungarian texts, from three models, through the tool.
**All nine contained a typographic or orthographic error** — between one and ten per text. Not
matters of taste: things that are simply wrong. An English quotation mark in a Hungarian sentence,
an em dash where the dash should be a spaced en dash, `1,250,000` for `1 250 000`, `HTML-el` for
`HTML-lel`.

Those are not bad because they look machine-made. They are bad because they make a text look
**careless**, and they are exactly the kind of error an author stops seeing on the tenth read.

That is the dependable part, and on a strong model's output it is usually the whole job: fix the
typography, leave everything else alone. The stylistic layer earns its keep on weaker models'
output, and even there it is not sound — see *Known limitations*.

## Install

```bash
/plugin marketplace add Hirannad/stet
```

```bash
/plugin install stet@stet
```

Or clone and symlink `skills/stet-hungarian` into `~/.claude/skills/`.

Then ask for it in Hungarian — *„nézd át ezt a szöveget”* — or in English over Hungarian text. It
returns the corrected text, a change table keyed by pattern ID, and a list of what it noticed and
deliberately left alone. It does not write to your files; see *What it is not* below.

## Why "let it stand"

Most tools of this kind are a list of tells plus an instruction to remove them. That works for
one pass and then keeps going: it has no way to say *this is fine here*, no way to say *I noticed
but I'm not touching it*, and no way to stop.

stet is built around the opposite default. Every mechanism in it answers one question: **when
should the tool decline to act?**

- **Severity levels** — always fix / fix only in these registers / fix only inside a cluster /
  never touch / flag but don't fix.
- **A suppression list** — 23 entries the tool is forbidden to "correct", because they are not
  errors. In Hungarian, a language model's default behaviour is to hypercorrect, and every such
  correction makes the text stiffer, which is to say *more* machine-like.
- **Evidence grading** — the marker records how much proof a pattern's *machine* claim is worth,
  which is a narrower question than whether the linguistics is sound. In this catalogue **every one
  of the 47 soft patterns is estimate-marked.** The sources behind them are real and some are
  quantitative, but a study showing that a construction is a calque is not a measurement of how
  often a model writes it — and the marker grades the second thing. An estimate-marked pattern can
  never justify an edit on its own score; it only contributes to a cluster. The fix-class patterns
  carry no marker because they make no claim about machines at all — they rest on the codified
  orthographic norm, where the question is not *is this a machine tell* but *is this correct*.
- **Register profiles** — informal / neutral / formal / legal, switching whole passes off. A
  contract is not a defective blog post; "plain-language" edits there lose legal effect.
- **A cluster gate** — soft patterns fire only when several *different* signals co-occur in one
  paragraph.
- **An edit budget** — a hard ceiling on the share of sentences touched. Above it the tool stops
  and reports instead of continuing.
- **A three-part output** — the corrected text, a change table keyed by pattern ID, and an
  explicit *"noticed but deliberately did not fix"* list.

The method is documented in [METHOD.md](METHOD.md); its values live in
[method/constants.yml](method/constants.yml), which is the single source for them. `scripts/check.py`
asserts that the prose agrees with the constants it reads — the constants file marks which of its
values are checked and which are, for now, only declared.

## When not to reach for it

- **The text is not Hungarian.** There is a language gate that stops and hands off, but then why
  start it.
- **You want a spell checker.** It is not one, deliberately. A missing consonant doubling or a
  compound written as two words goes straight past it.
- **You want a text to slip past an AI detector.** Not what it is for, and it would not work:
  fixing typography hides nothing.
- **You want a contract in plain language.** In a contract the formal nominal construction *is*
  the correct form, which is why whole passes switch off when the tool sees one. A plain-language
  version is separate work, not proofreading.

## What it is not

Not a spell checker, not a grammar checker, not a prescriptive language-nanny, not an AI
detector, and not a way to make text evade one. It will not fake humanity by inserting errors,
archaisms or idioms that were not there.

It also **does not write files** — but read the next sentence before relying on that. The skill
declares `allowed-tools: Read, Grep, Glob` and its instructions say to return the corrected text in
the conversation rather than overwrite anything. We measured whether the declaration is *enforced*,
and in an agent context it is not: the write tools remain available after the skill loads. So
review-only here is intent plus instruction-following, **not a sandbox.** Treat it as you would any
other agent instruction, and keep your text in version control.

## What it actually does, measured

This repository is a working plugin and a published measurement record, and the second half is not
decoration — [docs/programme.md](docs/programme.md) says what the project is for, what is settled,
and why a tool this size measures itself.

Three validation rounds so far, reported in full with their limitations in
[docs/validation.md](docs/validation.md). Round 2's corpus and every count ship in
[tests/corpus/](tests/corpus/), so you can re-run it and disagree — and since round 3 the runs
themselves ship too, in [tests/corpus/runs/](tests/corpus/runs/), machine-checkable by `make runs`.

**The soft layer barely fires on frontier-model Hungarian.** Round 2 ran the tool over nine
generated specimens, twice each. Across twelve runs on Sonnet- and Opus-written Hungarian it made
**zero** soft edits. All eighteen soft edits in the round came from Haiku-written text. The
typographic and orthographic layer, by contrast, fired on every specimen from every model — 137
changes across the eighteen runs.

**And it replicated.** Round 3 re-ran all nine specimens after the output format changed, which
also changed how edits are counted — and the sign held: every soft edit still came from
Haiku-written Hungarian, none from Sonnet's or Opus's. The absolute numbers do not carry across
the two rounds, and `docs/validation.md` says why.

Read that as guidance, not as a boast: on output from a strong model, expect this tool to fix
typography and stay quiet otherwise. It also means a catalogue of LLM tells is a moving target,
which is why the lexical lists carry a review date.

## Known limitations

Measured, published, and not resolved. Each item below is an open issue.

- **The soft layer is the weak part, and it is not fixed.** Round 1's blind ballot rejected every
  soft edit that reached a confident verdict, and wanted 8 of the 9 edits the tool declined. The
  suppression list and the fix layer held; the soft layer is miscalibrated in both directions. It
  needs rework before a 1.0. Round 2 deliberately did not redesign it on one rater's judgement.
- **The cluster gate and the edit budget are unmeasured.** The catalogue's most novel component
  decided the outcome in one run out of five in round 1; elsewhere every soft candidate was stopped
  earlier by its own exception clause. Seeded inputs can test whether the gate fires when a cluster
  is constructed, but they cannot say where the cut belongs — the density of a seeded cluster is
  chosen by whoever already believes the current threshold is right. Calibration is a question
  about a distribution, so it needs real text in both arms. Seeded inputs and a corpus are
  complementary here, not alternatives.
- **One rater, and it was the author.** Round 1 reports counts, not rates. It establishes no
  precision, no over-correction rate, no false-positive rate on clean Hungarian, and no
  per-pattern accuracy. Round 2 had no rater at all — it measured firing, not correctness. Read
  both as hypotheses a second reader may overturn. Disagreement is welcome as an issue.
- **Nothing here is measured to ±1.** Between two runs of the same specimen on the same catalogue,
  fix counts moved by up to 4 and the suspect list moved 24 %.
- **No pattern's `AI:` value rests on a citable measurement of machine output.** All 47 soft
  patterns carry the estimate marker and `measured_patterns` is empty. The linguistic sources are
  real, some are quantitative; none of them measures how often a model writes a given form.
- **Ordinary human typos are out of reach, by design.** The catalogue is provenance-shaped: it
  hunts machine tells, so a missing consonant doubling or a compound written as two words gets
  past it.
- **The fixtures in [tests/](tests/) are still specifications, not an automated suite.** The output
  now *has* a fixed shape and `scripts/parse_run.py` reads it, so the blocker is gone — but wiring
  the fixtures to it is a separate step nobody has taken.

## Coexisting with an English prose linter

If you install an unscoped English de-AI-ification skill alongside this one — several exist, and
they are good at what they do — be aware that **an English-phrased request over Hungarian text can
route to the wrong one.** This skill has a language gate that runs before anything else and hands
off when the text is not Hungarian. Most English tools have no such gate.

That matters because four common English prose rules prescribe the *opposite* of the Hungarian
norm: the spaced en dash and the `„…”` quote are correct Hungarian, the passive-voice ban is a
myth here, and copula-avoidance is meaningless in a language whose third person has no copula. A
misrouted run does not merely miss things — it introduces errors. See
[docs/design-rationale.md](docs/design-rationale.md).

## Skills

| skill | language | patterns |
|---|---|---|
| [stet-hungarian](skills/stet-hungarian) | Hungarian | 119 |

The skill's own documentation is in Hungarian — it is written for the people who will read its
output. The repository surface is English.

## Development

```bash
make check
```

Runs the structural checker: header grammar, severity and evidence enums, estimate markers,
required fields, unique and resolvable pattern IDs, single-source constants, the declared pass
inventory, link integrity across the whole repository, the Hungarian closing-quote glyph, and the
SKILL.md size budget. It is wired to a pre-commit hook (`make hooks`) and to CI.

The quote-glyph check exists because the catalogue once got it wrong in its own printed example —
69 occurrences of `„…"` with a straight closer, so a run that matched the example emitted
half-fixed output. That is the shape of bug this repository tries to make impossible rather than
merely fix.

## Licence and sources

MIT — see [LICENSE](LICENSE). Attribution and the relationship to prior work, including the
CC BY-SA 4.0 Wikipedia guide that six patterns take their taxonomy from, is set out in
[NOTICE.md](NOTICE.md). The Hungarian catalogue's own sources, and an honest account of what is
measured and what is estimated, are in
[skills/stet-hungarian/references/sources.md](skills/stet-hungarian/references/sources.md).
