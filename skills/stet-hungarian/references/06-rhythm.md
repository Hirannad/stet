# Pass 5 — Ritmus és szövegszint

Ez a pass fut utoljára, mert minden korábbi javítás megváltoztatja a mondathosszokat: előbb
ritmizálni annyi, mint kétszer dolgozni.

Itt a jelek **mondat fölöttiek**. Egy bekezdést kell nézni, nem egy mondatot — ezért itt nincs
`FIX`, minden minta `SOFT`, és mind klaszterküszöbhöz kötött.

A pass profilonkénti kapuját a `registers.md` mátrixa mondja meg — itt szándékosan nem ismételjük,
mert két helyen leírva előbb-utóbb két különböző szabály lesz belőle.

---

### HU-R01 · Egyenletes mondathossz · [SOFT] [AI:eros?] [kern]

Mi ez: a magyar prózában a mondathosszak szórása nagy. A gépi szöveg közepes hosszúságú mondatok
egyenletes sorozata.
Miért írja így a gép: a modell a legvalószínűbb folytatást választja, és az mindig a középérték felé húz.
ROSSZ: A csapat áttekintette az adatokat, majd összefoglalta a tanulságokat, és végül javaslatot
tett a folytatásra. Ezután a vezetőség megvitatta a javaslatot, majd döntést hozott a további
lépésekről, és tájékoztatta az érintetteket.
JÓ:    Áttekintettük az adatokat. Kijött egy kényelmetlen tanulság: rosszul mértünk. Innen kell
újrakezdeni, és ezt a vezetőség is elfogadta.
Mérés: a bekezdés mondathossz-szórása. Ha az összes mondat a középérték ±30%-án belül van, és
négynél több mondatról van szó, ez jel.
Mikor NE: **rövid szövegen nem értelmezhető.** Három mondat alatt ne fusson. Jogi és technikai
szövegben az egyenletesség szándékos.
Forrás: Tolcsvai Nagy Gábor: A magyar nyelv stilisztikája

### HU-R02 · Bekezdés-séma uniformitása · [SOFT] [AI:eros?] [kern]

Mi ez: minden bekezdés ugyanúgy épül fel — tételmondat, kifejtés, összegző zárómondat —, és
minden bekezdés nagyjából ugyanolyan hosszú.
Miért írja így a gép: a fogalmazástanítási séma erősen jelen van a korpuszban.
Jelek: minden bekezdés 3–5 mondat; minden bekezdés utolsó mondata összegez; a záró mondatok
`Tehát`, `Összességében`, `Ez azt jelenti, hogy` kezdetűek.
Javítás: töröld a fölösleges összegző zárómondatokat, és vonj össze vagy bonts szét bekezdéseket
úgy, hogy a hosszuk egyenetlen legyen. Egy egymondatos bekezdés is legitim.
Mikor NE: strukturált dokumentumban (eljárásleírás, specifikáció, jogi szöveg), ahol az
egyformaság a navigációt segíti.
Forrás: Tolcsvai Nagy Gábor · Szikszainé Nagy Irma: Leíró magyar szövegtan

### HU-R03 · Kényszeres hármas felsorolás · [SOFT] [AI:kozepes?] [kern]

Mi ez: a gondolatok hármas csoportba erőltetése, hogy „teljesnek” hasson.
ROSSZ: A rendezvény előadásokat, kerekasztal-beszélgetéseket és kapcsolatépítési lehetőségeket
kínál. A résztvevők inspirációt, tudást és kapcsolatokat visznek haza.
JÓ:    A rendezvényen előadások és kerekasztal-beszélgetések lesznek, a szünetekben pedig lehet
beszélgetni.
Mikor NE: **a hármasság önmagában nem AI-jel.** Ez a gyűjtemény egyik feloldott ellentmondása.
Csak akkor javíts, ha (a) a három tag párhuzamos `-ás/-és` képzős főnév, **vagy** (b) a hármasság
bekezdésenként visszatér. Egyetlen hármas felsorolás soha nem indok.
Forrás: Wikipedia: Signs of AI writing — „Rule of three overuse” magyar megfelelője (CC BY-SA 4.0;
a taxonómia onnan, a példák sajátok)

