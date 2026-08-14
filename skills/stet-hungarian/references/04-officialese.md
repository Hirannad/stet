# Pass 3 — Hivataloskodás

Ez a pass **teljes egészében regiszterkapun át fut.** A hivatali nyelv nem önmagában hiba: jogi,
szerződéses és hatósági szövegben a formális névszói szerkezet helyénvaló, és a „közérthetőre”
cserélés ott jelentést és joghatást veszít.

A profilonkénti kapu a `registers.md` mátrixában áll — itt szándékosan nem ismételjük meg.
Amit itt tudni kell: `legal` profilban ez a pass **nem fut**.

**Precedencia mindenek fölött:** a HU-H08 és a HU-H10 nem javítóminta, hanem őr. Ezek akkor is
érvényesek, amikor a pass egyébként áll — épp ők azok, amik leállítják. Ha bizonytalan vagy, hogy
egy szerkezet a regiszter része-e, ne nyúlj hozzá.

**Átfedés más passokkal.** Az `-ás/-és` főnevesítést és a birtokosláncot a HU-F01 kezeli, a
névutókat (`vonatkozásában`, `tekintetében`) a HU-F08. Itt ne javítsd őket újra — a halmozott
alkalmazás agresszív átírást okoz.

---

### HU-H01 · Funkcióigés szerkezet · [FIX-IF: informal, neutral] [AI:eros] [kern]

Mi ez: kiüresedett ige + `-ás/-és` főnév ott, ahol létezik azonos vonzatú tartalmas ige.
Miért írja így a gép: a hivatali korpusz tele van vele, és a modell formálisnak, tehát
„megfelelőnek” érzi.
Jelek: `döntést hoz`, `intézkedést foganatosít`, `ellenőrzést gyakorol`, `javítást végez`,
`vizsgálatot folytat`, `eszközöl`, `bonyolít`.
ROSSZ: A hatóság a helyszínen ellenőrzést gyakorolt, és intézkedést foganatosított.
JÓ:    A hatóság a helyszínen ellenőrzött és intézkedett.
Mikor NE: **HU-B18.** Az idiomatikus szerkezeteket (`köszönetet mond`, `zajt csap`, `zokon vesz`)
és azokat, amelyeknek a főnévi tagja definiált szakszó (`házkutatást tart`, `magánindítványt tesz`),
soha ne rövidítsd. Ha nem tudod eldönteni, idiomatikus-e, hagyd.
Forrás: Nyelvművelő kéziszótár · Minya Károly, e-nyelvmagazin.hu

### HU-H02 · `-ásra/-ésre kerül` · [FIX-IF: informal, neutral] [AI:kozepes] [kern]

Mi ez: a szenvedőpótló `kerül` szerkezet. A magyar erre általános alanyú T/3-at vagy megnevezett
cselekvőt használ.
Miért írja így a gép: az angol passzívumnak keres személytelen magyar megfelelőt, és ezt találja.
Jelek: `elfogadásra kerül`, `megrendezésre kerül`, `beszerzésre kerül`, `kifizetésre kerül`.
ROSSZ: A díjátadó ünnepség június 5-én megrendezésre kerül, a szerződés pedig aláírásra kerül.
JÓ:    A díjátadó ünnepséget június 5-én megrendezzük, a szerződést pedig aláírjuk.
Mikor NE: `legal` profilban soha. És akkor sem, ha a cselekvő elhallgatása **szándékos** és a
szöveg funkciója megkívánja — hatósági határozatban ez gyakran így van.
Vigyázat a HU-H09-cel: ha az előző mondatnak többes alanya van, a T/3 kétértelmű lesz.
Forrás: e-nyelv.hu: terpeszkedő szerkezetek · Nyelvművelő kéziszótár

### HU-H03 · `történik`, `valósul meg`, `nyer` · [FIX-IF: informal, neutral] [AI:eros] [kern]

