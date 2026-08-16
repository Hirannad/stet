---
name: stet-hungarian
description: |
  Remove signs of machine-generated and translated writing from Hungarian text. Use when
  editing, reviewing, or rewriting Hungarian prose that reads as AI-written, machine-translated,
  or bureaucratic. Detects Hungarian-specific tells: English-calque syntax (translationese),
  nominalisation chains, officialese and light-verb constructions, lost focus and word order,
  Hungarian quotation marks and dashes, LLM vocabulary, and uniform rhythm. Register-aware, with an
  explicit do-not-touch list of Hungarian prescriptive myths so the rewrite never hypercorrects.
  Hungarian text only — hand off if the text is in another language. Selection follows the language
  of the TEXT, not of the request: prefer this over any language-neutral prose or "humanizer" tool
  whenever the text is Hungarian, even when the request is phrased in English, because four common
  English prose rules prescribe the opposite of the Hungarian norm. Not a spell checker — ordinary
  human typos are out of scope by design.
  Triggers: magyar szöveg, magyartalan, gépi szöveg, tükörfordítás, hivataloskodó, AI-szagú,
  ChatGPT írta, gépi magyar szöveg javítása; de-AI this Hungarian draft, Hungarian text reads as
  AI-written, fix machine-translated Hungarian.
license: MIT
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.2.0"
  method: 1
  lists-reviewed: "2026-08"
---

# stet – magyar

*stet* – korrektúrajel: „maradjon”. Ez a skill magyar szövegből veszi ki azt, ami gépinek vagy
fordítottnak hat. **Nem** nyelvhelyességi korrektor, és **nem** nyelvművelő eszköz.

**A katalógus eredet-alakú, és ez hatókör, nem hiány.** A minták arra vannak kiélezve, ami
*géptől* jön. A hétköznapi emberi helyesírási hiba – elmaradt kettőzés, kétfelé írt összetétel,
rosszul kötőjelezett szóösszetétel – ezért **rendszeresen kicsúszik**, még akkor is, ha a szövegben
az az egyetlen kétségtelen hiba. Ha helyesírás-ellenőrzésre van szükség, az másik szerszám.

Két, egymástól független jelforrást kezel:

- **Fordításnyelv.** A modell latens angolból állítja elő a magyart, ezért a mondatszerkezet
  angol marad akkor is, ha a szöveget senki nem fordította. Ez a hangosabb jel.
- **LLM-retorika.** Metaszöveg, üres fokozás, hedging, klisés keretezés, egyenletes ritmus.

**Miért nyelvenként külön katalógus.** Az angol nyelvű prózajavító listák négy szabálya magyarul
az ellenkezőjét írná elő, mint a norma: a `„…”` idézőjel és a szóközös gondolatjel helyes magyar
forma; a szenvedő szerkezet tiltása babona; a kopulakerülés értelmezhetetlen, mert a magyar
E/3-ban nincs kopula. A gépezet – a súlyossági szintek, a regiszterkapuk, a klaszterküszöb, a
javítási költségvetés, az önellenőrzés – nyelvfüggetlen; a **minták és az értékek nem azok.**

## Nyelvi kapu – ez fut mindennél előbb

**A szöveg nyelve dönt, nem a kérésé.** Ha angolul kérnek meg, hogy javíts ki egy magyar
bekezdést, ez a skill a helyes; ha magyarul kérnek meg egy angol szöveghez, nem ez.

1. Állapítsd meg a **szöveg** nyelvét, és mondd ki egy sorban, ahogy a regisztert is.
2. Ha a szöveg nem magyar: **állj meg, és ne javíts.** Mondd meg, melyik nyelvű, és add át a
   megfelelő eszköznek. Egy másik nyelvre szabott lista mechanikus alkalmazása magyar szövegen –
   és fordítva – pont a fenti négy megfordult szabályon okoz kárt.
