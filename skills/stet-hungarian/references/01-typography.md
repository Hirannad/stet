# Pass 1 — Tipográfia és helyesírás

A leginkább determinisztikus réteg: itt nincs ítélet, csak norma. Ezért fut először — nem tud
jelentést változtatni, és letisztítja a képet, hogy utána látszódjon, mennyi az ítéletigényes maradék.

Ezek túlnyomórészt `[FIX]` minták: regisztertől függetlenül javítandók, klaszterküszöb nélkül.
Kivétel, ahol külön jelezve van.

**Figyelem a megfordult mintákra.** Az angol nyelvű prózajavító listák két tipográfiai szabálya
itt az ellenkezőjére fordul: a `„…”` idézőjel és a szóközös gondolatjel a **helyes** magyar forma,
nem AI-jel. Csak az angol `"…"` és az em dash (—) a hiba. Aki mechanikusan alkalmazza egy másik
nyelv listáját, elrontja a magyar tipográfiát.

---

### HU-T01 · Angol idézőjel magyar szövegben · [FIX] [AI:eros] [kern]

Mi ez: a magyar idézőjel alsó nyitó és felső záró — `„…”`. A belső idézet lúdláb (`»…«`), a
harmadik szint félidézőjel (`'…'`).
Miért írja így a gép: az egyenes `"…"` és az angol tipografált `“…”` a betanító korpusz
alapértelmezése,
és a legtöbb szerkesztő is ezt kínálja.
Jelek: `"…"` (egyenes) vagy `“…”` (angol tipografált) magyar mondatban.
ROSSZ: A jelentés szerint "a bevezetés csúszik", ezért új határidőt kértünk.
JÓ:    A jelentés szerint „a bevezetés csúszik”, ezért új határidőt kértünk.
Mikor NE: kódblokkban, karakterláncban, fájlnévben, idézett angol szövegben. És soha ne írd át
a **helyes** `„…”` alakot semmire.
Forrás: AkH. 12. 240. · Osiris Helyesírás

### HU-T02 · Em dash gondolatjel helyett · [FIX] [AI:eros] [kern]

Mi ez: a magyar gondolatjel félkvirtmínusz (`–`), **szóközökkel** körülvéve. Az angol em dash
(`—`) a mai magyar tipográfiában nem használatos, és a kiskötőjel (`-`) sem helyettesíti.
Miért írja így a gép: az angol em dash szóköz nélkül tapad, és a modell ezt hozza át.
Jelek: `—`, ` -- `, szóköz nélküli `–`.
ROSSZ: A terv jó — legalábbis papíron — de a költségek nem stimmelnek.
JÓ:    A terv jó – legalábbis papíron –, de a költségek nem stimmelnek.
Mikor NE: **a helyes gondolatjelet soha ne töröld.** Ez az a pont, ahol egy angol szabálylista
mechanikus átvétele kárt okoz: ott a cél a gondolatjel kiirtása, itt a cél a helyes alak
előállítása. Párbeszédben a sor eleji gondolatjel kötelező, ne szedd ki.
Forrás: AkH. 12. 249. · Osiris Helyesírás

### HU-T03 · Nagykötőjel helyett kiskötőjel · [FIX] [AI:kozepes] [kern]

Mi ez: nép- és nyelvnevek kapcsolatában, tulajdonnevek alkalmi összekapcsolásában és `-tól/-ig`
viszonyban nagykötőjel (`–`) áll, **szóköz nélkül** tapadva.
Miért írja így a gép: az angol írásmód itt is kiskötőjelt vagy en dasht használ szóközzel.
Jelek: `magyar-angol`, `Budapest-Bécs`, `2020-2024`.
ROSSZ: A 2020-2024 közötti magyar-angol projektben a Budapest-Bécs vonalat vizsgáltuk.
JÓ:    A 2020–2024 közötti magyar–angol projektben a Budapest–Bécs vonalat vizsgáltuk.
Mikor NE: ha a kötőjel valódi összetételt jelöl (`dél-afrikai`, `Kiss-Nagy Éva` mint egy név),
ott kiskötőjel a helyes.
Forrás: AkH. 12. 263.

### HU-T04 · Angol számformátum · [FIX] [AI:eros] [kern]

