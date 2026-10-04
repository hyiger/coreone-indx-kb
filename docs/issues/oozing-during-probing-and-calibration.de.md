---
title:        Oozing verdirbt Bettabtastung und Werkzeugkalibrierung
confidence:   reported
updated:      2026-10-04
author:       hyiger
printer:      Core One
toolhead:     INDX
hotend:       unknown
nozzle:       0.25mm, 0.4mm, 0.8mm reported
firmware:     unknown
sources:
  - https://forum.prusa3d.com/forum/prusa-indx-how-do-i-print-this-printing-help/petg-oozing-and-impeding-bed-probing/
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/printing-pc-on-indx-oozing-at-bed-probing-leveling/
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/psa-if-you-are-struggling-with-tool-offset-calibration-failing-non-stop-at-the-start-of-a-print-get-firmware-6-9-1/
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5483
  - https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/nozzle-cleaning-calibration-issues/
  - https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/a-summary-of-common-indx-problems/
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.9.1
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/compare/v6.9.1-beta...v6.9.1
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5494
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5505
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/lib/Marlin/Marlin/src/gcode/bedlevel/ubl/G29.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/src/feature/tool_offset_calibration/tool_offset_calibration.cpp
  - https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/bed-leveling-issues-3/
superseded_by:
source_sha:   680e50c58ad90641fc8ca1b3e0731c60f367d46ab8d3091d90b60babe88e06c2
---
# Oozing verdirbt Bettabtastung und Werkzeugkalibrierung

## Zusammenfassung

Filament, das austritt, während die Maschine abtastet oder kalibriert, bringt Material
genau dorthin, wo die Maschine eine Messung vornehmen will, und die Messung schlägt
fehl. Besitzer sind sowohl bei der Bettabtastung als auch bei der
Werkzeug-Offset-Kalibrierung darauf gestoßen, mit mehr als einer Filamentsorte. Es gibt
mehrere begünstigende Ursachen, und es lohnt sich, sie auseinanderzuhalten: Die mit den
besten Belegen aus erster Hand — ein verschmutztes Fenster des Offset-Sensors — lässt
sich zugleich am leichtesten beheben und wird am wenigsten wahrscheinlich zuerst
vermutet.

## Details

Zwei verschiedene Messungen werden durch Oozing verdorben, und sie schlagen
unterschiedlich fehl:

- **Bettabtastung.** Material sammelt sich vor oder während des Abtastvorgangs an der
  Düsenspitze an, sodass der Kontakt zu früh oder uneinheitlich erkannt wird. Besitzer
  berichten, dass die Abtastung sichtbare Ablagerungen auf dem Druckblech hinterlässt.
- **Werkzeug-Offset-Kalibrierung.** Austretendes Filament stört die korrekte Erfassung
  der Düse durch den Offset-Sensor, und die Kalibrierung schlägt fehl. Ein Besitzer
  berichtet, dass dies nach dem Wechseln von Düsengrößen bei jedem Werkzeug fehlschlug
  und er sämtliches Filament entladen, kalibrieren und dann wieder laden musste.

### Hier anfangen: das Fenster des Offset-Sensors reinigen

Die Lösung, die den maßgeblichen Thread dazu tatsächlich abgeschlossen hat, war das
Reinigen des Sensorfensters an jeder Düse. Der Besitzer berichtete, dass die
Wattestäbchen sichtbar schwarz wurden, obwohl er nicht glaubte, die Fenster berührt zu
haben, und dass ein Testdruck danach funktionierte. Das kostet ein paar Minuten und ist
der Punkt mit dem höchsten Nutzen.

Zu welchem Sensor dieses Fenster gehört, ist umstritten. Antworten im selben Thread
nennen es ein Temperaturfenster, und die [Seite zur Silikonsocke](silicone-sock-migration.md),
nach der der auf Wirbelströmen beruhende Offset-Sensor überhaupt kein optisches Fenster
hat, lässt die Zuordnung offen. Das Ergebnis der Reinigung gilt in beiden Fällen.

