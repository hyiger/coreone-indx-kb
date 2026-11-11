---
title:        Hardware
confidence:   unknown
updated:      2026-11-10
author:       hyiger
printer:      Core One, Core One Plus, Core One L
toolhead:     INDX
hotend:       unknown
nozzle:       unknown
firmware:     release naming checked for 6.9.1, 6.9.2, 7.0.0, 7.0.1, 8.0.0 and 8.0.1; otherwise unknown
sources:
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/core-one-l-with-indx-now-available-assembled-and-upgrade/
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/prusa-core-one-gen-2-indx-shipping-has-started-complete-printers-open-for-orders/
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/prusa-indx-update-shipping-starts-this-week/
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.9.1
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.9.2
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v7.0.0
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v7.0.1
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v8.0.0
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v8.0.1
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/src/common/printer_variant/printer_variant.hpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/CMakeLists.txt
  - https://help.prusa3d.com/downloads/core-one-indx
  - https://help.prusa3d.com/guide/4-indx-toolhead-side-filament-sensors_1096247
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/update-kit-from-indx-4t-to-8t/
  - https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/sourcing-tool-dock-hardware/
superseded_by:
source_sha:   f5d7de2e1bf8f70c3831f752f0242ede35739ca11ee2927c4d28ad775b4930e3
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
wobei die Auslieferung laut Angabe am 5. November 2026 beginnt. Dieses Datum ist
verstrichen, ohne dass im Ankündigungs-Thread eine Auslieferung gemeldet wurde. Am
27. Oktober gaben Besitzer dort E-Mails wieder, die ihre Bestellungen Chargen zuordnen,
die am 30. November oder, bei einer späteren Charge, um den 14. Dezember beginnen
sollen; Stand 5. November war zwei Besitzern des Umbausatzes für die L, einer davon mit
einer Bestellung vom ersten Tag, noch überhaupt keine Charge zugeteilt worden. Bis zum
10. November hatten zwei weitere Besitzer dieses Bausatzes, die ebenfalls am ersten Tag
bestellt hatten, noch immer keine. Besitzer in diesem Thread und im
[Haupt-Thread zum INDX-Versand](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/prusa-indx-update-shipping-starts-this-week/)
gaben außerdem einen neuen Wortlaut auf Prusas Seite mit Versandinformationen wieder:
Sommerbestellungen, die noch keine Chargennummer haben, sollen Anfang 2027 eine
erhalten und dann bearbeitet werden.

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
Firmware-Versionen 7.0.0, 7.0.1 und 8.0.0 erschienen zuerst auf Prusas Download-Seite,
dort datiert auf den 15., 19. und 22. Oktober 2026, unter einem einzigen Eintrag
Core One INDX, dessen Release Notes die Generationen nicht trennten. Am 3. November 2026
folgten für alle drei die Releases auf GitHub, und diese nennen die beiden getrennt.
7.0.1, eine einzige Korrektur für ein Einfrieren beim Start, ist allein für die
Core One+ (Gen 2) INDX und die Core One/+ INDX bestimmt. 7.0.0 und 8.0.0 sind jeweils
ein einziges Release für Prusas gesamte Produktpalette, dessen Liste der Maschinen die
Core One+ (Gen 2) INDX und die Core One INDX neben der einfachen Core One+ (Gen 2) und
Core One, der Core One L+ und Core One L und den übrigen führt. Jedes der drei
liefert eine einzige INDX-Firmwaredatei für beide Generationen, und 7.0.0 und 8.0.0
enthalten eine eigene Datei für die einfache Core One; im Quellcode ist die Generation
eine Reihe von Schaltern in der Hardwarekonfiguration und kein eigener Build (siehe die
[Montagehinweise](assembly-notes.md)). 8.0.1, am selben Tag erschienen, ist nur für die
Familien XL und MINI bestimmt, womit 8.0.0 Stand 8. November 2026 die neueste
INDX-Firmware ist. Prusas Release Notes zu 7.0.0 und 7.0.1 sagen, beide seien vor allem
der Vollständigkeit halber und zur Bereitstellung ihres Quellcodes veröffentlicht worden,
und verweisen Besitzer direkt auf 8.0.0. Der Sprung von 7 auf 8 innerhalb weniger Wochen
folgt aus einer Versionierungsregel, die die Release Notes zu 7.0.0 einführen: Die erste
Stelle steigt mit jedem Release, das vom Hauptzweig der Entwicklung abgezweigt wird.

