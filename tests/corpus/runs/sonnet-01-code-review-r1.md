<!-- stet-run: source=skills/stet-hungarian sha256=22f8a1a7 date=2026-08-17 -->

## 0. Nyelv és regiszter

A szöveg magyar. A regisztert a hívó rögzítette, nem következtetem ki: a szöveget `informal` profil szerint kezelem.

## 1. A javított szöveg

```
---
title: Miért és hogyan tartsunk code review-t
type: guide
status: active
updated: 2026-08-14
---

Szia csapat,

az elmúlt hetekben többször felmerült, hogy a code review sokaknak inkább formalitásnak tűnik, mint valódi értéknek. Szeretném összefoglalni, miért ragaszkodunk hozzá, és hogyan érdemes csinálni, hogy tényleg megérje az időt, amit rááldozunk.

A code review nem a hibavadászatról szól elsősorban. Persze kiszűr néhány bugot commit előtt, de a valódi haszna máshol van. Egyrészt szétteríti a tudást a kódbázisról – ha csak egy ember érti, hogyan működik egy modul, az kockázat, nem érdem. Másrészt konzisztenciát épít: ha mindenki más stílusban ír kódot, a karbantartás lassan pokollá válik. Harmadrészt tanulási alkalom mindkét irányban – a reviewer is tanul az író megoldásából, az író is a reviewer visszajelzéséből.

Néhány alapelv, amit érdemes betartani.

Kis PR-okat nyissunk. Egy 800 soros diffet senki nem néz át rendesen, csak átfut rajta, és rábólint. Ha egy feature túl nagy, bontsuk logikai lépésekre, és külön PR-ban vigyük be őket. Ökölszabályként 200–300 sor fölött már gyanakodjunk.

A PR leírása legyen érdemi. Mit csinál a változás, miért van rá szükség, mit érdemes külön megnézni. Ha a reviewernek magától kell kitalálnia a kontextust, kétszer annyi ideig tart a review, és rosszabb minőségű lesz.

Reviewerként ne csak a szintaxist nézzük. Kérdezzük meg magunktól: érthető ez valakinek, aki fél év múlva nyúl hozzá? Van-e egyszerűbb megoldás? Lefedi-e a teszt a határeseteket? A formázást és az apró stílusbeli kérdéseket hagyjuk a lintre – ne vesszünk el bennük, amikor van fontosabb is.

Kommentben legyünk konkrétak és kedvesek. „Ez nem jó” helyett írjuk le, miért nem jó, és ha lehet, javasoljunk alternatívát. Különbséget érdemes tenni a blokkoló észrevétel és a puszta javaslat között – jelöljük is, hogy melyik melyik, hogy az író tudja, mi a kötelező és mi a nice-to-have.

Íróként ne vegyük személyeskedésnek a visszajelzést. A review a kódról szól, nem rólunk. Ha nem értünk egyet egy észrevétellel, mondjuk el nyugodtan, miért – a vita gyakran jobb megoldáshoz vezet, mint bármelyik eredeti javaslat.

Válaszidőre is figyeljünk. Egy nyitva hagyott PR blokkolja a szerzőt, és lassítja az egész csapatot. Törekedjünk arra, hogy egy napon belül reagáljunk minden nyitott review-ra, még ha csak annyi is a válasz, hogy „később átnézem részletesen”.

Ez nem bürokrácia akar lenni, hanem védőháló. A cél, hogy a kódbázis olyan állapotban maradjon, amiben szívesen dolgozunk hónapok múlva is.

Ha valakinek van javaslata a folyamat finomítására, dobjátok be nyugodtan – ez a leírás sem végleges.
```

## 2. Változástábla

| ID | Eredeti | Új | Indok |
|---|---|---|---|
| HU-T03 | `200-300 sor` | `200–300 sor` | `-tól/-ig` viszonyban nagykötőjel áll, szóköz nélkül tapadva |

## 3. Gyanús, de nem javítottam

- **HU-M07** [pattern-exception] – `Szia csapat,` + kisbetűs folytatás. A magyar levélmegszólítás után felkiáltójel áll, a minta saját kikötése szerint viszont `informal` profilban csak akkor javítandó, ha a szöveg egyébként formális. Ez belső csapatlevél, tehát marad.

- **HU-T11** [pattern-exception] – `csak átfut rajta, és rábólint` – és ugyanez a vessző az `és` előtt még három mondatban (`bontsuk logikai lépésekre, és…`, `kétszer annyi ideig tart a review, és…`, `blokkolja a szerzőt, és…`). Halmozott állítmányként vessző nélkül volna helyes, de mindegyik második állítmánynak saját bővítménye van, tehát tagmondatként is olvasható – ott pedig a vessző kötelező. A rendszeresség inkább szerzői szokásra vall, mint gépi jelre, ezért nem nyúltam hozzá.

- **HU-R03** [pattern-exception] – `Egyrészt… Másrészt… Harmadrészt…`. **Szabály szerint nem javítható:** a három tag nem párhuzamos `-ás/-és` főnév, és a hármasság nem tér vissza bekezdésenként. Ugyanez áll a reviewer-bekezdés három egymás utáni kérdésére.

- **HU-F10** [pattern-exception] – `nem a hibavadászatról szól elsősorban`, az `it's not about X` tükre. A `vmi vmiről szól` fordulat magyarul meghonosodott, és a bekezdés `SOFT` pontszáma a 3-as küszöb alatt maradt: a másik két jelet a saját `Mikor NE`-jük állította meg, tehát nem adnak pontot.

- **HU-L06** [pattern-exception] – négy tagadó szembeállítás a szövegben (`nem a hibavadászatról szól`, `az kockázat, nem érdem`, `A review a kódról szól, nem rólunk`, `Ez nem bürokrácia akar lenni, hanem védőháló`). Egyik sem bukik el a szalmabáb-teszten – az első bekezdés épp azt rögzíti, hogy sokan formalitásnak látják a review-t –, így a klaszter-felülírás nem tüzel, és a szerkezet magyarul egyébként is helyes.

- **HU-H01** [pattern-exception] – `Különbséget érdemes tenni`. Funkcióigés szerkezetnek látszik, de a `különbséget tesz` idiomatikus, és a `megkülönböztet` más vonzatkeretet kíván – HU-B18 szerint hagyni kell.

## 4. Klaszterpontok

| # | Kezdet | Pont | Minták |
|---|---|---|---|
| 1 | `Szia csapat,` | 0 | nincs |
| 2 | `az elmúlt hetekben többször felmerült…` | 0 | nincs |
| 3 | `A code review nem a hibavadászatról szól…` | 0 | nincs |
| 4 | `Néhány alapelv, amit érdemes betartani.` | 0 | nincs |
| 5 | `Kis PR-okat nyissunk…` | 0 | nincs |
| 6 | `A PR leírása legyen érdemi…` | 0 | nincs |
| 7 | `Reviewerként ne csak a szintaxist nézzük…` | 0 | nincs |
| 8 | `Kommentben legyünk konkrétak és kedvesek…` | 0 | nincs |
| 9 | `Íróként ne vegyük személyeskedésnek…` | 0 | nincs |
| 10 | `Válaszidőre is figyeljünk…` | 0 | nincs |
| 11 | `Ez nem bürokrácia akar lenni…` | 0 | nincs |
| 12 | `Ha valakinek van javaslata…` | 0 | nincs |

A front matter nem szerepel a táblázatban: strukturált metaadat, nem bekezdés.
