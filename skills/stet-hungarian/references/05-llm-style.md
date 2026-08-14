# Pass 4 — LLM-retorika és lexika

Ez a réteg a legfeltűnőbb, de **nem a legfontosabb**. A szólista-csere önmagában nem javít semmit:
ha a mondatszerkezet fordításízű marad, a szinonimacsere csak elfedi. Ezért fut ez a pass a
szerkezeti passok után — és ezért fog itt jóval kevesebbet találni, mint amennyit egy nyers
szövegen találna.

**Ez a fájl évjáratos.** A lexikai listák `[2026-08]` jelöléssel állnak, és 12–18 havonta
felülvizsgálandók: a modellek szókincse változik, a mai árulkodó szó holnap semleges lehet.
A `[kern]` jelölésű minták (szerkezeti retorika) stabilak.

**A `?` jelölés.** Ahol `?` áll az `AI:` érték után, az becslés, nem mérés. Ebben a passban
**minden `SOFT` minta `?`-jelölt**, kivétel nélkül — ahogy a katalógus egészében is. Ilyen minta
**önmagában soha nem indokol javítást** a pontszámon keresztül; csak a klaszterpontszámba számít
bele. Egyetlen kivétel a klaszter-felülírás, amit nem az `AI:` érték hordoz, hanem egy megnevezett
szerkezeti teszt — lásd a HU-L06-nál és a HU-L14-nél.

---

### HU-L01 · Üres nyomatékosító jelzők · [SOFT] [AI:eros?] [2026-08]

Mi ez: fokozás, ami nem közöl semmit.
Miért írja így a gép: a modell a fontosságot állítja, ahelyett hogy megmutatná.
Jelek: `kulcsfontosságú`, `elengedhetetlen`, `kiemelkedő jelentőségű`, `létfontosságú`,
`alapvető fontosságú`, `nélkülözhetetlen`, `meghatározó`.
ROSSZ: A rendszeres visszajelzés kulcsfontosságú és elengedhetetlen a csapat fejlődéséhez.
JÓ:    Visszajelzés nélkül a csapat nem fejlődik.
Mikor NE: ha az állítás valóban fokozást kíván, és a szerző kiáll mellette. Egyetlen
`kulcsfontosságú` egy hosszú szövegben nem AI-jel — a jel a **halmozás**.
Forrás: SZTE magyar AI-detektor (ellenőrizetlen, lásd `sources.md`) · e-nyelv.hu

### HU-L02 · Magyar AI-szótár · [SOFT] [AI:eros?] [2026-08]

Mi ez: a magyar LLM-szöveg visszatérő szókincse.
Jelek: `zökkenőmentes`, `megvilágít`, `ökoszisztéma`, `mélyebbre ásunk`, `robusztus`,
`holisztikus`, `szinergia`, `paradigmaváltás`, `game changer`, `felhasználóbarát`,
`innovatív megoldás`, `proaktív`, `hozzáadott érték`.
ROSSZ: A mai rohanó világban a zökkenőmentes integráció kulcsfontosságú, ezért érdemes mélyebbre
ásni a témában.
JÓ:    Az integrációnak észrevétlenül kell működnie.
Mikor NE: ha a szó **terminus** az adott szakmában (`ökoszisztéma` biológiában, `robusztus`
statisztikában, `proaktív` HR-szövegben). Ott nem klisé, hanem pontos szó. Szakszövegben ez a
minta gyakorlatilag nem fut.
Forrás: SZTE magyar AI-detektor · NKE: MI és az akadémiai szövegalkotás

### HU-L03 · Metaszöveges keretezés · [FIX] [AI:eros] [kern]

