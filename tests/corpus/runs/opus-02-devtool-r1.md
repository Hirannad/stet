## 0. Nyelv és regiszter

A szöveg magyar; az angol szakszavak (`stack trace`, `failed assertion`, `flaky`) idegen nyelvű betétek, tehát érinthetetlen zónák. A regisztert a hívó rögzítette: `neutral` – nem következtettem rá, és nem is mérlegeltem. A megszólítás végig tegező (`nem kell látnod`, `a mintáid alapján`), ezt a HU-M01 szerint megtartom.

## 1. A javított szöveg

```
# Ellenőr – rend a CI-hibák között

## A probléma, amit ismerünk

A pipeline pirosra vált. Valaki megnyitja a futást, végigpörgeti a nyolcezer soros logot, és a hetedik percben megtalálja a lényeget: egy timeout egy teszt setupjában. Aztán másnap ugyanez, csak más ágon, más ember, újabb hét perc. A hét végén senki nem tudja megmondani, hogy ez most egy hiba volt tizennégyszer, vagy tizennégy hiba egyszer.

Az Ellenőr erre készült. Nem CI-rendszer, nem váltja le a meglévőt: mellé áll, és összeszedi, ami a futásokból kihullik.

## Mit csinál

**Kigyűjti a hibát a logból.** Az Ellenőr a nyers kimenetből kiemeli a valódi hibarészt – a stack trace-t, a failed assertiont, a nem nulla kilépési kódot adó parancsot és annak utolsó sorait. A többi kétszáz sor build-zajt nem kell látnod, de egy kattintással ott van, ha mégis kell.

**Csoportosítja.** Ez a lényegi rész. Az azonos gyökerű hibák egy ujjlenyomatot kapnak, akkor is, ha a szövegük eltér – más sorszám, más konténer-ID, más időbélyeg. Így nem tizennégy piros futást látsz, hanem egy hibát tizennégy előfordulással, mellette azzal, hogy mikor jelent meg először és melyik ágakon él.

**Megmutatja, mi új és mi visszatérő.** A lista tetejére az kerül, ami ma jött be először, mert azt valószínűleg egy friss commit hozta. Alatta a régi ismerősök, gyakoriság szerint. A flaky tesztek külön jelölést kapnak: az Ellenőr látja, ha ugyanaz a teszt ugyanazon a commiton egyszer elhasal, egyszer átmegy.

**Szól, de nem gyakran.** Egy hibaosztály első megjelenésekor küld egy értesítést Slackre vagy e-mailben, utána hallgat róla. Az összefoglaló naponta egyszer megy ki: mi nyílt, mi zárult, mi eszi a legtöbb CI-időt.

## Hogyan kapcsolható be

Az Ellenőr a CI-szolgáltató API-ján keresztül olvassa a futásokat. GitHub Actions, GitLab CI és Jenkins esetén elég egy olvasási jogú token és a repók kijelölése – a pipeline-fájlokhoz nem kell hozzányúlni. Egyéb rendszerekhez van egy CLI, ami a build végén feltölti a logot.

Az első futásokból az Ellenőr visszamenőleg is feldolgozza a megőrzött előzményeket, így a bekapcsolás után nem üres felülettel indulsz, hanem az elmúlt harminc nap képével.

## Amit nem csinál

Nem javítja meg a hibát, és nem tippel arról, melyik commit okozta – csak megmutatja, mi változott a hiba megjelenése körül. Nem gyűjt éles üzemi telemetriát: az Ellenőr a CI-ban marad. A logokat harminc napig tartja meg, utána csak az összesített adat marad. Titkos értékeket a feltöltés előtt kimaszkol a mintáid alapján.

## Mit nyersz vele

A csapatok nálunk két dolgot említenek. Az egyik a keresés megszűnése: a hiba lényege az első képernyőn van. A másik a vita megszűnése arról, hogy „ez a teszt csak néha bukik” – mert ott a szám, hogy pontosan hányszor.
```

## 2. Változástábla

