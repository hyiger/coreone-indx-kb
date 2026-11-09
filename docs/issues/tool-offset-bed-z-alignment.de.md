---
title:        Werkzeug-Offset-Kalibrierung schlägt fehl: Bett in Z nicht ausgerichtet
confidence:   provisional
updated:      2026-10-25
author:       hyiger
printer:      Core One
toolhead:     INDX
hotend:       unknown
nozzle:       unknown
firmware:     6.9.1-beta on the reported machine; the mechanism is not version-specific
sources:
  - https://help.prusa3d.com/article/tool-offset-failed-36130-core-one-indx_1089016
  - https://help.prusa3d.com/article/uneven-bed-31111-core-one-35111-core-one-l-36111-core-one-indx_856294
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1-beta/src/common/probe_analysis.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1-beta/src/marlin_stubs/G162.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/compare/v6.9.1-beta...v6.9.1
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/compare/v6.9.1...v6.9.2
  - https://help.prusa3d.com/downloads/core-one-indx
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5526
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5518
superseded_by:
source_sha:   25d74179e3ea5623d62e061c57eb3314116caeaf4545db166e92a8d2d79b3e2b
---
# Werkzeug-Offset-Kalibrierung schlägt fehl: Bett in Z nicht ausgerichtet

## Zusammenfassung

Die Werkzeug-Offset-Kalibrierung kann mit demselben Fehlercode wie eine defekte
Offsetsensor-Platine fehlschlagen, obwohl die Düsenspitzen sauber sind, der Sensor
sauber ist und kein Filament geladen ist, weil das Bett in Z nicht ausgerichtet ist.
Bei einem Besitzer auf 6.9.1-beta schlug die Kalibrierung von einem Durchlauf zum
nächsten an einem anderen Werkzeug fehl, und ein Ferritkern am Werkzeugkopfkabel
änderte nichts. Der Besitzer fuhr das Bett an das untere Ende seines Verfahrwegs, um
seine Ebene zurückzusetzen, was genau Z Alignment Calibration tut, und der Fehler
verschwand. Z Alignment Calibration kostet nichts und kann nichts verschlimmern;
führen Sie es also aus, bevor Sie die Sensorplatine oder die Wägezelle verdächtigen.

## Fehlercodes, die hierher führen

