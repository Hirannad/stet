<!-- stet-run: source=skills/stet-hungarian sha256=22f8a1a7 date=2026-08-17 -->

## 0. Nyelv és regiszter

A szöveg magyar. A szöveget `informal` regiszterként kezelem, és ezt a hívó rögzítette – nem én vezettem le. (A szöveg egyébként megfelel ennek: blogbejegyzés, végig tegező, belső csapathang.)

## 1. A javított szöveg

```
# Code review: miért és hogyan

Az elmúlt hónapokban kétféle review-t láttam nálunk. Az egyikben a PR három napig áll, aztán valaki átfutja és megnyomja az approve-ot. A másikban negyven komment megy egy változónévről, a szerző pedig este tizenegykor még mindig javít. Egyik sem működik, és mindkettőnek ugyanaz az oka: nincs kimondva, mire való a review.

Kezdjük a haszonnal. A hibakeresés csak a második helyen áll. A leghasznosabb dolog, amit a review ad, az a tudás szétterítése. Ha egy funkciót egyetlen ember írt meg és egyetlen ember érti, akkor az a funkció a szabadságáig működik. A review az egyetlen rendszeres alkalom, amikor valaki más is végigolvassa a kódot még azelőtt, hogy egy hajnali riasztás kényszerítené rá.

A második haszon a döntések nyoma. A PR alatti beszélgetés megmarad, és félév múlva a „miért pont így oldottuk meg?” kérdésre nem találgatás lesz a válasz. A hibák megtalálása is benne van a pakliban, de legyünk őszinték: a súlyos hibákat inkább a tesztek és a staging fogják ki. A review máshol erős – a szándék szintjén. Rossz absztrakció, félreértett követelmény, olyan eset, amire senki nem gondolt.

Innen jön a hogyan.

**A leírást olvasd először.** Ha a PR nem mondja meg, mit akar és miért, azt kérd, ne a kódot kommenteld. Három sor „mit és miért” több időt spórol, mint bármelyik review-checklist.

**Nagy PR-t ne fogadj el.** Ötszáz sor fölött elfogy az emberi figyelem, és onnantól már csak formázást veszünk észre. Ha mégis nagy jött, kérd szét. Ez nem sértés, hanem a review működésének feltétele.

**Válaszd külön a blokkolót a véleménytől.** Mostantól: „blokkoló:” előtag, ha nélküle nem mehet ki, „ötlet:”, ha csak felvetés. A szerző így tudja, mire kell reagálnia, és mire nem.

**Kérdezz, ne rendelkezz.** A „miért itt kezeljük a hibát?” gyakran kiderít valamit, amit a „tedd lejjebb” elfedett volna. Néha a szerzőnek van igaza, és ez így van rendben.

**Huszonnégy órán belül nézz rá.** Nem azért, mert a határidő szent, hanem mert egy álló PR mögött egy álló ember van, aki közben belekezd egy másik szálba, és a kettő össze fog ütni.

**Apróságokat ne kézzel kommentelj.** Ha formázáson vagy importsorrenden múlik, az a linter dolga. Aki ilyet ír bele, az a review idejét használja el olyanra, amit egy szkript ingyen megcsinál.

Egy dolgot még tegyünk hozzá, mert ezen szokott elcsúszni a hangulat: a review a kódról szól, nem a szerzőről. „Ez a függvény két dolgot csinál” és „te összekevered a felelősségeket” ugyanarra a problémára mutat, csak az egyikre lehet válaszolni.

Végül: az approve nem szívesség, és nem is vérrel írt aláírás. Azt jelenti, hogy elolvastam, értem és vállalom, hogy holnap akár én is javíthatom.
```

## 2. Változástábla

