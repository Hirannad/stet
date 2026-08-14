---
title: Miért és hogyan tartsunk code review-t
type: guide
status: active
updated: 2026-08-14
---

Szia csapat,

az elmúlt hetekben többször felmerült, hogy a code review sokaknak inkább formalitásnak tűnik, mint valódi értéknek. Szeretném összefoglalni, miért ragaszkodunk hozzá, és hogyan érdemes csinálni, hogy tényleg megérje az időt, amit rááldozunk.

A code review nem a hibavadászatról szól elsősorban. Persze kiszűr néhány bugot commit előtt, de a valódi haszna máshol van. Egyrészt szétteríti a tudást a kódbázisról – ha csak egy ember érti, hogyan működik egy modul, az kockázat, nem érdem. Másrészt konzisztenciát épít: ha mindenki más stílusban ír kódot, a karbantartás lassan pokollá válik. Harmadrészt tanulási alkalom mindkét irányban – a reviewer is tanul az író megoldásából, az író is a reviewer visszajelzéséből.

Néhány alapelv, amit érdemes betartani.

Kis PR-okat nyissunk. Egy 800 soros diffet senki nem néz át rendesen, csak átfut rajta, és rábólint. Ha egy feature túl nagy, bontsuk logikai lépésekre, és külön PR-ban vigyük be őket. Ökölszabályként 200-300 sor fölött már gyanakodjunk.

A PR leírása legyen érdemi. Mit csinál a változás, miért van rá szükség, mit érdemes külön megnézni. Ha a reviewernek magától kell kitalálnia a kontextust, kétszer annyi ideig tart a review, és rosszabb minőségű lesz.

Reviewerként ne csak a szintaxist nézzük. Kérdezzük meg magunktól: érthető ez valakinek, aki fél év múlva nyúl hozzá? Van-e egyszerűbb megoldás? Lefedi-e a teszt a határeseteket? A formázást és az apró stílusbeli kérdéseket hagyjuk a lintre – ne vesszünk el bennük, amikor van fontosabb is.

Kommentben legyünk konkrétak és kedvesek. „Ez nem jó” helyett írjuk le, miért nem jó, és ha lehet, javasoljunk alternatívát. Különbséget érdemes tenni a blokkoló észrevétel és a puszta javaslat között – jelöljük is, hogy melyik melyik, hogy az író tudja, mi a kötelező és mi a nice-to-have.

Íróként ne vegyük személyeskedésnek a visszajelzést. A review a kódról szól, nem rólunk. Ha nem értünk egyet egy észrevétellel, mondjuk el nyugodtan, miért – a vita gyakran jobb megoldáshoz vezet, mint bármelyik eredeti javaslat.

Válaszidőre is figyeljünk. Egy nyitva hagyott PR blokkolja a szerzőt, és lassítja az egész csapatot. Törekedjünk arra, hogy egy napon belül reagáljunk minden nyitott review-ra, még ha csak annyi is a válasz, hogy „később átnézem részletesen”.

Ez nem bürokrácia akar lenni, hanem védőháló. A cél, hogy a kódbázis olyan állapotban maradjon, amiben szívesen dolgozunk hónapok múlva is.

Ha valakinek van javaslata a folyamat finomítására, dobjátok be nyugodtan – ez a leírás sem végleges.
