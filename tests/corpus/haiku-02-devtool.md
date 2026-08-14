# Ellenőr – CI-hibagyűjtő eszköz

## Bevezetés

Az Ellenőr egy fejlesztőcsapatok számára tervezett szoftver, amely automatikusan gyűjti össze, rendezi és elemzi a CI-futások hibáit. A célja, hogy egyetlen helyen lássák az összes build-problémát, így a csapat gyorsabban tudjon reagálni és csökkenteni a regression-okat.

## Mit csinál?

Az Ellenőr integrálódik a CI-rendszerektől (GitHub Actions, GitLab CI, Jenkins, CircleCI) az API-n keresztül. Figyeli az összes sikertelen futást, és azokból kiszedi a releváns hibaüzeneteket. Nem csak azt rögzíti, hogy mi romlott meg, hanem azt is, hogy mikor, melyik commitban, és mely fejlesztő mergelte be.

Az eszköz ezután összegyűjti az azonos jellegű hibákat. Ha például az elmúlt egy hét alatt ötször volt timeout-hiba a teszt suite-ban, az Ellenőr azt egyetlen sor alatt mutatja, és javasol mintázatot. Ez nagyon hasznos ahhoz, hogy azonosítsuk a szisztematikus problémákat – például egy másodlagos infrastruktúrán, vagy egy nagyobb refactoring után.

## Jellemzők

**Valós idejű értesítés**: Rögtön kapnak egy figyelmeztető üzenetet Slack-en vagy e-mailben, amikor egy CI-futás meghibásodik, egy vagy több hasonló hiba után.

**Hibamintázat-felismerés**: Az Ellenőr gépi tanulást alkalmazhat, hogy csoportosítsa az egymáshoz hasonló hibákat, még akkor is, ha eltérő stack trace-szel vagy error message-szel jelenik meg.

**Trend-analízis**: Az eszköz mutatja, hogy mely hibák ismétlődnek, mely commitok vezetnek bukáshoz, és mely fejlesztőcsapatrészek felelősek a legtöbb hibáért – nem büntetésből, hanem támogatás végett.

**Dashboard és jelentések**: Egy webes felület mutatja az összes hiba előzményeit, szűrni lehet dátum, repository, hibatype vagy fejlesztő szerint. Heti vagy havi összefoglalót is készít automatikusan.

**Integráció a munkafolyamattal**: Közvetlenül linkelhető a Jira-ba vagy más issue tracker-be, így a CI-hiba rögtön egy ticket, ha szükséges.

## Használat

Az Ellenőr beállítása egyszerű: csatlakoztatod a CI-rendszeredet (API-key megadásával), és kiválasztod, mely projectek és branchek vizsgáljanak. Az eszköz azonnal kezd figyelni és gyűjteni. Az első nap után már látni lehet az alapvető statisztikákat.

A csapat tagjai beléphetnek a webes felületre és böngészhetik a hibákat. A senior fejlesztő vagy a tech lead gyorsan átláthatja, hogy mely problémák sürgősek, és mely podem halasztható vagy akár kívánatos-e rá visszatérni.

## Előnyök

Mivel a CI-hibák centralizálva vannak, nem maradnak el. Az a srác, aki gyorsan akar commitolni, nem mulaszthatja le, hogy a fejlesztő ágában egy korábbi failure van. Az Ellenőr azt közli: „Ez nem jó". Ez nem rosszindulat, csak tény.

A hibamintázat-felismerés miatt nem szalámis-slice jellegűen debuggolunk – nem azért, mert fájl xyz-ből jön a hiba, hanem azért, mert az Ellenőr azt mutatja, hogy öt hasonló timeout-hiba ugyanabban az okból származott.

A végeredmény: kevesebb regexe, gyorsabb fix-ek, és a csapat jobb intuíciója a kódqualityről.

## Árak és támogatás

Az Ellenőr ingyenes kis csapatoknál (5 fejlesztő alatt), és patnered díjú csomagok érhetők el nagyobb szervezeteknek. Az előfizetés tartalmazza a frissítéseket, az API-hozzáférést, és a 24 órás e-mail támogatást.