3. **Vegyes nyelvű szöveg:** ha a szöveg túlnyomórészt magyar, de vannak benne idegen nyelvű
   szakaszok (idézet, terméknév, kódrészlet, angol bekezdés), a kisebbségi nyelvű szakaszok
   **érinthetetlen zónák**. Magyar marketingszöveg angol terméknevekkel a tipikus eset: a magyar
   próza javítható, az angol betétek nem.

## A nem javítás az alapértelmezett

Ez a legfontosabb szabály, ezért áll elöl. **Bizonytalanság esetén ne nyúlj hozzá – írd a listára.**

A magyar nyelvművelői hagyomány miatt egy nyelvi modell alapból hiperkorrigál, és a hiperkorrekció
hivataloskodóbbá, tehát **gépiesebbé** teszi a szöveget. A túljavítás itt nem apró kockázat, hanem
a leggyakoribb hibamód.

## Tiltólista

Ezekhez soha ne nyúlj. Az indoklás a `references/do-not-touch.md`-ben van, de a lista maga itt áll,
mert akkor is érvényes, ha egyetlen referenciafájlt sem nyitsz meg.

1. `-va/-ve van` (`be van csukva`, `meg van írva`, `le lett zárva`) – nem germanizmus.
2. `ami` → `amely` csere. Soha, egyik irányba sem.
3. Mondatkezdő `De`, `És`, `Mert`, `Hát`, `Viszont`.
4. `de viszont` – szótározott összetett kötőszó.
5. Kettős tagadás (`nem láttam senkit`) – a magyarban kötelező.
6. Élettelen alany cselekvő igével (`a tanulmány kimutatja`).
7. Személyes névmás élettelenre (`őket`, `belőle`).
8. `-tatik/-tetik` alakok – és soha ne is gyárts ilyet.
9. `kell menjek`, `kell legyen` – és soha ne is gyárts ilyet.
10. Suksükölés, nákolás idézett beszédben – és soha ne is gyárts ilyet.
11. Páros testrész egyes vagy többes száma – no-op mindkét irányban.
12. `miatt` → `végett`. (Visszafelé, `végett` → `miatt`, megengedett.)
13. Szóismétlés a kulcsszón. Ne keress szinonimát; a szinonimalánc maga a gépi jel.
14. Diskurzusjelölők: `hát`, `ugye`, `szóval`, `persze`, `tulajdonképpen`, `amúgy`, `izé`, `nos`.
15. Álpleonazmusok: `ma már`, `visszatér`, `külön-külön`.
16. Meggyökeresedett idegen szavak – a purizmus nem cél.
17. Alárendelés mellérendelésre bontása.
18. Idiomatikus funkcióigés szerkezetek: `köszönetet mond`, `zajt csap`, `házkutatást tart`.
19. Formális kötőszavak `formal` és `legal` szövegben: `amennyiben`, `vonatkozásában`.
20. AkH. 12. vagylagos formái: `1-jén` ~ `1-én`, `18.30` ~ `18:30`.
21. Vessző gépies kitétele `és`, `hogy`, `mint` elé.
22. `Ön` / `ön` nagybetűzése – egyik irányba sem.
23. `jelen szerződés` névelő nélkül hivatalos iratban.

**És a meta-szabály: soha ne gyárts emberséget hibából.** Szándékos helyesírási hiba, stigmatizált
alak, archaizmus, regisztertörés nem humanizálás. Ha egy javítás csak úgy tenné emberibbé a
szöveget, hogy hibát visz bele, akkor nem javítás.

## Regiszter

Négy profil. A `neutral` az alapértelmezés.

| profil | tipikus szöveg |
|---|---|
| `informal` | blog, marketing, közösségi poszt, chat |
| `neutral` | dokumentáció, e-mail, termékszöveg |
| `formal` | üzleti levél, riport, akadémiai szöveg |
| `legal` | szerződés, hatósági irat, szabályzat |

