# Források és megbízhatóság

Ez a fájl azért van, mert a katalógus `AI:` értékeinek nagy része **becslés, nem mérés**. Ha ez
nincs kiírva, a modell mért ténynek olvassa a saját irányelvét, és nagyobb bizonyossággal javít,
mint amennyi indokolt.

---

## Mit tudunk mérésből

**A gépi gyakoriságról semmit, amit egy olvasó ellenőrizni tudna.** Ez szűkebb állítás, mint
ahogy elsőre hangzik, és pontosan ennyit jelent: nyelvészeti forrás van, több is, és van köztük
számszerű – de egyik sem azt méri, *milyen gyakran ír egy nyelvi modell* egy adott alakot. Márpedig
az `AI:` érték épp ezt állítja. A `method/constants.yml` `measured_patterns` listája ezért **üres**,
és a katalógus mind a 47 `SOFT` mintája `?`-jelölt.

Példa a különbségre, mert nem elvont: a HU-M02 mögött ott áll Domonkosi Ágnes adata – 240 hivatalos
levél 78%-ában `Ön`/`Önök`, `real.mtak.hu/75699` –, ami hivatkozható és számszerű. Csak épp azt
méri, hogyan írnak **emberek** hivatalos levelet, nem azt, hogy egy modell milyen gyakran halmozza
az `Ön`-t. A minta jogosultsága erős, az `AI:eros` becslés marad becslés, és ezért `?`-jelölt.

Korábban három minta – a HU-L01, a HU-L06 és a HU-L11 – állt `?` nélkül, egyetlen forrásra
hivatkozva: az SZTE 2026 januári magyar AI-szövegfelismerőjére (Kiss Mihály), amely a
`kulcsfontosságú`, `már nem pusztán`, `a cél nem`, `ez a gondolkodásmód`, `átfogó képet nyújt`,
`jelen kutatás célja`, `a kutatás újszerűsége`, `komplex módon` fordulatokat nevesíti.

**A fejlesztés azóta beazonosítható, a hivatkozás mégsem áll össze.** Ami előkerült: SZTE-s
hallgatói fejlesztés, Kiss Mihály, 350 ezer magyar szövegből álló tanítóhalmaz, 2026 januári
egyetemi és sajtóközlemények (`u-szeged.hu`, `computertrends.hu`, `infostart.hu`). Ez **név,
dátum és intézmény**, nem módszertan: nincs benne, honnan jön a nyolc fordulat, sem az, hogyan
mérték. Vagyis a forrás állapota **ellenőrizhetetlen emlékből hivatkozható sajtóhírré** lépett elő,
és nem méréssé.

A felismerés maga konzisztens a katalógus többi megfigyelésével, ezért a fordulatok a `Jelek`
sorokon maradnak – de a **jelöletlen `AI:` érték** továbbra sem áll: a katalógus egyetlen szabálya
épp ez: *„a modell mért ténynek olvassa a saját irányelvét, és nagyobb bizonyossággal javít, mint
amennyi indokolt.”* A `measured_patterns` üres marad. A szakdolgozat vagy a mögötte álló publikáció
– módszertannal, mintaszámmal – visszaadhatja a három mintának a mért státuszt; a sajtóközlemény
nem.

**Nyelvészeti korpuszadat viszont van, csak nem erről.** Klaudy Kinga átváltási műveletei és az
explicitációs hipotézis korpuszalapúak. Az idiómasűrűség kérdésében is van kísérleti adat: a túl
sűrű idiómahasználat ugyanúgy fordításízt ad, mint a hiánya – ezért a sűrítés-fék nem
óvatoskodás. Ez a fajta forrás azonban másra jó, mint amit egy `AI:` érték állít. Egy szakforrás
(Klaudy, É. Kiss, Keszler) azt igazolja, hogy a *szerkezet létezik* és kalk – nem azt, hogy
*milyen gyakran* írja így egy nyelvi modell. A minta jogosultsága tehát erős, a hozzárendelt
`AI:` érték viszont becslés, és ezért áll ott a `?`.

A tipográfiai és helyesírási mintáknál ez nem baj: ott nem az a kérdés, hogy AI-jel-e, hanem hogy
helyes-e – azt az AkH. eldönti. Ezért a `FIX` és `FIX-IF` minták `?` nélkül is állhatnak; ők nem
gépi evidenciára hivatkoznak, hanem kodifikált normára.

