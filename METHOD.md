# The stet method

*Non-normative.* `method/constants.yml` is authoritative; `scripts/check.py` enforces it.
This file explains why the machinery is shaped the way it is. Where the two disagree, the
constants win and this file is wrong.

## The problem with a flat rule list

Most prose-cleanup tools are a list of tells and an instruction to remove them. That works on a
first pass and then keeps going. It has no way to say *this one is fine here*, no way to say
*I noticed but I'm not touching it*, and no way to stop.

Every mechanism below exists to answer one question: **when should the tool decline to act?**

## Severity — what to do

| label | meaning |
|---|---|
| `FIX` | always correct it, regardless of register |
| `FIX-IF` | correct it only in the listed register profiles |
| `SOFT` | correct it only inside a cluster (see below) |
| `NEVER` | never touch this, and never generate it either |
| `[jelöld]` | do not correct; report it |

`NEVER` is not decoration. A language with a strong prescriptive tradition trains models to
"correct" forms that are not errors, and each such correction makes the text stiffer — that is,
more machine-like. The suppression list is the part of a language toolkit most likely to be
missing, and most costly to omit.

Suppression entries carry **no before/after example pair**, deliberately. An example pair teaches
a transformation; these entries prohibit one. Given a pair, a model starts *producing* the
stigmatised forms it was supposed to leave alone.

## Evidence strength — how much proof it is worth

Separate axis from severity, because they answer different questions. `AI:eros` / `kozepes` /
`gyenge`, with a trailing `?` marking an estimate rather than measured data.

The `?` is a brake: an estimate-marked pattern never justifies an edit through the score alone,
it only contributes to a cluster. In a young catalogue nearly everything is an estimate — in the
Hungarian one, every soft pattern without exception — and saying so is the difference between a
documented guess and a fabricated measurement. The list of exempt patterns
(`measured_patterns` in the constants) is a place to *earn* your way out, not a default. It is
currently empty.

The `?` does not block a **cluster override** (below), because an override rests on a named
structural test, not on a frequency claim.

## Stability — how long the pattern will hold

`kern` = anchored in a codified orthographic or syntactic norm; changes only when that norm does.
`YYYY-MM` = a lexical list with a review date. Model vocabulary moves; today's tell is tomorrow's
neutral word. Lexical lists get reviewed every 12–18 months.

## Register profiles

A register profile switches whole passes off. Formal and legal registers are not defective
informal ones: in a contract, the nominal construction *is* correct, and "plain-language" edits
lose legal effect.

The profile must be stated out loud before any edit. Silent register switching is the failure
mode where a tool turns a contract into a chat message.

The pass matrix lives in exactly one file per skill.

## The cluster gate

Soft patterns fire only when several **different** signals co-occur in one paragraph, above a
numeric threshold. Rules that keep it honest:

- Only `SOFT` hits score. Two wrong quotation marks do not prove a paragraph is machine-written.
- One pattern counts once, however many times it fires. A cluster is co-occurrence of *different*
  signals; otherwise any broad pattern grants itself an override by matching twice.
- **What you cannot act on is not evidence.** If a hit is blocked — by a register gate, an
  untouchable zone, or uncertainty — its points do not count. Otherwise a signal the tool did not
  dare act on would legitimise acting elsewhere.

**Cluster overrides.** A few patterns count as a cluster alone, because they typically appear
*isolated* in an otherwise clean paragraph and could never reach the threshold — which is exactly
the case that annoys readers most. Every override must name a falsifiable structural test. If you
cannot write the test, you do not get the override.

## The edit budget

Per-paragraph cap on soft edits, and a text-level ceiling on the share of sentences touched. Above
the ceiling the tool stops and reports rather than continuing.

Deletions count as touched. The most aggressive operation is exactly where a budget must not go
slack.

`FIX` and `FIX-IF` are exempt: typography and spelling are corrections, not rewrites. A text full
of wrong quotation marks may legitimately change in every sentence.

## Untouchable zones and the content invariant

Quotations, titles, metalinguistic mentions, code, legal citations, structured metadata, link text
and targets, and foreign-language spans are never rewritten. No edit may change a number, name,
date, legal term, or the scope of a negation, quantifier or focus. Never add a fact.

**The density brake:** never *insert* idiom, proverb or discourse particle where there was none.
Idiom density that is too high reads as translated just as reliably as density that is too low.
Humanity is not faked by adding flavour — and never by introducing an error.

## The self-audit

Numbered yes/no questions, not "read it again". Each one is falsifiable, and the first is the
strongest: every change must trace to a pattern ID, or it gets reverted.

## The four-part output

Corrected text; a change table keyed by pattern ID; an explicit **"noticed but did not fix"**
list; and the cluster score of every paragraph. The third part is not a formality — it is the
pressure valve that lets the tool record uncertainty instead of escaping into an edit. It is the
single mechanism that most reduces over-correction.

Each suspect entry carries a **reason code from a closed list**, and the fourth part prints the
score the cluster gate actually read. Both exist for the same reason: which brake binds, and how
close a paragraph came to the threshold, are measurable questions, and free prose could not answer
them. That is what makes every run calibration data rather than only a corrected text.

## Porting to another language

Shape is shared. **Values are not.** A sibling skill declares its own pass inventory, its own
register profiles and matrix, its own thresholds, and its own default stance — under its own key
in `method/constants.yml`.

Two things in the Hungarian skill look like method but are config:

1. **"Not editing is the default."** This rests on a Hungarian premise: a strong prescriptivist
   tradition makes hypercorrection the dominant failure mode. In a language without that
   tradition the dominant failure mode is the model's own tells, and a sibling inheriting this
   brake would simply underperform.
2. **The pass inventory.** There is no translationese pass for a skill whose target language is
   the model's own latent language. The typographic pass, by contrast, is heavier in English.

Do not copy a threshold across languages. Nobody has calibrated what a point is worth.