A hivatali regiszter nem hiba: jogi szövegben a formális névszói szerkezet helyénvaló, és beszélt
nyelvire cserélve a szöveg joghatást veszít.

**Egy szöveg két profilra is illeszkedhet, és ez a gyakori eset, nem a kivétel.** Egy
marketingstratégiai dokumentum a témája szerint `informal` (marketing), a műfaja szerint `neutral`
(dokumentáció). A feloldás kötött, és itt áll, nem három fájllal beljebb:

1. **A csatorna dönt, nem a téma.** Ahol a szöveg megjelenik: chat, poszt, blog → `informal`;
   e-mail, dokumentáció, súgó → `neutral`; riport, tanulmány → `formal`.
2. **Ha a csatorna sem dönt, a szigorúbb profil nyer** – vagyis az, amelyik kevesebb passzt
   engedélyez. A téves `formal` kezelés nem javít valamit, amit lehetne; a téves `informal`
   kezelés átír valamit, amit nem szabadna.

**A pass-mátrix egyetlen helyen áll: `references/registers.md`.** Sem ez a fájl, sem a pass-fájlok
nem ismétlik meg – két helyen leírva előbb-utóbb két különböző szabály lenne belőle.

**A regisztert ki kell mondanod egy sorban, mielőtt bármit átírsz.** Például: *A szöveget `neutral`
regiszterként kezelem.* Csendes regiszterváltás tilos. A pass-mátrix és a megszólítási szabályok a
`references/registers.md`-ben vannak – **olvasd be, mielőtt regisztert döntesz, ne emlékezetből
dolgozz.**

## Jelölésrendszer

Két tengely, mert két külön kérdésre válaszolnak. A `status` azt mondja meg, **mit tegyél**; az
`AI:` azt, **mennyi bizonyítékot ér**.

```
### HU-T01 · Angol idézőjel magyar szövegben · [FIX] [AI:eros] [kern]
### HU-H02 · `-ásra/-ésre kerül` · [FIX-IF: informal, neutral] [AI:kozepes] [kern]
### HU-L01 · Üres nyomatékosító jelzők · [SOFT] [AI:eros?] [2026-08]
```

| címke | jelentés |
|---|---|
| `FIX` | mindig javítsd, regisztertől függetlenül |
| `FIX-IF` | csak a felsorolt profilokban |
| `SOFT` | csak klaszterben |
| `NEVER` | ne nyúlj hozzá |
| `[jelöld]` | ne javítsd, csak írd a listára |

**A `?` a becslés jele, és fék.** A katalógus **mind a 47 `SOFT` mintája `?`-jelölt.** A `?` nem
azt jelöli, hogy a nyelvészet ingatag – a források valódiak, és van köztük számszerű is. Azt jelöli,
hogy **a gépi gyakoriságra** nincs hivatkozható mérésünk, márpedig az `AI:` érték épp azt állítja
(`references/sources.md` kimondja, miért). `?`-jelölt minta **önmagában soha nem indokol javítást a pontszámon keresztül** –
csak a klaszterpontszámba számít bele. A `FIX` és `FIX-IF` minták `?` nélkül állnak, mert nem gépi
evidenciára hivatkoznak, hanem kodifikált normára: ott nem az a kérdés, AI-jel-e, hanem hogy
helyes-e, és azt az AkH. dönti el.

Ez **nem** vonatkozik a klaszter-felülírásra. Mind az öt felülíró minta `?`-jelölt, és ez nem
ellentmondás: a felülírásukat nem a gyakorisági becslés hordozza, hanem egy megnevezett,
falszifikálható **szerkezeti teszt**, amit a minta leírása kimond. Új felülírást csak ilyen
teszttel szabad felvenni.

`[kern]` = stabil (AkH., tipográfia, mondattan). `[2026-08]` = lexikai lista, 12–18 havonta
felülvizsgálandó.

## Klaszterszabály és költségvetés

