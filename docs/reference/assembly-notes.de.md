---
title:        Montagehinweise — INDX-Umbausatz
confidence:   reported
updated:      2026-10-18
author:       hyiger
printer:      Core One, Core One Plus
toolhead:     INDX
hotend:       unknown
nozzle:       unknown
firmware:     unknown
sources:
  - https://help.prusa3d.com/manual/bondtech-indx-conversion-kit-for-the-prusa-core-one-founders-edition_2397
  - https://help.prusa3d.com/manual/prusa-indx-conversion-kit-for-the-prusa-core-one_2432
  - https://help.prusa3d.com/guide/4-indx-toolhead-side-filament-sensors_1096247
  - https://help.prusa3d.com/guide/5-spoolholders-tool-dock-assembly_1096255
  - https://help.prusa3d.com/article/assemblling-the-prusa-indx-core-one-with-the-gen-2-upgrade_1147602
  - https://help.prusa3d.com/downloads/core-one-indx
  - https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/list-of-differences-between-founders-edition-and-prusa-edition-instructions/
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/why-4-8-tools-tested-if-only-less-are-needed/
  - https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/bondtech-indx-conversion-kit-assembly-pain-points-prep-notes/
  - https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/sourcing-tool-dock-hardware/
  - https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/removing-magnets-from-tool-docks-you-dont-need-to-destroy-them/
  - https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/parts-list-for-screws-and-bolts/
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/update-kind-of/
  - https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/no-tools-in-my-indx-upgrade-kit/
  - https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/core-one-to-core-onegen2-indx-upgrade-path/
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/prusa-indx-update-shipping-starts-this-week/
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/bondtech-founders-edition-upgrade-path-to-core-one-gen-2/
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/coreone-with-mmu-upgrade-to-indx/
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/update-kit-from-indx-4t-to-8t/
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/how-many-types-of-fasteners-etc-come-with-indx-gen2-upgrade/
  - https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/indx-fe-upgrading-to-gen2/
  - https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/calibration-issues-from-beginning/
  - https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/bed-leveling-issues-3/
superseded_by:
source_sha:   05a9b822568ebf9c8f7d075754932bbfde317786b1d3398a2c519768cb09946d
---
# Montagehinweise — INDX-Umbausatz

