# Tiltólista – amihez nem szabad hozzányúlni

Ez a fájl másképp működik, mint a többi. **Nincs benne ROSSZ/JÓ példapár, és ez szándékos.**
Egy példapár átírási műveletet tanít. Ezek a tételek viszont nem átírást írnak elő, hanem
megtiltják – ha példapárt adnánk hozzájuk, az eszköz elkezdené *gyártani* a jelölt alakokat,
vagyis sztenderd szövegbe írna bele nákolást, archaizmust, regionális formát. Ezért minden tétel
felsorolja, **mit ne bántson**, és megindokolja, **miért merül fel egyáltalán**.

A magyar nyelvművelői hagyomány miatt egy nyelvi modell alapból hiperkorrigál. A hiperkorrekció
pedig pont azt csinálja, amit el akarunk kerülni: hivataloskodóbbá, tehát **gépiesebbé** teszi a
szöveget. Ez a fájl a skill legfontosabb része.

**Egyirányúsági szabály.** Ahol egy tétel irányt jelöl, az az irány kötött. A visszafelé csere
minden esetben tilos, akkor is, ha a szöveg amúgy indokolná.

---

## Nyelvtani babonák

### HU-B01 · A `-va/-ve van` szerkezet · [NEVER] [kern]

Ne nyúlj hozzá: `be van csukva`, `meg van írva`, `ki van fizetve`, `biztosítva van`,
`el van intézve`, `le lett zárva`, `meg lett oldva`.

Miért merül fel: 19. századi germanizmus-vád. Szepesy 500 évnyi adattal cáfolta – a szerkezet a
14. századi Jókai-kódextől Balassin, Petőfin, Aranyon, Kosztolányin át adatolt, és a vogulban is
megvan. A német szerkezet ráadásul szerkezetileg más.

Amit tilt: az állapotjelölő `-va/-ve van` átírását cselekvő múltra. A csere **jelentést változtat**:
a `le van zárva` állapot, a `lezárták` esemény.

Ami viszont tényleg idegenszerű, és a `03-grammar.md`-ben javítandó: a befejezett melléknévi igenév
névszói állítmányként – `az ajtó becsukott`, `a számla kifizetett`. Ez nem ugyanaz a szerkezet.

Forrás: Szepesy Gyula: Nyelvi babonák, 1. fejezet · Kálmán László, nyest.hu

### HU-B02 · `ami` → `amely` csere · [NEVER] [kern]

Ne cseréld `amely`-re az `ami`-t.

Miért merül fel: iskolai szabályként terjed, hogy az `ami` csak általános névmásra utalhat vissza.
Egész tagmondatra visszautalva az `ami` a normatív alak, és a köznyelvben főnév után is helyes.

Amit tilt: a gépi cserét mindkét irányban. Az `amely` ilyenkor hiperkorrekció, és hivataloskodóbbá
teszi a szöveget – vagyis rontja, amit javítani akarunk.

Forrás: nyest.hu: Ami és amely (Deme László álláspontjára) · Szepesy, 6. fejezet

### HU-B03 · Mondatkezdő kötőszó · [NEVER] [kern]

Ne írd át és ne töröld a mondat élén álló `De`, `És`, `Mert`, `Hát`, `Viszont` kötőszót.

Miért merül fel: fogalmazástanítási tanács, amit nyelvi szabályként adnak tovább. A Nyelvművelő
kézikönyv szerint is csak *szöveget* nem kezdünk kötőszóval, mondatot igen.

Amit tilt: az átírást hátravetett `azonban / mindazonáltal / ugyanakkor` láncra. Ez a csere
egyszerre hivataloskodóbb és monotonabb, tehát két AI-jelet ad hozzá.

Kapcsolódó precedencia: lásd lent, a mondatkezdő `azonban` kérdését.

Forrás: e-nyelv.hu: kötőszó mondat elején · Pölcz Ádám, kultura.hu

### HU-B04 · `de viszont` · [NEVER] [2026-08]

