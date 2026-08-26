---
title:        G-Code
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
source_sha:   f2dfe45823da1450da472ed07835b34ae810a1313e26ed6198129dda39292835
---
# G-Code

Start-, End-, Schichtwechsel- und Werkzeugwechselblöcke; Platzhaltersyntax; und
Firmware-Verhalten, das vom Slicer aus nicht offensichtlich ist.

## Warum es diesen Bereich gesondert gibt

Der G-Code eines Werkzeugwechslers trägt mehr Last als der eines Druckers mit einem
einzigen Werkzeug. Der Startblock muss den Zustand für Werkzeuge herstellen, die noch
nicht montiert sind, der Werkzeugwechselblock läuft pro Druck hunderte Male, und ein
Platzhalter, der sich anders auflöst als erwartet, kann das Verhalten für alle
Werkzeuge auf einmal stillschweigend verändern.

Mehrere berichtete INDX-Fehler lassen sich auf G-Code- und Slicer-Verhalten statt auf
die Hardware zurückführen — darunter mindestens ein Fall, in dem ein Wert, der beim
Abtasten vor dem Druck verwendet wird, aus dem Filament des ersten Werkzeugs abgeleitet
wird statt aus dem des Werkzeugs, das die Arbeit verrichtet. Solche Effekte lohnen eine
präzise Dokumentation, weil sie unsichtbar bleiben, bis man weiß, wonach man suchen muss.

## Was hierher gehört

- Kommentierte Start- und Endblöcke, mit dem Grund für jede Zeile statt nur der Zeile
  selbst.
- Platzhaltersyntax und wozu sich jeder Platzhalter tatsächlich auflöst.
- Firmware-Verhalten: welche Befehle beachtet werden, welche ignoriert werden und
  welche Parameter in der Firmware festgelegt sind und sich nicht aus dem G-Code
  überschreiben lassen.
- Werkzeugwechsel- und Spülsequenzen.

## Konventionen für Seiten in diesem Bereich

Fügen Sie G-Code **wörtlich** in abgegrenzte Codeblöcke ein. Formatieren Sie ihn nicht
um, rücken Sie ihn nicht neu ein und „bereinigen“ Sie ihn nicht — Leerraum und
Reihenfolge können eine Rolle spielen, und ein Leser kopiert ihn direkt.

Es gibt zwei Fälle, und sie werden unterschiedlich behandelt.

Ein **Snippet** — ein paar Zeilen, die zur Übernahme angeboten werden — ist ein
Ratschlag, und jedes numerische Argument darin ist eine Druckeinstellung, für die die
übliche Regel gilt: vor der Veröffentlichung auf Hardware überprüft, oder benannt, aber
mit zurückgehaltenem Argument.

Ein **vollständiges Profil**, wörtlich wiedergegeben und kommentiert, ist ein Artefakt
und kein Ratschlag. Seine Literale sind Teil dessen, was dokumentiert wird, und werden
unverändert wiedergegeben. Eine solche Seite wird als `measured` eingestuft, nennt die
Firmware-Version, aus der das Profil stammt, und gibt an, ob es die ausgelieferte
Voreinstellung oder die Anpassung einer Person ist — das sind sehr unterschiedliche
Aussagen. Entnehmen Sie einem solchen Profil keinen Wert, um ihn als Empfehlung
darzustellen: die Wiedergabe einer Voreinstellung beschreibt, was die Maschine tut,
während eine Empfehlung ein Ratschlag ist — und ein Ratschlag braucht die Überprüfung,
die Ratschläge erfordern.

## Seiten

- **[Kommentierter Start-, Schicht- und Werkzeugwechsel-G-Code](indx-profile-gcode.md)**
  — ein vollständiges, funktionierendes INDX-Profil, wörtlich wiedergegeben und Zeile
  für Zeile kommentiert, wobei jeder Befehl gegen den Firmware-Quellcode geprüft wurde,
  der ihn implementiert.
