# Pass 2a – Fordításnyelv

Ez a legerősebb jelforrás. Egy nyelvi modell a magyar szöveget gyakorlatilag latens angolból
állítja elő, ezért a tükörfordítás jegyei akkor is megjelennek, ha a szöveget senki nem fordította.
Aki magyar LLM-szöveget olvas, jellemzően **ezt** érzi meg, nem a szókincset.

A pass alapelve Klaudy Kinga átváltási műveleteiből jön: **az angol névszóközpontú, a magyar
igeközpontú.** A legtöbb minta ennek az egy különbségnek a részesete.

**Sorrendi megkötés:** ez a pass a lexikai pass (`05-llm-style.md`) **előtt** fut. Ha előbb
cserélnénk szavakat, a mondatszerkezet rögzülne, és nehezebb lenne igésíteni. Fordítva viszont
ez a pass magától elviszi az üres fokozók nagy részét.

---

### HU-F01 · Nominalizáció és birtokoslánc · [SOFT] [AI:eros?] [kern]

Mi ez: egymásra halmozott `-ás/-és` főnevek és `-nak/-nek a` birtokos lépcsők. A gyűjtemény
legnagyobb és legmegbízhatóbb mintája – de éppen ezért a legveszélyesebb is: **egyetlen műveletnek
kell tekinteni**, nem öt külön javításnak, különben halmozottan, agresszíven írja át a mondatot.
Miért írja így a gép: az angol `of`-lánc és a `-tion` főnevesítés szó szerinti útja. Az angolban
a főnévi szerkezet a semleges forma, magyarul az igei.
Jelek: két vagy több `-ás/-és` főnév egy mondatban; `-nak/-nek a` kétszer; `érdekében`,
`megvalósítása`, `biztosítása`, `elősegítése`.
ROSSZ: A projekt sikerességének biztosítása a csapat közötti kommunikáció hatékonyságának
javításán alapul.
JÓ:    A projekt akkor sikerül, ha a csapat jobban kommunikál.
Mikor NE: ha a `-ás/-és` főnév **terminus** (`házkutatás`, `teljesítményértékelés`,
`adatkezelés`), vagy ha a mondat jogi hivatkozás. `legal` profilban ez a minta csak akkor fut,
ha a lánc háromnál hosszabb.
**Mintaszintű szigorítás:** ebből a mintából bekezdésenként legfeljebb **egy** javítás mehet ki –
szigorúbb, mint a `SKILL.md` általános bekezdés-korlátja, és felülírja azt lefelé.

**A terminus-teszt.** A „terminus-e?” kérdés eldöntetlenül hagyva kilövi ezt a mintát minden
olyan szövegen, amely saját fogalmi szótárat épít – pedig ott érne a legtöbbet. Ezért:
a főnév akkor terminus, ha **a szövegen kívül is használják** a szakmában, **vagy** ha a szöveg
első előforduláskor definiálja. Ha egyik sem áll – vagyis a szerző maga találta ki, és nem vezeti
be –, az **nem terminus**, hanem bevezetetlen coinage: ott ne igésíts, hanem add át a
`06-rhythm.md` HU-R09 mintájának, amely a konkrét esetet kéri a szó helyett.
Forrás: Klaudy Kinga: A fordítás elmélete és gyakorlata, grammatikai lesüllyesztés

### HU-F02 · `azt a tényt, hogy` · [FIX] [AI:eros] [kern]

Mi ez: az angol `the fact that` magyarul üres.
Miért írja így a gép: az angol szerkezetnek nincs magyar megfelelője, a modell szóról szóra viszi át.
Jelek: `az a tény, hogy`, `azt a tényt, hogy`, `annak a ténynek`.
ROSSZ: A kutatók dokumentálni tudják azt a tényt, hogy az agy egész életen át változik.
JÓ:    A kutatók ki tudják mutatni, hogy az agy egész életen át változik.
Mikor NE: ha a `tény` valóban szembeállításban áll – `Nem a vélemény érdekel, hanem a tény, hogy
mi történt.` Ott a szó tartalmas.
Forrás: Klaudy Kinga

