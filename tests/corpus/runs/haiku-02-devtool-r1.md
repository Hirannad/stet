<!-- stet-run: source=skills/stet-hungarian sha256=22f8a1a7 date=2026-08-17 -->

## 0. Nyelv és regiszter

A szöveg magyar (angol szakszavakkal tűzdelve, de a próza végig magyar). A regisztert az operátor **rögzítette**, nem én vezettem le: a szöveget `neutral` regiszterként kezelem. A Pass 5 ezért mérsékelt módban fut, a Pass 3 pedig teljesen.

## 1. A javított szöveg

```
# Ellenőr – CI-hibagyűjtő eszköz

## Bevezetés

Az Ellenőr egy fejlesztőcsapatok számára tervezett szoftver, amely automatikusan gyűjti össze, rendezi és elemzi a CI-futások hibáit. A célja, hogy egyetlen helyen lássák az összes build-problémát, így a csapat gyorsabban tudjon reagálni és csökkenteni a regression-okat.

## Mit csinál?

Az Ellenőr integrálódik a CI-rendszerekkel (GitHub Actions, GitLab CI, Jenkins, CircleCI) az API-n keresztül. Figyeli az összes sikertelen futást, és azokból kiszedi a releváns hibaüzeneteket. Nem csak azt rögzíti, hogy mi romlott meg, hanem azt is, hogy mikor, melyik commitban, és mely fejlesztő mergelte be.

Az eszköz ezután összegyűjti az azonos jellegű hibákat. Ha például az elmúlt egy hét alatt ötször volt timeout-hiba a teszt suite-ban, az Ellenőr azt egyetlen sor alatt mutatja, és javasol mintázatot. Ez nagyon hasznos ahhoz, hogy azonosítsuk a szisztematikus problémákat – például egy másodlagos infrastruktúrán vagy egy nagyobb refactoring után.

## Jellemzők

**Valós idejű értesítés**: Rögtön kapnak figyelmeztető üzenetet Slack-en vagy e-mailben, amikor egy CI-futás meghibásodik, egy vagy több hasonló hiba után.

**Hibamintázat-felismerés**: Az Ellenőr gépi tanulást alkalmazhat, hogy csoportosítsa az egymáshoz hasonló hibákat, még akkor is, ha eltérő stack trace-szel vagy hibaüzenettel jelenik meg.

**Trend-analízis**: Az eszköz mutatja, hogy mely hibák ismétlődnek, mely commitok vezetnek bukáshoz, és mely fejlesztőcsapatrészek felelősek a legtöbb hibáért – nem büntetésből, hanem támogatás végett.

**Dashboard és jelentések**: Egy webes felület mutatja az összes hiba előzményeit, szűrni lehet dátum, repository, hibatype vagy fejlesztő szerint. Heti vagy havi összefoglalót is készít automatikusan.

**Integráció a munkafolyamattal**: Közvetlenül linkelhető a Jirába vagy más issue tracker-be, így a CI-hiba rögtön egy ticket, ha szükséges.

## Használat

Az Ellenőr beállítása egyszerű: csatlakoztatod a CI-rendszeredet (API-key megadásával), és kiválasztod, mely projectek és branchek vizsgáljanak. Az eszköz azonnal kezd figyelni és gyűjteni. Az első nap után már látni lehet az alapvető statisztikákat.

A csapat tagjai beléphetnek a webes felületre és böngészhetik a hibákat. A senior fejlesztő vagy a tech lead gyorsan átláthatja, hogy mely problémák sürgősek, és mely podem halasztható vagy akár kívánatos-e rá visszatérni.

## Előnyök

Mivel a CI-hibák centralizálva vannak, nem maradnak el. Az a srác, aki gyorsan akar commitolni, nem mulaszthatja le, hogy a fejlesztő ágában egy korábbi failure van. Az Ellenőr azt közli: „Ez nem jó”. Ez nem rosszindulat, csak tény.

A hibamintázat-felismerés miatt nem egyesével debuggolunk – nem azért, mert fájl xyz-ből jön a hiba, hanem azért, mert az Ellenőr azt mutatja, hogy öt hasonló timeout-hiba ugyanabban az okból származott.

A végeredmény: kevesebb regexe, gyorsabb fix-ek és a csapat jobb intuíciója a kódqualityről.

## Árak és támogatás

Az Ellenőr ingyenes kis csapatoknál (5 fejlesztő alatt), és patnered díjú csomagok érhetők el nagyobb szervezeteknek. Az előfizetés tartalmazza a frissítéseket, az API-hozzáférést és a 24 órás e-mail támogatást.
```

