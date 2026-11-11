---
title:        Fehlercodes der Werkzeug-Offset-Kalibrierung
confidence:   provisional
updated:      2026-11-08
author:       hyiger
printer:      Core One, Core One L
toolhead:     INDX
hotend:       unknown
nozzle:       unknown
firmware:     stock firmware reports all of these as 36130 through 7.0.1 (source-checked); stock 8.0.0 splits them over 36130, 36144, 36145 and 36146 (source-checked, not yet reported on hardware); the 3619x codes need firmware built from hyiger/Prusa-Firmware-Buddy
sources:
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/src/feature/tool_offset_calibration/tool_offset_calibration.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/lib/Marlin/Marlin/src/feature/contactless_offset/contactless_offset.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5482
  - https://github.com/hyiger/Prusa-Firmware-Buddy/blob/master/lib/Prusa-Error-Codes/yaml/buddy-error-codes.yaml
  - https://help.prusa3d.com/article/tool-offset-failed-36130-core-one-indx_1089016
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/lib/Prusa-Error-Codes/yaml/buddy-error-codes.yaml
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.6.3/src/feature/tool_offset_calibration/tool_offset_calibration.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5500
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.9.1-beta
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.9.2
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/compare/v6.9.1...v6.9.2
  - https://help.prusa3d.com/downloads/core-one-indx
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5548
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5526
  - https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/tool-offset-calibration-failing/
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5518
  - https://github.com/prusa3d/Prusa-Error-Codes/blob/9e609385d1c18cc080bcfaaf2bd1d6a7cd7cf5ad/yaml/buddy-error-codes.yaml
  - https://github.com/prusa3d/Prusa-Error-Codes/commit/a88544c7628067f03c768a26624000c463e971b6
  - https://github.com/prusa3d/Prusa-Error-Codes/commit/8a502d03acc0c5bf3ba524d68c6e10bd4c8d1acf
  - https://github.com/prusa3d/Prusa-Error-Codes/commit/bc278daf0a10e6657048416623a9e2e7f7845643
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v7.0.0
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v7.0.1
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v8.0.0
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/compare/v6.9.2...v7.0.1
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/compare/v6.9.2...v8.0.0
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/src/feature/tool_offset_calibration/tool_offset_calibration.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/lib/Marlin/Marlin/src/feature/contactless_offset/contactless_offset.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/src/common/tool_offset_failure_reason.hpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/src/common/marlin_server_types/fsm/tool_offsets_calibration_mapper.hpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/src/feature/tool_offset_wizard/screen_tool_offset_wizard.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/src/module/contactless_offset/src/contactless_offset/can_remote_sensor.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/lib/Prusa-Error-Codes/yaml/buddy-error-codes.yaml
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/8-0-0-firmware-for-prusa-core-one-gen-2-indx-core-one-indx/
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5577
superseded_by:
source_sha:   528dc6d509dfcb23c563a95a9b7296ad08efd229a26b2bc2ff3da5f645cb552d
---
# Fehlercodes der Werkzeug-Offset-Kalibrierung

## Zusammenfassung