| ID | Eredeti | Új | Indok |
|---|---|---|---|
| HU-T02 | `Ellenőr — rend` | `Ellenőr – rend` | em dash a főcímben; magyarul szóközös félkvirtmínusz a gondolatjel |
| HU-T02 | `hibarészt — a stack trace-t` | `hibarészt – a stack trace-t` | em dash gondolatjel helyett |
| HU-T02 | `eltér — más sorszám` | `eltér – más sorszám` | em dash gondolatjel helyett |
| HU-G14 | `A lista tetején az kerül` | `A lista tetejére az kerül` | a `kerül` irányhatározót vonz; az angol `at the top of the list` helyviszonya jött át |
| HU-T02 | `kijelölése — a pipeline-fájlokhoz` | `kijelölése – a pipeline-fájlokhoz` | em dash gondolatjel helyett |
| HU-T02 | `okozta — csak megmutatja` | `okozta – csak megmutatja` | em dash gondolatjel helyett |
| HU-T01 | `csak néha bukik"` | `csak néha bukik”` | angol záró idézőjel magyar mondatban |
| HU-T02 | `— mert ott a szám` | `– mert ott a szám` | em dash gondolatjel helyett |

## 3. Gyanús, de nem javítottam

- **HU-H05** – `GitHub Actions, GitLab CI és Jenkins esetén`: `neutral` profilban a kapu nyitva állna, de egyetlen `esetén` áll a mondatban, halmozódás nincs. A `ha`-mellékmondatra bontás három idegen terméknév toldalékolását kívánná (HU-T12), és az `és`-t `vagy`-ra váltaná, ami a kvantor hatókörét érinti – ezt a tartalmi invariáns tiltja.
- **HU-F01** – `a keresés megszűnése`, `a vita megszűnése`: két `-és` főnév egy-egy birtokos szerkezetben, igésíthető lenne. A bekezdés `SOFT` pontösszege 2, a küszöb 3 – a klaszterkapu zárva.
- **HU-G14** – `nem tippel arról, melyik commit okozta`: a `tippel` vonzata ingadozik, és a minta `Mikor NE`-je épp a többvonzatú igéket zárja ki. A `lista tetején` esetével szemben itt nincs egyértelmű hiba.
- **HU-L06** – `nem tizennégy piros futást látsz, hanem…` és `nem üres felülettel indulsz, hanem…`: a negatív párhuzam visszatér a szövegben, de bekezdésenként csak egyszer, és mindkettő átmegy a szalmabáb-teszten. A klaszter-felülíráshoz kettő kellene egy bekezdésen belül.
- **HU-R03** – `más sorszám, más konténer-ID, más időbélyeg`, illetve `mi nyílt, mi zárult, mi eszi a legtöbb CI-időt`: a hármasság visszatér, de a tagok nem párhuzamos `-ás/-és` főnevek, és nem áll minden bekezdésben hármas. A minta saját szabálya tiltja a javítást.
- **HU-R02, HU-R08** – négy egymást követő bekezdés azonos sémára épül: félkövér nyitómondat, majd kifejtés. Dokumentációban a tagolás funkció, nem dísz, a Pass 5 pedig `neutral` profilban mérsékelt, 4-es küszöbbel – kétszeresen zárt.
- **HU-M09** – a címsorséma (`Mit csinál`, `Hogyan kapcsolható be`, `Amit nem csinál`, `Mit nyersz vele`) terméklap-sablonra emlékeztet. Kérdőjel és átvezető kérdés viszont sehol nincs, a címsorok állító tagmondatok; a szerkezet a szerző döntése.
- **HU-M04, HU-M01** – a szöveg végig tegez. A HU-M04 `neutral` profilban önözést kérne, de a HU-M01 felülírja: a meglévő, következetes forma nyer. Szándékos nem-javítás.
- **nincs minta** – `küld egy értesítést Slackre vagy e-mailben`: a két bővítmény eltérő ragot visel, ezért a mellérendelés döccen. A katalógusban nincs erre minta, és mindkét vonzat önmagában helyes.
