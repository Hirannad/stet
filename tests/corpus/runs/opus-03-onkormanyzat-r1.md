<!-- stet-run: source=skills/stet-hungarian sha256=22f8a1a7 date=2026-08-17 -->

## 0. Nyelv és regiszter

A szöveg magyar. A regisztert a hívó **rögzítette**, nem én következtettem ki: a szöveget `formal` regiszterként kezelem. (Önkormányzati lakossági tájékoztató, végig önöző megszólítással; a pass-mátrix szerint így a Pass 3 gyakorlatilag zárva van, a Pass 5-ből pedig csak a HU-R09, HU-R10 és HU-R11 fut.)

## 1. A javított szöveg

```
# Lakcímigazolás online – indul az új szolgáltatás

**Kertvárad Város Önkormányzata** tájékoztatja a lakosságot, hogy szeptember 1-jétől lakcímigazolás sorban állás nélkül, otthonról is kérhető. A szolgáltatás a város ügyintézési portálján érhető el, éjjel-nappal.

## Kinek jó ez

Aki eddig azért vett ki fél napot, hogy a hivatalban kiállítsanak egy papírt, amit aztán a biztosítónak, az iskolának vagy a banknak kellett bemutatni, annak ez a szolgáltatás körülbelül tíz percet vesz el az életéből – és nem a hivatal nyitvatartása alatt.

Az igazolás a saját lakcíméről, illetve a Önnel egy lakcímen élő kiskorú gyermeke lakcíméről kérhető. Más felnőtt személy adatairól továbbra is csak írásos meghatalmazással, személyesen intézhető ügy.

## Mi kell hozzá

- **Azonosítás:** Ügyfélkapu+ vagy a Digitális Állampolgárság alkalmazás (DÁP). Ha még nincs ilyen azonosítója, a Kormányablakban néhány perc alatt beállítható.
- **Egy e-mail-cím**, amire az elkészült igazolást kéri.
- **Érvényes személyi azonosító.**

## Így zajlik

1. Nyissa meg az **ugyintezes.kertvarad.hu** oldalt, és kattintson a *Lakcímigazolás kérése* pontra.
2. Azonosítsa magát. A rendszer a nyilvántartásból behozza a nevét és a lakcímét – ezeket nem kell begépelni, csak ellenőrizni.
3. Jelölje meg, mire kell az igazolás, és hogy elektronikusan vagy postán kéri.
4. Küldje be a kérelmet. A visszaigazolás azonnal megjelenik a képernyőn, és e-mailben is megkapja.

Az elektronikus igazolás **három munkanapon belül** érkezik meg, PDF formában, hivatalos elektronikus bélyegzővel. Ez a dokumentum ugyanannyit ér, mint a papíron kiadott: kinyomtatva is elfogadják, de érdemes elektronikusan továbbküldeni, mert így az érvényessége ellenőrizhető marad. Postai kérés esetén a kiküldés öt munkanap.

## Mennyibe kerül

A lakcímigazolás kiadása **díjmentes**. Postai kiküldés esetén a küldemény díját az önkormányzat állja. Semmilyen díjat nem kérünk bankkártyával a portálon – ha ilyen felszólítást kap e-mailben vagy SMS-ben, az csalás, kérjük, ne kattintson rá, és jelezze a hivatalnak.

## Ha elakad

A személyes és a papíralapú ügyintézés **megmarad**, nem kötelező online igényelni. Ügyfélszolgálatunk a Fő utca 12-ben hétfőn és szerdán 8–16, csütörtökön 8–18 óra között várja Önöket.

Aki szeretné az online utat használni, de bizonytalan a technikában, annak segítünk: a Városi Könyvtár olvasótermében **szeptember hónapban minden csütörtök délután 14 és 17 óra között** ügyintéző segít a kérelem beadásában. Számítógépet és nyomtatót biztosítunk, hozza magával a személyi igazolványát.

Kérdés esetén hívja a **06 1 234 5678** számot munkanapokon 8 és 16 óra között, vagy írjon az **ugyfelszolgalat@kertvarad.hu** címre.

Az elkövetkező hónapokban további ügytípusokat nyitunk meg elektronikusan – elsőként a hatósági bizonyítványokat és a helyi adóügyeket. Az újdonságokról a város honlapján és a Kertváradi Hírmondóban adunk tájékoztatást.

*Kertvárad Város Önkormányzata*
```

