<!-- stet-run: source=skills/stet-hungarian sha256=22f8a1a7 date=2026-08-17 -->

## 0. Nyelv és regiszter

A szöveg magyar (angol szakszavakkal és egy német betéttel; ezek érinthetetlen zónák). A regisztert
a hívó **rögzítette**: `informal` – nem én állapítottam meg. (A csatorna alapján amúgy is ez adódna:
blogszerű, tegező szöveg.)

## 1. A javított szöveg

```
# Code review – Miért és hogyan?

A code review olyan, mint egy szellemi biztosíték. Nem azért csináljuk, mert nem bízunk a fejlesztőkben, hanem mert tudjuk: mindenki lát meg valamit, amit mások nem, és minden pár szem jobban lát, mint egy.

## Miért szükséges?

A leggyakoribb hiba az önbizalom. Akármilyen tapasztalt vagy, amikor saját kódodon dolgozol, apró buktatók maradhatnak rejtve. Egy fáradt szem másképp olvas végig egy függvényt, mint a fő szerző szempontja. Az első review megtalálja azokat az edge case-eket, amelyeket az eredeti fejlesztő gondolkodásmódjában nem voltak köztudatban.

A biztonság mellett van még néhány szuper gyakorlati előny. A code review során a junior fejlesztők tanulnak a senior kód logikájából és stílusából – nem kell külön oktatás, a valós munka során tanulnak. Az újabb csapattag könnyebben beépül, ha látja az általános elveket. A projekt kódja konzisztenssé válik, mert közösen fenntartják az irányelveket.

## Hogyan csináljuk?

Egy review nem lehetőség a kritika rögzítésére. Az a gondolat hibás. A review konstruktív beszélgetés: „Miért ezt a megközelítést választottad? Van-e rá okod, amit nem értek?”

Az elküldő (a patch szerzője) készüljön fel: írjon rövid leírást, amiben elmondja, mit csinál a módosítás és miért. Minél világosabb, annál gyorsabb a review.

A reviewer olvaszon végig konzentrieren, egyszer vagy kétszer. Ne írjon a kódba beletörődve. Gyűjtse össze a megjegyzéseit, majd írja meg összefüggő formában. Vagy – ha szóban jobb – beszéljen meg DirectMessage-ben vagy szervezzen 15 perces call-t.

Egy jó megjegyzés konkrét, nem pedig vag. Ne azt mondd, hogy „Ez nem szép.” Inkább: „Ez az if-lánc 5 elágazás mélyen jár, nehéz követni. Felraknánk egy guard clauseb?”

## A tárgy

Egy review célja nem a tökéletes kód. A cél a működő, érthető, fenntartható kód, és hogy a csapat közös nyelvén beszéljen. Ha egy megoldás helyes és biztonságos, de nem pont az, ahogy te csinálnád, nem vagyis blokkolni kell.

Ne ragozz kis stílusproblémákon. Ha az eszközöd automatikusan formázza a kódot (prettier, black, stb.), hagyd erre azt – az embereknek nem erről kell vitázni.

## Végül

A code review nem zárógát, nem börtön-orvos, nem a verseny. A csapat közös tulajdona minden sor. Minél gyorsabban és kedvesebbek vagyunk egymással a reviewban, annál jobban működik a folyamat. Egy fejlesztő, akinek sérült a ége a kritikáktól, lehet, hogy fél később biztonságosan felvetni a kérdéseket.

Szóval kezdjünk el. Ha eddig nem csináltatok reviewt, állítsatok be egy alapszintű folyamatot, és lépjetek be. Egy hét múlva már érzitek az előnyöket.
```

## 2. Változástábla

