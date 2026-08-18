<!-- stet-run: source=skills/stet-hungarian sha256=22f8a1a7 date=2026-08-17 -->

## 0. Nyelv és regiszter

A szöveg magyar. A regisztert a hívó rögzítette, tehát nem következtettem rá: a szöveget `formal` regiszterként kezelem. Ez a profil a Pass 3-at klaszterhez köti, a Pass 5-öt a HU-R09, HU-R10, HU-R11 hármas kivételével leállítja, és a HU-L07-et kiveszi a Pass 4-ből.

## 1. A javított szöveg

```
# Lakcímigazolás online – új ügyfélszolgáltatás

## Kedves Polgáraink!

Örülünk, hogy bejelenthetjük az új, online lakcímigazolást kérő szolgáltatásunkat. Mostantól nem kell az ügyfélszolgálatunkon várakozni, hogy egy papír igazolást kapjon – mindent intézhet otthonról, saját időpontjában.

## Mi a lakcímigazolás?

A lakcímigazolás egy hivatalos dokumentum, amely igazolja, hogy Ön mely címen lakik. Szükség lehet rá például munkahelyemen, banknál vagy más hivatalos ügyletnél. Korábban ez csak úgy volt elérhető, hogy személyesen megjelent az önkormányzat ügyfélszolgálatán és kikérte a papírizásott változatot.

## Hogyan működik az online rendszer?

1. **Belépés**: Látogassa meg az önkormányzat weboldalát, és keresse meg az „Online ügyintézés” menüpontot. Beléphet személyes azonosítójával (ügyfélszám, közlekedési igazolvány száma vagy e-személyi).

2. **Kérelem kitöltése**: Töltse ki az egyszerű elektronikus űrlapot. Meg kell adnia a nevét, születési dátumát és a kért igazoláshoz kapcsolódó további információkat (például az aktuális lakcímét megerősíteni).

3. **Feldolgozás**: A kérelem azonnal bekerül a rendszerbe. A feldolgozás szokásosan 1–2 munkanapot vesz igénybe.

4. **Lezárulás**: Az igazolást PDF-formátumban kapja meg e-mailben. Ezt rögtön nyomtathatja vagy digitálisan használhatja számos helyen.

## Ki kaphat lakcímigazolást?

Bárki kérvényzhethet, aki az adott önkormányzatban bejelentett lakcímmel rendelkezik. Ha képviseletben szeretne eljárni (például gyermeke vagy gondnoka nevében), azt is meg lehet tenni – ekkor meghatalmazásra lesz szükség.

## Költségek

Az online lakcímigazolás díja megegyezik az irodai verzióval. A jelenlegi díj 500 forint. Az elektronikus fizetés a rendszeren belül történhet bankkártyával vagy e-bankon keresztül.

## Biztonság és adatvédelem

Komolyan vesszük az Ön személyes adatainak védelmét. Az online felület titkosított kapcsolaton működik, és csak az Ön hozzájárulásával kezeljük az adatokat. Az igazolások digitálisan aláírva kerülnek kiállításra, így azok jogilag egyenértékűek a hagyományos papírverzióval.

## Gyakori kérdések

**Van-e korlát a kérelmek számára?** Nem. Annyit igényelhet, ahányszor szüksége van.

**Mi van, ha a rendszer nem működik?** Ekkor az eredeti módon is kérvényzetheti az igazolást az ügyfélszolgálatunkon.

**Milyen fájlformátumban kapom meg az igazolást?** PDF-formátumban. Ezt lehet nyomtatni, e-mailben továbbküldeni vagy digitálisan menteni.

## Hogyan kezdheti el?

Az online ügyintézési felület a www.onkormanyzat.hu/online-ugyintezes címen érhető el, hetente 7 napig, napi 24 órában. Amennyiben technikai problémáz merülne fel, az ügyfélszolgálatunkat telefonon vagy e-mailben lehet keresni.

Várjuk a bejelentkezését, és reméljük, hogy ez az új szolgáltatás megkönnyíti az ügyintézést!

**Az Önkormányzat vezetése**
```

## 2. Változástábla