## 2. Változástábla

| ID | Eredeti | Új | Indok |
|---|---|---|---|
| HU-T02 | `Lakcímigazolás online — indul` | `Lakcímigazolás online – indul` | em dash helyett szóközös gondolatjel |
| HU-T02 | `az életéből — és nem` | `az életéből – és nem` | em dash helyett szóközös gondolatjel |
| HU-T02 | `a lakcímét — ezeket nem kell` | `a lakcímét – ezeket nem kell` | em dash helyett szóközös gondolatjel |
| HU-T02 | `a portálon — ha ilyen` | `a portálon – ha ilyen` | em dash helyett szóközös gondolatjel |
| HU-T02 | `elektronikusan — elsőként` | `elektronikusan – elsőként` | em dash helyett szóközös gondolatjel |

## 3. Gyanús, de nem javítottam

- **nincs minta** [no-pattern] – `a Önnel egy lakcímen élő kiskorú gyermeke`: a névelő rossz alakja, `az Önnel` lenne. Kétségtelen hiba, de hétköznapi helyesírási típusú, nincs rá minta a katalógusban, és minta-ID nélküli javítást az 1. önellenőrzés visszavonat. Kézzel javítandó.
- **nincs minta** [no-pattern] – `csak írásos meghatalmazással, személyesen intézhető ügy`: elliptikus névszói állítmány, nehézkes. A HU-F13 nem fogja meg (az igenév jelzői helyzetben van), a HU-F01 sem (nincs `-ás/-és` lánc és nincs birtokoslépcső).
- **HU-H01** [register] – `adunk tájékoztatást`: valódi funkcióigés szerkezet (`tájékoztatunk`), de a minta profillistája `informal, neutral` – a `formal` pass-mátrix szerint a Pass 3-ból egyedül a HU-H04 fut, klaszterben. A regiszterkapu zárja.
- **HU-F04** [threshold] – `Egy e-mail-cím`: angolos határozatlan névelő gyanúja, de számnévi olvasata is van („egy darab e-mail-cím”). `SOFT`, és a felsorolás mint bekezdés 2 pontja nem éri el a hármas küszöböt.
- **HU-M09** [pattern-exception] – `Kinek jó ez`, `Mi kell hozzá`, `Mennyibe kerül`: kérdés alakú alcímsorok, a SEO-blog sablon jele. A minta saját `Mikor NE`-je zárja: lakossági tájékoztatóban a kérdés a keresés belépője, tehát funkció.
- **HU-R08** [register] – tíz félkövér kiemelés mondaton belül. A Pass 5 `formal`-ban áll (csak a HU-R09, HU-R10, HU-R11 fut), és a minta magyar-specifikus kivétele is véd: a kiemelések az operatív tényekre esnek (határidő, díjmentesség, elérhetőség), ez fókuszjelölés, nem díszítés.

## 4. Klaszterpontok

| # | Kezdet | Pont | Minták |
|---|---|---|---|
| 1 | `**Kertvárad Város Önkormányzata** tájékoztatja…` | 0 | nincs |
| 2 | `Aki eddig azért vett ki fél napot…` | 0 | nincs |
| 3 | `Az igazolás a saját lakcíméről…` | 0 | nincs |
| 4 | `- **Azonosítás:**…` (a teljes hárompontos felsorolás) | 2 | HU-F04 |
| 5 | `1. Nyissa meg az **ugyintezes.kertvarad.hu**…` (a teljes négypontos felsorolás) | 0 | nincs |
| 6 | `Az elektronikus igazolás **három munkanapon belül**…` | 0 | nincs |
| 7 | `A lakcímigazolás kiadása **díjmentes**…` | 0 | nincs |
| 8 | `A személyes és a papíralapú ügyintézés **megmarad**…` | 0 | nincs |
| 9 | `Aki szeretné az online utat használni…` | 0 | nincs |
| 10 | `Kérdés esetén hívja a **06 1 234 5678**…` | 0 | nincs |
| 11 | `Az elkövetkező hónapokban további ügytípusokat…` | 0 | nincs |
| 12 | `*Kertvárad Város Önkormányzata*` | 0 | nincs |
