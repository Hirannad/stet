<!-- stet-run: source=skills/stet-hungarian sha256=22f8a1a7 date=2026-08-17 -->

## 0. Nyelv és regiszter

A szöveg magyar. A regisztert a hívó **rögzítette**: a szöveget `neutral` regiszterként kezelem, nem én vezettem le. (A szöveg egyébként is ide esne: fejlesztői termékdokumentáció, nincs benne jogi terminus, közvetlen megszólítás sincs, a szerző T/1-et használ.)

## 1. A javított szöveg

```
---
title: Ellenőr — CI hibák egy helyen
type: reference
status: active
updated: 2026-08-14
---

# Ellenőr

Az Ellenőr egy fejlesztői eszköz, amely a CI-futások hibáit gyűjti össze, csoportosítja és rendezhető formában teszi elérhetővé a csapat számára. A cél egyszerű: senki ne töltsön napi fél órát azzal, hogy build logokat böngészve próbálja megérteni, miért bukott el a pipeline már megint.

## Mi a probléma, amit megold

Egy közepes méretű csapatnál naponta több tucat CI-futás fut le, és ezek egy része elbukik – néha valódi hiba miatt, néha flaky teszt miatt, néha egy külső szolgáltatás pillanatnyi kiesése miatt. A logok általában szét vannak szórva a CI-szolgáltató felületén, és ha valaki utólag akarja megérteni, mi történt tegnap délután, gyakran több kattintással sem talál rá a lényegre. Az Ellenőr ezt a szétszórtságot szünteti meg: minden futás hibaüzenetét egy központi felületen gyűjti össze, és megkeresi köztük a mintázatokat.

## Hogyan működik

Az Ellenőr egy könnyű ügynököt köt a CI-rendszerhez – GitHub Actionshöz, GitLab CI-hoz és Jenkinshez is van kész integráció –, amely minden futás végén elküldi a logkimenetet és a metaadatokat (branch, commit, futásidő, státusz). A beérkező hibákat az Ellenőr automatikusan kategorizálja: fordítási hiba, teszthiba, timeout, infrastrukturális probléma vagy ismeretlen kategória. A hasonló hibaüzeneteket összevonja egy csoportba, így azonnal látszik, ha ugyanaz a teszt harmadszor bukik el egy héten belül, vagy ha egy új típusú hiba jelent meg csak most reggel óta.

A felületen szűrhetünk repository, branch, időszak és hibakategória szerint. Minden hibacsoporthoz tartozik egy trend-nézet, amely megmutatja, mikor jelent meg először, milyen gyakran fordul elő, és mely commitok érintettek. Ha egy hiba flaky tesztre utal – vagyis ugyanaz a teszt hol lefut, hol nem, kód-módosítás nélkül –, az Ellenőr külön jelöléssel látja el, hogy ne kelljen mindig manuálisan kideríteni.

## Kinek ajánljuk

Elsősorban azoknak a csapatoknak hasznos, ahol a CI-futások száma és a hozzájuk tartozó zaj már meghaladja azt a szintet, amit egy ember fejben tud tartani. Ha a csapatban rendszeresen elhangzik a „megint ez a teszt bukik, de nem tudom, miért” mondat, az Ellenőr valószínűleg időt spórol.

## Integráció és beállítás

A telepítés egy CLI-paranccsal indul, amely regisztrálja a webhookot a CI-szolgáltatónál, és létrehozza az első projektet az Ellenőr felületén. A finomhangolás – kategóriák testreszabása, riasztási küszöbök, Slack-integráció a napi összefoglalóhoz – a beállítások menüben történik, külön dokumentáció nélkül is átlátható.

Az Ellenőr nem helyettesíti a CI-rendszert, csak a hibák utólagos átlátását teszi egyszerűbbé.
```

## 2. Változástábla

