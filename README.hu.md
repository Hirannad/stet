*[English](README.md) · **Magyar***

# stet

**stet** *(korrektúrajel: „maradjon”)* – az a jelölés, amivel a korrektor visszavon egy javítást.

Ha magyar szöveget írattál egy nyelvi modellel, ismered azt az érzést, hogy „ez valahogy nem
magyar”. Nem hibás. Nyelvtanilag rendben van. Csak épp senki nem így beszél.

Ez az eszköz azt keresi meg. És ami sokkal fontosabb: **azt is tudja, mihez ne nyúljon hozzá.**

## Kinek való

Ha magyar szöveget írsz vagy íratsz AI-val, és az mások elé kerül: ügyféllevél, dokumentáció,
termékszöveg, hírlevél, poszt, szabályzat.

A tipikus eset ez: megíratod, elolvasod, jónak tűnik, kiküldöd – aztán valaki visszaszól, hogy
„ez olyan gépi”. Ez az eszköz megmondja, konkrétan min múlt, mondatonként.

Ha viszont magadnak írsz jegyzetet, vagy a szöveg úgyis csak egy prompt lesz valami másnak, nem
éri meg a kört.

## Mit kapsz érte

A legutóbbi méréskor kilenc AI-írta magyar szöveget futtattunk át rajta, háromféle modelltől.
**Mind a kilencben talált tipográfiai vagy helyesírási hibát** – szövegenként 1 és 10 közöttit.
Nem stílushibát: olyat, ami egyszerűen rossz. Angol idézőjel magyar mondatban, em dash a
gondolatjel helyett, `1,250,000` a `1 250 000` helyett, `HTML-el` a `HTML-lel` helyett.

Ezek nem attól rosszak, hogy „gépiesek”. Attól, hogy **igénytelennek** mutatják a szöveget, és
pont az a fajta hiba, amit az ember maga már nem vesz észre a századik átolvasásra.

Ez a megbízható rész, és erős modell szövegén jellemzően ennyi is a dolga: rendbe rakja a
tipográfiát, és nem nyúl máshoz. A stilisztikai réteg gyengébb modellek szövegén dolgozik
igazán – és ott sem hibátlan, lásd az *Amit nem tud* részt.

## Telepítés

```bash
/plugin marketplace add Hirannad/stet
```

```bash
/plugin install stet@stet
```

Vagy klónozd, és linkeld be a `skills/stet-hungarian` mappát a `~/.claude/skills/` alá.

Utána csak kérd meg magyarul: *„nézd át ezt a szöveget”*. Visszaad három dolgot: a javított
szöveget, egy táblázatot arról, mit miért változtatott, és egy listát arról, **mit vett észre és
hagyott mégis békén.** A fájlodhoz nem nyúl.

## Mit talál meg

Két különböző dolgot, és ez nem ugyanaz.

**1. A szerkezet angol maradt.** A modell a magyart gyakorlatilag latens angolból állítja elő, ezért
angol mondatszerkezetet kapsz magyar szavakkal – akkor is, ha a szöveget senki nem fordította.
Ez a hangosabb jel, és ezt érzed meg elsőre:

| ez jön ki | ez lenne magyarul |
|---|---|
| Ez a megoldás lehetővé teszi számunkra, hogy csökkentsük a költségeket. | Ezzel a megoldással csökkenthetjük a költségeket. |
| A szabályzat a következő ülésen elfogadásra kerül. | A szabályzatot a következő ülésen elfogadják. |
| A projekt sikerességének biztosítása a kommunikáció hatékonyságának javításán alapul. | A projekt akkor sikerül, ha jobban kommunikálunk. |
| Ha Ön elfelejtette az Ön jelszavát, Ön a beállításokban módosíthatja azt. | Ha elfelejtette a jelszavát, a beállításokban módosíthatja. |

**2. Az LLM-modorosság.** A körülbeszélés, ami nem közöl semmit:

| ez jön ki | ez lenne magyarul |
|---|---|
| Fontos megjegyezni, hogy a határidő két okból csúszott. | A határidő két okból csúszott. |
| A rendszeres visszajelzés kulcsfontosságú és elengedhetetlen. | Visszajelzés nélkül a csapat nem fejlődik. |
| A mai rohanó világban az adatvédelem a bizalom letéteményese. | Az adatvédelem az elmúlt öt évben lett üzleti kérdés. |
| Összefoglalva elmondható, hogy a jövő fényes. | *(törölve – nem állít semmit)* |

És a tipográfia, ami magyarul egyszerűen máshogy van, mint angolul:

| ez jön ki | helyesen |
|---|---|
| `"idézet"` | `„idézet”` |
| `A terv jó — papíron` | `A terv jó – papíron` |
| `3.5%`, `1,250,000` | `3,5%`, `1 250 000` |
| `8GB`, `21°C` | `8 GB`, `21 °C` |
| `2026 Augusztus 2-án`, `Hétfőn` | `2026. augusztus 2-án`, `hétfőn` |
| `HTML-el` | `HTML-lel` |