Mi ez: a tizedes jele **vessző**, az ezres tagolás **szóköz** (a négyjegyű szám tagolatlan).
Miért írja így a gép: az angol pont/vessző konvenció fordítva működik, és ez a leggyakoribb
tükrözött formai hiba.
Jelek: `1,250,000`, `3.5`, `1,250.5`.
ROSSZ: A bevétel 1,250,000 forint, a marzs 3.5 százalék.
JÓ:    A bevétel 1 250 000 forint, a marzs 3,5 százalék.
Mikor NE: kódban, CSV-ben, API-válaszban, adatbázismezőben — ott az angol formátum a helyes.
Verziószámban (`3.5`) sem tizedesjel.
Forrás: AkH. 12. 288–290.

### HU-T05 · Szóköz szám és mértékegység között · [FIX] [AI:kozepes] [kern]

Mi ez: a rövidített mértékegység előtt szóköz áll (`5 kg`, `8 GB`, `25 °C`), a fokjel, a
százalék- és az ezrelékjel viszont **tapad** (`90°`, `60%`, `1000‰`).
Miért írja így a gép: az angol tipográfia itt ingadozik, és a modell vegyesen hozza.
Jelek: `8GB`, `60 %`, `25°C`.
ROSSZ: A szerver 25°C-on üzemel, a kihasználtság 60 %, a memória 8GB.
JÓ:    A szerver 25 °C-on üzemel, a kihasználtság 60%, a memória 8 GB.
Mikor NE: ha a szöveg egy másik szabványt követ (tudományos SI-jelölés, gyártói adatlap idézése).
Forrás: AkH. 12. 288. · Osiris Helyesírás

### HU-T06 · Dátum sorrendje és toldalékolása · [FIX] [AI:eros] [kern]

Mi ez: a magyar dátum év–hónap–nap sorrendű, az évszám után **pont** áll, a toldalék pedig
pont nélkül, kötőjellel kapcsolódik a napszámhoz.
Miért írja így a gép: az angol hónap–nap–év sorrend és a `2.-i` típusú kettőzött írásjel.
Jelek: `Augusztus 2, 2026`, `2026 augusztus 2`, `2.-i`, `2-ában`.
ROSSZ: A workshop Augusztus 2, 2026-ban lesz, a 2026 augusztus 2.-i döntés alapján.
JÓ:    A workshop 2026. augusztus 2-án lesz, a 2026. augusztus 2-i döntés alapján.
Mikor NE: ISO-formátumú dátum technikai szövegben (`2026-08-02`), naplóban, fájlnévben.
Forrás: AkH. 12. 297. · helyesiras.mta.hu

### HU-T07 · Angolos Title Case · [FIX] [AI:eros] [kern]

Mi ez: magyar címben, címsorban, gombfeliratban és menüpontban **csak az első szó és a
tulajdonnevek** nagy kezdőbetűsek. A kiemelt címsor végére nem kerül pont.
Miért írja így a gép: az angol title case a legerősebb szerkezeti anglicizmus. Magyarul
egyáltalán nincs ilyen konvenció, ezért itt **erősebb** jel, mint angol szövegben.
Jelek: két vagy több nagy kezdőbetűs köznév egymás után címben.
ROSSZ: ## Stratégiai Tárgyalások És Globális Partnerségek
JÓ:    ## Stratégiai tárgyalások és globális partnerségek
Mikor NE: ha a cím intézmény hivatalos neve (`Magyar Tudományos Akadémia`), márkanév, vagy
idézett angol cím.
Forrás: AkH. 12. 197. · Microsoft Hungarian Style Guide

### HU-T08 · Hónap, nap, népnév, ünnep nagybetűzése · [FIX] [AI:eros] [kern]

Mi ez: a hónapok, napok, népnevek, nyelvek, vallások és ünnepek nevét a magyar **kisbetűvel** írja.
Miért írja így a gép: az angol mindet nagybetűzi, és ez szóról szóra átjön.
Jelek: `Hétfő`, `Augusztus`, `Magyar`, `Karácsony`, `Angol nyelv`.
ROSSZ: A Magyar csapat Hétfőn, Augusztus 3-án indul, és Karácsony előtt tér haza.
JÓ:    A magyar csapat hétfőn, augusztus 3-án indul, és karácsony előtt tér haza.
Mikor NE: mondat elején, illetve ha a szó tulajdonnév része (`Magyar Nemzeti Bank`,
`Karácsony Gergely`).
Forrás: AkH. 12. 187., 194.

