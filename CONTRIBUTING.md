# Contributing

## The one rule that matters

**Every example sentence must be invented.** Do not copy, and do not translate, an example from a
source — a style guide, a linguistics paper, Wikipedia, or another tool. A translated example is a
derivative work and it breaks the licence story in `NOTICE.md`. It also tends to smuggle in the
source's assumptions along with its words.

## Adding a pattern

A pattern is a block in a `references/*.md` file:

```
### HU-X99 · Short name · [SEVERITY] [AI:strength?] [kern|YYYY-MM]

Mi ez:                 what it is
Miért írja így a gép:  why a model produces it
Jelek:                 what to look for
ROSSZ:                 an invented bad example
JÓ:                    the same content, fixed
Mikor NE:              when NOT to apply it
Forrás:                where the claim comes from
```

Rules the checker enforces:

- **`Mikor NE` is mandatory** on anything that is not `[NEVER]`. If you cannot write an exception,
  the pattern is probably too broad. This is the single most useful discipline in the catalogue.
- **`Forrás` is mandatory.** One `Forrás` line per pattern header, no exceptions.
- **An estimate marker is mandatory** on a `SOFT` pattern unless it is listed in
  `measured_patterns` in `method/constants.yml`. A pattern whose strength you are guessing at must
  say so — otherwise the tool reads its own guess as a measurement and edits with unearned
  confidence.
- **Constants live in one place.** Do not restate the cluster threshold, the point values, the
  budget or the pass matrix in a reference file. If you need a *tighter* limit for one pattern,
  say so explicitly as a pattern-level tightening.
Reviewed by hand, not by the checker — `method/constants.yml` marks the difference with
`[checked]` and `[declared]`:

- **A cluster override needs a named, falsifiable test.** "This one is important" is not a test.
  The checker verifies that the declared override set matches the patterns that claim one; it
  cannot judge whether the test is falsifiable. Five overrides exist; adding a sixth is a review
  question.

`[NEVER]` entries use a different shape, and carry **no example pair** on purpose: an example pair
teaches a transformation, and these entries prohibit one. Given a pair, the tool starts producing
the very forms it was meant to leave alone.

## Adding a language

Add `skills/stet-<language>/` and a matching key under `skills:` in `method/constants.yml`.

The shape is shared; the values are not. Declare your own pass inventory, register profiles, pass
matrix, thresholds and budgets. In particular, **do not copy Hungarian's thresholds or its
"not editing is the default" stance** — that stance rests on a Hungarian premise (a prescriptivist
tradition that makes hypercorrection the dominant failure mode) which may not hold for your
language. `METHOD.md` says which parts are shape and which are config.

Every skill must carry a language guard: detect the language of the **text**, not of the request,
and hand off rather than edit if it does not match. Without it, an English-phrased request over
Hungarian text routes to the wrong skill and applies rules that are precisely inverted.

## Before you commit

```bash
make check
```

`make hooks` installs it as a pre-commit hook. CI runs the same script, plus
`claude plugin validate . --strict` and Agent Skills discovery.

## Before you run the skill for a measurement

```bash
make cache
```

The Skill tool serves the **installed plugin**, not this working tree, and the two drift apart
without saying so — a run driven through `stet:stet-hungarian` can measure the released catalogue
and return plausible output while doing it. This fails when the copies differ, and names the copy
behind every recorded run. It is not part of the commit gate: which plugin is installed is a fact
about your machine, not about the change you are making.

## Reviewing a disputed pattern

Look at the source before defending the pattern. Four patterns were removed or softened during
development because the cited source did not say what the pattern claimed — in one case the
source argued the opposite. That is the expected failure mode here, not an unusual one.