## És most a lényeg: mihez NEM nyúl hozzá

Ez a rész választja el ezt az eszközt egy szólistától, és ezért érdemes elolvasni akkor is, ha
minden mást átugrasz.

Egy nyelvi modell magyarul **alapból túljavít.** Beszívta a magyar nyelvművelő hagyományt, és
elkezd „kijavítani” olyan dolgokat, amik nem hibák. A gond az, hogy minden ilyen javítás
hivataloskodóbbá teszi a szöveget – vagyis **gépiesebbé.** Épp az ellenkezőjét éri el.

Ezért van a katalógusban 23 tétel, amihez az eszköznek **tilos** hozzányúlnia:

| amit egy modell „kijavítana” | miért nem hiba |
|---|---|
| `le van zárva` → `lezárták` | Nem germanizmus. A 14. századtól adatolt, és nem ugyanazt jelenti: az egyik állapot, a másik esemény. |
| `ami` → `amely` | Egész tagmondatra visszautalva az `ami` a normatív alak. Az `amely` itt hiperkorrekció. |
| `De ez nem jelenti azt…` → `Ez azonban…` | Mondatot lehet kötőszóval kezdeni. Csak szöveget nem. A csere egyszerre hivataloskodóbb és monotonabb. |
| `nem láttam senkit` → `nem láttam valakit` | A magyarban a kettős tagadás **kötelező.** A „javított” alak nem stílushiba, hanem hibás mondat. |
| `a tanulmány kimutatja` → `a szerzők kimutatják` | Élettelen alany cselekvő igével teljesen rendben van. („Sétálhat-e az utca?” – Szepesy egy fejezetet szentel neki.) |
| `de viszont` → `de` | Szótározott összetett kötőszó, négy külön jelentésárnyalattal. |
| `hát`, `ugye`, `szóval` törlése | Diskurzusjelölők. Funkciójuk van, és nagyrészt ezek adják, hogy a szöveg emberi. |
| ugyanaz a kulcsszó 4× → szinonimák | **A szinonimalánc maga a gépi jel.** A magyar szakszöveg ugyanazon a néven nevezi ugyanazt. |
| `fáj a lábam` → `fájnak a lábaim` | Mindkettő helyes. Ez a tétel oda-vissza tilos. |

És a legfontosabb szabály az egészben: **soha nem gyárt emberséget hibából.** Nem visz be szándékos
elírást, nem archaizál, nem tör regisztert, hogy „élőbbnek” tűnjön. Ha egy javítás csak úgy tenné
emberibbé a szöveget, hogy hibát csinál belőle, akkor az nem javítás.

## Tudja, hogy mikor kell leállnia

Négy fék, mert egy szólista addig javít, amíg el nem fogy a szöveg:

- **Regiszter.** Blogot, dokumentációt, üzleti levelet és szerződést nem ugyanúgy kezel. Jogi
  szövegben a hivatalos névszói szerkezet **helyes** – ha „közérthetőbbre” írod, joghatást veszít.
  Ezért egész passzokat kikapcsol, ha szerződést lát.
- **Klaszterküszöb.** A bizonytalanabb stilisztikai minták csak akkor javítanak, ha **több
  különböző** jel áll össze egy bekezdésben. Egy `kulcsfontosságú` önmagában nem AI-jel. Egy
  `kulcsfontosságú` + `a mai rohanó világban` + `nem csupán… hanem` egy bekezdésben viszont az.
- **Javítási plafon.** Van egy felső korlát arra, hogy a mondatok mekkora részéhez nyúlhat hozzá.
  Fölötte megáll és jelez, nem megy tovább.
- **A harmadik lista.** Amit észrevett, de nem javított, azt **kiírja.** Ez nem formalitás: ez az a
  szelep, ahol a bizonytalanság kimondható ahelyett, hogy javításba menekülne.

## Miért nem elég egy angol „humanizer”

Vannak jó angol eszközök erre. A gond az, hogy **négy elterjedt angol szabály magyarul pont az
ellenkezőjét írja elő,** mint a norma:

- az angol lista irtja a gondolatjelet – magyarul a szóközös `–` a **helyes** alak;
- „kerüld a szenvedő szerkezetet” – magyarul a `-va/-ve van` tiltása babona;
- „minden mondatnak emberi alany kell” – magyarul a `döntés született` teljesen rendben van;
- a curly quote „javítása” elviszi a `„…”`-t, ami épp a helyes magyar idézőjel.

Ezért ez külön katalógus, nem fordítás. És ezért van a skillben egy nyelvi kapu, ami **a szöveg**
nyelvét nézi, nem a kérésé: ha angolul kérsz javítást magyar szövegre, ez az eszköz a helyes; ha
magyarul kérsz angol szövegre, nem ez. A legtöbb angol eszközben nincs ilyen kapu – vagyis ha
mellé telepítesz egyet, egy angolul megfogalmazott kérés magyar szövegen könnyen a rosszra fut, és
ott nemcsak elmulaszt dolgokat, hanem **hibát is visz be.**