### HU-T09 · Intézménynév nagy, rendezvénynév kicsi · [FIX-IF: neutral, formal, legal] [AI:kozepes] [kern]

Mi ez: az intézmény többelemű hivatalos nevében minden tagot nagybetűvel kezdünk; a rendezvények,
programok, mozgalmak nevét viszont kisbetűvel — kivéve az intézményszerű, állandó rendezvényeket
(`Szegedi Szabadtéri Játékok`).
Miért írja így a gép: felcseréli a kettőt, mert angolul mindkettő Title Case.
ROSSZ: A Nemzetközi Űrkutatási Konferencia előadói a Magyar tudományos akadémián gyűltek össze.
JÓ:    A nemzetközi űrkutatási konferencia előadói a Magyar Tudományos Akadémián gyűltek össze.
Mikor NE: ha a rendezvény bejegyzett, védett név, vagy ha a szervező következetesen nagybetűvel
használja a saját anyagaiban — akkor márkanév.
Forrás: AkH. 12. 187., 191.

### HU-T10 · Összetett szavak kötőjelezése · [FIX] [AI:eros] [kern]

Mi ez: két szabály együtt.
**Második mozgószabály:** ha különírt szókapcsolathoz összetételi utótag járul, a szókapcsolatot
egybeírjuk, és az utótagot kötőjellel kapcsoljuk — `meleg víz` + `csap` → `melegvíz-csap`;
`mesterséges intelligencia` + `alapú` → `mesterségesintelligencia-alapú`.
**6:3-as szabály:** legalább három tagból álló és hat szótagnál hosszabb összetételt a fő
összetételi határon kötőjellel bontunk — `időjárás-jelentés`, `munkaerő-nyilvántartás`.
Miért írja így a gép: az angol különír vagy szóközzel tagol, és a magyar egybeírási szabályok
nem transzferálódnak.
ROSSZ: A délutáni időjárásjelentés alapján a szerelő kicserélte a meleg víz csapot.
JÓ:    A délutáni időjárás-jelentés alapján a szerelő kicserélte a melegvíz-csapot.
Mikor NE: a 6:3-as szabály **kétrészes** összetételre nem alkalmazható — `oktatástechnikai`,
nem `oktatás-technikai`, bármilyen hosszú is.
Forrás: AkH. 12. 139., 141.

### HU-T11 · Oxford-vessző · [FIX] [AI:eros] [kern]

Mi ez: azonos szerepű mondatrészek felsorolásában az `és`, `s`, `meg`, `vagy` kötőszó elé **nem**
teszünk vesszőt. Magyarul nincs Oxford-vessző.
Miért írja így a gép: az angol szerkesztői konvenció átvétele.
ROSSZ: A csomagban laptop, dokkoló, és fejhallgató van.
JÓ:    A csomagban laptop, dokkoló és fejhallgató van.
Mikor NE: **tagmondathatáron kötelező** a vessző az `és` előtt — `Megérkezett a csomag, és
azonnal kibontottuk.` Itt két állítmány két külön alannyal áll, ez nem felsorolás.
Kapcsolódó: HU-B21 (ne tegyél vesszőt gépiesen).
Forrás: AkH. 12. 243. · helyesiras.mta.hu

### HU-T12 · Idegen tulajdonnév toldalékolása · [FIX] [AI:kozepes] [kern]

Mi ez: két eset.
Több különírt elemből álló idegen névhez az `-i`, `-s` képzőt **kötőjellel** kapcsoljuk, és a nagy
kezdőbetűket megtartjuk: `New York-i`, `Los Angeles-i`, `Walter Scott-os`.
Néma betűre vagy szokatlan betűkapcsolatra végződő névhez kötőjellel (`Voltaire-rel`,
`Bordeaux-ban`, `iPhone-ra`), egyébként közvetlenül, a hasonulást kiírva (`Bachhal`, `Mozarttal`,
`Brahmsszal`).
Miért írja így a gép: a magyar toldalékolás idegen tövön a modell egyik leggyengébb pontja.
ROSSZ: A new yorki iroda Bach-hal foglalkozó tanulmányát az iPhonera töltöttem le.
JÓ:    A New York-i iroda Bachhal foglalkozó tanulmányát az iPhone-ra töltöttem le.
Mikor NE: ha a név magyarosan meghonosodott (`Bécsben`, `Párizsban`), ott nincs kötőjel.
Forrás: AkH. 12. 215., 217.

