---
title: The programme — what this repository is, and why it measures itself
type: reference
status: active
updated: 2026-08-16
---

# The programme

[README.md](../README.md) describes a tool. This page describes the project the tool is part of,
because the two are not the same thing and a reader who assumes they are will misjudge both.

---

## Two things in one repository

**A working plugin.** [skills/stet-hungarian](../skills/stet-hungarian) is installable today and
does a job that measurement supports: it fixes Hungarian typography and orthography in
machine-written text. Every specimen in every round carried errors of that kind, from every model
tested. If that is what you came for, install it, read the README, and stop there.

**A published measurement record.** [docs/validation.md](validation.md) reports three rounds
against the tool, including the round whose headline finding is that the tool's most interesting
layer does not work. [tests/corpus/](../tests/corpus/) ships the material, the counts and the runs,
so the numbers can be re-derived by a stranger rather than believed. This half is written for
somebody building a similar catalogue in another language, or deciding whether to trust this one.

The two halves pull in opposite directions, and it is worth saying which wins. A tool wants to
claim as much as it can defend. A measurement record wants to claim as little as the evidence
forces. **Where they conflict here, the record wins** — which is why the README's limitations
section is longer than its feature list, and why `measured_patterns` in
[method/constants.yml](../method/constants.yml) is empty rather than populated with the best guess
available.

### What is settled and what is not

| layer | status |
|---|---|
| typography and orthography (`FIX`, `FIX-IF`) | dependable; rests on the codified norm, not on machine evidence |
| the suppression list (23 `NEVER` entries) | held every catch trial run against it |
| the register gate | the one brake round 1 found calibrated |
| the soft layer (47 patterns) | **not established**; see [issue #1](https://github.com/Hirannad/stet/issues/1) |
| the cluster gate and the edit budget | **unmeasured**; see [issue #2](https://github.com/Hirannad/stet/issues/2) |

A 1.0 waits on the fourth row. That is a deliberate choice about what a version number should mean
here, not a backlog that happens to be long.

---

## Why the measurement is worth it

### The `AI:` value is the whole claim

Every pattern in the catalogue carries an `AI:` value, and that value asserts one specific thing:
**this form appears more often in machine-written Hungarian than in human-written Hungarian.** It is
a claim about a rate difference between two populations.

The catalogue has real linguistic sources behind its patterns, and some of them are quantitative.
None of them measures that. A study establishing that a construction is a calque describes how
*people* write; it says nothing about how often a model produces the form. The two questions
diverge, and only the second one licenses an edit made on the grounds of machine origin.

This is why all 47 soft patterns carry the estimate marker and why `measured_patterns` is empty.
The gap is not an oversight the project has yet to get to. It is the project's central open
question, written into the machinery so that no pattern can quietly act as though the question were
settled.

### What follows if the measurement never happens

Two outcomes, and no third:

1. **The soft layer ships unproven.** The tool keeps rewriting Hungarian sentences on the strength
   of an argument, in a catalogue whose own first rule is that an argument is not a measurement.
   Round 1 already indicates what that costs: a native reader rejected every soft edit that reached
   a confident verdict, and wanted eight of the nine edits the tool had declined.
2. **The soft layer is cut.** What remains is a good typographic corrector — worth having, and
   honestly labelled, but the part that distinguishes this catalogue from a substitution table
   would be gone.

Neither is reached by waiting. Both are reached by deciding, and the measurement is what makes the
decision something other than a preference.

### Why a repository this size is the one doing it

The obvious objection is that a corpus study is out of proportion to a single-language prose linter
maintained by one person. The answer is that the study is the more durable artefact.

The pattern catalogue has a shelf life. Round 2 showed the soft layer firing on Haiku-written
Hungarian and never on Sonnet's or Opus's, which means some of what it calls a machine tell is
better described as a tell of a 2025-era machine. The lexical lists carry review dates for that
reason. A method for deciding *when a prose rule has earned the right to act* does not expire the
same way, and neither does a measured false-positive rate on human Hungarian, which nobody has
published for this or any comparable tool.

[METHOD.md](../METHOD.md) already states the shape of that method. What is missing is the evidence
step, and this is the repository where it is cheapest to add — the catalogue, the register
stratification, the suppression list and the run parser already exist.

### What "worth it" costs, and the cut that was made

[docs/round-3-protocol.md](round-3-protocol.md) specifies a four-arm corpus measurement: human
Hungarian, human-translated Hungarian, machine-translated Hungarian, and LLM-generated Hungarian,
each stratified by register. It is pre-registered, and it is more work than this project will
complete in one stretch.

**One arm runs first: the false-positive rate on edited, pre-2022 human Hungarian.** It is the
cheapest arm, it needs no corpus registration, and it answers the single question both prior rounds
name as unestablished. The other three arms stay specified and unrun, and the protocol says which
is which rather than letting the gap read as an omission.

The protocol also corrects a claim this repository made about itself. The README used to say that
calibrating the cluster gate needs seeded inputs rather than real text. Seeded inputs test whether
the gate fires when a cluster is constructed; they cannot say where the cut belongs, because the
density of a seeded cluster is chosen by whoever already believes the current threshold is right.
Calibration is a question about a distribution, and a distribution needs real text.

---

## How to read the rest of the documentation

| file | what it is for |
|---|---|
| [README.md](../README.md) | the tool: what it does, what it refuses to do, what not to reach for it for |
| [METHOD.md](../METHOD.md) | why the machinery is shaped this way; non-normative |
| [method/constants.yml](../method/constants.yml) | the authoritative values, marked `[checked]` or `[declared]` |
| [docs/validation.md](validation.md) | what was measured, in the order it ran, with its limitations |
| [docs/round-3-protocol.md](round-3-protocol.md) | what will be measured next, written before the measuring |
| [docs/design-rationale.md](design-rationale.md) | what was considered and rejected, so it is not re-adopted |
| [CONTRIBUTING.md](../CONTRIBUTING.md) | the rules a new pattern has to satisfy |

Disagreement is the contribution this project most needs, and the
[issues](https://github.com/Hirannad/stet/issues) are the place for it. Four patterns were already
removed or weakened during development because the cited source did not support them, and in one
case argued the opposite. That is the expected failure mode here, not an unusual one.
