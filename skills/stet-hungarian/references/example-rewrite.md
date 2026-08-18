# Mintafutás – a kimenet formátuma

**Ez formátumpélda, nem illesztési minta.** Az itteni mondatokat ne keresd a saját szövegedben, és
ne ezekhez hasonlítsd a bemenetet: a jeleket mindig a `01`–`06` referenciafájlokból azonosítsd.
Ez a fájl egyetlen dolgot tanít meg – **hogyan néz ki a háromrészes kimenet**, és milyen
részletességű a változástábla meg a gyanús-lista.

**A szakaszcímek és a táblázatoszlopok kötelező alakja a `SKILL.md` `## Kimenet` szakaszában áll.**
Ez a futás azt az alakot követi; ha a kettő eltér, a `SKILL.md` nyer, és ez a fájl a hibás.

Az alábbi futás `neutral` regiszterben készült. A bemenet **szándékosan elhelyezett jelekből**
épül – a változástábla minta-ID-i megszámolhatók, tehát a futás ellenőrizhető, nem hivatkozási
alap. Valós szövegen mért teljesítményről ez a fájl nem állít semmit.

---

## Bemenet

```
# Az Új Adatvédelmi Szabályzat Bevezetése És A Kapcsolódó Folyamatok

A mai rohanó világban az adatvédelem kulcsfontosságú és elengedhetetlen minden szervezet számára.
Fontos megjegyezni, hogy a szabályozás nem csupán egy jogi kötelezettség, hanem egy teljesen új
szemléletmód is.

Íme a három legfontosabb előny: gyorsabb folyamatok, egyszerűbb adminisztráció és
költséghatékonyabb működés. Ez a megoldás lehetővé teszi számunkra, hogy csökkentsük a
kockázatokat, ugyanakkor kihívást is jelent. Emellett a csapat képzése is szükséges. Továbbá, a
dokumentáció frissítése is feladat.

A projekt menedzsment és az adat vezérelt döntés hozás javította a folyamatot – legalábbis papíron.
A bevétel 1,250,000 forint volt 2026 Augusztus 2-án, a növekedés 3.5%. A kimenetet HTML-el
állítjuk elő, és a jelentés Hétfőn készül el.

A szabályzat a következő ülésen elfogadásra kerül. Ha Ön elfelejtette az Ön jelszavát, Ön a
beállításokban módosíthatja azt. Töltsd le az alkalmazást, majd jelentkezzen be a fiókjába.

A jelentés szerint "jelentős javulás" történt, tükrözve a csapat elkötelezettségét. Összefoglalva
elmondható, hogy a jövő fényes. Remélem, segítettem!
```

---

## 0. Nyelv és regiszter

A szöveg magyar. A szöveget `neutral` regiszterként kezelem. (Belső dokumentáció, nincs jogi
terminus, a megszólítás következetlen – a többségi forma az önözés.)

## 1. A javított szöveg

```
# Az új adatvédelmi szabályzat bevezetése és a kapcsolódó folyamatok

Az adatvédelem minden szervezet számára fontos. A szabályozás nem csupán egy jogi
kötelezettség, hanem egy teljesen új szemléletmód is.

A három legfontosabb előny: gyorsabb folyamatok, egyszerűbb adminisztráció és
költséghatékonyabb működés. Ezzel a megoldással csökkenthetjük a kockázatokat, ugyanakkor
kihívást is jelent. A csapat képzése és a dokumentáció frissítése is feladat.

A projektmenedzsment és az adatvezérelt döntéshozás javította a folyamatot – legalábbis
papíron. A bevétel 1 250 000 forint volt 2026. augusztus 2-án, a növekedés 3,5%. A kimenetet
HTML-lel állítjuk elő, és a jelentés hétfőn készül el.

A szabályzatot a következő ülésen elfogadják. Ha elfelejtette a jelszavát, a beállításokban
módosíthatja. Töltse le az alkalmazást, majd jelentkezzen be a fiókjába.

A jelentés szerint „jelentős javulás” történt, ami a csapat elkötelezettségét mutatja.
```

## 2. Változástábla

