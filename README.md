# Alkalmazásfejlesztés (VIAUMA09) házi feladat

Csapattagok (név, neptun kód): aaa (abc123), bbb (def123), ccc (ghi123)
Leadáshoz videó URL:

Leadáshoz checklist:
- 24 órával a személyes (vagy online) leadási időpont előtt 24 órával
  - Videó elkészítve, benne explicit kitérve minden pontozási szempontra (lásd pontozási szempontok videó elvárásai).
  - A pontozási listában be-X-elve minden pontozási szempont, amivel foglalkoztatok.
  - Github pull request létrehozva, előadó hozzárendelve reviewerként.
  - Amennyiben online időpont foglalásos bemutatás van, az időpontot le van foglalva a csapat számára.

# A házi feladat kiírása

A házi feladat célja egy diagnosztikai kliens program elkészítése egy szimulált vagy valós robothoz vagy más beágyazott rendszerhez. A kliens program grafikus felhasználói felület segítségével lehetővé teszi a robot vezérlését, valamint a tőle érkező adatok áttekinthető, hibakeresésre tényleg alkalmas megjelenítését. Szimulált robot esetén a bemutathatóság érdekében a szimulátor biztosítása (megírása, beszerzése) is a feladat része, melyre az előadáson fogunk látni példát.

## Jelentkezés módja

- A házi feladat elkészítése 3 fős csapatokban történik. Jelentkezni a 3. oktatási hét végéig kell az alábbi módon:
  - Moodle alatt az erre vonatkozó kérdőíven mindenkinek meg kell adni, hogy melyik csapatban van (mi a csapatneve).
  - A classroom.github.com rendszerben létre kell hozni a csapatot és a tagoknak be kell lépnie. Így mindenki megkapja a házi feladat elkészítésére szánt (private) repositoryt. Ehhez a meghívó URL a Moodle alatt érhető majd el.

- A 2 fős csapat is elfogadható, de a feladat mennyisége miatt 3 fő az ideális. A csapaton belüli esetleges súrlódások kezelése a csapat feladata, csak úgy, mint egy éles projektben. Az aláírás feltétele a csapatmunkában való aktív részvétel.
- Nem RobonAUT-hoz kapcsolódó házi feladatok esetében erősen javasolt, hogy beszéljetek az előadóval, nehogy véletlenül olyan megoldásba kezdjetek, amivel a szükséges pontokat nem tudjátok megszerezni.

(Sajnos élő példa miatt ha valaki a github classroomban olyan, nem szalonképes vagy offenzív csapatnevet választ, ami miatt például a github automatikusan blokkolja a tárgy organizationjét és így az összes repositoryját, az fegyelmi eljárást von maga után. De amúgy se igen akarjátok, hogy később a Google a nevetekre keresve ilyen csapatnév mellett mutasson titeket… pl. egy leendő munkáltatónak.)

## A leadás módja

A házi feladatot leadni a 14. oktatási héten kell, 2 lépésben.
- A személyes (vagy online) leadási időpont előtt 24 órával le kell adni
  - Egy max. 5 perces screen capture (vagy más módon elkészített) videót a megoldásról. (Ennek célja, hogy a leadáskor ne kelljen minden funkciót végignézni, hanem koncentrálhassunk az érdekesekre. Ezen kívül hogy ne kelljen azon aggódni, hogy például a robot éppen menni fog-e, ne kelljen hozzá feltétlenül speciális tesztpálya.) A pontozási szempontok mindegyikének explicit szerepelnie kell a videóban, a pontozási szempontnál megadott formában. A videó URL-jét ennek a fájlnak az elején kell megadni és egy böngészőben további telepítések nélkül lejátszhatónak kell lennie (pl. youtube vagy google drive megosztás).
  - Be kell adni egy github.com pull requestet, benne reviewerként megjelölve a tárgyfelelőst.
  - A megoldásnak a repository master ágán kell lennie.
  - A leadott verzióban ebben a README.md fájlban minden olyan pontozási szempontot be kell X-elni, amire szeretnétek pontot kapni.
