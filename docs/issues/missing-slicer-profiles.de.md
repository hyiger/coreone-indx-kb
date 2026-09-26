---
title:        Nur eine Düsengröße hat ein Slicer-Profil
confidence:   reported
updated:      2026-09-25
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
  - https://github.com/prusa3d/PrusaSlicer-settings-prusa-fff/blob/main/PrusaResearch/index.idx
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/firmware-and-slicer-update-to-use-other-nozzles-than-0-4hf/
  - https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/prusa-slicer-does-not-load-other-filaments/
  - https://forum.prusa3d.com/forum/prusa-indx-how-do-i-print-this-printing-help/printing-flex-material-on-indx-prusa-core-one-2-generation/
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.9.1
superseded_by:
source_sha:   ed651c9098ba1b4e1eb012e12b31b03e7748c452f39b8878ba73a697cba2c82f
---
# Nur eine Düsengröße hat ein Slicer-Profil

## Zusammenfassung

PrusaSlicer bietet für den INDX genau eine Düsenvariante an: High-Flow 0.4mm. Wer eine
Düse mit 0.25, 0.5, 0.6, 0.8 oder 1.0mm kauft, findet kein Profil, das sich dafür
auswählen ließe. Es geht nicht darum, dass Profile dünn oder unausgereift wären — die
übrigen Größen werden überhaupt nicht angeboten. Eine Anfrage, sie zu ergänzen, ist
upstream seit Juli 2026 offen, ohne Reaktion. Prusas neuestes Profil-Bundle, 2.5.10 vom
17. September 2026, deklariert weiterhin nur diese eine Variante.

Bei den Materialien hat sich seit der ersten Fassung dieser Seite etwas bewegt: Flexible
Filamente und BVOH haben im September INDX-Slicer-Presets erhalten. HIPS und PVA haben
weiterhin keine; die in Firmware 6.9.1 neuen PVA- und BVOH-Presets liegen auf dem Drucker
und sind keine Slicer-Profile.

Unterschiedliche Düsengrößen über die Werkzeuge hinweg waren ein beworbenes
Hauptmerkmal dieses Werkzeugwechslers; man sollte das also wissen, bevor man Düsen
kauft, und erst recht, bevor man Shop-Guthaben als Entschädigung für Düsen annimmt.

## Details

### Was tatsächlich im Bundle enthalten ist