### HU-R04 · Kapcsolóelem-túltengés · [SOFT] [AI:eros?] [kern]

Mi ez: minden mondat kapcsolóelemmel indul, mintha a szövegnek magyaráznia kellene a saját
szerkezetét.
Jelek: `ugyanakkor`, `emellett`, `továbbá`, `ezáltal`, `ennek megfelelően`, `mindazonáltal`,
`ezen túlmenően` — mondatkezdő pozícióban, egymás után.
ROSSZ: Ugyanakkor a bevezetés lassan haladt. Emellett a csapat létszáma is csökkent. Ezáltal a
határidő tarthatatlanná vált.
JÓ:    A bevezetés lassan haladt, közben a csapat létszáma is csökkent. A határidő így
tarthatatlanná vált.
Mikor NE: **nem a kapcsolóelem a hiba, hanem a sűrűsége.** Egy `azonban` nem jel (HU-B03: a
mondatkezdő kötőszó szabályos). Akkor javíts, ha háromból két mondat így kezdődik.
A vessző eltávolítása külön művelet: HU-T15.
Forrás: Szikszainé Nagy Irma · e-nyelv.hu

### HU-R05 · Mutató anafora halmozása · [SOFT] [AI:eros?] [kern]

Mi ez: a magyar mondathatáron **zéró anaforát** használ — nem ismétli meg az alanyt, ha az
azonos. A gépi szöveg minden mondatot `ez`, `ez a X`, `az említett` kezdéssel kapcsol.
Miért írja így a gép: az angolban az alany kötelező, ezért a modell mindig kitesz valamit.
ROSSZ: A rendszer hétfőn állt le. Ez a leállás négy órán át tartott. Ez az esemény érintette az
ügyfeleket is. Az említett hiba a fizetési modulban keletkezett.
JÓ:    A rendszer hétfőn állt le, négy órára. Az ügyfeleket is érintette. A hiba a fizetési
modulban keletkezett.
Mikor NE: ha a mutató névmás valódi kétértelműséget old fel (két lehetséges előzmény), vagy
szembeállít. Jogi szövegben `az említett` a pontosság eszköze — ott hagyd.
Forrás: Szikszainé Nagy Irma: Leíró magyar szövegtan

### HU-R06 · Koordinációs ellipszis elmaradása · [SOFT] [AI:kozepes?] [kern]

Mi ez: halmozott mondatrészben a magyar kihagyja a közös ragot és igerészt. A gépi szöveg
mindent kiír.
ROSSZ: A jelentést elkészítettük, a jelentést átnéztük, és a jelentést elküldtük a vezetőségnek.
JÓ:    A jelentést elkészítettük, átnéztük és elküldtük a vezetőségnek.
Mikor NE: ha az ismétlés **nyomatékosít**, vagy ha a kihagyás kétértelmű lenne (eltérő vonzatok).
Ez nem azonos HU-B13-mal: ott a kulcsszó szinonimára cserélése tilos, itt a szó szerinti,
funkciótlan ismétlés összevonásáról van szó.
Forrás: Keszler Borbála: Magyar grammatika · Szikszainé Nagy Irma

### HU-R07 · Jelzőtorlódás · [SOFT] [AI:eros?] [kern]

Mi ez: két probléma egy mintában.
Kettőnél több prenominális jelző halmozása, illetve az angol utójelzős főnévi csoport balra
tolása hosszú jelzői szerkezetként.
ROSSZ: Egy átfogó, innovatív, skálázható, felhőalapú vállalati megoldást vezettünk be. A bizottság
által a múlt héten közzétett, a kibocsátás csökkentésére vonatkozó jelentés vitát váltott ki.
JÓ:    Skálázható felhőalapú megoldást vezettünk be. A bizottság a múlt héten jelentést tett közzé
a kibocsátás csökkentéséről; a jelentés vitát váltott ki.
Vessző a jelzők között: csak akkor, ha **egyenrangúak**. A `hosszú fekete haj` és a
`hosszú, fekete haj` nem ugyanaz.
Mikor NE: terméknévben, jogi meghatározásban, ahol a jelzők együtt definiálnak.
Forrás: Keszler Borbála · AkH. 12. 244.