### HU-F03 · `lehetővé teszi számunkra, hogy` · [SOFT] [AI:eros?] [kern]

Mi ez: az `allows us to / enables` tükörfordítása.
Miért írja így a gép: az angol modális-kauzatív szerkezetnek nincs egyszavas magyar megfelelője,
és a modell a szó szerinti utat választja. Magyarul ugyanez eszközhatározóval vagy `-hat/-het`
képzővel fejeződik ki.
Jelek: `lehetővé teszi`, `biztosítja, hogy`, `képessé tesz arra`, `segít abban, hogy`.
ROSSZ: Ez a megoldás lehetővé teszi számunkra, hogy csökkentsük a költségeket.
JÓ:    Ezzel a megoldással csökkenthetjük a költségeket.
Mikor NE: ha a **lehetőség maga** az állítás lényege – jogosultság, engedély, hozzáférés.
`A licenc lehetővé teszi a kereskedelmi felhasználást.` Itt nem cserélhető.
Forrás: Klaudy Kinga, átváltási műveletek

### HU-F04 · Az `egy` névelő angolos túlhasználata · [SOFT] [AI:eros?] [kern]

Mi ez: az angol `a/an` nem fordul `egy`-gyel. Általános érvényű állításban a magyar névelőtlen
többes számot vagy határozott névelőt használ.
Miért írja így a gép: az angol határozatlan névelő kötelező, a magyar nem – a modell mégis kiteszi.
Jelek: `egy` háromnál többször egy bekezdésben; `egy` elvont főnév előtt.
ROSSZ: Egy parancsikon létrehozása egy egyszerű feladat, és egy fájl másolása is gyorsan megy.
JÓ:    A parancsikonok létrehozása egyszerű feladat, és a fájlok másolása is gyorsan megy.
Mikor NE: ha az `egy` tényleg számnév (`egy hibát találtam, nem kettőt`), vagy ha valódi
határozatlanságot jelöl (`Egy ismerősöm mesélte`). A kötetlen beszélt nyelv is használja
nyomatékosításra – `ez egy remek ötlet`.
Forrás: Klaudy Kinga · Microsoft Hungarian Style Guide

### HU-F05 · Hiányzó határozott névelő · [FIX] [AI:kozepes] [kern]

Mi ez: ahol az angol névelő nélkül áll – márkanév, elvont főnév, általános alany –, a magyarban
ki kell tenni a határozott névelőt.
Miért írja így a gép: az angol névelőtlen szerkezet közvetlenül átjön.
ROSSZ: Outlook használata során ügyeljen a beállításokra; kutatók szerint ez a leggyakoribb hibaforrás.
JÓ:    Az Outlook használata során ügyeljen a beállításokra; a kutatók szerint ez a leggyakoribb hibaforrás.
Mikor NE: címben, címsorban, gombfeliraton, listaelemben – ott a névelő elhagyása a magyar norma is.
Megszólításban sem (`Kedves Kollégák!`).
Forrás: Klaudy Kinga · Microsoft Hungarian Style Guide

### HU-F06 · Fölösleges névmáskitétel · [SOFT] [AI:eros?] [kern]

Mi ez: a magyar pro-drop nyelv. Az `én / mi / ő` és az `az én …-m` csak kontraszt vagy nyomaték
esetén kell; egyébként elég a személyrag és a birtokos személyjel.
Miért írja így a gép: az angolban a névmás kötelező, és a modell megtartja.
Jelek: `én úgy gondolom`, `az én véleményem szerint`, `ő azt mondta`, `a mi csapatunk`.
ROSSZ: Én úgy gondolom, hogy az én véleményem szerint mi meg tudjuk oldani az ő problémáját.
JÓ:    Szerintem meg tudjuk oldani a problémáját.
Mikor NE: **kontrasztban kötelező** – `Én maradok, te mehetsz.` Nyomatékosításnál is
(`Ezt én írtam.`). Ha törlöd, jelentést veszítesz.
Forrás: Klaudy Kinga · É. Kiss Katalin

### HU-F07 · Határozói igenév az `-ing` visszhangjaként · [SOFT] [AI:eros?] [kern]