- A leadási időpontban személyes vagy online leadást fogunk szervezni (járványügyi szempontok függvényében), amikor megnézzük a megoldás érdekesebb részleteit és egyeztetjük a kapott pontszámot. A RobonAUT robothoz kapcsolódó megoldások kedvéért ezen az alkalmon rendelkezésre áll majd egy tesztpálya, melyen egyúttal a robotokat is lehet tesztelni, miközben megnézzük a kliens programok működését. (A leadáshoz egy saját notebookot kell hozni. Ha ez akadályba ütközik, előre jelezzétek és megoldjuk egy gépteremben.)

Azoknak a csapatoknak, melyeknek a fenti leadásokat nem sikerül határidőre teljesíteni, a pótlási héten lesz lehetőség pótleadásra, ugyanígy 2 lépésben. (A fenti 1. lépés késedelmes teljesítése esetén már csak a pótleadáson lehet leadni a házi feladatot, mivel a találkozó előtt át kell tudunk nézni az előre leadott anyagokat.)

A konkrét 14. és pótlási heti időpontokat novemberben hirdetjük ki.
A félév vége és a RobonAUT verseny után (bőven hagyva időt) a kiadott repositorykat törölni fogjuk, így a verseny után érdemes egy véglegesebb repositoryt létrehozni és oda is pusholni.

## Köztes code reviewk

A félév során lesz két határidő, amikor az addig elkészült részekre lehet code reviewt kérni. Ehhez github alatt pull requestet kell készíteni és reviewernek meg kell adni a tárgyfelelőst (usernév: csorbakristof).

A code review célja a minél hasznosabb, személyes visszajelzés a csapatok számára, a saját megoldásukkal kapcsolatban. Nem kötelező, de pontozási szempont ez is.

Annak érdekében, hogy az adható visszajelzés minél hasznosabb legyen, javasoljuk, hogy a megoldásról ilyenkor is készítsetek egy rövid videót (benne a működésről, a forráskód felépítéséről, esetleges kérdéseitekről), hogy minél jobban átlássuk a megoldásotok működését. A videóra az URL-t a pull request szövegébe érdemes beleírni, mint ahogy oda való minden megjegyzés és esetleges kérdések is.

(Érdemes megemlíteni, hogy minden pull request két git branch különbségét tartalmazza. A legegyszerűbb, ha létrehoztok egy branchet a félév eleji állapotra és ehhez hasonlítjátok a beadandó állapotot.)

## Minimális követelmények (aláírás feltétele)

- Minden csapattag aktív részvétele a munkában, ami a git commit historyban is látszik (kivéve, ha páros programoztok és ezért a közös commitok egyikőtök nevében készülnek).
- A forráskód legyen áttekinthető, olvasható, esztétikus. (pl. ne legyen benne hatalmas, kikommentezett forráskód blokk, csomó üres sor egymás után, “teve” és “maci” (vagy szalonképtelen) nevű változó, ne egy óriás cpp fájlban legyen megírva az egész stb.)

## Normál pontot érő dolgok

(Minden szempontnál a megadott pont a maximális adható pont, részleges megoldás kevesebb pontot is érhet.)





- [ ] DocFX segítségével, XML kommentárokkal generált dokumentáció legalább 3 áttekintő UML diagrammal. A dokumentáció fejlesztői dokumentáció. Olyan mértékben kell, hogy tartalmazza a rendszer működését, hogy abból kiderüljön, hogy egy adott funkció hogy működik és hol található a forráskódban. A repository értelemszerűen tartalmazza a dokumentáció minden forrását is. A DocFX által generált HTML dokumentáció ZIP-elve a github.com release funkciójával letölthető formában kell, hogy elérhető legyen a leadási pull request létrehozásakor. https://github.com/blog/1547-release-your-software 
- [ ] 3p: Határidőre leadott pull request az 1. code reviewra, szignifikáns mennyiségű fejlesztéssel.
- [ ] 2p: Határidőre leadott pull request a 2. code reviewra, szignifikáns mennyiségű fejlesztéssel.