**A `?` és a klaszter-felülírás viszonya.** Mind az öt felülíró minta (HU-L06, HU-L14, HU-R09,
HU-R10, HU-R11) `?`-jelölt, és ez nem ellentmondás: a felülírásukat nem az `AI:` érték hordozza,
hanem egy **megnevezett, falszifikálható teszt** – a szalmabáb-teszt kettős kapuja, a
LinkedIn-teszt, az adatoltsági teszt, a negyedarány, a „ki mit csinál?” kérdés. A `?` a
gyakorisági becslést jelöli meg, a felülírás pedig szerkezeti feltételen áll. Új felülírást csak
ilyen teszttel szabad felvenni.

## Hitelességi szintek

**Magas – normatív vagy lektorált.**
`A magyar helyesírás szabályai, 12. kiadás` és a `helyesiras.mta.hu` Helyes blog · Osiris
Helyesírás · MTA Nyelvtudományi Intézet nyelvművelő GYIK (`archive.nytud.hu`) · `e-nyelv.hu`
nyelvi tanácsadás · Magyar Nyelvőr (`c3.hu`, `epa.oszk.hu`) · Magyar Nyelv · Nyelvtudományi
Közlemények · REAL-MTAK repozitórium · MeRSZ (Strukturális magyar nyelvtan, Kiefer–Gyuris:
Szemantika, Klaudy) · ELTE EDIT és ELTE szabadbölcsészet tananyagok · Anyanyelv-pedagógia ·
EU Intézményközi kiadványszerkesztési útmutató magyar kiadása.

**Magas – szakkönyv.**
Szepesy Gyula: *Nyelvi babonák* (Gondolat, 1986; teljes szöveg a MEK-en) · É. Kiss Katalin:
*A magyar mondatszerkezet* · Kiefer Ferenc: *Aspektus és akcióminőség* · Keszler Borbála:
*Magyar grammatika* · Klaudy Kinga: *A fordítás elmélete és gyakorlata*, *Az átváltási műveletek
rendszere* · Tolcsvai Nagy Gábor: *A magyar nyelv stilisztikája* · Szikszainé Nagy Irma: *Leíró
magyar szövegtan* · Gyurgyák János: *Szerkesztők és szerzők kézikönyve* · Fóris Ágota: *Hat
terminológia lecke*.

**Magas – szerző, ismeretterjesztő fórumon.**
Nádasdy Ádám · Kálmán László · Fejes László · Schirm Anita · Sinkovics Balázs · Domonkosi Ágnes ·
Lanstyák István · Pölcz Ádám · Minya Károly. Ezek nyest.hu-n, kultura.hu-n, e-nyelvmagazin.hu-n
jelentek meg, de a szerző szakmai súlya adja a hitelt, nem a felület.

**Közepes – iparági stílusútmutató.**
Microsoft Hungarian Style Guide · Mozilla, Ubuntu, GNOME magyar fordítói útmutatók. Ezek
**normatív döntések, nem leíró tények**: azt mondják meg, mit írjon elő egy cég, nem azt, mi a
magyar nyelv. Regiszter- és felületkérdésekben használhatók, nyelvhelyességi ítéletre nem.

**Külső taxonómia.**
A Wikipédia „Signs of AI writing” szócikke (CC BY-SA 4.0) hat mintánál szerepel forrásként.
Onnan a **jelenség megnevezése** származik; a magyar alakteszt, a kivételek és minden példamondat
saját. Részletek: a repó `NOTICE.md`-je.

**Alacsony – nem hivatkozási alap.**
SEO-blogok, marketinges „AI-detektor” oldalak, tartalomfarmok. Ahol egy jegy csak ilyen helyen
szerepelt, de a mért SZTE-listával egybevágott, ott megtartottuk, és a mintánál `?` áll.

---

## Ellenőrzött hibák a katalógusban

A gyűjtés során **négy forrás-félreidézés** derült ki. Ezeket javítottuk, de a tanulság
általános: **a katalógus bővítésekor a forrást el kell olvasni, nem elég a címére hivatkozni.**

1. Egy minta Szepesyre hivatkozva írta elő azt, amit Szepesy éppen cáfol (páros testrész
   birtokos többese). → HU-B11, no-op mindkét irányban.
2. Egy minta abszolút tiltássá keményítette a `helyesiras.mta.hu` blogját a mondatkezdő
   `azonban` ügyében, holott a blog maga mondja, hogy előfordul. → törölve, HU-B03 nyer.