| ID | Eredeti | Új | Indok |
|---|---|---|---|
| HU-T07 | `Az Új Adatvédelmi Szabályzat Bevezetése És A…` | `Az új adatvédelmi szabályzat bevezetése és a…` | magyar címben csak az első szó nagybetűs |
| HU-L04 | `A mai rohanó világban` | *(törölve)* | klisés keretezés, nem közöl semmit |
| HU-L01 | `kulcsfontosságú és elengedhetetlen` | `fontos` | halmozott üres fokozó; a törlés állítmány nélkül hagyná a mondatot, ezért kompromisszum |
| HU-L03 | `Fontos megjegyezni, hogy` | *(törölve)* | metaszöveges keret |
| HU-L12 | `Íme a három…` | `A három…` | csevegőmaradvány |
| HU-F03 | `Ez a megoldás lehetővé teszi számunkra, hogy csökkentsük` | `Ezzel a megoldással csökkenthetjük` | `allows us to` tükörfordítás → eszközhatározó |
| HU-R04, HU-T15 | `Emellett… Továbbá, …` | egy mondattá vonva | kapcsolóelem-túltengés; mondatkezdő elem után nincs vessző |
| HU-T14 | `projekt menedzsment`, `adat vezérelt`, `döntés hozás` | `projektmenedzsment`, `adatvezérelt`, `döntéshozás` | angol mintájú különírás |
| HU-T02 | `—` | ` – ` | em dash helyett szóközös gondolatjel |
| HU-T04 | `1,250,000`, `3.5%` | `1 250 000`, `3,5%` | angol számformátum |
| HU-T06, HU-T08 | `2026 Augusztus 2-án` | `2026. augusztus 2-án` | dátumforma; hónapnév kisbetűs |
| HU-T13 | `HTML-el` | `HTML-lel` | `-val/-vel` hasonulása kötőjel után |
| HU-T08 | `Hétfőn` | `hétfőn` | napnév kisbetűs |
| HU-H02 | `elfogadásra kerül` | `elfogadják` | `-ásra kerül`; `neutral` kapu nyitva, HU-H09 rendben |
| HU-M02, HU-F06 | `Ha Ön elfelejtette az Ön jelszavát, Ön…` | `Ha elfelejtette a jelszavát, …` | `Ön`-halmozás; a személyrag jelöli a megszólítottat |
| HU-M01 | `Töltsd le` | `Töltse le` | tegezés-önözés keveredés, a többségi forma nyer |
| HU-T01 | `"jelentős javulás"` | `„jelentős javulás”` | angol idézőjel |
| HU-L10 | `…történt, tükrözve a csapat elkötelezettségét.` | `…történt, ami a csapat elkötelezettségét mutatja.` | mondatvégi határozói igenév |
| HU-L03, HU-L13 | `Összefoglalva elmondható, hogy a jövő fényes.` | *(törölve)* | metaszöveg-keret + tartalmatlan pozitív zárlat |
| HU-L12 | `Remélem, segítettem!` | *(törölve)* | csevegőmaradvány |

## 3. Gyanús, de nem javítottam

- **HU-L06** – `nem csupán egy jogi kötelezettség, hanem egy teljesen új szemléletmód is`. A
  bekezdés 2 `SOFT` javítási kerete elfogyott (HU-L04, HU-L01). A szerkezet magyarul egyébként helyes.
- **HU-F04** – `egy jogi kötelezettség`, `egy teljesen új szemléletmód`: angolos `egy`. Ugyanaz a
  kerethiány.
- **HU-R03** – a hármas felsorolás. **Szabály szerint nem javítható:** a három tag nem párhuzamos
  `-ás/-és` főnév, és a hármasság nem tér vissza bekezdésenként.
- **HU-L08** – `kihívást is jelent`, üres igei körülírás. Kerethiány.
- **HU-F01** – `a csapat képzése` / `a dokumentáció frissítése`: nominalizáció maradt az összevont
  mondatban, de a minta jele nem teljesül – mindkettő egy lépcső, és a birtokos nem deverbális,
  tehát nem rétegzett lánc. A keret amúgy is elfogyott volna a HU-R04 után.
- **HU-G20** – egy `ugyanakkor`. `[jelöld]`, nem ismétlődik.
- **nincs minta** – `legalábbis papíron`, **szándékosan megtartva.** Feloldatlan feszültség, emberi
  jel (`06-rhythm.md`, megőrizendő jegyek).

---

## Amit a példa mutat

**A változástábla minden sora minta-ID-ra hivatkozik.** ID nélküli változtatást a Pass 6 diff-audit
visszavonat – ha nem tudod megnevezni, melyik minta alapján nyúltál hozzá, ne nyúlj hozzá.

**A gyanús-lista nem formalitás.** Ebben a futásban hét tétel került rá, és mind indoklással: hol
a klaszterküszöb, hol a bekezdésenkénti keret, hol pedig maga a szabály tiltotta a javítást
(HU-R03). Ez az a szelep, ahol a bizonytalanság kiírható ahelyett, hogy javításba menekülne.

**A `FIX` és a `SOFT` másképp viselkedik.** A tipográfia (HU-T*) végigfut, kerettől függetlenül –
ezért látszik itt sok javítás. A stilisztikai (`HU-L*`, `HU-R*`) minták viszont bekezdésenként
legfeljebb kettőt engednek, és ezért maradt a lista alján **három** kerethiány miatt el nem végzett
javítás (HU-L06, HU-F04, HU-L08). A hét tétel közül a többi máshogy állt le: a HU-R03-at és a
HU-F01-et a saját szabálya, a HU-G20-at a `[jelöld]` címke, a `legalábbis papíron`-t pedig
szándékos döntés.

**És ez a futás a szövegszintű plafonon áll – nem alatta.** A bemenet 15 mondat; `SOFT` javítás
hét mondatot érint, ha a HU-R04 összevonását két érintett mondatnak számoljuk, és hatot, ha egynek.
A `SKILL.md` szerint a törölt mondat érintett, és az összevonás két mondatot érint – tehát hét. Az
egyik olvasat átvitte volna a szövegszintű keretet, a másik pontosan ráállt, ráhagyás nélkül. A
konkrét értékek a `SKILL.md`-ben állnak, itt szándékosan nem ismételjük meg őket.

Ez a fájl ezt nem rejti el, mert ez a példa legtanulságosabb része: a bekezdésenkénti keret és a
szövegszintű plafon **normál magyar prózán ütközik**, nem szélső esetben – a magyar prózabekezdés
jellemzően 3–4 mondat, és ennél a keret hamarabb fogy el, mint hinnéd. A feloldás a `SKILL.md`-ben
áll: a plafon **megelőző**, nem utólagos, és az összevonás számolása ki van mondva. Ez a futás a
szabály tisztázása **előtt** készült, és szándékosan úgy maradt, hogy látszódjon, mit tisztáz.