### HU-R08 · Túltagolt makroszerkezet · [SOFT] [AI:eros?] [kern]

Mi ez: a szöveg úgy néz ki, mint egy prezentáció vázlata.
Jelek: három vagy több címszint rövid szövegben; félkövér kiemelés mondaton belül több helyen;
minden gondolat listaelem, próza szinte sehol; emoji a címekben; minden szakasz azonos hosszú.
Javítás: csökkentsd a címszinteket, vedd ki a mondaton belüli félkövéreket, és írd vissza prózává
azokat a listákat, amelyeknek a tagjai összefüggő mondatok. A lista akkor jó, ha a tagok tényleg
párhuzamosak és felcserélhetők.
Mikor NE: dokumentációban, eljárásleírásban, ellenőrzőlistában a tagolás funkció, nem dísz. `neutral`
profilban óvatosan, `legal`-ban egyáltalán ne.
**És egy magyar-specifikus kivétel:** a magyar a fókuszt szórenddel jelöli, írásban viszont
gyakran a félkövér tölti be ugyanezt a szerepet. Ha a kiemelés **szembeállított elempárra** esik
(`**bekerült**` … `**nem került be**`), az nem félkövér-infláció, hanem fókuszjelölés — hagyd.
Csak azt vedd ki, ami kulcsszót emel ki ok nélkül.
Forrás: Gyurgyák János: Szerkesztők és szerzők kézikönyve

### HU-R09 · Bevezetés nélküli kitalált szótár · [SOFT] [AI:eros?] [kern]

Mi ez: a szerző (jellemzően az asszisztens) kitalál egy absztrakt megnevezést, és onnantól úgy
használja, mintha bevett fogalom lenne. Az olvasónak sosem mutatja meg a konkrét esetet, amiből
a szó jött.
Miért írja így a gép: a modell szívesen általánosít és nevet ad. A név rögzíti a gondolatot, de
csak annak, aki már érti — az olvasó számára üres.
Jelek: metaforikus vagy elvont összetétel, ami sehol nincs definiálva és a szövegen kívül nem
használatos; a szó első előfordulása körül nincs példa, szám vagy megnevezett eset.
ROSSZ: A csendes elhalás a fő kockázat, amit a kapuzási elv old meg.
JÓ:    A fő kockázat az, hogy a munka észrevétlenül abbamarad. A tavalyi adatmigráció hat hétig
állt, és senki nem szólt. Ezért kér minden szakasz külön lezárást.
Javítás, ebben a sorrendben: (1) ha a szövegben **van** konkrét eset a szó mögött, hozd előre a
szó helyett; (2) ha nincs, írd körül hétköznapi szavakkal; (3) ha egyik sem megy új tény
kitalálása nélkül, hagyd, és tedd a gyanús-listára.
Mikor NE: ha a szó **bevett szakszó** (a szövegen kívül is használják), ha a szöveg **definiálja**
első előforduláskor, vagy ha a szerző szándékosan vezet be fogalmat, és a bevezetés meg is
történik. Metanyelvi említésben (ahol a szót *tárgyalják*, nem használják), idézetben, címben soha.

**Klaszter-felülírás.** Ez a minta **önmagában klaszternek számít**, ha a szó a szövegen kívül nem
adatolható és a szöveg nem definiálja. Nem kell mellé másik jel, és a `neutral` emelt küszöbe sem
alkalmazandó rá. Enélkül a minta gyakorlatilag néma: egy magányos coinage tiszta bekezdésben sosem
érné el a hármas küszöböt — pedig pont az az eset, amikor a leginkább zavar.

**Egy bekezdés coinage-ei egy művelet.** Ha ugyanabban a bekezdésben több bevezetetlen szó van,
azokat **együtt** takarítsd, és ez egyetlen javításnak számít a bekezdésenkénti keretben — ahogy a
HU-F01 nominalizációs családja is egy művelet. Kettőből egyet meghagyni rosszabb, mint egyiket sem.