| Code | Anzeige am Drucker |
|---|---|
| [`36130`](https://help.prusa3d.com/article/tool-offset-failed-36130-core-one-indx_1089016) | Tool offset failed |
| [`36193`](../codes.md#36193) | Probing the tool offset sensor failed |

Es ist derselbe Code wie beim [Fehler der Offsetsensor-Platine](offset-sensor-board-failure.md).
Die Meldung am Bildschirm fordert Sie auf zu prüfen, ob die Düse sauber ist. Wenn Sie
das getan haben und nichts geladen ist, ist diese Seite das Nächste, was auszuschließen
ist.

Firmware, die aus hyiger/Prusa-Firmware-Buddy gebaut ist, meldet eine verworfene
Berührung auf dem Sensor stattdessen als `36193`, dort teilt sich dieser Fehler also
keinen Code mehr mit der Sensorplatine.

## Details

Die Werkzeug-Offset-Kalibrierung am INDX nimmt zwei Arten von Messungen vor. Der
berührungslose Sensor erfasst die Düsenposition in X und Y, ohne sie zu berühren. Die
Z-Messung ist eine physische Berührung: Das Bett fährt nach oben, bis die Düse auf dem
Sensorgehäuse aufliegt und die Wägezelle den Kontakt registriert. Am Core One ist jede
Z-Bewegung eine Bewegung des Betts, dieser Kontakt hängt also davon ab, dass der
Bettschlitten auf seinen Gewindespindeln frei läuft.

Die Firmware akzeptiert eine Berührung nicht allein aufgrund des Kontakts. Sie hält
die Position nach dem Kontakt kurz und prüft, ob die gemessene Kraft stabil bleibt.
Ändert sich die Kraft weiter, während sich eigentlich nichts bewegen sollte, wird die
Messung verworfen. Im seriellen Log zeigt sich das als Abtastung, die als nicht in
Ordnung eingestuft wird, mit dem Merkmal `angle_after` und einem negativen Wert. Die
Kalibrierung wiederholt den Versuch je Werkzeug eine feste Anzahl von Malen und bricht
dann mit dem obigen Code ab.

Ein Bettschlitten, dessen Seiten nicht im Gleichschritt sind, klemmt leicht auf seinen
Führungen. Wenn die Düse auf ihn drückt, setzt sich der klemmende Schlitten, statt
still zu halten, sodass die Kraft an der Düse nach dem Kontakt nachlässt. Genau dieses
Muster verwirft die Prüfung. Es passt auch dazu, dass der Fehler von einem Durchlauf
zum nächsten zwischen den Werkzeugen wandert: Jedes Werkzeug stellt den Kontakt bei
einer etwas anderen Betthöhe her, und ein verkanteter Schlitten klemmt nicht auf jeder
Höhe gleich.

Was diesen Fehler leicht fehldeuten lässt:

- **Die Düse ist sauber und nichts ist geladen**, die Oozing-Erklärung greift also
  nicht, und der Hinweis am Bildschirm führt ins Leere.
- **Es sieht nach Störungen aus.** Fehler, die kommen und gehen, an verschiedenen
  Werkzeugen, an einer Maschine, die ihren Wägezellen-Selbsttest besteht: So sieht ein
  Störungsproblem von außen aus, und an anderen Maschinen waren Störungen tatsächlich
  die Ursache, siehe [Wägezellen-Störungen](loadcell-emi-noise.md). Der Besitzer hat
  auf dieser Grundlage einen Ferritkern angebracht. Es machte keinen Unterschied. Wie
  sich die beiden unterscheiden lassen, steht im Tipp unten.
- **Es sieht nach einer defekten Sensorplatine aus.** Die Seite zur Sensorplatine
  beschreibt eine Kalibrierung, die mitten in der Werkzeugfolge fehlschlägt, wobei der
  Abbruchpunkt zwischen den Versuchen wandert. Dieser Fehler zeigt sich genauso. Der
  Unterschied liegt im Log: Bei einem Platinenfehler kommt gar keine Messung zustande,
  während hier Messungen erfasst und verworfen werden.
- **Nichts im normalen Ablauf weist auf das Bett hin.** Die Firmware bietet Z Alignment
  Calibration von sich aus nur an, wenn ein Bed-Leveling-Durchlauf die Oberfläche um
  mehr als einen festen Betrag außerhalb der Ebene findet. Ein Schlitten, der weniger
  als das verkantet ist, druckt annehmbar und löst das Angebot nie aus, und die
  Werkzeug-Offset-Kalibrierung nivelliert das Bett überhaupt nicht.
  [7.0.0](https://help.prusa3d.com/downloads/core-one-indx), veröffentlicht am
  15. Oktober 2026, führt unter ihren Neuerungen eine automatische Ausrichtung der
  Z-Achse bei unebenem Bett auf. Was sie auslöst, sagen die Versionshinweise nicht, und
  der Quellcode ist noch nicht veröffentlicht. Tritt sie an die Stelle jenes Angebots,
  bliebe ein Schlitten, der weniger als diesen Betrag verkantet ist, vermutlich weiterhin
  unbehandelt. Das ist erschlossen. Die Versionshinweise zu 7.0.1 und zu 8.0.0,
  veröffentlicht am 19. und 22. Oktober 2026, fügen dazu nichts hinzu, und noch kein
  Besitzer hat über das neue Verhalten berichtet.

### Was zu tun ist

1. **Führen Sie Z Alignment Calibration aus**, unter Control, dann Calibrations &
   tests. Der Vorgang referenziert Z, fährt das Bett bis an das untere Ende seines
   Verfahrwegs und drückt ein kurzes Stück über den mechanischen Anschlag hinaus,
   sodass der Z-Antrieb am Rahmen Schritte überspringt, bis der Schlitten gerade
   sitzt. Das ist es, was die Ausrichtung zurücksetzt. Der Besitzer beschrieb das
   eigene Vorgehen als das Fahren des Betts an den Boden des Druckers, um die Ebene
   zurückzusetzen; genau diesen Schritt führt der Vorgang aus. Führen Sie ihn auch
   unter 7.0.0 und späteren Versionen von Hand aus: Nichts in deren Versionshinweisen
   sagt, dass die automatische Ausrichtung diesen Fall abdeckt.
2. **Führen Sie die Werkzeug-Offset-Kalibrierung erneut aus.** An der gemeldeten
   Maschine war der Fehler danach verschwunden.
3. **Wenn sie weiterhin fehlschlägt**, empfiehlt der Artikel des Herstellers zum
   unebenen Bett, das Bett nach unten zu fahren, die Trapezmuttern zu lösen und zu
   prüfen, ob sie frei auf den Gewindespindeln laufen. Zeichnen Sie danach ein
   serielles Log auf und gehen Sie zur
   [Seite zur Sensorplatine](offset-sensor-board-failure.md).

!!! tip "Die Fehler unterscheiden"
    Mehrere Fehler teilen sich diesen Fehlercode, und das serielle Log trennt drei von
    ihnen. Gar keine Messung deutet auf die [Sensorplatine](offset-sensor-board-failure.md).
    Erfasste und mit `angle_after` verworfene Messungen bedeuten, dass unter der Düse
    etwas nachgibt: Filament an der Spitze oder der Bettschlitten. Bei sauberen Spitzen
    und ohne geladenes Filament bleibt der Schlitten übrig. Reinigen und entladen Sie,
    bevor Sie etwas in das Log hineinlesen, denn
    [Oozing](oozing-during-probing-and-calibration.md) wird auf dieselbe Weise verworfen.
    [Störungen an der Wägezelle](loadcell-emi-noise.md) lassen Berührungen ebenfalls
    verwerfen, und dieser Seite liegt kein Log von Standard-Firmware vor, das zeigt,
    welche Prüfung sie verwirft. Achten Sie daher darauf, wann und wie es fehlschlägt. In
    den Berichten auf jener Seite scheitert die Kalibrierung bei Störungen zu
    Druckbeginn, während sie aus dem Menü gelingt, und man sieht die Düse zu früh
    anhalten. Ein Besitzer auf Standard-Firmware 6.9.2 beendete die Fehler, die nach dem
    Neuverlegen der Kabel geblieben waren, indem er die Statusleuchte am Bett im Menü
    ausschaltete
    ([Firmware-Issue 5526](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5526)).
    Seine neueste Zusammenfassung in
    [Firmware-Issue 5518](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5518)
    führt seine vollständige Behebung auf das Neuverlegen der Kabel, Ferritkerne an den
    Kabeln der Bett- und der Kammerbeleuchtung und eine niedrigere Abtasttemperatur im
    Start-G-Code zurück. Das Ausschalten der Leuchte steht nicht auf dieser Liste, obwohl
    er das Kabel der Bettbeleuchtung für die wahrscheinlichste Quelle hält; sein Ergebnis
    zeigt also nicht, dass das Ausschalten nötig ist. Ein zweiter Besitzer in Issue 5526,
    bei dem Ferritperlen nicht
    halfen, berichtet, dass das Ausschalten der Leuchte bisher anscheinend jedes Mal
    hilft. `provisional`, zwei Besitzer in einem Issue.

## Verifizierung

`provisional`: eine Maschine, ein Besitzer, und der Bericht erreichte den Autor direkt
während der Hilfe bei der Diagnose und nicht über einen öffentlichen Thread, sodass es
für den Bericht selbst keinen Link gibt. Was festgehalten ist: Auf 6.9.1-beta schlug
die Werkzeug-Offset-Kalibrierung wiederholt fehl, wobei das fehlschlagende Werkzeug
zwischen den Durchläufen wechselte, mit sauberen Düsenspitzen, sauberer Sensorplatine
und ohne geladenes Filament. Das Log zeigte Berührungen, die erfasst und mit
`angle_after` verworfen wurden. Ein Ferritkern am Werkzeugkopfkabel machte keinen
Unterschied. Nachdem der Besitzer das Bett an das untere Ende seines Verfahrwegs
gefahren hatte, um seine Ebene zurückzusetzen, war der Fehler verschwunden.

Der obige Mechanismus ist die Lesart des Autors vom Abtast-Klassifizierer der Firmware,
abgeglichen mit diesem Log. Er passt, ist aber weder vom Hersteller bestätigt noch an
einer anderen Maschine reproduziert. Die Firmware-Referenzen sind der Klassifizierer in
[probe_analysis.cpp](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1-beta/src/common/probe_analysis.cpp)
und der Ausrichtungsvorgang in
[G162.cpp](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1-beta/src/marlin_stubs/G162.cpp),
beide am Tag 6.9.1-beta. Keine der beiden Dateien hat sich in der
[stabilen 6.9.1](https://github.com/prusa3d/Prusa-Firmware-Buddy/compare/v6.9.1-beta...v6.9.1)
oder in [6.9.2](https://github.com/prusa3d/Prusa-Firmware-Buddy/compare/v6.9.1...v6.9.2)
geändert, die am INDX nur die Filament-Presets ändert; die Lesart gilt also für beide.
Prusa hat den Quellcode von
[7.0.0](https://help.prusa3d.com/downloads/core-one-indx), 7.0.1 und 8.0.0 noch nicht
veröffentlicht, daher lässt sich nicht prüfen, ob sich eine der beiden Dateien darin
geändert hat. Die Versionshinweise zu 7.0.0 nennen eine automatische Ausrichtung der
Z-Achse bei unebenem Bett und sagen nichts zur Werkzeug-Offset-Kalibrierung; die zu
7.0.1 und 8.0.0 erwähnen keines von beiden. Die Berichte zur Statusleuchte stammen von
einem Besitzer auf Standard-Firmware 6.9.2 und einem zweiten, der seine Firmware nicht
nennt, beide in
[Firmware-Issue 5526](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5526);
der erste von ihnen hat seine vollständige Behebung später in
[Firmware-Issue 5518](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5518) zusammengefasst.
Der Ersteller von Issue 5526 hat zwar auch aufgezeichnet, welche Prüfung die Berührungen
verwarf, aber auf einer selbst veränderten Firmware; diese Seite verwendet das daher
nicht. Wozu Z Alignment Calibration dient und der Menüpfad stammen aus dem
[Artikel des Herstellers zum unebenen Bett](https://help.prusa3d.com/article/uneven-bed-31111-core-one-35111-core-one-l-36111-core-one-indx_856294).

Wenn Ihre Maschine dem entspricht und die Z-Ausrichtung es behebt, ist dieser zweite
Bericht das, was diese Seite auf `reported` hebt. Siehe [Mitwirken](../contributing.md).

## Verwandte Seiten

- [Werkzeug-Offset-Kalibrierung schlägt fehl: kontaktloser Offset-Sensor](offset-sensor-board-failure.md).
  Derselbe Fehlercode. Gehen Sie dorthin, wenn die Z-Ausrichtung nichts ändert, und
  zeichnen Sie zuerst ein Log auf.
- [Probing schlägt fehl oder die Düse berührt das Bett nie](loadcell-emi-noise.md).
  Der Störungsfehler, mit dem dieser verwechselt wurde.
- [Oozing verdirbt Bettabtastung und Werkzeugkalibrierung](oozing-during-probing-and-calibration.md).
  Der andere Grund, aus dem eine Berührung verworfen wird. Schließen Sie ihn durch
  Reinigen und Entladen zuerst aus.