Mi ez: a modell bejelenti, mit fog mondani, ahelyett hogy mondaná.
Jelek: `Fontos megjegyezni, hogy`, `Érdemes megemlíteni, hogy`, `Az alábbiakban`,
`A következőkben bemutatjuk`, `Összefoglalva elmondható`, `Mint látható`, `Nézzük meg közelebbről`,
`Vágjunk bele`.
ROSSZ: Fontos megjegyezni, hogy a határidő csúszása több okra vezethető vissza.
JÓ:    A határidő két okból csúszott.
Mikor NE: ha a keret valódi szerkezeti funkciót lát el — hosszú dokumentumban egy `Az alábbiakban`
tényleg navigál. Egy tíz bekezdéses szövegben egy ilyen elem rendben van, ötben nem.
**És ha a keretet definíció vagy döntés követi, ne nyúlj hozzá.** A `Rögzítsük:` vagy a
`Megállapodtunk abban, hogy:` egy fogalommeghatározás vagy egy döntés előtt nem metaszöveg, hanem
jegyzőkönyvezés — a szerző „ezt most kimondom” gesztusa. Ugyanez áll a szabálykimondásra
(`A szabály a következő:`). Ez teljes kivétel, nem enyhítés: a minta ilyenkor egyszerűen nem fut.
A `Jelek` sor **zárt lista**: ne általánosítsd hasonló hangzású fordulatokra. Ami nincs rajta,
az nem HU-L03.
Forrás: hdmarketing.hu (alacsony hitelű, de konzisztens az SZTE-listával) · NKE

### HU-L04 · Klisés keretezés · [SOFT] [AI:eros?] [2026-08]

Mi ez: elkoptatott, készen kapott frázis konkrétum helyett.
Jelek: `a mai rohanó világban`, `a digitalizáció korszakában`, `tudás tárháza`, `letéteményese`,
`gazdag palettája`, `izgalmas utazás`, `új fejezet`, `mérföldkő`, `a jövő kulcsa`.
ROSSZ: A mai rohanó világban, a digitalizáció korszakában az adatvédelem a bizalom letéteményese.
JÓ:    Az adatvédelem az elmúlt öt évben lett üzleti kérdés a hazai cégeknél.
Mikor NE: ünnepi beszédben, méltatásban, marketingszövegben, ahol a pátosz a műfaj része.
`informal` profilban is óvatosan: a blogposzt megengedi az egy klisét.
Forrás: sulinet tudásbázis: nyelvi klisé

### HU-L05 · Univerzális nyitómondat · [FIX] [AI:eros] [kern]

Mi ez: az emberiség egészére hivatkozó bevezetés, ami nem közöl semmit.
Jelek: `Az emberiséget a kezdetek óta foglalkoztatja`, `A történelem során mindig`,
`A mai digitális világban`, `Nem véletlen, hogy`.
ROSSZ: Az emberiséget a kezdetek óta foglalkoztatja az időmérés kérdése.
JÓ:    Az első mechanikus órák a 13. században jelentek meg Európában.
Mikor NE: ha a szöveg tényleg történeti áttekintés, és a nyitás konkrét állítást tesz.
Forrás: Wikipedia: Signs of AI writing — „Undue emphasis on significance” magyar megfelelője
(CC BY-SA 4.0; a taxonómia onnan, a példák sajátok) · NKE

### HU-L06 · Negatív párhuzam · [SOFT] [AI:eros?] [kern]

Mi ez: a `nem csupán X, hanem Y is` és a `nem X, hanem Y` keret. **A szerkezet magyarul teljesen
helyes** — csak a halmozása gépies, és az, ha a tagadott fél szalmabáb.
Miért írja így a gép: az angol `not just X, but Y` az egyik legerősebb LLM-fordulat, és magyarul
is átjön.
ROSSZ: Ez nem csupán egy termék, hanem egy szemléletmód; nem egyszerűen gyorsabb, hanem alapjaiban
más.
JÓ:    A termék gyorsabb, és más elven működik.
Mikor NE: **ha valódi az ellentét, hagyd meg.** A teszt: állította-e bárki komolyan az X-et?
Ha nem, szalmabáb, és törölhető. Ha igen, a szembeállítás tartalmas.
Egy ilyen szerkezet bekezdésenként rendben van; kettő már jel.
Forrás: SZTE magyar AI-detektor (`már nem pusztán`; ellenőrizetlen, lásd `sources.md`)

**Klaszter-felülírás.** Ez a minta **önmagában klaszternek számít**, ha egy bekezdésben **kettő
vagy több** ilyen keret áll, **és** közülük legalább egy elbukik a szalmabáb-teszten. Nem kell
mellé másik jel, és a `neutral` emelt küszöbe sem alkalmazandó rá.

A teszt kettős kapuja szándékos, és ez az, ami falszifikálhatóvá teszi: az egy darab keret a saját
`Mikor NE`-je szerint rendben van, a valódi ellentét pedig akkor is rendben van, ha halmozódik.
A felülírás nélkül a minta gyakorlatilag néma — a `nem X, hanem Y` a legerősebb angolból átjövő
keret, és tipikusan egyébként tiszta bekezdésben áll, ahol sosem érné el a hármas küszöböt.

