# Code review: miért, és hogyan

Az elmúlt hónapokban kétféle review-t láttam nálunk. Az egyikben a PR három napig áll, aztán valaki átfutja és megnyomja az approve-ot. A másikban negyven komment megy egy változónévről, a szerző pedig este tizenegykor még mindig javít. Egyik sem működik, és mindkettőnek ugyanaz az oka: nincs kimondva, mire való a review.

Kezdjük a haszonnal. A hibakeresés csak a második helyen áll. A leghasznosabb dolog, amit a review ad, az a tudás szétterítése. Ha egy funkciót egyetlen ember írt meg és egyetlen ember érti, akkor az a funkció a szabadságáig működik. A review az egyetlen rendszeres alkalom, amikor valaki más is végigolvassa a kódot még azelőtt, hogy egy hajnali riasztás kényszerítené rá.

A második haszon a döntések nyoma. A PR alatti beszélgetés megmarad, és félév múlva a „miért pont így oldottuk meg?" kérdésre nem találgatás lesz a válasz. A hibák megtalálása is benne van a pakliban, de legyünk őszinték: a súlyos hibákat inkább a tesztek és a staging fogják ki. A review máshol erős — a szándék szintjén. Rossz absztrakció, félreértett követelmény, olyan eset, amire senki nem gondolt.

Innen jön a hogyan.

**A leírást olvasd először.** Ha a PR nem mondja meg, mit akar és miért, azt kérd, ne a kódot kommenteld. Három sor „mit és miért" több időt spórol, mint bármelyik review-checklist.

**Nagy PR-t ne fogadj el.** Ötszáz sor fölött elfogy az emberi figyelem, és onnantól már csak formázást veszünk észre. Ha mégis nagy jött, kérd szét. Ez nem sértés, hanem a review működésének feltétele.

**Válaszd külön a blokkolót a véleménytől.** Mostantól: „blokkoló:" előtag, ha nélküle nem mehet ki, „ötlet:", ha csak felvetés. A szerző így tudja, mire kell reagálnia, és mire nem.

**Kérdezz, ne rendelkezz.** A „miért itt kezeljük a hibát?" gyakran kiderít valamit, amit a „tedd lejjebb" elfedett volna. Néha a szerzőnek van igaza, és ez így van rendben.

**Huszonnégy órán belül nézz rá.** Nem azért, mert a határidő szent, hanem mert egy álló PR mögött egy álló ember van, aki közben belekezd egy másik szálba, és a kettő össze fog ütni.

**Apróságokat ne kézzel kommentelj.** Ha formázáson vagy importsorrenden múlik, az a linter dolga. Aki ilyet ír bele, az a review idejét használja el olyanra, amit egy szkript ingyen megcsinál.

Egy dolgot még tegyünk hozzá, mert ezen szokott elcsúszni a hangulat: a review a kódról szól, nem a szerzőről. „Ez a függvény két dolgot csinál" és „te összekevered a felelősségeket" ugyanarra a problémára mutat, csak az egyikre lehet válaszolni.

Végül: az approve nem szívesség, és nem is vérrel írt aláírás. Azt jelenti, hogy elolvastam, értem, és vállalom, hogy holnap akár én is javíthatom.
