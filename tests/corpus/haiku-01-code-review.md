# Code Review – Miért és hogyan?

A code review olyan, mint egy szellemi biztosíték. Nem azért csinálunk, mert nem bízunk a fejlesztőkben, hanem mert tudjuk: mindenki lát meg valamit, amit mások nem, és minden pár szem jobban lát, mint egy.

## Miért szükséges?

A leggyakoribb hiba az önbizalom. Akármilyen tapasztalt vagy, amikor saját kódodon dolgozol, apró buktatók maradhatnak rejtett. Egy fáradt szem másképp olvas végig egy függvényt, mint a fő szerző szempontja. Az első review megtalálja azokat az edge caseeket, amelyeket az eredeti fejlesztő gondolkodásmódjában nem voltak köztudatban.

A biztonság mellett van még néhány szuper gyakorlati előny. A code review során a junior fejlesztők megtanulnak a senior kód logikájából és stílusából – nem kell külön oktatás, a valós munka során tanulnak. Az újabb csapattag könnyebben beépül, ha látja az általános elveket. A projekt kódja konzisztenssé válik, mert közösen fenntartják az irányelveket.

## Hogyan csináljuk?

Egy review nem lehetőség a kritika rögzítésére. Az a gondolat hibás. A review konstruktív beszélgetés: „Miért ezt a megközelítést választottad? Van-e rá okod, amit nem értek?"

Az elküldő (a patch szerzője) készüljön fel: írjon rövid leírást, amiben elmondja, mit csinál a módosítás és miért. Minél világosabb, annál gyorsabb a review.

A reviewer olvaszon végig konzentrieren, egyszer vagy kétszer. Ne írjon a kódba beletörődve. Összegyűjtse a megjegyzéseit, majd írja meg összefüggő formában. Vagy – ha szóban jobb – beszéljen meg DirectMessage-ben vagy szervezzen 15 perces call-t.

Egy jó megjegyzés konkrét, nem pedig vag. Ne azt mondd, hogy „Ez nem szép." Inkább: „Ez az if-lánc 5 elágazás mélyen jár, nehéz követni. Felraknánk egy guard clauseb?"

## A tárgy

Egy review célja nem a tökéletes kód. A cél a működő, érthető, fenntartható kód, és hogy a csapat közös nyelvén beszéljen. Ha egy megoldás helyes és biztonságos, de nem pont az, ahogy te csinálnád, nem vagyis blokkolni kell.

Ne ragozz kis stílusproblémákon. Ha az eszközöd automatikusan formázza a kódot (prettier, black, stb.), hagyd erre azt – az embereknek nem erről kell vitázni.

## Végül

A code review nem zárógát, nem börtön-orvos, nem a verseny. A csapat közös tulajdona minden sor. Minél gyorsabban és kedvesebbek vagyunk egymással a reviewban, annál jobban működik a folyamat. Egy fejlesztő, akinek sérült a ége a kritikáktól, lehet, hogy fél később biztonságosan felvetni a kérdéseket.

Szóval kezdjünk el. Ha eddig nem csináltatok reviewt, állítsatok be egy alapszintű folyamatot, és belépjetek. Egy hét múlva már érzitek az előnyöket.
