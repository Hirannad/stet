# Pass 2b — Nyelvtan, szórend, fókusz

Ez a réteg a legmagyarabb, és a gépi szöveg itt csúszik meg a legláthatatlanabbul: a mondat
nyelvtanilag hibátlan lehet, mégis „lapos”, mert elveszett a fókuszjelölés, vagy mert az igeidő
és az aspektus angol logikát követ.

**Óvatosság.** Több minta itt jelentést változtat, ha rosszul alkalmazod. Ahol `[jelöld]` áll, ott
az eszköz **nem javít, csak jelez** — kiírja a „gyanús, de nem javítottam” listára.

---

## Fókusz és szórend

### HU-G01 · Igekötő-inverzió fókusz mellett · [FIX] [AI:kozepes] [kern]

Mi ez: ha fókusz áll az ige előtt, az igekötő az ige **mögé** kerül.
Miért írja így a gép: az angolban a hangsúly intonációval jelölődik, a magyarban szórenddel — a
modell a semleges alakot hagyja ott.
ROSSZ: A hibát a junior fejlesztő megtalálta, nem a senior.
JÓ:    A hibát a junior fejlesztő találta meg, nem a senior.
Mikor NE: ha nincs fókusz, az igekötő az igén marad (`Megtaláltuk a hibát.`). Tagadásban is
inverzió van (`nem találta meg`).
Forrás: É. Kiss Katalin: A magyar mondatszerkezet

### HU-G02 · A `nem` pozíciója · [FIX] [AI:eros] [kern]

Mi ez: ha egy **elemet** tagadsz, a `nem` közvetlenül az elé kerül, nem az ige elé.
ROSSZ: A megbeszélésen nem döntöttünk a költségvetésről, hanem az ütemezésről.
JÓ:    A megbeszélésen nem a költségvetésről döntöttünk, hanem az ütemezésről.
Mikor NE: ha az egész állítást tagadod, a `nem` az ige elé való (`Nem döntöttünk.`). A `hanem`
jelenléte a legjobb jel: ha van, az elemet tagadod.
Forrás: É. Kiss Katalin

### HU-G03 · Tagadásban `is` helyett `sem` · [FIX] [AI:kozepes] [kern]

Mi ez: ha az `is`-es elem hatóköre nagyobb a tagadásnál, `sem/se` lép a helyébe, és a `nem` eltűnik.
ROSSZ: A tesztek is nem futottak le a második környezetben.
JÓ:    A tesztek sem futottak le a második környezetben.
Mikor NE: ha a tagadás hatóköre nagyobb (`Az is nem baj, hanem katasztrófa` — ritka, de létezik).
Forrás: É. Kiss Katalin: Tagadás

### HU-G04 · Az `is` partikula helye · [SOFT] [jelöld] [AI:kozepes?] [kern]

Mi ez: az `is` közvetlenül az után az elem után áll, amelyre vonatkozik.
ROSSZ: Ez is azt jelenti, hogy a becslésünk túl optimista volt.
JÓ:    Ez azt is jelenti, hogy a becslésünk túl optimista volt.
Mikor NE: **soha ne mozgasd automatikusan.** Az `is` áthelyezése **jelentést változtat**, és a
fenti ROSSZ mondat tökéletes, ha az `ez` egy felsorolás újabb eleme. Ez a minta csak jelzésre való:
írd ki a listára, és bízd a szerzőre.
Forrás: É. Kiss Katalin

### HU-G05 · Elveszett kontrasztív topik · [SOFT] [AI:eros?] [kern]

Mi ez: szembeállításnál a szembeállított elem a mondat élére kerül; a magyar ezt szórenddel oldja
meg, nem kötőszóval és ismétléssel.
ROSSZ: Nem tudok jól prezentálni, de jól tudok írni.
JÓ:    Prezentálni nem tudok, írni viszont igen.
Mikor NE: ha nincs valódi szembeállítás, csak két egymás melletti állítás.
Forrás: É. Kiss Katalin

### HU-G06 · Topik–komment sorrend · [SOFT] [AI:kozepes?] [kern]

