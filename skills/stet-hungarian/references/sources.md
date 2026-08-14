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
és a katalógus mind a 46 `SOFT` mintája `?`-jelölt.

Példa a különbségre, mert nem elvont: a HU-M02 mögött ott áll Domonkosi Ágnes adata – 240 hivatalos
levél 78%-ában `Ön`/`Önök`, `real.mtak.hu/75699` –, ami hivatkozható és számszerű. Csak épp azt
méri, hogyan írnak **emberek** hivatalos levelet, nem azt, hogy egy modell milyen gyakran halmozza
az `Ön`-t. A minta jogosultsága erős, az `AI:eros` becslés marad becslés, és ezért `?`-jelölt.

Korábban három minta – a HU-L01, a HU-L06 és a HU-L11 – állt `?` nélkül, egyetlen forrásra
hivatkozva: az SZTE 2026 januári magyar AI-szövegfelismerőjére (Kiss Mihály), amely a
`kulcsfontosságú`, `már nem pusztán`, `a cél nem`, `ez a gondolkodásmód`, `átfogó képet nyújt`,
`jelen kutatás célja`, `a kutatás újszerűsége`, `komplex módon` fordulatokat nevesíti. Ehhez a
forráshoz **nincs hivatkozásunk**: se URL, se kiadás, se lapszám, se módszertani leírás. A
felismerés maga konzisztens a katalógus többi megfigyelésével, ezért a fordulatok a `Jelek`
sorokon maradnak – de a **jelöletlen `AI:` érték** ellenőrizhetetlen forrásra épült volna, és a
katalógus egyetlen szabálya épp ez: *„a modell mért ténynek olvassa a saját irányelvét, és nagyobb
bizonyossággal javít, mint amennyi indokolt.”* Aki elő tudja keríteni a hivatkozást, egy issue-val
visszaadhatja a három mintának a mért státuszt.

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

Néhány könyvforrás cím szerint szerepel, oldalszám nélkül: Kiefer *Aspektus és akcióminőség*,
Keszler *Magyar grammatika*, Szikszainé *Leíró magyar szövegtan*, Szili Katalin *Tetté vált
szavak*, Nemesi *Az alakzatok kérdése a pragmatikában*, Fóris *Hat terminológia lecke*, Gyurgyák
*Szerkesztők és szerzők kézikönyve*. Ezek bevett szakkönyvek, de a rájuk hivatkozó konkrét minták
szövegszerű ellenőrzése még hátravan.

Ha egy ilyen mintát vitatnak, először a forrást nézd meg, ne a mintát védd.

## Karbantartás

- `[kern]` jelölésű minták: AkH., tipográfia, mondattan. Stabilak, csak akkor változnak, ha az
  akadémiai szabályzat változik.
- `[2026-08]` jelölésű minták: lexikai listák. **12–18 havonta felülvizsgálandók.** A modellek
  szókincse változik; a mai árulkodó szó holnap semleges lehet, és fordítva.
- Új minta felvételekor kötelező a `Mikor NE` mező. Ha nem tudsz kivételt írni hozzá,
  valószínűleg túl tágan fogalmaztad. (A `[NEVER]` tételek kivételek: azok maguk tiltások.)
