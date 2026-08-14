---
title: Ellenőr — CI hibák egy helyen
type: reference
status: active
updated: 2026-08-14
---

# Ellenőr

Az Ellenőr egy fejlesztői eszköz, amely a CI-futások hibáit gyűjti össze, csoportosítja és rendezhető formában teszi elérhetővé a csapat számára. A cél egyszerű: senki ne töltsön napi fél órát azzal, hogy build logokat böngészve próbálja megérteni, miért bukott el a pipeline már megint.

## Mi a probléma, amit megold

Egy közepes méretű csapatnál naponta több tucat CI-futás fut le, és ezek egy része elbukik – néha valódi hiba miatt, néha flaky teszt miatt, néha egy külső szolgáltatás pillanatnyi kiesése miatt. A logok általában szét vannak szórva a CI szolgáltató felületén, és ha valaki utólag akarja megérteni, mi történt tegnap délután, gyakran több kattintással sem talál rá a lényegre. Az Ellenőr ezt a szétszórtságot szünteti meg: minden futás hibaüzenetét egy központi felületen gyűjti össze, és megkeresi köztük a mintázatokat.

## Hogyan működik

Az Ellenőr egy könnyű ügynököt köt a CI rendszerhez – GitHub Actionshöz, GitLab CI-hoz és Jenkinshez is van kész integráció –, amely minden futás végén elküldi a log kimenetet és a metaadatokat (branch, commit, futásidő, státusz). A beérkező hibákat az Ellenőr automatikusan kategorizálja: fordítási hiba, teszthiba, timeout, infrastrukturális probléma, vagy ismeretlen kategória. A hasonló hibaüzeneteket összevonja egy csoportba, így azonnal látszik, ha ugyanaz a teszt harmadszor bukik el egy héten belül, vagy ha egy új típusú hiba jelent meg csak most reggel óta.

A felületen szűrhetünk repository, branch, időszak és hibakategória szerint. Minden hibacsoporthoz tartozik egy trend-nézet, amely megmutatja, mikor jelent meg először, milyen gyakran fordul elő, és mely commitok érintettek. Ha egy hiba flaky tesztre utal – vagyis ugyanaz a teszt hol lefut, hol nem, kód-módosítás nélkül –, az Ellenőr külön jelöléssel látja el, hogy ne kelljen mindig manuálisan kideríteni.

## Kinek ajánljuk

Elsősorban azoknak a csapatoknak hasznos, ahol a CI-futások száma és a hozzájuk tartozó zaj már meghaladja azt a szintet, amit egy ember fejben tud tartani. Ha a csapatban rendszeresen elhangzik a „megint ez a teszt bukik, de nem tudom, miért” mondat, az Ellenőr valószínűleg időt spórol.

## Integráció és beállítás

A telepítés egy CLI paranccsal indul, amely regisztrálja a webhookot a CI szolgáltatónál, és létrehozza az első projektet az Ellenőr felületén. A finomhangolás – kategóriák testreszabása, riasztási küszöbök, Slack-integráció a napi összefoglalóhoz – a beállítások menüben történik, külön dokumentáció nélkül is átlátható.

Az Ellenőr nem helyettesíti a CI rendszert, csak a hibák utólagos átlátását teszi egyszerűbbé.