**Az adatoltság független legyen.** A „szövegen kívül is használják” feltétel csak akkor teljesül,
ha a szót **más szerző, más rendszerben** használja. Ugyanannak a szerzőnek egy másik dokumentuma
vagy bármely gépi úton előállított anyag **nem adatolás, hanem visszhang** — enélkül a kikötés
nélkül minden coinage „bevetté” válik attól, hogy egyszer leírtuk máshol is.

**Ha a szó strukturált metaadatban is szerepel** (front matter, property, adatbázismező, címke),
a mező érinthetetlen zóna marad, de ez **nem blokkolja a prózai javítást**. Írd át a prózát, és
**kötelezően** jelezd a kimenetben, hogy a mező ugyanezt a változtatást igényli. A holtpont — „ha
nem tudod mindkettőt, ne írd át egyiket sem” — rosszabb, mint az átmeneti eltérés: ha a műfaj
minden kulcsfogalmat metaadatba is kiír, a blokkolás a mintát teljesen kilövi.
Forrás: közvetlen megfigyelés; a minta feltétele maga a teszt — adatoltság a szövegen kívül.

### HU-R10 · Önhivatkozó mondat · [SOFT] [AI:kozepes?] [kern]

Mi ez: olyan mondat, amelynek egyetlen dolga, hogy egy másik dokumentumra, jegyzetre vagy
szakaszra mutasson. Nem közöl tartalmat, csak könyvel.
Miért írja így a gép: a modell teljességre törekszik, és a kapcsolatok felsorolását tartalomnak
érzi.
Jelek: a mondat elhagyásával nem vész el állítás; a mondat magja egy link, egy fájlnév vagy egy
státusz (`az a szakasz még nincs kész`, `erről a másik dokumentum szól`, `lásd még`).
ROSSZ: A telepítésről a másik dokumentum szól. Erről egyébként korábban is írtunk már, de az az
oldal még nincs kész, úgyhogy most nem számít.
JÓ:    (Töröld mindkét mondatot. Egyik sem állít semmit a telepítésről.)
Mikor NE: ha a hivatkozás **érvet** hordoz (`ezt már eldöntöttük, lásd X` — ott az érv a döntés
ténye), vagy ha a szöveg műfaja tényleg navigáció (tartalomjegyzék, index, hivatkozásgyűjtemény,
átirányító szakasz). Az érinthetetlen zónák a link **szövegét és célját** védik — ez a minta nem
a linket írja át, hanem a köré épült üres mondatot törli.

**Klaszter-felülírás.** Ez a minta **önmagában klaszternek számít**, ha egy bekezdésen belül a
mondatok több mint negyede ilyen. Nem kell mellé másik jel, és a `neutral` emelt küszöbe sem
alkalmazandó rá. (Bekezdésre számold, ne az egész szövegre — a kettő rendszeresen ellentétes
eredményt ad, és a bekezdés a releváns egység.)

**Két kötelező ellenőrzés törlés előtt. Ha mindkettő kivált, az 1. nyer** — tömöríts, és a
2. ellenőrzés jelzését is írd ki. A tömörítés és a jelzés nem alternatíva, hanem együtt jár.

1. **Konkrétum.** Ha a mondat megnevezett esetet, fájlnevet, számot vagy dátumot is tartalmaz,
   az nem puszta pointer. Mentsd ki a konkrétumot egy rövid mondatba, és csak a könyvelést töröld.
   **A kimentett mondat végállapot: a következő futáson nem HU-R10-célpont**, akkor sem, ha
   csak állapotot közöl. Enélkül a minta a saját eredményét jelölné meg, és ismételt futtatásnál
   oszcillálna.
2. **A link túléli-e.** Ez csak **feloldható** hivatkozásra vonatkozik: megnevezett fájl, jegyzet,
   URL, dokumentumcím. A `a másik dokumentum`, `egy korábbi jegyzet` típusú megnevezetlen utalást
   nincs hova átmenteni, tehát nem blokkol — az ilyen a minta legtisztább esete, töröld.
   Ha a feloldható hivatkozás **csak ebben a mondatban** szerepel, és sehol máshol — sem a
   dokumentum hivatkozásjegyzékében vagy link-mezőjében (pl. `related`, `see also`, `references`),
   sem másik mondatban —, akkor a törlés elveszíti a kapcsolatot. Ilyenkor hagyd a mondatot, és
   **kötelezően** írd a kimenetbe: a link átmozgatható a hivatkozásjegyzékbe, utána a mondat
   törölhető. Ne töröld szó nélkül, de ne is hallgass róla.
   Linkgazdag műfajban (wiki, belső tudásbázis, jegyzetgráf) az egyedi link a tipikus eset — ha ez
   az ellenőrzés csak blokkolna, a mintát a fő használati esetén lőné ki. Ezért az ajánlás nem
   opcionális.
