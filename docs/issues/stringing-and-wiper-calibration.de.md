---
title:        In den Druck geschleppte Blobs — Düsenwischer und Spülvorgang
confidence:   reported
updated:      2026-08-24
author:       hyiger
printer:      Core One
toolhead:     INDX
hotend:       unknown
nozzle:       0.4mm reported
firmware:     6.9.0; earlier behavior noted throughout
sources:
  - https://help.prusa3d.com/downloads/core-one-indx
  - https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/nozzle-cleaning-calibration-issues/
  - https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/nozzle-wiper-vs-indx-offset-sensor/
  - https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/a-summary-of-common-indx-problems/
superseded_by:
source_sha:   e4d6558aac0aac18bb1aadef8fb6ee98b53954ff554b9ed098abbae81c1aeab0
---
# In den Druck geschleppte Blobs — Düsenwischer und Spülvorgang

!!! tip "Vor allem anderen auf 6.9.0 aktualisieren"
    Firmware 6.9.0 hat die **automatische Kalibrierung des Düsenreinigers** eingeführt —
    das ist in Prusas eigenen Release Notes bestätigt und nicht nur aus Anwenderberichten
    abgeleitet. Dieselbe Version hat den Spülpunkt in Y verschoben und lässt die Düse im
    Reiniger wieder aufheizen, wenn ein Druck fortgesetzt wird. Anwender beschreiben
    zusätzlich einen überarbeiteten Wischpfad und geänderte Spülmengen.

    Drei Anwender berichten unabhängig voneinander von einem dramatischen Unterschied —
    saubere Werkzeugwechsel über Drucke mit gemischten Materialien hinweg, einer braucht
    keinen Brim mehr, um Verunreinigungen in der ersten Schicht aufzufangen, und — am
    aussagekräftigsten — der Anwender, der den ursprünglichen Beschwerde-Thread eröffnet
    hat, berichtet, dass 6.9.0 sowohl das Ausschwitzen als auch die Reinigung weitgehend
    beruhigt hat.

    Der größte Teil des unten beschriebenen manuellen Vorgehens existiert nur, weil diese
    Kalibrierung früher von Hand erledigt wurde, schlecht und ohne jede Möglichkeit zu
    sehen, was man tut. Wenn Sie 6.9.0 oder neuer einsetzen, aktualisieren Sie und testen
    Sie erneut, bevor Sie Zeit in manuelle Ausrichtung investieren.

## Zusammenfassung

Auf Firmware vor 6.9.0 war die häufigste Beschwerde über die Druckqualität des INDX,
dass Filament aus dem Spülbereich herausgeschleppt und auf dem Druck abgelegt wird —
Blobs, Pickel und Fäden, die zu Druckbeginn und bei Werkzeugwechseln auftreten. Die
Ursache ist meist nicht das Filament: Es ist die Position der Düse relativ zum
Silikon-Wischblock während des Spülens. Dass sie *im* Spülmaterial sitzt statt frei
davon, ist der Grund, weshalb ein Blob an der Düse haften bleibt und auf das Werkstück
mitfährt.

## Details

### Was tatsächlich passiert

Bei einem Werkzeugwechsel spült der Kopf in den Behälter und zieht sich dann auf dem Weg
zum Werkstück am Silikonblock an der Vorderseite vorbei zurück. Anwender beschreiben
durchgängig denselben Ablauf: Das Spülen findet statt, die Düse schleppt auf dem Rückweg
einen Teil davon mit, sitzt kurz darin und trägt es dann auf das Druckblech. Es zeigt
sich beim ersten Werkzeug eines Drucks und erneut bei den folgenden Wechseln.

Die Abhängigkeit vom Material schließt eine einzelne einfache Ursache aus. PLA-Drucke
kommen oft sauber durch, PETG und ABS nicht. Ausschwitzen erklärt den PETG-Fall
plausibel, aber ein Anwender wies ausdrücklich darauf hin, dass auch ABS Blobs bildet,
was Ausschwitzen allein nicht erklärt — die Haftung des Spülmaterials an der Düsenwand
ist ebenso wichtig wie die Menge, die ausschwitzt.