Bis einschließlich 7.0.1 zeigt die Standard-Firmware für elf verschiedene Arten, auf
die die Werkzeug-Offset-Kalibrierung fehlschlagen kann, ein und denselben Bildschirm,
36130, und dieser Bildschirm fordert Sie immer auf, Düse und Sensor zu reinigen. Die
Standard-Firmware 8.0.0 führt für einige davon drei eigene Codes ein, 36144 Sensor Not
Found, 36145 Sensor Failure und 36146 Tool Not Picked, und belässt den Rest bei 36130,
das nun das betroffene Werkzeug nennt; siehe
[was die Standard-Firmware 8.0.0 zeigt](#stock-800).
Firmware, die aus
[hyiger/Prusa-Firmware-Buddy](https://github.com/hyiger/Prusa-Firmware-Buddy)
gebaut ist, teilt diese elf auf neun Bildschirme auf. 36130 behält den einen Fehler,
zu dem seine Meldung passt, nämlich dass die Abtastfahrten über den Sensor die Düse
nicht finden, und 36190 bis 36197 benennen den Rest. Der QR-Code auf jedem dieser
Bildschirme öffnet den zugehörigen Abschnitt auf dieser Seite. Die Aufteilung des Forks
ist älter als die Version 8.0.0 und nicht die, die 8.0.0 übernommen hat. Die
Abschnitte unten sind nach den Codes des Forks gegliedert, und jeder sagt, was die
Standard-Firmware bei diesem Fehler zeigt.

Bei jeder Standard-Version sagt das [serielle Log](#stock-firmware) weiterhin, welcher
dieser Fehler es war. Prusa hat den Quellcode von 7.0.0, 7.0.1 und 8.0.0 am
3. November 2026 veröffentlicht. Bis einschließlich 7.0.1 zeigt jeder Fehler auf dieser
Seite 36130 und schreibt dieselben Log-Zeilen wie 6.9.2. 8.0.0 ändert sowohl die
Bildschirme als auch die Log-Zeilen. Prusa hat seine neuen Codes zwischen dem
21. September und dem 5. Oktober 2026, noch vor dem Erscheinen von 6.9.2, in seine
öffentliche Fehlercode-Liste aufgenommen, aber erst 8.0.0 zeigt sie an. Noch kein
Besitzer hat einen der neuen Bildschirme gemeldet.

Am Core One L beginnen die Codes mit 37 statt mit 36: 37130, 37144 bis 37146 und
37190 bis 37197. Jeder Abschnitt unten gilt für beide.

| Code | Der Bildschirm beginnt mit | Was fehlgeschlagen ist | Die Standard-Firmware 8.0.0 zeigt |
|---|---|---|---|
| [36130](#36130) | Tool offset calibration failed | Die Abtastfahrten liefen, fanden die Düse aber nicht | 36130, oder 36145, wenn eine Abtastfahrt an einem vom Sensor gemeldeten Fehler scheiterte |
| [36190](#36190) | The tool is not detected as picked | Der Drucker betrachtet das Werkzeug nicht als aufgenommen | 36146, oder 36130 bei der Temperaturprüfung |
| [36191](#36191) | Nozzle cleaning before tool offset calibration failed | Ein Reinigungsablauf wurde nicht abgeschlossen | 36130 |
| [36192](#36192) | Probing the bed for tool offset calibration failed | Eine Berührung auf der Druckplatte wurde verworfen | 36130 |
| [36193](#36193) | Probing the tool offset sensor failed | Die Berührung auf der Sensorplatine wurde verworfen | 36144 |
| [36194](#36194) | The tool offset sensor sent no usable data | Keine Abtastfahrt lieferte auswertbare Sensordaten | 36145, wenn der Sensor einen Fehler gemeldet hat, sonst 36130 |
| [36195](#36195) | The toolhead board restarted | Die Platine des INDX-Kopfs startete während der Abtastfahrten neu | 36145 |
| [36196](#36196) | The nozzle did not cool down enough | Die Düse blieb über der Temperaturgrenze für das Abtasten | 36130 |
| [36197](#36197) | Homing failed during tool offset calibration | Das Referenzieren vor der Messung schlug fehl | 36130, sofern überhaupt ein Bildschirm erscheint |

## Wie die Kalibrierung abläuft

Es hilft, die Reihenfolge der Schritte zu kennen, denn jeder Code ist das Scheitern
eines dieser Schritte.

Zu Beginn eines Drucks arbeitet der Drucker die Werkzeuge, die der Druck verwendet,
nacheinander ab. Er nimmt das Werkzeug auf und reinigt es im Düsenreiniger. Ein Druck
mit nur einem Werkzeug hört hier auf, weil es keinen Versatz zwischen Werkzeugen zu
messen gibt. Andernfalls berührt das Werkzeug die Druckplatte an einem Punkt auf einer
Linie nahe ihrer Vorderkante, wobei das erste Werkzeug beide Enden dieser Linie
berührt, und die Unterschiede zwischen diesen Berührungen ergeben die Z-Offsets der
Werkzeuge. Aus dem Kalibriermenü gibt es keine Reinigung und keine Berührung der
Druckplatte: Sie reinigen die Düsen selbst, und die Z-Offsets misst erst der nächste
Druck.

Zuletzt wird das Werkzeug über dem Offsetsensor vermessen. Die Düse setzt direkt neben
der Spule auf der Sensorplatine auf, um die Höhe der Sensoroberfläche zu finden.
Danach fährt sie mit zwei Geschwindigkeiten entlang X und entlang Y über der Spule hin
und her. Der Sensorwert erreicht seine Spitze, wenn die Düsenspitze die Spule
überquert, und die Firmware errechnet die Düsenposition aus der Lage dieser Spitzen.
Jede Abtastfahrt erhält einen Konfidenzwert, und beide Achsen brauchen eine Abtastfahrt
mit hoher Konfidenz. Die Firmware wiederholt jede Achse eine begrenzte Anzahl von
Malen, und wenn eine Abtastfahrt entlang Y nichts findet, verschiebt sie die Fahrt zur
Seite und versucht es erneut.

Bis einschließlich 7.0.1 reinigt Retry nach einer fehlgeschlagenen Messung über dem
Sensor das Werkzeug erneut und misst es noch einmal. Retry auf den anderen Bildschirmen
beginnt wieder beim ersten Werkzeug. Ab 8.0.0 fordert Retry nach jedem Fehler in den
Schritten eines Werkzeugs dieses Werkzeug erneut an, was es nur dann neu aufnimmt, wenn
der Drucker es nicht mehr als ausgewählt betrachtet, reinigt es dann während eines
Drucks erneut und vermisst nur dieses Werkzeug; die bereits vermessenen Werkzeuge
behalten ihre Ergebnisse
([Quellcode von 8.0.0](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/src/feature/tool_offset_calibration/tool_offset_calibration.cpp)).
Abort bricht den Druck ab oder beendet die Kalibrierung aus dem Menü. Keine Version
wiederholt von sich aus: Der Drucker wartet auf dem Bildschirm, bis Sie wählen. Ein
Besitzer hat stattdessen ein automatisches Reinigen und Wiederholen angeregt
([Firmware-Issue 5577](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5577),
offen).

Nach dem letzten Werkzeug vergleicht der Drucker die Offsets der Werkzeuge
miteinander und hält an, wenn die Z-Offsets, die XY-Offsets oder die daraus folgende
Sensorposition aus dem Rahmen fallen. Die Standard-Firmware gibt diesen Prüfungen
eigene Codes: 36131 Unsafe Z Tool Offset, 36133 Unsafe XY Tool Offset und 36134 Unsafe
Sensor Position, am Core One L 37131, 37133 und 37134. Diese Seite behandelt sie nicht.
Retry beginnt bei ihnen wieder beim ersten Werkzeug, unter 8.0.0 wie zuvor.

**Welches Werkzeug am Kopf ist.** Im Standard-Quellcode parkt jeder Fehlerbildschirm
der Kalibrierung den Kopf zuerst vorne, wo die Düse in Reichweite ist. Ein Fehler
während der Schritte eines Werkzeugs erscheint, während dieses Werkzeug noch am Kopf
ist, es sei denn, der Fehler besteht gerade darin, dass der Drucker nicht sicher weiß,
welches Werkzeug er hält (36130 mit der Standard-Firmware bis 7.0.1, 36146 unter 8.0.0,
36190 mit den Codes des Forks). Die Vergleichsprüfungen kommen nach dem letzten
Werkzeug, daher ist das Werkzeug am Kopf dann das zuletzt vermessene, und das muss
nicht dasjenige sein, dessen Offset aus dem Rahmen fiel. Ein Besitzer meldet mit der
Standard-Firmware 6.9.1, dass der Bildschirm mit einem sauberen Werkzeug am Kopf
erscheint, während das davor kalibrierte Werkzeug dasjenige mit Material daran war,
und sagt, ältere Firmware habe das verschmutzte Werkzeug präsentiert
([Firmware-Issue 5500](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5500)).
Der Bericht nennt keinen Code. Der Besitzer spricht von einem Z-Offset-Fehler, und wäre
es 36131, würde die Reihenfolge oben das erklären. Ebenso würde es Material erklären,
das das vorige Werkzeug auf der Sensorplatine hinterlassen hat, wo jedes Werkzeug
aufsetzt. Keine der beiden Lesarten ist bestätigt.

Ab 8.0.0 sagt der Bildschirm, welches Werkzeug Sie ansehen sollten, mit Einschränkungen.
Im Quellcode nennen 36130 und 36146 das Werkzeug, dessen Schritt fehlschlug. Die
Bildschirme 36131 und 36133 nennen das Werkzeug, das am weitesten abweicht, also
dasjenige, ohne das die Streuung am stärksten schrumpfen würde, aber nur, wenn
mindestens drei Werkzeuge vermessen wurden; bei zweien gibt es keine Mehrheit, an der
sich messen ließe, und es wird kein Werkzeug genannt. 36134, 36144 und 36145 nennen
kein Werkzeug
([Bildschirmdefinitionen](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/src/feature/tool_offset_wizard/screen_tool_offset_wizard.cpp)).
Die Versionshinweise zu 8.0.0 sagen, jeder Fehlerbildschirm zeige das betroffene
Werkzeug, auch bei unsicheren Messungen. Im Quellcode gilt das für 36130 und 36146;
36131 und 36133 nennen ein Werkzeug nur, wenn drei oder mehr Werkzeuge vermessen
wurden, und 36134, 36144 und 36145 nennen keines. Das Werkzeug am Kopf ist nach einer
Vergleichsprüfung weiterhin das zuletzt vermessene. Ein 36131 unter 8.0.0 bei einem
Druck mit drei oder mehr Werkzeugen würde den Ausreißer nennen, aber bisher hat noch
kein Besitzer einen gemeldet.

Im
[Quellcode von 6.6.3](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.6.3/src/feature/tool_offset_calibration/tool_offset_calibration.cpp)
laufen Schritte und Prüfungen in derselben Reihenfolge. Eine dokumentierte Änderung
betrifft den Bericht aber durchaus. Seit
[6.9.1-beta](https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.9.1-beta)
macht die Kalibrierung laut den Versionshinweisen bis zu 10 Versuche für ihr
Z-Abtasten statt 3. Im
[Quellcode von 6.9.1](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/lib/Marlin/Marlin/src/feature/contactless_offset/contactless_offset.cpp)
ist das die Berührung auf der Sensorplatine. Die Berührungen auf der Druckplatte, aus
denen die Z-Offsets hervorgehen, gehören nicht zu dieser Änderung, und die zusätzlichen
Versuche wiederholen nur: Eine Berührung, die die Abtastung verwirft, wird weiterhin
nicht akzeptiert. Ein Werkzeug mit Material daran bekommt also mehr Gelegenheiten für
eine akzeptierte Berührung auf der Sensorplatine und damit dafür, seine eigenen
Schritte abzuschließen, wo ihm früher eher die Versuche ausgingen und es auf seinem
eigenen Bildschirm stehen blieb. Hatte das Material auch seine Berührung auf der
Druckplatte verfälscht, würde sich das dann erst beim Z-Vergleich zeigen, mit dem
zuletzt vermessenen Werkzeug am Kopf. Das ist eine Lesart des Quellcodes, keine bestätigte
Ursache. Steht beim Fehlerbildschirm ein sauberes Werkzeug am Kopf, prüfen Sie auch die
davor vermessenen Werkzeuge.

## Was die Standard-Firmware 8.0.0 zeigt {#stock-800}

Ab 8.0.0 endet ein Fehler in den Schritten eines Werkzeugs auf einem von vier
Bildschirmen, jeder mit Retry und Abort. Welcher Fehler welchen Bildschirm bekommt,
wird an einer Stelle im
[Quellcode der Kalibrierung](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/src/feature/tool_offset_calibration/tool_offset_calibration.cpp)
entschieden, anhand der
[Fehlergründe](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/src/common/tool_offset_failure_reason.hpp),
die die Messung meldet, und die Codes stammen aus der
[Zuordnung von Bildschirm zu Code](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/src/common/marlin_server_types/fsm/tool_offsets_calibration_mapper.hpp)
und der
[Fehlercode-Liste](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/lib/Prusa-Error-Codes/yaml/buddy-error-codes.yaml)
beim Tag 8.0.0. Am Core One L lesen Sie 37 statt 36.

| Code | Titel | Erscheint, wenn | Was zu tun ist |
|---|---|---|---|
| 36130 | Tool Offset Failed | ein Reinigungsablauf nicht abgeschlossen wurde, eine Berührung auf der Druckplatte verworfen wurde, die Düse zu heiß blieb oder keine Temperatur meldete, das Referenzieren fehlschlug oder die Abtastfahrten liefen, ohne die Düse zu finden | Das Log sagt, welcher; siehe [unten](#stock-firmware) |
| 36144 | Sensor Not Found | die Berührung auf der Sensorplatine verworfen wurde | [36193](#36193) |
| 36145 | Sensor Failure | die Kopfplatine während der Abtastfahrten neu startete oder die Abtastfahrten aufgaben, nachdem mindestens eine von ihnen an einem Fehler scheiterte, den der Sensor selbst gemeldet hat | [36195](#36195) oder [36194](#36194), auch wenn der Sensor nur bei einigen der Abtastfahrten einen Fehler gemeldet hat |
| 36146 | Tool Not Picked | das Werkzeug, das gereinigt oder vermessen werden soll, nicht dasjenige ist, das der Drucker als ausgewählt betrachtet | [36190](#36190) |

Der Text von 36130 fordert weiterhin eine saubere Düse und einen sauberen Sensor, obwohl
dieser Bildschirm unter 8.0.0 auch Fehler bei Reinigung, Abtasten der Druckplatte,
Temperatur und Referenzieren abdeckt. Der Text von 36145 macht den Sensor oder sein
Kabel verantwortlich, was zu einem Neustart der Kopfplatine nicht passt; das Log
unterscheidet die beiden.

Drei Punkte im Quellcode sind wissenswert, alle davon Lesarten und keine beobachteten
Ergebnisse:

- Eine fehlgeschlagene Abtastfahrt zählt nur dann gegen den Sensor, wenn der Sensor
  währenddessen einen Fehler gemeldet oder Werte verloren hat. Eine Abtastfahrt, die
  ohne eine solche Meldung beim Warten auf ihren ersten Wert in eine Zeitüberschreitung
  läuft oder zu wenige Werte für die Auswertung bekommt, zählt nicht. Ein Sensor, der
  gar nichts sendet, würde daher bei 36130 enden, nicht bei 36145
  ([Quellcode der Messung](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/lib/Marlin/Marlin/src/feature/contactless_offset/contactless_offset.cpp),
  [Sensoranbindung](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/src/module/contactless_offset/src/contactless_offset/can_remote_sensor.cpp)).
- Die Liste beschreibt 36144 so, dass der Sensor nicht in der erwarteten Höhe gefunden
  wird. Die Prüfung auf eine Berührung weit unterhalb der Sensoroberfläche gibt es nur
  im Zwei-Spulen-Pfad des XL, am INDX löst also allein die verworfene Berührung den Code
  aus.
- Unter 8.0.0 löst nur diese Kalibrierung 36146 aus. Es ist keine allgemeine Prüfung
  der Werkzeugaufnahme.

Kann der Drucker aus dem Kalibriermenü heraus vor Beginn der Kalibrierung überhaupt
kein Werkzeug aufnehmen, zeigt 8.0.0 36138 Tool pickup failed, einen Code, den der
Werkzeugwechsler auch außerhalb dieser Kalibrierung verwendet. Diese Seite behandelt
ihn nicht.

## 36130 · 37130 · Werkzeug-Offset fehlgeschlagen {#36130}

<span id="37130"></span>

*Die Standard-Firmware bis 7.0.1 zeigt hier 36130. Die Standard-Firmware 8.0.0 zeigt
ebenfalls 36130, es sei denn, eine der Abtastfahrten scheiterte an einem vom Sensor
gemeldeten Fehler; dann zeigt sie [36145](#stock-800).*

**Was fehlgeschlagen ist.** Die Abtastfahrten liefen, und der Sensor lieferte Daten,
aber keine Abtastfahrt fand die Düse mit ausreichender Konfidenz. Etwas stört die Sicht
des Sensors auf die Düsenspitze. Für diesen Fall wurde der Hinweis auf dem Bildschirm
geschrieben, und der QR-Code auf diesem Bildschirm führt weiterhin zu Prusas eigenem
Artikel.

**Was zu tun ist.**

1. Reinigen Sie die Düsenspitze, dann das Sensorfenster. Wie das Fenster gereinigt
   wird und was man dafür nicht verwenden sollte, steht unter
   [Nachsickern beim Abtasten](issues/oozing-during-probing-and-calibration.md).
2. Entladen Sie das Filament aus dem Werkzeug, damit während der Messung nichts
   nachsickert. [Prusas Artikel zu diesem Code](https://help.prusa3d.com/article/tool-offset-failed-36130-core-one-indx_1089016)
   gibt denselben Rat.
3. Prüfen Sie, ob die Sensorplatine flach und fest sitzt. Die Abtastfahrten
   durchsuchen nur einen begrenzten Bereich um die erwartete Sensorposition, sodass
   eine verrutschte Platine die Spule außerhalb dieses Bereichs liegen lassen kann.
   Das ist eine Lesart der Firmware, kein gemeldeter Fall.
4. Wenn es weiterhin fehlschlägt, gehen Sie zu
   [berührungsloser Offsetsensor](issues/offset-sensor-board-failure.md).

Mit der Standard-Firmware bis 7.0.1 kann 36130 jeder der Codes unten sein. Unter 8.0.0
kann es weiterhin 36191, 36192, 36196 oder 36197 sein, die Temperaturprüfung unter
36190 oder ein Fehler unter 36194, den der Sensor nicht selbst gemeldet hat.

## 36190 · 37190 · Werkzeug nicht aufgenommen {#36190}

<span id="37190"></span>

*Code des Forks. Die Standard-Firmware zeigt hier bis 7.0.1 36130. Die
Standard-Firmware 8.0.0 zeigt [36146](#stock-800), oder 36130, wenn die fehlschlagende
Prüfung die Düsentemperatur ist.*

**Was fehlgeschlagen ist.** Bevor ein Werkzeug gereinigt und vermessen wird, prüft die
Firmware, ob das gerade aufgenommene Werkzeug dasjenige ist, das sie als ausgewählt
betrachtet. Die Messung braucht außerdem die Düsentemperatur des Werkzeugs, die der
INDX-Kopf nur von einem aufgenommenen Werkzeug lesen kann. Eine dieser Prüfungen schlug
fehl: Der Werkzeugwechsel meldete Erfolg, aber der Drucker betrachtet das Werkzeug
nicht als aufgenommen.

**Was zu tun ist.**

1. Sehen Sie sich den Kopf an. Wenn das Werkzeug nicht daran ist oder nicht richtig
   sitzt, drücken Sie Abort, setzen Sie das Werkzeug zurück in sein Dock, nehmen Sie es
   mit Control > Pick/Park Tool auf und beginnen Sie erneut. Unter 8.0.0 nimmt Retry
   das Werkzeug erneut auf, sobald es wieder in seinem Dock steht.
2. Wenn das Werkzeug am Kopf ist und richtig sitzt, liest der Kopf es falsch. Siehe
   [Phantom-Werkzeuge und Parkfehler](issues/tool-detection-ringdown-decay.md).

## 36191 · 37191 · Düsenreinigung fehlgeschlagen {#36191}

<span id="37191"></span>

*Code des Forks. Die Standard-Firmware zeigt hier 36130, auch 8.0.0.*

**Was fehlgeschlagen ist.** Einer der Reinigungsabläufe vor der Messung wurde nicht
abgeschlossen: das Auswerfen des letzten Blobs, das Spülen und Abstreifen oder die
abschließende Reinigung bei der Abtasttemperatur. Die Firmware bricht einen Ablauf ab,
wenn seine Bewegung mittendrin gestoppt wird; der Bildschirm sagt nicht, was sie
gestoppt hat. Ein abgebrochener Druck zeigt diesen Bildschirm nie, und auch das
Kalibriermenü nicht, das nicht reinigt.

**Was zu tun ist.**

1. Prüfen Sie den Düsenreiniger und den Abfallbehälter auf alles, was den Kopf
   blockieren könnte: einen vollen Behälter oder ein Pellet oder einen Faden, der im
   Abstreifer hängt.
2. Drücken Sie Retry.
3. Wenn die Reinigung weiterhin fehlschlägt, siehe
   [Abstreifer, Spülen und Blobs](issues/stringing-and-wiper-calibration.md) dazu, wie
   der Reiniger kalibriert wird.

## 36192 · 37192 · Abtasten des Betts fehlgeschlagen {#36192}

<span id="37192"></span>

*Code des Forks. Die Standard-Firmware zeigt hier 36130, auch 8.0.0.*

**Was fehlgeschlagen ist.** Eine der Berührungen auf der Druckplatte wurde auch nach
den eigenen Wiederholungen der Abtastung nicht akzeptiert. Das passiert nur zu Beginn
eines Drucks, der mehr als ein Werkzeug verwendet.

**Was zu tun ist.**

1. Reinigen Sie die Düsenspitze und die Vorderkante der Druckplatte. Material an der
   Spitze ist der übliche Grund, warum eine Berührung verworfen wird, siehe
   [Nachsickern beim Abtasten](issues/oozing-during-probing-and-calibration.md).
2. Halten Sie die Tür geschlossen. Ist die Einstellung Door Sensor eingeschaltet,
   stoppt das Öffnen der Tür während des Abtastens die Bewegung, und die unterbrochene
   Berührung gilt als fehlgeschlagen.
3. Wenn Spitze und Druckplatte sauber sind, führen Sie Z Alignment Calibration aus.
   Ein klemmender Bettschlitten führt dazu, dass Berührungen auf dem Sensor verworfen
   werden, siehe [Bett in Z nicht ausgerichtet](issues/tool-offset-bed-z-alignment.md);
   eine Berührung auf der Druckplatte wird vermutlich auf dieselbe Weise verworfen,
   aber bisher hat das niemand gemeldet.
4. Wenn die Düse sichtbar vor der Druckplatte stehen bleibt, siehe
   [Wägezellen-Störungen](issues/loadcell-emi-noise.md) sowie die beiden
   Störquellen, die Besitzer für diese Kalibrierung gemeldet haben, unter
   [36193](#36193).

## 36193 · 37193 · Abtasten des Sensors fehlgeschlagen {#36193}

<span id="37193"></span>

*Code des Forks. Die Standard-Firmware zeigt hier bis 7.0.1 36130 und unter 8.0.0
[36144 Sensor Not Found](#stock-800).*

**Was fehlgeschlagen ist.** Die Berührung auf der Sensorplatine, die vor den
Abtastfahrten die Höhe der Sensoroberfläche findet, wurde auch nach den eigenen
Wiederholungen der Abtastung nicht akzeptiert.

**Was zu tun ist.**

1. Reinigen Sie die Düsenspitze und die Sensorplatine.
2. Halten Sie die Tür geschlossen, aus demselben Grund wie unter [36192](#36192).
3. Wenn beides sauber ist und nichts geladen ist, führen Sie Z Alignment Calibration
   aus. Das ist der Fehler, der unter
   [Bett in Z nicht ausgerichtet](issues/tool-offset-bed-z-alignment.md) beschrieben ist.
4. Wenn die Düse vor dem Sensor stehen bleibt oder dieser Schritt aus dem
   Kalibriermenü gelingt, beim Start eines Drucks aber scheitert, siehe
   [Wägezellen-Störungen](issues/loadcell-emi-noise.md). Besitzer haben für diese
   Kalibrierung zwei Störquellen gemeldet. Die eine ist der Extrudermotor. Ein Besitzer
   hat unter 7.0.0 diesen Fehler beim Druckstart protokolliert und bei bestromtem Motor
   deutlich mehr Störungen an der Wägezelle gemessen, allerdings nicht während der
   fehlgeschlagenen Berührung selbst, und festgestellt, dass das Abschalten seines
   Treibers vor dem Abtasten die Fehler selten machte, eine Umgehung, keine Behebung
   ([Firmware-Issue 5548](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5548)).
   Bei einem zweiten Besitzer in diesem Issue gelang das Abtasten mit derselben Änderung
   nach mehreren Fehlschlägen beim ersten Versuch; das ist ein einziger Versuch.
   Ein separater Bericht unter 6.9.1 führt Störungen im Selbsttest der Wägezelle nach
   einem Werkzeugwechsel darauf zurück, dass derselbe Motor eingeschaltet bleibt
   ([Firmware-Issue 5518](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5518)).
   Die andere ist die Statusleuchte am Bett, die laut einem Besitzer während eines
   Drucks leuchtet, bei einer Kalibrierung aus dem Menü aber nicht. Mit
   Standard-Firmware berichten ein Besitzer, der sie im Menü ausgeschaltet hat, und ein
   weiterer, der zusätzlich Ferritperlen angebracht hat, dass ihre Fehler aufhörten
   ([Firmware-Issue 5526](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5526),
   [Thread zur Werkzeug-Offset-Kalibrierung](https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/tool-offset-calibration-failing/)).
   Ein weiterer Besitzer in diesem Thread, der seine Firmware nicht nennt, berichtet,
   dass der erste Lauf nach dem Ausschalten weder langsam war noch fehlschlug, bei dieser
   Kalibrierung und bei der Bettnivellierung.
   Der erste von ihnen hat inzwischen in
   [Firmware-Issue 5518](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5518)
   zusammengefasst, was seinen Drucker vollständig in Ordnung gebracht hat: verdrillte
   Versorgungsleitungen im Kabelbaum des Kopfes, Ferritkerne an den Kabeln der Bett- und
   der Kammerbeleuchtung und eine niedrigere Abtasttemperatur im Start-G-Code. Das
   Ausschalten der Leuchte steht nicht auf dieser Liste, obwohl er das Kabel der
   Bettbeleuchtung für die wahrscheinlichste Quelle hält; sein Ergebnis zeigt also
   nicht, dass das Ausschalten nötig ist.
   Ein dritter stellte in Firmware-Issue 5526 fest, dass Ferritperlen nicht halfen und
   das Ausschalten der Leuchte bisher anscheinend jedes Mal hilft. Der Ersteller von
   Firmware-Issue 5548 hat inzwischen gesagt, dass sein Druckstart nun neben dem Motor
   auch die Leuchte ausschaltet und dass das bisher sehr zuverlässig ist
   ([Firmware-Issue 5518](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5518));
   dieses Ergebnis trennt die beiden Störquellen nicht.

## 36194 · 37194 · Keine Daten vom Offsetsensor {#36194}

<span id="37194"></span>

*Code des Forks. Die Standard-Firmware zeigt hier bis 7.0.1 36130. Die
Standard-Firmware 8.0.0 zeigt [36145 Sensor Failure](#stock-800), wenn eine
Abtastfahrt an einem vom Sensor gemeldeten Fehler scheiterte, und sonst 36130.*

**Was fehlgeschlagen ist.** Der Drucker zeichnet bei jeder Abtastfahrt die Werte des
Sensors auf, und eine Abtastfahrt zählt nur, wenn diese Aufzeichnung ausgewertet werden
kann: Der Sensor muss mit dem Senden beginnen, darf keinen Fehler melden, keine Werte
verlieren und muss genug davon liefern. Keine einzige Abtastfahrt der gesamten Suche
ergab eine auswertbare Aufzeichnung. Der Sensor, seine Platine oder seine Verbindung
zum Drucker liefert keine Daten.

Liefert der Sensor nur zeitweise Daten, zeigt der Drucker stattdessen 36130, sodass
eine Verbindung, die ab und zu aussetzt, trotzdem wie eine verschmutzte Düse aussehen
kann. Die Standard-Firmware 8.0.0 zieht die Grenze anders. Dort genügt eine einzige
Abtastfahrt, die an einem vom Sensor gemeldeten Fehler scheitert, für 36145, sobald die
Messung aufgibt, während ein Sensor, der gar nichts sendet und daher auch nichts
meldet, bei 36130 endet. Das ist eine Lesart des Quellcodes von 8.0.0.

**Was zu tun ist.** Das ist der Fehler unter
[berührungsloser Offsetsensor](issues/offset-sensor-board-failure.md): Prüfen Sie das
Kabel und seine Stecker, zeichnen Sie ein serielles Log auf und prüfen Sie die LED auf
der Sensorplatine. Das Log nennt den Grund, aus dem jede Abtastfahrt fehlschlug, siehe
[unten](#stock-firmware).

## 36195 · 37195 · Werkzeugkopfplatine neu gestartet {#36195}

<span id="37195"></span>

*Code des Forks. Die Standard-Firmware zeigt hier bis 7.0.1 36130 und unter 8.0.0
[36145 Sensor Failure](#stock-800).*

**Was fehlgeschlagen ist.** Während der Abtastfahrten überwacht die Firmware den
Neustartzähler der INDX-Kopfplatine. Eine Platine, die mitten in der Messung neu
startet, verdirbt jeden Messwert danach, daher wird die Messung abgebrochen.

**Was zu tun ist.**

1. Prüfen Sie, ob das Werkzeugkopfkabel an beiden Enden vollständig eingesteckt ist,
   und suchen Sie entlang seines Verlaufs nach Zug oder Beschädigung.
2. Drücken Sie Retry.
3. Wenn es erneut passiert, zeichnen Sie ein serielles Log auf und wenden Sie sich an
   den Support, siehe [an wen man sich wendet](issues/support-and-warranty-path.md).

## 36196 · 37196 · Düse zu heiß {#36196}

<span id="37196"></span>

*Code des Forks. Die Standard-Firmware zeigt hier 36130, auch 8.0.0.*

**Was fehlgeschlagen ist.** Die Abtastfahrten brauchen die Düse unter einer
Temperaturgrenze für das Abtasten, die in der Firmware festgelegt ist. Vor den
Abtastfahrten senkt der Drucker die Zieltemperatur der Düse und wartet, bis sie
abkühlt, wobei der Bauteillüfter hilft. Das Warten endet, wenn die Temperatur nicht
mehr sinkt, und hier endete es, während die Düse noch über der Grenze lag.

**Was zu tun ist.**

1. Prüfen Sie, ob sich der Bauteillüfter dreht.
2. Lassen Sie die Düse abkühlen und drücken Sie dann Retry.

## 36197 · 37197 · Referenzieren fehlgeschlagen {#36197}

<span id="37197"></span>

*Code des Forks. Die Standard-Firmware zeigt hier 36130, auch 8.0.0, sofern
überhaupt ein Bildschirm erscheint.*

**Was fehlgeschlagen ist.** Jede Messung beginnt damit, jede Achse zu referenzieren,
die es braucht, und das Referenzieren schlug fehl. Ein fehlgeschlagenes Referenzieren
stoppt den Drucker normalerweise zuerst mit seinem eigenen Referenzierfehler. Während
eines Drucks kann stattdessen die Crash-Wiederherstellung einen Referenzierfehler
übernehmen, und so kann dieser Bildschirm erscheinen.

**Was zu tun ist.** Prüfen Sie, dass nichts das Bett oder den Kopf blockiert, und
drücken Sie dann Retry. Schlägt das Referenzieren weiterhin fehl, folgen Sie Prusas
Artikel für die Achse: denen, auf die die eigenen Referenzierfehler-Bildschirme des
Druckers verweisen, für [Z](https://prusa.io/36301), [X](https://prusa.io/36304)
und [Y](https://prusa.io/36305).

## Unterscheidung mit der Standard-Firmware {#stock-firmware}

Die Standard-Firmware bis 7.0.1 zeigt für all diese Fehler 36130, und der Fork tut das
ebenso auf anderen Druckern als dem INDX. Die Standard-Firmware 8.0.0 zeigt einen von
[vier Codes](#stock-800). In beiden Fällen sagt das serielle Log, welcher Fehler es war:
die Zeile, die kurz vor dem Erscheinen des Dialogs protokolliert wird. Wie Sie das Log
aufzeichnen, steht unter
[berührungsloser Offsetsensor](issues/offset-sensor-board-failure.md).

### 6.9.x bis 7.0.1

Diese Zeilen stammen aus dem Quellcode von 6.9.1 und sind bis 7.0.1 unverändert
([Vergleich](https://github.com/prusa3d/Prusa-Firmware-Buddy/compare/v6.9.2...v7.0.1)).
Der Fork schreibt sie ebenfalls.

| Das Log sagt | Code des Forks |
|---|---|
| `is not the selected tool, cannot clean` | [36190](#36190) |
| `Measurement failed: Nozzle has no valid temperature` | [36190](#36190) |
| `cleaning failed (step` oder `Nozzle cleaning failed`, ohne eine Zeile zum ausgewählten Werkzeug davor | [36191](#36191) |
| `Z probe failed for tool` oder `Z probe failed at reference-line end` | [36192](#36192) |
| `Measurement failed: Initial probing failed, sensor Z is NaN` | [36193](#36193) |
| `INDX puppy reset during XY scan; aborting FSM` | [36195](#36195) |
| `Measurement failed: Nozzle too hot for probing` | [36196](#36196) |
| `Measurement failed: Homing failed` | [36197](#36197) |
| `Measurement failed: Tool offset FSM finished without high confidence in both axes` oder `exceeded iteration limit` | [36130](#36130), oder [36194](#36194), wenn jede Abtastfahrt davor fehlschlug |

Eine fehlgeschlagene Abtastfahrt protokolliert `scan 'nozzle-offset-x' failed:` oder
`scan 'nozzle-offset-y' failed:`, gefolgt vom Grund. Die Gründe, die bedeuten, dass der
Sensor nichts Brauchbares geliefert hat, sind `Failed to get first sensor sample`,
`Sensor reported hardware failure`, `Sensor samples overflow` und
`Insufficient samples for analysis`. Mit dem Fork lautet die letzte Zeile, wenn
jede Abtastfahrt so fehlschlug, stattdessen
`Measurement failed: Tool offset FSM got no analyzable sensor data`.

### 8.0.0

Unter 8.0.0 protokolliert die Messung ihren Grund ohne das Präfix `Measurement failed:`,
und die Kalibrierung ergänzt danach `XY offset measurement failed for tool`. Auf einen
Fehler vor der Messung folgt `could not be prepared`
([Vergleich](https://github.com/prusa3d/Prusa-Firmware-Buddy/compare/v6.9.2...v8.0.0)).

| Das Log sagt | Die Standard-Firmware 8.0.0 zeigt | Abschnitt |
|---|---|---|
| `is not the selected tool, cannot clean`, `failed: no tool selected` oder `Selected tool must be picked` | 36146 | [36190](#36190) |
| `Nozzle has no valid temperature` | 36130 | [36190](#36190) |
| `could not be prepared (step`, ohne eine Zeile zum ausgewählten Werkzeug davor | 36130 | [36191](#36191) |
| `Z probe failed for tool` oder `Z probe failed at reference-line end` | 36130 | [36192](#36192) |
| `Initial probing failed, sensor Z is NaN` | 36144 | [36193](#36193) |
| `INDX puppy reset during XY scan; aborting FSM`, danach `Tool offset FSM aborted: hardware failure` | 36145 | [36195](#36195) |
| `Nozzle too hot for probing` | 36130 | [36196](#36196) |
| `Homing failed` | Stammt die Zeile von `ContactlessOffset`, 36130, sofern überhaupt ein Bildschirm erscheint; stammt sie zu Beginn von `ToolOffsetCalib`, erscheint kein Kalibrierbildschirm | [36197](#36197) |
| `Tool offset FSM finished without high confidence in both axes` oder `Tool offset FSM exceeded iteration limit` | 36145, wenn der Sensor bei einer Abtastfahrt davor einen Fehler gemeldet hat (meist protokolliert als `Sensor reported hardware failure` oder `Sensor sample overflow`), sonst 36130 | [36194](#36194) oder [36130](#36130) |

Jede Log-Zeile nennt den Teil der Firmware, der sie geschrieben hat; daran
unterscheiden sich die beiden Zeilen `Homing failed`.
Die Zeilen zu den Abtastfahrten sind wie zuvor. `Failed to get first sensor sample`
zählt nur dann für 36145, wenn der Sensor zusätzlich einen Fehler gemeldet hatte, was das
Log in dieser Zeile nicht zeigt. Nach einer Vergleichsprüfung folgt auf
`Z offset spread too large` oder `XY offset spread too large` die Zeile
`Biggest outlier on` mit dem Werkzeug, wenn drei oder mehr Werkzeuge vermessen wurden.

## Überprüfung

`provisional`. Was jeder Code bedeutet, ist aus dem Quellcode der Firmware gelesen:
Jeder Abschnitt nennt eine Prüfung, die die Firmware vornimmt, und den Code, den der
Fork zeigt, wenn diese Prüfung fehlschlägt, und die Log-Zeilen stammen aus dem
Standard-Quellcode beim Tag 6.9.1. Ein Vergleich der Tags 6.9.2 und 7.0.1 ergibt
dieselbe Fehlerbehandlung und dieselben Log-Zeilen. Was die Standard-Firmware 8.0.0
zeigt und was sie protokolliert, ist aus dem Quellcode beim Tag 8.0.0 gelesen. Noch kein
Besitzer hat einen Fehlerbildschirm von 8.0.0 gemeldet, daher ist nichts davon an einem
Drucker beobachtet worden. All das ist nur so verlässlich wie die Lesart des Quellcodes,
der oben verlinkt ist. Codes und Titel der Vergleichsprüfungen stammen aus der
[Fehlercode-Liste](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/lib/Prusa-Error-Codes/yaml/buddy-error-codes.yaml)
der Standard-Firmware beim Tag 6.9.1 und sind beim Tag 8.0.0 dieselben. Die Meldung
eines sauberen Werkzeugs am Kopf stammt von einem einzelnen Besitzer. Zwei weitere
Besitzer haben inzwischen im selben Issue gesagt, dass sie dasselbe sehen, ohne zu
sagen, welchen Teil, und der Hersteller hat nicht geantwortet. Die Anzahl der Versuche
stammt aus den Versionshinweisen zu 6.9.1-beta, und für welche Berührung sie gilt, ist
aus dem Quellcode beim Tag 6.9.1 gelesen.
Von den beiden Störquellen unter 36193 stützt sich
der Extrudermotor für diese Kalibrierung auf die Messungen eines Besitzers und den
einzelnen Versuch eines zweiten, beide in Firmware-Issue 5548. Der erste von ihnen
schaltet inzwischen auch die Statusleuchte aus, sodass sein neuestes Ergebnis, das er
bisher sehr zuverlässig nennt, den Motor nicht isoliert. Unabhängig davon meldet
Firmware-Issue 5518, dass derselbe Motor den Selbsttest der Wägezelle stört; dessen
Ersteller vermutet einen Zusammenhang mit Fehlern beim Druckstart, hat ihn aber nicht
nachgewiesen. Die Statusleuchte stützt sich auf zwei Besitzer mit Standard-Firmware, in
Firmware-Issue 5526 und in einem Forenthread, die berichten, dass das Ausschalten der
Leuchte, allein oder zusammen mit Ferritperlen, ihre Fehler beendet hat, und auf einen
dritten im Issue, der seine Firmware nicht nennt und bei dem Ferritperlen allein nicht
halfen. Der erste dieser beiden führt seine vollständige Behebung inzwischen in
Firmware-Issue 5518 auf das Neuverlegen der Kabel, Ferritkerne an den Kabeln der
Beleuchtung und eine niedrigere Abtasttemperatur zurück, ohne das Ausschalten der
Leuchte aufzuführen, obwohl er das Kabel der Bettbeleuchtung für die wahrscheinlichste
Quelle hält; sein Ergebnis zeigt also nicht, dass das Ausschalten nötig ist. Ein
weiterer Besitzer im selben Forenthread berichtet von einem guten Lauf nach dem
Ausschalten, ohne seine Firmware zu nennen; da er im selben Thread schreibt, zählt sein
Bericht nicht als weitere Quelle für die Stufe dieser Seite.
Der Ersteller von Firmware-Issue 5526 hat die
Leuchte auf einer selbst veränderten Firmware getestet, auf die sich diese Seite nicht
stützt.

Was bei jedem Code zu tun ist, ist die Lesart dieser Prüfungen durch den Autor. Wo ein
Abschnitt Sie auf eine andere Seite schickt, gilt deren eigene Stufe. Der Rest wurde
nicht an Hardware getestet, und noch kein Besitzer hat die Codes des Forks oder die
neuen Bildschirme von 8.0.0 gemeldet. Wenn Sie einer dieser Bildschirme zu einer Lösung
geführt hat oder ein Schritt hier nichts bewirkt hat, ist genau diese Meldung das, was
diese Seite eine Stufe höher bringt. Siehe [Mitwirken](contributing.md).

Die Codes des Forks gibt es nur in Firmware, die aus dem Fork gebaut ist. Den
fehlgeschlagenen Schritt zu melden statt eines einzigen allgemeinen Dialogs wurde
upstream in [Firmware-Issue 5482](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5482)
vorgeschlagen. Ein Prusa-Entwickler antwortete am 23. September 2026, dass der Hersteller
bereits daran arbeite, ohne Liefertermin. Die Meldung des fehlgeschlagenen Schritts ist in
[6.9.2](https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.9.2),
erschienen am 7. Oktober 2026, nicht enthalten; diese Version
[ändert am INDX nur](https://github.com/prusa3d/Prusa-Firmware-Buddy/compare/v6.9.1...v6.9.2)
die Filament-Presets: Die Standard-Firmware 6.9.2 zeigt für jeden Fehler auf dieser
Seite weiterhin 36130 und schreibt dieselben Log-Zeilen wie 6.9.1.
[7.0.0](https://help.prusa3d.com/downloads/core-one-indx), am 15. Oktober 2026 auf
Prusas Download-Seite veröffentlicht, führt die Meldung des fehlgeschlagenen Schritts
ebenfalls nicht auf: Ihre Versionshinweise sagen nichts zu Fehlern der
Werkzeug-Offset-Kalibrierung, und ebenso wenig die
[ausführlichen Versionshinweise](https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v7.0.0),
die mit ihrem Quellcode erschienen sind. Auch 7.0.1, veröffentlicht am 19. Oktober 2026
mit einer einzigen Behebung für ein Hängenbleiben beim Start, führt sie nicht auf
([Versionshinweise](https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v7.0.1)).
Ihr Quellcode, öffentlich seit dem 3. November 2026, leitet weiterhin jeden Fehler auf
dieser Seite an die eine Warnung 36130 und schreibt dieselben Log-Zeilen wie 6.9.2
([Vergleich](https://github.com/prusa3d/Prusa-Firmware-Buddy/compare/v6.9.2...v7.0.1)).
Das passt zum Bericht eines Besitzers unter 7.0.0, der den Bildschirm 36130 zusammen mit
der Log-Zeile meldet, die diese Seite 36193 zuordnet
([Firmware-Issue 5548](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5548)).

Auch 8.0.0, am 22. Oktober 2026 auf der Download-Seite veröffentlicht, schien die
Meldung zunächst nicht zu enthalten. Weder die Download-Seite noch die
[Ankündigung im Forum](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/8-0-0-firmware-for-prusa-core-one-gen-2-indx-core-one-indx/)
des Herstellers erwähnt sie, und beide beschreiben nur die allgemeine Änderung an den
Fehlerbildschirmen, die den Hash des Druckers und die Signaturmarkierungen entfernt und
den QR-Code vereinfacht. Die
[Versionshinweise auf GitHub](https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v8.0.0),
die am 3. November 2026 mit dem Quellcode erschienen sind, führen sie auf, gekennzeichnet
für den INDX und den XL+: Ein fehlgeschlagenes Werkzeug wird nun allein erneut vermessen,
statt die ganze Kalibrierung neu zu beginnen, und jeder Fehler erhält einen eigenen
Bildschirm mit einem Code und dem betroffenen Werkzeug. Der Quellcode bestätigt das, mit
den Einschränkungen unter [was die Standard-Firmware 8.0.0 zeigt](#stock-800) und im
Absatz davor dazu, welches Werkzeug der Bildschirm nennt. Die Änderung ist in keinem der
früheren Tags enthalten: 7.0.1 hat noch für keinen einzelnen Fehler einen eigenen
Bildschirm. Firmware-Issue 5482 ist weiterhin offen, und kein Commit verweist darauf,
aber einige der Commits in 8.0.0, die die Änderung vornehmen, wenn auch nicht alle,
tragen die interne Referenz, die der Entwickler dort genannt hat
([Vergleich](https://github.com/prusa3d/Prusa-Firmware-Buddy/compare/v6.9.2...v8.0.0)).
Die Aufteilung der Standard-Firmware 8.0.0 ist nicht die des Forks. Sie hat drei neue
Codes, wo der Fork acht hat, und belässt Fehler bei Reinigung, Abtasten der
Druckplatte, Temperatur und Referenzieren bei 36130.

Prusas eigene Codes für einige dieser Fehler standen bereits in seiner öffentlichen
[Fehlercode-Liste](https://github.com/prusa3d/Prusa-Error-Codes/blob/9e609385d1c18cc080bcfaaf2bd1d6a7cd7cf5ad/yaml/buddy-error-codes.yaml).
Zwei wurden am 21. September 2026 hinzugefügt
([Commit](https://github.com/prusa3d/Prusa-Error-Codes/commit/a88544c7628067f03c768a26624000c463e971b6))
und am 2. Oktober als freigegeben markiert
([Commit](https://github.com/prusa3d/Prusa-Error-Codes/commit/8a502d03acc0c5bf3ba524d68c6e10bd4c8d1acf)):
36144 Sensor Not Found, wenn der Offsetsensor nicht in der Höhe gefunden wird, in der
der Drucker ihn erwartet, und 36145 Sensor Failure, wenn der Sensor während der Messung
verstummt. Ein dritter, 36146 Tool Not Picked, folgte am 5. Oktober
([Commit](https://github.com/prusa3d/Prusa-Error-Codes/commit/bc278daf0a10e6657048416623a9e2e7f7845643))
und ist noch nicht als freigegeben markiert. Sein Commit beschreibt ihn als Meldung
einer fehlgeschlagenen Werkzeugaufnahme, bei der die Motoren eingeschaltet bleiben; er
ist also möglicherweise eine allgemeine Prüfung der Werkzeugaufnahme und nicht
spezifisch für diese Kalibrierung. Alle drei wurden hinzugefügt, bevor 6.9.2 am 7.
Oktober erschien, und 6.9.2 zeigt sie nicht an. Am Core One L lauten sie 37144, 37145
und 37146. Die Änderung vom September formuliert außerdem 36134 Unsafe Sensor Position
um: Statt zum Reinigen von Düse und Sensor aufzufordern, sagt der Text nun, der Sensor
sei möglicherweise aus seiner Lage gestoßen worden. Allein nach ihren Beschreibungen
schien 36144 am nächsten bei 36193 auf dieser Seite zu liegen, 36145 bei 36194 und 36146
bei 36190, wobei sich erst nach der Veröffentlichung des Quellcodes lesen ließ, welche
Prüfungen sie auslösen. Der Quellcode von 8.0.0 klärt das, unter
[was die Standard-Firmware 8.0.0 zeigt](#stock-800): 36144 ist der Fehler unter 36193,
36145 deckt 36195 und Teile von 36194 und 36130 ab, und 36146 ist 36190 ohne dessen
Temperaturprüfung. 36146 wird nur von dieser Kalibrierung ausgelöst und ist also nicht
die allgemeine Prüfung der Werkzeugaufnahme, die seine Commit-Beschreibung nahelegte.
Die Liste beim Tag 8.0.0 markiert ihn weiterhin als nicht freigegeben, eine Markierung,
die das README der Liste selbst als eigentlich nutzlos beschreibt, und 8.0.0 löst ihn
trotzdem aus. Die Liste beim Tag 7.0.0 enthält bereits 36144, 36145 und den neu
formulierten Text von 36134, aber nichts in 7.0.0 oder 7.0.1 löst die ersten beiden
aus. Die Versionshinweise zu 8.0.0 beschreiben die neuen Bildschirme, ohne ihre Codes
zu nennen.

## Verwandt

- [Berührungsloser Offsetsensor](issues/offset-sensor-board-failure.md): 36194 (36145
  mit der Standard-Firmware 8.0.0), und 36130, wenn Reinigen nicht geholfen hat
- [Bett in Z nicht ausgerichtet](issues/tool-offset-bed-z-alignment.md): 36193 (36144
  mit der Standard-Firmware 8.0.0), und möglicherweise 36192
- [Nachsickern beim Abtasten](issues/oozing-during-probing-and-calibration.md): 36130,
  36192 und 36193
- [Phantom-Werkzeuge und Parkfehler](issues/tool-detection-ringdown-decay.md): 36190
  (36146 mit der Standard-Firmware 8.0.0)
- [Abstreifer, Spülen und Blobs](issues/stringing-and-wiper-calibration.md): 36191
- [Wägezellen-Störungen](issues/loadcell-emi-noise.md): 36192 und 36193
- [An wen man sich wendet](issues/support-and-warranty-path.md): 36194 und 36195 (36145
  mit der Standard-Firmware 8.0.0)
