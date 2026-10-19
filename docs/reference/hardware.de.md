---
title:        Hardware
confidence:   unknown
updated:      2026-10-18
author:       hyiger
printer:      Core One, Core One Plus, Core One L
toolhead:     INDX
hotend:       unknown
nozzle:       unknown
firmware:     unknown
sources:
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/core-one-l-with-indx-now-available-assembled-and-upgrade/
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/prusa-core-one-gen-2-indx-shipping-has-started-complete-printers-open-for-orders/
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/prusa-indx-update-shipping-starts-this-week/
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.9.1
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.9.2
  - https://help.prusa3d.com/downloads/core-one-indx
  - https://help.prusa3d.com/guide/4-indx-toolhead-side-filament-sensors_1096247
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/update-kit-from-indx-4t-to-8t/
  - https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/sourcing-tool-dock-hardware/
superseded_by:
source_sha:   4c9f9b3567bede0a88b46bbcaef447293411c2635e03c7e4d5c90984be771420
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

Bei der Core One selbst verkauft Prusa den kompletten INDX-Drucker als Core One+
(Gen 2), eine Revision, zu deren Änderungen neue Riemen, Riemenscheiben und
Ausgleichselemente für die Wärmeausdehnung gehören. Er ist fertig montiert oder als
Bausatz erhältlich, mit vier oder acht Werkzeugen, und Prusa hat die Gen-2-Teile
außerdem der ersten Charge seiner INDX-Umbausätze beigelegt; eine umgebaute Core One
kann also zu jeder der beiden Generationen gehören. Die Release Notes führen sie
getrennt auf: Die stabile Firmware 6.9.1, veröffentlicht am 25. September 2026, nennt
die Core One+ (Gen 2) INDX und die Core One/+ INDX als die Maschinen, die sie
unterstützt, und 6.9.2, veröffentlicht am 7. Oktober 2026, nennt dieselben beiden. Die
Firmware 7.0.0 für den INDX, datiert auf den 15. Oktober 2026, war bis zum 18. Oktober
nur auf Prusas Download-Seite erschienen, nicht als Release auf GitHub. Dort steht sie
unter einem einzigen Eintrag Core One INDX, auf einer Seite mit der Überschrift
Core One/+ INDX, und ihre Release Notes führen die beiden Generationen nicht getrennt
auf. Dieselbe Seite enthält eine eigene 7.0.0 für die Core One L+, datiert auf den
5. Oktober 2026, deren Release Notes den INDX überhaupt nicht erwähnen. Keines dieser
Releases nennt eine Core One L mit INDX. Lassen Sie zwischen den Generationen
dieselbe Sorgfalt walten wie zwischen den Modellen, wo immer ein Befund die Riemen,
ihre Riemenscheiben oder die Ausgleichselemente des Betts betrifft, die zu den Teilen
gehören, die Gen 2 ändert.

**Vier oder acht Werkzeuge.** Prusas Produktseite beschreibt die beiden Satzgrößen so,
dass sie sich Smart Head und Docking-Hardware teilen und sich nur darin unterscheiden,
wie viele passive Werkzeuge beiliegen. Besitzer von Vier-Werkzeug-Sätzen der Founders
Edition berichten bei ihren Sätzen von einem weiteren Unterschied, der zählt, wenn Sie
später erweitern: Der zweite seitliche Filamentsensor, der die Werkzeuge fünf bis acht
bedient, lag nicht im Karton. Auch Prusas eigener Vier-Werkzeug-Satz lässt ihn weg:
Prusas Montageanleitung sagt Erbauern eines Vier-Werkzeug-Satzes, dass nur die linke
Sensorplatine, die mit zwei Anschlüssen, im Karton liegt, und die Anleitung zur
Founders Edition sagt dasselbe über deren Satz. Prusa verkauft den rechten Sensor
inzwischen einzeln. Die [Montagehinweise](assembly-notes.md) beschreiben, was das
Ergänzen von Werkzeugen erfordert.