### Die Pellets lesen — die beste Diagnose auf dieser Seite

Die Form des verworfenen Spülmaterials zeigt Ihnen, wo Sie stehen, ganz ohne Messung:

- **Kompakte Pellets in Reiskorngröße** — das klassische „gute“ Ergebnis.
- **Lange Würmer, Kaulquappen oder aneinanderhängende Stränge** — das Spülmaterial zieht
  sich in die Länge, statt sauber abzureißen.

Eine kleine Änderung der Y-Position kippt zwischen diesen beiden Ergebnissen. Diese
Empfindlichkeit ist das Nützlichste, was man vor dem Justieren wissen kann, denn sie
bedeutet, dass Sie ein schmales Fenster suchen und kein breites.

TODO(verify): die Größenordnung der Y-Anpassung, die ein Anwender als Unterschied
zwischen Reiskörnern und Würmern angegeben hat. Sie liegt bei einem kleinen Bruchteil
eines Millimeters und ist maschinenspezifisch, wird hier also zurückgehalten statt als
Zielwert veröffentlicht.

!!! note "Welche Pelletform tatsächlich besser ist, ist umstritten"
    Die Community-Wissensdatenbank hat den Wechsel von kompakten Pellets zu
    fadenförmigen Enden aus der 6.6.2-Zeit als Rückschritt festgehalten. Ein Anwender im
    Forum-Thread argumentierte später gegenteilig — Würmer könnten Absicht gewesen sein,
    weil ein Wurm die Düse davon abhält, sich in die Oberseite eines Blobs zu setzen,
    sich leichter löst und weniger Schaden anrichtet, wenn er doch auf den Druck gelangt.
    Beide Lesarten stehen in den Quellen. Behandeln Sie die Pelletform als *empfindlichen
    Hinweis darauf, dass sich Ihre Ausrichtung verändert hat*, was sie mit Sicherheit
    ist, und nicht als Zielgröße, auf die hin optimiert wird.

### Die eigentliche Schwierigkeit ist, dass man es nicht sehen kann

Anwender sind sich einig, dass die Schwierigkeit in der Sicht liegt, nicht in der
Beurteilung. Der Wischer sitzt an einer Stelle, die man während des Spülens nicht
einsehen kann, und Anwender haben zu Zahnarztspiegeln gegriffen. Zwei Techniken sind im
Umlauf:

- **Von hinten beleuchten.** Stellen Sie eine Lichtquelle hinter den Behälter und
  justieren Sie, bis das Licht gerade eben hinter der Düse verschwindet. Das ergibt eine
  wiederholbare visuelle Referenz dort, wo direkte Beobachtung keine liefert.
- **Während eines Drucks justieren.** Ab 6.6.3 gibt es im Tune-Menü des Druckers den
  Eintrag *Nozzle Cleaner Y Offset*, der bei laufendem Druck erreichbar ist, sodass Sie
  die Position ändern und die Wirkung sofort am nächsten Pellet sehen können. Frühere
  Firmware bot die X- und Y-Reinigungsoffsets auf dieselbe Weise an. Beachten Sie, dass
  diese nur während eines Drucks erreichbar sind, was Absicht ist — man braucht einen
  laufenden Druck, um überhaupt etwas beurteilen zu können.

TODO(verify): Richtung und Größenordnung eines brauchbaren Nozzle Cleaner Y Offset.
Dieser Wert ist tatsächlich maschinenspezifisch — die Community-Wissensdatenbank hält
fest, dass Anwender mit Offsets in **entgegengesetzten Richtungen** Erfolg melden, es
gibt also keinen korrekten Wert zu veröffentlichen. Ermitteln Sie Ihren eigenen anhand
der Pelletform.

