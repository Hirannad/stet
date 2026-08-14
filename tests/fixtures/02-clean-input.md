A keresés lassú lett, és három hétig nem tudtuk, miért. Végül kiderült: a gyorsítótár minden
kérésre újraépült, mert valaki kivett egy feltételt egy `if`-ből. Egy sor volt.

Hát, ennyi. Nem volt se architekturális hiba, se kapacitásprobléma – bár őszintén szólva azt hittem,
az lesz. (Majdnem meg is rendeltem két új node-ot.) A gyorsítótár azóta is gyorsítótár, ugyanaz a
kód, ugyanaz a kulcsképzés; csak a feltétel van a helyén.

Amit ebből megtanultunk, azt nehéz szabályba tenni. A mérés jó volt, a riasztás is jó volt, csak
senki nem nézte meg azt a commitot, mert egysoros volt. Most a review-ban az egysoros változás sem
megy át külön szem nélkül. Nem tudom, meddig tartjuk magunkat ehhez.