### HU-L07 · Túlzott hedging · [SOFT] [AI:eros?] [kern]

Mi ez: halmozott tompítás, ami a felelősséget veszi ki az állításból.
Jelek: `általánosságban elmondható`, `sok esetben`, `érdemes lehet`, `bizonyos mértékig`,
`számos tényező`, `bizonyos szempontból`, `viszonylag`.
ROSSZ: Általánosságban elmondható, hogy sok esetben érdemes lehet bizonyos mértékig felülvizsgálni
a folyamatot.
JÓ:    Ezt a folyamatot át kell szabni.
Mikor NE: **ez a legveszélyesebb minta a fájlban.** A hedge törlése nem stilisztikai, hanem
**episztemikus** művelet: a `sok esetben` elhagyása hamis általánosítást gyárt. Csak akkor javíts,
ha **egy mondaton belül kettő vagy több** tompító halmozódik, és akkor is csak a fölöslegeset
vedd ki — az állítás bizonyossági fokát nem szabad megemelni.
Tudományos és jogi szövegben a hedging kötelező elem. `formal` és `legal` profilban ne fusson.
Forrás: NKE: MI és az akadémiai szövegalkotás

### HU-L08 · Üresen járó igei körülírás · [SOFT] [AI:eros?] [kern]

Mi ez: elvont ige + `hogy`-os mellékmondat egyetlen konkrét ige helyett.
Jelek: `hozzájárul ahhoz, hogy`, `lehetőséget kínál`, `kihívást jelent`, `elősegíti`,
`támogatja azt, hogy`, `szerepet játszik abban, hogy`.
ROSSZ: Az új folyamat hozzájárul ahhoz, hogy a csapat hatékonyabban működjön, ugyanakkor kihívást
is jelent.
JÓ:    Az új folyamattal a csapat gyorsabban dolgozik, de előbb meg kell tanulnia.
Mikor NE: ha az ok-okozat tényleg részleges (`hozzájárul` ≠ `okozza`) — ott a körülírás pontos.
Forrás: Minya Károly, e-nyelvmagazin.hu

### HU-L09 · Üres létige-körülírás · [SOFT] [AI:kozepes?] [kern]

Mi ez: `rendelkezik`, `szolgál`, `képvisel`, `otthont ad`, `bír` a `van` vagy egy tartalmas ige
helyett.
Miért írja így a gép: hivatalosabbnak „érzi”, mint a létigét.
ROSSZ: A galéria a kortárs művészet bemutatóhelyeként szolgál, és négy kiállítóteremmel rendelkezik.
JÓ:    A galéria kortárs művészetet mutat be. Négy kiállítóterme van.
Mikor NE: **ez nem a létige kerülésének angol mintája** — az magyarra nem értelmezhető, mert a
magyar jelen idő E/3-ban amúgy sincs kopula. Itt kizárólag a fenti konkrét igékről van szó.
A `rendelkezik` jogi szövegben tartalmas (`a törvény úgy rendelkezik`), azt ne bántsd.
Forrás: Nyelvművelő kéziszótár

### HU-L10 · Mondatvégi határozói igenév · [SOFT] [AI:eros?] [kern]

Mi ez: a mondat végére ragasztott `tükrözve / hangsúlyozva / kiemelve / biztosítva` toldás. Az
angol mondatvégi `-ing`-toldás magyar megfelelője, és az egyik legmegbízhatóbb jel.
ROSSZ: A pályaudvar 1904-es acélszerkezete a korszak mérnöki magabiztosságát idézi, tükrözve a
város akkori gyors növekedését.
JÓ:    A pályaudvar acélszerkezete 1904-ben készült. A város akkoriban gyorsan növekedett.
Mikor NE: ha az igenév valódi módhatározó (`Sietve válaszolt.`), vagy ha a mondat elején áll —
az más szerkezet (HU-F07).
Ez a minta gyakran **kitalált értelmezést** is hoz magával: a toldás olyan jelentőséget állít,
ami nincs a forrásban. Ilyenkor a törlés nemcsak stílusjavítás.
Forrás: Wikipedia: Signs of AI writing — „Superficial analyses with -ing endings” magyar
megfelelője (CC BY-SA 4.0; a taxonómia onnan, a példák sajátok)

### HU-L11 · Akadémiai sablonfordulatok · [SOFT] [AI:eros?] [2026-08]