| ID | Eredeti | Új | Indok |
|---|---|---|---|
| HU-T11 | `miért, és hogyan` | `miért és hogyan` | azonos szerepű mondatrészek közt nincs vessző az `és` előtt |
| HU-T01 | `„miért pont így oldottuk meg?"` | `„miért pont így oldottuk meg?”` | angol záró idézőjel magyar mondatban |
| HU-T02 | `erős — a szándék` | `erős – a szándék` | em dash helyett szóközös gondolatjel |
| HU-T01 | `„mit és miért"` | `„mit és miért”` | angol záró idézőjel magyar mondatban |
| HU-T01 | `„blokkoló:"`, `„ötlet:"` | `„blokkoló:”`, `„ötlet:”` | angol záró idézőjel magyar mondatban |
| HU-T01 | `„miért itt kezeljük a hibát?"`, `„tedd lejjebb"` | `„miért itt kezeljük a hibát?”`, `„tedd lejjebb”` | angol záró idézőjel magyar mondatban |
| HU-T01 | `„Ez a függvény két dolgot csinál"`, `„te összekevered a felelősségeket"` | `„Ez a függvény két dolgot csinál”`, `„te összekevered a felelősségeket”` | angol záró idézőjel magyar mondatban |
| HU-T11 | `elolvastam, értem, és vállalom` | `elolvastam, értem és vállalom` | halmozott állítmány közös alannyal: nincs vessző az `és` előtt |

## 3. Gyanús, de nem javítottam

- **HU-L14** [pattern-exception] – `a review a kódról szól, nem a szerzőről`: szimmetrikus, kiemelhető mondat, de közvetlenül mellette ott a konkrét példapár, tehát a minta saját `Mikor NE`-je (indoklás, nem ál-bölcsesség) blokkolja, és a bekezdésben van konkrétum, így a klaszter-felülírás sem tüzel.
- **HU-R11** [threshold] – `A review máshol erős`: elvont alany + mérhetetlen melléknév, a második alak. A rá következő töredék (`Rossz absztrakció, félreértett követelmény…`) és a bekezdés konkrétumai kizárják a felülírást, a küszöböt pedig nem éri el.
- **HU-L06** [pattern-exception] – `Ez nem sértés, hanem a review működésének feltétele`: negatív párhuzam, de a szalmabáb-teszten átmegy (a sértettség valós reakció, amit a szerző megelőz), és bekezdésenként csak egy ilyen keret áll.
- **HU-R02** [pattern-exception] – a hat félkövér vezérmondatos bekezdés egyforma sémára épül. `informal` blogban a listaszerű tagolás műfaji elem, a bekezdéshosszak egyenetlenek (van egymondatos bekezdés is), és egyik érintett bekezdés sem éri el a klaszterküszöböt.
- **HU-T11** [uncertain] – `mire kell reagálnia, és mire nem`: közös alanyú, mellérendelt mellékmondatpár, tehát alakilag ugyanaz az eset, mint a két javított vessző. Itt viszont polaritásváltás és ellipszis van (`és mire nem` = `és mire nem kell reagálnia`), ami szünetet indokol, ezért nem nyúltam hozzá.
- **HU-T11** [uncertain] – `az approve nem szívesség, és nem is vérrel írt aláírás`: közös alanyú halmozott névszói állítmány, de nyomatékos tagadó halmozás (`és nem is`), ahol a vessző bevett. Ugyanaz a bizonytalanság, ugyanaz a döntés.
- **nincs minta** [no-pattern] – `félév múlva`: itt fél évről van szó, tehát külön írandó. Hétköznapi helyesírási hiba, nem gépi jel; a katalógus hatókörén kívül esik, ezért nem javítottam.

## 4. Klaszterpontok

| # | Kezdet | Pont | Minták |
|---|---|---|---|
| 1 | `Az elmúlt hónapokban kétféle review-t…` | 0 | nincs |
| 2 | `Kezdjük a haszonnal…` | 0 | nincs |
| 3 | `A második haszon a döntések nyoma…` | 2 | HU-R11 |
| 4 | `Innen jön a hogyan.` | 0 | nincs |
| 5 | `**A leírást olvasd először.**…` | 0 | nincs |
| 6 | `**Nagy PR-t ne fogadj el.**…` | 0 | nincs |
| 7 | `**Válaszd külön a blokkolót…**` | 0 | nincs |
| 8 | `**Kérdezz, ne rendelkezz.**…` | 0 | nincs |
| 9 | `**Huszonnégy órán belül nézz rá.**…` | 0 | nincs |
| 10 | `**Apróságokat ne kézzel kommentelj.**…` | 0 | nincs |
| 11 | `Egy dolgot még tegyünk hozzá…` | 0 | nincs |
| 12 | `Végül: az approve nem szívesség…` | 0 | nincs |
