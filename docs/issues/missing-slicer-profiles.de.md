---
title:        Nur eine Düsengröße hat ein Slicer-Profil
confidence:   reported
updated:      2026-10-18
author:       hyiger
printer:      Core One
toolhead:     INDX
hotend:       CHT high-flow
nozzle:       0.4mm is the only variant offered
firmware:     unknown
sources:
  - https://github.com/prusa3d/PrusaSlicer-settings-prusa-fff/issues/45
  - https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/missing-profiles-in-slicer-for-non-0-4-nozzles-and-other-materials/
  - https://github.com/prusa3d/PrusaSlicer-settings-prusa-fff/blob/main/PrusaResearch/2.5.10.ini
  - https://github.com/prusa3d/PrusaSlicer-settings-prusa-fff/blob/main/PrusaResearch/2.5.11.ini
  - https://github.com/prusa3d/PrusaSlicer-settings-prusa-fff/issues/48
  - https://github.com/prusa3d/PrusaSlicer/releases/tag/version_3.0.0-alpha11
  - https://github.com/prusa3d/PrusaSlicer-settings-prusa-fff/blob/main/PrusaResearch/index.idx
  - https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/firmware-and-slicer-update-to-use-other-nozzles-than-0-4hf/
  - https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/prusa-slicer-does-not-load-other-filaments/
  - https://forum.prusa3d.com/forum/prusa-indx-how-do-i-print-this-printing-help/printing-flex-material-on-indx-prusa-core-one-2-generation/
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.9.1
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.9.2
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/compare/v6.9.1...v6.9.2
  - https://forum.prusa3d.com/forum/prusa-indx-how-do-i-print-this-printing-help/3d-fuel-pctg-pro-profile-for-indx/
  - https://github.com/prusa3d/PrusaSlicer/blob/version_2.9.6/src/slic3r/GUI/MainFrame.cpp
  - https://github.com/prusa3d/PrusaSlicer-settings-prusa-fff/blob/main/PrusaResearch/2.5.12.ini
  - https://help.prusa3d.com/downloads/core-one-indx
  - https://github.com/prusa3d/PrusaSlicer/blob/version_3.0.0-alpha12/resources/presets/prusa-research-fff/PrusaResearch/preset-tool-coreone-indx.yaml
  - https://github.com/OrcaSlicer/OrcaSlicer/tree/v2.5.0-alpha/resources/profiles/Prusa/machine
  - https://github.com/OrcaSlicer/OrcaSlicer/blob/v2.5.0-alpha/docs/HLSD/prusa-indx-profiles.md
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/where-are-all-the-print-profiles/
  - https://forum.prusa3d.com/forum/prusa-indx-how-do-i-print-this-printing-help/nylon-with-indx/
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/set-colormix-colors-in-prusaslicer/
  - https://github.com/Zsoldier/PrusaSlicer-OpenPrintTagImport
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/flex-filament-stuck-and-cannot-dock-tool/
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/indx-review/
superseded_by:
source_sha:   ae54bad6b2276781af44916a2cd9e8048bbf32dabb434f8a911842b91015f6a7
---
# Nur eine Düsengröße hat ein Slicer-Profil

## Zusammenfassung

PrusaSlicer 2.9.6, die aktuelle stabile Version, bietet für den INDX genau eine
Düsenvariante an: High-Flow 0.4mm. Wer eine Düse mit 0.25, 0.5, 0.6, 0.8 oder 1.0mm
kauft, findet dort kein Profil, das sich dafür auswählen ließe. Es geht nicht darum, dass
Profile dünn oder unausgereift wären — die übrigen Größen werden überhaupt nicht
angeboten. Die 3.0-Alphas wählen Düsen auf andere Weise, doch in der neuesten davon,
Alpha 12, hat das INDX-Profil aktive benannte Druck-Presets ebenfalls nur für diese eine
Düse, und
Besitzer, die die Alphas ausprobiert haben, fanden auch keine andere Größe (siehe unten).
Die ersten INDX-Profile von OrcaSlicer, in dessen Alpha 2.5.0 vom 16. Oktober, decken
ebenfalls nur die High-Flow-Düse mit 0.4mm ab. Zwei Anfragen, die Größen zu ergänzen, sind
upstream offen, die erste seit Juli 2026; keine hat eine Reaktion von Prusa erhalten, nur
weitere Kommentatoren, die dasselbe verlangen. Prusas neuestes Profil-Bundle, 2.5.12 vom
15. Oktober 2026, deklariert weiterhin nur diese eine Variante, auch wenn es und davor
2.5.11 weitere Vorarbeiten für andere Größen anlegen, von denen keine erreichbar ist.

Bei den Materialien hat sich seit der ersten Fassung dieser Seite etwas bewegt: Flexible
Filamente und BVOH haben im September INDX-Slicer-Presets erhalten, PVA im Oktober mit
Bundle 2.5.12 ein generisches. HIPS hat weiterhin keines. Druckerseitige PVA- und
BVOH-Presets, für Firmware 6.9.1 angekündigt, aber darin nicht enthalten, kamen am
7. Oktober mit 6.9.2 und bleiben in 7.0.0 erhalten; das sind die eigenen Presets des
Druckers, keine Slicer-Profile.

Unterschiedliche Düsengrößen über die Werkzeuge hinweg waren ein beworbenes
Hauptmerkmal dieses Werkzeugwechslers; man sollte das also wissen, bevor man Düsen
kauft, und erst recht, bevor man Shop-Guthaben als Entschädigung für Düsen annimmt.