| ID | Eredeti | Új | Indok |
|---|---|---|---|
| HU-T07 | `Code Review` | `Code review` | angolos Title Case magyar címsorban; a törzsszöveg végig kisbetűzi |
| HU-G13 | `Nem azért csinálunk` | `Nem azért csináljuk` | odaértett határozott tárgy mellett tárgyas ragozás kell |
| HU-F09 | `maradhatnak rejtett` | `maradhatnak rejtve` | befejezett melléknévi igenév állítmányi helyzetben; az állapotot a `-va/-ve` alak jelöli |
| HU-T12 | `edge caseeket` | `edge case-eket` | néma `e`-re végződő idegen szó toldaléka kötőjellel kapcsolódik |
| HU-G14 | `megtanulnak a senior kód logikájából` | `tanulnak a senior kód logikájából` | a `megtanul` tárgyas vonzatú; `-ból/-ből` mellett a `tanul` áll |
| HU-T01 | `nem értek?"` | `nem értek?”` | angol záró idézőjel magyar mondatban |
| HU-G01 | `Összegyűjtse a megjegyzéseit` | `Gyűjtse össze a megjegyzéseit` | felszólító főmondatban az igekötő az ige mögé kerül |
| HU-T01 | `„Ez nem szép."` | `„Ez nem szép.”` | angol záró idézőjel magyar mondatban |
| HU-T01 | `guard clauseb?"` | `guard clauseb?”` | angol záró idézőjel magyar mondatban |
| HU-G01 | `és belépjetek` | `és lépjetek be` | felszólító főmondatban az igekötő az ige mögé kerül |

## 3. Gyanús, de nem javítottam

- **HU-L14** [pattern-exception] – `A code review olyan, mint egy szellemi biztosíték.` Idézhetőre
  csiszolt metafora, a LinkedIn-teszt elbukik, és a bekezdésben nincs konkrét eset (szám, dátum,
  név), amire cserélhetném. A minta saját szabálya szerint ilyenkor jelzés a kimenet, nem átírás.
- **HU-F10** [zone] – `minden pár szem jobban lát, mint egy`: a `Több szem többet lát` szólás
  tükörfordított változata. A szólás behelyettesítése a sűrítés-fékbe ütközne – idiómát nem szúrok
  be oda, ahol nem volt. (A bekezdés amúgy sem érné el a küszöböt: a HU-L14 találat blokkolt.)
- **HU-G01** [pattern-exception] – `mindenki lát meg valamit`: igekötő-hátravetés látszólag fókusz
  nélkül. A `mindenki` kvantoros, szembeállító olvasata védhető, és a minta `Mikor NE`-je épp a
  fókuszos esetet zárja ki.
- **HU-R11** [pattern-exception] – `A leggyakoribb hiba az önbizalom.` Elvont névszói állítás, de
  tételmondat, és a bekezdésben van földet érés (`saját kódodon`, `függvényt`, `edge case`) – a
  minta saját `Mikor NE`-je zárja ki.
- **nincs minta** [no-pattern] – `Egy fáradt szem másképp olvas végig egy függvényt, mint a fő
  szerző szempontja.` Az összehasonlítás két oldala nem azonos (`szem` vs. `szempontja`); a javítás
  új tartalmat igényelne.
- **nincs minta** [no-pattern] – `amelyeket az eredeti fejlesztő gondolkodásmódjában nem voltak
  köztudatban`: a vonatkozói mellékmondat egyeztetése és vonzata is hibás, a szándékolt állítás nem
  rekonstruálható.
- **HU-M01** [pattern-exception] – `Az elküldő (a patch szerzője) készüljön fel`: a harmadik
  személyű felszólító alakok (`készüljön`, `olvaszon`, `beszéljen`, `szervezzen`) saját, megnevezett
  alanyt kapnak, tehát nem önözés a tegező szövegben, hanem harmadik személyű leírás. Nincs mit
  egységesíteni.
- **nincs minta** [no-pattern] – `A reviewer olvaszon végig konzentrieren, egyszer vagy kétszer.`
  Az `olvaszon` elmaradt kettőzés – emberi típusú helyesírási hiba, a katalógus hatókörén kívül. A
  `konzentrieren` ráadásul német betét, vagyis érinthetetlen idegen nyelvű szakasz.
- **nincs minta** [no-pattern] – `Ne írjon a kódba beletörődve.` A mondat értelmezhetetlen; a
  `beletörődve` igenévnek nincs mihez kapcsolódnia.