Mi ez: a főnévben rejlő igét kell állítmánnyá tenni.
Jelek: `beszerzése történik`, `feltöltése valósul meg`, `alkalmazást nyer`, `megvalósításra kerül sor`.
ROSSZ: A friss áru beszerzése hetente történik, a raktár feltöltése pedig hétvégén valósul meg.
JÓ:    Hetente szerzünk be friss árut, a raktárat pedig hétvégén töltjük fel.
Mikor NE: ha a `történik` valódi jelentésű (`Mi történt?`), vagy ha a `megvalósul` absztrakt
folyamatra utal, aminek tényleg nincs egyszemélyű cselekvője (`A terv megvalósult.`).

**Alpont — felelősség-elrejtő `történt` · `[jelöld]`.** Külön eset: `Hibák történtek.`,
`Késések adódtak.`, `Félreértés keletkezett.` Akkor jel, ha a szöveg **máshol megnevezi a
cselekvőket**, és csak a kínos ponton vált személytelenre — ez a hangváltás az árulkodó, nem a
szerkezet.
**Soha ne írd át magadtól.** A cselekvő beírása olyan felelősségi állítás, ami nincs a forrásban,
és a tartalmi invariánst sértené. A HU-B06 ráadásul védi az élettelen alanyt: a `döntés született`
teljesen rendben van. Ezért ez kizárólag a gyanús-listára megy, egy mondatos indoklással:
*a szöveg máshol megnevezi, ki mit tett, itt nem.*
Forrás: Minya Károly · Magyar Nyelvőr. Az angol prózajavító gyakorlat ugyanezt a jelenséget a
megnevezetlen felelős kapcsán tárgyalja; itt szűkebben, `[jelöld]`-ként vettük át.

### HU-H04 · `képez`, `jelent` névszói állítmány helyett · [FIX-IF: informal, neutral, formal] [AI:kozepes] [kern]

Mi ez: hagyd el az igét, és tedd a főnevet névszói állítmánnyá.
ROSSZ: A műszaki leírás a szerződés elválaszthatatlan részét képezi.
JÓ:    A műszaki leírás a szerződés elválaszthatatlan része.
Mikor NE: ha a `jelent` valódi jelentésű (`Ez azt jelenti, hogy…`), vagy ha a `képez` képzésre
utal (`szakembereket képez`).
Ez a minta `formal`-ban is fut, mert a csere nem rövidít és nem lazít regisztert — csak egy üres
igét vesz ki.
Forrás: Nyelvművelő kéziszótár

### HU-H05 · `esetén`, `hiányában` helyett mellékmondat · [FIX-IF: informal, neutral] [AI:eros] [kern]

Mi ez: a főnévi feltételt `ha`-val kezdődő mellékmondatra bontsd, lehetőleg pozitív állításként.
Jelek: `esetén`, `hiányában`, `esetében`, `végett`, `céljából`.
ROSSZ: Hozzájárulás hiányában az ügyfélszolgálaton történő benyújtás esetén az adatokat töröljük.
JÓ:    Ha Ön az ügyfélszolgálaton nyújtja be a kérelmet, és nem járul hozzá, töröljük az adatokat.
Mikor NE: `legal` profilban soha — a jogi szövegben a feltétel főnévi formája pontosabb hatókört
ad, mint a mellékmondat. `formal`-ban csak akkor, ha kettőnél több halmozódik egy mondatban.
Forrás: Minya Károly: Hivatalosan, terpeszkedve – de közérthetően

### HU-H06 · Formális kötőszó-körülírások · [FIX-IF: informal, neutral] [AI:eros] [kern]

Mi ez: `amennyiben` → `ha`, `tekintettel arra, hogy` → `mivel`, `azon tény fényében, hogy` → `mivel`.
ROSSZ: Amennyiben a számlával kapcsolatban kifogása van, tekintettel arra, hogy a határidő lejárt,
kérelem benyújtása szükséges.
JÓ:    Ha kifogása van a számlával, küldjön kérelmet, mert a határidő már lejárt.
Mikor NE: **HU-B19.** Ezek nem hibák, csak hosszabbak. `formal`-ban csak klaszterben,
`legal`-ban soha — ott a lecserélés regisztertörést okoz, ami rosszabb, mint a terjengősség.
Forrás: Lanstyák István · Minya Károly

### HU-H07 · Hivatali klisék · [FIX-IF: informal, neutral] [AI:kozepes] [2026-08]