!!! warning "Das Sensorfenster nicht mit IPA reinigen"
    Der im Thread weitergegebene Rat lautet, Seifenwasser und ein Wattestäbchen zu
    verwenden statt Isopropylalkohol, mit der Begründung, IPA sei für dieses Fenster
    zu aggressiv. Die Herkunft gehört klar benannt: Dies wurde als eine auf Discord
    kursierende Herstellerempfehlung beschrieben, und die Person, die sie weitergab,
    sagte offen, dass sie keine offizielle Quelle nennen könne. Seifenwasser ist
    ohnehin die risikoärmere Wahl, ihm ist also der Vorzug zu geben — die Begründung
    sollte jedoch als unbestätigt gelten.

    TODO(verify): ob der Hersteller ein offizielles Reinigungsverfahren für das
    Fenster des Offset-Sensors veröffentlicht hat.

!!! warning "Reinigen, aber nicht polieren"
    Eine spätere Warnung im selben Thread ist beachtenswert: Die Sensorfläche soll
    matt sein und darf am Ende nicht glänzend oder spiegelnd wirken. Gehen Sie
    sparsam vor. Ziel ist es, Filamentrückstände abzunehmen, nicht Glanz zu erzeugen.

    Ein Vorbehalt zu diesem Rat — der Besitzer, der ihn gibt, beschreibt den Sensor
    als infrarotbasiert, während der Offset-Sensor an anderer Stelle als
    wirbelstrombasiert beschrieben wird. Das sind unterschiedliche Messprinzipien,
    und es ist nicht klar, welche Komponente gemeint ist. Die praktische Anweisung
    trägt in beiden Fällen: die Rückstände entfernen und es dabei belassen.

### Das Filament trocknen

Früh und wiederholt vorgeschlagen, insbesondere für PETG: Feuchtigkeit lässt Filament
Fäden ziehen und begünstigt, dass es an der Düse haften bleibt. Das ist gängige Praxis
und keine INDX-spezifische Erkenntnis, und in diesen Threads wurde es als erste
Vermutung und nicht als bestätigte Ursache geäußert — der INDX gilt Berichten zufolge
jedoch als feuchtigkeitsempfindlicher als der Nextruder, den er ersetzt, weshalb es
sich lohnt, dies auszuschließen, bevor man Komplizierterem nachjagt.

### Die Abtasttemperatur ist möglicherweise nicht die erwartete

Es gibt ein berichtetes Verhalten von Firmware und Slicer, bei dem die Temperatur für
die Bettabtastung vor dem Druck aus dem Filament abgeleitet wird, das **Werkzeug 1**
zugewiesen ist, und nicht aus dem Werkzeug, das die Abtastung tatsächlich ausführt. Ist
T1 ein Hochtemperaturmaterial zugewiesen, tastet alles heiß ab und sickert, unabhängig
davon, was anderswo geladen ist.

Der berichtete Workaround ist elegant, sofern er trägt: Es genügt, im Slicer für T1 ein
Niedertemperatur-Filament zu *deklarieren* — das physische Filament muss gar nicht
vorhanden sein —, was erklären würde, warum Aufträge, die aus Profilen mit einem
angenommenen Niedertemperaturmaterial gesliced wurden, das Problem nie zeigten. Im Standardprofil, das diese
Website wiedergibt, ist die Regel allerdings an das Startwerkzeug des Drucks gebunden und
nicht an T1 — lesen Sie den PC-Abschnitt weiter unten, bevor Sie sich darauf verlassen. Es
gibt außerdem einen Ansatz über den Start-G-Code, der die Abtasttemperatur vor dem Block für
das Mesh Bed Leveling erzwingt, indem der erzeugte Temperaturbefehl durch einen festen
ersetzt wird.

TODO(verify): die zu erzwingende Abtasttemperatur sowie den genauen G-Code-Befehl und
das zugehörige Argument. Außerdem TODO(verify): die Absenkung, die ein Besitzer beim
gleichen Symptom auf einer Core One ohne INDX erfolgreich verwendet hat, angegeben als
Bereich statt als Einzelwert. Auf dieser Seite wird keine Temperatur veröffentlicht,
bevor sie jemand auf der Hardware bestätigt hat.

