---
title:        Kalibrierung
confidence:   unknown
updated:      2026-08-24
author:       hyiger
printer:      unknown
toolhead:     unknown
hotend:       unknown
nozzle:       unknown
firmware:     unknown
sources:      []
superseded_by:
source_sha:   c507e2cfa75ec89908f532abfc672b8fae935ef10d03d51602b3e49895e5994e
---
# Kalibrierung

Werte pro Filament und pro Düse, jeweils erfasst mit der Hardware und der Methode,
mit der sie gemessen wurden.

!!! danger "Jede Zahl hier wird vor der Veröffentlichung von einem Menschen überprüft"
    Kein Kalibrierwert gelangt aus einem Forenbeitrag, aus einer plausiblen
    Schlussfolgerung oder aus einem Tool auf diese Website. Jemand führt den Test
    durch, hält das Ergebnis fest und nennt die Hardware, auf der er ihn durchgeführt
    hat.

    Das ist die Regel, von der die Website nicht abweicht. Eine falsche
    Düsentemperatur, die unter dem Namen einer Person veröffentlicht wird, verursacht
    eine Verstopfung im Drucker eines Fremden.

## Warum der Hardware-Kontext verbindlich ist

Ein Kalibrierwert gilt für ein bestimmtes Filament **und** eine bestimmte Düse
**und** oft auch einen bestimmten Drucker. Ein Extrusionsmultiplikator, der an einer
0.4mm Diamondback gemessen wurde, lässt sich nicht auf eine 0.6mm CHT übertragen —
andere Geometrie, anderer Wärmeübergang, anderer Fluss. Insbesondere die
High-Flow-Düsengeometrie des INDX leitet Wärme anders als der Nextruder, von dem
viele Besitzer kommen.

Deshalb nennt jede Seite hier `printer`, `toolhead`, `hotend`, `nozzle` und
`firmware` in ihrem Front Matter. Weicht Ihre Hardware in einem dieser Punkte ab,
behandeln Sie den Wert als Ausgangspunkt und überprüfen Sie ihn erneut, statt ihn
einfach zu übernehmen.

## Was hierher gehört

- Extrusionsmultiplikator, Pressure Advance, Schrumpfkompensation, maximale
  volumetrische Geschwindigkeit — jeweils mit dem Test, aus dem sie abgeleitet wurden.
- Temperaturbereiche, die tatsächlich durchgefahren wurden, nicht die vom Spulenetikett.
- Retraktionswerte, mit dem Hinweis, dass diese stark maschinenspezifisch sind.

## Was nicht

Werte, die von einer anderen Website, aus einer Slicer-Voreinstellung oder aus einem
Forenbeitrag übernommen wurden, der seine Methode nicht beschrieben hat. Das sind
Hinweise, die jemand testen kann, keine Einträge.

!!! note "Vorerst leer"
    Hier steht noch nichts. Die Kalibrierung ist genau wegen der Überprüfungsregel
    der Bereich, der sich am langsamsten füllt, und das ist der beabsichtigte
    Kompromiss.

    Beiträge, die einen Wert von `provisional` nach `measured` heben — indem der Test
    durchgeführt und die Hardware dokumentiert wird —, sind das Wertvollste, was
    jemand beisteuern kann. Siehe [Mitwirken](../contributing.md).
