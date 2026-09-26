---
title:        Fehlercodes der Werkzeug-Offset-Kalibrierung
confidence:   provisional
updated:      2026-09-25
author:       hyiger
printer:      Core One, Core One L
toolhead:     INDX
hotend:       unknown
nozzle:       unknown
firmware:     stock firmware reports all of these as 36130; the 3619x codes need firmware built from hyiger/Prusa-Firmware-Buddy
sources:
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/src/feature/tool_offset_calibration/tool_offset_calibration.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/lib/Marlin/Marlin/src/feature/contactless_offset/contactless_offset.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5482
  - https://github.com/hyiger/Prusa-Firmware-Buddy/blob/master/lib/Prusa-Error-Codes/yaml/buddy-error-codes.yaml
  - https://help.prusa3d.com/article/tool-offset-failed-36130-core-one-indx_1089016
superseded_by:
source_sha:   21eec362b8180f1855d7e8b71adb7d2a4b70ac98096f0877d8c00d7e3d2494b9
---
# Fehlercodes der Werkzeug-Offset-Kalibrierung

## Zusammenfassung

Die Standard-Firmware zeigt für elf verschiedene Arten, auf die die
Werkzeug-Offset-Kalibrierung fehlschlagen kann, ein und denselben Bildschirm, 36130,
und dieser Bildschirm fordert Sie immer auf, Düse und Sensor zu reinigen. Firmware, die
aus [hyiger/Prusa-Firmware-Buddy](https://github.com/hyiger/Prusa-Firmware-Buddy)
gebaut ist, teilt diese elf auf neun Bildschirme auf. 36130 behält den einen Fehler,
zu dem seine Meldung passt, nämlich dass die Abtastfahrten über den Sensor die Düse
nicht finden, und 36190 bis 36197 benennen den Rest. Der QR-Code auf jedem dieser
Bildschirme öffnet den zugehörigen Abschnitt auf dieser Seite.

Mit der Standard-Firmware sehen Sie immer nur 36130, aber das
[serielle Log](#stock-firmware) sagt trotzdem, welcher dieser Fehler es war.

Am Core One L beginnen die Codes mit 35 statt mit 36: 35130 und 35190 bis 35197.
Jeder Abschnitt unten gilt für beide.

| Code | Der Bildschirm beginnt mit | Was fehlgeschlagen ist |
|---|---|---|
| [36130](#36130) | Tool offset calibration failed | Die Abtastfahrten liefen, fanden die Düse aber nicht |
| [36190](#36190) | The tool is not detected as picked | Der Drucker betrachtet das Werkzeug nicht als aufgenommen |
| [36191](#36191) | Nozzle cleaning before tool offset calibration failed | Ein Reinigungsablauf wurde nicht abgeschlossen |
| [36192](#36192) | Probing the bed for tool offset calibration failed | Eine Berührung auf der Druckplatte wurde verworfen |
| [36193](#36193) | Probing the tool offset sensor failed | Die Berührung auf der Sensorplatine wurde verworfen |
| [36194](#36194) | The tool offset sensor sent no usable data | Keine Abtastfahrt lieferte auswertbare Sensordaten |
| [36195](#36195) | The toolhead board restarted | Die Platine des INDX-Kopfs startete während der Abtastfahrten neu |
| [36196](#36196) | The nozzle did not cool down enough | Die Düse blieb über der Temperaturgrenze für das Abtasten |
| [36197](#36197) | Homing failed during tool offset calibration | Das Referenzieren vor der Messung schlug fehl |

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

Retry nach einer fehlgeschlagenen Messung über dem Sensor reinigt das Werkzeug erneut
und misst es noch einmal. Retry auf den anderen Bildschirmen beginnt wieder beim ersten
Werkzeug. Abort bricht den Druck ab oder beendet die Kalibrierung aus dem Menü.

## 36130 · 35130 · Werkzeug-Offset fehlgeschlagen {#36130}

<span id="35130"></span>

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

Mit der Standard-Firmware kann 36130 jeder der Codes unten sein.

## 36190 · 35190 · Werkzeug nicht aufgenommen {#36190}

<span id="35190"></span>

**Was fehlgeschlagen ist.** Bevor ein Werkzeug gereinigt und vermessen wird, prüft die
Firmware, ob das gerade aufgenommene Werkzeug dasjenige ist, das sie als ausgewählt
betrachtet. Die Messung braucht außerdem die Düsentemperatur des Werkzeugs, die der
INDX-Kopf nur von einem aufgenommenen Werkzeug lesen kann. Eine dieser Prüfungen schlug
fehl: Der Werkzeugwechsel meldete Erfolg, aber der Drucker betrachtet das Werkzeug
nicht als aufgenommen.

**Was zu tun ist.**

1. Sehen Sie sich den Kopf an. Wenn das Werkzeug nicht daran ist oder nicht richtig
   sitzt, drücken Sie Abort, setzen Sie das Werkzeug zurück in sein Dock, nehmen Sie es
   mit Control > Pick/Park Tool auf und beginnen Sie erneut.
2. Wenn das Werkzeug am Kopf ist und richtig sitzt, liest der Kopf es falsch. Siehe
   [Phantom-Werkzeuge und Parkfehler](issues/tool-detection-ringdown-decay.md).

## 36191 · 35191 · Düsenreinigung fehlgeschlagen {#36191}

<span id="35191"></span>

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

## 36192 · 35192 · Abtasten des Betts fehlgeschlagen {#36192}

<span id="35192"></span>

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
   [Wägezellen-Störungen](issues/loadcell-emi-noise.md).

## 36193 · 35193 · Abtasten des Sensors fehlgeschlagen {#36193}

<span id="35193"></span>

**Was fehlgeschlagen ist.** Die Berührung auf der Sensorplatine, die vor den
Abtastfahrten die Höhe der Sensoroberfläche findet, wurde auch nach den eigenen
Wiederholungen der Abtastung nicht akzeptiert.

**Was zu tun ist.**

1. Reinigen Sie die Düsenspitze und die Sensorplatine.
2. Halten Sie die Tür geschlossen, aus demselben Grund wie unter [36192](#36192).
3. Wenn beides sauber ist und nichts geladen ist, führen Sie Z Alignment Calibration
   aus. Das ist der Fehler, der unter
   [Bett in Z nicht ausgerichtet](issues/tool-offset-bed-z-alignment.md) beschrieben ist.
4. Wenn die Düse vor dem Sensor stehen bleibt, siehe
   [Wägezellen-Störungen](issues/loadcell-emi-noise.md).

## 36194 · 35194 · Keine Daten vom Offsetsensor {#36194}

<span id="35194"></span>

**Was fehlgeschlagen ist.** Der Drucker zeichnet bei jeder Abtastfahrt die Werte des
Sensors auf, und eine Abtastfahrt zählt nur, wenn diese Aufzeichnung ausgewertet werden
kann: Der Sensor muss mit dem Senden beginnen, darf keinen Fehler melden, keine Werte
verlieren und muss genug davon liefern. Keine einzige Abtastfahrt der gesamten Suche
ergab eine auswertbare Aufzeichnung. Der Sensor, seine Platine oder seine Verbindung
zum Drucker liefert keine Daten.

Liefert der Sensor nur zeitweise Daten, zeigt der Drucker stattdessen 36130, sodass
eine Verbindung, die ab und zu aussetzt, trotzdem wie eine verschmutzte Düse aussehen
kann.

**Was zu tun ist.** Das ist der Fehler unter
[berührungsloser Offsetsensor](issues/offset-sensor-board-failure.md): Prüfen Sie das
Kabel und seine Stecker, zeichnen Sie ein serielles Log auf und prüfen Sie die LED auf
der Sensorplatine. Das Log nennt den Grund, aus dem jede Abtastfahrt fehlschlug, siehe
[unten](#stock-firmware).

## 36195 · 35195 · Werkzeugkopfplatine neu gestartet {#36195}

<span id="35195"></span>

**Was fehlgeschlagen ist.** Während der Abtastfahrten überwacht die Firmware den
Neustartzähler der INDX-Kopfplatine. Eine Platine, die mitten in der Messung neu
startet, verdirbt jeden Messwert danach, daher wird die Messung abgebrochen.

**Was zu tun ist.**

1. Prüfen Sie, ob das Werkzeugkopfkabel an beiden Enden vollständig eingesteckt ist,
   und suchen Sie entlang seines Verlaufs nach Zug oder Beschädigung.
2. Drücken Sie Retry.
3. Wenn es erneut passiert, zeichnen Sie ein serielles Log auf und wenden Sie sich an
   den Support, siehe [an wen man sich wendet](issues/support-and-warranty-path.md).

## 36196 · 35196 · Düse zu heiß {#36196}

<span id="35196"></span>

**Was fehlgeschlagen ist.** Die Abtastfahrten brauchen die Düse unter einer
Temperaturgrenze für das Abtasten, die in der Firmware festgelegt ist. Vor den
Abtastfahrten senkt der Drucker die Zieltemperatur der Düse und wartet, bis sie
abkühlt, wobei der Bauteillüfter hilft. Das Warten endet, wenn die Temperatur nicht
mehr sinkt, und hier endete es, während die Düse noch über der Grenze lag.

**Was zu tun ist.**

1. Prüfen Sie, ob sich der Bauteillüfter dreht.
2. Lassen Sie die Düse abkühlen und drücken Sie dann Retry.

## 36197 · 35197 · Referenzieren fehlgeschlagen {#36197}

<span id="35197"></span>

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

Die Standard-Firmware zeigt für all diese Fehler 36130, und diese Firmware tut das
ebenso auf anderen Druckern als dem INDX. Das serielle Log sagt, welcher es war: die
Zeile, die kurz vor dem Erscheinen des Dialogs protokolliert wird. Wie Sie das Log
aufzeichnen, steht unter
[berührungsloser Offsetsensor](issues/offset-sensor-board-failure.md).

| Das Log sagt | Code mit dieser Firmware |
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
`Insufficient samples for analysis`. Mit dieser Firmware lautet die letzte Zeile, wenn
jede Abtastfahrt so fehlschlug, stattdessen
`Measurement failed: Tool offset FSM got no analyzable sensor data`.

## Überprüfung

`provisional`. Was jeder Code bedeutet, ist aus dem Quellcode der Firmware gelesen:
Jeder Abschnitt nennt eine Prüfung, die die Firmware vornimmt, und den Code, den diese
Firmware zeigt, wenn diese Prüfung fehlschlägt, und die Log-Zeilen stammen aus dem
Standard-Quellcode beim Tag 6.9.1. Dieser Teil ist nur so verlässlich wie die Lesart
des Quellcodes, der oben verlinkt ist.

Was bei jedem Code zu tun ist, ist die Lesart dieser Prüfungen durch den Autor. Wo ein
Abschnitt Sie auf eine andere Seite schickt, gilt deren eigene Stufe. Der Rest wurde
nicht an Hardware getestet, und noch kein Besitzer hat die aufgeteilten Codes gemeldet.
Wenn Sie einer dieser Bildschirme zu einer Lösung geführt hat oder ein Schritt hier
nichts bewirkt hat, ist genau diese Meldung das, was diese Seite eine Stufe höher
bringt. Siehe [Mitwirken](contributing.md).

Die aufgeteilten Codes gibt es nur in Firmware, die aus dem Fork gebaut ist. Den
fehlgeschlagenen Schritt zu melden statt eines einzigen allgemeinen Dialogs wurde
upstream in [Firmware-Issue 5482](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5482)
vorgeschlagen. Ein Prusa-Entwickler antwortete am 23. September 2026, dass der Hersteller
bereits daran arbeite, ohne Liefertermin. Was die Standard-Firmware am Ende anzeigt, muss
nicht den Codes auf dieser Seite entsprechen.

## Verwandt

- [Berührungsloser Offsetsensor](issues/offset-sensor-board-failure.md): 36194, und
  36130, wenn Reinigen nicht geholfen hat
- [Bett in Z nicht ausgerichtet](issues/tool-offset-bed-z-alignment.md): 36193, und
  möglicherweise 36192
- [Nachsickern beim Abtasten](issues/oozing-during-probing-and-calibration.md): 36130,
  36192 und 36193
- [Phantom-Werkzeuge und Parkfehler](issues/tool-detection-ringdown-decay.md): 36190
- [Abstreifer, Spülen und Blobs](issues/stringing-and-wiper-calibration.md): 36191
- [Wägezellen-Störungen](issues/loadcell-emi-noise.md): 36192 und 36193
- [An wen man sich wendet](issues/support-and-warranty-path.md): 36194 und 36195