Forrás: közvetlen megfigyelés; szerkesztői konvenció — töröld azt a mondatot, amelynek egyetlen
dolga, hogy egy másik dokumentumra mutasson.

### HU-R11 · Elvont névszói állítás konkrétum nélkül · [SOFT] [AI:eros?] [kern]

Mi ez: rövid, tömör mondat, amelyben az alany és az állítmány is elvont főnév, és sehol nincs
mögötte cselekvő, eset vagy szám. **Nem terjengős** — épp ez a csapda: a HU-F01 nem fogja meg,
mert nincs `-ás/-és` lánc és nincs birtokoslépcső. Mégis ez az, amitől a szöveg „nem gyakorlatias”.
Miért írja így a gép: az absztrakció tömör és megcáfolhatatlan. A modell így tud lezárni egy
gondolatot anélkül, hogy elköteleződne bármi ellenőrizhető mellett.
Jelek: `X az Y` alakú mondat, ahol mindkét oldal elvont főnév, és sem alany, sem tárgy nem
személy vagy megnevezett dolog. **Második alak:** elvont főnév + üres, mérhetetlen melléknév —
`A tét nagy.`, `Az okok strukturálisak.`, `A következmények jelentősek.` Itt csak az alany
elvont, de az állítmány semmit nem közöl, mert nincs mihez viszonyítani.
ROSSZ (második alak): A tét nagy, és a következmények jelentősek.
JÓ:    Ha csúszunk, a szerződés júniusban lejár, és újra kell pályáznunk.
Teszt: **meg tudod mondani, ki mit csinál a mondat szerint?** Ha nem, és a bekezdésben sincs
konkrét eset, ez a minta.
ROSSZ: A hatékonyság feltétele az átláthatóság. Ami hiányzik, az a felelősség tisztázása.
JÓ:    Akkor haladunk gyorsabban, ha látjuk, ki min dolgozik. Most nem látjuk, és senki nem
mondta meg, kinek kellene.
Javítás: tedd vissza a cselekvőt és az igét, vagy hozd elő a konkrét esetet **a bekezdésből**
(ugyanaz a hatókör, mint a HU-L14-nél — nem az egész szövegből).
Ha egyik sem megy **új tény kitalálása nélkül**, hagyd, és tedd a gyanús-listára — ott legalább
látszik, hogy a mondat üres. Mint a HU-L14-nél, itt is a jelzés a gyakoribb kimenet, nem az átírás.

**Klaszter-felülírás.** Ez a minta **önmagában klaszternek számít**, ha a „ki mit csinál?” teszt
elbukik **és** a bekezdésben nincs egyetlen konkrétum sem (szám, dátum, név, megnevezett eset).
Nem kell mellé másik jel, és a `neutral` profil emelt küszöbe sem alkalmazandó rá.

Enélkül a minta halott. A definíciója szerint pont **tömör** mondatokra vonatkozik, amiket a
HU-F01 terjengősség-alapú jelzőszáma nem fog meg — vagyis tipikusan olyan bekezdésben áll, ami
egyébként tiszta. Egy `eros` minta önmagában 2 pont, a küszöb 3 vagy 4: sosem érné el.
Ugyanez a gond volt a HU-R09-nél, ugyanez a megoldás.

**A felülírás ára, és ezért szűk a feltétel:** ha van a bekezdésben bármi konkrétum, a minta nem
tüzel önmagában, mert akkor az olvasónak van hol földet érnie. A felülírás csak a tiszta
absztrakciót célozza.

Mikor NE:
- Definícióban, tételmondatban, jogi meghatározásban, ahol az absztrakció **maga a tartalom**.
  Filozófiai és elméleti szövegben szintén nem hiba.
