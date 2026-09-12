---
title:        Verrutschen der Silikonsocke über den Temperatursensor
confidence:   provisional
updated:      2026-09-12
author:       hyiger
printer:      Core One
toolhead:     INDX
hotend:       unknown
nozzle:       unknown
firmware:     unknown
sources:
  - https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/indx-maintenance/
  - https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/nozzle-wiper-vs-indx-offset-sensor/
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/problems-with-nozzle-socks/
superseded_by:
source_sha:   6f43d5a6696b2b04a80b5dd51decaae7e043729d2926fd1634a592ae672dbb4c
---
# Verrutschen der Silikonsocke über den Temperatursensor

!!! warning "Eine aus einzelnen Berichten zusammengesetzte Kette"
    Jedes Glied dieser Kette wird von jemandem berichtet. Die **Kette als Ganzes** —
    verrutschte Socke führt zu Überhitzung, führt zu Anbackungen, führt zum Fehlschlagen
    der Kalibrierung — stammt aus einem einzigen Bericht. Lesen Sie den Abschnitt
    Überprüfung, bevor Sie sie als gesichert behandeln.

## Zusammenfassung

Die Silikonsocke einer INDX-Düse kann so weit aus ihrer Sitzposition nach oben wandern,
dass sie das Fenster des Temperatursensors am Werkzeugkopf teilweise verdeckt. Bei
teilweise verdecktem Sensor läuft die Düse heißer als vorgegeben. Bei der PET-Familie,
und Berichten zufolge am ausgeprägtesten bei PCTG, backt die überschüssige Hitze
Filament an der Düsenspitze fest, und die entstehende Ablagerung reicht aus, um die
Werkzeug-Offset-Kalibrierung scheitern zu lassen.

Die Abhilfe ist trivial, sobald man weiß, wonach zu suchen ist: die Socke wieder nach
unten setzen. Der Grund, davon zu wissen, ist, dass sämtliche Symptome auf etwas anderes
hindeuten — auf die Düse, auf das Filament oder auf den Offset-Sensor.

## Nicht der Offset-Sensor

**Es handelt sich um einen Temperatursensor, nicht um den Werkzeug-Offset-Sensor.** Das
sind unterschiedliche Bauteile mit unterschiedlichen Messprinzipien, und die
Unterscheidung ist wichtig, weil das Symptom — fehlgeschlagene Offset-Kalibrierung — auf
das falsche Bauteil deutet.

Ein Bericht beschreibt das verdeckte Teil als IR-Fenster, ein anderer als Rechteck des
Temperatursensors. Beide Beschreibungen sind thermischer Natur. Der
Werkzeug-Offset-Sensor ist an anderer Stelle als wirbelstrombasiert dokumentiert, und
Wirbelstrommessung hat kein optisches Fenster, das verdeckt werden könnte. Siehe
[Ausfall der Offset-Sensorplatine](offset-sensor-board-failure.md) zu diesem Bauteil.

TODO(verify): ob das „IR-Fenster“ und das „Rechteck des Temperatursensors“ dasselbe
physische Merkmal sind und nach welchem Messprinzip der Temperatursensor des
Werkzeugkopfs tatsächlich arbeitet. Zwei Besitzer beschreiben es mit unterschiedlichen
Worten, und keine der Beschreibungen ist gegen einen Schaltplan oder die Dokumentation
des Herstellers abgesichert.

## Im Einzelnen

### Wandern der Socke

Berichten zufolge rutscht die Socke aus ihrer Sitzposition nach oben. Ein Besitzer fand
sie in einer Position vor, in der sie den Temperatursensor teilweise verdeckte, und
erhielt als unmittelbare Folge einen Thermal-Runaway-Fehler — das ist ein
Erfahrungsbericht aus erster Hand zur Verdeckung und ihrer unmittelbaren Konsequenz. Der
Autor dieser Seite fand die Socke an drei verschiedenen Düsen einer Maschine verschoben
vor, und ein weiterer Besitzer musste sie in einem [anderen Thread](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/problems-with-nozzle-socks/) nach nur
wenigen Testdrucken an zwei Werkzeugen wieder zurechtsetzen. Das Wandern ist nicht mehr
etwas, das an einer einzigen Maschine beobachtet wurde.

Warum sie wandert, ist nicht geklärt. Keiner der Berichte benennt einen Auslöser, und
weder der Hersteller noch die Community haben eine Ursache veröffentlicht.

### Überhitzung und Anbackungen

Ein teilweise verdeckter Temperatursensor misst zu niedrig, sodass die Heizung stärker
nachregelt, um einen Sollwert zu erreichen, den die Maschine für noch nicht erreicht
hält. Die Düse läuft dann oberhalb der vorgegebenen Temperatur.

Dass Filament an INDX-Düsenspitzen anbackt, wird unabhängig davon berichtet und hängt
nicht davon ab, ob die Kette dieser Seite zutrifft: Die PET-Familie allgemein und PCTG
im Besonderen bleibt Berichten zufolge bereitwillig an diesen Düsen haften. Ein Besitzer
führt das teilweise auf die Geometrie der Socke zurück und merkt an, dass sie fast bis
zur Spitze reicht, sodass Ablagerungen etwas zum Anhaften finden; er stellt dem
beschichtete Düsen gegenüber, die Material besser abweisen.

Dass Überhitzung dies verschlimmert, ist mechanistisch plausibel und entspricht dem, was
der einzige Bericht über die vollständige Kette beschreibt, ist aber eine Schlussfolgerung
und kein gemessener Zusammenhang.

### Fehlschlagen der Kalibrierung

