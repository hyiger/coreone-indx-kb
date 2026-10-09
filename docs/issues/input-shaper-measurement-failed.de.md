---
title:        Input-Shaper-Kalibrierung bricht mit „Measurement failed“ ab
confidence:   provisional
updated:      2026-10-08
author:       hyiger
printer:      Core One / Core One+ with INDX, mostly Founders Edition; one Founders Edition with the Gen 2 upgrade
toolhead:     INDX (one report is an 8-tool head; the rest do not say)
hotend:       unknown
nozzle:       unknown
firmware:     6.9.0 and 6.9.1-beta; one report also on 6.6.3
sources:
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5436
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.6.0
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.6.3
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.9.0
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.9.1
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/compare/v6.9.0...v6.9.1
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.9.2
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/compare/v6.9.1...v6.9.2
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/src/feature/factory_reset/factory_reset.hpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/src/feature/factory_reset/factory_reset.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/src/gui/screen/screen_factory_reset.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/src/persistent_stores/store_instances/config_store/store_definition.hpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/src/persistent_stores/store_instances/config_store/store_definition.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/src/common/printer_variant/coreone.hpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/src/gui/MItem_hardware.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.6.3/src/persistent_stores/store_instances/config_store/store_definition.hpp
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/coreone-with-mmu-upgrade-to-indx/
  - https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/toolhead-docking-calibration-fails/
superseded_by:
source_sha:   23616c2a551975af7eef4f40e62c46096a76787b3c52b7dcf11c10c0712f6ce1
---
# Input-Shaper-Kalibrierung bricht mit „Measurement failed“ ab

!!! warning "Ein offenes Issue, mehrere Melder, keine Ursache gefunden"
    Jeder Bericht über diesen Fehler stammt aus einem einzigen GitHub-Issue. Mehrere
    INDX-Besitzer haben dort eigene Berichte ergänzt, doch ein Issue ist eine Quelle, und
    Prusa hat noch nicht gesagt, woran es liegt. `provisional`.

## Zusammenfassung

An INDX-Druckern mit der Firmware 6.9.0 oder der Beta von 6.9.1 kann die
Input-Shaper-Kalibrierung bei ihrer ersten Messung mit „Measurement failed.“ abbrechen,
obwohl der Beschleunigungssensor gerade anstandslos kalibriert wurde. Prusa untersucht
das Problem, und das Issue ist offen; in den Versionshinweisen zu 6.9.1 geht nichts
darauf ein, und 6.9.2, erschienen am 7. Oktober 2026, ändert nur die
Filament-Presets des Druckers. Ob die stabile Version 6.9.1, die nach den meisten
dieser Berichte erschien, oder 6.9.2 betroffen ist, sagt bisher kein Bericht; der
jüngste Bericht nennt keine Firmware-Version. Die erste Prüfung, die ein
Prusa-Entwickler nannte, galt der Einstellung **1.5GT Belts**, die zu den tatsächlich im
Drucker eingebauten Riemen passen muss. Die Rückkehr zur Firmware 6.6.3 brachte die
Kalibrierung bei zwei Besitzern wieder zum Laufen. Bei einem dritten scheiterte sie auch
unter 6.6.3, und sie gelang ihm erst, nachdem er zusätzlich „Common Misconfigurations“
zurückgesetzt hatte.

## Im Einzelnen

### Was Besitzer sehen

Der Ablauf ist in jedem ausführlichen Bericht derselbe: Die Kalibrierung des
Beschleunigungssensors wird abgeschlossen, dann scheitert die erste Achsmessung — X,
sofern die Achse genannt wird — mit „Measurement failed.“ Die Phase-Stepping-Kalibrierung
funktioniert an dem einen Drucker, bei dem sie erwähnt wurde, weiterhin.