## Details

### Was tatsächlich im Bundle enthalten ist

Das ist überprüfbar und keine Frage von Berichten. Prusa veröffentlicht sein
Profil-Bundle, und in der aktuellen Ausgabe
([2.5.12](https://github.com/prusa3d/PrusaSlicer-settings-prusa-fff/blob/main/PrusaResearch/2.5.12.ini),
geprüft am 18. Oktober 2026) deklarieren beide INDX-Druckermodelle — das mit
vier und das mit acht Werkzeugen — eine einzige Variante:

```ini
variants = HF0.4
```

Diese eine Zeile ist die Einschränkung. Eine Variante ist das, was PrusaSlicer beim
Hinzufügen des Druckers zur Auswahl stellt; ist nur eine deklariert, bietet PrusaSlicer
2.9.6 keine andere Düsengröße an, gleich welche Materialprofile dahinter vorhanden sein
mögen.

Die Variante ist High-Flow; eine Standard-Flow-Düse hat also ebenfalls keine Variante,
selbst bei 0.4mm. Das ist inzwischen praktisch relevant. Im ursprünglichen Thread
berichtete ein Besitzer im September, dass seine 0.25mm-Düse vom Hersteller angekommen
sei: Prusa Connect akzeptierte 0.25mm als Düsengröße des Werkzeugs, doch PrusaSlicer
2.9.6 und die ausprobierte 3.0-Alpha boten kein Preset dafür an. Der Autor dieser Seite
antwortete im selben Thread, Standard-Flow-Profile für 0.4 und 0.25 beim INDX seien in
einer 3.0-Alpha aufgetaucht und in der nächsten wieder verschwunden, und ein anderer
Besitzer dort fand in der Alpha überhaupt keinen Weg, die Düsengröße zu ändern. Dass es
diese Profile gab, stützt sich auf den eigenen Bericht des Autors, nicht auf einen
unabhängigen, und ist hier nicht überprüft, doch deshalb lohnt es sich, neben dem
2.5.x-Bundle auch die 3.0-Reihe im Blick zu behalten. Eines schränkt das ein: Der Autor
verortete diese Profile in Alpha 10, die er vor der öffentlichen Freigabe sah,
und Prusas Versionshinweise vom 1. September nennen Alpha 11
[die erste öffentliche 3.0-Alpha](https://github.com/prusa3d/PrusaSlicer/releases/tag/version_3.0.0-alpha11);
kein Besitzer in den Quellen hat die Profile in einer öffentlichen Alpha gefunden.
Unabhängig davon bestätigte im Oktober ein weiterer Besitzer im Thread, der beide
Größen und dazu eine HF0.6 besitzt, dass die Profile wieder verschwunden sind, ohne zu
sagen, ob er sie selbst gesehen hatte.

Prusas [Versionshinweise zu Alpha 11](https://github.com/prusa3d/PrusaSlicer/releases/tag/version_3.0.0-alpha11)
beschreiben für 3.0 zudem einen anderen Mechanismus: Düsengröße und High-Flow-Status
werden je Werkzeug im Druckerprofil gewählt, statt als Druckervarianten deklariert zu
werden. Was den INDX dort begrenzt, ist also, für welche Düsenwerte sein 3.0-Profil
Presets mitbringt, nicht eine `variants =`-Zeile. In Alpha 12, veröffentlicht am
21. September und am 18. Oktober weiterhin die neueste 3.0-Alpha, hat die Datei mit den
[Druck-Presets je Werkzeug](https://github.com/prusa3d/PrusaSlicer/blob/version_3.0.0-alpha12/resources/presets/prusa-research-fff/PrusaResearch/preset-tool-coreone-indx.yaml)
des INDX aktive benannte Druck-Presets nur für eine High-Flow-Düse mit 0.4mm; die für
High-Flow 0.5, 0.6 und 0.8 sowie für eine Standard-Düse mit 0.25 stehen darin, aber
auskommentiert, auch wenn der gemeinsame Basisblock am Anfang der Datei bereits Werte für
Düsen von 0.25 bis 0.8mm enthält. Das deckt sich mit dem, was Besitzer in den Alphas vorfanden. Die Filament-Presets von 3.0
hat diese Seite nicht geprüft, und sie hat die Alpha auch nicht ausgeführt, um zu sehen,
was ihre Oberfläche anbietet.

Ein anderer Slicer ist bislang kein Ausweg. Der Besitzer, der den weiter unten
beschriebenen dritten Thread eröffnete, fragte, ob es für OrcaSlicer etwas für den INDX
gebe. Dessen
[Alpha 2.5.0](https://github.com/OrcaSlicer/OrcaSlicer/tree/v2.5.0-alpha/resources/profiles/Prusa/machine),
veröffentlicht am 16. Oktober, fügt INDX-Drucker mit vier und mit acht Werkzeugen hinzu,
jeweils mit einem einzigen Preset für eine High-Flow-Düse mit 0.4mm; laut den
[Erläuterungen von OrcaSlicer](https://github.com/OrcaSlicer/OrcaSlicer/blob/v2.5.0-alpha/docs/HLSD/prusa-indx-profiles.md)
sind sie aus Prusas Bundle 2.5.10 übertragen.

Später im September berichtete ein anderer Besitzer in einem separaten Thread, der
Hersteller liefere nun Standard-Düsen in 0.4 und 0.25mm, und fragte, wann Firmware und
PrusaSlicer sie unterstützen würden. Die Antworten, allesamt von anderen Besitzern,
verlängerten die Warteschlange, statt die Frage zu beantworten: Der Eröffner des
ursprünglichen Threads schrieb, eine Reihe von Käufern der Founders Edition habe mit
ihren Kits Düsen mit 0.25 und 0.6mm bestellt und noch keine Profile dafür gesehen,
ebenso wenig wie für HIPS; ein Besitzer hat Düsen mit 0.25 und 0.8mm; ein weiterer, der
sein Kit noch zusammenbaut, hat vier 0.25mm-Düsen dafür bereitliegen. Weder Prusa noch
der Hersteller hatten bis zum 4. Oktober geantwortet. Dass der Hersteller eine
Standard-Düse mit 0.4mm verkauft, stützt sich vor allem auf den Eröffnungsbericht. Im
ursprünglichen Thread schrieb ein Besitzer im August, er wolle Shop-Guthaben des
Herstellers für Standard-Düsen (ohne CHT) mit 0.4 ausgeben, und der oben genannte
Besitzer vom Oktober besitzt eine solche, sagt aber nicht, woher sie stammt. Eine zweite
Schilderung kam Mitte Oktober von jemandem, der die
[erste Upstream-Anfrage](https://github.com/prusa3d/PrusaSlicer-settings-prusa-fff/issues/45)
kommentierte: Der Hersteller habe ihm einige Wochen zuvor Standard-Düsen mit 0.25 und 0.4
geschickt; nichts in den Quellen verbindet diese Person mit einem der Forumsthreads.

Am 18. Oktober eröffnete ein weiterer Besitzer einen
[dritten Thread](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/where-are-all-the-print-profiles/):
Er betreibt einen INDX mit acht Werkzeugen, hat Düsen mit 0.25, 0.6 und 0.8mm gekauft und
für keine davon ein Profil gefunden.

Das Bundle enthält durchaus eine große Zahl INDX-spezifischer Filamenteinträge, und
einige der internen Vererbungsvorlagen verweisen auf größere Extrusionsbreiten. Es gibt
also Vorarbeiten. Das meiste davon ist allerdings abgeschaltet. Über tausend
INDX-Filamenteinträge stehen auskommentiert in der Datei, sodass PrusaSlicer sie nie
lädt: Basiseinträge ohne Düse im Namen, andere Materialien und Marken bei HF0.4
(einige davon Prusament), Kopien für die High-Flow-Düsen 0.5, 0.6 und 0.8, Kopien für
Standard-Flow 0.6 und 0.8 sowie zwei für 0.25, Prusament PLA und seit 2.5.11 Prusament
PETG. Keiner ist nach einer Standard-Düse mit 0.4 benannt, doch mehr als die Hälfte der
Basiseinträge trägt Kompatibilitätsbedingungen, die High-Flow-Düsen ausschließen, sodass
sie neben anderen Standard-Größen auf eine Standard-Düse mit 0.4 passen; seit 2.5.11
passen etwa hundert davon, alle auf den PLA- oder PETG-Vorlagen aufgebaut, auf eine
Standard-Düse mit 0.4 und auf keine andere Größe. (Bis Oktober stand hier, es gebe überhaupt keine
Einträge für eine Standard-Düse mit 0.4; das galt nur für die Namen.) Nur zwanzig
INDX-Filament-Presets sind aktiv (bis 2.5.12 neunzehn), alle nach HF0.4 benannt, wobei
die Bedingungen der beiden Presets für flexible Filamente nur eine 0.4-Düse verlangen,
keine High-Flow-Düse. Bei den Druck-Presets ist man weiter: Seit Bundle 2.5.8 zielen sechs aktive INDX-Druck-Presets auf Düsen mit 0.25
und 0.3mm, ohne High-Flow-Bedingung, und Drucker-Presets für 0.25, HF0.6 und HF0.8, je
eines für das Modell mit vier und das mit acht Werkzeugen, stehen auskommentiert in der
Datei. Erreichbar ist davon noch nichts, da kein aktives Filament-Preset zu diesen Größen
passt.
Für jede Größe außer HF0.4 fehlt zuerst die druckerseitige Variantendeklaration; ohne sie
gäbe es selbst nach dem Einschalten dieser Einträge nichts, womit man sie auswählen
könnte.

Bundle 2.5.11, veröffentlicht am 2. Oktober, ist im Änderungsprotokoll nur für das
HT-Hotend am Core One und am größeren Core One L aufgeführt und ändert am INDX nichts
Auswählbares: Aktiv sind dieselben neunzehn Filament-, zehn Druck- und zwei
Drucker-Presets wie in 2.5.10. Seine INDX-Änderungen sind allesamt intern oder
abgeschaltet: neue Filament-Vorlagen für PLA und PETG bei einer 0.25mm-Düse, auf denen
die beiden 0.25-Einträge nun aufbauen; die oben beschriebene Eingrenzung auf eine
Standard-Düse mit 0.4; ausgefüllte Einträge für Prusament PLA und PETG bei HF0.6; und
die Druck-Vorlagen für High-Flow-Düsen mit 0.5, 0.6 und 0.8mm, die so umbenannt wurden,
dass ihr Name sie als High-Flow kennzeichnet (die Namen, auf die ihre auskommentierten
Druck-Presets schon verwiesen), und deren Werte teils geändert wurden, wobei ihre
Bedingungen weiterhin nur den Düsendurchmesser prüfen. Die druckerseitige Deklaration
fehlt weiterhin, sodass auch davon nichts erreichbar ist.

Bundle 2.5.12, veröffentlicht am 15. Oktober, dem Tag, an dem Firmware 7.0.0 erschien,
lässt die Düsenseite, wie sie war. Beide Modelle deklarieren weiterhin nur `HF0.4`,
dieselben zehn Druck- und zwei Drucker-Presets sind aktiv, und die Zahl der
auskommentierten Einträge ist unverändert. Sein
[Änderungsprotokoll](https://github.com/prusa3d/PrusaSlicer-settings-prusa-fff/blob/main/PrusaResearch/index.idx)
nennt drei INDX-Punkte: ein überarbeitetes Werkzeugwechsel-Skript, beschrieben auf der
[Seite zum kommentierten G-Code](../gcode/indx-profile-gcode.md); einen neuen
Firmware-Versionshinweis; und ein Preset Generic PVA, die einzige auswählbare Ergänzung
(siehe unten). Darunter fügt es gemeinsame Vorlagen für Düsen mit 0.6 und 0.8mm hinzu, auf
denen die vorhandenen PLA-, PETG-, ABS-, PC-, PA-, FLEX- und PP-Vorlagen für diese
Größen nun aufbauen; genutzt werden diese Vorlagen nur von abgeschalteten Presets.
Außerdem legt es eigene Vorlagen an, deren Bedingungen Core-One-L-INDX-Modelle
nennen, die das Bundle nicht als Drucker deklariert. Nichts davon ist an einem Core One
INDX erreichbar.

### Materialien

Dieselbe Upstream-Anfrage bittet auch um Materialien, und hier hat sich das Bundle
bewegt.

**Stand der ersten Fassung (Bundle 2.5.7, August 2026) — nur, was PrusaSlicer lädt,
Vorlagen ebenso wie Presets; teilweise überholt:**

- **FLEX** taucht in INDX-spezifischen Vorlagen auf, es gibt also zumindest teilweise
  Vorarbeiten.
- **HIPS** taucht in keinem INDX-spezifischen Abschnitt auf.
- **TPU**, **PVA** und **BVOH** ebenso wenig.

Diese Punkte stimmten nur für das, was PrusaSlicer lädt: Schon 2.5.7 enthielt
auskommentierte INDX-Einträge für HIPS, TPU, PVA und BVOH.

**Seit Bundle 2.5.9** (am 8. September 2026 ins Repository eingecheckt), laut dessen
[Änderungsprotokoll](https://github.com/prusa3d/PrusaSlicer-settings-prusa-fff/blob/main/PrusaResearch/index.idx)
und der Datei selbst:

- **Flexible Filamente** haben nun aktive INDX-Presets: Prusament TPU 95A und Generic
  FLEX. TPU 95A ist zudem in die Standard-Materialliste beider Modelle aufgenommen worden.
  Ihr Filament-Start-G-Code ruft `M906 P2` auf, das Extruderstrom-Profil für FLEX, das
  Firmware 6.9.0 eingeführt hat.
- **BVOH** hat zwei, beide für Spulen von Drittanbietern (Verbatim und Fiberlogy). Auch
  ihr Start-G-Code ruft `M906 P2` auf.
- **HIPS** fehlt auch in 2.5.12 weiterhin. Wie schon in 2.5.7 gibt es INDX-Einträge
  dafür, aber nur unter den auskommentierten. PVA war bis 2.5.12 in derselben Lage.

**Seit Bundle 2.5.12** (am 15. Oktober 2026 eingecheckt), laut demselben
Änderungsprotokoll und der Datei:

- **PVA** hat ein aktives INDX-Preset, Generic PVA, für HF0.4. Es baut auf dem
  INDX-Preset Verbatim BVOH auf und setzt einige eigene Werte; sein eigener
  Filament-Start-G-Code ruft ebenfalls `M906 P2` auf. Die auskommentierten INDX-Einträge
  für ein Marken-PVA bleiben abgeschaltet.

Die für Anwender sichtbare Standard-Materialliste beider INDX-Modelle wurde hier als die
übliche PLA- und PETG-Familie beschrieben, was sie schon im August untertrieb. Stand
2.5.12 umfasst sie PLA, PETG, ASA, die PC Blends und Woodfill sowie seit 2.5.9 TPU 95A,
alle für die eine verfügbare Variante; keines der löslichen Materialien steht darauf.

**Druckerseitige PVA- und BVOH-Presets sind etwas anderes, und sie kamen mit Firmware
6.9.2.** Die [Version 6.9.1](https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.9.1)
vom 25. September führte sie als neu auf und strich den Punkt dann wieder, weil ein
Fehler im Ablauf sie aus dem Build herausgehalten hatte.
[6.9.2](https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.9.2), erschienen
am 7. Oktober, fügt sie hinzu, und ein
[Vergleich der beiden Release-Tags](https://github.com/prusa3d/Prusa-Firmware-Buddy/compare/v6.9.1...v6.9.2)
zeigt darin nichts weiter, was einen INDX betrifft. Solche Presets sind die eigenen
Filamenteinträge des Druckers, die man beim Laden einer Spule an der Maschine verwendet,
und fügen PrusaSlicer kein Druckprofil hinzu. Mit 6.9.2 war BVOH damit an beiden Enden
abgedeckt, PVA nur am Drucker; seit Bundle 2.5.12 ist auch PVA an beiden Enden
abgedeckt. Firmware 7.0.0 vom 15. Oktober behält die Presets, die ihre
[Versionshinweise](https://help.prusa3d.com/downloads/core-one-indx) als aus 6.9.2
übernommen kennzeichnen.

Das ist mehr als eine Frage der Bequemlichkeit: HIPS und die löslichen Materialien sind
das, wozu man greift, um auf einem Werkzeugwechsler Kontaktflächen von Stützstrukturen
zu drucken — und genau das ist zu einem großen Teil der Grund, warum man sich einen
anschafft. BVOH und seit 2.5.12 auch PVA decken den löslichen Fall bei der einen
Düsengröße nun ab; HIPS noch nicht.

### Filament-Presets anderer Marken

Die auskommentierten Einträge erklären auch, warum ein über den Konfigurationsassistenten
von PrusaSlicer installiertes Filament für die Werkzeuge des INDX womöglich nicht
angeboten wird. Ein Besitzer installierte auf diesem Weg mehrere Drittanbieter-Marken
und fand keine davon für den INDX angeboten, obwohl sie an anderer Stelle im Slicer
auftauchten; bislang ist das der einzige Bericht zu anderen Marken. Früher im September
stieß ein anderer Besitzer in einem separaten Thread mit flexiblen Filamenten auf
dieselbe Hürde: über den Assistenten installiert, am INDX aber nicht auswählbar. Das war
drei Tage, bevor Bundle 2.5.9 zwei INDX-Presets für Flex hinzufügte, Prusament TPU 95A
und Generic FLEX; für flexible Filamente gibt es am INDX also inzwischen Presets zur
Auswahl, die Flex-Einträge anderer Marken sind aber wie der Rest weiterhin
abgeschaltet. Das Bundle bestätigt beide Berichte: Seine Filament-Presets
tragen jeweils eine Kompatibilitätsbedingung, die die Druckermodelle und die Düse
nennt, für die sie gelten.
Die gewöhnlichen Core-One-Presets nennen Core-One-Modelle, zu denen der INDX nicht passt,
und die INDX-Kopien, die passen würden, sind genau die abgeschalteten.

Der Besitzer mit den anderen Marken kam weiter, indem er das generische Preset
desselben Materials unter neuem Namen speicherte und die Werte des Filamentherstellers
eintrug. Die
Kompatibilitätsbedingung eines Core-One-Presets so zu lockern, dass sie den INDX
einschließt, ist der andere Weg, mit einem Haken, der in der Datei sichtbar ist: Die
INDX-Presets sind keine umbenannten Core-One-Presets. Sie legen INDX-spezifische
Vorlagen darüber und ersetzen den Filament-Start-G-Code, sodass ein erweitertes
Core-One-Preset seinen Core-One-G-Code mitbringt. So oder so ist das Ergebnis ein
selbst gebautes Profil, kein getestetes.

Ein dritter Weg um diesen Haken herum kam im Oktober auf, gestützt auf den Bericht eines
Besitzers in einem
[Thread zu Nylon](https://forum.prusa3d.com/forum/prusa-indx-how-do-i-print-this-printing-help/nylon-with-indx/),
einem Material ohne aktives INDX-Preset. Statt ein Core-One-Preset zu erweitern, schrieb
er einen eigenen INDX-Eintrag, der ein Core-One-Nylon-Preset und danach die INDX-Vorlagen
des Bundles für Nylon als Eltern angibt — dieselbe Schichtung, die Prusas INDX-Presets
verwenden, sodass der INDX-Start-G-Code mitkommt. Wie er ihn in PrusaSlicer geladen hat,
sagte er nicht. Sein erster Druck damit scheiterte an einer Spule, die sich in ihrer
Trockenbox verklemmte, was mit dem Profil nichts zu tun hatte; den nächsten, einen Tag
später, nannte er gelungen. Das ist ein Druck eines einzelnen Besitzers, und seine
Einstellungen werden hier nicht wiedergegeben.

Anfang Oktober tauchten zwei andere Wege auf, jeder gestützt auf den Bericht eines
einzelnen Besitzers. Der erste ist ein Profil, das jemand anderes geteilt hat. Im Oktober
versuchte ein Besitzer, ein in einem
[Forumsthread](https://forum.prusa3d.com/forum/prusa-indx-how-do-i-print-this-printing-help/3d-fuel-pctg-pro-profile-for-indx/)
geteiltes INDX-Filamentprofil über File > Import > Import Config zu laden, und erhielt ein
Projekt, in dem fast jedes Feld „default“ lautete. Der Autor des Profils, der zugleich
Autor dieser Seite ist, verwies stattdessen auf Import Config Bundle im selben Menü; ob
das beim Fragenden funktionierte, wurde nicht berichtet.
[PrusaSlicers eigenes Menü](https://github.com/prusa3d/PrusaSlicer/blob/version_2.9.6/src/slic3r/GUI/MainFrame.cpp)
beschreibt die beiden unterschiedlich: Import Config lädt eine einzelne exportierte
Konfiguration, Import Config Bundle einen Satz von Presets. Der Besitzer im
[Thread zu flexiblen Filamenten](https://forum.prusa3d.com/forum/prusa-indx-how-do-i-print-this-printing-help/printing-flex-material-on-indx-prusa-core-one-2-generation/)
war ebenfalls daran gescheitert, eine im Forum gefundene .ini zu importieren, ohne zu
sagen, auf welchem Weg. Der zweite Weg kam im Oktober von einem weiteren Besitzer in
diesem Thread: ein auf Reddit geteilter OpenPrintTag-Importer für PrusaSlicer, der nach
seinen Worten bei ihm funktioniert, PrusaSlicer 3 eingeschlossen. Im selben Satz heißt es
dann, er habe danach keine Filamente finden können, und aus dem Beitrag geht nicht hervor,
in welchem Slicer das war oder was nicht klappte. Er sagte nicht, für welche Filamente er
ihn nutzte oder wie dessen Presets dem INDX zugeordnet werden, und diese Seite hat ihn
nicht ausprobiert. Zehn Tage später verlinkte derselbe Besitzer in einem
[Thread zu ColorMix-Farben](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/set-colormix-colors-in-prusaslicer/)
das GitHub-Repository eines OpenPrintTag-Importers, vermutlich desselben Werkzeugs, und
empfahl ihn erneut für PrusaSlicer 2 und 3; das ist dieselbe Person, kein zweiter Bericht.
Die
[README dort](https://github.com/Zsoldier/PrusaSlicer-OpenPrintTagImport) beantwortet die Frage der Zuordnung: Jedes importierte Preset geht von
einem Filament-Preset aus, das man für den Zieldrucker wählt, und behält dessen
Druckerkompatibilität und Filament-G-Code; ersetzt wird nur, was OpenPrintTag liefert,
etwa Temperaturen und Farbe. Am INDX heißt das, auf einem der HF0.4-Presets aufzubauen;
er kann also Marken hinzufügen, aber keine Düsengrößen.
Keiner dieser Wege liefert ein von Prusa getestetes Profil.

### Warum das die Düsen-Entschädigung verschärft

Die Abhilfe des Herstellers für das Problem der Düsenhärte bietet Shop-Guthaben zu
einem höheren Satz als Bargeld, und Guthaben legt naturgemäß den Kauf weiterer Düsen
nahe. Ein Besitzer, der zwischen beidem abwog, wies auf den Zirkelschluss hin: Er hatte
nie andere Düsengrößen ausprobiert, weil es keine Profile dafür gibt.

Guthaben für Düsen ist daher weniger wert, als der genannte Satz vermuten lässt,
solange das nicht gelöst ist. Beziehen Sie das in Ihre Entscheidung ein. Siehe
[Düsenhärte](nozzle-hardness.md).

### Was Sie tun können

Direkt wenig — es handelt sich um Upstream-Konfiguration und nicht um etwas, das eine
Einstellung an Ihrer Maschine ändert.

- **Schließen Sie sich den offenen Anfragen an.** Die erste ist
  [Issue 45 in Prusas FFF-Settings-Repository](https://github.com/prusa3d/PrusaSlicer-settings-prusa-fff/issues/45),
  offen seit dem 31. Juli 2026 für Größen und Materialien. Bis Oktober hatte sie keinen
  einzigen Kommentar; dann schrieben zwei weitere Kommentatoren dazu, einer mit der
  Frage, ob weitere Größen und Düsen ohne CHT kommen, einer mit dem Hinweis, dass seine
  Standard-Düsen vom Hersteller weiterhin nichts haben, womit sie laufen könnten; Prusa
  hatte bis zum 18. Oktober nicht reagiert. Die zweite,
  [Issue 48](https://github.com/prusa3d/PrusaSlicer-settings-prusa-fff/issues/48), wurde
  am 29. September von jemand anderem eingereicht und bittet allein um die Düsengrößen,
  namentlich 0.25, 0.5, 0.6, 0.8 und 1.0; ihr einziger Kommentar ist der erste dieser
  Kommentatoren, der seine Frage wiederholt, und auch sie hatte bis zum 18. Oktober keine
  Reaktion von Prusa erhalten. Ein Issue mit einem einzigen Melder und ohne Resonanz
  bleibt leicht unbeachtet; mehrere Besitzer, die benennen, welche Größen und Materialien
  sie tatsächlich brauchen, lassen sich schwerer übergehen. Die Material-Presets vom
  September kamen übrigens, ohne dass Issue 45 angerührt wurde, und die 0.25-Vorarbeiten
  in 2.5.11 sowie Generic PVA in 2.5.12, ohne dass Prusa auf eines der beiden Issues
  antwortete; ihr Schweigen sagt also wenig über den Fortschritt, in die eine wie die
  andere Richtung.
- **Nehmen Sie Bundle-Updates mit, wenn sie kommen.** Die INDX-Presets werden mit dem
  Profil-Bundle ausgeliefert, nicht mit dem Slicer: Die Bundle-Reihe, die sie enthält,
  setzt PrusaSlicer 2.9.6 voraus, die aktuelle Version auf Prusas Download-Seite, und
  jedes neue Bundle erreicht sie als Konfigurations-Update statt als neue Slicer-Version.
- **Kaufen Sie Düsen unter der Annahme, sie noch nicht nutzen zu können**, oder warten
  Sie ab. Das gilt für PrusaSlicer 2.9.6; die Alpha 2.5.0 von OrcaSlicer liefert, nach
  ihren Preset-Dateien zu urteilen, ebenfalls kein Preset für andere Größen, und
  niemand in den Quellen berichtet, darin eine ausprobiert zu haben. Für die 3.0-Alphas
  beruht es auf Berichten von Besitzern und auf der Profildatei von Alpha 12, die diese
  Seite gelesen, aber nicht ausgeführt hat. Wenn Sie zwischen den
  Entschädigungsformen wählen, spricht das für Bargeld statt Guthaben, sofern es Sie nicht
  stört, die Hardware ungenutzt zu halten.

TODO(verify): ob sich ein eigenes Profil für eine andere Düsengröße von Hand zum Laufen
bringen lässt und was dabei zerbricht. Niemand in den Quellen hat über einen gelungenen
Versuch berichtet. Ende September kündigten zwei Besitzer an, es zu versuchen, einer für
0.25mm-Düsen und einer für Düsen mit 0.25 und 0.8mm sowie HIPS; bis zum 4. Oktober hatte
keiner von beiden berichtet. Am nächsten an einem Ergebnis ist bislang der Besitzer mit
einem INDX mit acht Werkzeugen vom Oktober, der ein Profil baute, offenbar für die
0.8mm-Düse, und es für eines seiner Werkzeuge nicht angezeigt bekam, ohne zu sagen, wie
er es gebaut hatte. Bis jemand mehr berichtet, spekuliert diese Seite nicht — das Spül-
und Kalibrierverhalten des Werkzeugwechslers hängt auf nicht offensichtliche Weise am
Profil.

## Überprüfung

`reported` (mehrfach berichtet), und der tragende Teil ist stärker, als diese Stufe
verlangt.

**Die zentrale Aussage ist verifiziert, nicht bloß berichtet.** Dass nur `HF0.4`
angeboten wird, ergibt sich aus dem Lesen von Prusas eigenem veröffentlichtem
Profil-Bundle, in dem beide INDX-Druckermodelle diese eine Variante deklarieren. Das
sind veröffentlichte Daten aus erster Hand, in derselben Klasse wie eine Anmerkung zu
einer Firmware-Veröffentlichung — und nicht die Schilderung einer fremden Maschine. Am
18. Oktober 2026 wurde es anhand von 2.5.12 erneut gelesen, ebenso wie die
Material-Presets, die auskommentierten Einträge und die oben beschriebenen
Kompatibilitätsbedingungen. Die Druck-Preset-Datei von Alpha 12 der Version 3.0 und die
Drucker-Presets der Alpha 2.5.0 von OrcaSlicer wurden am selben Tag in ihrem
veröffentlichten Quellcode gelesen; keiner der beiden Slicer wurde ausgeführt.

**Die Auswirkung ist berichtet**, von sechs Besitzern in
[einem Forumsthread](https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/missing-profiles-in-slicer-for-non-0-4-nozzles-and-other-materials/),
von denen einer Düsen mit 0.5 und 1.0mm kaufte, bevor er feststellte, dass sie sich
nicht nutzen lassen, ein anderer die Sache beim Abwägen der Düsen-Entschädigung ansprach
und zwei Düsen mit 0.25mm besitzen, für die sich kein Preset auswählen lässt. (Bis
Oktober nannte diese Seite vier; die beiden mit 0.25mm-Düsen schrieben erst nach ihrer
ersten Fassung.) Die
[erste Upstream-Anfrage](https://github.com/prusa3d/PrusaSlicer-settings-prusa-fff/issues/45)
ist ein zweiter Ort, wurde jedoch von derselben Person eingereicht, die den
Forumsthread eröffnet hat, und ist damit ein Cross-Post statt einer unabhängigen
Bestätigung. Die
[zweite](https://github.com/prusa3d/PrusaSlicer-settings-prusa-fff/issues/48) stammt von
einer anderen Person; nichts in den Quellen verbindet sie mit jemandem aus einem der
beiden Threads. Ein
[separater Thread](https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/firmware-and-slicer-update-to-use-other-nozzles-than-0-4hf/),
im September von einem anderen Besitzer eröffnet, fragt, wann die Standard-Flow-Düsen,
die der Hersteller inzwischen liefert, unterstützt werden. Der Eröffnungsbeitrag ist
eine Frage und kein Bericht davon, an einer Maschine auf die Lücke gestoßen zu sein. Von
den drei Besitzern, die antworteten, hatten zwei schon im ursprünglichen Thread
geschrieben; der dritte, dessen 0.25mm-Düsen auf Profile warten, baut sein Kit noch
zusammen. Der Thread zeigt dieselbe Lücke aus einer zweiten Richtung, fügt aber nur zwei
neue Besitzer hinzu: den, der fragte, und den, der noch baut. Ein
[dritter Thread](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/where-are-all-the-print-profiles/),
eröffnet am 18. Oktober, fügt einen weiteren Besitzer hinzu, der andere Größen gekauft
und nichts zur Auswahl gefunden hat; die bislang einzige Antwort kam vom Autor dieser
Seite. Bei den Upstream-Anfragen meldeten im Oktober zwei weitere Kommentatoren ihren
eigenen Bedarf an, einer davon bei beiden Issues; nichts in den Quellen verbindet einen
der beiden mit den Forumsthreads.

**Das Symptom ist berichtet, der Fall anderer Marken vorläufig.** Zwei Besitzer in zwei
Threads stellten fest, dass sich über den Assistenten installierte Filamente am INDX
nicht auswählen ließen: einer mit
[anderen Marken](https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/prusa-slicer-does-not-load-other-filaments/)
und, schon früher, einer mit
[flexiblen Filamenten](https://forum.prusa3d.com/forum/prusa-indx-how-do-i-print-this-printing-help/printing-flex-material-on-indx-prusa-core-one-2-generation/).
Der zweite Bericht betrifft ein Material, das damals kein aktives INDX-Preset hatte, und
nennt keine Marke; er bestätigt also das Symptom, nicht die Markenliste. Dass gerade
Drittanbieter-Marken betroffen sind, stützt sich auf einen Besitzer. Der Mechanismus
hinter beiden ist aus dem Bundle gelesen, nicht aus einem der Threads übernommen.

**Die weiteren Wege sind vorläufig.** Der von Hand geschriebene Nylon-Eintrag stützt
sich auf einen Besitzer in
[einem Thread](https://forum.prusa3d.com/forum/prusa-indx-how-do-i-print-this-printing-help/nylon-with-indx/)
und einen gelungenen Druck; dass die darin genannten INDX-Vorlagen existieren, ist gegen
das Bundle geprüft, sonst nichts daran. Der gescheiterte Import stützt sich auf
einen Besitzer in
[einem Thread](https://forum.prusa3d.com/forum/prusa-indx-how-do-i-print-this-printing-help/3d-fuel-pctg-pro-profile-for-indx/),
und die vorgeschlagene Alternative kam vom Autor dieser Seite; sie ist also nicht
unabhängig bestätigt und wurde nie als funktionierend gemeldet, und ob der gescheiterte
Import des Besitzers mit den flexiblen Filamenten dieselbe Ursache hatte, ist unbekannt.
Der OpenPrintTag-Importer stützt sich allein auf die Aussage eines Besitzers, dass der
Importer bei ihm funktioniert, PrusaSlicer 3 eingeschlossen; hinzu kommt eine unklare
Bemerkung im selben Beitrag, danach keine Filamente gefunden zu haben; seine zweite
Empfehlung, in einem anderen Thread, stammt wieder von demselben Besitzer. Hier geprüft
ist, wie PrusaSlicers eigenes Menü die beiden Import-Einträge beschreibt und was die
README des Importers dazu sagt, was er vom Basis-Preset behält; den Importer selbst hat
diese Seite nicht ausgeführt.

**Wo das schwächer ist, als es aussieht.** Ob FLEX wirklich nutzbar ist, bleibt unklar:
Die Vorlagen sind im Bundle vorhanden, doch das ist nicht dasselbe wie ein auswählbares,
getestetes Profil, und anfangs berichtete kein Besitzer in den Quellen, damit gedruckt zu
haben. Behandeln Sie die obigen Materialbefunde als Beschreibung dessen, was in der
Datei steht, und nicht dessen, was funktioniert. Seit 2.5.9 sind die Presets für flexible
Filamente und BVOH auswählbar, was die erste Hälfte davon erledigt. Die zweite Hälfte
war bis Mitte Oktober offen; dann berichteten Besitzer in drei Threads, am INDX flexibles
Filament gedruckt zu haben, mit gemischtem Ergebnis; in zwei dieser Threads nennt ein
Besitzer das verwendete INDX-Preset. Im
[Thread zu flexiblen Filamenten](https://forum.prusa3d.com/forum/prusa-indx-how-do-i-print-this-printing-help/printing-flex-material-on-indx-prusa-core-one-2-generation/)
druckte ein Besitzer ein TPU eines Drittanbieters mit dem Preset Prusament TPU 95A: Der
erste Versuch verstopfte im Extruder, und nachdem er das Werkzeug mit PLA freigespült
hatte, gelang ein zweiter Versuch mit einer anderen Schichthöhe auf einer PLA-Basis. In
einem
[Thread über einen veröffentlichten Testbericht zum INDX](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/indx-review/)
schrieb ein weiterer Besitzer, eine Reihe mehrfarbiger Drucke in einem TPU eines
Drittanbieters sei auf der serienmäßigen CHT-Düse ohne Probleme gelaufen, mit den von
ihm so genannten generischen Profilen, und wiederholte einen Tag später, dass TPU bei ihm
funktioniert habe; welches Flex-Preset er wählte, sagte er nicht. In einem
[Thread zu einem Werkzeug, das sich nicht ablegen ließ](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/flex-filament-stuck-and-cannot-dock-tool/),
saß bei zwei Besitzern ein Werkzeug am Kopf fest, weil sich flexibles Filament um die
Extruderzahnräder verklemmt hatte, bei einem davon mit dem Preset Generic FLEX. Keiner
der Threads klärt, ob die Presets taugen; sie zeigen, dass Flex am INDX funktionieren,
aber auch klemmen kann. Die Erfolge stammen von zwei Besitzern in zwei Threads, von denen
nur einer das Preset nennt, und sind daher als vorläufig zu behandeln; die Verklemmungen
stammen von drei Besitzern in zwei Threads, den ersten Versuch des ersten Besitzers
mitgezählt. Niemand in den Quellen berichtet bislang, BVOH oder PVA mit den Presets
gedruckt zu haben.

Das veraltet schnell. Es ist eine Konfigurationslücke, die eine Profilveröffentlichung
mit einem einzigen Update schließt; prüfen Sie daher das aktuelle Bundle, bevor Sie
danach handeln. Teilweise ist das schon geschehen: Die Materialliste hat sich binnen
eines Monats nach dieser Seite bewegt, die Düsenvarianten nicht.

## Verwandte Themen

- [Düsenhärte](nozzle-hardness.md) — die Entschädigung, mit der dies zusammenwirkt
- [Kommentierter Profil-G-Code](../gcode/indx-profile-gcode.md) — was ein Profil
  mitführt und warum die Düsendeklaration pro Werkzeug von Bedeutung ist
