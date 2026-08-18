<!-- stet-run: source=skills/stet-hungarian sha256=22f8a1a7 date=2026-08-17 -->

## 0. Nyelv és regiszter

A szöveg magyar. A szöveget `formal` regiszterként kezelem – a regisztert a hívó **rögzítette**, nem a szövegből vezettem le. Ez zárja a Pass 3-at a HU-H04-en kívül, kiveszi a HU-L07-et a Pass 4-ből, és leállítja a Pass 5-öt a HU-R09, HU-R10, HU-R11 kivételével.

## 1. A javított szöveg

```
---
title: Online lakcímigazolás az önkormányzatnál
type: guide
status: active
updated: 2026-08-14
---

# Lakcímigazolás mostantól online is igényelhető

Tisztelt Lakosok!

Örömmel tájékoztatjuk Önöket, hogy önkormányzatunk elindította új online ügyintézési szolgáltatását, amelynek keretében lakcímigazolás mostantól otthonról, ügyfélfogadási időponthoz kötöttség nélkül is igényelhető. A fejlesztés célja, hogy a leggyakrabban kért, egyszerűbb ügytípusok intézése ne igényeljen személyes megjelenést a hivatalban.

## Kinek szól a szolgáltatás

Azoknak a lakosoknak ajánljuk, akiknek munkáltató, bank, iskola vagy más hivatal felé kell igazolniuk a bejelentett lakcímüket, és nem szeretnének emiatt sorban állni. A szolgáltatás igénybevételéhez érvényes ügyfélkapu- vagy DÁP-regisztráció szükséges, mivel a rendszer ezen keresztül azonosítja a kérelmezőt.

## Hogyan igényelhető

Az igazolás igényléséhez keressék fel önkormányzatunk honlapját, majd a főoldalon található „Online ügyintézés” menüpont alatt válasszák a „Lakcímigazolás igénylése” lehetőséget. A rendszer ezt követően átirányítja Önöket az azonosítási felületre, ahol Ügyfélkapus vagy arcképes azonosítással léphetnek be. Sikeres azonosítás után egy rövid űrlapot kell kitölteni, amelyben meg kell adni, hogy az igazolást milyen célra kérik – ez azért fontos, mert egyes intézmények csak a célnak megfelelő formátumú igazolást fogadják el.

Az igénylés beküldése után a rendszer automatikusan ellenőrzi az adatokat a nyilvántartásban, és amennyiben nincs eltérés vagy hiányosság, az igazolás elektronikusan, hitelesített formában kerül kiállításra. Ez a folyamat a tapasztalataink szerint néhány percen belül lezajlik, de kivételes esetben, amikor kézi ellenőrzésre van szükség, egy munkanapot is igénybe vehet.

## Mit kapnak kézhez

Az elkészült igazolás PDF formátumban, elektronikus aláírással és időbélyeggel érkezik a regisztrált tárhelyre vagy a megadott e-mail-címre, az igénylés során választott opciótól függően. Ez a dokumentum jogilag egyenértékű a papír alapon, személyesen igényelt igazolással, így bármely intézménynél elfogadható.

## Mi a helyzet azokkal, akik nem tudják online igényelni

Fontos hangsúlyoznunk, hogy a személyes ügyintézés lehetősége továbbra is megmarad. Aki nem rendelkezik ügyfélkapu-regisztrációval, vagy egyszerűen a hagyományos utat részesíti előnyben, változatlanul felkeresheti az Okmányirodát a szokásos ügyfélfogadási időben.

## Segítségre van szükségük?

Ha az igénylés során technikai problémába ütköznek, vagy kérdésük merül fel a folyamattal kapcsolatban, keressék ügyfélszolgálatunkat telefonon vagy a honlapon található elérhetőségeken. Munkatársaink készséggel segítenek az online ügyintézésben is.

Bízunk benne, hogy az új szolgáltatás sok lakosunk mindennapjait egyszerűsíti meg.
```

## 2. Változástábla

| ID | Eredeti | Új | Indok |
|---|---|---|---|
| HU-M01 | `Mit kapunk kézhez` | `Mit kapnak kézhez` | megszólításkeveredés: a szöveg végig önöz, a T/1 `mi` viszont mindenhol máshol az önkormányzatot jelöli, itt a lakost; a többségi forma nyer |
| HU-T14 | `e-mail címre` | `e-mail-címre` | angol mintájú különírás; a magyar összetétel kötőjeles, mert az előtag már tartalmaz kötőjelet |

## 3. Gyanús, de nem javítottam