[GitHub #5436](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5436) wurde von
einem Besitzer einer Founders Edition unter 6.9.0 eröffnet, der angab, der Fehler habe
mit der neuen Firmware begonnen und sei nach dem erneuten Flashen von 6.6.3
verschwunden. Weitere folgten:

- ein Besitzer ohne weitere Angaben;
- ein Besitzer unter 6.9.1-beta, dessen Drucker auf Core One+ eingestellt und bei dem
  die Option 1.5GT Belts ausgeschaltet war; auch bei ihm behob die Rückkehr zu 6.6.3 das
  Problem;
- ein Besitzer einer Founders Edition, bei dem es unter 6.6.3, 6.9.0 und 6.9.1-beta
  gleichermaßen scheiterte, obwohl 6.6.3 einen Monat zuvor noch einwandfrei kalibriert
  hatte. Er hatte das Filament entladen, den Drucker abkühlen lassen, die Riemen
  nachgespannt, die Rechtwinkligkeit des Portals geprüft und Vibrationen von außen
  ausgeschlossen;
- zuletzt ein Besitzer einer Founders Edition mit 8 Werkzeugen, mit dem Gen-2-Upgrade und
  den dazugehörigen 1.5GT-Riemen.

### Wo sich die Berichte widersprechen

Der Ersteller des Issues und der Besitzer unter 6.9.1-beta sagen beide, das erneute
Flashen von 6.6.3 habe den Fehler behoben. Der Besitzer, der die Riemen nachgespannt
hatte und dessen Drucker einen Monat zuvor unter 6.6.3 kalibriert hatte, sagt, es sei
auch unter 6.6.3 gescheitert. Später brachte er es zum Laufen, indem er 6.6.3 erneut
flashte **und** „Common Misconfigurations“ zurücksetzte; bei ihm ist also nicht bekannt,
welcher der beiden Schritte es bewirkt hat. Diese Seite gibt beide Darstellungen wieder
und entscheidet sich für keine.

„Common Misconfigurations“ ist einer der Einträge auf dem Bildschirm **Factory Reset**
des Druckers (`Settings > System > Factory Reset`), und das dortige Preset
„Fix Common Misconfigurations“ setzt diesen Eintrag zurück und behält alle anderen bei,
die Hardwarekonfiguration eingeschlossen, sodass die Riemeneinstellung erhalten bleibt.
Der Firmware-Quellcode beschreibt, was das Preset löscht, als experimentelle
Einstellungen und ähnliche Anpassungen, die Probleme verursachen können. In der Praxis
löscht es gespeicherte Überschreibungen wie die X/Y-Schritte pro Millimeter, die
Motorströme und das Microstepping, und es setzt außerdem die Homing-Empfindlichkeit und
die PID-Werte auf ihre Standardwerte zurück. Ob dieses Zurücksetzen allein, ohne
Downgrade, den Fehler unter 6.9.x behebt, wurde nicht berichtet.

### Was Prusa gesagt hat

Ein Prusa-Entwickler wies darauf hin, dass 6.9 die erste Firmware mit Unterstützung für
1.5GT-Riemen ist. Ist diese Option an einem Drucker eingeschaltet, der diese Riemen nicht
hat, wird die Bewegung für den falschen Riemen skaliert, was nach Aussage des
Entwicklers die Messung verfälschen könne. Die beiden Besitzer, die antworteten, hatten sie
ausgeschaltet, und keiner von beiden gab an, 1.5GT-Riemen zu haben; ihre Fehler erklärt
das also nicht. Der Entwickler bat daraufhin um ein Log: `Settings > System > Save Logs To File`
einschalten, die Kalibrierung bis zum Scheitern laufen lassen und das Logging wieder
ausschalten, bevor der USB-Stick abgezogen wird, damit die Datei vollständig geschrieben
wird. Zwei Besitzer hängten Logs an, und Prusa sagte, das Problem werde intern verfolgt.

Weder die Versionshinweise zu 6.9.1 noch die Titel der Commits zwischen 6.9.0 und 6.9.1
erwähnen Input Shaping oder den Beschleunigungssensor. Die einzige Quelldatei des Input
Shapers, die sich zwischen den beiden Tags geändert hat, enthält lediglich ein kleines
Refactoring der Art, wie Filternamen nachgeschlagen werden. Am INDX ändert 6.9.2 nichts
außer den Filament-Presets für PVA und BVOH, die in den Versionshinweisen zu 6.9.1
angekündigt waren, in jener Version selbst aber fehlten. 6.9.2 berührt keinen Code des
Input Shapers oder des Beschleunigungssensors.

Zuvor hatten Prusas Versionshinweise zu 6.6.0, der ersten INDX-Firmware, gelegentliche
Fehler bei der Input-Shaper- und der Phase-Stepping-Kalibrierung als bekanntes Problem
aufgeführt, das ein Neustart und ein zweiter Versuch meist beheben würden. Die
Versionshinweise zu 6.6.3, 6.9.0 und 6.9.1 wiederholen das nicht, und niemand in #5436
sagt, ob er einen Neustart versucht hat.

## Was zu tun ist

**Prüfen Sie zuerst die Riemeneinstellung.** Der Eintrag **1.5GT Belts** in den
Hardwareeinstellungen des Druckers muss zu den Riemen an der Maschine passen:
eingeschaltet für 1.5GT-Riemen, ausgeschaltet für die ursprünglichen. Nachsehen kostet
nichts, und es ist die einzige Prüfung, die Prusa genannt hat.

Gehen Sie nicht davon aus, dass sie stimmt. Zwei Besitzer stellten in getrennten
Forenthreads fest, dass der Drucker nach dem Flashen der INDX-Firmware angenommen hatte,
die Gen-2-Riemen seien eingebaut. Bei
[einem](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/coreone-with-mmu-upgrade-to-indx/)
traf das zu. Der
[andere](https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/toolhead-docking-calibration-fails/)
hatte die Gen-2-Teile noch nicht eingebaut, und die Dock-Kalibrierung scheiterte
daraufhin; siehe
[Dock-Kalibrierung lehnt einige oder alle Docks ab](dock-calibration-rejects-docks.md)
und die [Montagehinweise](../reference/assembly-notes.md). Der Ersteller dieses Issues,
der von 6.6.3 kam, fand die Option ausgeschaltet vor. Prusas Firmware-Quellcode passt zu
beidem: Der gespeicherte Standardwert ist „aus“, doch ein erster Start
oder ein Zurücksetzen auf Werkseinstellungen, das die Hardwarekonfiguration löscht,
wendet die Gen-2-Variante an und schaltet die Option dabei ein. Dass das Flashen der
INDX-Firmware als erster Start zählt, ist erschlossen, nicht bestätigt. Nach derselben
Lesart behält ein Drucker, der ohne Zurücksetzen von 6.6.3 aus aktualisiert wurde —
einer Version ganz ohne Riemeneinstellung —, die Option ausgeschaltet, selbst wenn
seither Gen-2-Riemen eingebaut wurden. Auch das ist aus dem Quellcode erschlossen; der
jüngste Melder, der diese Riemen hat, gab nicht an, wie die Einstellung bei ihm steht.

Ändern Sie die Einstellung erst, wenn Sie wissen, welche Riemen eingebaut sind; die
Seite [Dock-Kalibrierung lehnt einige oder alle Docks ab](dock-calibration-rejects-docks.md)
beschreibt, wie man sie durch Zählen der Zähne unterscheidet. Der Drucker warnt beim
Ändern, und Prusas Quellcode zeigt, dass die Änderung die Ergebnisse von Homing,
Riemenabstimmung, Rechtwinkligkeit des Portals und X/Y-Selbsttest zurücksetzt. Starten
Sie also neu, wenn Sie dazu aufgefordert werden, und führen Sie die Kalibrierungen von
Anfang an erneut aus, bevor Sie es wieder mit der Input-Shaper-Kalibrierung versuchen.
War die Einstellung bereits richtig, lassen Sie sie, wie sie ist.

**Starten Sie neu und versuchen Sie es noch einmal.** Das kostet nichts, und es war
Prusas Rat bei den Input-Shaper-Fehlern, die in 6.6.0 als bekanntes Problem aufgeführt
waren. `provisional` — niemand hat berichtet, ob es bei diesem Fehler unter 6.9.x hilft.

**Erfassen Sie ein Log und fügen Sie es #5436 hinzu**, statt ein neues Issue zu
eröffnen, und folgen Sie dabei den oben beschriebenen Schritten zum Logging. Geben Sie
an, welche Riemen Sie haben und für welchen Drucker die Firmware Ihr Gerät hält.

**Wenn Sie das Zurücksetzen von Common Misconfigurations versuchen**, verwenden Sie nur
das Preset Fix Common Misconfigurations und lassen Sie jeden anderen Eintrag auf Keep.
Es lässt sich nicht rückgängig machen und verwirft die oben aufgeführten
Überschreibungen und abgestimmten Werte. Verwenden Sie weder Full Reset noch den
Hard-Reset am Ende der Liste noch eine Auswahl, die HW Configuration zurücksetzt: Diese
stellen den Gen-2-Standard des ersten Starts wieder her, die Riemeneinstellung
eingeschlossen, was an einem Drucker mit den ursprünglichen Riemen genau die
Fehlkombination erzeugt, vor der der Entwickler gewarnt hat. Prüfen Sie den Eintrag
1.5GT Belts nach jedem Zurücksetzen erneut.

**Wägen Sie ein Downgrade sorgfältig ab.** Die Rückkehr zu 6.6.3 half zwei Besitzern,
bei denen die Option 1.5GT ausgeschaltet war, einem dritten aber erst, nachdem er
zusätzlich Common Misconfigurations zurückgesetzt hatte. Außerdem gibt man damit auf,
was später kam, darunter die Homing-Korrektur aus 6.9.1 und den Assistenten zur
Rechtwinkligkeit des Portals. An einem Gen-2-Drucker oder an jedem Drucker mit
1.5GT-Riemen ist es wahrscheinlich gar keine Option: Prusa hat 6.6.3 für die Core One
INDX und die Core One+ INDX veröffentlicht, und die Unterstützung für die Gen-2-Hardware
und die 1.5GT-Riemen beginnt mit 6.9.0. Unter 6.6.3 würden diese Riemen also mit den
Schritten pro Millimeter der ursprünglichen Riemen betrieben: dieselbe Art von Fehlkombination,
vor der der Entwickler gewarnt hat, nur in umgekehrter Richtung. Das ist aus den
Versionshinweisen und dem Firmware-Quellcode erschlossen; niemand hat berichtet, es
versucht zu haben.

## Überprüfung

`provisional` — ein GitHub-Issue. Mehrere Besitzer beschreiben darin denselben Fehler,
doch an einer Stelle gesammelte Berichte sind keine unabhängige Bestätigung. Einer der
fünf fügt außer Zustimmung nichts hinzu, und zwei (der Ersteller und der jüngste) machen
nur wenige Angaben; der jüngste sagt nicht, wie bei ihm die Einstellung 1.5GT Belts
steht. Der Widerspruch, ob 6.6.3 allein das Problem behebt, ist ungelöst. Ob die stabile
Version 6.9.1 oder 6.9.2 betroffen ist, sagt bisher kein Bericht. Bei einer erneuten
Prüfung am 8. Oktober 2026 hatte das Issue keine Kommentare, die neuer waren als der
jüngste Bericht.

Die beiden Berichte über die Riemeneinstellung in den Montagehinweisen betreffen die
Einstellung und die Dock-Kalibrierung; keiner von beiden berichtete diesen Fehler. Die
beiden Forenthreads in den Quellen werden nur für diese Berichte zur Riemeneinstellung
angeführt. Keiner der für diese Website gesammelten Forenthreads berichtet über den
Fehler.

**Erstanbieter.** Die Presets unter Factory Reset, was der Eintrag
Common Misconfigurations umfasst, der gespeicherte Standardwert der Riemeneinstellung,
die Gen-2-Variante, die bei einem ersten Start und nach einem Zurücksetzen der
Hardwarekonfiguration angewendet wird, und was eine Änderung der Riemeneinstellung
zurücksetzt, stammen alle aus Prusas Firmware-Quellcode beim Git-Tag 6.9.1; dass 6.6.3
keine Riemeneinstellung hat, stammt aus dem Quellcode bei dessen Tag. Dass 6.9.2 nur die
Filament-Presets ändert, ergibt sich aus dem
[Vergleich ihres Tags mit dem von 6.9.1](https://github.com/prusa3d/Prusa-Firmware-Buddy/compare/v6.9.1...v6.9.2).
Die Warnung beim Ändern der Riemeneinstellung ist die des Druckers selbst. Das bekannte
Problem mit Fehlern bei der Input-Shaper-Kalibrierung stammt aus Prusas
Versionshinweisen zu 6.6.0.

Was weiterhelfen würde: dass Prusa eine Ursache nennt oder eine Behebung ausliefert,
oder ein Bericht in einem separaten Thread oder Issue.

## Verwandte Seiten

- [Dock-Kalibrierung lehnt einige oder alle Docks ab](dock-calibration-rejects-docks.md) —
  dieselbe Riemeneinstellung; wie Sie erkennen, welche Riemen Sie haben, und was eine
  Änderung zurücksetzt
- [Wen Sie kontaktieren](support-and-warranty-path.md) — wenn ein Downgrade keine Option
  ist und das Issue offen bleibt
- [Montagehinweise](../reference/assembly-notes.md) — der Bildschirm der
  Hardwarekonfiguration nach dem ersten Flashen, einschließlich der Riemeneinstellung