Mi ez: a magyar mondat az ismert elemmel kezd, és az újat viszi az ige elé vagy a mondat végére.
A gépi szöveg angol SVO-sorrendet tart, és ettől lesz „lapos”.
ROSSZ: A vállalat bejelentette a döntést hétfőn a sajtótájékoztatón.
JÓ:    A vállalat hétfőn, a sajtótájékoztatón jelentette be a döntést.
Mikor NE: **fontos korlát.** A semleges magyar mondatban az ige utáni bővítménysor teljesen
szabályos, és a sorrendjük szabad — önmagában az, hogy valami az ige után áll, nem hiba. Ez a
minta csak akkor fut, ha a mondatban van azonosító fókusz, ami elveszett. Klaszterben, egyesével.
Forrás: É. Kiss Katalin · Anyanyelv-pedagógia: Topik? Fókusz?

## Igeidő, igemód, aspektus

### HU-G07 · Igeidő-egyeztetés a függő beszédben · [FIX] [AI:kozepes] [kern]

Mi ez: a magyar mellékmondat igeideje a **közléshez** igazodik, nem a főmondatéhoz. Nincs backshift.
Miért írja így a gép: az angol `said that he was` kötelező egyeztetését hozza át.
ROSSZ: Azt mondta, hogy beteg volt, ezért nem jött el. (ha most is beteg)
JÓ:    Azt mondta, hogy beteg, ezért nem jött el.
Mikor NE: ha a mellékmondat eseménye tényleg korábbi a főmondaténál, akkor a múlt idő helyes.
Forrás: Keszler Borbála: Magyar grammatika

### HU-G08 · `fog` a `will` tükreként · [SOFT] [AI:eros?] [kern]

Mi ez: a magyar jövő időt jellemzően jelen idővel és időhatározóval, vagy igekötős befejezett
alakkal fejezi ki. A `fog` segédige jóval ritkább, mint az angol `will`.
ROSSZ: A csapat jövő héten el fogja készíteni a jelentést, és be fogja mutatni a vezetőségnek.
JÓ:    A csapat jövő héten elkészíti a jelentést, és bemutatja a vezetőségnek.
Mikor NE: ha a jövőre utalás hangsúlyos vagy ígéret értékű (`Meg fogom csinálni.`), illetve ha a
jelen idő félreérthető lenne.
Forrás: e-nyelv.hu · Kiefer Ferenc

### HU-G09 · Feltételes mód tükrözése · [SOFT] [AI:eros?] [kern]

Mi ez: az angol `would / could / should` udvariassági és hipotetikus használata nem mindig
feltételes módú magyarul. A tényszerű állítás ne legyen feltételesben.
ROSSZ: Ez a megoldás csökkentené a költségeket, és javítaná a teljesítményt. (ha ez tény)
JÓ:    Ez a megoldás csökkenti a költségeket, és javítja a teljesítményt.
Mellékszabály: múlt idejű feltételesben a `volna` a helyes (`megtettem volna`), a `lenne` jelen
idejű. A `meg lettem volna` típusú keveredés hiba.
Mikor NE: valódi feltétel, udvarias kérés, óvatos állítás — ott a feltételes helyénvaló.
Forrás: Keszler Borbála · e-nyelv.hu

### HU-G10 · Főnévi igenév felszólító mellékmondat helyett · [SOFT] [AI:eros?] [kern]

Mi ez: akarást, kérést, javaslatot kifejező ige után a magyar `hogy` + felszólító módot használ,
nem főnévi igenevet.
Miért írja így a gép: az angol `I suggest reviewing / I ask you to check` szerkezetet tükrözi.
ROSSZ: Javaslom átnézni a szerződést, és kérem visszaigazolni a határidőt.
JÓ:    Javaslom, hogy nézzük át a szerződést, és kérem, hogy igazolja vissza a határidőt.
Mikor NE: ha az alany azonos és a szerkezet rövid (`Szeretnék elmenni.`) — ott a főnévi igenév a
természetes.
Forrás: Keszler Borbála: Magyar grammatika

### HU-G11 · Igekötő és befejezettség · [FIX] [AI:kozepes] [kern]

Mi ez: ha az esemény lezárult vagy eredményes, a magyar kiteszi a perfektiváló igekötőt. Az
igekötő hiánya folyamatosságot vagy eredménytelenséget jelöl — ez **jelentéskülönbség**, nem stílus.
Miért írja így a gép: az angolban az aspektust az igeidő hordozza, nem a szó alakja.
ROSSZ: Tegnap írtam a jelentést, és küldtem a vezetőnek.
JÓ:    Tegnap megírtam a jelentést, és elküldtem a vezetőnek.
Mikor NE: ha tényleg folyamatos (`Tegnap egész nap a jelentést írtam.`), vagy ha fókusz áll az ige
előtt — akkor az igekötő hátra kerül, de nem tűnik el (HU-G01).
Forrás: Kiefer Ferenc: Aspektus és akcióminőség