Ne bontsd szét és ne egyszerűsítsd `de`-re vagy `viszont`-ra.

Miért merül fel: tautológiának szokás bélyegezni. A magyar nyelv nagyszótára négy külön
jelentésárnyalattal tartja nyilván, tehát önálló összetett kötőszó.

Amit tilt: az automatikus átírást. Kötetlen és élőbeszédet idéző szövegben a szétbontás
regiszterhibát okoz. Formális és jogi szövegben magától sem fog előfordulni.

Forrás: Schirm Anita: A deviszont viszontagságai, nyest.hu

### HU-B05 · Kettős tagadás · [NEVER] [kern]

Ne töröld a második tagadószót: `nem láttam senkit`, `soha nem mondta`, `amíg meg nem jön`.

Miért merül fel: „logikátlan”, mert két tagadás állítás – ez a latin-logikai érvelés a magyarra
nem áll. A magyar tagadószó-egyeztető nyelv: a `senki / semmi / soha` mellett a `nem` **kötelező**.

Amit tilt: az angol mintájú átírást. A `nem láttam valakit` nem stílushiba, hanem hibás mondat.

Forrás: É. Kiss Katalin: Tagadás · nyest.hu: Hogy miket (nem) mondunk?!

### HU-B06 · Élettelen alany cselekvő igével · [NEVER] [kern]

Ne írd körül: `a tanulmány kimutatja`, `döntés született`, `a szerződés kimondja`, `az adatok azt
mutatják`.

Miért merül fel: a „csak élőlény cselekedhet / születhet” logikai kifogás. Szepesy külön fejezetet
szentel neki („Sétálhat-e az utca?”).

Amit tilt: emberi cselekvő beírását pusztán azért, mert az alany élettelen. A körülírás
hosszabb és hivataloskodóbb lesz.

Forrás: Szepesy, 13. fejezet · Pölcz Ádám: Alanyi jogon

### HU-B07 · Személyes névmás élettelenre · [NEVER] [kern]

Ne cseréld `az / azokat / abból` alakra az `ő / őket / belőle` névmást csak azért, mert élettelenre
utal.

Miért merül fel: „a személyes névmás csak személyre vonatkozhat” – ilyen szabály nincs.

Forrás: Fejes László, nyest.hu

### HU-B08 · `-tatik / -tetik` igealakok · [NEVER] [kern]

Ne írd át a megkövült szenvedő alakokat: `kéretik`, `tétetik`, `megmérettetett`, `adatik`.

Miért merül fel: idegen elemnek tartják. Magyar képzőkből állnak; a stílusértékük archaikus vagy
ironikus, de nem hibásak.

Amit tilt: a törlést és a „modernizálást”. **És a fordított irányt is:** soha ne állíts elő
`-tatik/-tetik` alakot sztenderd szövegből.

Forrás: Kálmán László: A magyar nyelv hősies harca a szenvedő szemlélettel, nyest.hu

### HU-B09 · `kell menjek`, `kell legyen` · [NEVER] [kern]

Ne sztenderdizáld `el kell mennem` alakra.

Miért merül fel: regionális (elsősorban erdélyi) és köznyelvi változat, amit hibának tanítanak.
Nem az.

Amit tilt: a javítást élőbeszédben, párbeszédben, idézetben, erdélyi hangban. **És a fordított
irányt is:** soha ne gyárts `kell menjek` alakot sztenderd mondatból.

Forrás: MTA Nyelvtudományi Intézet, nyelvművelő GYIK

### HU-B10 · Suksükölés, szukszükölés, nákolás · [NEVER] [kern]

Ne javítsd idézett beszédben, párbeszédben, nyelvjárási hangban: `elhalasszuk` (felszólító alakú
kijelentő), `megnákolt` feltételes alakok.

Miért merül fel: erősen stigmatizált, ezért hibának tűnik. Rendszerszerű nyelvjárási jelenség,
nem nyelvtani hiba.

