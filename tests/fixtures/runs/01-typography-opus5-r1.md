<!-- stet-run: source=skills/stet-hungarian sha256=624d938a date=2026-09-26 -->

## 0. Nyelv és regiszter

A szöveg magyar. A szöveget `neutral` regiszterként kezelem: belső projektdokumentáció-jellegű állapotleírás, nincs benne jogi terminus, hivatkozásjegyzék vagy megszólítási forma, a csatorna pedig dokumentáció, nem közösségi felület.

## 1. A javított szöveg

```
A projekt heti jelentése szerint „a migráció csúszik”, ezért a csapat új határidőt kért. A vezető
– aki egyébként maga is fejlesztő – annyit üzent, hogy a döntés a következő tervezési körben
születik meg.

A becsült ráfordítás 2,5 nap, a rendelkezésre álló idő 3 nap, tehát a különbség 0,5 nap. A
csapat a 2020–2024 közötti szakaszban már háromszor futott bele ugyanebbe. Az új keretrendszer
8 GB memóriát kér, a régi 4 GB-ot igényelt, és a mérés 21 °C-on készült.

A „Projekt Áttekintés” nevű dokumentum tartalmazza a Budapest–Bécs vonal adatait is.
```

## 2. Változástábla

| ID | Eredeti | Új | Indok |
|---|---|---|---|
| HU-T01 | `"a migráció csúszik"` | `„a migráció csúszik”` | angol idézőjel magyar mondatban |
| HU-T02 | `— aki egyébként maga is fejlesztő —` | `– aki egyébként maga is fejlesztő –` | em dash helyett szóközös gondolatjel |
| HU-T04 | `2.5 nap`, `0.5 nap` | `2,5 nap`, `0,5 nap` | a tizedes jele magyarul vessző |
| HU-T03 | `2020-2024` | `2020–2024` | `-tól/-ig` viszony: nagykötőjel, tapadva |
| HU-T05 | `8GB`, `4GB-ot`, `21°C-on` | `8 GB`, `4 GB-ot`, `21 °C-on` | szóköz a szám és a rövidített mértékegység között |
| HU-T01 | `"Projekt Áttekintés"` | `„Projekt Áttekintés”` | angol idézőjel; csak az idézőjel változik, a cím maga nem |
| HU-T03 | `Budapest-Bécs` | `Budapest–Bécs` | tulajdonnevek alkalmi kapcsolata: nagykötőjel |

## 3. Gyanús, de nem javítottam

- **HU-T07** [zone] – `Projekt Áttekintés`: magyar címben csak az első szó lenne nagybetűs, itt viszont a dokumentum **neve** áll („nevű dokumentum”), tehát cím és tulajdonnév – érinthetetlen zóna, és a tartalmi invariáns is védi. Ha a dokumentum valódi címe kisbetűs, a szerző javíthatja; a szövegből ez nem dönthető el.
- **HU-R10** [pattern-exception] – `A „Projekt Áttekintés” nevű dokumentum tartalmazza a Budapest–Bécs vonal adatait is.` A mondat gyakorlatilag mutató: egy másik dokumentumra könyvel. A minta kötelező konkrétum-ellenőrzése viszont kivált – megnevezett dokumentum és megnevezett vonal áll benne –, tehát nem puszta pointer, és a mondat már a legtömörebb alakjában van. **Kötelező jelzés a második ellenőrzésből:** a hivatkozás feloldható, és csak ebben az egy mondatban szerepel; ha a szöveg hivatkozásjegyzéket kap, a cím átmozgatható oda, és a mondat utána törölhető. Törlés előtt viszont elveszne a kapcsolat.
- **nincs minta** [preserve] – `– aki egyébként maga is fejlesztő –` és az `egyébként`: közbevetés és diskurzusjelölő, emberi jegyek (`06-rhythm.md`, megőrizendő jegyek; HU-B14). Szándékosan maradt, csak a gondolatjel alakját javítottam.

## 4. Klaszterpontok

| # | Kezdet | Pont | Minták |
|---|---|---|---|
| 1 | `A projekt heti jelentése szerint…` | 0 | nincs |
| 2 | `A becsült ráfordítás 2,5 nap…` | 0 | nincs |
| 3 | `A „Projekt Áttekintés” nevű dokumentum…` | 0 | nincs |