Mi ez: a hatósági levélnyelv készen kapott fordulatai.
Jelek: `Tájékoztatom, hogy`, `Kérjük tájékoztatásunk tudomásulvételét`, `nem áll módunkban`,
`a fentiek értelmében`, `az alábbiak szerint`, `jelen dokumentum célja`, `szíves tájékoztatásul`.
ROSSZ: Tájékoztatom, hogy kérelme elbírálásra került. Kérjük tájékoztatásunk tudomásulvételét!
JÓ:    Elbíráltuk a kérelmét. Ha valami nem világos, keressen minket.
Mikor NE: `legal` profilban a `jelen dokumentum`, `a fentiek értelmében` marad (HU-B23). És
figyelj rá, hogy a `nem áll módunkban` cseréje ne váltson át közvetlen elutasításba, ha a szöveg
udvariassági funkciója fontos.
Forrás: Magyar Nyelvőr · Grétsy László

### HU-H08 · Jogi vonzatváltozás — ne igésíts · [NEVER] [kontextus: legal, formal]

Mi ez: ne igésítsd a szerkezetet, ha a szinonim ige **más vonzatot** kíván, és a kötelező tárgy
kitétele megváltoztatná a jogi tartalmat.
Példa: `feljelentést tesz` ≠ `feljelenti` — az utóbbi kötelező tárgyat kíván, tehát megnevezi,
kit jelentenek fel. Ez más jogi állítás.
Mikor alkalmazd: minden `legal` és `formal` szövegben, mielőtt a HU-H01-et futtatnád.
Forrás: B. Kovács Mária: A funkcióigés szerkezetek a jogi szaknyelvben, Magyar Nyelvőr 123

### HU-H09 · A T/3 általános alany kétértelműsége · [FIX] [AI:gyenge] [kern]

Mi ez: ha a HU-H02 javítása után T/3 igét kapsz, és az előző mondatnak **többes számú alanya
van**, az olvasó ráértheti az alanyt — ilyenkor nevezd meg a cselekvőt, vagy hagyd a főnévi
szerkezetet.
ROSSZ: A nyomozó hatóságok megállapították, hogy a zsarolás a presszóban zajlott. A váltságdíjat
is ott adták át. (kik? a hatóságok?)
JÓ:    A nyomozó hatóságok megállapították, hogy a zsarolás a presszóban zajlott. A váltságdíj
átadása is ott történt.
Mikor NE: ha nincs megelőző többes alany, a T/3 tökéletesen egyértelmű.
Ez a minta a HU-H02 **utáni** ellenőrzés, nem önálló javítás.
Forrás: B. Kovács Mária, Magyar Nyelvőr 123

### HU-H10 · A hivatali regiszter nem lazítható · [NEVER] [kontextus: formal, legal]

Mi ez: **precedencia-szabály, nem minta.** Jogi, szerződéses és hatósági szövegben a formális
névszói szerkezet helyénvaló. Beszélt nyelvi fordulatra cserélve a szöveg jelentést és joghatást
veszít.
Rossz „javítás”: *A szerződés attól a naptól él, amikor mindkét fél aláírta, és ha valaki ki akar
szállni, harminc nappal előbb szóljon.*
Helyes, érintetlen forma: *A szerződés a felek aláírásának napján lép hatályba. Felmondására
harmincnapos határidővel, írásban van lehetőség.*
Ez a tétel **felülír minden mintát ebben a fájlban és a `substitutions.md`-ben.** Ha a szöveg
`legal` vagy `formal` profilú, a plain-language javítás nem alapértelmezés, hanem kivétel, amit
külön indokolni kell.
Forrás: Lanstyák István: nyelvhelyesség vs. nyelvi helyénvalóság, Fórum Társadalomtudományi Szemle

---

## Sorrend ebben a passban

1. Először HU-H08 és HU-H10: eldől, fut-e egyáltalán a pass.
2. HU-H01, HU-H02, HU-H03, HU-H04 — a funkcióigés család. **Mondatonként legfeljebb egy.**
3. HU-H05, HU-H06 — feltétel és kötőszó.
4. HU-H07 — klisék.
5. HU-H09 — utólagos ellenőrzés a HU-H02 javításaira.
