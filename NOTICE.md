# Notices and attribution

This repository is MIT-licensed (see `LICENSE`). This file records what it draws on, and on what
terms, because the licence question here is easy to get wrong.

## Wikipedia — "Signs of AI writing" (CC BY-SA 4.0)

Six patterns in the Hungarian catalogue cite the English Wikipedia guide
[Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), maintained by
WikiProject AI Cleanup, as the source of the **name of the phenomenon**:

- `HU-L05` — undue emphasis on significance
- `HU-L10` — superficial analyses with -ing endings
- `HU-L12` — collaborative communication artifacts
- `HU-L13` — generic positive conclusions
- `HU-M09` — outline-like sections, fragmented headers
- `HU-R03` — rule-of-three overuse (adopted **and then overridden**: this catalogue holds that a
  triple is not on its own a machine tell)

What is taken is the taxonomy — that these phenomena exist and are worth naming. **No text,
example sentence or phrasing is copied or translated from that page.** Every example sentence in
this repository is invented for it, and the Hungarian form tests, exceptions and register gates
are original work. Attribution is given here and at each pattern's `Forrás` line.

We are explicit about CC BY-SA because that page is copyleft, and a taxonomy borrowed without a
notice is how an attribution chain quietly breaks. If you extend this repository by *translating*
material from that page rather than restating it, the result is a derivative work and MIT is no
longer the right licence for it — write your own examples instead.

## Prior art in English

Two MIT-licensed projects address the same problem in English and were read while this catalogue
was built:

- [`blader/humanizer`](https://github.com/blader/humanizer) — MIT, © Siqi Chen
- [`hardikpandya/stop-slop`](https://github.com/hardikpandya/stop-slop) — MIT

**No pattern text, rule text or example was copied from either.** Their influence is at the level
of ideas — that a quotable-sounding sentence is a tell, that a density question belongs in a
self-audit — and where a specific idea was adopted or deliberately rejected, the reasoning is
recorded in [`docs/design-rationale.md`](docs/design-rationale.md).

Four of the English rules would prescribe the *opposite* of the Hungarian norm, which is why this
is a separate catalogue and not a translation. That, too, is documented rather than assumed.

## Hungarian sources

The linguistic sources — the Hungarian Academy's orthographic rules, Szepesy, Klaudy, É. Kiss,
Keszler, Tolcsvai Nagy, Domonkosi and others — are cited per pattern and listed with credibility
levels in `skills/stet-hungarian/references/sources.md`. They are cited, not reproduced; rule
statements are restated in our own words.

Four source misattributions were found and corrected during development. They are listed in
`sources.md` rather than quietly fixed, because the lesson generalises: when extending the
catalogue, read the source — citing its title is not enough.