- **HU-L03** [pattern-exception] – `Fontos hangsúlyoznunk, hogy` metaszöveges keret a bekezdés élén, de a minta `Jelek` sora zárt lista, és ez a fordulat nincs rajta; a minta kifejezetten tiltja a hasonló hangzású fordulatokra általánosítást.
- **HU-H02** [register] – `az igazolás … kerül kiállításra`: szenvedőpótló `-ásra kerül`, a gyorsteszt 4. jele. A minta `FIX-IF: informal, neutral`, a rögzített regiszterben a kapu zárva.
- **HU-H07** [register] – `Örömmel tájékoztatjuk Önöket, hogy`: hivatali klisé a `Tájékoztatom, hogy` családból. Ugyanaz a regiszterkapu zárja.
- **HU-H06** [register] – `amennyiben nincs eltérés vagy hiányosság`: formális kötőszó-körülírás. `formal`-ban csak klaszterben cserélhető, a bekezdés `SOFT` pontszáma 2, a küszöb 3 (HU-B19).
- **HU-F08** [register] – `kérdésük merül fel a folyamattal kapcsolatban`: terjengős névutó. `FIX-IF: informal, neutral`, `formal`-ban a saját `Mikor NE`-je is zárja.
- **HU-L09** [threshold] – `Aki nem rendelkezik ügyfélkapu-regisztrációval`: üres létige-körülírás a `van` helyett. A bekezdés pontszáma 1 (`kozepes?`), a küszöb 3.
- **HU-M12** [threshold] – `Ügyfélkapus` a bekezdésben, `ügyfélkapu-regisztráció` két másik helyen: ugyanaz a fogalom kétféle írásmóddal. A bekezdés nem éri el a küszöböt, és a nagybetűs alak lehet a szolgáltatás hivatalos neve – az egységesítés iránya bizonytalan.
- **HU-F01** [threshold] – `A fejlesztés célja, hogy a … ügytípusok intézése ne igényeljen személyes megjelenést`: három `-ás/-és` főnév egy mondatban. 2 pont, a küszöb 3.
- **HU-F01** [threshold] – `Az igénylés beküldése után … nincs eltérés vagy hiányosság`: nominalizációs lánc. Szintén 2 pont, és az `igénylés` ráadásul a szöveg terminusa.
- **HU-G14** [pattern-exception] – `munkáltató, bank, iskola vagy más hivatal felé kell igazolniuk`: a `felé` névutó a részes eset helyett hivatali vonzatcsere, nem angol prepozíció-kalk, ezért a minta `Jelek` sorára nem illik.
- **HU-T09** [pattern-exception] – `felkeresheti az Okmányirodát`: köznévi intézménytípus nagy kezdőbetűvel. A minta `Mikor NE`-je szerint a szervező saját anyagában ez márkanévhasználatnak számít, ezért nem nyúltam hozzá.
- **HU-T10** [pattern-exception] – `PDF formátumban`: a betűszóhoz kapcsolt összetételi utótag kötőjeles lenne (`PDF-formátumban`), de ezt az esetet a minta nem sorolja fel (mozgószabály és 6:3 nem érinti), ezért minta-ID nélküli javítás lenne.
- **HU-L13** [pattern-exception] – `Bízunk benne, hogy az új szolgáltatás sok lakosunk mindennapjait egyszerűsíti meg.`: általános pozitív zárlat, de nincs a minta zárt `Jelek` listáján, tehát ezen a címen nem törölhető.
- **HU-R09** [pattern-exception] – `DÁP-regisztráció`: feloldatlan rövidítés, az olvasó nem tudja meg, mi az. A minta nem fut, mert a szövegen kívül adatolható, bevett szakszó – a feloldás hiánya viszont szerzői döntés kérdése.
- **nincs minta** [no-pattern] – `Mi a helyzet azokkal, akik nem tudják online igényelni`: kérdő címsor kérdőjel nélkül, miközben a `Segítségre van szükségük?` címsor kiteszi. Következetlenség, de egyik tipográfiai minta sem fedi.

## 4. Klaszterpontok

| # | Kezdet | Pont | Minták |
|---|---|---|---|
| 1 | `Tisztelt Lakosok!` | 0 | nincs |
| 2 | `Örömmel tájékoztatjuk Önöket…` | 2 | HU-F01 |
| 3 | `Azoknak a lakosoknak ajánljuk…` | 0 | nincs |
| 4 | `Az igazolás igényléséhez keressék fel…` | 2 | HU-M12 |
| 5 | `Az igénylés beküldése után a rendszer…` | 2 | HU-F01 |
| 6 | `Az elkészült igazolás PDF formátumban…` | 0 | nincs |
| 7 | `Fontos hangsúlyoznunk, hogy a személyes…` | 1 | HU-L09 |
| 8 | `Ha az igénylés során technikai problémába…` | 0 | nincs |
| 9 | `Bízunk benne, hogy az új szolgáltatás…` | 0 | nincs |

A front matter nem szerepel a táblázatban: strukturált metaadat, nem bekezdés.