| ID | Eredeti | Új | Indok |
|---|---|---|---|
| HU-T14 | `a CI szolgáltató felületén` | `a CI-szolgáltató felületén` | angol mintájú különírás; betűszóhoz az összetételi utótag kötőjellel járul, és a szöveg máshol maga is `CI-futás` alakot ír |
| HU-T14 | `a CI rendszerhez`, `a log kimenetet` | `a CI-rendszerhez`, `a logkimenetet` | ugyanaz az angol mintájú különírás: betűszó + utótag kötőjellel, köznévi összetétel egybe |
| HU-T11 | `infrastrukturális probléma, vagy ismeretlen kategória` | `infrastrukturális probléma vagy ismeretlen kategória` | Oxford-vessző: felsorolásban a `vagy` elé magyarul nem kerül vessző |
| HU-T14 | `egy CLI paranccsal`, `a CI szolgáltatónál` | `egy CLI-paranccsal`, `a CI-szolgáltatónál` | angol mintájú különírás, betűszó + összetételi utótag |
| HU-T14 | `a CI rendszert` | `a CI-rendszert` | angol mintájú különírás, betűszó + összetételi utótag |

## 3. Gyanús, de nem javítottam

- **HU-T02** [zone] – `Ellenőr — CI hibák egy helyen`: a front matter `title` mezőjében em dash áll szóközös gondolatjel helyett. A strukturált metaadat érinthetetlen zóna, ezért változatlanul hagytam; a mező javítása a szerző döntése.
- **HU-F04** [pattern-exception] – `Az Ellenőr egy fejlesztői eszköz`: angolos `egy` a névszói állítmány előtt, magyarul `Az Ellenőr fejlesztői eszköz` a semlegesebb. A minta `Jelek` feltétele viszont nem teljesül (egyetlen `egy` a bekezdésben, és nem elvont főnév előtt), a bekezdés pontszáma pedig nem éri el a küszöböt.
- **HU-H03** [pattern-exception] – `A finomhangolás … a beállítások menüben történik`: alakilag a `történik`-minta, de itt a `történik` valódi helyhatározói jelentésű, a mondat állítása maga a hely. Bármelyik igésítés vagy cselekvőt találna ki, vagy szétverné a közbevetett felsorolást, ezért a minta saját `Mikor NE`-je alá esik.
- **HU-T14** [pattern-exception] – `build logokat`: kéttagú, teljes egészében idegen írásmódú kifejezés, amit a magyar különírva hagy. Ez más eset, mint a `logkimenet`, ahol a magyar utótag miatt az összetétel egyértelmű, ezért ezt nem vontam össze.
- **HU-M09** [pattern-exception] – a `Mi a probléma, amit megold` és a `Hogyan működik` kérdés alakú alcímsor. A minta másik fele hiányzik: nincsenek átvezető kérdések és retorikai lezárások, a műfaj pedig dokumentáció, ahol a kérdés a keresés belépője lehet.
- **nincs minta** [no-pattern] – `trend-nézet`: fölösleges kötőjel kéttagú összetételben, helyesen `trendnézet`. A katalógus eredet-alakú, a túlkötőjelezés hétköznapi helyesírási hiba, nincs rá minta.
- **nincs minta** [no-pattern] – `kód-módosítás nélkül`: ugyanaz a fölösleges kötőjel, helyesen `kódmódosítás`. Szintén minta nélkül.
- **HU-B01** [pattern-exception] – `A logok általában szét vannak szórva`: szándékosan megtartva. A `-va/-ve van` állapotjelölő szerkezet érinthetetlen, a cselekvő múltra cserélése jelentést változtatna.

## 4. Klaszterpontok

| # | Kezdet | Pont | Minták |
|---|---|---|---|
| 1 | `Az Ellenőr egy fejlesztői eszköz…` | 0 | nincs |
| 2 | `Egy közepes méretű csapatnál naponta…` | 0 | nincs |
| 3 | `Az Ellenőr egy könnyű ügynököt köt…` | 0 | nincs |
| 4 | `A felületen szűrhetünk repository…` | 0 | nincs |
| 5 | `Elsősorban azoknak a csapatoknak hasznos…` | 0 | nincs |
| 6 | `A telepítés egy CLI-paranccsal indul…` | 0 | nincs |
| 7 | `Az Ellenőr nem helyettesíti a CI-rendszert…` | 0 | nincs |

A front matter nem szerepel a táblázatban: strukturált metaadat, nem bekezdés.