## 2. Változástábla

| ID | Eredeti | Új | Indok |
|---|---|---|---|
| HU-G14 | `integrálódik a CI-rendszerektől` | `integrálódik a CI-rendszerekkel` | az angol `integrates with` prepozíciója rossz esetraggal jött át; a magyar vonzat itt `-val/-vel` |
| HU-T11 | `infrastruktúrán, vagy egy nagyobb refactoring` | `infrastruktúrán vagy egy nagyobb refactoring` | magyarul nincs Oxford-vessző: a `vagy` kötőszó elé felsorolásban nem kerül vessző |
| HU-F04 | `kapnak egy figyelmeztető üzenetet` | `kapnak figyelmeztető üzenetet` | angolos `egy` névelő; a felsorolásban ötször áll, a bekezdés klaszterpontszáma 4 |
| HU-M12 | `error message-szel` | `hibaüzenettel` | a szöveg ugyanezt máshol `hibaüzenet`-nek nevezi; nem magyarítás, hanem terminológiai következetesség |
| HU-T12 | `a Jira-ba` | `a Jirába` | magánhangzóra végződő idegen névhez a toldalék kötőjel nélkül kapcsolódik |
| HU-T01 | `„Ez nem jó"` | `„Ez nem jó”` | a záró idézőjel angol egyenes alakban maradt a helyes nyitó mellett |
| HU-R09 | `nem szalámis-slice jellegűen debuggolunk` | `nem egyesével debuggolunk` | bevezetetlen, magyarul nem adatolható kifejezés; a hétköznapi megfelelőt a mondat saját szembeállítása adja, új tény nélkül |
| HU-T11 | `gyorsabb fix-ek, és a csapat` | `gyorsabb fix-ek és a csapat` | Oxford-vessző az `és` előtt, három azonos szerepű mondatrész felsorolásában |
| HU-T11 | `az API-hozzáférést, és a 24 órás` | `az API-hozzáférést és a 24 órás` | Oxford-vessző az `és` előtt, három azonos szerepű mondatrész felsorolásában |

## 3. Gyanús, de nem javítottam