Mi ez: a tudományos szövegek készen kapott keretei tartalom nélkül.
Jelek: `jelen kutatás célja`, `átfogó képet nyújt`, `a kutatás újszerűsége`, `komplex módon`,
`a téma aktualitása`, `rávilágít arra, hogy`.
ROSSZ: Jelen tanulmány célja, hogy átfogó képet nyújtson a téma komplex összefüggéseiről.
JÓ:    Ebben a tanulmányban három kérdésre keresek választ.
Mikor NE: ha a műfaj tényleg megköveteli (pályázati űrlap, absztrakt kötött szerkezettel).
Ott a sablon a forma része.
Forrás: SZTE magyar AI-detektor (ellenőrizetlen, lásd `sources.md`) · NKE

### HU-L12 · Csevegőmaradványok · [FIX] [AI:eros] [kern]

Mi ez: a chatfelület fordulatai, amik bent maradtak a szövegben.
Jelek: `Íme`, `Természetesen!`, `Remélem, segítettem!`, `Szólj, ha kifejtsem`, `Nagyszerű kérdés!`,
`Összefoglalva a fentieket`, `Ha további kérdésed van`.
ROSSZ: Íme a francia forradalom áttekintése. Remélem, segítettem! Szólj, ha bármelyik részt kifejtsem.
JÓ:    A francia forradalom 1789-ben kezdődött, amikor a pénzügyi válság és az élelmiszerhiány
elégedetlenséghez vezetett.
Mikor NE: ha a szöveg tényleg beszélgetés átirata, vagy ha a `természetesen` tartalmas
módosítószó (`Természetesen fizetünk érte.`).
Forrás: közvetlen megfigyelés · Wikipedia: Signs of AI writing — „Collaborative communication
artifacts” (CC BY-SA 4.0)

### HU-L13 · Általános pozitív zárlat · [SOFT] [AI:eros?] [kern]

Mi ez: tartalmatlan, felfelé mutató lezárás, ami nem közöl semmit. A HU-L03 a **keretet** viszi
el (`Összefoglalva elmondható, hogy`), ez a minta a maradékot — a zárlat állítását magát.
Miért írja így a gép: a modell lezárást akar adni, de nincs mit lezárnia, ezért optimizmust ad.
Jelek — **zárt lista**, ne általánosítsd: `a jövő fényes`, `izgalmas idők várnak`, `jó úton
haladunk`, `ez fontos lépés a helyes irányba`, `a lehetőségek határtalanok`, `minden szempontból
megéri`. Ami nincs rajta, az nem HU-L13, tehát nem is törölhető ezen a címen.
Határeset: a **záró pozícióban álló aforizma** nem ide tartozik, hanem a HU-L14-hez — ott pedig
tilos a törlés. Csak akkor töröld, ha a mondat illeszkedik a fenti zárt listára.
ROSSZ: Összefoglalva elmondható, hogy a jövő fényes. Izgalmas idők várnak ránk.
JÓ:    (Töröld a bekezdést. Az utolsó konkrét tényen érjen véget a szöveg. Ha a forrásban van
valódi terv vagy szám, azt írd ide helyette — de újat ne találj ki.)
Mikor NE: ha a zárlat **konkrétumot** tartalmaz (dátum, szám, névvel megnevezett következő lépés),
akkor nem üres, hagyd. Marketing- és ünnepi szövegben a pozitív zárlat műfaji elem.
**Fontos:** ez a minta egész tagmondat vagy mondat törlését engedi, ami a fájl legagresszívebb
művelete. Ezért `SOFT`, és csak akkor fusson, ha a mondatban nincs egyetlen konkrét adat sem.
Forrás: Wikipedia: Signs of AI writing — „Generic positive conclusions” magyar megfelelője
(CC BY-SA 4.0; a taxonómia onnan, a példák sajátok)

### HU-L14 · Aforizma-formula · [SOFT] [AI:eros?] [kern]

