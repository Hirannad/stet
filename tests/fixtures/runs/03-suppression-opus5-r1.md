<!-- stet-run: source=skills/stet-hungarian sha256=624d938a date=2026-09-26 -->

## 0. Nyelv és regiszter

A szöveg magyar. A szöveget `neutral` regiszterként kezelem: belső projektállapot-feljegyzés, a csatorna e-mail/dokumentáció; jogi terminus nincs benne – a szövegben szerepel egy szerződés, de a szöveg maga nem az. A személyes hang (`a szemem előtt van`, `amúgy`) a lazább kezelést is felvetné, de a csatorna nem dönti el egyértelműen, ezért a szigorúbb profilt választottam.

## 1. A javított szöveg

```
A migrációs terv le van zárva, a következő szakasz viszont még nyitott. Az elemzés kimutatja, hogy
a régi séma két helyen is ütközik az újjal, és a szerződés kimondja, hogy a leállás nem lehet
hosszabb négy óránál.

De ez nem jelenti azt, hogy nincs mozgásterünk. A csapat nem látott senkit a hétvégi ügyeletben,
aki a séma migrációját korábban végigvitte volna, ezért kértünk egy külső szakértőt. Ami ebből
következik: a séma migrációja két embertől függ, nem egytől.

A séma migrációja amúgy nem új téma. Tavaly is felmerült, de viszont akkor nem volt rá kapacitás.
A szemem előtt van a tavalyi ütemterv, és ma már látom, hol becsültünk alá.
```

## 2. Változástábla

nincs

## 3. Gyanús, de nem javítottam

- **HU-B01** [pattern-exception] – `le van zárva`. Állapotjelölő `-va/-ve van`, nem germanizmus; a `lezárták` eseményt állítana állapot helyett, tehát jelentést változtatna.
- **HU-B06** [pattern-exception] – `Az elemzés kimutatja`, `a szerződés kimondja` (egy mondat, egy tétel). Élettelen alany cselekvő igével; emberi cselekvő beírása hosszabb és hivataloskodóbb lenne.
- **HU-B03** [pattern-exception] – `De ez nem jelenti azt…`. A mondatkezdő kötőszó szabályos; hátravetett `azonban`-ra cserélve egyszerre lenne hivataloskodóbb és monotonabb.
- **HU-B05** [pattern-exception] – `nem látott senkit`. A magyar tagadószó-egyeztető nyelv, a `nem` itt kötelező.
- **HU-B02** [pattern-exception] – `Ami ebből következik`. Az `ami` egész tagmondatra utal vissza; `amely`-re cserélve hiperkorrekció lenne.
- **HU-L03** [pattern-exception] – `Ami ebből következik:` bejelentő keretnek látszik, de a minta `Jelek` sora zárt lista, és ez a fordulat nincs rajta. Nem általánosítom rá.
- **HU-L06** [pattern-exception] – `két embertől függ, nem egytől`. Egyetlen ilyen keret a bekezdésben, és a szembeállítás valódi (egy ember kontra kettő), tehát a szalmabáb-teszten nem bukik el. A klaszter-felülíráshoz kettő kellene.
- **nincs minta** [zone] – `A csapat nem látott senkit… ezért kértünk egy külső szakértőt. Ami ebből következik: … két embertől függ, nem egytől.` A következtetés nem jön ki az előzményből: a szöveg egy külső szakértőt nevez meg, a második ember kiléte sehol nem szerepel. Kitölteni csak új tény kitalálásával lehetne, amit a tartalmi invariáns tilt – ezt a szerzőnek kell pontosítania.
- **HU-B04** [pattern-exception] – `de viszont`. Szótározott összetett kötőszó; a szétbontás itt regisztert törne.
- **HU-B14** [pattern-exception] – `amúgy`. Diskurzusjelölő a helyén, pragmatikai funkcióval – pont ez adja a szöveg emberi hangját.
- **HU-B15** [pattern-exception] – `ma már`. Álpleonazmus, nyomatékot hordoz.
- **HU-B13, HU-M12** [pattern-exception] – `a séma migrációja` háromszor. A kulcsszót ismételni kell; a szinonimalánc maga a gépi jel.
- **nincs minta** [preserve] – `A szemem előtt van a tavalyi ütemterv, és ma már látom, hol becsültünk alá.` Konkrét részlet és feloldatlan önkritika – a `06-rhythm.md` megőrizendő jegyei közé tartozik. Nem a katalógus hallgatott: egy szabály mondja, hogy maradjon.

## 4. Klaszterpontok

| # | Kezdet | Pont | Minták |
|---|---|---|---|
| 1 | `A migrációs terv le van zárva…` | 0 | nincs |
| 2 | `De ez nem jelenti azt…` | 0 | nincs |
| 3 | `A séma migrációja amúgy…` | 0 | nincs |