- **nincs minta** [no-pattern] – `Egy jó megjegyzés konkrét, nem pedig vag.` A `vag` csonka szó; a
  kiegészítése találgatás lenne.
- **nincs minta** [no-pattern] – `Felraknánk egy guard clauseb?` A `clauseb` csonka toldalékolás; a
  helyes alak attól függ, mit akart a szerző mondani.
- **HU-R03** [pattern-exception] – `a működő, érthető, fenntartható kód` és `nem zárógát, nem
  börtön-orvos, nem a verseny`: két hármas felsorolás. **Szabály szerint nem javítható:** a tagok
  nem párhuzamos `-ás/-és` főnevek, és a hármasság nem tér vissza bekezdésenként.
- **nincs minta** [no-pattern] – `nem vagyis blokkolni kell`: a `vagyis` itt nem értelmezhető, a
  mondat vége romlott.
- **nincs minta** [no-pattern] – `Ne ragozz kis stílusproblémákon.` A `ragoz` tárgyas ige, `-on/-en`
  vonzattal nem áll; a szándékolt szó valószínűleg más, de ezt nem találhatom ki.
- **nincs minta** [no-pattern] – `hagyd erre azt`: a mutató névmások keverednek, a szerkezet romlott.
- **HU-T10** [pattern-exception] – `börtön-orvos`: kétrészes összetétel fölösleges kötőjellel. A
  minta a **hiányzó** kötőjelet írja elő, a fölöslegeset nem, és a `SKILL.md` kimondja, hogy a
  rosszul kötőjelezett összetétel emberi hibaként szándékosan kicsúszik.
- **HU-L14** [pattern-exception] – `A csapat közös tulajdona minden sor.` Aforizma-formula; a
  bekezdésben nincs konkrét eset, amit a mondat körülírna, ezért a minta nem cserél és nem is töröl.
- **nincs minta** [no-pattern] – `Minél gyorsabban és kedvesebbek vagyunk egymással a reviewban`:
  eltérő szófajú tagok mellérendelése (`gyorsabban` vs. `kedvesebbek`).
- **HU-F11** [threshold] – `biztonságosan felvetni a kérdéseket`: tükörfordított kollokáció
  (`safely raise questions`). A bekezdés 2 ponton áll, a küszöb 3 – ez a szöveg egyetlen olyan
  bekezdése, ahol egyáltalán van élő `SOFT` pont. A magyaros alak (`nem mer majd kérdezni`) amúgy
  is átfogalmazná az állítást.
- **nincs minta** [no-pattern] – `akinek sérült a ége a kritikáktól`: az `ége` csonka szó.
- **nincs minta** [no-pattern] – `Szóval kezdjünk el.` A `kezdjünk el` bővítmény nélkül csonka; a
  `Szóval` diskurzusjelölő viszont maradt (HU-B14).
- **HU-M09** [threshold] – `## Miért szükséges?` és `## Hogyan csináljuk?`: kérdés-alcímes
  blogsablon. `SOFT` minta, de a klaszterkapu bekezdésre számol, a címsor pedig nem bekezdés –
  nincs mire számolni, tehát pontot sem ad.

## 4. Klaszterpontok

| # | Kezdet | Pont | Minták |
|---|---|---|---|
| 1 | `A code review olyan, mint…` | 0 | nincs |
| 2 | `A leggyakoribb hiba az önbizalom…` | 0 | nincs |
| 3 | `A biztonság mellett van még…` | 0 | nincs |
| 4 | `Egy review nem lehetőség…` | 0 | nincs |
| 5 | `Az elküldő (a patch szerzője)…` | 0 | nincs |
| 6 | `A reviewer olvaszon végig…` | 0 | nincs |
| 7 | `Egy jó megjegyzés konkrét…` | 0 | nincs |
| 8 | `Egy review célja nem a tökéletes…` | 0 | nincs |
| 9 | `Ne ragozz kis stílusproblémákon…` | 0 | nincs |
| 10 | `A code review nem zárógát…` | 2 | HU-F11 |
| 11 | `Szóval kezdjünk el…` | 0 | nincs |