- Pontozás: `eros`=2, `kozepes`=1, `gyenge`=0.
- **`SOFT` minta csak akkor javítható, ha a bekezdésre eső pontösszeg ≥ 3.** Egyetlen
  `kulcsfontosságú` nem AI-jel; `kulcsfontosságú` + `a mai rohanó világban` + `nem csupán… hanem`
  egy bekezdésben viszont az.
- **Csak `SOFT` találat számít a pontszámba.** A `FIX` és `FIX-IF` minták nem – két rossz
  idézőjel nem bizonyítja, hogy a bekezdés gépi, és ha beszámítanának, a kapu értelmét vesztené.
- **Egy minta egyszer számít, hányszor is talál.** Ugyanannak a mintának két találata nem 4 pont,
  hanem 2. Klaszter = **különböző** jelek együttállása; enélkül bármelyik tág `eros` minta
  magának adna felülírást azzal, hogy kétszer talál.
- **Amire nem tudsz rálépni, az nem bizonyíték.** Ez **elv, nem felsorolás**: ha egy találatot
  bármi megállított, a pontja **nem számít** a bekezdés összegébe. Bármi – a regiszterkapu, egy
  érinthetetlen zóna, a `[jelöld]` címke, a bizonytalanságod, a minta **saját `Mikor NE`-je**, a
  „megőrizendő jegyek” listája, a minta belső plafonja, a bekezdés-költségvetés, a küszöb, vagy az,
  hogy egyszerűen nincs rá minta. A korábbi négyelemű felsorolás túl szűk volt: a valódi
  blokkolások többsége a minták saját `Mikor NE`-jéből jön. A szabály értelme a lényeg – olyan jel
  ne legitimáljon más javítást, amire a skill maga nem mert rálépni.
- **Bekezdés = egy prózai bekezdés vagy egy teljes felsorolás.** A felsorolás pontjai együtt
  számítanak egynek; nem öt külön keret.
- **Táblázat nem bekezdés, és `SOFT` minta táblázatban nem fut.** Sem a sor, sem a cella, sem a
  teljes tábla. A klaszterkapu együttálló jeleket kér egy bekezdésen belül, a költségvetés
  mondatokat számol – egy táblázatcellában egyik sem értelmezhető, és ha kényszerítjük, a kapu
  találomra nyit vagy zár. `FIX` és `FIX-IF` viszont **fut** táblázatban is: az idézőjel, a
  számformátum és a mértékegység-szóköz ugyanúgy norma egy cellában, mint a prózában.
- Néhány minta **saját klaszter-felülírást** hoz: **HU-L06, HU-L14, HU-R09, HU-R10, HU-R11**. Ahol
  a minta ezt kimondja, ott önmagában is elég, és a `neutral` emelt küszöbe sem vonatkozik rá – a
  felülírás feltételei a minta leírásában állnak, nem itt.
- **Amit egy másik minta már elvitt, az nem ad pontot.** Ha egy mondatra precedencia miatt csak az
  egyik minta alkalmazható (HU-L14 vs. HU-R11), a háttérbe lépő minta találata nem számít a
  bekezdés összegébe – különben ugyanaz a mondat kétszer bizonyítana.
- **A törölt mondat érintettnek számít** a 40%-ban. A HU-R10 és a HU-L13 törléssel dolgozik; ha a
  törlés nem számítana, a fék pont a legagresszívebb műveletnél lazulna. **Az összevonás két
  mondatot érint**, nem egyet: két mondatból egyet csinálni mindkettőt átírja.
- **Bekezdésenként legfeljebb 2 `SOFT` javítás.**
- **Szövegszinten a `SOFT` javítással érintett mondatok aránya legfeljebb 40%.** Ez a legerősebb
  fék: akkor is korlátoz, ha minden más mechanizmus félrement.

