---
title:        Düsenhärte und abrasive Filamente
confidence:   reported
updated:      2026-08-30
author:       hyiger
printer:      Core One
toolhead:     INDX
hotend:       CHT high-flow, and plain-bore variants
nozzle:       0.4mm standard
firmware:     unknown
sources:
  - https://blog.prusa3d.com/prusa-core-one-gen-2-indx-shipping-has-started-complete-printers-open-for-orders_137623/
  - https://help.prusa3d.com/article/unknown-nozzle-36121-core-one-indx_1072730
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/nozzlegate-communications/
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/bondtech-nozzle-hardening-debacle-how-does-this-affect-prusa-indx-orders/
  - https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/a-summary-of-common-indx-problems/
  - https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/missing-profiles-in-slicer-for-non-0-4-nozzles-and-other-materials/
superseded_by:
source_sha:   6ecaf27c35d6a0f917c18146749fb67147011149393d19e76e56483c0117493e
---
# Düsenhärte und abrasive Filamente

## Zusammenfassung

Der INDX wurde mit gehärteten Düsen beworben, die für kohlefaser- und glasfasergefüllte
Filamente ausgelegt seien. Die ausgelieferten Düsen sind oberflächenbehandelt und nicht
durchgehärtet, mit einer Härte deutlich unterhalb dessen, was die Branche üblicherweise
unter „gehärtet“ versteht. Wenn Sie einen INDX in der Erwartung gekauft haben, vom ersten
Tag an abrasives Filament verarbeiten zu können, geht das nicht, und der Hersteller hat
ein Entschädigungsangebot veröffentlicht, das auch eine vollständige Rückgabe umfasst.
Betrachten Sie abrasives Filament auf den aktuellen Düsen als deren Verbrauch.

## Fehlercodes, die hierher führen