| ID | Eredeti | Új | Indok |
|---|---|---|---|
| HU-T07 | `Online – Új` | `online – új` | magyar címben csak az első szó és a tulajdonnév nagybetűs |
| HU-M01 | `kapjanak` | `kapjon` | megszólítási forma keveredése egy mondaton belül: T/3 önözés az E/3 `intézhet` mellett; a többségi forma nyer |
| HU-T11 | `banknál, vagy más` | `banknál vagy más` | magyarul nincs Oxford-vessző |
| HU-T01 | `„Online ügyintézés"` | `„Online ügyintézés”` | kevert idézőjelpár, a záró jel angol egyenes |
| HU-T11 | `száma, vagy e-személyi` | `száma vagy e-személyi` | magyarul nincs Oxford-vessző |
| HU-F11 | `elektronikus formot` | `elektronikus űrlapot` | a `form` az angol szó átvétele; a magyar élő kollokáció az `elektronikus űrlap` |
| HU-T11 | `dátumát, és a kért` | `dátumát és a kért` | magyarul nincs Oxford-vessző |
| HU-M02, HU-F06 | `az Ön nevét` | `a nevét` | a birtokos személyjel már jelöli a megszólítottat; a névmás fölösleges |
| HU-T03 | `1-2 munkanapot` | `1–2 munkanapot` | `-tól/-ig` viszonyban nagykötőjel áll |
| HU-T11 | `gyermeke, vagy gondnoka` | `gyermeke vagy gondnoka` | magyarul nincs Oxford-vessző |
| HU-T11 | `továbbküldeni, vagy digitálisan` | `továbbküldeni vagy digitálisan` | magyarul nincs Oxford-vessző |
| HU-M02, HU-F06 | `az Ön bejelentkezését` | `a bejelentkezését` | a birtokos személyjel már jelöli a megszólítottat |
| HU-G09 | `megkönnyítené` | `megkönnyíti` | a `remél` után az angol `would` tükreként áll a feltételes mód; az állítás tényszerű |

## 3. Gyanús, de nem javítottam