Quelle ist die [datierte Ankündigung](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/core-one-l-with-indx-now-available-assembled-and-upgrade/) des Herstellers vom 27. August 2026; sie
ist es, die Verfügbarkeit und Liefertermin festhält. Die Produktseiten für den
[fertig montierten Drucker](https://www.prusa3d.com/en/product/prusa-core-one-l-indx-8-tool/)
und den [Umbausatz](https://www.prusa3d.com/product/indx-8-tool-conversion-kit-for-core-one-l/)
sind nur als bequeme Verweise angegeben — Shop-Texte ändern sich, sie sind nicht der
Beleg. Die Angaben zu Gen 2 stammen aus Prusas eigenem
[Startbeitrag zum Gen-2-INDX](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/prusa-core-one-gen-2-indx-shipping-has-started-complete-printers-open-for-orders/)
und seiner [Versandankündigung](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/prusa-indx-update-shipping-starts-this-week/),
die Firmware-Bezeichnungen aus den Releases
[6.9.1](https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.9.1) und
[6.9.2](https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.9.2) und, für
7.0.0, von Prusas [Download-Seite](https://help.prusa3d.com/downloads/core-one-indx) in
ihrem Stand vom 18. Oktober 2026. Der Unterschied bei den Sätzen der Founders Edition
ist das, was deren Besitzer berichten, in
[einem Thread über die Erweiterung eines Vier-Werkzeug-Satzes](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/update-kit-from-indx-4t-to-8t/)
und in [einem über die Beschaffung von Dock-Hardware](https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/sourcing-tool-dock-hardware/).
Dass auch Prusas Vier-Werkzeug-Satz der Sensor fehlt, steht im
[Kapitel zu den seitlichen Filamentsensoren](https://help.prusa3d.com/guide/4-indx-toolhead-side-filament-sensors_1096247)
von Prusas Anleitung; dasselbe Kapitel der Anleitung zur Founders Edition sagt dasselbe
über den Satz der Founders Edition und bestätigt damit auch die Meldungen der
Besitzer. Der Wortlaut der Produktseite ist so wiedergegeben, wie ein Besitzer ihn im
Thread über die Erweiterung eines Vier-Werkzeug-Satzes weitergegeben hat, und nicht
dem Shop entnommen.

!!! note "`provisional` — nur dieser Abschnitt"
    Die Seite als Ganzes ist eine ungeprüfte Rumpfseite und deklariert
    `confidence: unknown`. Dieser Abschnitt ist die Ausnahme und trägt seine eigene
    Stufe, damit er nicht außerhalb des Konfidenzmodells der Website veröffentlicht wird.

    `provisional` ist die ehrliche Stufe für die Core One L: Eine Quelle stützt sie, die
    Ankündigung des Herstellers. Die Produktseiten sind bequeme Verweise und
    ausdrücklich kein Beleg. Und der 5. November 2026 ist eine zum Zeitpunkt der
    Ankündigung **erklärte Absicht** und kein verstrichenes Datum — behandeln Sie die
    Lieferangabe als Plan und die Verfügbarkeitsangabe als zutreffend für August 2026,
    nicht für den Zeitpunkt, zu dem Sie dies lesen. Der Absatz zu Gen 2 stützt sich auf
    mehr — Prusas eigene Beiträge und Release Notes —, ebenso der Absatz zu den
    Satzgrößen, mit Besitzern in zwei getrennten Threads und der eigenen Anleitung
    dieser Edition für die Founders Edition und Prusas Anleitung für Prusas Satz; beide
    stehen aber in diesem Abschnitt und übernehmen seine Stufe. Die Bezeichnungen zu
    7.0.0 stützen sich auf eine Download-Seite, die Prusa an Ort und Stelle ändert,
    nicht auf ein getaggtes Release, und sollten erneut geprüft werden, sobald ein
    Release auf GitHub erscheint.

## Überprüfung

`unknown` — nichts anderes auf dieser Seite wurde geprüft. Es sollte weder eine
Komponentenspezifikation noch eine Revisionskennung oder ein Messwert von hier
übernommen werden, solange dieser Hinweis nicht entfernt und das Feld confidence
gesetzt ist.

## Verwandte Seiten

- [Referenz-Übersicht](index.md)
- [Probleme](../issues/index.md) — dort werden Ausfälle dieser Komponenten dokumentiert
