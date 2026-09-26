<!-- stet-run: source=skills/stet-hungarian sha256=624d938a date=2026-09-26 -->

## 0. Nyelv és regiszter

A szöveg magyar. A szöveget `neutral` regiszterként kezelem – a csatorna nem dönthető el (személyes hangú, de műfaja szerint belső incidensjegyzet is lehet), ezért a szigorúbb profilt választottam.

## 1. A javított szöveg

```
A keresés lassú lett, és három hétig nem tudtuk, miért. Végül kiderült: a gyorsítótár minden
kérésre újraépült, mert valaki kivett egy feltételt egy `if`-ből. Egy sor volt.

Hát, ennyi. Nem volt se architekturális hiba, se kapacitásprobléma – bár őszintén szólva azt hittem,
az lesz. (Majdnem meg is rendeltem két új node-ot.) A gyorsítótár azóta is gyorsítótár, ugyanaz a
kód, ugyanaz a kulcsképzés; csak a feltétel van a helyén.

Amit ebből megtanultunk, azt nehéz szabályba tenni. A mérés jó volt, a riasztás is jó volt, csak
senki nem nézte meg azt a commitot, mert egysoros volt. Most a review-ban az egysoros változás sem
megy át külön szem nélkül. Nem tudom, meddig tartjuk magunkat ehhez.
```

## 2. Változástábla

nincs

## 3. Gyanús, de nem javítottam

- **HU-F04** [pattern-exception] – `kivett egy feltételt egy if-ből`. Két `egy` egy mondatban, de a minta `Mikor NE`-je zárja: az egyik valódi számnév (egyetlen feltétel), a másik valódi határozatlanság (valamelyik `if`). Nem angolos névelőtúltengés.
- **HU-L14** [pattern-exception] – `A gyorsítótár azóta is gyorsítótár`. Alakilag tükörszimmetrikus, csattanós mondat, de a LinkedIn-teszt nem bukik el, és a folytatás konkrétumot mond ki (ugyanaz a kód, ugyanaz a kulcsképzés, a visszatett feltétel); a bekezdésben ott a két node is. A klaszter-felülírás második feltétele – nincs konkrét eset a bekezdésben – nem teljesül.
- **HU-R09** [pattern-exception] – `kulcsképzés`. Elvont `-és` összetétel, de nem bevezetetlen coinage: átlátszó, a szakmában a szövegen kívül is adatolt szó, és a mondat körül ott a konkrét eset. A `Jelek` feltétele nem teljesül.
- **nincs minta** [preserve] – `Hát, ennyi.` Diskurzusjelölő (HU-B14) és töredékes, ritmust adó mondat. Szándékosan megtartva; a megőrizendő jegyek közé tartozik.
- **nincs minta** [preserve] – `(Majdnem meg is rendeltem két új node-ot.)` Önjavító közbevetés konkrét számmal – a megőrizendő jegyek egyik legnehezebben hamisítható eleme.
- **nincs minta** [preserve] – `Nem tudom, meddig tartjuk magunkat ehhez.` Feloldatlan feszültség zárlatként. Nem HU-L13: nem felfelé mutató, tartalmatlan zárlat, hanem az ellenkezője.

## 4. Klaszterpontok

| # | Kezdet | Pont | Minták |
|---|---|---|---|
| 1 | `A keresés lassú lett, és három hétig…` | 0 | nincs |
| 2 | `Hát, ennyi. Nem volt se architekturális…` | 0 | nincs |
| 3 | `Amit ebből megtanultunk, azt nehéz…` | 0 | nincs |