Amit tilt: két dolgot. A javítást ott, ahol a forma a szereplő hangja – **és minden olyan
műveletet, ami ilyen alakot állít elő** sztenderd szövegből. Ez utóbbi a súlyosabb: az eszköz
nem írhat bele stigmatizált formát a felhasználó szövegébe. Lásd a záró meta-szabályt.

Forrás: Sinkovics Balázs: A suksükölő igeragozás · nyest.hu

### HU-B11 · Páros testrész birtokos többese · [NEVER] [kern]

Ne egységesítsd egyik irányba sem: `fáj a lábam` és `fájnak a lábaim` egyaránt helyes.

Miért merül fel: „a magyar a páros testrészt egyes számban mondja” – féligazság; Szepesy épp azt
mutatja ki, hogy a klasszikusok mindkettőt használják.

Amit tilt: **mindkét irányú cserét.** Ez a tétel no-op: hagyd, ahogy a szerző írta.

Forrás: Szepesy: Fáj a lábam – fájnak a lábaim

### HU-B12 · `miatt` → `végett` · [NEVER] [kern]

Soha ne írd át `végett`-re az okot jelölő `miatt`-ot.

Miért merül fel: a „végett csak célt jelölhet” szabály történetileg gyenge alapú, de a *fordított*
csere valódi hiperkorrekciós hiba, és az egyik legfeltűnőbb.

Egyirányú: az okhatározói `végett` → `miatt` javítás **megengedett** (lásd `substitutions.md`).
Visszafelé soha.

Forrás: nyest.hu: Mi végett kell beszólni? · A hiperkorrekció

---

## Stilisztikai babonák

### HU-B13 · Szóismétlés · [NEVER] [kern]

Ne keress szinonimát a kulcsszóra, és ne írd körül.

Miért merül fel: az angol „elegant variation” elvárás átvétele. A magyar szakszöveg és a köznyelv
ugyanazon a néven nevezi ugyanazt; a szinonimakényszer zavarosabb, mint az ismétlés.

Amit tilt: a szinonimacserét terminuson, kulcsszón, tulajdonnéven. A „színes” váltogatás
önmagában AI-jel.

**Precedencia:** ez a tétel felülírja minden olyan mintát, amely változatosságot ír elő.

Forrás: nyest.hu: Miért kell félni a szóismétléstől?

### HU-B14 · Diskurzusjelölők · [NEVER] [kern]

Ne töröld: `hát`, `ugye`, `szóval`, `persze`, `tulajdonképpen`, `amúgy`, `izé`, `nos`.

Miért merül fel: „töltelékszónak” tanítják őket. Pragmatikai funkciójuk van, és jelentős részben
ezek adják a szöveg emberi hangját – pont azt, amit a skill meg akar őrizni.

Amit tilt: a törlést kötetlen és félkötetlen regiszterben. A mondatkezdő `hát` nem cserélhető
mesterkélt `nos`-ra.

**Precedencia:** ütközik a töltelékszó-törlő mintákkal. Feloldás lent.

Forrás: Schirm Anita: Diskurzusjelölők szövegeken innen és túl

### HU-B15 · Álpleonazmusok · [NEVER] [kern]

Ne irtsd: `ma már`, `visszatér`, `külön-külön`, `egyes-egyedül`, `lelki szemei előtt`.

Miért merül fel: szószaporításnak látszanak. Jelentéskülönbséget vagy nyomatékot hordoznak.

Forrás: nyest.hu: Henye szavak és társaik · Schirm Anita: Pleonazmus és tautológia

### HU-B16 · Meggyökeresedett idegen szavak · [NEVER] [kern]

Ne magyarítsd erőszakkal.

Miért merül fel: purizmus. Csak akkor cseréld, ha a magyar megfelelő tényleg használatban van
**és** érthetőbb – nem azért, mert magyarabb.

Kivétel: terminológiai következetesség. Egy fogalmat egy szövegen belül egyféleképpen nevezz;
ez viszont már nem purizmus, hanem `05-llm-style.md`.

Forrás: nyest.hu: 100% magyar termék – A nyelvi purizmus