Mi ez: idézhetőre csiszolt ál-bölcsesség — szimmetrikus, csattanós mondat, ami mély igazságnak
hangzik, de a konkrét állítást csak körülírja. A teszt maga a szabály: **kiemelhető lenne
LinkedIn-idézetnek a szövegkörnyezete nélkül? Akkor gyanús.**
Miért írja így a gép: a modell lezárásnak és nyomatéknak szánja; a kvázi-idézet formát a korpusz
jutalmazza, mert sokszor látta kiemelve.
Jelek: `X a Y valutája / nyelve / kulcsa / művészete`; birtokos metafora két elvont főnévből;
tükörszimmetria (`Aki nem mér, az nem tanul; aki nem tanul, az nem nő`); szentenciózus jelen idejű
általános alany (`Az ember akkor fejlődik, amikor...`).
ROSSZ: A bizalom a növekedés valutája. A jó csapat nem a hibákat kerüli, hanem a tanulás nyelvén
beszél.
JÓ:    A vevők akkor ajánlanak tovább minket, ha megbíznak bennünk. A jó csapat a hibáiból tanul.
Javítás: cseréld arra a konkrét állításra, amit a formula körülír — **a bekezdésben** keresd, ne az
egész szövegben. **Ha nincs ilyen, ne töröld: tedd a gyanús-listára.** Aforizmát nem pótolunk
aforizmával, de egész mondatot sem törlünk azért, mert üresen hangzik.

**Ez a minta jellemzően jelez, nem átír — és ez a szándékolt viselkedés, nem sikertelen futás.**
A felülírás akkor tüzel, ha a bekezdésben *nincs* konkrétum; a csere viszont épp konkrétumot
igényel. A két ablak alig fedi egymást, tehát a tipikus kimenet a gyanús-lista. Ne érezd
hiányosnak, és ne nyúlj emiatt a cseréhez.

**Klaszter-felülírás.** Ez a minta **önmagában klaszternek számít**, ha a LinkedIn-teszt elbukik
**és** a mondat mögött a bekezdésben nincs konkrét eset (szám, dátum, név, megnevezett esemény).
Nem kell mellé másik jel, és a `neutral` emelt küszöbe sem alkalmazandó rá.
Enélkül a minta halott, ugyanabból az okból, amiből a HU-R09 és a HU-R11 is az volt: az aforizma
tipikusan **magányosan** áll egy egyébként tiszta bekezdésben, egy `eros` minta pedig 2 pont, a
küszöb 3 vagy 4. Ha van a bekezdésben konkrétum, a minta nem tüzel önmagában — akkor az olvasónak
van hol földet érnie.

Mikor NE:
- Mottó, cím, szándékos szlogen, marketing- és kampányszöveg, ahol az idézhetőség maga a cél.
  Valódi, tulajdonnévhez kötött idézet érinthetetlen zóna.
- **Definícióban.** Az `X az a pont, ahol…` alakú fogalommeghatározás alakilag hasonlít, de a
  tartalma épp a pontosítás.
- **Ha a mondat konkrét döntést indokol** a saját mondatán belül vagy közvetlenül mellette
  (`a találgatás rosszabb, mint a nyitva hagyott kérdés` — és ott áll mellette, hogy melyik
  kérdést hagyták nyitva, és miért). Az ilyen nem ál-bölcsesség, hanem indoklás.
- Töredékes, ritmust adó mondatpárra — az a „megőrizendő jegyek” közé tartozik.
**Precedencia a HU-R11-gyel.** Mindkettő illik az elvont mondatra, ezért kötött a sorrend:
**ha a mondat csiszolt vagy szimmetrikus — birtokos metafora, tükörszerkezet, szentencia —,
a HU-L14 nyer** (specifikusabb). Ha csak lapos és elvont, a HU-R11. Egy mondatra **soha ne
alkalmazd mindkettőt.** A gyógymód mindkettőnél azonos: konkrét állításra cserélni, ha van a
forrásban; ha nincs, gyanús-lista. Így a routing nem dönthet törlés és megtartás között.
Forrás: közvetlen megfigyelés. Az angol nyelvű prózajavító gyakorlatban ugyanez a jelenség
„aforizma-formula”, illetve „idézhetőség” néven ismert — a magyar alakteszt és a példák sajátok.

---

## Klaszterszabály ehhez a passhoz

A `SOFT` minták itt szinte mind `?`-jelöltek vagy évjáratosak, ezért egyetlen találat **soha** nem
elég. A pontértékek, a küszöb és a bekezdésenkénti korlát a `SKILL.md`-ben állnak, egy helyen —
itt szándékosan nem ismételjük meg őket.

Egy `kulcsfontosságú` önmagában nem AI-jel. Egy `kulcsfontosságú` + `a mai rohanó világban` +
`nem csupán… hanem` + hármas felsorolás egy bekezdésben viszont vallomás.