Keines dieser Releases nennt eine Core One L mit INDX. Die L und L+ erhalten in 7.0.0
und in 8.0.0 eine einzige Firmwaredatei ohne INDX im Namen, und die Download-Seite
führte für die L+ eigene Einträge zu 7.0.0 und 8.0.0 und listet Stand 8. November 2026
die einfache L mit genau diesen beiden Einträgen und ihren gemeinsamen L/L+-Dateien;
keine ihrer Release Notes erwähnt den INDX. Diese Seite bietet auch keine
INDX-Firmware für die L an, obwohl ihr Website-Menü auf einen Drucker Core One L+ INDX
im Shop verweist. Prusas Firmware-Quellcode enthält durchaus ein INDX-Build-Ziel für
die Core One L, schon in 6.9.1 vorhanden und weiterhin in 8.0.0; das zeigt, dass es
diese Arbeit gibt, nicht, wann Firmware dafür erscheint. Lassen Sie zwischen den
Generationen dieselbe Sorgfalt walten wie zwischen den Modellen, wo immer ein Befund
die Riemen, ihre Riemenscheiben oder die Ausgleichselemente des Betts betrifft, die zu
den Teilen gehören, die Gen 2 ändert.

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
ist es, die Verfügbarkeit und Liefertermin festhält; die Chargen, die Besitzern genannt
wurden, und die Bausatz-Bestellungen ohne Charge stammen aus späteren Beiträgen im selben
Thread, so wie die Besitzer sie wiedergeben. Der Wortlaut zu Anfang 2027 ist so
wiedergegeben, wie Besitzer ihn am 9. und 10. November 2026 in diesem Thread und im
Haupt-Thread zum Versand weitergaben; diese Seite hat die Seite mit
Versandinformationen, die Prusa an Ort und Stelle ändert, nicht selbst gelesen. Die
Produktseiten für den
[fertig montierten Drucker](https://www.prusa3d.com/en/product/prusa-core-one-l-indx-8-tool/)
und den [Umbausatz](https://www.prusa3d.com/product/indx-8-tool-conversion-kit-for-core-one-l/)
sind nur als bequeme Verweise angegeben — Shop-Texte ändern sich, sie sind nicht der
Beleg. Die Angaben zu Gen 2 stammen aus Prusas eigenem
[Startbeitrag zum Gen-2-INDX](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/prusa-core-one-gen-2-indx-shipping-has-started-complete-printers-open-for-orders/)
und seiner [Versandankündigung](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/prusa-indx-update-shipping-starts-this-week/),
die Firmware-Bezeichnungen aus den Releases auf GitHub zu
[6.9.1](https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.9.1),
[6.9.2](https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.9.2),
[7.0.0](https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v7.0.0),
[7.0.1](https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v7.0.1),
[8.0.0](https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v8.0.0) und
[8.0.1](https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v8.0.1) und den
daran angehängten Firmwaredateien, die letzten vier veröffentlicht am 3. November 2026.
Die Daten im Oktober und die Einträge zur L+ stammen von Prusas
[Download-Seite](https://help.prusa3d.com/downloads/core-one-indx) in ihrem Stand vom
18. und 25. Oktober 2026, die Auflistung der einfachen L und das Fehlen einer INDX-Firmware
für die L von derselben Seite am 8. November 2026. Dass die Generation eine Reihe von
Schaltern in der Hardwarekonfiguration ist, stammt aus dem
[Quellcode von 8.0.0](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/src/common/printer_variant/printer_variant.hpp),
das Build-Ziel für die L aus dessen
[CMakeLists.txt](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/CMakeLists.txt),
abgeglichen mit dem Tag 6.9.1. Der Unterschied bei den Sätzen der Founders Edition
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
    ausdrücklich kein Beleg. Und der 5. November 2026 war zum Zeitpunkt der Ankündigung
    eine **erklärte Absicht**; er ist inzwischen verstrichen, ohne dass eine Auslieferung
    gemeldet wurde, und die seither genannten Chargen-Termine geben Besitzer im selben
    Thread aus den E-Mails des Herstellers wieder; auch sie sind also Pläne und keine
    eingehaltenen Termine. Behandeln Sie die Verfügbarkeitsangabe als
    zutreffend für August 2026, nicht für den Zeitpunkt, zu dem Sie dies lesen. Der
    Absatz zu Gen 2 stützt sich auf
    mehr — Prusas eigene Beiträge und Release Notes —, ebenso der Absatz zu den
    Satzgrößen, mit Besitzern in zwei getrennten Threads und der eigenen Anleitung
    dieser Edition für die Founders Edition und Prusas Anleitung für Prusas Satz; beide
    stehen aber in diesem Abschnitt und übernehmen seine Stufe. Die Bezeichnungen zu
    7.0.0, 7.0.1 und 8.0.0 stützen sich jetzt auf ihre getaggten Releases auf GitHub, wie
    die zu 6.9.1 und 6.9.2; nur ihre Daten im Oktober und die Einträge zur L+ und L
    stammen von der Download-Seite, die Prusa an Ort und Stelle ändert. Das Build-Ziel für
    die L ist eine Lesart des Quellcodes, keine Produktankündigung.

## Überprüfung

`unknown` — nichts anderes auf dieser Seite wurde geprüft. Es sollte weder eine
Komponentenspezifikation noch eine Revisionskennung oder ein Messwert von hier
übernommen werden, solange dieser Hinweis nicht entfernt und das Feld confidence
gesetzt ist.

## Verwandte Seiten

- [Referenz-Übersicht](index.md)
- [Probleme](../issues/index.md) — dort werden Ausfälle dieser Komponenten dokumentiert