Das ist überprüfbar und keine Frage von Berichten. Prusa veröffentlicht sein
Profil-Bundle, und in der aktuellen Ausgabe
([2.5.10](https://github.com/prusa3d/PrusaSlicer-settings-prusa-fff/blob/main/PrusaResearch/2.5.10.ini),
erneut geprüft am 25. September 2026) deklarieren beide INDX-Druckermodelle — das mit
vier und das mit acht Werkzeugen — eine einzige Variante:

```ini
variants = HF0.4
```

Diese eine Zeile ist die Einschränkung. Eine Variante ist das, was PrusaSlicer beim
Hinzufügen des Druckers zur Auswahl stellt; ist nur eine deklariert, lässt sich keine
andere Düsengröße auswählen, gleich welche Materialprofile dahinter vorhanden sein
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
2.5.x-Bundle auch die 3.0-Reihe im Blick zu behalten. Später im selben Monat
berichtete ein anderer Besitzer in einem separaten Thread, der Hersteller liefere nun
Standard-Düsen in 0.4 und 0.25mm, und fragte, wann Firmware und PrusaSlicer sie
unterstützen würden; zum Zeitpunkt des Schreibens hatte niemand geantwortet. Der Teil
zur Standard-Düse mit 0.4mm stützt sich auf diesen einen Bericht.

Das Bundle enthält durchaus eine große Zahl INDX-spezifischer Filamenteinträge, und
einige der internen Vererbungsvorlagen verweisen auf größere Extrusionsbreiten. Es gibt
also Vorarbeiten. Das meiste davon ist allerdings abgeschaltet. Über tausend
INDX-Filamenteinträge stehen auskommentiert in der Datei, sodass PrusaSlicer sie nie
lädt: Basiseinträge ohne Bezug zu einer Düse, andere Materialien und Marken bei HF0.4
(einige davon Prusament), Kopien für die High-Flow-Düsen 0.5, 0.6 und 0.8 sowie Kopien
für Standard-Flow 0.6 und 0.8 und eine einzelne für 0.25. Für eine Standard-Düse mit
0.4 gibt es keine, nicht einmal abgeschaltet. Nur neunzehn INDX-Filament-Presets sind
aktiv, alle nach HF0.4 benannt, wobei die Bedingungen der beiden Presets für flexible
Filamente nur eine 0.4-Düse verlangen, keine High-Flow-Düse. Bei den Druck-Presets ist
man weiter: Seit Bundle 2.5.8 zielen sechs aktive INDX-Druck-Presets auf Düsen mit 0.25
und 0.3mm, ohne High-Flow-Bedingung, und Drucker-Presets für 0.25, HF0.6 und HF0.8, je
eines für das Modell mit vier und das mit acht Werkzeugen, stehen auskommentiert in der
Datei. Erreichbar ist davon noch nichts, da kein aktives Filament-Preset zu diesen Größen
passt.
Für jede Größe außer HF0.4 fehlt zuerst die druckerseitige Variantendeklaration; ohne sie
gäbe es selbst nach dem Einschalten dieser Einträge nichts, womit man sie auswählen
könnte.

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
- **HIPS** und **PVA** fehlen auch in 2.5.10 weiterhin. Wie schon in 2.5.7 gibt es
  INDX-Einträge für beide, aber nur unter den auskommentierten.

Die für Anwender sichtbare Standard-Materialliste beider INDX-Modelle wurde hier als die
übliche PLA- und PETG-Familie beschrieben, was sie schon im August untertrieb. Stand
2.5.10 umfasst sie PLA, PETG, ASA, die PC Blends und Woodfill sowie seit 2.5.9 TPU 95A,
alle für die eine verfügbare Variante.

**Firmware 6.9.1 bringt PVA und BVOH auf den Drucker, und das ist nicht dasselbe.** Die
[stabile Version](https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.9.1)
vom 25. September führt Filament-Presets für PVA und BVOH als neu auf. Das sind die
eigenen Filamenteinträge des Druckers, die man beim Laden einer Spule an der Maschine
verwendet; sie fügen PrusaSlicer kein Druckprofil hinzu. BVOH ist damit an beiden Enden
abgedeckt, während sich PVA zwar am Drucker laden lässt, aber weiterhin kein INDX-Preset
hat, mit dem man es slicen könnte.

Das ist mehr als eine Frage der Bequemlichkeit: HIPS und die löslichen Materialien sind
das, wozu man greift, um auf einem Werkzeugwechsler Kontaktflächen von Stützstrukturen
zu drucken — und genau das ist zu einem großen Teil der Grund, warum man sich einen
anschafft. BVOH deckt den löslichen Fall bei der einen Düsengröße nun ab; HIPS und PVA
noch nicht.

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

- **Schließen Sie sich der offenen Anfrage an.** Es ist
  [Issue 45 in Prusas FFF-Settings-Repository](https://github.com/prusa3d/PrusaSlicer-settings-prusa-fff/issues/45),
  offen seit dem 31. Juli 2026 und am 25. September weiterhin ohne Kommentar und ohne
  Reaktion. Ein Issue mit einem einzigen Melder und ohne Resonanz bleibt leicht
  unbeachtet; mehrere Besitzer, die benennen, welche Größen und Materialien sie
  tatsächlich brauchen, lassen sich schwerer übergehen. Die Material-Presets vom
  September kamen übrigens, ohne dass das Issue angerührt wurde; sein Schweigen sagt
  also wenig über den Fortschritt, in die eine wie die andere Richtung.
- **Nehmen Sie Bundle-Updates mit, wenn sie kommen.** Die INDX-Presets werden mit dem
  Profil-Bundle ausgeliefert, nicht mit dem Slicer: Die Bundle-Reihe, die sie enthält,
  setzt PrusaSlicer 2.9.6 voraus, die aktuelle Version auf Prusas Download-Seite, und
  jedes neue Bundle erreicht sie als Konfigurations-Update statt als neue Slicer-Version.
- **Kaufen Sie Düsen unter der Annahme, sie noch nicht nutzen zu können**, oder warten
  Sie ab. Wenn Sie zwischen den Entschädigungsformen wählen, spricht das für Bargeld
  statt Guthaben, sofern es Sie nicht stört, die Hardware ungenutzt zu halten.

TODO(verify): ob sich ein eigenes Profil für eine andere Düsengröße von Hand zum Laufen
bringen lässt und was dabei zerbricht. Niemand in den Quellen berichtet von einem
solchen Versuch, und diese Seite spekuliert nicht — das Spül- und Kalibrierverhalten des
Werkzeugwechslers hängt auf nicht offensichtliche Weise am Profil.

## Überprüfung

`reported` (mehrfach berichtet), und der tragende Teil ist stärker, als diese Stufe
verlangt.

**Die zentrale Aussage ist verifiziert, nicht bloß berichtet.** Dass nur `HF0.4`
angeboten wird, ergibt sich aus dem Lesen von Prusas eigenem veröffentlichtem
Profil-Bundle, in dem beide INDX-Druckermodelle diese eine Variante deklarieren. Das
sind veröffentlichte Daten aus erster Hand, in derselben Klasse wie eine Anmerkung zu
einer Firmware-Veröffentlichung — und nicht die Schilderung einer fremden Maschine. Am
25. September 2026 wurde es anhand von 2.5.10 erneut gelesen, ebenso wie die
Material-Presets, die auskommentierten Einträge und die oben beschriebenen
Kompatibilitätsbedingungen.

**Die Auswirkung ist berichtet**, von vier Besitzern in
[einem Forumsthread](https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/missing-profiles-in-slicer-for-non-0-4-nozzles-and-other-materials/),
von denen einer Düsen mit 0.5 und 1.0mm kaufte, bevor er feststellte, dass sie sich
nicht nutzen lassen, und ein anderer die Sache beim Abwägen der Düsen-Entschädigung
ansprach. Die
[Upstream-Anfrage](https://github.com/prusa3d/PrusaSlicer-settings-prusa-fff/issues/45)
ist ein zweiter Ort, wurde jedoch von derselben Person eingereicht, die den
Forumsthread eröffnet hat, und ist damit ein Cross-Post statt einer unabhängigen
Bestätigung. Ein
[separater Thread](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/firmware-and-slicer-update-to-use-other-nozzles-than-0-4hf/),
im September von einem anderen Besitzer eröffnet, fragt, wann die Standard-Flow-Düsen,
die der Hersteller inzwischen liefert, unterstützt werden. Das ist eine Frage und kein
Bericht davon, an einer Maschine auf die Lücke gestoßen zu sein, zeigt dieselbe Lücke
aber aus einer zweiten, unabhängigen Richtung.

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

**Wo das schwächer ist, als es aussieht.** Ob FLEX wirklich nutzbar ist, bleibt unklar:
Die Vorlagen sind im Bundle vorhanden, doch das ist nicht dasselbe wie ein auswählbares,
getestetes Profil, und kein Besitzer in den Quellen berichtet, damit gedruckt zu haben.
Behandeln Sie die obigen Materialbefunde als Beschreibung dessen, was in der Datei
steht, und nicht dessen, was funktioniert. Seit 2.5.9 sind die Presets für flexible
Filamente und BVOH auswählbar, was die erste Hälfte davon erledigt; die zweite Hälfte
bleibt bestehen, denn kein Besitzer in den Quellen berichtet, mit ihnen TPU, FLEX oder
BVOH auf einem INDX gedruckt zu haben.

Das veraltet schnell. Es ist eine Konfigurationslücke, die eine Profilveröffentlichung
mit einem einzigen Update schließt; prüfen Sie daher das aktuelle Bundle, bevor Sie
danach handeln. Teilweise ist das schon geschehen: Die Materialliste hat sich binnen
eines Monats nach dieser Seite bewegt, die Düsenvarianten nicht.

## Verwandte Themen

- [Düsenhärte](nozzle-hardness.md) — die Entschädigung, mit der dies zusammenwirkt
- [Kommentierter Profil-G-Code](../gcode/indx-profile-gcode.md) — was ein Profil
  mitführt und warum die Düsendeklaration pro Werkzeug von Bedeutung ist
