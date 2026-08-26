---
title:        Montagehinweise — INDX-Umbausatz
confidence:   reported
updated:      2026-08-24
author:       hyiger
printer:      Core One, Core One Plus
toolhead:     INDX
hotend:       unknown
nozzle:       unknown
firmware:     unknown
sources:
  - https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/bondtech-indx-conversion-kit-assembly-pain-points-prep-notes/
  - https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/sourcing-tool-dock-hardware/
  - https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/removing-magnets-from-tool-docks-you-dont-need-to-destroy-them/
  - https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/parts-list-for-screws-and-bolts/
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/update-kind-of/
superseded_by:
source_sha:   42305582293e9b681ff6d026e968b0f73396c5cb6c3b6219a3038453a4d462bf
---
# Montagehinweise — INDX-Umbausatz

!!! info "Dies ergänzt die offizielle Anleitung, es ersetzt sie nicht"
    Bauen Sie nach der
    [offiziellen Bondtech-INDX-Umbauanleitung](https://help.prusa3d.com/manual/bondtech-indx-conversion-kit-for-the-prusa-core-one-founders-edition_2397).
    Was folgt, ist die gesammelte Erfahrung von Erbauern, die den Umbau hinter sich
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
  Einpresslehre für die Dock-Magnete.
- Ein **großes Stück Karton**, auf das Sie den Drucker stellen, damit Sie ihn während
  der unhandlichen Schritte frei drehen und kippen können.

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

## Tücken beim Lieferumfang

**Zu geringe Stückzahlen bei Verbindungselementen sind die mit Abstand häufigste
Beschwerde.** Mehr als ein Beutel wurde mit weniger Schrauben ausgeliefert, als sein
Etikett angibt, und mindestens ein Schritt verlangt mehr, als mehrere Erbauer erhalten
haben. Manche mussten selbst beschaffen oder zuschneiden. Das ist der Grund für das
Schraubensortiment weiter oben — mitten im Schritt auszugehen ist der Unterschied
zwischen einem Abend und einem Wochenende.

**Es gibt keine zusammengefasste Liste der Verbindungselemente.** Verbindungselemente
sind in der Anleitung Schritt für Schritt aufgeführt und sonst nirgends; wer gern in
beschriftete Fächer vorsortiert, muss sich diese Liste selbst herausschreiben. Im
Forum kursiert ein inoffizielles PDF zu den Verbindungselementen, es war jedoch
KI-generiert und von seinem eigenen Verfasser nicht überprüft — behandeln Sie es als
Ausgangspunkt für den Abgleich mit der Anleitung, nicht als Stückliste.

**„Alle Werkzeuge enthalten“ bedeutet etwas Bestimmtes.** Wenn auf Ihrem Tisch bereits
ein fertig aufgebauter Core One steht, kamen die benötigten Werkzeuge mit ihm. Im
Karton des Umbausatzes liegt nur der T10-Schraubendreher.

**MMU3-Besitzer:** Die Einheit muss zuerst herunter, und die Anleitung behandelt den
Ausbau kaum. Planen Sie ihn als eigene Aufgabe ein, bevor Sie den eigentlichen Umbau
beginnen.

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
jeden. Schon das Ansetzen in den Startbohrungen fällt schwer, und einen Magneten
vollständig zu setzen erfordert echte, gerichtete Kraft. Planen Sie nicht damit, das
von Hand zu schaffen. Erbauer verwenden eine Einhandzwinge oder eine gedruckte
Einpresslehre.

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
Neodym-Stäbchen mit 3 × 8 mm; der Aktivierungsmagnet ist ein ungewöhnliches Stäbchen
mit 5 × 8,47 mm, das offenbar nur von sehr wenigen Anbietern zu bekommen ist. Zudem
werden zwei Federgrößen benötigt. Beachten Sie, dass die Sammlung der Druckteile
**zwei verschiedene Halter für die Düsendichtung** enthält — einen für die Founders
Edition und einen für die Prusa-Version —, prüfen Sie also vor dem Drucken, welchen
Sie brauchen.

!!! warning "Eine Meldung über einen Wechsel der Magnetgüte"
    Ein Besitzer berichtet, die Originalmagnete durch eine stärkere Güte ersetzt zu
    haben, und dass diese die Werkzeuge fester halten; er merkt außerdem an, dass die
    ursprüngliche Güte außerhalb Europas ungewöhnlich schwer zu beschaffen sei. Das
    ist eine **Einzelmeldung**. Stärkere Magnete verändern die Kraft, die der
    Mechanismus bei jedem Aufnehmen und Ablegen überwinden muss, und
    Langzeitergebnisse hat niemand berichtet. Wenn Sie lediglich Ersatz beschaffen
    wollen, halten Sie sich an die Originalspezifikation.

## Erwartungen, die vor dem ersten Start zu klären sind

**Am Werkzeugkopf gibt es keinen Filamentsensor.** Der INDX hat ausschließlich
seitliche Sensoren, was im Firmware-Quellcode bestätigt ist. In der Praxis: Das
automatische Laden funktioniert nur für das gerade aufgenommene Werkzeug, Sie führen
jedes Filament von Hand bis zum Kopf und nur das letzte kurze Stück wird eingezogen,
und es gibt **keine Verstopfungs- oder Filamentende-Erkennung am Kopf selbst**. Das
überrascht Umsteiger vom Nextruder.

**Vier- und Acht-Werkzeug-Sätze teilen sich eine Anleitung.** Schritte, die acht
PTFE-Schläuche oder acht Kabel zeigen, sind normal — ein Vier-Werkzeug-Satz nutzt die
Hälfte, und bei dieser Version führt nur eine Ader zum Sensor.

**Nur ein Z-Motor-Anschluss wird verwendet.** Ein leerer ist zu erwarten und kein
Fehler.

**Firmware vom USB-Stick flashen**, nicht über das Netzwerk. Einige
Firmware-Anweisungen wurden aus der Anleitung des einfachen Core One übernommen und
passen hier nur schlecht.

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

Unabhängig bestätigt:

- **Die fehlende Liste der Verbindungselemente** wird bestätigt durch
  [Parts list for screws and bolts?](https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/parts-list-for-screws-and-bolts/),
  wo ein Erbauer danach fragt und die Auskunft erhält, dass die Anleitung
  Verbindungselemente Schritt für Schritt und sonst nirgends aufführt.
- **Die Presspassung und das Herausdrücken der Magnete** sind aus erster Hand und mit
  Fotos behandelt in
  [Removing magnets from Tool docks](https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/removing-magnets-from-tool-docks-you-dont-need-to-destroy-them/),
  von einem Erbauer, der es gemacht hat, mit zwei weiteren Besitzern, die alternative
  Vorgehensweisen beschreiben.
- **Die Beschaffung der Hardware** stammt aus
  [Sourcing tool dock hardware](https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/sourcing-tool-dock-hardware/),
  das als beantwortet markiert und von einem Besitzer zusammengestellt ist, der einen
  Vier-Werkzeug-Satz um weitere Docks ergänzt hat.

Schwächer: Der Wechsel der Magnetgüte und die Bootloader-Sperre des MK4S sind jeweils
die Erfahrung eines einzelnen Besitzers, und beide sind an Ort und Stelle als solche
gekennzeichnet. Die Sperre stammt aus dem allgemeinen Diskussions-Thread, in dem es
überwiegend um Versand und Bestellungen geht — sie wurde beim Lesen aller 1534
Beiträge gefunden und ist einer von nur zwei belastbaren technischen Punkten, die aus
diesem gesamten Thread die Prüfung überstanden haben. Das kursierende inoffizielle PDF
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
- [Wen Sie kontaktieren sollten](../issues/support-and-warranty-path.md) — Weiterleitung
  bei Support und Garantie