### Tiefer als man denkt

Die nützlichste Erkenntnis aus der Zeit vor 6.9.0, und die mit der klarsten Bestätigung
aus erster Hand, betrifft Z und nicht Y. Die Arbeitsposition liegt **tief** — die Düse
steckt tatsächlich im Silikon, statt es nur leicht zu streifen.

Ein Anwender schloss, dass ein Vergraben der Düse im Silikon diese abdichtet und die
Bildung eines abschließenden Blobs verhindert, testete es und meldete zurück, dass das
seine ABS-Blobbildung **vollständig behoben** hat — beim ersten Werkzeug ebenso wie bei
jedem späteren Wechsel. Die Community-Wissensdatenbank hält unabhängig davon einen
systematischen Höhentest fest, der zum selben Ergebnis kommt: Die Arbeitsposition liegt
tiefer als die Faustregel vom leichten Kontakt, die viele annehmen.

Wenn Sie von Hand kalibrieren, irren Sie lieber zu tief als zu flach.

TODO(verify): der nominale Spaltwert, dem diese Erkenntnis widerspricht, sowie jede
gemessene Tiefe. Beides wird hier nicht veröffentlicht — die handlungsrelevante Form ist
eine Richtungsangabe („tiefer als nur berührend“), die keine Zahl benötigt.

!!! warning "Eine offene Frage zur automatischen Kalibrierung"
    Vor dem Erscheinen von 6.9.0 äußerte ein Anwender die Sorge, dass eine automatische
    Routine, die auf *gerade eben berührend* kalibriert, genau die Blobbildung
    wiederherstellen könnte, die das Vergraben der Düse behoben hatte. Frühe Berichte zu
    6.9.0 sind gut und zeigen das nicht, aber niemand hat bestätigt, auf welche Tiefe die
    automatische Routine tatsächlich abzielt. Wenn Sie aktualisieren und die Blobbildung
    zurückkehrt, nachdem sie zuvor durch mehr Tiefe behoben war, ist das der erste
    Verdacht.

### Behelfslösungen ohne Kalibrierung

- **Drucken Sie einen Skirt oder Brim.** Mehrere Anwender berichten, dass das die
  anfänglichen Verunreinigungen auffängt, bevor sie das Werkstück erreichen. Es ist die
  billigste Abhilfe, und beim Anwender, der den Haupt-Thread eröffnet hat, hat sie
  funktioniert. Einer merkt an, dass sich Brims mühsam vom Druckblech lösen lassen.
- **Verwenden Sie einen Reinigungsturm statt des Spülbehälters.** Der G-Code für den
  Werkzeugwechsel verzweigt danach, ob ein Reinigungsturm verwendet wird, sodass ein
  Reinigungsturm die Sequenz der Spülstation vollständig umgeht. Ein Anwender druckte
  einen durch Blobs verdorbenen ABS-Auftrag mit einem minimalen Reinigungsturm erneut
  und berichtete, er sei sehr sauber geworden, bei geringfügig längerer Druckzeit.

    Der Kompromiss hängt vom Material ab und lohnt es, richtig getroffen zu werden: Ein
    Reinigungsturm eignet sich für mehrere Farben **desselben** Materials, wo es nur
    darum geht, den Fluss zu stabilisieren. Bei **unterschiedlichen** Materialien, die
    nicht miteinander verbinden, hat der Spülbehälter den klaren Vorteil, denn ein Turm
    aus Materialien, die nicht aneinander haften, fällt auseinander.

    TODO(verify): das reduzierte Spülvolumen, das für den minimalen Reinigungsturm
    verwendet wurde, und der Standardwert, von dem aus es reduziert wurde. Das sind
    Slicer-Einstellungen und werden zurückgehalten.

- **Ergänzen Sie periodische Wischvorgänge** bei Drucken mit nur einer Düse und bei
  klebrigen Filamenten.

### Bevor Sie den Wischer verantwortlich machen