Mi ez: az angol `-ing` és a participiumos mellékmondat nem `-va/-ve`, `lévén`, `figyelembe véve`
alakban jön át magyarul, hanem önálló tagmondatként (Klaudy: grammatikai felemelés).
Miért írja így a gép: az angol participium tömör, a magyar igenév látszólag megfelel neki – de a
magyar szívesebben bont mondatra.
Jelek: `-va/-ve` a mondat élén; `lévén`; `figyelembe véve`; `így téve lehetővé`.
ROSSZ: A boldogság mindhárom fajtáját megismerve, és így téve lehetővé a teljes életet, a szerző
új utat kínál.
JÓ:    A szerző mindhárom boldogságfajtát bemutatja, és ezzel új utat kínál a teljes élethez.
Mikor NE: **ez nem a HU-B01!** Az állapotjelölő `-va/-ve van` (`be van csukva`) tilos átírni.
Itt csak a mondat élén álló, angol participiumot visszhangzó igenévről van szó. Ha bizonytalan
vagy, hogy melyikkel van dolgod, ne nyúlj hozzá.
Forrás: Klaudy Kinga, grammatikai felemelés

### HU-F08 · Terjengős névutók · [FIX-IF: informal, neutral] [AI:eros] [kern]

Mi ez: a `vonatkozásában / tekintetében / esetében / kapcsán / -t illetően` névutók egyszerű
esetraggal vagy tagmondattal helyettesíthetők.
Miért írja így a gép: az angol prepozíciós szerkezet (`regarding`, `with respect to`,
`in the case of`) kész magyar névutót keres, és a leghosszabbat találja meg.
ROSSZ: A határidők vonatkozásában további egyeztetésre van szükség a fejlesztői csapat esetében.
JÓ:    A határidőkről még egyeztetnünk kell a fejlesztőkkel.
Mikor NE: **`formal` profilban csak klaszterben, `legal`-ban soha** – lásd HU-B19. Jogi és
hivatali szövegben ezek helyénvalók, és a csere regisztertörést okoz, ami rosszabb hiba, mint a
terjengősség.
Forrás: Klaudy Kinga · Lanstyák István (regiszterkorlát)

### HU-F09 · `által` + befejezett melléknévi igenév · [FIX] [AI:kozepes] [kern]

Mi ez: az angol passzívum leggyakoribb rossz magyar megoldása: a befejezett melléknévi igenév
névszói állítmányként, gyakran `által`-lal. Ez az, amit a nyelvművelés „tötő nyelvnek” nevez.
Miért írja így a gép: az angol `was approved by` szerkezetnek szó szerinti utat keres.
Jelek: `a … által … -ott/-ett/-ött`; `-ott` melléknévi igenév állítmányi helyzetben.
ROSSZ: A jelentés a vezetőség által jóváhagyott, a nyugtatók 70–80%-a alvási zavarokra használt.
JÓ:    A jelentést a vezetőség jóváhagyta, a nyugtatók 70–80%-át pedig alvási zavarokra szedik.
Mikor NE: **ez nem a szenvedő szerkezet tiltása.** A `-va/-ve van` (HU-B01) és a `-tatik/-tetik`
(HU-B08) érinthetetlen. Itt kizárólag a befejezett melléknévi igenév **állítmányi** használatáról
van szó – jelzőként teljesen szabályos: `a jóváhagyott jelentés`.
Forrás: Szepesy Gyula (a valódi idegenszerűség elkülönítése) · Klaudy Kinga

### HU-F10 · Szó szerint fordított fordulatok · [SOFT] [AI:eros?] [2026-08]

Mi ez: idiómát és diskurzusjelölőt a jelentése, nem a szavai szerint kell átültetni.
Miért írja így a gép: az angol fordulat gyakori a korpuszban, és a magyar megfelelője nem
szóról szóra épül.
Jelek: `a nap végén`, `amikor arról van szó, hogy`, `nem csupán X, hanem Y is`,
`ez nem X-ről szól, hanem`, `a helyzet az, hogy`, `légy nyugodt`.
ROSSZ: A nap végén, amikor a döntésekről van szó, ez nem csupán a költségről szól, hanem a
határidőről is.
JÓ:    Végső soron a döntésnél nemcsak a költség számít: a határidő is.
Mikor NE: ha a fordulat magyarul is meghonosodott és a szöveg regisztere elbírja. A `végső soron`
és a `nap mint nap` élő magyar; a `nap végén` időhatározóként (`a nap végén hazamentem`) szó
szerinti értelmű, azt ne bántsd.
Forrás: Klaudy Kinga

