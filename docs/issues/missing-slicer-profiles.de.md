---
title:        Nur eine Düsengröße hat ein Slicer-Profil
confidence:   reported
updated:      2026-08-25
author:       hyiger
printer:      Core One
toolhead:     INDX
hotend:       CHT high-flow
nozzle:       0.4mm is the only variant offered
firmware:     unknown
sources:
  - https://github.com/prusa3d/PrusaSlicer-settings-prusa-fff/issues/45
  - https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/missing-profiles-in-slicer-for-non-0-4-nozzles-and-other-materials/
superseded_by:
source_sha:   68348d9c666ee37cdad0ae2f151c928916ff805cced373a7606558515455c97f
---
# Nur eine Düsengröße hat ein Slicer-Profil

## Zusammenfassung

PrusaSlicer bietet für den INDX genau eine Düsenvariante an: High-Flow 0.4mm. Wer eine
Düse mit 0.25, 0.5, 0.6, 0.8 oder 1.0mm kauft, findet kein Profil, das sich dafür
auswählen ließe. Es geht nicht darum, dass Profile dünn oder unausgereift wären — die
übrigen Größen werden überhaupt nicht angeboten. Eine Anfrage, sie zu ergänzen, ist
upstream seit Juli 2026 offen, ohne Reaktion.

Unterschiedliche Düsengrößen über die Werkzeuge hinweg waren ein beworbenes
Hauptmerkmal dieses Werkzeugwechslers; man sollte das also wissen, bevor man Düsen
kauft, und erst recht, bevor man Shop-Guthaben als Entschädigung für Düsen annimmt.

## Details

### Was tatsächlich im Bundle enthalten ist

Das ist überprüfbar und keine Frage von Berichten. Prusa veröffentlicht sein
Profil-Bundle, und in der aktuellen Ausgabe deklarieren beide INDX-Druckermodelle — das
mit vier und das mit acht Werkzeugen — eine einzige Variante:

```ini
variants = HF0.4
```

Diese eine Zeile ist die Einschränkung. Eine Variante ist das, was PrusaSlicer beim
Hinzufügen des Druckers zur Auswahl stellt; ist nur eine deklariert, lässt sich keine
andere Düsengröße auswählen, gleich welche Materialprofile dahinter vorhanden sein
mögen.

Das Bundle enthält durchaus eine große Zahl INDX-spezifischer Filamenteinträge, und
einige der internen Vererbungsvorlagen verweisen auf größere Extrusionsbreiten. Es gibt
also Vorarbeiten. Was fehlt, ist die druckerseitige Variantendeklaration, die all das
überhaupt erst erreichbar machen würde.

### Materialien

Dieselbe Upstream-Anfrage bittet auch um Materialien. Ein Blick in das Bundle:

- **FLEX** taucht in INDX-spezifischen Vorlagen auf, es gibt also zumindest teilweise
  Vorarbeiten.
- **HIPS** taucht in keinem INDX-spezifischen Abschnitt auf.
- **TPU**, **PVA** und **BVOH** ebenso wenig.

Die für Anwender sichtbare Standard-Materialliste beider INDX-Modelle ist die übliche
PLA- und PETG-Familie für die eine verfügbare Variante.

Das ist mehr als eine Frage der Bequemlichkeit: HIPS und die löslichen Materialien sind
das, wozu man greift, um auf einem Werkzeugwechsler Kontaktflächen von Stützstrukturen
zu drucken — und genau das ist zu einem großen Teil der Grund, warum man sich einen
anschafft.

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
  offen seit dem 31. Juli 2026, zum Zeitpunkt des Schreibens ohne Kommentare und ohne
  Reaktion. Ein Issue mit einem einzigen Melder und ohne Resonanz bleibt leicht
  unbeachtet; mehrere Besitzer, die benennen, welche Größen und Materialien sie
  tatsächlich brauchen, lassen sich schwerer übergehen.
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
einer Firmware-Veröffentlichung — und nicht die Schilderung einer fremden Maschine.

**Die Auswirkung ist berichtet**, von vier Besitzern in
[einem Forumsthread](https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/missing-profiles-in-slicer-for-non-0-4-nozzles-and-other-materials/),
von denen einer Düsen mit 0.5 und 1.0mm kaufte, bevor er feststellte, dass sie sich
nicht nutzen lassen, und ein anderer die Sache beim Abwägen der Düsen-Entschädigung
ansprach. Die
[Upstream-Anfrage](https://github.com/prusa3d/PrusaSlicer-settings-prusa-fff/issues/45)
ist ein zweiter Ort, wurde jedoch von derselben Person eingereicht, die den
Forumsthread eröffnet hat, und ist damit ein Cross-Post statt einer unabhängigen
Bestätigung.

**Wo das schwächer ist, als es aussieht.** Ob FLEX wirklich nutzbar ist, bleibt unklar:
Die Vorlagen sind im Bundle vorhanden, doch das ist nicht dasselbe wie ein auswählbares,
getestetes Profil, und kein Besitzer in den Quellen berichtet, damit gedruckt zu haben.
Behandeln Sie die obigen Materialbefunde als Beschreibung dessen, was in der Datei
steht, und nicht dessen, was funktioniert.

Das veraltet schnell. Es ist eine Konfigurationslücke, die eine Profilveröffentlichung
mit einem einzigen Update schließt; prüfen Sie daher das aktuelle Bundle, bevor Sie
danach handeln.

## Verwandte Themen

- [Düsenhärte](nozzle-hardness.md) — die Entschädigung, mit der dies zusammenwirkt
- [Kommentierter Profil-G-Code](../gcode/indx-profile-gcode.md) — was ein Profil
  mitführt und warum die Düsendeklaration pro Werkzeug von Bedeutung ist
