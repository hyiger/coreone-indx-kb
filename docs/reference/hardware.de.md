---
title:        Hardware
confidence:   unknown
updated:      2026-08-28
author:       hyiger
printer:      Core One, Core One L
toolhead:     INDX
hotend:       unknown
nozzle:       unknown
firmware:     unknown
sources:      []
superseded_by:
source_sha:   ec7d643b4e4e630266cde8885e101948788b244ae651d6296bcd37885f33334d
---
# Hardware

!!! warning "Rumpfseite"
    Diese Seite ist ein Platzhalter. Sie existiert, um zu belegen, dass die Vorlage,
    die Front-Matter-Konvention und die Navigation durchgängig funktionieren. Nichts
    weiter unten wurde überprüft, und es wurden noch keine Spezifikationen erfasst.

## Zusammenfassung

Referenz für die physischen Komponenten eines Core One mit INDX: wie die einzelnen
Teile heißen, was die einzelnen Sensoren messen und welche Revision Sie vor sich haben.

## Details

Vorgesehene Inhalte, noch nichts davon geschrieben:

- **Werkzeugkopf** — der intelligente Kopf, seine Induktionsspule und wie das
  Vorhandensein eines Werkzeugs erfasst wird.
- **Werkzeuge und Docks** — Nummerierung, Dock-Positionen, Magnete und Befestigungsmaterial.
- **Sensoren** — die Wägezelle für den Z-Kontakt zum Druckbett und der davon getrennte
  berührungslose Induktivsensor für die Werkzeug-Offsets. Das sind unterschiedliche
  Teile mit unterschiedlichen Fehlerbildern, die häufig verwechselt werden.
- **Controller** — Platinenrevisionen und wie Sie Ihre bestimmen, da sich manches
  berichtete Verhalten je nach Revision unterscheidet.
- **Verkabelung** — der Hauptkabelbaum des Werkzeugkopfs und seine Stecker.
- **Düsen** — Geometrien, Materialien und Oberflächenbehandlungen.

## Maschinen, auf denen der INDX ausgeliefert wird

Der INDX wird sowohl als Umbausatz für eine bereits vorhandene Maschine als auch ab
Werk in einem vollständigen Drucker verbaut verkauft. Stand August 2026 führt der
Hersteller ihn für die Core One und neuerdings für die größere Core One L — letztere
als fertig montierten Achtwerkzeug-Drucker oder als Umbausatz für eine vorhandene L,
wobei die Auslieferung laut Angabe am 5. November 2026 beginnt.

Das ist für die Lektüre des übrigen Angebots hier von Bedeutung. Die Seiten halten in
ihrem `printer:`-Feld fest, von welcher Maschine ein Befund stammt, und ein Befund von
einer Core One überträgt sich nicht automatisch auf eine L: Der Bauraum unterscheidet
sich, und die Montagehinweise beschreiben ein anderes Chassis.

Quelle ist die Ankündigung des Herstellers samt Produktseiten:
[fertig montiert](https://www.prusa3d.com/en/product/prusa-core-one-l-indx-8-tool/) ·
[Umbausatz](https://www.prusa3d.com/product/indx-8-tool-conversion-kit-for-core-one-l/).
Anders als der Rest dieser Seite ist dieser Abschnitt belegt und kein Platzhalter.

## Überprüfung

`unknown` — nichts anderes auf dieser Seite wurde geprüft. Es sollte weder eine
Komponentenspezifikation noch eine Revisionskennung oder ein Messwert von hier
übernommen werden, solange dieser Hinweis nicht entfernt und das Feld confidence
gesetzt ist.

## Verwandte Seiten

- [Referenz-Übersicht](index.md)
- [Probleme](../issues/index.md) — dort werden Ausfälle dieser Komponenten dokumentiert
