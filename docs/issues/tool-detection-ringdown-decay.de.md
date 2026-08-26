---
title:        Phantom-Werkzeuge, „Werkzeug nicht erkannt“ und Park-Fehler
confidence:   reported
updated:      2026-08-25
author:       hyiger
printer:      Core One
toolhead:     INDX
hotend:       unknown
nozzle:       unknown
firmware:     6.6.3, 6.9.0
sources:
  - https://help.prusa3d.com/article/tool-park-failed-36127-core-one-indx_1073624
  - https://help.prusa3d.com/downloads/core-one-indx
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5392
  - https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/6-9-0-firmware-tool-docking/
  - https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/a-summary-of-common-indx-problems/
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/will-the-prusa-indxs-wave1-ship-with-fixed-induction-coils/
superseded_by:
source_sha:   2001ea301d2a33dd066696784f3376fe28770209bc23e5f7e6990738c4cbef9c
---
# Phantom-Werkzeuge, „Werkzeug nicht erkannt“ und Park-Fehler

## Zusammenfassung

Der INDX entscheidet über die Anwesenheit eines Werkzeugs, indem er eine Induktionsspule
im Kopf anregt und misst, wie das Nachschwingen abklingt — die Firmware nennt diesen Wert
*ringdown decay*. In der Mitte der Skala gibt es ein Band, in dem die Messung mehrdeutig
ist, und in diesem Band behält die Firmware bei, was sie zuletzt angenommen hat. Dieses
eine Konstruktionsdetail erklärt den größten Teil des verwirrenden Verhaltens in dieser
Fehlerfamilie: warum ein falscher Werkzeugstatus bestehen bleibt, warum er einen erneuten
Versuch übersteht und warum zwei Maschinen mit gegensätzlichen Symptomen dieselbe
zugrunde liegende Ursache haben können.

## Fehlercodes, die hierher führen

