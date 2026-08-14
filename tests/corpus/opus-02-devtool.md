# Ellenőr — rend a CI-hibák között

## A probléma, amit ismerünk

A pipeline pirosra vált. Valaki megnyitja a futást, végigpörgeti a nyolcezer soros logot, és a hetedik percben megtalálja a lényeget: egy timeout egy teszt setupjában. Aztán másnap ugyanez, csak más ágon, más ember, újabb hét perc. A hét végén senki nem tudja megmondani, hogy ez most egy hiba volt tizennégyszer, vagy tizennégy hiba egyszer.

Az Ellenőr erre készült. Nem CI-rendszer, nem váltja le a meglévőt: mellé áll, és összeszedi, ami a futásokból kihullik.

## Mit csinál

**Kigyűjti a hibát a logból.** Az Ellenőr a nyers kimenetből kiemeli a valódi hibarészt — a stack trace-t, a failed assertiont, a nem nulla kilépési kódot adó parancsot és annak utolsó sorait. A többi kétszáz sor build-zajt nem kell látnod, de egy kattintással ott van, ha mégis kell.

**Csoportosítja.** Ez a lényegi rész. Az azonos gyökerű hibák egy ujjlenyomatot kapnak, akkor is, ha a szövegük eltér — más sorszám, más konténer-ID, más időbélyeg. Így nem tizennégy piros futást látsz, hanem egy hibát tizennégy előfordulással, mellette azzal, hogy mikor jelent meg először és melyik ágakon él.

**Megmutatja, mi új és mi visszatérő.** A lista tetején az kerül, ami ma jött be először, mert azt valószínűleg egy friss commit hozta. Alatta a régi ismerősök, gyakoriság szerint. A flaky tesztek külön jelölést kapnak: az Ellenőr látja, ha ugyanaz a teszt ugyanazon a commiton egyszer elhasal, egyszer átmegy.

**Szól, de nem gyakran.** Egy hibaosztály első megjelenésekor küld egy értesítést Slackre vagy e-mailben, utána hallgat róla. Az összefoglaló naponta egyszer megy ki: mi nyílt, mi zárult, mi eszi a legtöbb CI-időt.

## Hogyan kapcsolható be

Az Ellenőr a CI-szolgáltató API-ján keresztül olvassa a futásokat. GitHub Actions, GitLab CI és Jenkins esetén elég egy olvasási jogú token és a repók kijelölése — a pipeline-fájlokhoz nem kell hozzányúlni. Egyéb rendszerekhez van egy CLI, ami a build végén feltölti a logot.

Az első futásokból az Ellenőr visszamenőleg is feldolgozza a megőrzött előzményeket, így a bekapcsolás után nem üres felülettel indulsz, hanem az elmúlt harminc nap képével.

## Amit nem csinál

Nem javítja meg a hibát, és nem tippel arról, melyik commit okozta — csak megmutatja, mi változott a hiba megjelenése körül. Nem gyűjt éles üzemi telemetriát: az Ellenőr a CI-ban marad. A logokat harminc napig tartja meg, utána csak az összesített adat marad. Titkos értékeket a feltöltés előtt kimaszkol a mintáid alapján.

## Mit nyersz vele

A csapatok nálunk két dolgot említenek. Az egyik a keresés megszűnése: a hiba lényege az első képernyőn van. A másik a vita megszűnése arról, hogy „ez a teszt csak néha bukik" — mert ott a szám, hogy pontosan hányszor.