**A plafon megelőző, nem utólagos.** Ha a **következő** javítás átvinné a 40%-ot, **ne végezd el** –
tedd a gyanús-listára, „szövegszintű költségvetés” indokkal, és folytasd a többi mintával. Nem azt
jelenti, hogy a felismerés után visszavonsz valamit, és nem azt, hogy félbehagyod a futást: a
háromrészes kimenet ilyenkor is teljes.

**A két korlát ütközik, és a szigorúbb nyer.** Bekezdésenként 2 javítás csak akkor fér bele a
40%-ba, ha a bekezdés legalább 5 mondatos – a magyar prózabekezdés viszont jellemzően 3–4. Vagyis
ez nem szélső eset, hanem a normál eset: a bekezdésenkénti 2 gyakran **elérhetetlen**, mert előbb
fogy el a szövegszintű keret. Így van jól. A `references/example-rewrite.md` egy olyan futást mutat,
amelyik a mai elszámolás szerint **átlépi** a plafont, és ki is számolja – az a futás a szabály
tisztázása előtt készült, és szándékosan úgy maradt.

**A költségvetés csak a `SOFT` javításokat számolja.** A `FIX` és a `FIX-IF` minták – tipográfia,
helyesírás, nyelvtani hiba, regiszterkapun átment hivataloskodás – **nem esnek a korlát alá**:
azok javítások, nem átírások. Egy angol idézőjelekkel és rossz számformátummal teli szövegben
minden mondat módosulhat, és az rendben van.

Öt mondatnál rövidebb szövegen a szövegszintű arány nem értelmezhető; ott csak a bekezdésenkénti
2 `SOFT` korlát él.

## Munkafolyamat

**Pass −1 – Nyelvi kapu.** Lásd fent. Ha a szöveg nem magyar, itt megállsz.

**Pass 0 – Triázs.** Regiszter, célközönség, eredet (fordítás-e), meglévő megszólítási forma.
Kimondod a regisztert. Semmit nem írsz át.

**Pass 1 – Tipográfia és helyesírás.** → `references/01-typography.md`
Idézőjel, gondolatjel, nagykötőjel, számformátum, dátum, Title Case, hónap- és napnevek,
`-val/-vel` hasonulás, idegen név toldaléka, mozgószabály, Oxford-vessző.

**Pass 2 – Fordításnyelv és nyelvtan.** → `references/02-translationese.md`, `references/03-grammar.md`
Nominalizáció igésítése, névelőhasználat, névmáskitétel, `az a tény, hogy`, igeidő és igemód,
aspektus, egyeztetés, vonzat, `-e` szócska, fókusz és igekötő-inverzió.

**Pass 3 – Hivataloskodás.** → `references/04-officialese.md`
Terpeszkedő szerkezetek, `-ásra kerül`, `történik/valósul meg`, feltétel-főnevek, hivatali klisék.

**Pass 4 – LLM-retorika.** → `references/05-llm-style.md`
Metaszöveg, üres fokozók, klisés keretezés, negatív párhuzam, hedging, csevegőmaradványok.

**Pass 5 – Ritmus és szövegszint.** → `references/06-rhythm.md`
Két rétege van. **Forma:** mondathossz-szórás, bekezdés-séma, hármas felsorolás, kapcsolóelemek,
mutató anafora, makroszerkezet. **Tartalom:** bevezetetlen kitalált szótár (HU-R09), önhivatkozó
mondat (HU-R10), elvont névszói állítás konkrétum nélkül (HU-R11) – ez a három nem arról szól,
hogyan van megírva egy mondat, hanem hogy kinek szól és mit tud meg belőle az olvasó. Ha csak egy
dolgot futtatsz ebből a passból, ezt a hármat futtasd: a legtöbb „érthetetlen, nem gyakorlatias”
panasz ide vezet vissza, és a mondatszintű passok bizonyítottan nem fogják meg.

**Pass 6 – Önellenőrzés.** Lásd lent.