### HU-B17 · Alárendelés mellérendelésre bontása · [NEVER] [kern]

Ne bontsd szét az alárendelő összetett mondatot mellérendelő láncra azzal az indokkal, hogy „az
alárendelés nem magyaros”.

Miért merül fel: 19. századi nyelvművelői tétel. A szétbontás halmozott `és`-eket és gyerekes
ritmust hoz – vagyis rontja a szöveget.

Ez nem azonos a `06-rhythm.md` mondatbontásával: ott a **túl hosszú** mondat tagolásáról van szó,
konkrét hossz alapján, nem az alárendelés elvi kerüléséről.

Forrás: nyest.hu: Lelkes mondatok

### HU-B18 · Idiomatikus funkcióigés szerkezetek · [NEVER] [kern]

Ne rövidítsd egyszerű igére: `köszönetet mond`, `zajt csap`, `zokon vesz`, `megadja az engedélyt`,
`számot ad`.

Miért merül fel: a terpeszkedő kifejezések listája mellé sodródnak. Ezek idiomatikusak, vagy más a
stílusértékük, mint az egyszerű igének.

Ide tartozik az is, amikor a szerkezet főnévi tagja definiált szakszó, amiből csak elvonással
lehetne igét gyártani: `házkutatás`, `tényállítás`, `magánindítvány`, `óvadék`.

**Precedencia:** ez a tétel felülírja a `04-officialese.md` terpeszkedés-mintáit. Ha bizonytalan
vagy, hogy egy szerkezet idiomatikus-e, ne nyúlj hozzá.

Forrás: Nyelvművelő kézikönyv 3. kategóriája (Heltai–Gósy, Magyar Nyelvőr 129) · B. Kovács Mária,
Magyar Nyelvőr 123

### HU-B19 · Formális kötőszavak és névutók hivatalos szövegben · [NEVER] [kontextus: formal, legal]

Ne cseréld automatikusan: `amennyiben`, `illetően`, `vonatkozásában`, `tekintetében`, `esetén`.

Miért merül fel: a plain-language ajánlások egyszerűsítést kérnek. Jogi és hivatali regiszterben
ezek helyénvalók, és a lecserélés **regisztertörést** okoz – ami rosszabb hiba, mint a terjengősség.

Egyirányú és regiszterfüggő: `informal` és `neutral` profilban a csere megengedett
(`substitutions.md`), `formal`-ban csak klaszterben, `legal`-ban soha.

Forrás: Lanstyák István: A nyelvi aformalizmus és a formális stílus, Fórum Társadalomtudományi Szemle

---

## Helyesírási babonák

### HU-B20 · AkH. 12. vagylagos formái · [NEVER] [kern]

Ne javítsd vissza a 11. kiadás szerint. Mindkét alak helyes: `1-jén` ~ `1-én`, `18.30` ~ `18:30`,
`e-mail` ~ `ímél`. Az AkH. 12. megváltoztatta: `nyitvatartás` (üzemidő értelemben), `kerekesszék`,
`elsőfokú`, `észszerű`.

Amit tilt: a „javítást” ott, ahol nincs hiba. Egy szövegen belül viszont **legyen következetes** –
ha a szerző kevert, egységesítheted a gyakoribbra, és ezt jelezd.

Forrás: helyesiras.mta.hu: Az AkH. 12. változásairól

### HU-B21 · Vessző `és`, `hogy`, `mint` előtt · [NEVER] [kern]

Ne tegyél vesszőt gépiesen.

- `és` előtt: halmozott mondatrészek között és ugyanahhoz az alanyhoz tartozó két állítmány között
  **nincs** vessző.
- `hogy` előtt: az `anélkül / ahelyett / aszerint hogy` szerkezetben a vessző a kapcsolóelem elé
  kerül, a `hogy` elé nem.
- `mint` előtt: hasonlítás nélkül nem kell vessző.

Forrás: helyesiras.mta.hu: A tanárok vesszőparipája

### HU-B22 · `Ön` / `ön` nagy kezdőbetűje · [NEVER] [kern]