- **HU-T11** [uncertain] – `mikor, melyik commitban, és mely fejlesztő mergelte be`: nem dőlt el, hogy felsorolás-e (akkor a vessző hibás) vagy tagmondathatár-e (akkor kötelező), mert a harmadik tagnak saját alanya és állítmánya van. Bizonytalanság esetén nem nyúlok hozzá.
- **HU-L06** [pattern-exception] – `Nem csak azt rögzíti…, hanem azt is…`: a saját `Mikor NE`-je blokkolja, az ellentét valódi (mit vs. mikor/ki), és bekezdésenként egy ilyen keret rendben van.
- **HU-T14** [uncertain] – `a teszt suite-ban`: félig fordított összetétel. A minta példái meghonosodott magyar tagpárok; itt az utótag angol marad, és a helyes írásmód (`tesztsuite`, `test suite`) nem dönthető el hipotézis nélkül.
- **HU-G06** [pattern-exception] – `és javasol mintázatot`: angol SVO-sorrend, magyarul `mintázatot javasol` lenne a semleges. A minta `Mikor NE`-je viszont kimondja, hogy csak elveszett azonosító fókusz esetén fut – itt nincs ilyen.
- **HU-M01** [pattern-exception] – `Rögtön kapnak…`: alany nélküli T/3, miközben a „Használat” szakasz tegez (`csatlakoztatod`, `a CI-rendszeredet`), máshol pedig T/1 áll (`debuggolunk`). Nincs önözés, tehát nincs klasszikus keveredés, és fejlesztői eszközben a tegezés legitim (HU-M04 `Mikor NE`) – a többségi forma nem állapítható meg, a szerzőé a döntés.
- **HU-T10** [pattern-exception] – `Trend-analízis`: kétrészes összetétel fölösleges kötőjellel (`trendanalízis`). A minta a 6:3-as és a mozgószabályt írja elő, a fölös kötőjel kivételét nem – és a katalógus a rosszul kötőjelezett összetételt kifejezetten hatókörön kívülinek mondja.
- **HU-M12** [paragraph-budget] – `hibatype`: magyar–angol hibrid szóalak. A bekezdés (a teljes „Jellemzők” felsorolás) 2 `SOFT` javítási kerete elfogyott (HU-F04, HU-M12).
- **HU-F04** [paragraph-budget] – `Egy webes felület mutatja`: angolos `egy` mondat élén. Ugyanaz a kerethiány.
- **HU-F04** [paragraph-budget] – `a CI-hiba rögtön egy ticket`: angolos `egy` névszói állítmány előtt. Ugyanaz a kerethiány.
- **nincs minta** [no-pattern] – `mely projectek és branchek vizsgáljanak`: vonzatszerepek felcserélve, a projektek a vizsgálat tárgyai, nem alanyai (`mely projekteket és brancheket vizsgálja`). Egyik minta sem fedi, a diff-audit ID nélküli javítást visszavonatna.
- **nincs minta** [no-pattern] – `mely podem halasztható vagy akár kívánatos-e rá visszatérni`: a `podem` nem magyar szó, és a tagmondat két kérdésformát kever. A javításhoz ki kellene találni, mit akart mondani.
- **nincs minta** [no-pattern] – `Az a srác, aki…, nem mulaszthatja le`: regisztertörés a dokumentációs hangban, plusz nem létező igekötős alak (`elmulaszt` helyett). Egyik jelenségre sincs minta.
- **nincs minta** [no-pattern] – `fájl xyz-ből`, `ugyanabban az okból származott`: angolos szórend a jelzős szerkezetben, illetve a mutató névmás esetragja nem egyezik a főnévével (`ugyanabból az okból`). Nyelvtani hiba, nem gépi jel – nincs rá minta.
- **nincs minta** [no-pattern] – `kevesebb regexe`, `kódqualityről`: elrontott, illetve hibrid szóalakok. A katalógus szándékosan nem helyesírás-ellenőrző.
- **nincs minta** [no-pattern] – `patnered díjú csomagok`: elrontott szóalak, a jelentése sem egyértelmű (`fizetős`? `partneri`?). Ugyanaz az ok.
- **nincs minta** [preserve] – `Ez nem rosszindulat, csak tény.`: **szándékosan megtartva.** Rövid, töredékes mondat két hosszabb után – megőrizendő emberi ritmusjel, és a bekezdésben van konkrétum, tehát a HU-R11 felülírása sem tüzel.

## 4. Klaszterpontok

| # | Kezdet | Pont | Minták |
|---|---|---|---|
| 1 | `Az Ellenőr egy fejlesztőcsapatok…` | 0 | nincs |
| 2 | `Az Ellenőr integrálódik a CI-rendszerekkel…` | 0 | nincs |
| 3 | `Az eszköz ezután összegyűjti…` | 0 | nincs |
| 4 | `**Valós idejű értesítés**…` (a teljes „Jellemzők” felsorolás) | 4 | HU-F04, HU-M12 |
| 5 | `Az Ellenőr beállítása egyszerű…` | 0 | nincs |
| 6 | `A csapat tagjai beléphetnek…` | 0 | nincs |
| 7 | `Mivel a CI-hibák centralizálva vannak…` | 0 | nincs |
| 8 | `A hibamintázat-felismerés miatt…` | 2 | HU-R09 |
| 9 | `A végeredmény: kevesebb regexe…` | 0 | nincs |
| 10 | `Az Ellenőr ingyenes kis csapatoknál…` | 0 | nincs |