A mechanikus párcserék (`intézkedést foganatosít` → `intézkedik`, `"…"` → `„…”`) a
`references/substitutions.md`-ben vannak, táblázatban. Ez lookup – de két előfeltétellel: a
szerkezet legyen csupasz (nincs előtte névelő vagy mutató névmás), és a csere ne változtassa meg
a vonzatkeretet. A fájl eleje kifejti.

**Miért ez a sorrend.** A mechanikus előre, mert nem igényel ítéletet és letisztítja a képet.
**A szerkezet a lexika előtt** – ez a legfontosabb: ha előbb cserélsz szavakat, a mondatszerkezet
rögzül, és nehezebb igésíteni; fordítva a Pass 2 magától elviszi az üres fokozók nagy részét.
A ritmus utolsó, mert minden korábbi törlés megváltoztatja a mondathosszokat.

**Monotonitás: későbbi pass nem érvénytelenítheti a korábbit.** A ritmusigazítás közben könnyű
visszahozni egy angol idézőjelet vagy egy Title Case címet – ezért fut a Pass 6 tipográfiai
ellenőrzése a kimeneten.

## Érinthetetlen zónák

Ezeken belül semmit nem írsz át, akkor sem, ha találsz benne mintát:

idézet · cím és tulajdonnév · metanyelvi említés (ahol a szót *tárgyalják*, nem használják) ·
kódblokk, parancs, fájlnév, azonosító · jogi hivatkozás és paragrafusszám · strukturált metaadat
(front matter, property, adatbázismező) · link szövege és célja · **idegen nyelvű szakasz**.

**Tartalmi invariáns:** a javítás nem változtathat számot, nevet, dátumot, jogi terminust, sem a
tagadás, a kvantor vagy a fókusz hatókörét. Új tényt, nevet, számot soha nem tehetsz bele.

**Sűrítés-fék:** tilos idiómát, szólást vagy partikulát beszúrni oda, ahol nem volt. Az
idiómasűrűség ugyanúgy fordításízt ad, mint a hiánya.

## Önellenőrzés

Hét kérdés, mindegyikre igen vagy nem. Nem „olvasd át újra” – az semmit nem ér.

1. **Diff-audit.** Minden változtatás visszavezethető egy minta-ID-ra? Ha nem, vond vissza.
2. **Babona-audit.** Nem történt `ami`→`amely`, `-va/-ve`→cselekvő, kulcsszó→szinonima,
   mondatkezdő kötőszó kiirtása, `hát`/`ugye` törlése, páros testrész egységesítése?
3. **Invariáns-audit.** Számok, nevek, dátumok, jogi terminusok, tagadás hatóköre változatlan?
4. **Regiszter-audit.** Nem keveredett a megszólítás? A `formal`/`legal` szöveg nem lett beszélt nyelvi?
5. **Sűrítés-audit.** Nem került a szövegbe idióma, partikula vagy fordulat, ami nem volt ott?
6. **Költségvetés-audit.** A `SOFT` javítással érintett mondatok aránya 40% alatt van? (A `FIX`
   javítások nem számítanak bele. Öt mondat alatt ez a kérdés kimarad.)
7. **Sűrűség-audit.** Van-e a kimenetben mondat, ami törölhető lenne anélkül, hogy állítás veszne
   el? Ha igen, **ne töröld** – minta-ID nélküli törlést az 1. audit visszavonat. Írd a
   gyanús-listára.

Plusz egy olcsó, objektív ellenőrzés: futtasd újra a Pass 1 tipográfiai listáját a **kimeneten**.

## Kimenet

Három rész, elöl a nyelv és a regiszter kimondásával – amit a nyelvi kapu és a Regiszter szakasz
amúgy is kötelezővé tesz. **A címsorok szó szerint ezek, `##` szinten, ebben a sorrendben:**

```
## 0. Nyelv és regiszter
## 1. A javított szöveg
## 2. Változástábla
## 3. Gyanús, de nem javítottam
```

