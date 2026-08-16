# Regiszterek, megszólítás, műfajok

A skill legtöbb mintája regiszterfüggő. Regiszter megállapítása nélkül az eszköz túljavít: a
jogi szövegből beszélt nyelvet csinál, a blogból hivatalos levelet. Ezért a Pass 0 nem opcionális.

---

## A négy profil

| profil | tipikus szöveg | Pass 1 | Pass 2 | Pass 3 | Pass 4 | Pass 5 |
|---|---|---|---|---|---|---|
| `informal` | blog, marketing, közösségi poszt, belső chat | teljes | teljes | teljes | teljes | teljes |
| `neutral` (alap) | dokumentáció, súgó, termékszöveg, e-mail | teljes | teljes | teljes | teljes | mérsékelt |
| `formal` | üzleti levél, riport, akadémiai szöveg | teljes | teljes | csak HU-H04, klaszterben | teljes, HU-L07 nélkül | ki |
| `legal` | szerződés, hatósági irat, jogszabály, szabályzat | teljes | csak `FIX` | **ki** | csak HU-L03, HU-L12 | ki |

**Ez a mátrix az egyetlen hely, ahol a pass-kapuk állnak.** A pass-fájlok nem ismételhetik meg a
saját kapujukat; ha eltérést látsz, ez a táblázat nyer.

- **`mérsékelt`** = a klaszterküszöb 3 helyett **4**, és bekezdésenként legfeljebb **egy** javítás
  mehet ki abból a passból.
- **`csak klaszterben`** = `FIX-IF` minta sem tüzel egymagában, csak ha a bekezdés eléri a küszöböt.
- **A Pass 3 `formal`-cellája szűkebb, mint amilyennek látszik.** A `FIX-IF` minta a **saját**
  profillistája szerint fut, és a Pass 3 mintái közül **egyedül a HU-H04 sorolja fel a `formal`-t**
  – a HU-H01, HU-H02, HU-H03, HU-H05, HU-H06 és HU-H07 nem. Vagyis a „klaszterben” feltétel a
  gyakorlatban egyetlen mintára vonatkozik. Ez így szándékos: a hivatali regiszter formális
  szövegben **nem hiba**, és a Pass 3 kinyitása ott több beavatkozást engedne, amit előbb mérni
  kellene. A mátrix itt a mintákhoz igazodik, nem fordítva.
- **A Pass 5 `formal`-kivétele:** a HU-R09, a HU-R10 és a HU-R11 `formal` profilban is fut, mert
  ezek **tartalmi**, nem formai minták – nem arról szólnak, hogyan van megírva egy mondat, hanem
  hogy megtud-e belőle bármit az olvasó. A Pass 5 többi mintája `formal`-ban áll.

Ha nem tudod eldönteni, a `neutral` az alapértelmezés. Kétség esetén **azt a profilt válaszd,
amelyik kevesebb javítást enged** (a táblázatban lefelé: `legal` a legmegengedőbb a szöveggel
szemben, mert ott áll le a legtöbb pass). A túl kevés javítás visszafordítható, a regisztertörés nem.

## Regiszter megállapítása

1. **Ha a felhasználó megmondta, azt használod.** Nincs mérlegelés.
2. Ha nem, ebből a checklistából vezeted le:
   - Van benne jogi terminus, paragrafusszám, hatályra utalás? → `legal`
   - Megszólítás: tegező? → `informal` vagy `neutral`. Önöző? → `neutral` vagy `formal`.
   - Csatorna: chat, poszt, blog → `informal`. E-mail, dokumentáció → `neutral`. Riport,
     hivatalos levél → `formal`.
   - Van benne hivatkozásjegyzék, absztrakt, számozott szakasz? → `formal`
3. **Kimondod egy sorban, mielőtt bármit átírsz.** Például: *A szöveget `neutral` regiszterként
   kezelem.* Így a felhasználó felülbírálhatja, mielőtt kár lesz. **Csendes regiszterváltás tilos.**

**A regisztert a csatorna dönti, nem a felek viszonya.** Domonkosi adata: tegeződő cégek belső
hivatalos levelezése is önöz, mert az írásbeliség és a hivatalosság kétszeresen státuszjelöltté
teszi a közlést. Attól, hogy a cégnél tegeződnek, a hivatalos levél még önöz.