- Hétköznapi főnévre önmagában (`kérdés`, `lépés`, `válasz`) — a jel az, hogy a mondat **mindkét**
  oldala elvont, és a bekezdésben nincs földet érés.
- **Ha az alulmeghatározottság szándékos.** Nyitott kérdést rögzítő szövegben (kérdéslista,
  döntési vázlat, egy RFC nyitott pontja, szándékosan függőben hagyott megfogalmazás) a homály nem hanyagság,
  hanem az állítás maga. Minden konkretizálás cselekvőt választ — és ezzel megválaszolja azt a
  kérdést, aminek a nyitva tartása a szöveg egyetlen tartalma. Ilyenkor a gyanús-lista a helyes
  kimenet, nem a javítás.
- **Kvantor-korlát.** A konkretizálás nem tágíthat: ha az eredeti szűkít (`csak ott`, `két
  kivétellel`, `bizonyos esetben`), a javított mondat sem lehet általánosabb. A tartalmi
  invariáns a kvantor hatókörére is vonatkozik.
- Rövid, töredékes mondatra, ami ritmust ad (`Ennyi. Nem több.`). Az ilyen a „megőrizendő jegyek”
  közé tartozik, nem ide.
Forrás: közvetlen megfigyelés; a tömör absztrakció válfaja, amit a HU-F01 terjengősség-alapú
jelzőszáma nem fog meg.

---

## Amit meg kell őrizni — az emberi magyar szöveg jegyei

Ha ezeket látod, **hagyd békén a bekezdést** — de pontosan meghatározva: ez a lista a `SOFT`
ritmusjavításokat (HU-R01, HU-R02, HU-R07, HU-R08) blokkolja, **nem** a `FIX` tipográfiát és nem a
HU-R09/HU-R10 tartalmi mintáit. Egy emberi hangú bekezdésben is javítandó az angol idézőjel, és
attól még lehet benne bevezetetlen coinage.

Ezek nehezen hamisíthatók, és a túljavítás pont ezeket törli ki először.

- **Konkrét, ellenőrizhető részlet.** Név, összeg, dátum, helyszín, egy fura idézet. A modell
  lekerekíti a specifikumot; az ember gyűjti.
- **Feloldatlan feszültség.** „Szerintem jó, de valami zavar benne, és nem tudom megfogalmazni.”
  A gépi szöveg lezárt véleményt ad.
- **Önjavítás, közbevetés.** „(Majdnem azt írtam, hogy biztos — pedig nem az.)”
- **Egyenetlen ritmus.** Egy háromszavas mondat egy hosszú után.
- **Diskurzusjelölő a helyén.** `hát`, `ugye`, `amúgy`, `persze` — lásd HU-B14.
- **Korhoz kötött utalás.** Szleng, mém, belső poén, ami egy adott évhez és közeghez tapad.
- **Szóismétlés a kulcsszón.** Ez nem hiba, hanem a magyar szakszöveg normája (HU-B13).
- **2022. november 30. előtt írt szöveg.** A ChatGPT nyilvános indulása. Ennél régebbi anyagnál
  a jelek elméletileg sem AI-eredetűek.

## Sűrítés-fék

Ez a pass **nem tehet be** a szövegbe olyat, ami nem volt benne. Konkrétan tilos idiómát,
szólást, partikulát vagy diskurzusjelölőt beszúrni azért, hogy a szöveg oldottabbnak hasson.
Az idiómasűrűség ugyanúgy fordításízt ad, mint a hiánya. Ez fordítástudományi megfigyelés,
nem a mi mérésünk — lásd `sources.md`.

A ritmusjavítás **átrendez és töröl**, nem díszít. Ha egy bekezdés a törlések után is lapos, az
a szerző dolga, nem a skillé: írd a „gyanús, de nem javítottam” listára.

## Monotonitás

Ez a pass nem érvénytelenítheti a korábbiakat. A mondatok átrendezése közben könnyű visszahozni
egy angol idézőjelet, egy Title Case címet vagy egy `kulcsfontosságú`-t. A Pass 6 önellenőrzés
ezért futtatja újra a tipográfiai ellenőrzést a kimeneten.