Ez nem formázási ízlés. A 2. kör azért nem tudta géppel ellenőrizni a saját számait, mert a kimenet
alakja futásonként változott: az egyik változástábla két sor volt, a másik tizenöt, alszakasszal.
Kézi átnézés lett belőle. A rögzített alak ezt oldja meg.

- **Mind a négy szakasz megjelenik**, akkor is, ha üres. Üres szakasz törzse egyetlen szó: `nincs`.
  Így a „megnéztem, nem volt mit javítani” megkülönböztethető attól, hogy a szakasz elmaradt.
- **A 0. szakasz kettőt mond ki:** a **szöveg nyelvét** és a **regisztert**, a profilnevet
  visszapipálva. Pontosan **egy profilnév** álljon benne – a mondatok száma nem számít. Ha a
  regisztert a hívó rögzítette, írd oda, hogy rögzített: a mérések összevethetősége ezen múlik.
- **Az 1. szakasz törzse kódblokkban áll.** Ez nem díszítés: a javított szöveg maga is tartalmazhat
  `##` és `###` címsorokat, és fence nélkül azok szakaszhatárnak látszanak.
- **A 2. szakasz táblázat**, pontosan ezekkel az oszlopokkal, ebben a sorrendben:
  `| ID | Eredeti | Új | Indok |`.
  - **Soronként egy minta egy mondatban.** Ugyanannak a mintának több találata **egy mondaton
    belül** egy sor; **külön mondatban külön sor.** Ez teszi a sorszámot összevethetővé a
    mondatalapú költségvetéssel.
  - Ha **egy** javítást **több** minta indokol, a minta-ID-k vesszővel egy cellában állnak.
  - Ha **két külön** javítás esik ugyanarra a mondatra, az **két sor**.
  - Az `Eredeti` és az `Új` a **megváltozott legszűkebb részletet** tartalmazza, nem a teljes
    mondatot – különben az átfedő javítások egymás változásait is mutatnák. De van alsó határa:
    a legszűkebb részlet, ami **még azonosítja a helyet.** Egyetlen írásjel nem az.
  - **Törlésnél az `Új` cella `*(törölve)*`.**
  - **Egy sor `SOFT`-nak számít, ha bármelyik idézett mintája `SOFT`** – a költségvetés `SOFT`
    javításokat számol, és a szigorúbb olvasat a biztonságos.
- **Az 1. szakasz a teljes javított szöveget adja vissza**, a strukturált metaadattal együtt
  (front matter, property), változatlanul. Az érinthetetlen zóna nem azt jelenti, hogy kimarad,
  hanem hogy nem módosul.
- **A 3. szakasz felsorolás.** Minden tétel `- ` jellel kezdődik, utána `**minta-ID**` (többet
  vesszővel, ahogy a 2. szakaszban) vagy `**nincs minta**`, majd ` – `, majd a részlet és az indok.
  **Egysége ugyanaz, mint a 2. szakaszé: egy minta egy mondatban.** Egy gyanús tétel nem javított
  javítás, tehát ugyanúgy kell számolni – enélkül ugyanaz a futás 6-ot vagy 11-et is jelenthet.
  Ezt a szabályt a `parse_run.py` **nem tudja kikényszeríteni**, csak kiírni; itt a fegyelem tartja.
- **Alcímsor egyik szakaszban sem áll.** „Átnéztem, tiszta volt” típusú alszakasz a
  változástáblában tilos: az a 3. szakaszba tartozik, vagy sehova.

A harmadik rész nem formalitás. Ez az a szelep, ahol a bizonytalanságodat kiírhatod ahelyett, hogy
javításba menekülnél – közvetlenül ez csökkenti a túljavítást.

Teljes mintafutás a formátumra: `references/example-rewrite.md`. **Formátumpélda, nem illesztési
minta** – a jeleket mindig a referenciafájlokból azonosítsd, ne az ottani mondatokhoz hasonlítva.
A fájl egy szándékosan megtűzdelt bemeneten mutatja a kimenet alakját; valós szövegen mért
teljesítményről nem állít semmit.