!!! info "Dies ergänzt die offizielle Anleitung, es ersetzt sie nicht"
    Bauen Sie nach der offiziellen Anleitung für die Edition Ihres Satzes: der
    [Anleitung zur Founders Edition](https://help.prusa3d.com/manual/bondtech-indx-conversion-kit-for-the-prusa-core-one-founders-edition_2397)
    für einen Satz von Bondtech oder der
    [Anleitung zur Prusa-Edition](https://help.prusa3d.com/manual/prusa-indx-conversion-kit-for-the-prusa-core-one_2432)
    für Prusas eigenen Satz. Worin sich beide unterscheiden, steht weiter unten. Was
    folgt, ist die gesammelte Erfahrung von Erbauern, die den Umbau hinter sich
    haben — die Schritte, bei denen es sich lohnt, langsamer zu werden, die Dinge, die
    man im Voraus bereitlegen sollte, und die Stellen, an denen Anleitung und
    Wirklichkeit auseinandergegangen sind.

    Prusa behebt gemeldete Probleme in der Anleitung aktiv, daher kann manches, was hier
    festgehalten ist, bereits korrigiert sein. Betrachten Sie die aktuelle Anleitung als
    maßgeblich und diese Seite als das, was Sie vorwarnt, was auf Sie zukommt.

## Zusammenfassung

Der größte Teil der Mühe bei diesem Aufbau lässt sich durch Vorbereitung vermeiden.
Drucken Sie zuerst drei Dinge, legen Sie ein kleines Schraubensortiment und einen
M3-Gewindebohrer bereit, und wissen Sie im Voraus, welche vier oder fünf Schritte
Erbauer regelmäßig aus dem Tritt bringen. Der Aufbau ist eher lang als schwierig; der
Ärger entsteht daraus, dass mitten im Schritt ein Verbindungselement ausgeht, oder
dass sich herausstellt, dass ein Druckteil hätte nachgeschnitten werden müssen,
nachdem Sie bereits angefangen haben, Schrauben einzudrehen.

## Diese Teile vor dem Beginn drucken

- **Ein Werkzeug zum Entfernen von Spreiznieten.** Die Demontage bedeutet, viele
  Nylon-Spreiznieten herauszuziehen, und dieses Teil wird mit weitem Abstand am
  häufigsten als Vorab-Druck gelobt. Es verhindert, dass Sie Panels zerkratzen oder
  Nieten durch den Raum schießen. Klein und schnell gedruckt.
- **Eine Riemen-Montagelehre.** Aus der Community, gefertigt nach der Geometrie der
  offiziellen Montageplatte. Sie hält beide Riemen zusammen, sodass sie bei gleicher
  Spannung auf gleiche Länge kommen, erlaubt es, sie bündig mit der Montageplatte zu
  kürzen, und erlaubt es, sie hinterher in exakt dieselbe Position zurückzubringen.
  Riemen und Werkzeugkopfmontage sind der fummeligste Teil des Aufbaus, und das nimmt
  der Sache viel von ihrer Schärfe. Der Bau der Lehre erfordert
  Einschmelz-Gewindeeinsätze und eine Handvoll M3-Schrauben, drucken Sie sie also aus
  und legen Sie diese Teile bereit, bevor Sie an diese Stelle kommen.
- **Alle Strukturteile, die Sie sich selbst schulden.** Druckteile tragen
  Versionsbuchstaben, und welche davon dem Satz beiliegen, hängt von der Serie ab.
  Einige liefert Prusa im Karton mit; andere lädt man herunter und druckt sie selbst,
  und sie sind mit den Werksteilen identisch. Gleichen Sie Ihre Teilebeutel mit der
  offiziellen Sammlung ab, *bevor* Sie anfangen, statt eine Lücke mitten im Aufbau zu
  entdecken.

Laden Sie eine **frische Kopie** der offiziellen Teilesammlung herunter, statt Dateien
wiederzuverwenden, die Sie sich früher geholt haben. Sie wurde seit dem Erscheinen
überarbeitet — das Docking-Panel verbraucht jetzt weniger Material, und der
Silikonreiniger sowie der Abfallbehälter sind enthalten —, ältere Downloads passen
also nicht zur aktuellen Anleitung.

## Diese Dinge bereitlegen

- Ein kleines **M3-Schraubensortiment**. Siehe die Engpässe bei Verbindungselementen
  weiter unten.
- Einen **M3-Gewindebohrer** oder eine M3-Ersatzschraube zum Vorschneiden von Hand.
- Eine **Zwinge** — eine Einhandzwinge vom Typ Quick-Grip — oder eine gedruckte
  Einpresslehre für die Dock-Magnete, falls Sie eigene Docks drucken oder ergänzen
  wollen. Keine der beiden Editionen der Anleitung lässt Sie Magnete in die
  mitgelieferten Werkzeughalter setzen.
- Ein **großes Stück Karton**, auf das Sie den Drucker stellen, damit Sie ihn während
  der unhandlichen Schritte frei drehen und kippen können.
- Einen oder zwei **Ersatz-Riemenspanner**, gedruckt oder gekauft, solange der Drucker
  noch läuft. Beim Aufbau werden die Riemen abgenommen und wieder gespannt, und
  Besitzer in zwei Threads berichten, dass ein Teil des Spanners versagt hat. Einer,
  dessen Drucker mehrere Umbauten hinter sich hat, zuletzt den auf den INDX, hat dabei
  einen zerbrochen und sagt, das sei vielen anderen ebenfalls passiert. Der andere
  brauchte beim ursprünglichen Aufbau des Core One ein neues Teil für die
  Spannrolle und musste, ohne zweiten Drucker, warten, bis der Support eines schickte.
  Prusas Edition der Anleitung lässt Sie die Spannschrauben bei der Arbeit an den
  Riemen herausnehmen und schmieren, um späteren Ärger zu vermeiden; die Anleitung zur
  Founders Edition lockert sie nur.

**Prüfen Sie Ihre Druckplatte jetzt, nicht hinterher.** Wenn Sie auf einer
übergroßen Federstahlplatte eines Drittanbieters drucken, kann es sein, dass sie die
Werkzeug-Docks nach deren Einbau nicht mehr freigängig passiert — auch wenn sie heute
einwandfrei in Ihre Maschine passt. Siehe
[Druckplatten-Kompatibilität](build-plate-compatibility.md). Das vor dem Beginn zu
klären ist besser, als den Aufbau abzuschließen und dann festzustellen, dass die
Platte Ihrer Wahl unbrauchbar ist.

!!! danger "Die Firmware aktualisieren, *bevor* Sie den alten Drucker zerlegen"
    Wenn Sie eine Maschine umbauen, die als MK4S begonnen hat, bringen Sie deren
    Firmware auf den Stand, den der Umbau voraussetzt, **solange sie noch
    zusammengebaut und funktionsfähig ist**. Ein Besitzer hat den INDX-Satz auf ein
    von MK4S auf Core One aufgerüstetes Gerät gebaut, ohne den Core One je in seiner
    Nextruder-Form betrieben und ohne zuvor die MK4S-Firmware angehoben zu haben. Die
    zusammengebaute Maschine startete beim ersten Einschalten in einen roten
    Fehlerbildschirm, von dem aus es keinen Weg nach vorn gab.

    Die Wiederherstellung, falls Sie bereits in dieser Lage sind: den ursprünglichen
    Nextruder wieder montieren und den Türsensor abklemmen, sodass der Bootloader die
    Maschine wieder als MK4S erkennt. Das genügt, damit die Firmware-Updates
    durchlaufen; danach können Sie den Umbau wieder zusammensetzen.

    *Einzelmeldung.* Ein Besitzer, aus erster Hand, der die Maschine gerettet hat —
    aber niemand hat es reproduziert, und die Wiederherstellung bedeutet, den Aufbau
    teilweise rückgängig zu machen. Lesen Sie es als Grund, früh zu aktualisieren, und
    nicht als Vorgehen, das Sie erwarten sollten zu brauchen.

## Founders Edition oder Prusa-Edition

Den Satz gibt es in zwei Editionen, jede mit eigener Anleitung: die Founders Edition,
verkauft von Bondtech, und Prusas eigenen Satz. Prusa stellt beide Anleitungen bereit,
und ihre Kapitel und Schritte entsprechen einander fast eins zu eins. Ein Besitzer, der
im Forum nach einer Liste der Unterschiede fragte, bekam keine offizielle. Legt man die
beiden Anleitungen in ihrem Stand vom 18. Oktober 2026 nebeneinander, unterscheiden sie
sich an diesen Stellen, die ändern, was Sie tun:

- **Gen 2.** Nur die Prusa-Anleitung behandelt das Gen-2-Upgrade, und sie markiert
  jede Stelle, an der ein kombinierter Aufbau die Anleitung wechselt; siehe unten. Die
  Anleitung zur Founders Edition lässt Gen 2 ganz weg.
- **Riemenspanner.** Die Prusa-Anleitung nimmt die Spannschrauben heraus und schmiert
  sie; die Anleitung zur Founders Edition lockert sie nur.
- **Dock-Lüfter.** Die Teile unterscheiden sich in Bezeichnung und Verpackung. Die
  Prusa-Anleitung führt ein Bauteillüfter-Gebläse und eine „Verteilerplatine für den
  Dock-Lüfter“ auf, beide aus ihrer Elektronikbox, und nennt diese Platine einen Schritt
  später FunFan-Platine. Der Satz der Founders Edition bringt ein Dock-Lüfter-Gebläse
  und seine FunFan-Platine in einem eigenen Beutel mit. Ob sich die Teile selbst
  unterscheiden, sagt keine der beiden Anleitungen. Bei einem Core One, der aus einem
  MK4 oder MK4S umgebaut wurde, tauscht die Prusa-Anleitung die beiden Lüfter: Das
  Gebläse aus dem Satz wird zum Bauteillüfter, weil der eigene Lüfter des umgebauten
  Druckers ein deutlich längeres Kabel hat, und dieser ausgebaute Lüfter wird zum
  Dock-Lüfter.
- **Halter der Düsendichtungen.** Die Prusa-Anleitung fügt eine Anweisung hinzu, jeden
  zusammengebauten Halter vor dem Einbau umzudrehen, sodass das gebogene Ende jeder
  Dichtung nach unten zeigt. Die Anleitung zur Founders Edition enthält keine solche
  Anweisung. Beim Einbau der Halter lassen Sie dann beide Anleitungen die gebogenen
  Enden mit der Abbildung abgleichen.
- **Abstreifer.** Die Prusa-Anleitung nimmt zu Beginn des Kapitels zum Werkzeugdock die
  rechte Seitenverkleidung ab und montiert die Düsenreinigung außerhalb des Druckers an
  ihr; die Anleitung zur Founders Edition lässt die Verkleidung angebaut und setzt die
  Düsenreinigung von innerhalb des Druckers an sie.
- **Firmware.** Die Anleitung zur Founders Edition flasht von einem USB-Stick, der dem
  Satz beiliegt und die Firmware bereits enthält. Die Prusa-Anleitung lässt Sie die
  aktuelle Firmware selbst auf einen USB-Stick laden; halten Sie also einen bereit.

Besitzer ergänzen Unterschiede bei den Teilen selbst. Ein Besitzer sagt, dass die
Frontplatte des Prusa-Satzes die Querstreben der Founders Edition nicht mehr hat, was
den Blick freier macht, und vermutet, dass eine Edition einige gespritzte Teile
verwendet, wo die andere gedruckte hat, ohne zu sagen, welche. Der Autor dieser Seite
ergänzt, dass sich die Adapter der Düsendichtungen unterscheiden, damit sie zur
Prusa-Frontplatte passen; dazu passt, dass die Sammlung der Druckteile für jede Edition
einen eigenen Halter für die Düsendichtung enthält, wie unter Bezugsquellen weiter
unten vermerkt. Der Besitzer, der die Frontplatte beschrieben hat, merkt außerdem an,
dass neuere Core-One-Drucker mit einer gelochten rechten Seitenverkleidung für den
größeren Abfallbehälter ausgeliefert werden. Keiner der beiden Sätze enthält sie, eine
vorhandene Maschine muss sie also getrennt kaufen.

**Prüfen Sie nach jedem Sprung für vier Werkzeuge, in welcher Anleitung Sie sind.** Das
Kapitel der Prusa-Anleitung zu den seitlichen Filamentsensoren weist Erbauer eines
Vier-Werkzeug-Satzes zweimal an, vorzuspringen, und beide Verweise führen in das
entsprechende Kapitel der Anleitung zur Founders Edition. Ein Besitzer ist einem davon
gefolgt und hat in der falschen Anleitung bis ins nächste Kapitel weitergebaut, bevor
der Fehler auffiel, und hat dann beim Schritt einen Kommentar mit dem richtigen Verweis
hinterlassen. Bei der Prüfung für diese Seite am 18. Oktober 2026 zeigten beide
Verweise noch auf die Anleitung zur Founders Edition. Die Schritte direkt nach dem
Sprung sind in beiden Anleitungen nahezu gleich, sodass der Fehler zunächst wenig
kostet, doch Dock-Lüfter und Halter der Düsendichtungen unterscheiden sich weiter
hinten. Achten Sie nach dem Sprung auf den Titel der Anleitung oben auf der
Seite.

*Gemischte Stufen.* Die Liste der Unterschiede zwischen den Anleitungen ist der eigene
Vergleich dieser Seite zu jenem Datum; Prusa überarbeitet die Anleitungen, prüfen Sie
also die aktuellen Fassungen. Die Unterschiede bei den Teilen sind *vorläufig*: die
Schilderung eines Besitzers und die des Autors dieser Seite, in einem einzigen Thread.
Die Sprungverweise beruhen auf der Meldung dieses Besitzers und der Prüfung dieser
Seite.

## Tücken beim Lieferumfang

**Zu geringe Stückzahlen bei Verbindungselementen sind die mit Abstand häufigste
Beschwerde.** Mehr als ein Beutel wurde mit weniger Schrauben ausgeliefert, als sein
Etikett angibt, und mindestens ein Schritt verlangt mehr, als mehrere Erbauer erhalten
haben. Manche mussten selbst beschaffen oder zuschneiden. Das ist der Grund für das
Schraubensortiment weiter oben — mitten im Schritt auszugehen ist der Unterschied
zwischen einem Abend und einem Wochenende.

**Es gibt keine zusammengefasste Liste der Verbindungselemente.** Verbindungselemente
sind in der Anleitung Schritt für Schritt aufgeführt und sonst nirgends; wer gern in
beschriftete Fächer vorsortiert, muss sich diese Liste selbst herausschreiben. Prusas
[Spickzettel zum Core One INDX](https://www.prusa3d.com/downloads/others/C1_INDX_cheatsheet_EN_1_0.pdf)
ist nicht unbedingt diese Liste: Ein Besitzer fragte, ob jedes Verbindungselement und
jeder Clip auf seiner Übersicht im Satz enthalten sei, und die einzige Antwort lautete,
die Übersicht sei allgemein gehalten. *Einzelne Antwort.* Im
Forum kursiert ein inoffizielles PDF zu den Verbindungselementen, es war jedoch
KI-generiert und von seinem eigenen Verfasser nicht überprüft — behandeln Sie es als
Ausgangspunkt für den Abgleich mit der Anleitung, nicht als Stückliste. Dasselbe gilt
für eine spätere, KI-erstellte Liste der Typen von Verbindungselementen in INDX- und
Gen-2-Satz zusammen, bei der ihr Verfasser selbst einräumte, dass sie falsch sein
könnte, und ankündigte, sie nach Eintreffen der Teile zu überprüfen.

**Erwarten Sie kein Werkzeug im Karton.** Der Umbausatz geht davon aus, dass das
benötigte Werkzeug mit dem Core One gekommen ist, der bereits auf Ihrem Tisch steht, und
die Einleitung beider Editionen der Anleitung sagt das auch: Verwenden Sie das Werkzeug,
das dem Drucker beilag. Die Aufbaunotizen zur Founders Edition, aus denen diese Seite
hervorgegangen ist, nennen einen einzelnen T10-Schraubendreher im Satz. Der von Prusa
verkaufte Satz enthält Berichten zufolge gar keines, und ein Vertreter von Prusa hat im
Forum bestätigt, dass das so gewollt ist: Ein Upgrade-Satz setzt auf das Werkzeug, das
mit dem Drucker geliefert wurde. Wenn Ihr Core One fertig montiert kam, haben Sie dieses
Werkzeug womöglich nicht. Die Anleitung selbst weist darauf hin, dass der
T10-Schraubendreher nur Bausatz-Druckern beilag, bezeichnet ihn aber als Erleichterung,
nicht als Notwendigkeit. Derselbe Vertreter sagt, jeder
Drucker, ob Bausatz oder montiert, solle mit Werkzeug ausgeliefert werden, und der
Support helfe, falls es bei Ihnen fehlte — dennoch hat ein Besitzer eines montierten
Geräts nie welches erhalten. Prüfen Sie das vor dem Beginn, nicht erst bei der ersten
Schraube.

**MMU3-Besitzer:** Die Einheit muss zuerst herunter, und die Anleitung behandelt den
Ausbau kaum. Planen Sie ihn als eigene Aufgabe ein, bevor Sie den eigentlichen Umbau
beginnen. Er macht weniger Arbeit, als der Rat der Anleitung, die MMU-Montage rückwärts
durchzugehen, vermuten lässt. Ein Besitzer, der von einer MMU3 umgebaut hat, weist
darauf hin, dass der gesamte Extruder ersetzt wird — erhalten bleiben nur ein paar
Schrauben und der Bauteillüfter —, sodass man die Änderungen der MMU daran nicht
einzeln zurückbauen muss; die Einheit wurde samt Kabeln und Schläuchen herausgehoben.
Besitzer in einem anderen Thread beschreiben denselben Umbau als unkompliziert.

**Manche Sätze enthalten ein zweites Upgrade.** Prusa hat der ersten Charge der
Bestellungen des Prusa-INDX-Umbausatzes sein Core One+ (Gen 2)-Upgrade beigelegt — neue
Riemen, Riemenscheiben und Ausgleichselemente für die Wärmeausdehnung —, in einem
eigenen Karton und mit der Absicht, dass es während des INDX-Aufbaus eingebaut wird.
Prusas Anleitung bezeichnet es als optional: Der INDX braucht es nicht. Besitzer,
darunter einer, der beides im Karton fand, waren sich über die Reihenfolge unsicher,
doch Prusa hat sie festgelegt. Der Verweis in seiner Ankündigung,
[prusa.io/Prusa-INDX-GEN-2](http://prusa.io/Prusa-INDX-GEN-2), führt nicht zu einer
reinen Gen-2-Anleitung, sondern zu einem kombinierten Artikel, der die INDX-Anleitung
und die Gen-2-Anleitung nebeneinander führt und jeden Schritt nennt, an dem gewechselt
wird, und die Anleitung zur Prusa-Edition verweist an diesen Stellen auf ihn. Er bringt
die ersten Gen-2-Teile, die Ausgleichselemente, ins Spiel, sobald die
Bett-Abstandshalter und der Offset-Sensor sitzen, was nahe an der Stelle liegt, an der
der Autor dieser Seite die Gen-2-Teile eingebaut hatte. Er lässt Sie außerdem die
Spannschrauben der Riemen mit dem Schmiermittel schmieren, das dem INDX-Satz beiliegt,
und beide Motorkabel, X und Y, zu Beginn an der Platine abziehen und gegen Ende wieder
einstecken, jedes in seinen beschrifteten Anschluss — eine Gelegenheit, sie zu
vertauschen; siehe die auf Montagefehler zurückgeführten Fehlschläge weiter unten. Zwei
Besitzer im Ankündigungs-Thread von Prusa raten, beide Arbeiten zusammen zu erledigen,
da beide die Riemen und das Bett betreffen; einer, der einen Satz der Founders Edition
gebaut hatte, stellte fest, dass die Gen-2-Arbeit nur den Tausch der Riemenscheiben
hinzufügte. Der Artikel erwähnt den Gen-2-Düsenabstreifer nicht. Der Autor dieser
Seite lässt ihn weg, da der INDX-Aufbau keine Verwendung für ihn hat, und ein Besitzer
der Founders Edition rät in einem anderen Thread ebenfalls dazu, dieses Teil
wegzulassen.

Zwei Kommentare zum kombinierten Artikel betreffen dessen Foto, das zeigt, wie die X-
und Y-Kabel wieder an die Platine kommen. Einer sagt, auf dem Foto stecke das Kabel des
Z-Motors in der falschen Buchse. Ein weiterer Besitzer, dessen hinterer Z-Motor nach
dem kombinierten Upgrade nicht richtig lief, stellt dieselbe Frage und gibt an, sein
Z-Kabel habe eine Buchse rechts von der Stelle gesteckt, die das Foto zeigt. Was
richtig ist, ist ungeklärt; stecken Sie jedes Kabel daher nach der Beschriftung auf der
Platine. *Vorläufig*: zwei Kommentare zu einem einzigen Artikel, ohne Antwort von
Prusa.

Prüfen Sie nach dem ersten Flashen den Bildschirm der Hardwarekonfiguration: Ein
Besitzer stellte mit der INDX-Firmware, die Mitte September 2026 aktuell war, also vor
dem stabilen Release 6.9.1, fest, dass sie angenommen hatte, die Gen-2-Riemen seien
verbaut — in diesem Fall zu Recht, aber sie hatte keine Möglichkeit, das zu erkennen.
Ein zweiter Besitzer fand in einem anderen Thread dieselbe Einstellung an einer
Maschine, deren Gen-2-Teile noch nicht verbaut waren, und sie ließ die
Dock-Kalibrierung scheitern; siehe
[Dock-Kalibrierung](../issues/dock-calibration-rejects-docks.md). Prusas
Firmware-Quellcode, wie für 6.9.1 veröffentlicht, wendet beim ersten Start die
Gen-2-Variante an, was beides erklären würde; dass das Flashen der INDX-Firmware als
erster Start zählt, ist jedoch erschlossen, nicht bestätigt. Der Quellcode zu 7.0.0
ist nicht veröffentlicht, und die zugehörigen
[Release Notes](https://help.prusa3d.com/downloads/core-one-indx) nennen keine Änderung
an dieser Voreinstellung; prüfen Sie den Bildschirm also auch unter 7.0.0.

## Schritte, bei denen man langsamer machen sollte

**Das Kopfkabel anschließen.** Der meistverfluchte Schritt des Aufbaus. Was
funktioniert: zuerst nur ein kurzes Stück der Nylon-Zugschnur durchführen, die
Kabelabdeckung sichern und *dann* den Rest nachführen — sonst zieht die Spannung die
Schnur immer wieder aus ihrer Nut heraus.

TODO(verify): die Länge der Zugschnur, die vor dem Sichern der Abdeckung durchzuführen
ist.

**Die Linearschiene ausrichten.** Lösen Sie die sechs Schienenschrauben **nur zwei
oder drei Umdrehungen** — Prusa hat das in den Kommentaren zur Anleitung bestätigt.
Drehen Sie sie nicht vollständig heraus: Der mittlere Block kann herausfallen, und ihn
wieder zusammenzusetzen ist wirklich unangenehm. Das ist ein guter Moment, die Schiene
nachzuschmieren, solange Sie herankommen. Ziehen Sie die untere Portalschraube wieder
an, bevor Sie fortfahren.

**Z anheben für die Spulenhalterschrauben.** Die in der Anleitung angegebene Z-Höhe
legt Berichten zufolge nur zwei der vier Schrauben frei. Erbauer berichten, dass sie
merklich höher fahren mussten.

TODO(verify): die Z-Höhe, die die Anleitung angibt, und die Höhe, die tatsächlich
funktioniert. Beide stehen im Quell-Thread. Hier etwas falsch zu machen kostet Sie
nichts außer Zugänglichkeit, daher ist die qualitative Form — höher fahren, als die
Anleitung sagt — der brauchbare Teil.

**Verkabelung des Offset-Sensors.** Führen Sie **zuerst** das Kabel des Offset-Sensors
durch die Bohrung, danach das dickere RGB-LED-Kabel. Die andere Reihenfolge passt
nicht. Achten Sie auf die Schraube an dieser Stelle: Man greift dort blind und
ungünstig, und das Gewinde reißt leicht aus. Ein Erbauer hat lieber einen
Einschmelz-Gewindeeinsatz gesetzt, statt sich damit herumzuschlagen.

**Filamentsensor-Blöcke.** Die Schrauben der Kugelerkennung sollen locker bleiben — so
locker, dass die Stahlkugel von allein wieder herunterfällt. Prüfen Sie jeden Block,
bevor Sie ihn montieren; hinterher zu kontrollieren ist deutlich schwieriger.

**Gewinde in Druckteile schneiden.** Senkkopf- und selbstschneidende Schrauben reißen
hier leicht aus, und die Bohrungen sind eng. Schneiden Sie mit einer M3-Ersatzschraube
vor. Allein die Vorderseite des Werkzeughalters hat über zwei Dutzend Bohrungen zu
schneiden, richten Sie sich also darauf ein und arbeiten Sie langsam — Abrutschen
hinterlässt Spuren auf der Frontplatte.

## Magnete der Werkzeug-Docks

Die Dock-Magnete sind eine **absichtlich sehr straffe Presspassung**, und das erwischt
jeden, der damit zu tun bekommt. Schon einen Magneten in seiner Bohrung anzusetzen ist
mühsam, und ihn vollständig zu setzen erfordert echte, gerichtete Kraft. Planen Sie
nicht damit, das von Hand zu schaffen. Erbauer verwenden eine Einhandzwinge oder eine
gedruckte Einpresslehre. Damit zu tun bekommen Sie es, wenn Sie Docks drucken, ersetzen
oder ergänzen: Keine der beiden Editionen der aktuellen Anleitung hat einen Schritt, der
Magnete in die mitgelieferten Werkzeughalter setzt.

### Wenn Sie Docks neu drucken und die Magnete zurückbrauchen

Sie müssen die alten Docks nicht zerstören. Die mit Fotos belegte Technik besteht
darin, das Dock mit der Vorderseite nach unten auf eine Schneidematte zu legen, die
Spitze eines geraden Mini-Hakens hinter der Position des Magneten anzusetzen und
gleichmäßig durchzudrücken — PETG gibt mit wenig Kraft nach — und den Magneten dann
von der anderen Seite mit einer Zange herauszuziehen. Halten Sie die freie Hand aus
dem Weg, falls der Haken abrutscht.

Der andere berichtete Ansatz besteht schlicht darin, die Teile neu zu drucken und
frische Magnete zu kaufen und die alten als verbraucht zu betrachten.

### Bezugsquellen

Ein Besitzer, der einen Vier-Werkzeug-Satz um weitere Docks ergänzt hat, hat
Bezugsquellen für die Hardware zusammengetragen. Die Dock-Magnete sind
Neodym-Stäbchen mit 3 × 8 mm. Beim Aktivierungsmagneten im Fingerhut des Docks gehen
die Angaben auseinander. Die zuerst kursierende Größe, ein ungewöhnliches Stäbchen mit
5 × 8,47 mm, das nur sehr wenige Anbieter führen, stammte aus einem Chat-Kanal des
Herstellers und nicht aus einer Messung. Der Besitzer, der die Liste zusammengestellt
hat, maß den Magneten später in einem eingebauten Dock mit 7 × 8 mm und legte sich für
die offiziellen Druckteile auf diese Größe fest, während ein zweiter Besitzer
vermutete, der kleinere Wert gehöre zu einem anderen Satz. Ein Remix des Fingerhuts aus
der Community nimmt den 5-mm-Magneten auf und hat im Dock des Zusammenstellers
funktioniert. Messen Sie eines Ihrer eigenen Docks nach, bevor Sie bestellen. Zudem
werden zwei Federgrößen benötigt, eine große in jedem Fingerhut und zwei kleine in
jedem Halter, die beide Editionen der Anleitung als 0,5 × 8,5 × 30 × 15 und
0,63 × 5 × 15 × 11 führen. Beachten Sie, dass die Sammlung der Druckteile **für
jede Edition einen eigenen Halter für die Düsendichtung** enthält, Founders Edition und
Prusa, prüfen Sie also vor dem Drucken, welchen Sie brauchen. Für die Dichtung selbst
gibt es einen bekannten Ersatz: Besitzer in zwei Threads verweisen auf die
Ersatz-Düsendichtung des Prusa XL, deren Blatt etwas kürzer ist, in einem umgestalteten
Halter, der das ausgleicht.

Die Beschaffung ist inzwischen einfacher geworden. Der Prusa-Shop führt INDX-Bauteile
jetzt einzeln — darunter einen [Werkzeughalter mit Magneten](https://www.prusa3d.com/product/tool-holder-with-magnets-2/), einen seitlichen
Filamentsensor und das [Filamentsensor-Kabel für den INDX](https://www.prusa3d.com/product/filament-sensor-cable-for-indx/) —, und passive
Werkzeuge sollen im Shop des Herstellers vorrätig sein. Wenn Sie Docks ergänzen, prüfen
Sie den fertigen Halter, bevor Sie Magnete einzeln suchen; was genau er enthält, sollten
Sie anhand des Angebots klären. Nicht jeder würde ihn allerdings kaufen. Ein Besitzer,
bei dem sich trotz Vorschneidens von Hand zwei Schrauben in die mitgelieferten
Dock-Teile geschmolzen haben, empfiehlt, eine Community-Variante zu drucken, die
Nyloc-Muttern aufnimmt, und die Magnete selbst zu beschaffen. Ob der jetzt einzeln
verkaufte Halter dieselbe Schwäche hat, wurde nicht berichtet.

**Von vier auf acht Werkzeuge.** Ein eigener Upgrade-Satz ist nicht angekündigt. Prusas
Produktseite beschreibt die beiden Satzgrößen so, dass sie sich Smart Head und
Docking-Hardware teilen und sich nur in der Zahl der passiven Werkzeuge unterscheiden,
die sich später ergänzen lassen. Besitzer von Vier-Werkzeug-Sätzen der Founders
Edition berichten von ihren eigenen Maschinen einen weiteren Unterschied: Die Werkzeuge
fünf bis acht laufen über einen zweiten, rechten seitlichen Filamentsensor, der ihrem
Satz nicht beilag, und für die Erweiterung braucht es außerdem dessen Kabel, mehr
PTFE-Schlauch und — falls gewünscht — Spulenhalter. Dieser Sensor war das einzige
Teil, das niemand anderswo beschaffen konnte, und er gehört inzwischen zu den Teilen im
Prusa-Shop. Auch Prusas eigener Vier-Werkzeug-Satz lässt ihn weg: Prusas Anleitung
sagt Erbauern eines Vier-Werkzeug-Satzes, dass nur die linke Sensorplatine, die mit
zwei Anschlüssen, im Karton liegt, und die Anleitung zur Founders Edition sagt dasselbe
über deren Satz. Der gedruckte Block, in dem der Sensor sitzt, enthält Teile, die
schwerer zu finden sind. Die Anleitung setzt in jede Spur
eine Stahlkugel und einen Stabmagneten mit 7 × 8 mm, der auf der Kugel sitzt, dazu
Senkkopf-Magnete, die in das obere Teil des Blocks geschraubt werden:

- **Seine Senkkopf-Magnete.** Ein Besitzer hat sie mit 10 mm Durchmesser und 5 mm
  Dicke gemessen und online ein passendes Gegenstück gefunden, in einer Güte, deren
  Verhältnis zum Original unbekannt ist. Die Anleitung führt sie als Magnet 3.2 x 5 und
  nennt sie im Text des Schritts einen 5x2-Magneten; keine der beiden Bezeichnungen
  passt erkennbar zu dieser Messung, messen Sie also vor dem Bestellen nach. Ein
  zweiter Besitzer hat seither ein weiteres
  Angebot in dieser Größe gefunden, das überhaupt keine Güte angibt. Der Autor dieser
  Seite hat keine Bezugsquelle gefunden und vermutet Sonderanfertigungen; ein weiterer
  Besitzer sucht noch. Der erste Besitzer merkt an, dass der Sensor stärker von der
  Magnetstärke abhängt als das Dock, weil er mit dem Hall-Effekt arbeitet. Noch ein
  weiterer Besitzer, der nach eigener Einschätzung die Teile für eine Erweiterung in
  Eigenregie beisammen hat, hat sich Anfang Oktober 2026 bei den ringförmigen Magneten
  des Sensors (vermutlich den Senkkopf-Magneten; der Beitrag sagt es nicht) für einen
  annähernd passenden Ersatz entschieden und weiß noch nicht, ob sich der Sensor damit
  kalibrieren lässt. Dass ein Ersatz im Sensor funktioniert, hat bislang niemand
  berichtet.
- **Die Stabmagnete mit 7 × 8 mm.** Sie haben die Größe, die ein Besitzer für den
  Aktivierungsmagneten des Docks gemessen hat, und sie können schwer zu bekommen sein:
  Ein Besitzer, der im Oktober 2026 in den USA Teile suchte, fand die kleineren
  Stabmagnete des Docks online, aber keinen Stabmagneten mit 7 × 8 mm zu einem
  vernünftigen Preis, und hat sich für zwei
  gestapelte Magnete mit 7 × 4 mm an jeder Position für 7 × 8 mm entschieden, im Sensor
  ebenso wie im Fingerhut des Docks. Der bestellte Satz war bis Mitte Oktober nicht eingetroffen,
  der Stapel ist also ungetestet. *Einzelmeldung.*
- **Die schlichten Kunststoff-Abstandshalter im gedruckten Gehäuse** — nicht die
  Spannzangen, in die der PTFE-Schlauch gesteckt wird. Eine Bezugsquelle ist nicht
  bekannt. Die Anleitung führt neben den Spannzangen eine kleine Hülse je Spur mit der
  Bezeichnung 2 × 5, die diese sein könnte. Ein Besitzer ist einen anderen Weg gegangen,
  mit einem Community-Adapter, der handelsübliche PC4-M10-Steckverbinder aufnimmt und den
  PTFE-Schlauch direkt hindurchführt. *Einzelmeldung.*

!!! warning "Meldungen über einen Wechsel der Magnetgüte"
    Der Autor dieser Seite hat die ursprünglichen Dock-Magnete durch eine stärkere Güte
    ersetzt und festgestellt, dass diese die Werkzeuge fester halten; er merkt außerdem
    an, dass die ursprüngliche Güte außerhalb Europas ungewöhnlich schwer zu beschaffen
    ist. Ein zweiter Besitzer setzt die stärkere Güte, wie er in einem anderen Thread
    berichtet, in selbst gedruckten Docks ohne Probleme ein und findet, dass sie
    vielleicht etwas fester greifen — diese Magnete waren allerdings auch etwas größer
    und sitzen in einer Aufnahme, die er in der Druckdatei vergrößert hat, sodass sich
    die Wirkung der Güte aus dieser Meldung nicht herauslösen lässt. Eine
    **unabhängige Meldung unter gleichen Bedingungen gibt es nicht**. Stärkere Magnete
    verändern die Kraft, die der Mechanismus bei jedem Aufnehmen und Ablegen überwinden
    muss, und Langzeitergebnisse sind dünn: Etwa zwei Monate nach der ersten Meldung des
    Wechsels berichtet der Autor von keinen Nachteilen und davon, dass seither kein
    Werkzeug mehr unerklärlich herabgefallen ist, was weiterhin allein die Schilderung
    des Autors ist. Ein weiterer Besitzer, dem die Originalmagnete die Werkzeuge etwas
    zu locker halten, erwägt denselben Wechsel. Wenn Sie lediglich Ersatz beschaffen
    wollen, halten Sie sich an die Originalspezifikation.

## Erwartungen, die vor dem ersten Start zu klären sind

**Am Werkzeugkopf gibt es keinen Filamentsensor.** Der INDX hat ausschließlich
seitliche Sensoren, was im Firmware-Quellcode, wie für 6.9.1 veröffentlicht, bestätigt
ist; nichts in den
[Release Notes zu 7.0.0](https://help.prusa3d.com/downloads/core-one-indx) deutet auf
eine Änderung hin. In der Praxis: Das
automatische Laden funktioniert nur für das gerade aufgenommene Werkzeug, Sie führen
jedes Filament von Hand bis zum Kopf und nur das letzte kurze Stück wird eingezogen,
und es gibt **keine Verstopfungs- oder Filamentende-Erkennung am Kopf selbst**. Das
überrascht Umsteiger vom Nextruder.

**Vier- und Acht-Werkzeug-Sätze teilen sich eine Anleitung.** Schritte, die acht
PTFE-Schläuche oder acht Kabel zeigen, sind normal — ein Vier-Werkzeug-Satz nutzt die
Hälfte, und bei dieser Version führt nur eine Ader zum Sensor. Laut Anleitung darf sie
in jeden der beiden Anschlüsse der Sensorplatine.

**Vor einem Druck werden nur die Werkzeuge kalibriert, die er verwendet.** Ein Besitzer
glaubte, der Drucker prüfe vor jedem Druck jedes Werkzeug, und stellte dann fest, meist
Drucke beobachtet zu haben, die alle acht verwendeten; ein weiterer Besitzer im selben
Thread bestätigt, dass nur die Werkzeuge des Auftrags kalibriert werden. Was
der Druckstart ausführt und wann er darauf zurückfällt, jedes Werkzeug zu kalibrieren,
steht auf der [Seite zum G-Code des Profils](../gcode/indx-profile-gcode.md).
*Ein einziger Thread.*

**Nur ein Z-Motor-Anschluss wird verwendet.** Ein leerer ist zu erwarten und kein
Fehler.

**Firmware von einem USB-Stick flashen** (bei der Founders Edition dem beiliegenden,
bei Prusas Satz einem eigenen), nicht über das Netzwerk. Einige Firmware-Anweisungen
wurden aus der Anleitung des einfachen Core One übernommen und passen hier nur
schlecht.

## Wenn der erste Selbsttest fehlschlägt

Zwei Kalibrierfehler treten bei ansonsten einwandfreien Aufbauten immer wieder auf,
und beide haben eine eigene Seite:

- Ein Fehlschlag des **Heizungstests**, der eine Düsentemperatur außerhalb des
  zulässigen Bereichs meldet. Ein Erbauer hat ihn beseitigt, indem er die Kalibrierung
  mit bereits geladenem Filament erneut ausgeführt hat. Das hat eher die Form eines
  Firmware-Problems als die eines Aufbaufehlers.
- **Werkzeug-Offset außerhalb des zulässigen Bereichs**, mitunter zusammen mit einem
  instabilen Wägezellentest. Siehe
  [Werkzeug-Offset-Kalibrierung](../issues/offset-sensor-board-failure.md) und
  [Wägezellen-Rauschen](../issues/loadcell-emi-noise.md).

TODO(verify): die Temperatur, die der Heizungstest meldet, und das Akzeptanzfenster,
gegen das sie geprüft wird. Beide erscheinen im Quell-Thread und werden hier
zurückgehalten.

Die Empfehlung des Herstellers lautet, auf aktueller INDX-Firmware zu sein, die
Kalibrierung mit geladenem Filament auszuführen und — wenn sie weiterhin fehlschlägt —
mit dem vollständigen Log den Support einzuschalten, statt jedes Mal einen neuen Weg
darum herum zu finden. Die Maschine ist darauf angewiesen, dass diese Kalibrierungen
stimmen; ein Behelf an dieser Stelle rächt sich später umso mehr.

## Auf Montagefehler zurückgeführte Fehlschläge

Zwei Fehlschläge haben sich als Montagefehler erwiesen; jeweils hat der Besitzer, dem
der Fehler unterlaufen war, ihn als Ursache bestätigt:

- **X- und Y-Motorkabel am Board vertauscht.** Ein Besitzer, der sowohl den INDX als
  auch das Gen-2-Upgrade eingebaut hatte, brachte die Kalibrierungen der X- und Y-Achse
  nur mit herausgenommenen Werkzeugen zum Bestehen; mit eingesetzten Werkzeugen fuhr
  der Kopf in die angedockten Werkzeuge. Die Riemenabstimmung bestand ihre erste
  Prüfung des Portals, versuchte dann aber bei einem zweiten Durchgang, den Kopf über
  den Rahmen des Druckers hinauszufahren, und bei der Referenzfahrt zerrte der Drucker
  so lange an Werkzeug 8 in seinem Dock, bis er aufgab. Ein anderes Forumsmitglied
  schlug vor zu prüfen, welcher Motor an welcher Buchse des xBuddy-Boards steckt, und
  nachdem die beiden Kabel richtig herum gesteckt waren, lief alles einwandfrei
  ([Thread](https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/calibration-issues-from-beginning/)).
  Prusas oben beschriebener kombinierter Artikel zu INDX und Gen 2 zieht beide Kabel
  zwischendurch ab; der Besitzer sagt nicht, ob die Vertauschung dabei geschah.
- **Ein alter Heizbett-Abstandshalter wieder eingebaut.** Ein Besitzer, bei dem die
  Abtastung hinten rechts am Bett immer wieder fehlschlug, arbeitete eine lange Liste
  von Prüfungen ab, bevor er feststellte, dass er die Bett-Abstandshalter verwechselt
  und den alten statt seines Ersatzes wieder eingebaut hatte. Mit dem richtigen
  Abstandshalter funktionierte die Abtastung
  ([Thread](https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/bed-leveling-issues-3/)).

*Vorläufig.* Beides sind Einzelmeldungen, jede aus einem eigenen Thread.

## Gen 2 an einem fertigen Aufbau der Founders Edition nachrüsten

Besitzer der Founders Edition bekommen die Gen-2-Teile getrennt statt im INDX-Karton,
und manche bauen sie an eine Maschine, die schon eine Weile mit dem INDX druckt. Ein
Besitzer, der das Gen-2-Upgrade für eine solche Maschine gerade erhalten hatte, fand
keine Prusa-Anleitung, die von einem bereits umgebauten Drucker ausgeht, ein Besitzer
in einem anderen Thread sagt, dass keine erschienen ist, und ein Kommentar zu Prusas
kombiniertem Artikel sagt dasselbe. Dieser Artikel deckt nur beide Arbeiten zugleich
ab. Was Besitzer berichten, die diesem ersten
Besitzer geantwortet haben:

- **Zuerst ausschalten und vom Netz trennen.** Keine der Antworten sagt, ob der Drucker
  ausgeschaltet war, aber bei jedem der folgenden Schritte bleiben Kopf- und Motorkabel
  an der Platine angeschlossen. Arbeiten Sie daher nur bei ausgeschaltetem und vom
  Stromnetz getrenntem Drucker.
- **Der Kopf lässt sich abnehmen, ohne ihn abzustecken.** Nach dem Abnehmen des Gebläses der
  Bauteilkühlung liegen die vier Schrauben frei, die den Druckkopf halten, und das
  Hauptkabel kann angeschlossen bleiben. Das beruht allein auf der Schilderung des
  Autors dieser Seite.
- **Die Motorkabel können am Board bleiben.** Der Autor dieser Seite und ein weiterer
  Besitzer haben beide die Riemenscheiben getauscht, während die Kabel der X- und
  Y-Motoren am Board angeschlossen blieben, und beide fanden, dass die Kabel dafür genug
  Spiel haben. Der Autor legte jeden Motor dabei auf einer Stange ab; der andere
  Besitzer ließ die hintere Abdeckung montiert.
- **Die Seitenverkleidungen sind optional.** Der Autor dieser Seite weist darauf hin,
  dass eine flexible Schraubendreher-Verlängerung die Motorschrauben auch bei
  montierten Verkleidungen erreicht; ein Besitzer hat sie trotzdem abgenommen.
- **Die neuen Riemen mit den alten einziehen.** Ein Besitzer befestigte jeden neuen
  Riemen mit Klebeband am jeweils alten und zog ihn auf dem Weg des alten Riemens
  durch, solange die Motoren noch festgeschraubt waren. Derselbe Besitzer schraubte
  die Spanner vollständig heraus, um Spiel für das Befestigen der Riemenenden an der
  Montageplatte des Kopfes zu bekommen, ließ Schrauben in den losen Vierkantmuttern
  stecken — in den Spannern und in den Halterungen der Luftführung am Kopf —, damit
  keine herausfallen konnte, und fettete vor dem Wiedereinbau der Spanner deren
  Muttern, damit die Gewinde nicht fressen.
- **Die Spulenhalter wieder anbringen.** Bei abgenommenen Seitenverkleidungen lassen
  sich die Muttern für die hinteren Halter nur schwer ansetzen. Der Autor dieser Seite
  hielt jede Mutter mit einem Stück stark klebendem doppelseitigem Klebeband auf der
  Fingerspitze; zwei andere Besitzer schlugen stattdessen gedruckte Einsetzhilfen für
  Muttern vor.

*Vorläufig.* Alle obigen Schritte stammen aus einem einzigen Thread. Der Schritt zum
Abnehmen des Kopfes, der Weg mit der flexiblen Verlängerung und der Trick mit dem
Klebeband beruhen allein auf der Schilderung des Autors dieser Seite.

## Woher Dateien und Hilfe kommen

Prusa veröffentlicht die offiziellen Druckteile auf Printables. Bondtech veröffentlicht
die INDX-CAD-Daten auf GitHub statt in einem Printables-Konto, und die meisten Lehren
und Hilfsmittel aus der Community, die Sie finden werden, sind Remixe dieser CAD-Daten.

Hilfe zu Aufbau und Kalibrierung der Founders Edition leistet Bondtech, überwiegend
über seinen Discord, statt dass sie direkt beim Prusa-Support liegt. Mehrere Erbauer
berichten, der Discord sei schwer zu überblicken. Ein Beitrag im Prusa-Forum ist
ebenfalls ein gangbarer Weg — ein Community-Manager leitet Threads an die Entwickler
weiter — und ein Forenbeitrag ist später auffindbar, wie es eine Chat-Nachricht nicht
ist. Geben Sie Ihre Firmware-Version, die Anzahl der Werkzeuge und den genauen
fehlschlagenden Schritt an. Siehe
[wen Sie kontaktieren sollten](../issues/support-and-warranty-path.md) zur Aufteilung
zwischen Diagnose und Ersatzteilen, sobald der Aufbau hinter Ihnen liegt.

## Verifizierung

`reported` (mehrfach berichtet) — Montageerfahrung verteilt sich über mehrere
unabhängige Threads und viele Erbauer.

Die Hauptquelle ist
[Assembly Pain Points & Prep Notes](https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/bondtech-indx-conversion-kit-assembly-pain-points-prep-notes/),
ein Thread mit 194 Beiträgen, dessen Eröffnungsbeitrag eine Zusammenstellung aus
mehreren hundert Kommentaren zu den Schritten der offiziellen Anleitung selbst sowie
aus Forenberichten ist. Diese Zusammenstellung ist gegenüber den einzelnen Erbauern,
die die einzelnen Punkte gemeldet haben, aus zweiter Hand, bündelt aber einen weit
größeren Erfahrungsbestand, als ihn irgendein einzelner Thread hier enthält.

Die Belege für jede Aussage, Punkt für Punkt:

- **Die fehlende Liste der Verbindungselemente** wird bestätigt durch
  [Parts list for screws and bolts?](https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/parts-list-for-screws-and-bolts/),
  wo ein Erbauer danach fragt und die Auskunft erhält, dass die Anleitung
  Verbindungselemente Schritt für Schritt und sonst nirgends aufführt. Die Frage zum
  Spickzettel, die einzige Antwort darauf und die KI-erstellte Liste der Typen stehen
  alle in
  [einem Thread über die Verbindungselemente in INDX- und Gen-2-Satz](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/how-many-types-of-fasteners-etc-come-with-indx-gen2-upgrade/).
- **Die Presspassung und das Herausdrücken der Magnete** sind aus erster Hand und mit
  Fotos behandelt in
  [Removing magnets from Tool docks](https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/removing-magnets-from-tool-docks-you-dont-need-to-destroy-them/),
  von einem Erbauer, der es gemacht hat, mit zwei weiteren Besitzern, die alternative
  Vorgehensweisen beschreiben.
- **Die Beschaffung der Hardware** stammt aus
  [Sourcing tool dock hardware](https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/sourcing-tool-dock-hardware/),
  das als beantwortet markiert und von einem Besitzer zusammengestellt ist, der einen
  Vier-Werkzeug-Satz um weitere Docks ergänzt hat. Der zweite seitliche
  Filamentsensor, der Vier-Werkzeug-Sätzen der Founders Edition fehlt, und die
  XL-Düsendichtung als Ersatz werden dort und erneut in
  [einem Thread über die Erweiterung eines Vier-Werkzeug-Satzes auf acht](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/update-kit-from-indx-4t-to-8t/)
  berichtet. Keiner der beiden Threads enthält eine Meldung aus erster Hand zum Sensor
  von einem Besitzer des Vier-Werkzeug-Satzes von Prusa, doch das
  [Kapitel der Prusa-Anleitung zu den seitlichen Filamentsensoren](https://help.prusa3d.com/guide/4-indx-toolhead-side-filament-sensors_1096247)
  sagt es; dasselbe Kapitel der Anleitung zur Founders Edition sagt dasselbe über den
  Satz dieser Edition und bestätigt damit auch die Meldungen der Besitzer. Das Kapitel
  der Prusa-Anleitung ist die Quelle für Stahlkugel und Magnet mit 7 × 8 mm in jeder
  Spur, für die Hülsen und für die Bezeichnungen der Senkkopf-Magnete. Die gestapelten
  Magnete des Besitzers aus den USA erscheinen in beiden genannten Threads, vom selben
  Besitzer, und zählen daher einmal.
- **Sätze ohne Werkzeug** stützen sich auf einen einzigen Thread,
  [einen über das fehlende Werkzeug](https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/no-tools-in-my-indx-upgrade-kit/),
  der aber die eigene Aussage des Herstellers enthält: Zwei Besitzer berichten es dort,
  und ein Vertreter von Prusa bestätigt das Vorgehen und liefert die Begründung. Kein
  zweiter Thread greift es auf, doch die Einleitung beider Editionen der Anleitung sagt
  dasselbe und ist die Quelle für den Hinweis zum T10-Schraubendreher und zu montierten
  Druckern. Der einzelne
  T10-Schraubendreher im Satz der Founders Edition stützt sich nur auf die
  Zusammenstellung oben, die der Autor dieser Seite verfasst hat, und liefert daher
  keine unabhängige Bestätigung.
- **Die knappe Anleitung zum Ausbau der MMU3** wird erneut angesprochen in
  [einem Thread über die Kombination von Gen 2 und INDX](https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/core-one-to-core-onegen2-indx-upgrade-path/),
  und Besitzer in
  [einem weiteren über den Tausch einer MMU3 gegen den INDX](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/coreone-with-mmu-upgrade-to-indx/)
  beschreiben diesen Umbau als ereignislos.
- **Gen-2-Teile in den ersten Sätzen** sind eine eigene Aussage von Prusa, in seiner
  [Versandankündigung](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/prusa-indx-update-shipping-starts-this-week/),
  die zudem sagt, sie beim Einbau des INDX mit einzubauen. Zwei Besitzer im selben
  Thread raten unabhängig davon, beide Arbeiten zusammen zu erledigen. Ein Besitzer
  bestätigt in einem getrennten Thread,
  [dem über die Kombination von Gen 2 und INDX](https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/core-one-to-core-onegen2-indx-upgrade-path/),
  dass das Gen-2-Upgrade seinem INDX-Satz beilag. Die Reihenfolge der Arbeiten, die
  Motorkabel und das Schmiermittel für die Spanner sind Prusas eigene Angaben, in seinem
  [kombinierten Artikel](https://help.prusa3d.com/article/assemblling-the-prusa-indx-core-one-with-the-gen-2-upgrade_1147602),
  zu dem der Kurzlink der Ankündigung führt und der zuletzt am 15. Oktober 2026
  überarbeitet wurde; dass das Upgrade optional ist, steht in der Einleitung der
  Prusa-Anleitung. Die beiden Kommentare zu seinem Foto zum Wiedereinstecken stehen auf
  der Seite dieses Artikels selbst.
- **Die beiden Editionen und ihre Anleitungen.** Die Unterschiede darin, was Sie tun,
  stammen aus dem Vergleich der beiden Anleitungen am 18. Oktober 2026, Kapitel für
  Kapitel; die beschriebenen Schritte zu Spannern, Dock-Lüfter und Haltern der
  Düsendichtungen stehen in
  [Kapitel 4](https://help.prusa3d.com/guide/4-indx-toolhead-side-filament-sensors_1096247)
  und [Kapitel 5](https://help.prusa3d.com/guide/5-spoolholders-tool-dock-assembly_1096255)
  der Prusa-Anleitung. Die Unterschiede bei den Teilen, die Seitenverkleidung und der
  fehlgeleitete Sprungverweis stammen aus
  [einem Thread, der nach dieser Liste fragt](https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/list-of-differences-between-founders-edition-and-prusa-edition-instructions/);
  die Adapter der Düsendichtungen dort stammen vom Autor dieser Seite und werden nicht
  mitgezählt. Dass beide Sprungverweise noch auf die Anleitung zur Founders Edition
  zeigten, ist die eigene Prüfung dieser Seite an jenem Datum. Dass es für die
  mitgelieferten Werkzeughalter keinen Magnetschritt gibt, stammt aus derselben Lektüre
  beider Anleitungen.
- **Nur die Werkzeuge, die ein Druck verwendet, werden kalibriert** — das stützt sich
  auf [einen einzigen Thread](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/why-4-8-tools-tested-if-only-less-are-needed/),
  in dem sich der fragende Besitzer selbst korrigierte und ein weiterer Besitzer
  zustimmte. Der Autor dieser Seite hat dort ebenfalls geantwortet und wird nicht
  mitgezählt.
- **Ersatz-Riemenspanner** stützen sich auf zwei Besitzer in getrennten Threads, einen
  im oben verlinkten Thread über den Tausch einer MMU3 gegen den INDX und einen im
  Thread zur Versandankündigung von Prusa. Derselbe Rat erscheint in letzterem auch vom
  Autor dieser Seite und wird nicht mitgezählt.

Schwächer: Die Bootloader-Sperre des MK4S ist die Erfahrung eines einzelnen Besitzers
und an Ort und Stelle als solche gekennzeichnet. Sie stammt aus dem allgemeinen
Diskussions-Thread, in dem es überwiegend um Versand und Bestellungen geht — sie wurde
beim Lesen aller 1534 Beiträge gefunden und ist einer von nur zwei belastbaren
technischen Punkten, die aus diesem gesamten Thread die Prüfung überstanden haben.
Ebenfalls Einzelmeldungen und an Ort und Stelle gekennzeichnet: die Riemeneinstellung
nach dem ersten Flashen, der montiert gelieferte Drucker ohne Werkzeug, die in
Dock-Teile geschmolzenen Schrauben, der Behelf für die Abstandshalter im Sensorgehäuse,
die Messung der Senkkopf-Magnete zusammen mit den beiden Angeboten, die in dieser
Größe gefunden wurden, und dem annähernd passenden Magneten, dessen Test noch aussteht,
sowie beide Montagefehler, jeder aus einem eigenen Thread. Die Größe des
Aktivierungsmagneten beruht auf der Messung eines Besitzers gegenüber einem Wert, den
niemand gemessen hat. An welche Stelle der INDX-Abfolge die Gen-2-Teile gehören, legt
inzwischen Prusa selbst im kombinierten Artikel fest; die frühere Praxis des Autors
dieser Seite liegt nahe daran, ist aber kein Beleg. Das Weglassen des
Düsenabstreifers ist die Praxis des Autors, die der Artikel weder bestätigt noch
widerlegt, und hat eine unabhängige Stimme, in
[einem anderen Thread](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/bondtech-founders-edition-upgrade-path-to-core-one-gen-2/).
Die Hinweise zum Nachrüsten von Gen 2 an einem fertigen Aufbau der Founders Edition
stammen alle aus
[einem Thread über diese Nachrüstung](https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/indx-fe-upgrading-to-gen2/):
Der Schritt zum Abnehmen des Kopfes, der Weg mit der flexiblen Verlängerung bei
montierten Seitenverkleidungen und der Klebeband-Trick für die Muttern der Spulenhalter
stammen allein vom Autor dieser Seite, das Spiel der
Motorkabel hat neben dem Autor einen unabhängigen Besitzer, und die Hinweise zu Riemen,
Vierkantmuttern und Spannern stammen von einem einzelnen Besitzer. Dass Besitzer der
Founders Edition die Gen-2-Teile getrennt kaufen, steht dort und in dem unmittelbar
zuvor verlinkten Thread. Dass Prusa keine Anleitung hat, die von einem umgebauten
Drucker ausgeht, steht dort, im Thread über die Unterschiede zwischen den Editionen und
in einem Kommentar zu Prusas kombiniertem Artikel.
Der Wechsel der Magnetgüte wurde zuerst vom Autor dieser Seite gemeldet, und eine
unabhängige Schilderung unter gleichen Bedingungen gibt es nicht: Der einzige weitere
Besitzer, der ihn meldet, hat neben der Güte auch die Magnetgröße geändert. Die
Rückmeldung des Autors nach zwei Monaten und der Besitzer, der den Wechsel erwägt,
stehen beide im
[Thread über das Entfernen der Dock-Magnete](https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/removing-magnets-from-tool-docks-you-dont-need-to-destroy-them/).
Das kursierende inoffizielle PDF
zu den Verbindungselementen wurde von der Person, die es geteilt hat, als KI-generiert
und ungeprüft beschrieben und ist hier nur als etwas festgehalten, dem Sie begegnen
können, nicht als Quelle, auf die man sich stützen sollte.

Diese Seite gibt die Schrittfolge der offiziellen Anleitung bewusst **nicht** wieder.
Sie hält fest, wo Erbauer hängen geblieben sind — der Teil, den die Anleitung Ihnen
nicht sagen kann.

## Verwandt

- [Werkzeug-Offset-Kalibrierung schlägt fehl](../issues/offset-sensor-board-failure.md) —
  der häufigste Fehlschlag beim ersten Start
- [Antasten schlägt fehl oder die Düse berührt das Bett nie](../issues/loadcell-emi-noise.md) —
  wenn der Wägezellentest ab Werk instabil ist
- [Dock-Kalibrierung lehnt einige oder alle Docks ab](../issues/dock-calibration-rejects-docks.md) —
  wenn die Dock-Kalibrierung an einem frisch aufgebauten Drucker scheitert; prüfen Sie
  zuerst die Riemeneinstellung
- [Input-Shaper-Kalibrierung bricht mit „Measurement failed“ ab](../issues/input-shaper-measurement-failed.md)
  — wenn die Input-Shaper-Kalibrierung direkt nach der Kalibrierung des
  Beschleunigungssensors scheitert; prüfen Sie zuerst die Riemeneinstellung
- [Wen Sie kontaktieren sollten](../issues/support-and-warranty-path.md) — Weiterleitung
  bei Support und Garantie
