# The generation prompt

This is the prompt that produced the nine specimens in this directory. It was **byte-identical**
across the three models apart from the output paths, and it deliberately says nothing about style,
about machine tells, or about wanting natural Hungarian — a specimen generated under instructions to
sound human would measure the instructions, not the model.

Each model was run once, in a fresh Claude Code agent context, with no other conversation. The three
texts per model came out of a single request.

```
Írj három magyar szöveget. Mindegyik 300–500 szó legyen.

Mentsd őket pontosan ezekre az útvonalakra:

1. <PATH>/01-code-review.md — Belső csapatszöveg egy fejlesztőcsapatnak arról, miért érdemes
   code review-t tartani, és hogyan érdemes csinálni.

2. <PATH>/02-devtool.md — Terméktájékoztató egy fejlesztői eszközről, ami a CI-futások hibáit
   gyűjti össze és rendezi. Az eszköz neve Ellenőr.

3. <PATH>/03-onkormanyzat.md — Lakossági tájékoztató egy önkormányzat új online ügyintézési
   szolgáltatásáról, amivel lakcímigazolást lehet kérni.

Csak a három szöveget írd meg és mentsd el. Ne adj hozzá kommentárt, magyarázatot vagy
összefoglalót.
```

## Why these three topics

Each one pins a different register profile, and round 1 exercised only `neutral`:

| topic | register | why |
|---|---|---|
| `01-code-review` | `informal` | internal team writing, the register where the tool is least restrained |
| `02-devtool` | `neutral` | product copy — the default profile, and round 1's only one |
| `03-onkormanyzat` | `formal` | municipal notice, where officialese is correct rather than a defect |

The register was **pinned by the operator before each run**, not inferred by the skill. The method
requires the register to be stated out loud before any edit, and letting the skill choose would have
added a second variable.

## Specimen sizes

| specimen | words |
|---|---|
| `haiku-01-code-review` | 392 |
| `haiku-02-devtool` | 443 |
| `haiku-03-onkormanyzat` | 357 |
| `sonnet-01-code-review` | 398 |
| `sonnet-02-devtool` | 398 |
| `sonnet-03-onkormanyzat` | 348 |
| `opus-01-code-review` | 431 |
| `opus-02-devtool` | 435 |
| `opus-03-onkormanyzat` | 408 |

3 610 words total. The length band matters: the text-level edit budget only engages above five
sentences, and the cluster gate needs a paragraph with room for several co-occurring signals. A
300-character specimen would have measured nothing about the soft layer, which is the layer under
test.

## Known limits of this corpus

- **The generator was an agent, not a bare model.** Each specimen came from a Claude Code agent with
  its own system prompt, so this is "how a Claude Code user gets Hungarian", not "how the raw model
  writes Hungarian". The same is true for all three, so the cross-model comparison holds; the
  absolute numbers carry that caveat.
- **One prompt per topic, one run per model.** No sampling, so nothing here separates model
  behaviour from run-to-run variance.
- **Three topics is not a genre survey.** No fiction, no legal text, no translated source, no
  academic prose.