Eine Ablagerung an der Düsenspitze verändert das, was der Offset-Sensor erfasst. Die
Werkzeug-Offset-Kalibrierung schlägt dann fehl. Das schließt an die vorhandene
Darstellung an, wonach Verschmutzung die Kalibrierung unterläuft, siehe
[Nachsickern beim Abtasten](oozing-during-probing-and-calibration.md) — ein anderer Weg
zum selben Ergebnis.

## Was zu tun ist

**Prüfen Sie die Socke, bevor Sie irgendetwas anderem nachgehen.** Wenn die
Offset-Kalibrierung an einem Werkzeug zu scheitern beginnt, das zuvor einwandfrei lief,
sehen Sie nach, ob die Socke über das Sensorfenster gewandert ist, bevor Sie den Sensor,
die Düse oder das Filament untersuchen. Das kostet Sekunden und ist umkehrbar.

**Setzen Sie sie wieder nach unten.** Jeder Bericht über das Wandern beschreibt, dass
die Socke einfach wieder in Position geschoben wurde, und keiner brauchte dafür ein
Ersatzteil.

**Entfernen Sie die Socke nicht, um das Wandern zu verhindern.** Das ist die naheliegende
Lösung und die falsche. Der Autor dieser Seite hat den Firmware-Quellcode gelesen und
geschlossen, dass die Temperaturmessung der Düse eine montierte Socke voraussetzt; ohne
sie dürfte der Messwert so weit abweichen, dass ein Thermal-Runaway-Fehler droht. Das
ist eine Schlussfolgerung aus dem Quellcode und kein Test, aber die Folgen sind ernst
genug, um sie zu beachten.

**Prüfen Sie die Socken von Zeit zu Zeit.** Ohne bekannten Auslöser und ohne Behebung
ist Nachsehen der einzige Schutz. Nach einem Klumpen lohnt es sich besonders: An der
Maschine des Autors wurde ein an der Düsenspitze haftender PCTG-Klumpen so fest durch
den Abstreifer gezogen, dass die Socke riss. Ersatzsocken lagen dem Bausatz nicht bei und
waren zum Zeitpunkt der Abfassung im Shop des Herstellers nicht zu finden; eine
gerissene Socke kann also Wartezeit bedeuten.

**Reinigen Sie die Spitze, wenn bereits Material festgebacken ist.** Siehe
[Nachsickern beim Abtasten](oozing-during-probing-and-calibration.md) für die
Vorsichtsmaßnahme beim Reinigen — Ablagerungen entfernen, nicht polieren.

## Überprüfung

`provisional` — die Kette stützt sich auf einen einzigen Bericht.

Was in unterschiedlichen Threads von unterschiedlichen Besitzern bestätigt wird:

- **Wandern der Socke, nun in zwei Threads.** Ein Bericht aus erster Hand im
  [Wartungs-Thread](https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/indx-maintenance/)
  beschreibt einen genau dadurch verursachten Thermal-Runaway-Fehler, und ein zweiter
  Besitzer musste in [einem späteren Thread](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/problems-with-nozzle-socks/) die Socke an zwei Werkzeugen wieder
  zurechtsetzen. Jener spätere Thread wurde vom Autor dieser Seite eröffnet, der
  bestätigende Bericht stammt aber von einem anderen Besitzer, weshalb er zählt. Für sich
  genommen erfüllt die Aussage zum Wandern nun `reported`; die Seite als Ganzes bleibt
  `provisional`, weil die Kette darunter das nicht tut.
- **Anbacken der PET-Familie und von PCTG an INDX-Düsenspitzen**, einschließlich der
  Beobachtung, dass die Geometrie der Socke dazu beiträgt, im
  [Wischer-Thread](https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/nozzle-wiper-vs-indx-offset-sensor/).

**Nicht** bestätigt ist die Ursachenkette, die beides verbindet: dass die Verdeckung die
Anbackungen antreibt und dass die Anbackungen die Kalibrierung scheitern lassen. Das ist
die eigene Beobachtung des Autors dieser Seite aus erster Hand, wiederholt an drei Düsen
einer Maschine — deshalb existiert diese Seite —, aber es bleiben eine Maschine und ein
Beobachter, und es wurde keine Temperatur gemessen. Beide Enden sind einzeln belegt; die
Verbindung dazwischen ist erschlossen.

Die Einschätzung, dass Düse oder Socke überarbeitet werden müssten, ist die
Schlussfolgerung dieses Autors und keine Herstellerposition; sie wird als Meinung
festgehalten, nicht als Befund. Ebenso drei spätere Ergänzungen, alle vom Autor selbst
und jeweils von einer einzigen Maschine: der Rat, die Socke nicht zu entfernen, die von
einem Klumpen zerrissene Socke und die nicht erhältlichen Ersatzteile.

Was diese Seite auf `reported` heben würde: ein zweiter Besitzer, der die vollständige
Abfolge — verschobene Socke, dann Überhitzung, dann Anbackungen, dann fehlgeschlagene
Kalibrierung — an einem zitierbaren Ort beschreibt. Eine Messung der tatsächlichen
gegenüber der vorgegebenen Düsentemperatur bei teilweise verdecktem Sensor wäre noch
besser und würde die Mitte der Kette auf `measured` heben.

## Verwandte Seiten

- [Ausfall der Offset-Sensorplatine](offset-sensor-board-failure.md) — der
  Wirbelstromsensor, mit dem dies häufig verwechselt wird
- [Nachsickern beim Abtasten](oozing-during-probing-and-calibration.md) — Verschmutzung,
  die die Kalibrierung auf anderem Weg unterläuft
- [Düsenhärte](nozzle-hardness.md) — weitere Defekte auf Düsenebene