Zwei weitere berichtete Einzelheiten in diesem Bereich, die man kennen sollte, bevor man
auf die Suche geht: Ein Konfigurationsupdate des Slicers hat die Ableitung für die
meisten Materialien korrigiert, mindestens ein Konstruktionsmaterial tastet jedoch
weiterhin heiß ab; und die Temperatur für die Werkzeug-Offset-Kalibrierung ist in der
Firmware fest hinterlegt und lässt sich nicht per G-Code ändern, weshalb dieser
Workaround gegen diesen Fehlerfall nicht hilft. Die zweite Einzelheit stammt weiterhin
aus einer einzigen Quelle. Es gibt zudem eine verwandte Slicer-Falle, bei der die
**Bett**temperatur auf dieselbe Weise T1 folgt.

**Das Konstruktionsmaterial ist PC.** Ein [zweiter Besitzer](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/printing-pc-on-indx-oozing-at-bed-probing-leveling/) geriet damit an
PC Blend und beschrieb es von der anderen Seite: Die Abtastung lief heiß genug, um auf
das Blech zu sickern und das Leveling scheitern zu lassen, und ein händisches Absenken
der Düsentemperatur beim nächsten Versuch behob es vollständig. Damit stand „mindestens
ein Konstruktionsmaterial tastet weiterhin heiß ab“ nicht mehr auf einem einzigen
Bericht und bekam einen Namen, und es ist seither nicht bei einem Besitzer geblieben. Zwei
weitere Besitzer im selben Thread, einer in einem [anderen Thread](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/psa-if-you-are-struggling-with-tool-offset-calibration-failing-non-stop-at-the-start-of-a-print-get-firmware-6-9-1/) und ein
[Firmware-Issue](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5483) beschreiben alle, dass PC Blend beim Abtasten des Betts
scheitert, bis die Temperatur sinkt.

**Woher die Temperatur kommt.** Es gibt **kein eigenes Feld für die Abtasttemperatur** im
Slicer, wohl aber eine Regel. Der Standard-Start-G-Code des Druckers ermittelt die
Abtasttemperatur aus dem Filament des **Startwerkzeugs** des Drucks — des ersten
Werkzeugs, das der Druck tatsächlich nutzt — und behandelt PC und PA gesondert:
mit einem festen Abstand unter der Temperatur der ersten Schicht. Das kommentierte Profil
gibt diesen Ausdruck in seinem Abschnitt zu den globalen Variablen und der
Abtasttemperatur wieder — siehe [kommentiertes Profil](../gcode/indx-profile-gcode.md). An
diese Regel stoßen diese Besitzer immer wieder.

**Startwerkzeug, nicht T1.** Dieser Ausdruck liest das Filament von `initial_tool`, und
das ist nicht das weiter oben berichtete T1-Verhalten. Beide wählen nur dann dasselbe
Filament, wenn ein Druck auf T1 beginnt. Bei einem Druck, der auf einem anderen Werkzeug
beginnt, zeigen sie auf verschiedene Presets — in diesem Profil hilft es also nicht, für
T1 ein Niedertemperatur-Filament zu deklarieren, wenn der Druck auf T3 beginnt;
maßgeblich ist das Filament, mit dem Ihr Druck startet. Ob der frühere T1-Bericht ein
älteres Profil oder einen anderen Maschinenzustand beschreibt, ist nicht geklärt.