### HU-F11 · Tükörfordított kollokáció · [SOFT] [AI:eros?] [kern]

Mi ez: a szokatlan szókapcsolat azonnal elárulja a fordítást. A magyarban élő kollokációt kell
megkeresni, nem szavanként fordítani.
Miért írja így a gép: a kollokáció nyelvspecifikus, és a modell a leggyakoribb szópárt választja
szó szinten, nem szerkezet szinten.
Jelek: `boldogság megtörténik`, `döntést csinál`, `figyelmet fizet`, `erős kávé` helyett
`hatalmas kávé`.
ROSSZ: A boldogság akkor történik meg, ha megvan az érzelmi kielégülés.
JÓ:    Akkor vagyunk boldogok, ha érzelmileg is elégedettek vagyunk.
Mikor NE: ha a szokatlan kapcsolat **szándékos** – szépirodalom, reklámszöveg, szójáték. Ott a
meghökkentés a cél.
Forrás: Klaudy Kinga

### HU-F12 · `magas -ú/-ű` típusú jelzős kalk · [SOFT] [AI:kozepes?] [2026-08]

Mi ez: az angol `high-X` szerkezet magyar tükre.
Miért írja így a gép: az angol `high-quality`, `high-intelligence` mintájára képez `-ú/-ű` jelzőt
ott, ahol a magyar melléknevet vagy állítmányt használna.
Jelek: `magas` + elvont főnév + `-ú/-ű`; `kiemelkedő …-ú`.
ROSSZ: A pályázó egy magas intelligenciájú, kiemelkedő motivációjú személy.
JÓ:    A pályázó okos, és nagyon akarja ezt a munkát.
Mikor NE: **fontos korlát.** A `-ú/-ű` képzős jelzős szerkezet ősi és termékeny magyar minta –
`nagy tudású`, `jó szívű`, `nagy tapasztalatú`, `barna hajú`. Ezeket soha ne bántsd. Csak a
`magas / kiemelkedő / alacsony` + elvont főnév kombináció gyanús, és az is csak klaszterben.
Forrás: NKE: MI és az akadémiai szövegalkotás (a `magas intelligenciájú` példa)

### HU-F13 · Igekötős igenév igei alak helyett · [FIX] [AI:kozepes] [kern]

Mi ez: az angol `cannot be determined` típusú szerkezet magyarul nem melléknévi igenév, hanem
`-ható/-hető` igealak.
Miért írja így a gép: az angol passzív-modális szerkezet közvetlen tükre.
ROSSZ: A hely nem meghatározható a rendszer által a megadott adatok alapján.
JÓ:    A megadott adatok alapján nem határozható meg a hely.
Mikor NE: ha az igenév valóban jelzői helyzetben van – `a nem meghatározható tényezők`.
Ez a minta a szórendet is érinti: a magyar az új információt az ige elé vagy a mondat végére
teszi, nem angol SVO-sorrendbe. Lásd `03-grammar.md`, HU-G09.
Forrás: Klaudy Kinga

---

## Amit ez a pass NEM csinál

- **Nem cseréli a visszatérő kulcsszót szinonimára.** Az ellenkezője igaz: a szinonimalánc maga
  a fordításíz. Lásd HU-B13.
- **Nem irtja a szenvedő szerkezetet.** Csak a HU-F09 szűk esetét javítja.
- **Nem bontja mellérendelésre az alárendelést.** Lásd HU-B17.
- **Nem tesz be idiómát oda, ahol nem volt.** Az idiómasűrűség ugyanúgy fordításízt ad, mint a
  hiánya. Ez fordítástudományi megfigyelés, nem a mi mérésünk – lásd `sources.md`.
