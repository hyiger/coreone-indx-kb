---
title:        Werkzeug-Offset-Kalibrierung schlägt fehl — kontaktloser Offset-Sensor
confidence:   reported
updated:      2026-08-25
author:       hyiger
printer:      Core One
toolhead:     INDX
hotend:       unknown
nozzle:       unknown
firmware:     6.9.0 for the calibration regression; the board fault is not version-specific
sources:
  - https://help.prusa3d.com/article/tool-offset-failed-36130-core-one-indx_1089016
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5442
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/offset-sensor-failure/
  - https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/tool-offset-calibration-failing/
  - https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/a-summary-of-common-indx-problems/
superseded_by:
source_sha:   0fb3079a066907633d62298c0668474f9e2a4d1ca37762d340f55b5a5fac6078
---
# Werkzeug-Offset-Kalibrierung schlägt fehl — kontaktloser Offset-Sensor

## Zusammenfassung

Wenn die Tool Offset Calibration wiederholt fehlschlägt und die Fehlermeldung nichts
Brauchbares mitteilt, liegt meistens eine defekte Platine des kontaktlosen
Offset-Sensors vor und kein Montagefehler. Reinigen Sie zuerst den Sensor, denn ein
Filamentkrümel darauf erzeugt genau denselben Fehler. Hilft die Reinigung nicht,
besteht die von mehreren Besitzern berichtete Lösung im Austausch der Sensorplatine —
und die Riemenspannung, die der Support unter Umständen vorschlägt, hat keinen
einzigen berichteten Fall behoben.

!!! important "Bevor Sie die Platine verdächtigen: Läuft bei Ihnen 6.9.0?"
    Ein offener Fehlerbericht zur Firmware beschreibt, dass die
    Werkzeug-Offset-Kalibrierung **nach dem Upgrade auf 6.9.0** wiederholt
    fehlschlägt, an einer Maschine, an der sie zuvor funktioniert hat. Ein zweiter
    Besitzer bestätigt dasselbe. Betroffen sind alle Düsen, und ein erneuter Durchlauf
    des Kalibrierassistenten gelingt erst nach mehreren Versuchen.

    Das ist hier von Belang, weil es sich fast identisch zu dem Hardwarefehler
    darstellt, um den es auf dieser Seite geht, die Abhilfe aber eine völlig andere
    ist. Wenn Ihre Kalibrierung vor einem Update einwandfrei lief und danach
    fehlzuschlagen begann, liegt eher dieser Fall vor als eine defekte Sensorplatine —
    und ein Hardwaretausch hilft dann nicht.

    Der Bericht ist zum Zeitpunkt der Erstellung offen und ungelöst; es gibt also außer
    erneuten Versuchen noch keine Abhilfe, auf die sich verweisen ließe. Prüfen Sie den
    aktuellen Stand des Issues, bevor Sie eine RMA anstoßen. Die Firmware verlinkt
    außerdem einen offiziellen Hilfeartikel zu diesem Fehlercode, der dem Melder nach
    eigener Aussage nicht geholfen hat.

## Fehlercodes, die hierher führen