| Code | Anzeige am Drucker |
|---|---|
| [`36125`](https://help.prusa3d.com/article/tool-pickup-failed-36125-core-one-indx_1083573) | Werkzeugaufnahme fehlgeschlagen |
| [`36127`](https://help.prusa3d.com/article/tool-park-failed-36127-core-one-indx_1073624) | Werkzeugparken fehlgeschlagen |
| [`36128`](https://help.prusa3d.com/article/retry-tool-park-36128-core-one-indx_1072357) | Werkzeugparken wiederholen |
| [`36124`](https://help.prusa3d.com/article/tool-lost-36124-core-one-indx_1072958) | Werkzeug verloren |
| [`36123`](https://help.prusa3d.com/article/occupied-dock-36123-core-one-indx_1072788) | Dock belegt |
| [`36202`](https://help.prusa3d.com/article/hotend-preheat-error-36202-core-one-indx_1088818) | Hotend-Vorheizfehler |
| [`36135`](https://help.prusa3d.com/article/toolchanger-error-17135-xl-36135-core-one-indx_399944) | Werkzeugwechsler-Fehler |

Erkennungsfehler äußern sich als einer dieser Codes. `36125` und `36127` sind die beiden
Hälften des auf dieser Seite beschriebenen Problems — ein Werkzeug, das sich nicht als
aufgenommen lesen lässt, und eines, das sich nicht als geparkt lesen lässt. `36128` ist
der Wiederholversuch, der meist gelingt.

## Details

Messungen führen zu einer von drei Schlussfolgerungen: eindeutig kein Werkzeug, eindeutig
ein Werkzeug oder mehrdeutig. Im mehrdeutigen Mittelbereich hält die Firmware den zuletzt
bekannten Zustand, statt zu raten. Das ist ein sinnvoller Entwurf, bedeutet aber, dass
eine Maschine, deren Messwerte in oder nahe diesem mittleren Band liegen, *hartnäckig*
falsche Antworten bekommt statt sprunghafter.

### Den Wert an der eigenen Maschine ablesen

Der Live-Wert steht am Drucker unter **Info → Sensor Info → Ringdown Decay**.

Zwei Besitzer haben Messwerte von gesunden Maschinen veröffentlicht, und sie stimmen eng
überein:

| | Kopf leer | Werkzeug angedockt |
|---|---|---|
| Maschine A | 29 | 101 |
| Maschine B | 27 | 103–104 |

Zwei Maschinen sind keine Erhebung; behandeln Sie das daher als „ungefähr das, was gesund
aussieht“ und nicht als Bestehensgrenze. Sie wurden jedoch unabhängig voneinander über das
oben genannte Menü erfasst und liegen an beiden Enden nur wenige Punkte auseinander — mehr,
als das Forum bisher zu bieten hatte. Ein Wert nahe diesen Zahlen bei leerem Kopf bedeutet,
dass die Erkennung wahrscheinlich nicht Ihr Problem ist. Einer, der deutlich darüber liegt,
ist eine Untersuchung wert.

TODO(verify): ob der Messwert driftet, sobald Kopf und Spule warm sind. Ein Besitzer hat
dies aufgeworfen, nachdem sich seine Maschine trotz gesunder Kaltwerte fehlerhaft verhielt,
und schlug vor, jemand solle mitten in einem langen Auftrag oder unmittelbar danach einen
Wert ablesen, um ihn mit dem Kaltwert zu vergleichen. Niemand hat berichtet, das getan zu
haben. Die Community-Zusammenfassung hält separat fest, dass der Leerlauf-Grundwert mit der
Umgebungstemperatur steigt, die Frage ist also berechtigt.

Prusas eigene Release Notes zur Firmware 6.9.0 benennen den Abklingschwellwert für die
„nozzle presence“ und geben sowohl seinen alten als auch seinen neuen Wert an: Er wurde von
**0.095 auf 0.085** verschoben. Prusa stellt dies als Lockerung der oberen Grenze im
Interesse einer zuverlässigeren Erkennung dar. Das ist eine Erstanbieter-Angabe und wird
deshalb hier veröffentlicht. Beachten Sie die Skala: In der Community wurden diese Werte
mit tausend multipliziert diskutiert, ein Forenbeitrag, der einen Schwellwert von „95“
beschreibt, und die `0.095` aus dem Changelog meinen also dieselbe Zahl.

TODO(verify): den *unteren* Schwellwert. Eine Zahl kursiert im Forum, doch der Besitzer,
der sie zitierte, kennzeichnete sie als Vermutung und nicht als Messwert, und Prusas
Release Notes benennen nur den oberen. Ebenfalls offen: wie sich Leerlaufwerte zwischen
Revisionen der Controller-Platine unterscheiden — das bleibt eine Community-Behauptung
ohne veröffentlichte Zahlen dahinter.

### Zwei gegensätzliche Symptome, ein Mechanismus

**Liest ein Werkzeug, das nicht da ist (Phantom-Werkzeug).** Der Leerlaufwert des Kopfes
liegt hoch genug, um bei leerem Kopf als „Werkzeug vorhanden“ gewertet zu werden; die
Maschine glaubt also, ein Werkzeug zu halten, das sie nicht hält.

Beachten Sie, dass ein Park-Fehler **kein** zuverlässiges Symptom dafür ist. Es sieht
danach aus — die Maschine besteht nach dem Parken darauf, dass ein Werkzeug vorhanden ist —,
aber es gibt eine separate, besser dokumentierte Ursache mit einer anderen Lösung, die
weiter unten behandelt wird. Wenn Ihr Werkzeug physisch korrekt parkt und ein
Wiederholversuch den Fehler behebt, lesen Sie jenen Abschnitt, bevor Sie schließen, dass
Ihr Kopf grenzwertig ist.

**Liest kein Werkzeug, obwohl eines montiert ist.** Das Spiegelbild: Ein echtes, aus dem
Dock aufgenommenes Werkzeug liest knapp unterhalb der Schlussfolgerung „Werkzeug
vorhanden“, sodass die Firmware meldet, das Werkzeug sei nach der Aufnahme nicht erkannt
worden. Ein Unterscheidungsmerkmal ist, dass es dazu neigt, jedes Mal an *derselben
Dock-Position* aufzutreten.

Drei Dinge beeinflussen, wo ein bestimmter Kopf liegt:

- **Revision der Controller-Platine.** Leerlaufwerte bei leerem Kopf unterscheiden sich
  systematisch zwischen den xBuddy-Platinenrevisionen, während Werte mit angedocktem
  Werkzeug über die Revisionen hinweg deutlich einheitlicher sind. Besitzer der frühesten
  Revision sind die am stärksten betroffene Gruppe.
- **Umgebungstemperatur.** Der Leerlauf-Grundwert driftet nach oben, je wärmer der Raum
  wird; eine Maschine, die morgens einwandfrei läuft, kann sich nachmittags fehlerhaft
  verhalten.
- **Betriebsdauer.** Mehrere Maschinen haben sich über Tage des Druckens *nach unten*
  eingependelt und sind ohne Eingriff von grenzwertig zu komfortabel gesund gewandert.
  Wenn Sie nahe an der Grenze liegen, kann der Betrieb der Maschine eher helfen als
  schaden.

Ein tatsächlich defekter Kopf liest im Leerlauf hoch, unabhängig davon, an welcher Platine
er steckt, und unabhängig vom Kabel. Wo das verfolgt wurde, änderten Platinentausch und
Ersatz-Hauptkabel nichts, und die Lösung war ein Ersatz-Werkzeugkopf vom Hersteller. An
mindestens einer solchen Einheit wurde ein sich lösender Litzendraht an der Spule selbst
gefunden, und Besitzer haben Spulenverschleiß und beschädigte Spulenverdrahtung als
allgemeinere Qualitätsfrage aufgeworfen.

### Der Vorheizfehler ist wahrscheinlich kein separates Problem

Es gibt einen Vorheizfehler, der auf betroffenen Maschinen bei der ersten Werkzeugaufnahme
während der Werkzeug-Offset-Kalibrierung auftritt. Die Belege deuten darauf hin, dass er
*sekundär* zur Erkennung ist: Die Firmware bestromt die Heizung eines Werkzeugs nicht,
dessen Anwesenheit sie nicht für gesichert hält. An einer Maschine behob ein Austausch des
Werkzeugkopfs sowohl den Erkennungsfehler als auch die Vorheizfehler zugleich. Behandeln
Sie beides als einen Komplex und verfolgen Sie das Erkennungsproblem statt der Heizung.

!!! danger "Modifizierte Firmware-Schwellwerte — lesen Sie dies, bevor Sie danach suchen"
    Einige Besitzer haben eigene Firmware mit veränderten Erkennungsschwellwerten
    kompiliert, damit ihre Maschinen wieder drucken. Machen Sie sich klar, was das
    bedeutet, bevor Sie es in Erwägung ziehen. Auf dieser Hardware erfordert es eine
    **irreversible physische Modifikation der Controller-Platine**. Es wird von beiden
    Unternehmen nicht unterstützt. Und es wirkt, indem es die Firmware *bereitwilliger
    macht, einem grenzwertigen Messwert zu vertrauen* — was der richtige Schritt ist,
    wenn Ihr Kopf gesund und die Firmware zu streng ist, und der falsche, wenn Ihr Kopf
    tatsächlich ausfällt, weil es einen Hardwarefehler verdeckt, den Sie sonst auf
    Garantie hätten ersetzen lassen.

    Diese Seite liefert keine Bauanleitung. **Firmware 6.9.0 hat diese Änderung
    inzwischen offiziell vollzogen**, was den größten Teil des Grundes beseitigt, aus dem
    das überhaupt jemand von Hand tat — aktualisieren Sie, bevor Sie über das Patchen von
    irgendetwas nachdenken. Klären Sie zuerst mit dem Hersteller, ob Ihr Kopf defekt ist.

!!! important "Firmware 6.9.0 hat den Erkennungsschwellwert gelockert — was das für Sie bedeutet"
    Prusas Release Notes zu 6.9.0 halten zwei zusammenhängende Änderungen fest: Sie haben
    **die obere Grenze der Düsenerkennung gelockert**, mit einer zuverlässigeren Erkennung
    als erklärtem Ziel, und den Abklingschwellwert von 0.095 auf 0.085 verschoben.

    **Wenn Ihr Fehler darin bestand, dass ein Werkzeug nach der Aufnahme als fehlend
    gelesen wurde**, ist das die Änderung, auf die Sie gewartet haben. Messwerte, die
    zuvor knapp unter der alten Grenze blieben, erfüllen die neue; aktualisieren Sie also,
    bevor Sie einen Ersatz-Werkzeugkopf verfolgen.

    **Wenn Ihr Fehler die Park-Erkennung betrifft**, siehe den Abschnitt weiter unten.
    Eine frühere Fassung dieser Seite legte nahe, die Schwellwertänderung könnte ihn
    verursachen. Inzwischen sind bessere Belege eingetroffen, die woandershin deuten,
    daher wurde diese Vermutung zurückgezogen.

    Behandeln Sie jede Schwellwertangabe von vor 6.9.0, die Sie im Forum finden, als
    Beschreibung des alten Verhaltens.

### „Werkzeug wird nach dem Parken weiterhin erkannt“ ist ein Timing-Problem, kein Schwellwertproblem

Das verdient eine Trennung vom Rest der Seite, denn der Mechanismus ist ein anderer und
die Lösung ebenso.

Ein mit Logs eingereichter Fehlerbericht gegen die Firmware beschreibt, dass das Parken auf
**6.6.3** die Düse nicht als abwesend bestätigt. Die Routine, die den Düsenzustand prüft,
läuft in eine Zeitüberschreitung, protokolliert, dass die Düse nach dem Parken weiterhin
erkannt wird, versucht es erneut, läuft erneut in eine Zeitüberschreitung, und der
Werkzeugwechsel schlägt fehl. Das Werkzeug hat dabei durchgehend physisch korrekt geparkt —
es löst sich und bleibt im Dock. Rund zwanzig Sekunden später kommt die Firmware von selbst
darauf und korrigiert ihren eigenen Eintrag auf „kein Werkzeug“; der Messwert pendelt sich
also *doch* ein. Er pendelt sich nur lange nach dem Ende des Prüffensters ein.

Zwei Details machen das überzeugend. Der Melder hat denselben Drucker auf **6.6.2**
zurückgestuft, und das Problem verschwand vollständig, ohne dass sonst etwas geändert
wurde. Und das Aufnehmen eines Werkzeugs mit leerem Kopf funktioniert einwandfrei — es ist
speziell das Parken, das fehlschlägt.

**Warum das für die Schwellwert-Erzählung oben wichtig ist:** Der Park-Fehler war bereits
in 6.6.3 vorhanden, also *bevor* 6.9.0 den Erkennungsschwellwert lockerte. Die
Schwellwertänderung kann somit nicht seine Ursache sein, und ein Besitzer, der auf 6.9.0
Park-Meldungen berichtet, sieht höchstwahrscheinlich denselben altbekannten Fehler und
keine Nebenwirkung der Lockerung. Wenn Ihr Parken fehlschlägt, das Werkzeug aber physisch
angedockt ist und ein Wiederholversuch den Fehler behebt, haben Sie es wahrscheinlich mit
dem Einpendelzeit-Problem zu tun und nicht mit einem grenzwertigen Kopf.

Eine zweite Beweislinie weist in dieselbe Richtung. Einer der Besitzer, der die oben
genannten gesunden Werte veröffentlicht hat — an beiden Enden komfortabel von jedem
Schwellwert entfernt —, ist derselbe Besitzer, dessen Maschine fehlgeschlagene
Entladevorgänge gemeldet hatte. Ein derart gesund lesender Kopf kann nicht grenzwertig
sein; was auch immer seine Park-Meldungen verursachte, war also kein grenzwertiger
Erkennungswert. Das passt zu einem Einpendelzeit-Problem und lässt sich schwer mit einem
Schwellwertproblem vereinbaren.

TODO(verify): die Zeitüberschreitung, die die Firmware für die Prüfung zulässt, und wie
lange der Messwert tatsächlich zum Einpendeln braucht. Beides wird im verlinkten Issue
genannt, das zum Zeitpunkt des Schreibens offen und ungelöst ist.

## Überprüfung

`reported` (gemeldet) — die Fehlerfamilie wird unabhängig voneinander von mehreren
Besitzern über mehrere Threads und mehr als eine Firmware-Generation hinweg beschrieben.

Aus erster Hand und aktuell: [6.9.0 Firmware, Werkzeug-Docking](https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/6-9-0-firmware-tool-docking/)
ist ein Besitzer, der Park-Erkennungsfehler meldet, die mit 6.9.0 begannen, auf einer
Maschine, auf der das Parken selbst immer gelingt — ein sauberes Beispiel dafür, dass die
Erkennungsebene der physischen Realität widerspricht, und ein unabhängiger Beleg dafür,
dass diese Fehlerfamilie auf aktueller Firmware lebendig ist. [Werden die INDX der Wave 1
von Prusa mit korrigierten Induktionsspulen ausgeliefert?](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/will-the-prusa-indxs-wave1-ship-with-fixed-induction-coils/)
zeigt Besitzer, die Spulenverschleiß im Vorfeld der Handelswelle als bekanntes Problem
behandeln, wobei dieser Thread eher Spekulation über die Qualitätssicherung als Diagnose
ist und ein Teilnehmer darin das Spulenproblem mit dem separaten Düsenproblem verwechselt.

**Eine Korrektur.** Eine frühere Fassung dieser Seite legte nahe, der gelockerte
Schwellwert in 6.9.0 könnte die Berichte über „Werkzeug wird nach dem Parken weiterhin
erkannt“ erklären — seinerzeit ausdrücklich als Schlussfolgerung und nicht als Behauptung
einer Quelle gekennzeichnet. Ein Firmware-Fehlerbericht hat seither gezeigt, dass der
Park-Fehler auf 6.6.3 auftritt und bei einem Downgrade auf 6.6.2 verschwindet — bevor sich
der Schwellwert überhaupt bewegte. Die Vermutung wurde zurückgezogen, und das Park-Verhalten
hat nun einen eigenen Abschnitt, in dem die Belege stattdessen auf ein
Einpendelzeit-Problem deuten. Das Issue ist offen und ungelöst, daher kann sich auch diese
Darstellung noch ändern.

**Erstanbieter.** Die Schwellwertänderung in 6.9.0 — sowohl die Lockerung als auch die
konkreten Abklingwerte — stammt aus
[Prusas eigenen Release Notes](https://help.prusa3d.com/downloads/core-one-indx), der
stärksten Quellenklasse auf dieser Website: datiert, eindeutig und veröffentlicht von den
Leuten, die die Firmware geschrieben haben. Sie stützt zudem nachträglich das
Schwellwertmodell der Community, da der von Prusa genannte Wert mit der von Besitzern
abgeleiteten Zahl übereinstimmt und sich nur um den Faktor tausend in der Schreibweise
unterscheidet.

**Einzelquelle, und der wichtigste Vorbehalt auf dieser Seite:** Das Drei-Band-Modell der
Schwellwerte, die Unterschiede zwischen Platinenrevisionen, die Temperaturdrift, der
Einlaufeffekt und der Zusammenhang mit dem Vorheizfehler stammen sämtlich aus der
[Zusammenfassung häufiger Probleme](https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/a-summary-of-common-indx-problems/),
die eine inzwischen offline genommene Community-Wissensdatenbank verdichtet. Diese
Verdichtung ist detailliert und in sich stimmig, wurde aber im Forenkorpus nicht unabhängig
reproduziert, und sie stammt aus der Zeit vor 6.9.0. Der erklärende Mechanismus sollte als
gut belegt, aber unbestätigt gelesen werden und nicht als gesichert.

Die Position des Herstellers, wie sie dort wiedergegeben wird, war, dass die Untersuchung
zwischen „Hardwarefehler“ und „Firmware zu streng“ offen blieb. Beides erwies sich für
unterschiedliche Maschinen als zutreffend, weshalb diese Seite mit dem Mechanismus beginnt
statt mit einer Lösung.

## Verwandte Seiten

- [Die Sondierung schlägt fehl oder die Düse berührt das Druckbett nie](loadcell-emi-noise.md) —
  ein anderer Sensor und ein anderer Fehler, aber beide sind „der Drucker glaubt etwas
  Unwahres über seinen eigenen Zustand“
- [Fehler bei der Werkzeug-Offset-Kalibrierung](offset-sensor-board-failure.md) — dort
  tritt der Vorheizfehler meist auf
- [Werkzeugkopf kollidiert mit fertigen Teilen](complete-individual-objects-collision.md) —
  das andere, was rund um ein Parken und einen Werkzeugwechsel schiefgehen kann, und das
  zerstörerischere. Anderer Mechanismus: ein Freiraumfehler der Bewegung, kein
  Erkennungsfehler.
- [In den Druck geschleppte Blobs](stringing-and-wiper-calibration.md) — der andere
  Bereich, den 6.9.0 überarbeitet hat. Besitzer berichten diese Änderung als klare
  Verbesserung, was gegen die oben beschriebene Regression der Park-Erkennung abzuwägen
  ist.
- [An wen Sie sich wenden](support-and-warranty-path.md) — für einen Austausch des
  Werkzeugkopfs