- **Schließen Sie zuerst Ausschwitzen und Fehler beim Antasten aus.** Wenn sich Material
  beim Antasten statt bei Werkzeugwechseln ansammelt, siehe
  [Ausschwitzen beim Antasten und Kalibrieren](oozing-during-probing-and-calibration.md).
- **Prüfen Sie, ob der Silikonblock fest montiert ist.** Wenn er sich beim Reinigen
  leicht verschiebt, bleibt keine noch so gute Kalibrierung konsistent.
- **Wenn die Ergebnisse zwischen den Werkzeugen uneinheitlich sind**, verdächtigen Sie
  eher die Werkzeug-Offsets als den Wischer — Werkzeuge, die geringfügig unterschiedlich
  zum Block zum Stehen kommen, erzeugen genau dieses Symptom. Siehe
  [Werkzeug-Offset-Kalibrierung](offset-sensor-board-failure.md).
- **Trocknen Sie das Filament.** Der INDX gilt Berichten zufolge als
  feuchtigkeitsempfindlicher als der Nextruder, den er ersetzt.

### Temperaturen, Retraktion und Fluss

In der Community besteht Einigkeit, dass mehrere Werte der Standardprofile nicht gut zur
High-Flow-Düsengeometrie dieses Werkzeugkopfs passen, die Wärme effizienter überträgt als
das, was viele Anwender bisher gewohnt sind — die allgemeine Richtung ist daher kühler
statt heißer, bei Retraktionswerten, die stark maschinenspezifisch sind.

**Auf dieser Seite erscheinen keine Werte.** Jede Temperatur, jede Retraktionsdistanz,
jeder Extrusionsmultiplikator und jeder Pressure-Advance-Wert, der in den Quellen
besprochen wird, wird zurückgehalten, bis er auf Hardware verifiziert ist.

TODO(verify): Standard-Temperaturbereiche gegenüber den von der Community bevorzugten je
Material; Retraktionsbereiche und die Profilstandards, von denen sie abweichen; der
reduzierte Extrusionsmultiplikator, der für mindestens ein gefülltes Material berichtet
wird; und die nach Düsendurchmesser aufgeschlüsselte Pressure-Advance-Tabelle, die als
Start-G-Code-Schnipsel kursiert. Genau diese Zahlen richten Schaden am Drucker eines
Fremden an, wenn sie falsch sind, und sie sind der Grund, weshalb dieser Abschnitt
bewusst leer ist.

## Verifizierung

`reported` (gemeldet) — mehrere unabhängige Anwender, in zwei eigenen Threads, über rund
einen Monat Firmware-Änderungen hinweg, wobei das Firmware-Verhalten selbst
herstellerseitig bestätigt ist.