| Code | Anzeige am Drucker |
|---|---|
| [`36130`](https://help.prusa3d.com/article/tool-offset-failed-36130-core-one-indx_1089016) | Tool offset failed |
| [`36136`](https://help.prusa3d.com/article/calibrate-dock-from-menu-17136-xl-36136-core-one-indx_1037195) | Calibrate dock from menu |

`36130` behandelt diese Seite. Es ist auch der Code, zu dem die Firmware ihren eigenen
Hilfeartikel verlinkt — jenen Artikel, der dem Besitzer, der die 6.9.0-Regression
meldet, nach eigener Aussage nicht weitergeholfen hat.

## Details

An der Einrichtung eines INDX sind zwei verschiedene Sensoren beteiligt, und zu wissen,
welcher von beiden ausgefallen ist, erspart sehr viel vergebliche Mühe. Die Wägezelle
erfasst den Z-Kontakt mit dem Druckbett. Für die Werkzeug-Offsets ist ein separater
kontaktloser Induktivsensor auf einer eigenen kleinen Platine zuständig. Bei diesem
Fehlerbild läuft das Z-Probing über die Wägezelle einwandfrei durch; es ist der
kontaktlose Sensor, der überhaupt keine Messwerte liefert, sodass der Kalibrierung die
Grundlage fehlt.

Das Firmware-Log trägt einen charakteristischen Fingerabdruck — einen Fehler, der die
kontaktlose Offset-Routine benennt, zusammen mit einem fehlgeschlagenen Abgriff eines
ersten Sensormesswerts. Diese Logzeile ist das Nützlichste, was Sie festhalten können,
denn die Meldung auf dem Display ist generisch und der dort angezeigte Hinweis, die
Düse zu reinigen, führt in die Irre.

Was diesen Fehler verwirrend macht:

- **Die Werkzeugnummer, bei der es fehlschlägt, ist nicht aussagekräftig.** Manche
  Besitzer berichten von einem Fehlschlag beim ersten Werkzeug, andere kommen mehrere
  Werkzeuge weit, bevor es fehlschlägt, wobei die Abbruchstelle zwischen den Versuchen
  wandert, ohne dass zwischendurch etwas geändert wurde. Unterschiedliche
  Abbruchstellen bedeuten nicht unterschiedliche Probleme.
- **Werkzeuge untereinander zu tauschen hilft nicht**, und erneutes Einsetzen der
  Werkzeuge ebenso wenig. Mehrere Besitzer haben Permutationen durchprobiert, bevor sie
  auf den Sensor als Ursache schlossen.
- **Die Riemenspannung ist hier eine falsche Fährte.** Sie ist eine naheliegende erste
  Vermutung und wurde vom Support vorgeschlagen, doch Besitzer, die das Portal gründlich
  ausgerichtet und die Riemen neu gespannt haben, berichten von keiner Änderung.
  Verbringen Sie damit keine Nacht, bevor Sie ein Log aufgezeichnet haben.
- **Ein bestandener Durchgangstest des Kabels entlastet den Sensor nicht.** Ein Besitzer
  prüfte das Kabel, fand es elektrisch einwandfrei — und die Platine war dennoch die
  Ursache. Ein bloßer Kabeltausch hat in den berichteten Fällen nichts behoben.

### Vorgehen, der Reihe nach

1. **Reinigen Sie den Sensor selbst**, nicht nur die Düse. Ein kleiner Filamentrückstand
   auf der Sensorfläche verursacht ein identisches Fehlerbild, und dies ist die eine
   Ursache, die Sie in einer Minute selbst beheben können.
2. **Zeichnen Sie über die serielle USB-C-Verbindung ein Firmware-Log auf** und bewahren
   Sie es auf. Das ist der Nachweis, der einen Supportfall schnell zum Abschluss bringt
   — mindestens ein Besitzer berichtet, dass der Hersteller die Platine ausdrücklich auf
   Grundlage eingereichter Logs als defekt bestätigt hat. TODO(verify): die
   einzustellende serielle Baudrate. Sie steht im Summary-Thread, aber ein Leser wird
   sie in ein Terminal eintippen, daher muss sie zuerst geprüft werden.
3. **Prüfen Sie die LED auf der Sensorplatine.** Wenn sie weiterhin schnell blinkt,
   nachdem eine Kalibrierung bereits fehlgeschlagen ist, deutet das auf die Platine
   selbst hin — das schnelle Muster soll nur erscheinen, während der Mikrocontroller des
   Sensors geflasht wird. Es außerhalb eines Firmware-Updates zu sehen, ist ein
   deutliches Signal.
4. **Eröffnen Sie einen Supportfall.** Der berichtete Weg ist zuerst die Diagnose bei
   Prusa und danach ein Bondtech-Ticket für die Ersatzplatine, das die Befunde von Prusa
   mitführt. Ein Ticket, das bereits benennt, was Prusa festgestellt hat, kommt schneller
   voran als eines, das bei den Symptomen beginnt. Eröffnen Sie ihn früh, auch wenn Sie
   noch nicht handeln wollen, damit das Datum aktenkundig ist — siehe
   [wen Sie kontaktieren](support-and-warranty-path.md).

Der Sensor arbeitet mit Wirbelströmen, was aus zwei Gründen wissenswert ist: Es ist der
Grund, weshalb eine nichtleitende Düsenspitze für künftige Düsenvarianten eine
konstruktive Einschränkung darstellt, und es ist der Grund, weshalb Verschmutzung der
Sensoroberfläche so stark ins Gewicht fällt.

Ein in der Zusammenfassung berichteter Vergleich zweier Platinen ergab, dass ein
defektes und ein funktionierendes Exemplar dieselbe Hardware-Revision aus derselben
Produktionscharge waren; es sieht also nach Streuung auf Exemplarebene aus und nicht
nach einer schlechten Charge, die sich anhand einer Seriennummer erkennen ließe.

!!! warning "Ein Vorschlag aus den Threads ist keine Reparatur"
    Ein Besitzer brachte ins Gespräch, die Sensorplatine im Reflow-Ofen nachzuarbeiten.
    Es gibt keinen Bericht darüber, dass das jemand erfolgreich getan hätte, und es
    würde jeden Garantieanspruch auf das Teil mit ziemlicher Sicherheit beenden. Lassen
    Sie die Platine austauschen.

## Verifizierung

`reported` (mehrfach berichtet) — zwei unabhängige Threads, zwei verschiedene Besitzer,
beide endend beim Austausch der Platine.

[Ausfall des Offset-Sensors](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/offset-sensor-failure/)
dokumentiert eine Kalibrierung, die beim ersten Werkzeug fehlschlägt, und legt den
Support-Weg fest, auf den sich die Besitzer verständigt haben.
[Werkzeug-Offset-Kalibrierung schlägt fehl](https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/tool-offset-calibration-failing/)
stammt von einem anderen Besitzer mit einem anders aussehenden Erscheinungsbild —
Fehlschlag mitten in der Werkzeugfolge, sporadisch —, der Riemenspannung und
Werkzeugtausch ohne Verbesserung durchprobierte, den Kabeldurchgang als einwandfrei
nachwies und berichtet, dass der Hersteller nach Durchsicht eingereichter Logs die
Platine als Ursache bestätigte. Dass zwei unähnliche Symptommuster auf dasselbe Bauteil
hinauslaufen, ist das Nützlichste auf dieser Seite.

Der Log-Fingerabdruck, die LED-Diagnose, der Wirbelstrom-Mechanismus und der Vergleich
innerhalb derselben Charge stammen aus der
[Zusammenfassung häufiger Probleme](https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/a-summary-of-common-indx-problems/),
einer Verdichtung einer inzwischen offline genommenen Community-Wissensdatenbank. Diese
Einzelheiten haben nur eine Quelle und wurden im Forumsbestand nicht gesondert bestätigt.

Wo die Quellen sich widersprechen: Die ersten Vorschläge des Supports schwankten zwischen
Kabel und Platine, und in einem Fall wurde die Riemenspannung angeführt. Die Erfahrung
der Besitzer weist durchgängig auf die Platine.

**Seit der Erstveröffentlichung ergänzt.** Die Kalibrierungsregression unter 6.9.0 stammt
aus dem [Firmware-Issue-Tracker](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5442),
der für Firmware-Verhalten eine stärkere Quellenklasse ist als das Forum — er ist
herstellereigen, versioniert und reproduzierbar. Zwei Besitzer berichten davon. Es ist ein
offenes Issue; es kann behoben, neu eingeordnet oder als etwas anderes erkannt werden.
Betrachten Sie den obigen Abschnitt daher als Stand zum Zeitpunkt der Erstellung und nicht
als gesichert.

## Verwandte Seiten

- [Probing schlägt fehl oder die Düse berührt das Bett nie](loadcell-emi-noise.md) — der
  andere Sensor, häufig mit diesem verwechselt
- [Montagehinweise](../reference/assembly-notes.md) — wenn dies an einer frisch
  aufgebauten Maschine fehlschlägt, die noch nie erfolgreich kalibriert hat, prüfen Sie
  zuerst den Aufbau: Dies ist einer der beiden Selbsttest-Fehler, die bei Neuumbauten
  immer wieder auftreten
- [Wen Sie kontaktieren](support-and-warranty-path.md) — so kommen Sie an das Ersatzteil:
  Diagnose von Prusa, Hardware von Bondtech, und eröffnen Sie den Fall früh genug, dass
  das Datum in Ihren Garantiezeitraum fällt.