Ne egységesítsd nagybetűre, és ne írd át kisbetűre.

A megszólítottra utaló 2. személyű névmás levélben tiszteletből nagybetűvel írható (`Ön`, `Téged`),
de a kisbetűs alak sem hiba. A tisztelet jelzése **nem terjed ki más szavakra** – a `Cégünk`,
`Munkatársaink` nagybetűzése viszont már hiba, azt javítsd.

Forrás: AkH. 12. 147. · helyesiras.mta.hu: Nagy Ön, kicsi ön

### HU-B23 · `jelen szerződés` névelő nélkül · [NEVER] [kontextus: formal, legal]

Ne tedd ki a névelőt: `jelen szerződés`, `jelen dokumentum`, `jelen szabályzat`.

Ünnepélyesebb, de nem hibás. Hivatalos iratban hagyd.

Forrás: e-nyelv.hu: (a) jelen

---

## Precedencia – a nyolc ütköző szabálypár

Ezek a párok nyíltan ellentmondanak egymásnak. A feloldás kötelező, nem mérlegelés tárgya.

| Ütközés | Feloldás |
|---|---|
| `amennyiben → ha` csere vs. HU-B19 | A regiszter dönt. `informal`/`neutral`: cserélj. `formal`: csak klaszterben. `legal`: soha. |
| Minden hármas felsorolás gyanús vs. „a hármasság önmagában nem AI-jel” | A hármasság **csak klaszterben** számít. Egyetlen hármas felsorolás soha nem indok. |
| Töltelékszó-törlés vs. HU-B14 (diskurzusjelölők) | A diskurzusjelölő nyer. Törölni csak a tartalmatlan fokozókat szabad (`gyakorlatilag`, `alapvetően`), a pragmatikai jelölőket soha. |
| Dokumentációs T/1 (`nézzük meg`) vs. önözési norma | A **meglévő** forma nyer. Ha a szöveg már választott, tartsd meg; ha nincs benne megszólítás, ne vigyél be. |
| Mondatkezdő kötőszó szabad (HU-B03) vs. „az `azonban` ne álljon elöl” | HU-B03 nyer. Az MTA-blog maga mondja, hogy az élen álló `azonban` előfordul – nincs tiltás. |
| Páros testrész egyes vs. többes szám | HU-B11: no-op. Egyik irányba se. |
| HU-L14 (aforizma) vs. HU-R11 (elvont állítás) – mindkettő illik | Csiszolt, szimmetrikus mondatra HU-L14 nyer; laposan elvontra HU-R11. Egy mondatra soha mindkettőt. A gyógymód azonos: **a bekezdésben** keresett konkrétumra cserélni, ha van; ha nincs, gyanús-lista – egyik sem töröl. |
| Záró pozícióban álló aforizma: HU-L14 vs. HU-L13 (törölhet!) | HU-L14 nyer, tehát **nem törölhető** – kivéve, ha a mondat illeszkedik a HU-L13 zárt `Jelek` listájára. Ez a pár azért kritikus, mert a HU-L13 azon két minta egyike, amelyik egész mondatot töröl (a másik a HU-R10). |

---

## Meta-szabály: ne gyárts emberséget hibából

A humanizálás **soha** nem jelenthet szándékos hibát vagy regisztertörést. Konkrétan tilos:

- helyesírási hibát bevinni, hogy „emberibb” legyen;
- stigmatizált alakot (suksükölés, nákolás, `kell menjek`) előállítani ott, ahol nem volt;
- archaizmust (`-tatik/-tetik`) beírni sztenderd szövegbe;
- idiómát, partikulát, szólást betenni oda, ahol nem volt – az idiómasűrűség ugyanúgy
  fordításízt ad, mint a hiánya;
- a regisztert lefelé vinni (hivatalosból társalgásiba) a szerző jelzése nélkül.

Ha egy javítás csak úgy tenné emberibbé a szöveget, hogy közben hibát visz bele, akkor nem javítás.
Hagyd, és írd a „gyanús, de nem javítottam” listára.