## Bónusz pontot érő dolgok
Ezek a szempontok csak akkor érnek pontot, ha (1) a normál pontokból legalább 40 pont összegyűlt és (2) bónusz pontot csak a normál leadási időpontban lehet szerezni, a pótleadáson már nem.


## Mínusz pontok

Van pár alapelvárás, ami pontot nem ér, de ha valaki nem tartja be, az ütközik a tantárgy munkafolyamataival és ezért mínusz pontot ér. Kérünk mindenkit, hogy figyeljen a formai kérésekre is és ezekre a retorziókra ne legyen szükség... sajnos ezt korábbi számos rossz tapasztalat miatt kellett bevezetni.

- Videó hossza több, mint 5 perc.
- Generált fájlok (fordítási eredmények, exe, generált dokumentáció) a git repositoryban
- A beadott verzió nem a master ágon van.
- Ronda forráskód: forráskódban kikommetezett kódrészletek, TODO kommentárok, szalonképtelen változónevek, több üres sor egymás után.
- A git pull request nem pont a leadandó megoldást tartalmazza. Például a pull request nem az aktuális és félév eleji állapot különbségét mutatja, hanem egy későbbi állapotból indul ki, így sok munka nem szerepel benne.

## Jegymegajánlás

Elvileg a házi feladat 50 pontot ér, de főleg a bónusz feladatokkal együtt ennel több pont is gyűjthető, ami ugyanúgy hozzáadódik a féléves pontszámhoz. Amennyiben egy csapat sok többlet pontot szerez (és időben adja le a házi feladatot és nem a pótladáson), amennyiben eléri a 70 pontot, a házi feladatra megajánlott 5-ös adható.

# ----------------------------------- korábbi
(Megajánlás 70 ponttól!)




Házi feladat pontozási szempontok
Alap esetben a minimális és alap feladatokat kell teljesíteni és azok alapján történik a pontozás. Amennyiben valaki időben (nem késedelmesen) leadja a házi feladatot, akkor kaphat plusz pontokat a bónusz kategóriából, de csak akkor, ha az alap feladatokból (max. 40p) legalább 30 pontot elért. 

Minimális feladatok (e nélkül a házi feladat értékelhetetlen és nem ér pontot, valamint az aláírásnak is előfeltétele):
A kliens programnak C++-ban, Qt és QML-ben kell készülnie, GIT verziókövetéssel a tárgy keretében létrehozott classroom.github.com-os repositoryban. Bár a qmake és gcc toolchainnel foglalkozunk az előadáson és így erre van támogatás, a Visual Studio alapú toolchain is elfogadható.
Grafikus felülettel kell rendelkeznie, ami parancsokat tud küldeni és állapotot tud fogadni a robottól vagy egy szimulátortól.
A szimulátorral TCP socketen, soros porton vagy bluetoothon keresztül kell kommunikálnia.
Egy parancs kiadására (pl. start) a visszakapott adatokból egyértelműen látszania kell, hogy a robot (igazi vagy szimulált) tényleg elindult. (Például a motoráram megnő, változik a pozíció stb.)
A leadáskor a master branchen lévő verzió forduljon és fusson egy Windows 10 vagy Ubuntu virtuális gépen. Természetesen ha egy igazi robot jelenléte kell neki, akkor nem gond, ha nem működik minden funkció, de induljon el és ezt a tényt esztétikus formában jelezze. A helyes működés pedig a demó videón úgyis látszani fog.