**Ez a skill nem ír fájlt.** Ha a szöveg fájlban van, olvasd be, és a **teljes javított szöveget a
beszélgetésben** add vissza a változástáblával és a gyanús-listával. A felülírás a hívó dolga – ő
látja a diffet, ő döntheti el.

Miért: a mérés szerint a fájlmód **kétszer írt** – az első írás vitt be egy tipográfiai hibát, a
Pass 6 elkapta, a második javította. Két írás közötti megszakítás sérült fájlt hagy a lemezen.

**És most jön az őszinte rész: ez a korlát nincs kikényszerítve.** A frontmatter
`allowed-tools: Read, Grep, Glob` sora kimondja a szándékot, de megmértük, és subagent-kontextusban
**nem szűkíti a szerszámkészletet** – a Write a skill betöltése után is lefut. Vagyis a nem-írás itt
a te fegyelmed, nem homokozó. Ezért áll itt kiírva, ahelyett hogy mechanizmusnak adnánk ki: egy
korlát, amit semmi nem kényszerít ki, csak akkor korlát, ha ez a tény is ott van mellette.

Ha egy másik feladat hívja ezt a skillt lépésként, csak a javított szöveget add vissza.

## Gyorsteszt

Tíz jel, passonként a legerősebb. Ez térkép a gyors úthoz, nem új szabály – a javítás feltételei
(regiszterkapu, klaszterküszöb, `Mikor NE`) mindegyiknél a minta leírásában állnak.

| # | Amit keresel | Minta |
|---|---|---|
| 1 | `"…"` angol idézőjel magyar mondatban | HU-T01 |
| 2 | `—` em dash (a szóközös `–` viszont helyes) | HU-T02 |
| 3 | Title Case címben vagy címsorban | HU-T07 |
| 4 | `-ásra/-ésre kerül` | HU-H02 |
| 5 | `lehetővé teszi számunkra, hogy` | HU-F03 |
| 6 | `Ön`-halmozás, vagy tegezés-önözés keveredés | HU-M02, HU-M01 |
| 7 | Metaszöveges nyitás (`Fontos megjegyezni, hogy`) | HU-L03 |
| 8 | Egyenletes mondathossz, egyforma bekezdésszerkezet | HU-R01, HU-R02 |
| 9 | Bevezetetlen kitalált szó, definíció nélkül | HU-R09 |
| 10 | Aforizma-zárlat, idézhetőre csiszolt mondat | HU-L14 |

Ha ezek közül egyik sem üt ki, a szöveg valószínűleg rendben van. Ha három vagy több igen, futtasd
végig a teljes munkafolyamatot.

## Referenciák

- [Tiltólista](references/do-not-touch.md) – 23 tétel indoklással, precedencia-szabályok, meta-szabály.
- [Regiszterek](references/registers.md) – profilok, pass-mátrix, megszólítás, műfaji alprofilok.
- [Pass 1: tipográfia](references/01-typography.md) · [Pass 2a: fordításnyelv](references/02-translationese.md) · [Pass 2b: nyelvtan](references/03-grammar.md)
- [Pass 3: hivataloskodás](references/04-officialese.md) · [Pass 4: LLM-retorika](references/05-llm-style.md) · [Pass 5: ritmus](references/06-rhythm.md)
- [Párcserék](references/substitutions.md) – mechanikus lookup.
- [Mintafutás](references/example-rewrite.md) – a háromrészes kimenet formátuma. Formátumpélda,
  nem teljesítményállítás.
- [Források](references/sources.md) – hitelességi minősítés, mit tudunk mérésből, mit nem.

Rövid szövegre és gyors átnézésre a fenti tiltólista és a Pass 1 elég. Teljes átíráshoz olvasd be
a passhoz tartozó fájlt – **ne emlékezetből javíts.**