---

## A magyar megszólítási rendszer négyosztatú

Ez a fájl legfontosabb megállapítása, és a gépi szöveg itt téved a legrendszeresebben.

A nemtegező viszonyon belül **négy** változat él:

1. `maga`
2. `Ön`
3. **névmás nélküli egyes szám 3. személy** – a „névmáskerülő” forma
4. `tetszik` + főnévi igenév

A gépi szöveg gyakorlatilag csak a (2)-t ismeri, és épp a (3)-at nem használja – pedig az a
leggyakoribb a magyarban. **A magyar természetesség nem az `Ön` helyes megválasztásában áll,
hanem a névmás elhagyásában.**

### HU-M01 · Tegezés és magázás keverése · [FIX] [AI:eros] [kern]

Mi ez: egy szövegen belül egyetlen megszólítási forma lehet. A váltás a leggyakoribb és
legfeltűnőbb gépi hiba.
ROSSZ: Kedves Felhasználó! Töltsd le az alkalmazást, majd jelentkezzen be a fiókjába.
JÓ:    Kedves Felhasználó! Töltse le az alkalmazást, majd jelentkezzen be a fiókjába.
Mikor NE: **a meglévő formát tartsd meg, ne te válaszd meg.** Ha a szöveg túlnyomórészt tegez,
egységesíts tegezésre; ha önöz, önözésre. A döntés a szerzőé – te csak a következetlenséget
javítod. Ha nincs benne megszólítás, ne vigyél be.
Forrás: Microsoft Hungarian Style Guide · Domonkosi Ágnes

### HU-M02 · Az `Ön` névmás halmozása · [SOFT] [AI:eros?] [kern]

Mi ez: az igei személyrag már jelöli a megszólítottat. Az `Ön` csak értelmi hangsúlynál vagy
szembeállításnál kell.
Miért írja így a gép: az angol `you` kötelező, és a magyar hivatali szokás fel is erősíti.
Domonkosi 240 hivatalos levélből 78%-ban talált `Ön`/`Önök` névmást, sokszor olyan helyzetben is,
ahol elhagyható lenne.
ROSSZ: Ha Ön elfelejtette az Ön jelszavát, Ön a beállításokban módosíthatja azt.
JÓ:    Ha elfelejtette a jelszavát, a beállításokban módosíthatja.
Ugyanez a birtokos névmásra és az `ő`-re: lásd HU-F06.
Mikor NE: szembeállításnál kötelező (`Ön dönt, nem mi.`). Jogi szövegben az `Ön` a fél
azonosítása lehet – ott hagyd.
Az `Ön` nagybetűzését ne egységesítsd: HU-B22.
Forrás: Domonkosi Ágnes, real.mtak.hu/75699

### HU-M03 · A `maga` névmás írott üzleti szövegben · [FIX-IF: neutral, formal] [AI:kozepes] [2026-08]

Mi ez: írott üzleti és ügyfélszövegben ne a `maga` legyen a nemtegező forma, hanem az `Ön` vagy a
névmás nélküli E/3.
ROSSZ: Ha maga elfelejtette a jelszavát, maga új jelszót kérhet a felületen.
JÓ:    Ha elfelejtette a jelszavát, új jelszót kérhet a felületen.
Mikor NE: **a `maga` nem hiba, hanem társas kockázat.** Élőbeszédben, párbeszédben, szereplő
hangjában teljesen legitim, és bizonyos régiókban semleges. Csak írott ügyfélszövegben cseréld.
Forrás: Domonkosi Ágnes

### HU-M04 · Felületi és súgószöveg megszólítása · [FIX-IF: neutral] [AI:kozepes] [2026-08]

Mi ez: általános célú szoftverfelületen és ügyfélkommunikációban a magyar norma az önözés.
Tegezni gyerek- és játékszoftverben, parancssori eszközben, illetve kifejezetten tegező
márkahangban szabad.
ROSSZ: Kattints a Tovább gombra, majd add meg a jelszavad.
JÓ:    Kattintson a Tovább gombra, majd adja meg a jelszavát.
Mikor NE: **HU-M01 felülírja.** Ha a szöveg már következetesen tegez, ne váltsd át – az a
márkahang. Szabad szoftveres súgóban a T/1 felszólítás (`Kattintsunk az OK gombra`) bevett
harmadik út; ha a szöveg ezt használja, hagyd.
Forrás: Microsoft Hungarian Style Guide · Mozilla és Ubuntu magyar fordítói útmutató