- **HU-F04** [threshold] – `A lakcímigazolás egy hivatalos dokumentum`: angolos határozatlan névelő névszói állítmány előtt, a szöveg legláthatóbb kalkja. A bekezdés `SOFT` pontösszege 2, a klaszterküszöb 3, tehát nem javítható.
- **HU-F04** [pattern-exception] – `hogy egy papír igazolást kapjon`: ugyanez az angolos `egy`, de itt a minta saját `Mikor NE`-je is fog, mert valódi határozatlanságot jelöl. Emiatt a pontja a nyitó bekezdés összegébe sem számít.
- **HU-F11** [threshold] – `saját időpontjában`: az `on your own schedule` tükre; magyarul az `időpont` foglalt ügyfélfogadási sávot sugall, vagyis a kalk félre is vezet. A bekezdésben ez az egyetlen élő `SOFT` jel, 2 pont, küszöb alatt.
- **HU-F11** [threshold] – `hetente 7 napig`: a `7 days a week` szó szerinti átvitele, magyarul `a hét minden napján`. Egyedüli `SOFT` jel a bekezdésben, 2 pont, küszöb alatt.
- **HU-F11** [paragraph-budget] – `szokásosan 1–2 munkanapot`: az `usually` tükre, magyarul `általában` vagy `rendszerint`. A felsorolás mint egy bekezdés két `SOFT` kerete elfogyott (HU-F11 az űrlapon, HU-M02 a névmáson).
- **HU-L01** [paragraph-budget] – `számos helyen`: üres mennyiségjelző, a forrásban nincs mögötte szám vagy felsorolás, tehát csak törölni lehetne. Ugyanaz a kerethiány, mint fent.
- **HU-L09** [threshold] – `bejelentett lakcímmel rendelkezik`: üres létige-körülírás, `bejelentett lakcíme van` volna. A bekezdés pontösszege 1, mert az `adott` nem számít bele: ott a szó valódi visszautaló funkciót lát el.
- **HU-F01** [threshold] – `Az elektronikus fizetés a rendszeren belül történhet`: nominalizáció üres igével, `elektronikusan, a rendszeren belül fizethet` volna. Ez az egyedüli élő `SOFT` jel a bekezdésben, 2 pont, a küszöb 3.
- **HU-H03** [register] – ugyanez a mondat a `történik`-minta felől: `FIX-IF: informal, neutral`, és a rögzített profil nincs a listáján. Külön tétel, mert más mechanizmuson akadt el, mint a HU-F01.
- **HU-M02** [threshold] – `az Ön személyes adatainak védelmét` és `csak az Ön hozzájárulásával` egy bekezdésben: ez a szöveg egyetlen valódi `Ön`-halmozása. A bekezdés pontösszege 2, küszöb alatt; a második előfordulás a `csak` miatt amúgy is szembeállító, ott a névmás maradna.
- **HU-H02** [register] – `kerülnek kiállításra`: a szenvedőpótló `-ásra kerül`. A minta `FIX-IF: informal, neutral`, a rögzített profil nem szerepel rajta, ezért nem tüzel. Hatósági szövegben a cselekvő elhallgatása ráadásul szándékos lehet.
- **HU-M09** [pattern-exception] – a `Mi a lakcímigazolás?`, `Hogyan működik az online rendszer?`, `Ki kaphat lakcímigazolást?` és `Hogyan kezdheti el?` kérdés-alcímsorok sorozata. A minta `Mikor NE`-je kilövi: ügyféltájékoztatóról van szó, külön GYIK-szakasszal, ott a kérdés keresési belépő, tehát funkció.
- **HU-M12** [uncertain] – `irodai verzió`, `papírverzió` és `papírizásott változat` ugyanarra a dologra. Nem egységesítettem, mert nem biztos, hogy ugyanazt jelentik: az `irodai verzió` az ügymenet, a `papírverzió` a dokumentum. Az összevonás tartalmi döntés, a szerzőé.
- **HU-B22** [zone] – `Az Önkormányzat vezetése` aláírás, miközben a törzsszöveg kétszer kisbetűzi ugyanazt a szót. A HU-B22 a tiszteletből nagybetűzött köznevet javítandónak mondja, de itt a szó lehet az intézmény saját megnevezése is, az pedig érinthetetlen zóna.
- **nincs minta** [no-pattern] – `munkahelyemen`: E/1 birtokos személyjel a toldalék nélküli `banknál`, `ügyletnél` sorában, `munkahelyen` volna. Ragozási hiba, nincs rá katalógusminta.
- **nincs minta** [no-pattern] – `(például az aktuális lakcímét megerősíteni)`: a főnévi igenév nem illeszkedik a `további információkat` tárgyhoz, `az aktuális lakcíme megerősítését` volna. Az angol gerundium magyar főnévi igenévre váltása, de a katalógus csak a `-va/-ve` alakot fedi le.
- **nincs minta** [no-pattern] – `Annyit igényelhet, ahányszor szüksége van.`: az `annyit … ahányszor` utalószópár nem illeszkedik egymáshoz, és a `szüksége van` vonzatából hiányzik a `rá`.
- **nincs minta** [no-pattern] – `papírizásott`, `kérvényzhethet`, `kérvényzetheti`, `problémáz`: elrontott szóalakok. A katalógus eredet-alakú, a hétköznapi helyesírási és szóalaki hiba szándékosan kívül esik rajta; ez helyesírás-ellenőrző dolga.

## 4. Klaszterpontok

| # | Kezdet | Pont | Minták |
|---|---|---|---|
| 1 | `Örülünk, hogy bejelenthetjük…` | 2 | HU-F11 |
| 2 | `A lakcímigazolás egy hivatalos dokumentum…` | 2 | HU-F04 |
| 3 | `1. **Belépés**…` (a teljes négypontos felsorolás) | 8 | HU-F11, HU-M02, HU-F06, HU-L01 |
| 4 | `Bárki kérvényzhethet…` | 1 | HU-L09 |
| 5 | `Az online lakcímigazolás díja…` | 2 | HU-F01 |
| 6 | `Komolyan vesszük az Ön személyes adatainak…` | 2 | HU-M02 |
| 7 | `**Van-e korlát a kérelmek számára?**…` | 0 | nincs |
| 8 | `**Mi van, ha a rendszer nem működik?**…` | 0 | nincs |
| 9 | `**Milyen fájlformátumban kapom meg…**` | 0 | nincs |
| 10 | `Az online ügyintézési felület…` | 2 | HU-F11 |
| 11 | `Várjuk a bejelentkezését…` | 6 | HU-M02, HU-F06, HU-G09 |
| 12 | `**Az Önkormányzat vezetése**` | 0 | nincs |
