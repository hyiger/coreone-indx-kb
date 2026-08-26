---
title:        Referenz
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
source_sha:   07b136b727d89e8e9d613a6e8d78aaca11aa1494da85d1e91ec6f9b9b7810fd5
---
# Referenz

Hardware-Spezifikationen, Werkzeugnummerierung, Montagehinweise und das Vokabular,
das der Rest der Website voraussetzt.

## Seiten

- **[Montagehinweise](assembly-notes.md)** — was Erbauer gern gewusst hätten, bevor
  sie mit dem Umbau begonnen haben: was im Voraus zu drucken und bereitzulegen ist,
  die wenigen Schritte, die immer wieder für Probleme sorgen, und die Dock-Magnete.
- **[Kompatibilität der Druckplatten](build-plate-compatibility.md)** — übergroße
  Druckbleche von Drittanbietern kommen an den Werkzeugdocks nicht mehr vorbei,
  sobald diese montiert sind, obwohl sie auf einen serienmäßigen Core One
  einwandfrei passen.
- **[Hardware](hardware.md)** — Komponenten, Revisionen und was jeder Sensor
  tatsächlich tut.

## Was hierher gehört

Dauerhafte Fakten über die Maschine statt Erkenntnisse darüber, wie sie sich
fehlerhaft verhält. Komponentenbezeichnungen und Revisionen, Sensortypen und was sie
messen, Werkzeugnummerierung und Dock-Positionen, Identifikation von Steckern und
Kabeln, Versionsverlauf der Firmware.

Der Prüfstein dafür, ob etwas hierher und nicht zu
[Probleme](../issues/index.md) gehört, ist die Frage, ob es auf einer einwandfrei
funktionierenden Maschine immer noch zuträfe. „Der Offset-Sensor arbeitet nach dem
Wirbelstromprinzip“ ist Referenz. „Die Platine des Offset-Sensors fällt bei ungefähr
so vielen Bausätzen aus“ ist ein Problem.

## Warum dieser Bereich Gewicht hat

Ein großer Teil der INDX-Fehlersuche hängt davon ab, das richtige Teil zu benennen.
An der Einrichtung einer Maschine sind zwei verschiedene Sensoren beteiligt, sie
fallen mit sich überschneidenden Symptomen aus, und Besitzer verfolgen regelmäßig den
falschen — was Tage kostet. Das richtige Vokabular ist hier keine Pedanterie; es ist
das, was den Rest der Website überhaupt erst benutzbar macht.

Firmware-Versionsangaben sind aus demselben Grund wichtig. Das Verhalten hat sich über
Releases hinweg geändert, daher beschreibt eine Erkenntnis ohne zugehörige Version
möglicherweise eine Maschine, die es nicht mehr gibt.