### HU-M05 · Megszólításkerülés ismeretlen regiszterben · [SOFT] [AI:kozepes?] [kern]

Mi ez: ha nem tudod, tegező vagy nemtegező a viszony, **kerüld el a megszólítást** – személytelen
szerkezettel, főnevesítéssel vagy `-hat/-het` lehetőséggel.
ROSSZ: Töltsd ki a kérdőívet, majd Ön küldje el nekünk a megadott címre.
JÓ:    A kérdőívet kitöltés után a megadott címre lehet elküldeni.
Ez az egyetlen hely, ahol a főnevesítés **jó** megoldás – a HU-F01 itt nem alkalmazandó.
Mikor NE: ha a szöveg regisztere egyértelmű, vagy ha a felhasználó megmondta. Akkor nem kerülni
kell a megszólítást, hanem következetesen használni a megállapított formát. `legal` profilban
szintén nem fut: ott a személytelen szerkezet amúgy is az alapforma.
Forrás: Domonkosi Ágnes

### HU-M06 · Tetszikelés írott üzleti szövegben · [FIX-IF: neutral, formal] [AI:gyenge] [kern]

Mi ez: a `tetszik` + főnévi igenév bizalmasan udvarias, beszélt nyelvi forma (gyerek–felnőtt,
idősek, egészségügy). Írott ügyfélszövegben és felületen nem használatos.
ROSSZ: Kedves Vásárlónk! Meg tetszik tudni adni a rendelési számot?
JÓ:    Kedves Vásárlónk! Meg tudja adni a rendelési számot?
Mikor NE: párbeszédben, idézetben, és minden olyan szövegben, ahol a beszélt nyelvi hang a cél.
Forrás: Domonkosi Ágnes

---

## Műfaji alprofilok

A profil megmondja, milyen szigorral javítunk. A műfaj azt, **mit** keresünk.

### HU-M07 · Levélmegszólítás írásjele · [FIX] [AI:eros] [kern]

Mi ez: a magyar levélmegszólítás után **felkiáltójel** áll, és a szöveg új sorban, nagy
kezdőbetűvel indul. Az angol „vessző + kisbetűs folytatás” idegen.
ROSSZ: `Kedves János,` / `köszönöm a levelét, hamarosan válaszolok.`
JÓ:    `Kedves János!` / `Köszönöm a levelét, hamarosan válaszolok.`
Mikor NE: a vesszős forma az utóbbi években terjed, és informális e-mailben már nem feltűnő.
`informal` profilban csak akkor javítsd, ha a szöveg egyébként is formális.
Az elköszönő formula (`Üdvözlettel`, `Tisztelettel`, vesszővel vagy kettősponttal) **ízlés
kérdése, nem norma** – ne nyúlj hozzá.
Forrás: AkH. 12. · e-nyelv.hu

### HU-M08 · Amerikai e-mail-keret · [SOFT] [AI:eros?] [2026-08]

Mi ez: az amerikai üzleti levél udvariassági kerete magyarul túlzó.
Jelek: `Remélem, jól vagy!`, `Remélem, ez a levél jó egészségben találja`,
`Ne habozzon kapcsolatba lépni velünk`, `Nagyszerű kérdés!`, `Örömmel segítek!`,
`Kérjük, vegye figyelembe, hogy`, `Előre is köszönöm a türelmét`.
ROSSZ: Kedves Anna! Remélem, jól vagy! Nagyszerű kérdés. Kérjük, vegye figyelembe, hogy a
szolgáltatás vasárnap szünetel. Ne habozzon kapcsolatba lépni velünk!
JÓ:    Kedves Anna! A szolgáltatás vasárnap 2 és 4 óra között szünetel. Ha valami nem világos,
keress nyugodtan.
Mikor NE: ha a kapcsolat tényleg megkívánja a személyes nyitást (régi ismerős, hosszú szünet után
írsz). A magyar üzleti levél rövidebb és tárgyszerűbb, de nem barátságtalan.
A `Kérjük, vegye figyelembe, hogy` (`Please note that`) mindig törölhető: mondd ki a tényt.
Forrás: Microsoft Hungarian Style Guide · Domonkosi Ágnes