## Egyeztetés és vonzat

### HU-G12 · Számbeli egyeztetés · [FIX] [AI:kozepes] [kern]

Mi ez: két külön szabály, mindkettő az angolból romlik el.
**Mennyiségjelző után egyes szám:** számnév, `sok`, `több`, `néhány`, `minden` után a főnév egyes
számban áll.
**Elvont főnév nem többesül:** a magyar az elvont és gyűjtő jelentésű főnevet egyes számban
használja ott, ahol az angol többest tesz.
ROSSZ: Sok fejlesztők dolgoztak rajta, és több információkat gyűjtöttünk a kockázatokról.
JÓ:    Sok fejlesztő dolgozott rajta, és több információt gyűjtöttünk a kockázatokról.
Mikor NE: ha a többes szám valódi, elkülönülő példányokra utal (`a kockázatok`, ha felsorolható
tételekről van szó). Az `információk` létező alak, csak ritkább.
Forrás: Keszler Borbála · e-nyelv.hu

### HU-G13 · Alanyi és tárgyas ragozás · [FIX] [AI:kozepes] [kern]

Mi ez: határozott tárgy (névelős főnév, birtokos személyjeles alak, tulajdonnév, `azt`) mellett
tárgyas ragozás kell; határozatlan tárgy mellett alanyi.
Miért írja így a gép: az angolban nincs ilyen megkülönböztetés, és a modell néha eltalálja, néha nem.
ROSSZ: Látok a jelentést, és olvasom egy könyvet.
JÓ:    Látom a jelentést, és olvasok egy könyvet.
Mikor NE: nincs kivétel. Ez mindig hiba.
Forrás: Keszler Borbála: Magyar grammatika

### HU-G14 · Vonzatkeret-anglicizmus · [FIX] [AI:kozepes] [kern]

Mi ez: az ige és a melléknév magyar esetragos vonzata nem azonos az angol prepozícióval.
Jelek: `függ -tól/-től` (nem `-on`), `felel -ért` (nem `-ra`), `koncentrál -ra` (nem `-on`),
`hatással van -ra`, `képes -ra/-re`, `alkalmas -ra/-re`, `érdeklődik -ról/-ről` és `iránt`.
ROSSZ: A döntés függ a költségvetésen, és a csapat felelős a határidőre.
JÓ:    A döntés függ a költségvetéstől, és a csapat felelős a határidőért.
Mikor NE: ha az ige több vonzatot is enged, eltérő jelentéssel (`gondol rá` / `gondol róla`).
Forrás: e-nyelv.hu vonzatkérdések · Magyar grammatika

### HU-G15 · A `-e` kérdő szócska · [FIX] [AI:kozepes] [kern]

Mi ez: eldöntendő kérdést tartalmazó mellékmondatban a `-e` kötelező, és mindig a **ragozott
igéhez** tapad, kötőjellel.
Miért írja így a gép: az angol `whether/if` szerkezetnek nincs magyar szórendi megfelelője.
ROSSZ: Nem tudom, hogy a jelentés elkészült, és megkérdezem, hogy jön-e ő is vagy nem.
JÓ:    Nem tudom, hogy elkészült-e a jelentés, és megkérdezem, hogy eljön-e.
Mikor NE: kiegészítendő kérdésben (`Nem tudom, mikor jön`) nem kell `-e`. Az élőbeszédben
előfordul a `hogy … vajon` — azt hagyd.
Forrás: AkH. 12. · Keszler Borbála

## Mondatszerkezet

### HU-G16 · `hogy`-halmozás · [SOFT] [AI:kozepes?] [kern]

Mi ez: egy mondatban egy-két `hogy` elég; a többit bontsd önálló mondatra vagy igeneves szerkezetre.
ROSSZ: Azt mondta, hogy úgy gondolja, hogy jó lenne, hogy ha minél előbb elkezdenénk a tervezést.
JÓ:    Azt mondta, szerinte jó lenne minél előbb elkezdeni a tervezést.
Mikor NE: **ez nem az alárendelés kerülése** (HU-B17). Csak a háromszoros és afölötti egymásba
ágyazásról van szó. Kettő `hogy` egy mondatban teljesen rendben.
Forrás: e-nyelv.hu

