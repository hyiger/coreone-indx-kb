---
title:        Oozing verdirbt Bettabtastung und Werkzeugkalibrierung
confidence:   reported
updated:      2026-08-24
author:       hyiger
printer:      Core One
toolhead:     INDX
hotend:       unknown
nozzle:       0.25mm, 0.4mm, 0.8mm reported
firmware:     unknown
sources:
  - https://forum.prusa3d.com/forum/prusa-indx-how-do-i-print-this-printing-help/petg-oozing-and-impeding-bed-probing/
  - https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/nozzle-cleaning-calibration-issues/
  - https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/a-summary-of-common-indx-problems/
superseded_by:
source_sha:   6709a449eb6899c0d5cb3b379c11ad47d15419db871d567f3b4e75c01355c64e
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
angenommenen Niedertemperaturmaterial gesliced wurden, das Problem nie zeigten. Es gibt
außerdem einen Ansatz über den Start-G-Code, der die Abtasttemperatur vor dem Block für
das Mesh Bed Leveling erzwingt, indem der erzeugte Temperaturbefehl durch einen festen
ersetzt wird.

TODO(verify): die zu erzwingende Abtasttemperatur sowie den genauen G-Code-Befehl und
das zugehörige Argument. Außerdem TODO(verify): die Absenkung, die ein Besitzer beim
gleichen Symptom auf einer Core One ohne INDX erfolgreich verwendet hat, angegeben als
Bereich statt als Einzelwert. Auf dieser Seite wird keine Temperatur veröffentlicht,
bevor sie jemand auf der Hardware bestätigt hat.

Zwei weitere berichtete Einzelheiten in diesem Bereich, beide aus einer einzigen Quelle
und beide zu kennen, bevor man auf die Suche geht: Ein Konfigurationsupdate des Slicers
hat die Ableitung für die meisten Materialien korrigiert, mindestens ein
Konstruktionsmaterial tastet jedoch weiterhin heiß ab; und die Temperatur für die
Werkzeug-Offset-Kalibrierung ist in der Firmware fest hinterlegt und lässt sich nicht
per G-Code ändern, weshalb dieser Workaround gegen diesen Fehlerfall nicht hilft. Es
gibt zudem eine verwandte Slicer-Falle, bei der die **Bett**temperatur auf dieselbe
Weise T1 folgt.

### Wenn nichts davon hilft

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