**Keine der beiden 6.9.1-Versionen nennt hier eine Änderung.** Die Beta senkte die
Temperatur für die *Werkzeug-Offset-Kalibrierung*, einen eigenen Firmware-Schritt. Die
Temperatur beim Abtasten des Betts stammt aus dem Slicer-Profil, weshalb PC Blend auch
unter der Beta weiterhin heiß abtastet, und der gegen die Beta eröffnete
[Fehlerbericht](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5483) ist
noch immer offen und unbeantwortet. Die
[stabile Version 6.9.1](https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.9.1),
veröffentlicht am 2026-09-25, nennt einen Assistenten zum Ausrichten des Portals und eine
Korrektur beim Referenzieren — zur Abtasttemperatur nichts.
Auch die Kalibrierungsänderungen der Beta tauchen in den Versionshinweisen der stabilen
Version nicht wieder auf, enthalten sind sie trotzdem: Im Firmware-Repository ist die
stabile Version das Beta-Tag plus
[15 weitere Commits](https://github.com/prusa3d/Prusa-Firmware-Buddy/compare/v6.9.1-beta...v6.9.1),
von denen keiner die Werkzeug-Offset-Kalibrierung berührt. Das ergibt sich aus der
Release-Historie, nicht aus den Versionshinweisen. Wie PC Blend unter der stabilen
Version abtastet, hat bislang kein Besitzer berichtet.

**Anpassen.** Ein Besitzer vergrößerte den PC-Abstand im Start-G-Code des Druckers, und
die Fehlschläge hörten auf. Der Haken, auf den er selbst hinwies: Ein
Konfigurationsupdate des Druckers ersetzt den Start-G-Code, sodass die Änderung nach
jedem Update neu vorgenommen werden muss. Derselbe Ausdruck prüft außerdem die
Filamentnotizen des Startwerkzeugs auf eine Überschreibungsmarke, bevor er überhaupt
den PC-Fall erreicht; das deutet auf einen Weg je Filament hin, der solche Updates
überstehen würde — doch das ist eine Lesart des Profils und nichts, das ein Besitzer als
getestet berichtet hat. Und die slicereigene **Option zur Sickerverhinderung half
nicht**, sodass es einen Druck kostet, zuerst danach zu greifen.

TODO(verify): Diese Berichte nennen die Temperatur, mit der PC abgetastet wurde, die
niedrigeren, die funktionierten, und den angepassten Abstand. Nichts davon wird hier
veröffentlicht. Forenbeiträge und ein Fehlerbericht sind nicht die Hardware-Bestätigung,
die diese Seite verlangt, bevor eine Temperatur auf ihr erscheint — aber sie sind
Hinweise, und es ist dieselbe Angabe, nach der die Markierung weiter oben fragt.

### Wenn das Leveling scheitert und neu ansetzt

`provisional` für die Berichte der Besitzer — es sind wenige, und auf den ersten Blick
stimmen sie nicht überein. Der Firmware-Quellcode, weiter unten, ordnet jeden dem
Schritt zu, der fehlschlug. Ist das Bett-Leveling an einer verschmutzten Düse
gescheitert, sollten Sie nicht darauf zählen, dass der nächste
Versuch mit einer sauberen beginnt. Eine
[Funktionsanfrage](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5494)
beschreibt, wie der Kopf zum Abstreifer fährt und dann für einen weiteren Versuch zum
Bett zurückkehrt, ohne die Düse zu säubern. Ein Besitzer mit der 6.9.1-Beta fand im
[Thread zur Düsenreinigung](https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/nozzle-cleaning-calibration-issues/)
das Werkzeug im Silikon-Abstreifblock geparkt vor, wo die Düse für eine Reinigung von
Hand nicht erreichbar war; der Druck lief erst nach mehreren Wiederholungen an. Zwei
weitere Besitzer dort beschreiben etwas anderes: einen neuen Versuch, der die Düse erneut
aufheizt, spült und abstreift, selbst nachdem sie von Hand gereinigt wurde, und sie dabei
so verschmutzt, dass es wieder scheitert. Einer von ihnen nutzte ebenfalls einen
6.9.1-Build und hält es für möglich, dass seine eigene Abstreifer-Einstellung oder ein
Fehler der Wägezelle schuld ist; der andere nennt keine Version, und die Funktionsanfrage
ebenso wenig. Die Firmware-Version erklärt den Unterschied also nicht, und diese beiden
Beiträge sagen nicht, ob das Bett-Leveling oder die Werkzeug-Offset-Kalibrierung der
fehlschlagende Schritt war.

**Zwei Schritte, zwei Wiederholungen.** Gegen den Firmware-Quellcode gelesen,
widersprechen sich die Berichte nicht mehr: Sie beschreiben verschiedene Schritte.
Bekommt das Bett-Leveling keinen Messwert, parkt der Drucker den Kopf an seiner
Parkposition, die der Code innerhalb des Bereichs des Düsenreinigers verortet, fragt,
ob erneut versucht werden soll, und verlässt bei Ja den Reiniger und tastet erneut ab,
ohne dazwischen zu reinigen. Das sind die Funktionsanfrage und der Besitzer mit der
Beta. Scheitert die Werkzeug-Offset-Kalibrierung während eines Drucks, parkt der Drucker
den Kopf vorn bei abgesenktem Bett, wo die Düse erreichbar ist, und führt bei Retry die
Vorbereitung je Werkzeug erneut aus — aufheizen, spülen, abkühlen, abstreifen —, bevor
er abtastet. Nach einem gescheiterten XY-Scan betrifft das nur das fehlgeschlagene
Werkzeug; nach einer gescheiterten Z-Antastung beginnt die Wiederholung die Kalibrierung
wieder beim ersten Werkzeug, sodass jedes Werkzeug erneut spült. Das ist das erneute
Verschmutzen, das die beiden anderen Besitzer beschreiben, und es geschieht, ganz
gleich, wie gründlich die Düse gerade gereinigt wurde. Beide Pfade durchlaufen in 6.9.0,
der 6.9.1-Beta und der stabilen 6.9.1 dieselben Schritte (an der Vorbereitung hat die
Beta nur die Temperatur geändert, auf die sie abkühlt), weshalb die Version die Berichte
nicht trennte. Das gilt für Prusas eigene Builds; der Besitzer mit einem 6.9.1-Build
schrieb vor der stabilen Version und sagte nicht, welcher Build es war. Der Code für das
Bett-Leveling hat zwar einen Zweig, der abstreift und es erneut versucht, doch er gehört
zu einem Reinigungsdurchgang beim Abtasten, den der Standard-Start-G-Code des INDX nicht
aufruft.

In der Praxis: Ein gescheitertes Bett-Leveling reinigt die Düse nicht für Sie, und nach
einer gescheiterten Werkzeug-Offset-Kalibrierung folgt auf die Reinigung von Hand ein
erneutes Spülen. Ein
[Bericht an den Hersteller](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5505)
zur Beta bittet darum, dass die Wiederholung der Kalibrierung das Spülen auslässt und
nur wieder aufheizt und abstreift, da erneutes Spülen das Problem wieder einspeist; er
ist offen und unbeantwortet. Dies ist eine Lesart des Codes im Stand des Git-Tags v6.9.1, nicht etwas,
das ein Besitzer bestätigt hat, indem er beide Fehlschläge an einer Maschine beobachtet
hätte.

### Wenn nichts davon hilft

Um herauszufinden, ob Oozing überhaupt beteiligt ist, ließ ein Besitzer den Drucker mit
einem leeren Werkzeug abtasten, sodass nichts austreten konnte; die Abtastung schlug
genauso fehl, was Oozing für ihn ausschloss
([Thread](https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/bed-leveling-issues-3/)).
Einzelbericht, und sein Fehler war weiterhin ungelöst.

Wenn die Abtastung fehlschlägt, während die Düse offensichtlich nirgends in der Nähe
des Druckblechs ist — ein Abstand, den man sieht und nicht misst —, dann ist das ein
ganz anderer Fehler, und Oozing ist nicht Ihr Problem. Siehe
[Störeinflüsse auf die Wägezelle](loadcell-emi-noise.md). Wenn die
Werkzeug-Offset-Kalibrierung unabhängig von Sauberkeit und Filamentzustand
fehlschlägt, siehe [Ausfall der Offset-Sensorplatine](offset-sensor-board-failure.md).

## Überprüfung

`reported` (mehrfach berichtet) — das Symptom wird von verschiedenen Besitzern mit
unterschiedlichen Materialien unabhängig voneinander berichtet.

[PETG sickert und behindert die Bettabtastung](https://forum.prusa3d.com/forum/prusa-indx-how-do-i-print-this-printing-help/petg-oozing-and-impeding-bed-probing/)
ist der maßgebliche Thread: Der ursprüngliche Verfasser berichtet, dass PETG so stark
austritt, dass es die Bettabtastung verdirbt, und ein zweiter Besitzer berichtet
unabhängig davon von derselben Fehlerklasse mit PLA bei jedem Werkzeug während der
Kalibrierung. Der Thread ist als beantwortet markiert, und die angenommene Antwort ist
die Reinigung des Sensorfensters, aus erster Hand von der Person bestätigt, die das
Problem hatte. Das sind die stärksten Belege auf dieser Seite.

Aus einer einzigen Quelle und unbestätigt: Die Temperaturableitung über Werkzeug 1, der
Workaround mit dem deklarierten kühlen Filament, das Überschreiben per G-Code, die
Korrektur der Slicer-Konfiguration und die fest einprogrammierte Kalibriertemperatur
stammen sämtlich aus der
[Zusammenfassung häufiger Probleme](https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/a-summary-of-common-indx-problems/),
einer Verdichtung einer inzwischen offline genommenen Community-Wissensdatenbank.
Nichts davon ist im Forumsbestand gesondert bestätigt, und es werden hier keine Zahlen
daraus wiedergegeben.

Das Verhalten bei Wiederholungen ist aus dem Firmware-Quellcode im Stand des Git-Tags v6.9.1 gelesen —
aus dem
[Befehl für das Bett-Leveling](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/lib/Marlin/Marlin/src/gcode/bedlevel/ubl/G29.cpp)
und der
[Werkzeug-Offset-Kalibrierung](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/src/feature/tool_offset_calibration/tool_offset_calibration.cpp)
—, und die Tags 6.9.0 und 6.9.1-Beta nehmen dieselben Wiederholungspfade. Die Beta hat
geändert, wie sie ablaufen, nicht welche Schritte sie umfassen: Die Vorbereitung je
Werkzeug kühlt weiter ab, der XY-Scan läuft kühler, und das Antasten auf der Sensorplatine
bekommt mehr Versuche, bevor es als gescheitert gilt (siehe
[Fehlercodes](../codes.md)). Es wird
festgehalten, weil es jeden Besitzerbericht in jenem Abschnitt erklärt, ohne einem davon
zu widersprechen, zeigt aber, was der Code tut, nicht was ein Besitzer beobachtet hat.

Wo die Quellen sich widersprechen: Das Trocknen wurde mit Nachdruck als wahrscheinliche
Ursache für PETG genannt, doch der Fall, der tatsächlich gelöst wurde, wurde durch
Reinigen gelöst, nicht durch Trocknen. Nehmen Sie Feuchtigkeit nicht allein deshalb an,
weil es sich um PETG handelt — als die Frage dem ursprünglichen Verfasser direkt
gestellt wurde, antwortete er, er habe unmittelbar aus einem Filamenttrockner gedruckt,
was Feuchtigkeit für diesen Fall vollständig ausschließt.

## Verwandte Themen

- [Abtastung schlägt fehl oder die Düse berührt das Bett nie](loadcell-emi-noise.md)
- [Werkzeug-Offset-Kalibrierung schlägt fehl](offset-sensor-board-failure.md)
- [Phantomwerkzeuge und Fehler beim Parken](tool-detection-ringdown-decay.md)
- [In den Druck geschleppte Klumpen](stringing-and-wiper-calibration.md) — dasselbe
  Problem von Material am falschen Ort, das jedoch bei Werkzeugwechseln auftritt und
  nicht während der Abtastung. Wenn Ihre Ablagerungen bei Werkzeugwechseln erscheinen,
  beginnen Sie dort.