## Mit tudunk róla mérésből

Három mérési kör futott. Mindegyik a [docs/validation.md](docs/validation.md)-ben van, a
korlátaival együtt. A szövegkorpusz, minden szám **és maguk a futások** bent vannak a repóban
([tests/corpus/](tests/corpus/)), tehát újrafuttathatod, és nem kell elhinned.

**A legérdekesebb eredmény, és kétszer is kijött:** 9 magyar szöveget generáltunk három Claude
modellel. A Sonnet és az Opus által írt magyaron az eszköz **egyetlen** stilisztikai javítást sem
végzett. A tipográfiait viszont mindegyiken elvégezte. Ugyanez jött ki a második körben és a
harmadikban is, pedig közben megváltozott, hogyan számoljuk.

Magyarul: **erős modell szövegén ez az eszköz a tipográfiát rakja rendbe, és egyébként csendben
marad.** Gyengébb vagy gyorsabb modell szövegén dolgozik. Ez egyben azt is jelenti, hogy egy
„gépi jelek” katalógus mozgó célpont – a szólisták ezért visznek felülvizsgálati dátumot.

A harmadik kör nem stílust mért, hanem azt tette lehetővé, hogy egyáltalán mérni lehessen: a
kimenetnek fix alakja lett, és egy szkript olvassa. Előtte kézzel kellett átnézni minden futást,
ami pár tucatnál tovább nem skálázódik.

## Mikor ne használd

- **Ha a szöveg nem magyar.** Van benne nyelvi kapu, ami megáll és átad, de akkor minek indítsd el.
- **Ha helyesírás-ellenőrzőt keresel.** Nem az, és ez szándékos. Egy elmaradt kettőzés vagy egy
  kétfelé írt összetett szó átmegy rajta.
- **Ha azt akarod, hogy egy AI-detektor ne fogja meg a szöveget.** Nem erre való, és nem is
  működne: a tipográfia rendbetétele semmit nem rejt el.
- **Ha jogi szöveget akarsz „közérthetőbbre” írni.** Szerződésben a hivatalos névszói szerkezet a
  helyes alak, és az eszköz ezért kapcsol ki egész passzokat, ha szerződést lát. A közérthető
  változat külön munka, nem lektorálás.

## Amit nem tud, és nem is állítja

- **A stilisztikai réteg a gyenge pont.** Az első kör vakteszten megbukott: amit az eszköz
  átírt, azt egy anyanyelvi fül elutasította, amit viszont nem mert átírni, azt kilencből nyolc
  esetben elvégezték volna. Ez a rész átdolgozásra vár, és ezt nem takarítjuk el.
- **Nincs mögötte mért adat arról, hogy egy modell milyen gyakran ír így.** Nyelvészeti forrás van,
  van köztük számszerű is – de az azt méri, hogyan írnak *emberek*. Ezért a 47 stilisztikai minta
  **mindegyike** kérdőjelet visel a katalógusban: a jelölés azt mondja, hogy az erősség becslés,
  nem mérés.
- **Nem helyesírás-ellenőrző.** Szándékosan. A minták arra vannak kiélezve, ami géptől jön, ezért
  egy elmaradt kettőzés vagy egy kétfelé írt összetétel átmegy rajta – akkor is, ha a szövegben
  épp az az egyetlen kétségtelen hiba.
- **Nem AI-detektor**, és nem is arra van, hogy egy szöveg kikerüljön egy AI-detektort.
- **Nem homokozó.** Nem ír fájlt – de ezt nem a rendszer kényszeríti ki, hanem az utasítás.
  Lemértük. Tartsd verziókövetésben a szövegeidet, mint bármi mást.

## Ha nem értesz egyet

Az a jó. Az egészet **egy ember** ítélte meg, aki egyben az eszköz szerzője is – ezt a
`docs/validation.md` ki is mondja. Ha egy minta szerinted rossz, nyiss egy
[issue-t](https://github.com/Hirannad/stet/issues): melyik minta, melyik mondat, és miért nem hiba
az, amit kijavított. A fejlesztés során **négy** mintát kellett törölni vagy gyengíteni, mert a
hivatkozott forrás nem azt írta, amit a minta állított – egy esetben épp az ellenkezőjét. Ez itt a
várható hibamód, nem a kivételes.

## Licenc

MIT – lásd [LICENSE](LICENSE). Ami máshonnan jön, és milyen feltételekkel, az a
[NOTICE.md](NOTICE.md)-ben van. A magyar nyelvi források és az, hogy melyik állítás mérés és melyik
becslés, a [sources.md](skills/stet-hungarian/references/sources.md)-ben.
