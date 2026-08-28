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
sources:
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/core-one-l-with-indx-now-available-assembled-and-upgrade/
superseded_by:
source_sha:   5144299989d66f085f0461cbb35f1c63566b64fb67ff207016e8fba45fa47d46
---
# Hardware

!!! warning "Rumpfseite"
    Diese Seite ist ein Platzhalter. Sie existiert, um zu belegen, dass die Vorlage,
    die Front-Matter-Konvention und die Navigation durchgängig funktionieren. Es wurden
    noch keine Spezifikationen erfasst, und nichts weiter unten wurde überprüft —
    **ausgenommen** die Maschinen, für die der INDX angeboten wird; dieser
    Abschnitt trägt seine eigene Stufe inline.

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

## Maschinen, für die der INDX angeboten wird

Der INDX wird sowohl als Umbausatz für eine bereits vorhandene Maschine als auch ab
Werk in einem vollständigen Drucker verbaut verkauft. Stand August 2026 führt der
Hersteller ihn für die Core One und neuerdings für die größere Core One L — letztere
als fertig montierten Achtwerkzeug-Drucker oder als Umbausatz für eine vorhandene L,
wobei die Auslieferung laut Angabe am 5. November 2026 beginnt.

Das ist für die Lektüre des übrigen Angebots hier von Bedeutung. Die Seiten halten in
ihrem `printer:`-Feld fest, von welcher Maschine ein Befund stammt, und ein Befund von
einer Core One überträgt sich nicht automatisch auf eine L: Der Bauraum unterscheidet
sich, und die Montagehinweise beschreiben ein anderes Chassis.

Quelle ist die [datierte Ankündigung](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/core-one-l-with-indx-now-available-assembled-and-upgrade/) des Herstellers vom 27. August 2026; sie
ist es, die Verfügbarkeit und Liefertermin festhält. Die Produktseiten für den
[fertig montierten Drucker](https://www.prusa3d.com/en/product/prusa-core-one-l-indx-8-tool/)
und den [Umbausatz](https://www.prusa3d.com/product/indx-8-tool-conversion-kit-for-core-one-l/)
sind nur als bequeme Verweise angegeben — Shop-Texte ändern sich, sie sind nicht der
Beleg.

!!! note "`provisional` — nur dieser Abschnitt"
    Die Seite als Ganzes ist eine ungeprüfte Rumpfseite und deklariert
    `confidence: unknown`. Dieser Abschnitt ist die Ausnahme und trägt seine eigene
    Stufe, damit er nicht außerhalb des Konfidenzmodells der Website veröffentlicht wird.

    `provisional` ist die ehrliche Stufe: Eine Quelle stützt ihn, die Ankündigung des
    Herstellers. Die Produktseiten sind bequeme Verweise und ausdrücklich kein Beleg.
    Und der 5. November 2026 ist eine zum Zeitpunkt der Ankündigung **erklärte Absicht**
    und kein verstrichenes Datum — behandeln Sie die Lieferangabe als Plan und die
    Verfügbarkeitsangabe als zutreffend für August 2026, nicht für den Zeitpunkt, zu dem
    Sie dies lesen.

## Überprüfung

`unknown` — nichts anderes auf dieser Seite wurde geprüft. Es sollte weder eine
Komponentenspezifikation noch eine Revisionskennung oder ein Messwert von hier
übernommen werden, solange dieser Hinweis nicht entfernt und das Feld confidence
gesetzt ist.

## Verwandte Seiten

- [Referenz-Übersicht](index.md)
- [Probleme](../issues/index.md) — dort werden Ausfälle dieser Komponenten dokumentiert
