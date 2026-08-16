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

- **HU-L14** – `A code review olyan, mint egy szellemi biztosíték.` Idézhetőre csiszolt metafora, a
  LinkedIn-teszt elbukik, és a bekezdésben nincs konkrét eset (szám, dátum, név), amire cserélhetném.
  A minta saját szabálya szerint ilyenkor jelzés a kimenet, nem átírás.
- **HU-F10** – `minden pár szem jobban lát, mint egy`: a `Több szem többet lát` szólás tükörfordított
  változata. A bekezdés `SOFT` pontösszege nem éri el a küszöböt – a HU-L14 találat blokkolt, tehát
  nem ad pontot –, a szólás behelyettesítése pedig a sűrítés-fékbe ütközne.
- **HU-G01** – `mindenki lát meg valamit`: igekötő-hátravetés látszólag fókusz nélkül. A `mindenki`
  kvantoros, szembeállító olvasata védhető, ezért nem nyúltam hozzá.
- **HU-R11** – `A leggyakoribb hiba az önbizalom.` Elvont névszói állítás, de tételmondat, és a
  bekezdésben van földet érés (`saját kódodon`, `függvényt`, `edge case`) – a minta saját `Mikor NE`-je
  zárja ki.
- **nincs minta** – `Egy fáradt szem másképp olvas végig egy függvényt, mint a fő szerző szempontja.`
  Az összehasonlítás két oldala nem azonos (`szem` vs. `szempontja`); a javítás új tartalmat igényelne.
- **nincs minta** – `amelyeket az eredeti fejlesztő gondolkodásmódjában nem voltak köztudatban`: a
  vonatkozói mellékmondat egyeztetése és vonzata is hibás, a szándékolt állítás nem rekonstruálható.
- **HU-M01** – `Az elküldő (a patch szerzője) készüljön fel`: a harmadik személyű felszólító alakok
  (`készüljön`, `olvaszon`, `beszéljen`, `szervezzen`) saját, megnevezett alanyt kapnak, tehát nem
  önözés a tegező szövegben, hanem harmadik személyű leírás. Nincs mit egységesíteni.
- **nincs minta** – `A reviewer olvaszon végig konzentrieren, egyszer vagy kétszer.` Az `olvaszon`
  elmaradt kettőzés – emberi típusú helyesírási hiba, a katalógus hatókörén kívül –, a `konzentrieren`
  pedig német betét, vagyis érinthetetlen idegen nyelvű szakasz.
- **nincs minta** – `Ne írjon a kódba beletörődve.` A mondat értelmezhetetlen; a `beletörődve`
  igenévnek nincs mihez kapcsolódnia.
- **nincs minta** – `Egy jó megjegyzés konkrét, nem pedig vag.` A `vag` csonka szó; a kiegészítése
  találgatás lenne.
- **nincs minta** – `Felraknánk egy guard clauseb?` A `clauseb` csonka toldalékolás; a helyes alak
  attól függ, mit akart a szerző mondani.
- **HU-R03** – `a működő, érthető, fenntartható kód` és `nem zárógát, nem börtön-orvos, nem a verseny`:
  két hármas felsorolás. **Szabály szerint nem javítható:** a tagok nem párhuzamos `-ás/-és` főnevek,
  és a hármasság nem tér vissza bekezdésenként.
- **nincs minta** – `nem vagyis blokkolni kell`: a `vagyis` itt nem értelmezhető, a mondat vége romlott.
- **nincs minta** – `Ne ragozz kis stílusproblémákon.` A `ragoz` tárgyas ige, `-on/-en` vonzattal nem
  áll; a szándékolt szó valószínűleg más, de ezt nem találhatom ki.
- **nincs minta** – `hagyd erre azt`: a mutató névmások keverednek, a szerkezet romlott.
- **HU-T10** – `börtön-orvos`: kétrészes összetétel fölösleges kötőjellel. A minta a **hiányzó**
  kötőjelet írja elő, a fölöslegeset nem, és a `SKILL.md` kimondja, hogy a rosszul kötőjelezett
  összetétel emberi hibaként szándékosan kicsúszik.
- **HU-L14** – `A csapat közös tulajdona minden sor.` Aforizma-formula; a bekezdésben nincs konkrét
  eset, amit a mondat körülírna, ezért a minta nem cserél és nem is töröl.
- **nincs minta** – `Minél gyorsabban és kedvesebbek vagyunk egymással a reviewban`: eltérő szófajú
  tagok mellérendelése (`gyorsabban` vs. `kedvesebbek`).
- **HU-F11** – `biztonságosan felvetni a kérdéseket`: tükörfordított kollokáció (`safely raise
  questions`). A bekezdés nem éri el a klaszterküszöböt, a magyaros alak pedig (`nem mer majd kérdezni`)
  átfogalmazná az állítást.
- **nincs minta** – `akinek sérült a ége a kritikáktól`: az `ége` csonka szó.
- **nincs minta** – `Szóval kezdjünk el.` A `kezdjünk el` bővítmény nélkül csonka; a `Szóval`
  diskurzusjelölő viszont maradt (HU-B14).
- **HU-M09** – `## Miért szükséges?` és `## Hogyan csináljuk?`: kérdés-alcímes blogsablon. `SOFT`
  minta, de a klaszterkapu bekezdésre számol, a címsor pedig nem bekezdés – nem tudok rálépni.