| Code | Was der Drucker anzeigt |
|---|---|
| [`36121`](https://help.prusa3d.com/article/unknown-nozzle-36121-core-one-indx_1072730) | Unbekannte Düse |
| [`36122`](https://help.prusa3d.com/article/unknown-nozzle-36122-core-one-indx_1072738) | Unbekannte Düse |

Sie werden ausgelöst, wenn die montierte Düse nicht zu der Angabe in der Druckdatei passt —
der Deklaration je Werkzeug, die auch die Kennzeichen für abrasiv und High-Flow trägt.

## Details

### Was versprochen wurde und was ausgeliefert wurde

Das Marketing für die passiven Werkzeuge beschrieb eine Konstruktion aus gehärtetem Stahl
mit einer Abrasionsbeständigkeit, die für Kohlefaser-, Glasfaser- und nachleuchtende
Filamente ohne nennenswerten Verschleiß ausreiche, und führte gehärtete Düsen als
Serienausstattung auf. Diese Formulierung wurde später aus den Shop-Einträgen entfernt,
und der Hersteller veröffentlichte das Eingeständnis, dass die ausgelieferten Düsen
nitrocarburiert sind — eine Oberflächenbehandlung — bei rund 30–32 HRC.

Zum Hintergrund, warum Besitzer darin einen wesentlichen Unterschied sehen und keine
Spitzfindigkeit: Die in den Threads ausführlich vertretene Position der Community ist,
dass „gehärtet“ in dieser Branche üblicherweise etwas im Bereich von 50–60 HRC meint und
dass ein Käufer das Marketing berechtigterweise so verstehen konnte. Eine
Oberflächenbehandlung im unteren Dreißigerbereich liegt einer unbehandelten Edelstahldüse
weit näher als einer gehärteten.

Erschwerend kommt hinzu, dass der High-Flow-Einsatz aus blankem Messing besteht. Selbst
wenn man die Behandlung des Grundkörpers beiseitelässt, werden gefüllte Filamente also die
Strömungsgeometrie erodieren. Und Verkaufsverpackung wie Produktseiten trugen die
ursprüngliche Härte-Aussage noch, als dies öffentlich wurde.

### Warum vollständig gehärtete Düsen hier tatsächlich schwierig sind

Das lohnt sich zu verstehen, denn es erklärt, warum die Lösung langsam kommt und nicht
bloß vorenthalten wird. Der INDX heizt seine Düsen induktiv. Konventionelles Härten beruht
darauf, Stahl in ein martensitisches Gefüge abzuschrecken, und dieses Gefüge hat eine
deutlich geringere magnetische Permeabilität — es ist ein schlechter magnetischer Leiter
und setzt damit dem schnellen magnetischen Fluss entgegen, auf den induktives Heizen
angewiesen ist. Eine vollständig gehärtete Düse und effizientes induktives Heizen wirken
gegeneinander.

Der Darstellung des Herstellers zufolge ließ sich die geplante vollständig gehärtete
Version nicht zuverlässig fertigen. Besitzer haben angemerkt, dass mindestens ein anderer
induktionsbasierter Werkzeugwechsler durchaus Düsen aus gehärtetem Stahl ausliefert, die
Einschränkung ist also offenkundig nicht absolut — es handelt sich aber um einen realen
technischen Zielkonflikt und nicht um einen rein kommerziellen.

### Was die Verschleißtests des Herstellers ergaben

Am 30. August 2026 veröffentlichte der Hersteller die Ergebnisse seiner Verschleißtests
an den ausgelieferten Düsen, zusammen mit der Ankündigung, dass Gen-2-Maschinen
ausgeliefert werden. Es ist die erste Aussage aus erster Hand darüber, was diese Düsen
tatsächlich aushalten — im Unterschied zu dem, wie sie spezifiziert waren — und sie ist
brauchbarer als alles, was auf dieser Seite davor steht.

Drei Punkte gehen daraus hervor.

**Die Härtefrage ist von Herstellerseite geklärt.** Diese Düsen tragen eine gehärtete
Oberfläche über einem ungehärteten Grundkörper, was der Hersteller darauf zurückführt,
wie Bondtech sie spezifiziert hat. Das ist nichts mehr, was aus Marketingtexten und
deren Rücknahme erschlossen wird; es wird von der Seite, die sie ausliefert, klar
festgestellt.

**Das Drucken nicht abrasiver Materialien ist nicht betroffen.** Alles Ungefüllte
verhält sich wie an einer Standarddüse der Core One, und die Liste des Herstellers ist
breit genug, um sie zu gruppieren: die vier Alltagsmaterialien (PLA, PETG, ABS, ASA);
die Flexiblen (TPU, TPE); die löslichen und Stützmaterialien (PVA, BVOH, HIPS); und die
ungefüllten technischen Kunststoffe — Nylon, PP, PBT, PC und PC-Blends. Wer kein
gefülltes oder abrasives Filament verarbeitet, hat das Problem dieser Seite nicht.

**Für Abrasives gibt es nun eine Standzeit statt einer Warnung.** Je Düse lauten die
derzeitigen Schätzungen des Herstellers:

| Filament | Ungefähre Standzeit je Düse |
|---|---|
| PETG-CF | 10 kg |
| PC-CF | 5 kg |
| stark abrasives Glow-Filament | 0,5 kg |

Er sagt außerdem klar, dass eine Maschine, die ausschließlich stark abrasives Material
verarbeitet, mit dem derzeit Ausgelieferten nicht gut bedient ist.

Zwei Vorbehalte sind mitzunehmen. Der Hersteller bezeichnet dies als derzeitige Werte aus
noch laufenden Tests und stellt eine ausführlichere Darstellung in Aussicht — sie können
sich also ändern. Und er berichtet die Ergebnisse als besser, als seine eigenen ersten
beschleunigten Tests nahelegten, was eine Aussage über jene früheren Tests ist und keine
unabhängige Bestätigung.

### Was jetzt zu tun ist

**Schalten Sie die Einstellung „Düse gehärtet“ am Drucker aus**, im Menü für alle
Werkzeuge. Das ist praktisch von Bedeutung: Ist sie aus, erzeugt das Slicen eines Profils
für abrasives Material eine Warnung, statt stillschweigend fortzufahren. Es ist die eine
Einstellungsänderung, die Sie vor Ihrem eigenen Muskelgedächtnis schützt.

**Behandeln Sie kohlefaser- und glasfasergefülltes Filament als Einsatz auf eigenes
Risiko** und bevorzugen Sie für gefüllte Materialien eine Düse mit glatter Bohrung
gegenüber der High-Flow-Geometrie — die glatte Bohrung hat weniger feine innere Struktur,
die erodieren kann.

**Prüfen Sie das Entschädigungsangebot.** Der Hersteller hat Optionen veröffentlicht, die
ein Shop-Guthaben je Düse, eine geringere Barerstattung je Düse oder die vollständige
Rückgabe des Founders-Edition-Kits gegen volle Erstattung ohne Kosten umfassen. Ansprüche
laufen über das Kontaktformular des Herstellers, mit Ihrer Bestellnummer und der von Ihnen
gewählten Option.

TODO(verify): die Guthaben- und Erstattungsbeträge je Düse und je Kit, die Rückgabefrist
und ob ein montiertes und benutztes Kit noch zurückgegeben werden kann. Jede dieser
Angaben ist ein Betrag oder eine Frist, bei der ein Irrtum den Leser Geld oder eine
versäumte Frist kostet — holen Sie sie aus der aktuellen Erklärung des Herstellers selbst,
nicht von dieser Seite. Unabhängig davon hat Prusa eine verlängerte Rückgabefrist für
Kit-Bestellungen aus der ersten Charge veröffentlicht; TODO(verify) auch deren Länge.

**Wie der Anspruch abläuft, nach Angaben von Besitzern, die einen gestellt haben.** Das
Kontaktformular hat keine offensichtlich passende Kategorie; Besitzer berichten, unter dem
allgemeinen Anfragetyp „Sonstiges“ eingereicht zu haben. Rechnen Sie mit einer sofortigen
automatischen Eingangsbestätigung und danach mit Wartezeit — ein Besitzer berichtet, eine
Woche zuvor geschrieben und eine Bestätigung erhalten zu haben, aber immer noch ohne
inhaltliche Antwort zu sein. Ein anderer hat an dem Tag eingereicht, an dem dies
geschrieben wurde, und berichtet weitgehend dasselbe. Reichen Sie also früh ein, führen Sie
eine eigene Aufzeichnung darüber, was Sie beantragt haben, und deuten Sie Schweigen nicht
als Ablehnung.

Sie können auch eine **Mischung** aus Guthaben und Barerstattung beantragen statt
ausschließlich das eine. Mindestens ein Besitzer hat das getan, weil er genug Guthaben
wollte, um eine wirklich gehärtete Düse zu kaufen, sobald es eine gibt.

!!! note "Shop-Guthaben kauft Düsen, die Sie vielleicht noch nicht nutzen können"
    Wissenswert, bevor Sie Guthaben statt Bargeld wählen: PrusaSlicer bietet für den INDX
    derzeit nur eine einzige Düsenvariante an, für andere Größen existiert also kein Profil
    zum Drucken. Ein Besitzer, der genau vor dieser Entscheidung stand, hat es unumwunden
    gesagt — die betreffende Person hatte andere Größen nie ausprobiert, weil es keine
    Profile dafür gibt, was Guthaben-für-mehr-Düsen zu einer schwächeren Option macht, als
    es aussieht — beide INDX-Druckermodelle deklarieren in Prusas veröffentlichtem
    Profilpaket eine einzige Düsenvariante, sodass keine andere Größe auswählbar ist. Siehe
    [fehlende Slicer-Profile](missing-slicer-profiles.md).

Beachten Sie, dass die Angemessenheit der Entschädigung umstritten ist. Mindestens ein
Besitzer hat die Rechnung durchgeführt und kam zu dem Ergebnis, dass das angebotene
Guthaben einen deutlich geringeren Aufschlag darstellt als der Aufpreis für gehärtet
gegenüber Standard im Shop des Herstellers selbst und bei anderen Düsenherstellern. Das
ist eine Berechnung aus der Community und keine Angabe des Herstellers, aber es ist
vernünftig, das vor der Annahme einer Option selbst zu prüfen.

### Was kommt

Ein Drittanbieter von Diamantdüsen hat eine INDX-kompatible Variante bestätigt.
Bemerkenswert ist, dass der Diamant dotiert wird, damit er für den
Wirbelstrom-Offsetsensor erkennbar bleibt — eine vollständig nichtleitende Spitze wäre für
diesen Sensor unsichtbar, was eine reale konstruktive Randbedingung für jede Ersatzdüse
darstellt. Der Zeitrahmen wurde in Monaten und nicht in Wochen beschrieben.

!!! note "Zwei getrennte Defekte werden häufig zusammen mit diesem diskutiert"
    Eine Reihe von Düsen wurde bereits verstopft ausgeliefert, und unabhängige Zerlegungen
    fanden Bearbeitungsspäne im Inneren — in einem Fall ein Stahlspan in der Mischkammer,
    in einem anderen Rückstände quer über dem Austrittskanal. Das ist ein Fertigungsfehler,
    kein Verschleiß- oder Härteproblem, und der Hersteller tauscht betroffene Düsen aus.
    Daneben gibt es eine separate, zu klein ausgeführte Bohrung der Filamentführung, die
    das Entladen betrifft; sie ist auf
    [einer eigenen Seite](filament-guide-bore-unload-failure.md) behandelt.

## Verifikation

`reported` (gemeldet) — dies ist das am besten belegte Thema im gesamten Material. Die
beiden Hauptthreads, [nozzlegate communications](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/nozzlegate-communications/)
und [Bondtech nozzle hardening debacle](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/bondtech-nozzle-hardening-debacle-how-does-this-affect-prusa-indx-orders/),
umfassen zusammen mehrere hundert Beiträge von rund fünfzig verschiedenen Teilnehmern, und
beide zitieren den ursprünglichen Marketingtext, das veröffentlichte Eingeständnis des
Herstellers und dessen Entschädigungserklärung direkt.

Stark belegt: die Marketingaussage und ihre Entfernung, die Natur als
Oberflächenbehandlung und der Härtewert, der Messingeinsatz, Existenz und Aufbau des
Entschädigungsangebots sowie die Erklärung über Induktion und Permeabilität — all das
erscheint in den Threads als zitiertes Material des Herstellers und nicht als
Schlussfolgerung von Besitzern.

!!! note "Warum hier Härtewerte stehen, andere Zahlen aber nicht"
    Diese Website hält Kalibrierwerte, Temperaturen und Druckeinstellungen zurück, bis ein
    Mensch sie an der Hardware verifiziert hat. Ein Härtewert ist eine andere Art von Zahl:
    Er ist eine veröffentlichte Materialeigenschaft und kein Wert, den jemand in einen
    Slicer oder an einer Bohrmaschine einstellt; ein Irrtum darüber führt also in die Irre,
    statt Hardware zu beschädigen. Der niedrigere Wert ist das vom Hersteller selbst
    veröffentlichte Eingeständnis; der höhere ist die Branchenkonvention, an der Besitzer
    ihn messen, und keine Spezifikation eines ausgelieferten Teils. Beide sind belegt.
    Bitte entfernen Sie sie nicht — ohne sie lässt sich die zentrale Aussage dieser Seite
    nicht überprüfen.

    Die am 30. August ergänzten Angaben zur Standzeit der Düsen fallen unter dieselbe
    Begründung. Eine Verschleißschätzung in Kilogramm je Düse ist kein Wert, den jemand
    irgendwo einstellt; sie ist die veröffentlichte Angabe des Herstellers dazu, wann ein
    Verschleißteil aufgebraucht ist, und sie ist auf die Ankündigung belegt, aus der sie
    stammt.

Schwächer: Der Härtewert, den ein Käufer hätte erwarten „dürfen“, ist eine Konvention der
Community und kein veröffentlichter Standard. Die Rechnung zur Angemessenheit der
Entschädigung ist die Berechnung eines einzelnen Besitzers. Der Zeitplan für die
Diamantdüse ist eine Absichtserklärung eines Drittanbieters.

Wo die Quellen sich widersprechen: Besitzer sind sich deutlich uneins darüber, ob die
Entschädigung angemessen ist und wie groß die praktische Auswirkung der Härte für jemanden
tatsächlich ist, der wenig Abrasives druckt. Beide Positionen werden in den Threads in
gutem Glauben vertreten. Diese Seite bezieht in der kommerziellen Frage bewusst keine
Position — nur in der technischen Tatsache, dass diese Düsen nicht im herkömmlichen Sinne
gehärtet sind.

## Verwandte Seiten

- [Zu kleine Bohrung der Filamentführung](filament-guide-bore-unload-failure.md)
- [Wen Sie kontaktieren](support-and-warranty-path.md) — der Weg für Ansprüche und Rückgaben
- [Werkzeug-Offset-Kalibrierung](offset-sensor-board-failure.md) — warum die
  Leitfähigkeit der Düse für den Sensor wichtig ist