### HU-T13 · `-val/-vel` hasonulása kötőjel után · [FIX] [AI:kozepes] [kern]

Mi ez: ha a `-val/-vel`, `-vá/-vé` toldalékot kötőjellel kapcsoljuk számjegyhez, jelhez,
rövidítéshez vagy betűszóhoz, a `v` **hasonult** alakját mindig kiírjuk.
Miért írja így a gép: a hasonulás nem látszik az írásképben, a modell a csupasz toldalékot teszi ki.
Jelek: `HTML-el`, `15%-al`, `4-el`, `PhD-vel` helyett `PhD-val`.
ROSSZ: A kimenetet HTML-el állítjuk elő, és 15%-al csökkentjük a méretét.
JÓ:    A kimenetet HTML-lel állítjuk elő, és 15%-kal csökkentjük a méretét.
Mikor NE: nincs kivétel. Ez mindig hiba.
További példák: `4-gyel`, `DNS-sel`, `Bp.-tel`, `EU-val`, `SQL-lel`.
Forrás: AkH. 12. 163.

### HU-T14 · Angol mintájú különírás összetételekben · [FIX] [AI:kozepes] [kern]

Mi ez: az angolból két szóként átvett összetételeket a magyar egybeírja.
Miért írja így a gép: az angol `project management`, `data driven` szóközös alakja átjön.
Jelek: `projekt menedzsment`, `adat vezérelt`, `döntés hozás`, `ügyfél szolgálat`, `web fejlesztés`.
ROSSZ: A projekt menedzsment és az adat vezérelt döntés hozás javította a folyamatot.
JÓ:    A projektmenedzsment és az adatvezérelt döntéshozás javította a folyamatot.
Mikor NE: ha tényleg jelzős szerkezet, nem összetétel (`nagy projekt`, `friss adat`). A próba:
összetételben a jelentés több, mint a tagok összege, és a hangsúly az első tagon van.
Forrás: AkH. 12. 95., 100.

### HU-T15 · Vessző a mondatkezdő kötőszó után · [FIX] [AI:eros] [kern]

Mi ez: a magyar nem tesz vesszőt a mondat élén álló kapcsolóelem után.
Miért írja így a gép: az angol `Furthermore,` / `Moreover,` konvenciója.
Jelek: `Továbbá,`, `Emellett,`, `Ezen túlmenően,`, `Végül,`, `Ugyanakkor,`, `Ennek megfelelően,`.
ROSSZ: Továbbá, a rendszer támogatja a kétfaktoros hitelesítést. Ezen túlmenően, az adatokat
titkosítva tárolja.
JÓ:    A rendszer kétfaktoros hitelesítést is támogat, és titkosítva tárolja az adatokat.
Mikor NE: ha a mondatkezdő elem valódi közbevetés vagy megszólítás (`Egyébként, ha jól emlékszem,…`;
`Kedves Péter,`). Ott a vessző helyes.
A halmozott kapcsolóelemek összevonása már `06-rhythm.md`, HU-R04 — itt csak a vesszőt vedd ki.
Forrás: AkH. 12. 243.

---

## Amit ebben a passban keresni kell, sorrendben

1. `"…"` vagy `“…”` magyar mondatban → `„…”`
2. `—` és ` -- ` → ` – ` (a meglévő ` – ` marad)
3. `magyar-angol`, `2020-2024` típusú kapcsolatok → nagykötőjel
4. `1,250,000` és `3.5` → `1 250 000` és `3,5`
5. `8GB`, `60 %` → `8 GB`, `60%`
6. angol dátumsorrend és `2.-i` → magyar forma
7. Title Case címben és címsorban → kisbetű
8. `Hétfő`, `Augusztus`, `Magyar` → kisbetű
9. `-val/-vel` hasonulás kötőjel után
10. idegen név toldaléka
11. mozgószabály és 6:3
12. Oxford-vessző

Az 1–6. és a 9. gépiesen ellenőrizhető — ezeket futtasd le a kimeneten is, a Pass 6
önellenőrzés részeként.