### HU-M09 · SEO-blog sablon · [SOFT] [AI:eros?] [2026-08]

Mi ez: a kérdés-alcímes szerkezet és a retorikai átvezetés.
Jelek: `Mi az X?` / `Miért fontos az X?` / `Hogyan működik az X?` alcímsor; minden szakasz végén
átvezető kérdés; `De mit is jelent ez a gyakorlatban?`; `Nézzük meg közelebbről!`
Javítás: írd át az alcímeket állító mondatra vagy főnévi szerkezetre, és töröld az átvezető
kérdéseket.
Mikor NE: ha a szöveg tényleg GYIK vagy súgó, ahol a kérdés a keresés belépője. Ott funkció.
Forrás: közvetlen megfigyelés · Wikipedia: Signs of AI writing – „Outline-like sections”,
„Fragmented headers” (CC BY-SA 4.0)

### HU-M10 · Közösségi poszt sablon · [SOFT] [AI:eros?] [2026-08]

Mi ez: a generált poszt felismerhető formája.
Jelek: emoji minden bekezdés elején; hashtag-sor a végén; egymondatos bekezdések sorozata;
záró kérdés (`Mi a te tapasztalatod?`); `🚀`, `💡`, `👇`.
Javítás: vedd ki az emoji-listát és a hashtag-sort, vond össze a bekezdéseket, töröld a
kötelező záró kérdést.
Mikor NE: ha a szerző márkahangja tényleg ilyen, vagy ha a platform megköveteli (a hashtag
LinkedInen funkcionális). `informal` profilban ez csak jelzés, nem automatikus javítás.
Forrás: közvetlen megfigyelés

### HU-M11 · Névsorrend és titulushasználat · [FIX] [AI:kozepes] [kern]

Mi ez: magyar névnél a sorrend vezetéknév–keresztnév. Első említéskor teljes név, utána
vezetéknév vagy teljes név – a csak keresztnévi hivatkozás magyar szövegben bizalmaskodó.
ROSSZ: Anna Kovács elmondta, hogy… Később Anna hozzátette…
JÓ:    Kovács Anna elmondta, hogy… Később Kovács hozzátette…
Mikor NE: idegen névnél a forrásnyelvi sorrend marad (`John Smith`). Ha a szöveg tudatosan
közvetlen (belső poszt, csapatlevél), a keresztnév rendben van.
Forrás: AkH. 12. · Gyurgyák János: Szerkesztők és szerzők kézikönyve

### HU-M12 · Terminológiai következetesség · [SOFT] [AI:eros?] [kern]

Mi ez: egy fogalmat egy szövegen belül egyféleképpen nevezz. A gépi szöveg ingadozik a magyar és
az angol terminus között, és a szinonimakergetés miatt még variál is.
ROSSZ: A deployment automatikus. A telepítés éjszaka fut, és a kiszállítás naplózva van.
JÓ:    A telepítés automatikus, éjszaka fut, és naplózva van.
Az angol szakszó toldalékolására: `deployment-et`, `API-t`, `commitot` – lásd HU-T12, HU-T13.
Mikor NE: **ez nem purizmus** (HU-B16). Nem az a cél, hogy magyarítsd a szakszót, hanem hogy
következetes legyen. Ha a szakma angolul mondja, maradjon angolul – de végig.
Ez a minta a HU-B13 szóismétlés-tilalmának a párja: a terminust **ismételni kell**.
Forrás: Fóris Ágota: Hat terminológia lecke

---

## Precedencia a megszólításban

1. **A meglévő forma nyer.** Ha a szöveg már választott (tegez, önöz, T/1-et használ), azt tartsd
   meg, és csak a következetlenséget javítsd.
2. Ha nincs megszólítás a szövegben, **ne vigyél be**. HU-M05: kerüld el.
3. Ha van, de következetlen, a **többségi** forma nyer.
4. A `legal` profil felülír: ott az önözés vagy a személytelen forma az egyetlen opció.
