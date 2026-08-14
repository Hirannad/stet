# Mechanikus párcserék

Ez a fájl **lookup**: a bal oldal helyére a jobb oldal kerül, ha a regiszterkapu engedi. Ami
ennél több mérlegelést kíván, az a `0X-*.md` fájlokban van blokk formában.

**Két előfeltétel minden cserére. Ha bármelyik sérül, a sor nem alkalmazható.**

1. **A szerkezet legyen csupasz.** A terpeszkedő és a `kerül`-táblázat sorai csak akkor
   cserélhetők, ha a főnévi tag **determinálatlan és nem referenciális** – nincs előtte névelő,
   mutató névmás vagy jelző. `döntést hoz` → `dönt`, de az `ezt a döntést meghozni` **marad**:
   ott a `döntés` valódi, visszautaló tárgy, nem a szerkezet üres tagja.
2. **A vonzatkeret legyen azonos.** Csak akkor cserélj, ha a tartalmas ige ugyanazt a vonzatot
   kívánja, mint a szerkezet. `döntést hoz a pályázatokról` → `dönt a pályázatokról` rendben;
   ha a csere kötelező tárgyat vagy más esetragot hozna be, ne cseréld (HU-H08).

Ha egy sor alkalmazhatóságában bizonytalan vagy, ne cseréld – írd a „gyanús, de nem javítottam”
listára. A HU-B18 (idiomatikus szerkezetek) és a HU-H10 (hivatali regiszter) mindkét előfeltétel
fölött áll.

**Regiszterkapu.** Ahol `L` áll a jobb szélen, ott a csere `legal` profilban **tilos**;
ahol `F`, ott `formal`-ban is csak klaszterben. Jelöletlen sor minden profilban megy.

**Egyirányúság.** Minden csere egyirányú. A visszafelé csere tilos, akkor is, ha a szöveg
indokolná – lásd `do-not-touch.md`.

---

## Terpeszkedő kifejezések → egyszerű ige

| Helyette | Ez | |
|---|---|---|
| döntést hoz | dönt | L |
| intézkedést foganatosít | intézkedik | L |
| javítást végez | megjavít | L |
| vizsgálatot folytat | megvizsgál | L |
| ellenőrzést gyakorol | ellenőriz | L |
| értékelést végez | értékel | L |
| módosítást eszközöl | módosít | L |
| beszerzést bonyolít | beszerez | L |
| javaslatot tesz | javasol | L |
| kérelmet nyújt be | kérelmez | L |
| bejelentést tesz | bejelent | L |
| megállapítást nyer | megállapítják | L |
| alkalmazást nyer | alkalmazzák | L |
| intézkedés történik | intézkednek | L |
| felülvizsgálat alá von | felülvizsgál | L |
| használatba vesz | használni kezd | L |
| tájékoztatást ad | tájékoztat | L |
| engedélyt ad | engedélyez | L |

Kivétel: `köszönetet mond`, `zajt csap`, `zokon vesz`, `házkutatást tart`, `feljelentést tesz`,
`magánindítványt tesz` – ezek idiomatikusak vagy szakszavak. Lásd HU-B18, HU-H08.

## `-ásra/-ésre kerül` → cselekvő

| Helyette | Ez | |
|---|---|---|
| elfogadásra kerül | elfogadják | L |
| megrendezésre kerül | megrendezik | L |
| aláírásra kerül | aláírják | L |
| kifizetésre kerül | kifizetik | L |
| kiadásra kerül | kiadják | L |
| telepítésre kerül | telepítik | L |
| bevezetésre kerül | bevezetik | L |
| törlésre kerül | törlik | L |
| hatályon kívül helyezésre kerül | hatályon kívül helyezik | L |
| megállapításra kerül | megállapítják | L |

Utána mindig ellenőrizd a HU-H09-et: ha az előző mondatnak többes alanya van, a T/3 kétértelmű.

## Névutók → esetrag

| Helyette | Ez | |
|---|---|---|
| vonatkozásában | -ról/-ről, -ban/-ben | F, L |
| tekintetében | -ról/-ről | F, L |
| esetében | -nál/-nél, vagy elhagyható | F, L |
| kapcsán | -ról/-ről | F |
| -t illetően | -ról/-ről | F, L |
| értelmében | szerint | L |
| keretében | -ban/-ben, során | F |
| terén | -ban/-ben | F |
| révén | -val/-vel, által | F |
| hiányában | ha nincs | L |
| esetén | ha | L |
| céljából | hogy | L |
| érdekében | hogy | F |

## Formális kötőszavak

| Helyette | Ez | |
|---|---|---|
| amennyiben | ha | F, L |
| tekintettel arra, hogy | mivel | F, L |
| azon tény fényében, hogy | mivel | F |
| abban az esetben, ha | ha | F |
| annak érdekében, hogy | hogy | F |
| azzal a céllal, hogy | hogy | F |
| ennek megfelelően | ezért | |
| ezen túlmenően | ráadásul, és | |
| mindazonáltal | mégis, viszont | |
| a fentiek értelmében | ezért | L |

## Metaszöveg → törlés

| Ez törlendő | |
|---|---|
| Fontos megjegyezni, hogy | |
| Érdemes megemlíteni, hogy | |
| Meg kell jegyezni, hogy | |
| Az alábbiakban bemutatjuk | |
| A következőkben áttekintjük | |
| Összefoglalva elmondható, hogy | |
| Mint látható | |
| Nézzük meg közelebbről | |
| Vágjunk bele | |
| Kérjük, vegye figyelembe, hogy | |
| Íme | |
| Természetesen! | |
| Remélem, segítettem! | |
| Nagyszerű kérdés! | |