3. Egy minta „angolos hatásnak” nevezte a halmozott alany értelmi egyeztetését, amiről a
   hivatkozott MTA-blog egy szót sem ejt, sőt mindkét egyeztetést helyesnek mondja. → törölve.
4. Az `illetve` forrása nem hibáztat, hanem jogszabály-szerkesztési előírást idéz. → HU-G20
   `[jelöld]`-re szelídítve.

Ezért szuppressziós formátumú a `do-not-touch.md`: példapár nélkül. Egy ROSSZ/JÓ pár átírási
műveletet tanít, és a babona-mintáknál ez **visszafelé** tanított volna át transzformációt.

## Amit nem ellenőriztünk

Néhány könyvforrás cím szerint szerepel, oldalszám nélkül. Ezek bevett szakkönyvek, de a rájuk
hivatkozó konkrét minták szövegszerű ellenőrzése még hátravan.

| forrás | függő minták | ebből egyedüli forrás | állapot |
|---|---|---|---|
| Keszler *Magyar grammatika* | HU-G07, HU-G09, HU-G10, HU-G12, HU-G13, HU-G14, HU-G15, HU-G17, HU-R06, HU-R07 | HU-G07, HU-G10, HU-G13 | nem ellenőrizve; szabadon elérhető példány nincs |
| Szikszainé *Leíró magyar szövegtan* | HU-R02, HU-R04, HU-R05, HU-R06 | HU-R05 | nem ellenőrizve |
| Kiefer *Aspektus és akcióminőség* (2006) | HU-G08, HU-G11 | HU-G11 | nem ellenőrizve; teljes szöveg: `real-eod.mtak.hu/19513` |
| Gyurgyák *Szerkesztők és szerzők kézikönyve* | HU-R08, HU-M11 | HU-R08 | nem ellenőrizve |
| Fóris *Hat terminológia lecke* | HU-M12 | HU-M12 | **ellenőrizve**, lásd lent |

**A legélesebb kockázat: három `[FIX]` minta egyedüli forrása olvasatlan könyv** – HU-G07, HU-G11,
HU-G13. A `[FIX]` némán javít, nem jelöl, tehát ott egy forráshiba `?` nélkül terjed tovább.

**HU-M12 – ellenőrizve.** A Fóris 3.3. szakasza (*Terminológiai és szemantikai norma a
szaknyelvekben*, 60–61. o.) elkülöníti a terminológiai normát (a helyes, elfogadott terminus
kerül-e használatra az adott szövegben) és a szemantikai normát, és kimondja, hogy a többféle
lehetséges elnevezés közül a szakemberek választják ki „azt az egyet (esetleg néhányat)”, amely
normaként funkcionál. Ez megalapozza a HU-M12-t.

**De egy árnyalattal, amit meg kell tartani:** ugyanez a könyv (1.4.) kifejezetten **tévesnek**
nevezi azt a nézetet, hogy a szaknyelvekben nincsenek szinonimák, és példákat is hoz rájuk
(*egyenlet ~ formula ~ összefüggés*, *feszültség ~ potenciál*). A HU-M12 tehát a **szövegen belüli
következetességre** hivatkozhat, arra nem, hogy egy fogalomnak egyetlen neve volna. A minta
jelenlegi megfogalmazása és a `Mikor NE: ez nem purizmus` kikötése ezzel összefér – így is kell
maradnia.

**Két könyv törölve ebből a listából:** Szili *Tetté vált szavak* és Nemesi *Az alakzatok kérdése
a pragmatikában*. A katalógusban **egyetlen minta sem hivatkozik rájuk** – csak ez a felsorolás
említette őket, vagyis a fájl a sajátjánál nagyobb kitettséget vallott be.

Ha egy ilyen mintát vitatnak, először a forrást nézd meg, ne a mintát védd.

## Karbantartás

- `[kern]` jelölésű minták: AkH., tipográfia, mondattan. Stabilak, csak akkor változnak, ha az
  akadémiai szabályzat változik.
- `[2026-08]` jelölésű minták: lexikai listák. **12–18 havonta felülvizsgálandók.** A modellek
  szókincse változik; a mai árulkodó szó holnap semleges lehet, és fordítva.
- Új minta felvételekor kötelező a `Mikor NE` mező. Ha nem tudsz kivételt írni hozzá,
  valószínűleg túl tágan fogalmaztad. (A `[NEVER]` tételek kivételek: azok maguk tiltások.)