### HU-G17 · Utalószó · [SOFT] [AI:kozepes?] [kern]

Mi ez: két irány, és mindkettő óvatosan.
Határozói vonzatú ige mellett az utalószó (`benne`, `arra`, `abban`) **jellemzően** kell:
`bízik benne, hogy`. Ugyanakkor az `Az a tény, hogy…` típusú körülírás helyett majdnem mindig
van egyszerűbb mondat.
ROSSZ: Az a tény, hogy a határidő módosult, azt eredményezte, hogy újra kell terveznünk.
JÓ:    Módosult a határidő, ezért újra kell terveznünk.
Mikor NE: az utalószó elhagyhatósága igénként változik, és a `Bízom, hogy sikerül` típus is
adatolt a sztenderdben. Ne kényszerítsd ki egyik irányt sem — csak a nyilvánvalóan terjengős
`az a tény, hogy … azt eredményezte, hogy` láncot bontsd.
Forrás: Keszler Borbála · e-nyelv.hu

### HU-G18 · Birtokoslánc és a `-nak/-nek` · [SOFT] [AI:eros?] [kern]

Mi ez: kettőnél több tagú birtokoslánc helyett bontsd fel a szerkezetet. A `-nak/-nek` ragot elég
egyszer kitenni, a lánc elején vagy végén.
ROSSZ: A kerületi önkormányzatnak az oktatási bizottságának az elnökének a beszéde elmaradt.
JÓ:    Elmaradt a kerületi önkormányzat oktatási bizottsága elnökének a beszéde.
Mikor NE: a többszörös `-nak/-nek` nem agrammatikus, csak nehézkes — stílusajánlás, nem szabály.
Ne javítsd `legal` profilban, és ne halmozd a HU-F01-gyel: **a kettő együtt egy művelet.**
Forrás: Nyelvművelő kéziszótár · e-nyelv.hu: Birtokos jelző

### HU-G19 · Vessző `illetve`, `valamint`, `továbbá` előtt · [FIX] [AI:gyenge] [kern]

Mi ez: e három kötőszó elé **mindig** vessző kell — felsorolásban is, tagmondatok között is.
Ez az ellentéte az `és` szabályának (HU-T11).
ROSSZ: Kérjük a nevét valamint az e-mail-címét, továbbá a telefonszámát.
JÓ:    Kérjük a nevét, valamint az e-mail-címét, továbbá a telefonszámát.
Mikor NE: nincs kivétel.
Forrás: AkH. 12. 243.

### HU-G20 · `illetve` és `ugyanakkor` pontatlansága · [SOFT] [jelöld] [AI:kozepes?] [2026-08]

Mi ez: az `illetve` háromértelmű (`vagy`, `és`, pontosítás), az `ugyanakkor` pedig egyszerre
jelölhet egyidejűséget és ellentétet. A gépi szöveg mindkettőt túlhasználja, mert semlegesnek
„érzi” őket.
ROSSZ: A jelentést a vezető, illetve a helyettese írja alá. Az elemzés kész, ugyanakkor a
bevezetés csúszik, ugyanakkor jövőre újra megpróbáljuk.
JÓ:    A jelentést a vezető vagy a helyettese írja alá. Az elemzés kész, a bevezetés viszont
csúszik. Jövőre újra megpróbáljuk.
Mikor NE: **egyik szó sem hibás.** Az `ugyanakkor` ellentétes használata régóta adatolt és
szótározott, az `illetve` tág használatát a források nem hibáztatják, csak a többértelműségére
figyelmeztetnek. Ezért: `informal`/`neutral` profilban javítható, ha **ismétlődik**;
`legal` profilban csak jelöld, mert ott a pontosság kérdése a szerzőé.
Forrás: e-nyelv.hu · A magyar nyelv nagyszótára

---

## Precedencia

- HU-G18 és HU-F01 **egy művelet**. Ne alkalmazd mindkettőt ugyanarra a mondatra.
- HU-G16 nem HU-B17. Az alárendelés elvi kerülése tilos; a háromszoros `hogy`-lánc bontása nem az.
- HU-G04 és HU-G20 `[jelöld]`: soha ne írja át magától.
- A mondatkezdő `azonban` kérdésében HU-B03 nyer — nincs tiltás.