Ezek törlése után a mondat a tartalommal kezdődik, és általában nagy kezdőbetűre kell javítani.

## Töltelék → törlés

| Ez törlendő, ha nincs funkciója | |
|---|---|
| gyakorlatilag | |
| alapvetően | |
| lényegében | |
| voltaképpen | |
| maga a(z) | |
| tulajdonképpeni | |

**Nem törlendő:** `hát`, `ugye`, `szóval`, `persze`, `tulajdonképpen`, `amúgy`, `izé`, `nos`,
`bizony`, `csak` – ezek diskurzusjelölők, funkciójuk van (HU-B14), és a HU-B14 `[NEVER]`, tehát ez
nem enyhítés, hanem tilalom. A `ma már`, `visszatér`, `külön-külön` sem törlendő (HU-B15).

A `tulajdonképpeni` **más szó**, és törölhető: melléknév (`a tulajdonképpeni feladat`), nem
diskurzusjelölő. A kettőt a HU-B14 nem mossa össze, és itt sem szabad.

## Üres fokozók → konkrétum

| Helyette | Ez |
|---|---|
| kulcsfontosságú | (mondd meg, mi történik nélküle) |
| elengedhetetlen | (ugyanaz) |
| kiemelkedő jelentőségű | (ugyanaz) |
| létfontosságú | (ugyanaz) |
| számos | (mondj számot, vagy hagyd el) |
| különböző | (nevezd meg, vagy hagyd el) |
| megfelelő | (mihez képest?) |
| adott | (melyik?) |

Ezek nem egy-az-egyben cserék: a fokozó helyére **konkrét állítás** kerül, nem másik szó.
Ha nincs konkrétum a forrásban, töröld – új tényt nem találhatsz ki.

**Ha a törlés megcsonkítja a mondatot** (a fokozó volt az állítmány névszói része, például
`X kulcsfontosságú`), akkor a törlés nem járható út. Ilyenkor két lehetőséged van, ebben a
sorrendben: (1) fogalmazd át a mondatot úgy, hogy a forrásban meglévő következményt mondja ki
(`A visszajelzés kulcsfontosságú` → `Visszajelzés nélkül a csapat nem fejlődik`, **ha** ez a
következmény szerepel a szövegben); (2) ha nem szerepel, cseréld semleges melléknévre (`fontos`),
és **írd be a változástáblába, hogy ez kompromisszum** – a fokozás megmaradt, csak halkabban.
Új tényt egyik úton sem hozhatsz be.

## Tükörfordított fordulatok

| Helyette | Ez |
|---|---|
| a nap végén (átvitt értelemben) | végső soron |
| amikor arról van szó, hogy | ha |
| az a tény, hogy | (hagyd el) |
| lehetővé teszi számunkra, hogy | -hat/-het, vagy eszközhatározó |
| biztosítja, hogy | gondoskodik róla, vagy egyszerű ige |
| ez nem X-ről szól, hanem | (bontsd fel állításra) |
| nem csupán X, hanem Y is | (állítsd egyszerűen) |
| játszik szerepet abban, hogy | (konkrét ige) |
| hozzájárul ahhoz, hogy | (konkrét ige) |

## Üres létige-körülírás

| Helyette | Ez | |
|---|---|---|
| -val/-vel rendelkezik | van neki | L |
| -ként szolgál | (konkrét ige) | |
| -t képvisel | (konkrét ige) | |
| otthont ad -nak | (konkrét ige) | |
| részét képezi | része | |
| jelentőséggel bír | fontos | |
| fontossággal bír | fontos | |

Kivétel: `a törvény úgy rendelkezik` – ott tartalmas.

## Tipográfiai jelcserék

| Helyette | Ez |
|---|---|
| `"…"` vagy `“…”` | `„…”` |
| `—` (em dash) | ` – ` (szóközös gondolatjel) |
| ` -- ` | ` – ` |
| `1,250,000` | `1 250 000` |
| `3.5` (tizedes) | `3,5` |
| `8GB` | `8 GB` |
| `60 %` | `60%` |
| `25°C` | `25 °C` |
| `Augusztus 2, 2026` | `2026. augusztus 2.` |
| `2.-i` | `2-i` |
| `Hétfő`, `Augusztus`, `Magyar` (köznévi) | `hétfő`, `augusztus`, `magyar` |
| `HTML-el`, `15%-al` | `HTML-lel`, `15%-kal` |
| `Továbbá,` mondat élén | `Továbbá` (vessző nélkül) |
| `projekt menedzsment` | `projektmenedzsment` |
| `magyar-angol`, `2020-2024` | `magyar–angol`, `2020–2024` |

**Soha ne cseréld vissza:** a `„…”` és a szóközös ` – ` a helyes magyar forma.

## Hivatali klisék

| Helyette | Ez | |
|---|---|---|
| Tájékoztatom, hogy | (mondd ki a tényt) | L |
| Kérjük tájékoztatásunk tudomásulvételét | (hagyd el) | L |
| nem áll módunkban | nem tudjuk | L |
| szíves tájékoztatásul | (hagyd el) | L |
| jelen dokumentum célja | (mondd meg, miről szól) | L |
| Maradok tisztelettel | Üdvözlettel | |

## Egyéb, ellenőrzött egyirányú javítások

| Helyette | Ez |
|---|---|
| `végett` okhatározóként (`az eső végett`) | `miatt` |
| `a számla kifizetett` (igenév állítmányként) | `a számlát kifizették` |
| `Sok fejlesztők` | `Sok fejlesztő` |
| `függ -on/-en` | `függ -tól/-től` |
| `felelős -ra/-re` | `felelős -ért` |

Visszafelé egyik sem. A `miatt` → `végett` csere hiperkorrekciós hiba (HU-B12).