Die Änderungen in 6.9.0 sind in
[Prusas eigenen Release Notes](https://help.prusa3d.com/downloads/core-one-indx)
dokumentiert, die die automatische Kalibrierung des Düsenreinigers, die Verschiebung des
Spülpunkts und das Wiederaufheizen der Düse beim Fortsetzen benennen. Das hebt die
Kernaussage dieser Seite von einer Schlussfolgerung der Anwender auf eine vom Hersteller
dokumentierte Tatsache.

Die Hauptquelle ist
[Probleme bei Düsenreinigung und -kalibrierung](https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/nozzle-cleaning-calibration-issues/),
ein Thread mit 58 Beiträgen und neun Teilnehmern von Ende Juli bis Ende August 2026. Er
enthält die Symptomberichte, die Klagen über die fehlende Sicht, die Anpassungen im
Tune-Menü, das Reinigungsturm-Experiment und das Ergebnis unter 6.9.0.

Die Verbesserung durch 6.9.0 ist von drei Anwendern **unabhängig bestätigt**: Einer
berichtet von sauberen Werkzeugwechseln bei einem gemischten TPU/PETG-Druck und erneut
bei einem vierfarbigen PETG-Druck; ein zweiter berichtet separat, das Ergebnis sei
deutlich sauberer und er brauche keinen Brim mehr, um Verunreinigungen aufzufangen; und
der Anwender, der den Thread eröffnet hat — die Person mit dem schwersten Fall — hat
seither bestätigt, dass 6.9.0 das Ausschwitzen und die Reinigung für ihn weitgehend
gelöst hat. Der letzte davon ist der stärkste einzelne Datenpunkt auf dieser Seite, weil
hier der ursprüngliche Beschwerdeführer seinen eigenen Bericht abschließt. Das ist die
stärkste Aussage auf dieser Seite.

Die Erkenntnis „die Düse vergraben“ stammt aus
[Düsenwischer vs. INDX-Offset-Sensor](https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/nozzle-wiper-vs-indx-offset-sensor/),
wo ein Anwender die Hypothese aufstellt, sie testet und das bestätigte Ergebnis im selben
Thread meldet — Hypothese und Ergebnis von derselben Person, was schwächer ist als zwei
unabhängige Berichte, aber stärker als eine unbelegte Behauptung. Die
[Zusammenfassung häufiger Probleme](https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/a-summary-of-common-indx-problems/)
hält einen separaten systematischen Höhentest fest, der zum selben Ergebnis kommt.

Wo die Quellen sich widersprechen: ob die Änderung der Pelletform ein Rückschritt oder
eine beabsichtigte Verbesserung war, wie im Text vermerkt. Die Quellen stehen einander
direkt entgegen, und keine von beiden ist bestätigt.

Ausdrücklich **nicht** auf diese Seite übernommen: eine Behauptung im Thread, dass die
Einstellung für das Mindestspülvolumen des Reinigungsturms trotz ihres Namens auch das
Volumen des Spülbehälters steuert. Der Anwender, der sie gepostet hat, sagte offen, dass
er sie mit einem KI-Assistenten nachvollzogen und nicht die Firmware gelesen habe, und
riet den Lesern, sie mit Vorsicht zu genießen. Sie wird hier als Hinweis zum Nachprüfen
festgehalten, nicht als Handlungsempfehlung.

Ebenfalls nicht übernommen: ein Problem mit dem dynamischen Lüfterprofil für Überhänge,
das in der Community-Wissensdatenbank beschrieben wird. Es taucht in keinem anderen
Thread des Forum-Korpus auf, und es ist ein Kühlungsproblem und keines des Wischers — es
gehört auf eine eigene Seite mit `provisional`, wenn jemand es bestätigen kann.

## Verwandte Seiten

- [Ausschwitzen verdirbt Bett-Antastung und Werkzeugkalibrierung](oozing-during-probing-and-calibration.md)
  — Material am falschen Ort, aber beim Antasten statt bei Werkzeugwechseln
- [Werkzeug-Offset-Kalibrierung schlägt fehl](offset-sensor-board-failure.md) — die
  Ursache, die zu vermuten ist, wenn die Wischerergebnisse zwischen den Werkzeugen
  abweichen
- [Phantom-Werkzeuge und Fehler beim Ablegen](tool-detection-ringdown-decay.md) — der
  andere Bereich, den 6.9.0 verändert hat, dort möglicherweise zum Schlechteren
- [Diagonale Streifenbildung über Druckwände hinweg](diagonal-banding.md) — die andere
  Seite zur Druckqualität. Wenn Ihr Defekt ein regelmäßiges Muster auf den Wänden ist und
  keine einzelnen Blobs, die auf dem Werkstück landen, liegt es am Extruder und nicht am
  Wischer.
- [Werkzeugkopf kollidiert mit fertigen Teilen](complete-individual-objects-collision.md)
  — ebenfalls Schaden rund um einen Werkzeugwechsel, aber mechanisch statt
  materialbedingt. Wenn Teile angestoßen oder aufgerissen statt verschmutzt werden, lesen
  Sie stattdessen dort.
