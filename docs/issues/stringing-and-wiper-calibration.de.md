---
title:        In den Druck geschleppte Blobs — Düsenwischer und Spülvorgang
confidence:   reported
updated:      2026-09-25
author:       hyiger
printer:      Core One
toolhead:     INDX
hotend:       unknown
nozzle:       0.4mm reported
firmware:     6.9.0, re-checked against 6.9.1; earlier behavior noted throughout
sources:
  - https://help.prusa3d.com/downloads/core-one-indx
  - https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/nozzle-cleaning-calibration-issues/
  - https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/nozzle-wiper-vs-indx-offset-sensor/
  - https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/a-summary-of-common-indx-problems/
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.9.1-beta
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.9.1
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/compare/v6.9.1-beta...v6.9.1
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5391
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5496
superseded_by:
source_sha:   bdb833895697dfc21ea46c578ca2c428d3d2e464f5afe3e2df3e7f16659ac7e5
---
# In den Druck geschleppte Blobs — Düsenwischer und Spülvorgang

!!! tip "Vor allem anderen auf 6.9.0 oder neuer aktualisieren"
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
    beruhigt hat. Dabei blieb es nicht. Wochen später, noch auf 6.9.0, schlug beim
    selben Anwender ein Druck mit einem anderen Filament fehl, und danach ließ sich die
    Werkzeugkalibrierung nicht mehr bestehen, was für ihn neu war; nachdem er die
    Maschine zurückgesetzt und jedes Werkzeug neu kalibriert hatte, war auch das
    Ausschwitzen wieder da. Anschließend bestanden nach seinem Bericht alle
    Kalibrierungen auf einem 6.9.1-Build, ohne dass klar wurde, auf welchem; Prusas 6.9.1
    lag zu diesem Zeitpunkt nur als Beta vor. Siehe
    [Werkzeug-Offset-Kalibrierung](offset-sensor-board-failure.md).

    Der größte Teil des unten beschriebenen manuellen Vorgehens existiert nur, weil diese
    Kalibrierung früher von Hand erledigt wurde, schlecht und ohne jede Möglichkeit zu
    sehen, was man tut. Wenn Sie etwas Älteres als 6.9.0 einsetzen, aktualisieren Sie und
    testen Sie erneut, bevor Sie Zeit in manuelle Ausrichtung investieren.

    Die Release Notes der stabilen Version 6.9.1 nennen keine Änderung am Wischer oder am
    Spülvorgang. Die Beta hat für den Reiniger eine Sache geändert: Das Bett fährt während
    der Nozzle-Cleaner-Kalibrierung gegebenenfalls nach unten und lässt Platz für eine
    Hand oder einen Schraubenschlüssel. Die Notes der stabilen Version wiederholen das
    nicht, aber die stabile Version baut auf der Beta auf: Im Firmware-Repository fügt sie
    dem Beta-Tag
    [15 Commits](https://github.com/prusa3d/Prusa-Firmware-Buddy/compare/v6.9.1-beta...v6.9.1)
    hinzu, von denen keiner den Düsenreiniger betrifft. Das ergibt sich aus der
    Release-Historie, nicht aus den Notes. Auf einem 6.9.1-Build fand ein Anwender PLA,
    das zu langen Fäden ausgezogen an der Düse hing, woraufhin das Antasten der Düsen
    scheiterte; mit 6.9.0 lief es anscheinend besser, er vermutete aber seine
    eigene Wischereinstellung oder einen Fehler der Wägezelle. Ein zweiter Anwender, auf
    der Beta, fand nach dem Wischen noch PETG an der Düse, genug, um die
    Bettnivellierung scheitern zu lassen, rechnet der Beta aber an, die meisten seiner
    PETG-Kalibrierprobleme behoben zu haben. Beides sind Einzelberichte. Zu Fehlern beim
    Antasten allgemein siehe
    [Ausschwitzen beim Antasten und Kalibrieren](oozing-during-probing-and-calibration.md).

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
    Beide Lesarten stehen in den Quellen. Ein späterer Bericht liefert einen weiteren
    Datenpunkt, ohne die Frage zu entscheiden: Bei demselben Anwender, der im Warnkasten
    weiter unten zitiert wird, kam das Spülmaterial als aneinandergereihte Würmer heraus,
    und einige davon landeten auf dem Bett. Behandeln Sie
    die Pelletform als *empfindlichen Hinweis darauf, dass sich Ihre Ausrichtung verändert
    hat*, was sie mit Sicherheit ist, und nicht als Zielgröße, auf die hin optimiert wird.

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

    Ein späterer Anwender, Firmware nicht angegeben, berichtet von Problemen durch zu wenig
    Kontakt. Beim Vorspülen blieb Material an der Rückseite seiner Düse hängen und fiel
    während des Drucks auf das Bett; nachdem er die Höhe des Wischers so eingestellt hatte,
    dass er die Düse sicher berührte, verlief zumindest das Vorspülen sauber, und jede neue
    Kalibrierung des Wischers brachte ihm ein anderes Spülergebnis. Sein Wischer hatte
    die Düse zuvor nicht zuverlässig berührt, was nicht dasselbe ist wie ein auf gerade
    eben berührend eingestellter Wischer; das ist also ein einzelner Bericht dafür, dass
    mehr Kontakt hilft. Er sagt nichts darüber aus, ob die automatische Routine zu kurz
    greift.

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
- **Ein einzelner Blob an der Stelle, an der ein Druck fortgesetzt wurde,** hat eine
  andere Ursache. Ein Anwender auf 6.6.3 führte Blobs nach einem Spool Join darauf
  zurück, dass die Düse ausschwitzte, während das Bett auf Druckhöhe zurückfuhr, und
  meldete das dem Hersteller
  ([#5391](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5391)). 6.9.0 heizt
  die Düse beim Fortsetzen nun im Reiniger wieder auf, was damit zusammenhängen könnte;
  ob es das Problem behebt, hat niemand berichtet. Einzelbericht, `provisional`.

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
zwei Monate Firmware-Änderungen hinweg, wobei das Firmware-Verhalten selbst
herstellerseitig bestätigt ist.

Die Änderungen in 6.9.0 sind in
[Prusas eigenen Release Notes](https://help.prusa3d.com/downloads/core-one-indx)
dokumentiert, die die automatische Kalibrierung des Düsenreinigers, die Verschiebung des
Spülpunkts und das Wiederaufheizen der Düse beim Fortsetzen benennen. Das hebt die
Kernaussage dieser Seite von einer Schlussfolgerung der Anwender auf eine vom Hersteller
dokumentierte Tatsache.

Die Hauptquelle ist
[Probleme bei Düsenreinigung und -kalibrierung](https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/nozzle-cleaning-calibration-issues/),
ein Thread mit 87 Beiträgen und sechzehn Teilnehmern von Ende Juli bis Mitte September
2026. Er enthält die Symptomberichte, die Klagen über die fehlende Sicht, die Anpassungen
im Tune-Menü, das Reinigungsturm-Experiment, das Ergebnis unter 6.9.0 sowie die späteren
Einzelberichte zur Wischerhöhe und zu 6.9.1. Ein großer Teil der späteren
Beiträge dreht sich um die Werkzeug-Offset-Kalibrierung, die
[eine eigene Seite](offset-sensor-board-failure.md) hat.

Die Nachprüfung gegen 6.9.1: Die
[Notes der stabilen Version](https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.9.1)
nennen einen Assistenten zum Rechtwinkligstellen der Gantry, Voreinstellungen für PVA
und BVOH sowie eine Korrektur beim Referenzieren, und nichts davon betrifft den Reiniger.
Dass das Bett während der Nozzle-Cleaner-Kalibrierung nach unten fährt, steht nur in den
[Notes der Beta](https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.9.1-beta).
Keine der beiden widerspricht etwas auf dieser Seite.

Die Verbesserung durch 6.9.0 ist von drei Anwendern **unabhängig bestätigt**: Einer
berichtet von sauberen Werkzeugwechseln bei einem gemischten TPU/PETG-Druck und erneut
bei einem vierfarbigen PETG-Druck; ein zweiter berichtet separat, das Ergebnis sei
deutlich sauberer und er brauche keinen Brim mehr, um Verunreinigungen aufzufangen; und
der Anwender, der den Thread eröffnet hat — die Person mit dem schwersten Fall — hat
seither bestätigt, dass 6.9.0 das Ausschwitzen und die Reinigung für ihn weitgehend
gelöst hat. Der letzte davon ist der stärkste einzelne Datenpunkt auf dieser Seite, weil
hier der ursprüngliche Beschwerdeführer seinen eigenen Bericht abschließt. Das ist die
stärkste Aussage auf dieser Seite. Sie hat eine Einschränkung, die im Hinweis ganz oben
steht: Wochen später, nach einem fehlgeschlagenen Druck, traten beim selben Anwender
unter 6.9.0 Fehler bei der Werkzeugkalibrierung auf, die bei ihm neu waren, und das
Ausschwitzen kehrte zurück, nachdem er die Maschine zurückgesetzt und jedes Werkzeug
neu kalibriert hatte.

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

Ebenso wenig ein Bericht an den Hersteller, wonach der Wischpfad der Firmware in Y
durchgehend neben der Mitte des Silikonpads landet
([#5496](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5496)). Er klingt nach
der Frage zum Nozzle Cleaner Y Offset weiter oben, betrifft aber einen Core One+ (Gen 2)
ohne INDX mit eigenem Wischer-Zubehör, auf der Nicht-INDX-Firmware 6.8.1. Er belegt
keinen systematischen Y-Fehler am INDX, und die Lesart, dass der Y-Offset
maschinenspezifisch ist, bleibt bestehen.

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