Alap feladatok (max.40 pont):
Az aktuális állapot szövegesen és a vektor érték(ek) esetében grafikusan is jelenjen meg.
A korábbi állapotok szövegesen és grafikusan jelenjenek meg (redundancia nem kell, minden úgy jelenjen meg, ahogy logikusabb, csak legyen szöveges és grafikus is).
Az alkalmazás felhasználói felülete ne hasonlítson kísértetiesen a SimpleTelemetryVisualizer minta alkalmazáséra. (Pl. legyen felülnézeti “térkép”, más színek, más elrendezés, polárkoordinátás megjelenítés, zoomolható diagram stb.)
Az alkalmazás használja a Qt signals and slots mechanizmusát legalább egy olyan helyen is, ami a SimpleTelemetryVisualizerben nem szerepel.
A dokumentáció készüljön a forráskód alapján (kiegészítve egyéb fájlokkal) Doxygen segítségével. A generált HTML verziót a github “release” funkciójával kell letölthetővé tenni.
A dokumentációban legyen legalább 1 UML class diagram és legalább 1 UML szekvencia diagram. (Itt nem a Doxygen által automatikusan generált UML diagramokra gondolok, hanem saját készítésű, áttekintő diagramokra, amin azok az osztályok szerepelnek, ami a magyarázathoz ott éppen indokolt.)
A kliens program felhasználói felülete legyen esztétikus. Például az ablakot átméretezve ne essen szét az egész, hanem kövesse az átméretezést.
A GIT repositoryban látszódjanak a fejlesztés során készült commitok, vagyis ne egyetlen commit rakja be a kész programot a repositoryba a munka legvégén. A commitok ne szélsőségesen csak egy csapattagtól származzanak. A commit megjegyzések legyenek kifejezőek.

Bónusz pontok:
6p: Alapos öntesztelő funkció a robot számára. A tesztet futtathatja a kliens program is, de a robot firmwareje is. A lényeg, hogy van öntesztelési funkció.
3p: A dokumentáció számos (5+) UML diagramot használ, a leírások kihasználják a Markdown lehetőségeit, valamint a dokumentációban vannak hivatkozások, @see, @warning stb. parancsok.
3p: QTest unit teszt, legalább 3 eltérő (nem triviális) test case.
5p: A fejlesztés során tapasztalt tanulságok részletes összefoglalása egy publikálható jegyzet (“snippet”) formájában, githubon pull request formájában leadva. Erre példát a snippet oldalon az előző félév hasonló összefoglalói között találhat: http://bmeaut.github.io/snippets/snippets/AlkFejlHfTanulsagok/alkfejlhf/ 
(Ennek határideje is a házi feladat leadási határideje. Lásd még lejjebb az ellenőrzési listát!)

Néhány minta demó videó (az érintett csapatok beleegyezésével):
https://drive.google.com/drive/folders/0B4jF_XaQKmkuUm9XRWVRRGRxNjg?usp=sharing
https://www.youtube.com/watch?v=DFJsDSGP1IQ&ab_channel=GyulaSzab%C3%B3

Leadás előtti ellenőrzési lista, hogy ne maradjon le semmi:
A végleges verzió a master branchen van.
A docs/borito.md a helyén van és ki van töltve, benne a megosztott videó URL-jével.
A git repositoryban nincsen fordítási eredmény (pl. build vagy bin vagy obj könyvtár, vagy a Doxygen html kimenete)
A release elkészült és bináris csatolmányként fel van hozzá töltve a Doxygen kiemenete (a html könyvtár) egy zip-ben.

Snippet készítés esetén az ellenőrzési lista:
A snippet könyvtára a snippets\AlkFejlHfTanulsagok\##\", ahol ## a sorszáma. Mivel több készül párhuzamosan, előre kérjetek egy egyedi sorszámot Kristóftól, hogy ne legyen ütközés.
A sorszám szerepel az index.md fejlécében is “codename: AlkFelHf##” formában.
A pull requestet a https://github.com/bmeaut/snippets repository gh-pages branchére küldtétek, vagyis oda akarjátok mergelni (és nem a masterre, mert a webes felületen nem az jelenik meg).
