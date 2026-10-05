---
title:        Probing schlägt fehl oder die Düse berührt das Bett nie — Rauschen im Wägezellensignal
confidence:   reported
updated:      2026-09-25
author:       hyiger
printer:      Core One
toolhead:     INDX
hotend:       unknown
nozzle:       unknown
firmware:     unknown
sources:
  - https://help.prusa3d.com/article/loadcell-measure-failed-31526-core-one-35526-core-one-l-36526-core-one-indx-26526-mk4s-13526-mk4-27526-mk3-9s-21526-mk3-9-36526-core-one-indx_405741
  - https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/nozzle-not-touching-bed-during-probing/
  - https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/a-summary-of-common-indx-problems/
  - https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/tool-offset-calibration-failing/
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5468
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.9.1-beta
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.9.1
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/compare/v6.9.1-beta...v6.9.1
superseded_by:
source_sha:   0eb57cb747bbdc4f583eadc68c8df3421543b18288b6a2c9dfba2a4c03039085
---
# Probing schlägt fehl oder die Düse berührt das Bett nie — Rauschen im Wägezellensignal

## Zusammenfassung

Wenn sich das Abtasten des Betts so verhält, als habe die Düse bereits aufgesetzt,
während sie sichtbar noch deutlich von der Druckplatte entfernt ist, liegt die Ursache
eher in elektrischen Störungen im Wägezellensignal als in etwas Mechanischem. Der
Hersteller hat Störeinkopplung vom Heizelement als Arbeitshypothese bestätigt. Die
Lösung aus der Community, die inzwischen auch der Herstellersupport empfiehlt, ist ein
aufklappbarer Ferritkern am Hauptkabel des Werkzeugkopfs, nahe der Stelle, an der es in
die Controllerplatine eintritt. Mehrere Besitzer berichten, dass der Fehler damit
vollständig behoben war.

## Fehlercodes, die hierher führen

| Code | Anzeige am Drucker |
|---|---|
| [`36526`](https://help.prusa3d.com/article/loadcell-measure-failed-31526-core-one-35526-core-one-l-36526-core-one-indx-26526-mk4s-13526-mk4-27526-mk3-9s-21526-mk3-9-36526-core-one-indx_405741) | Loadcell measure failed |
| [`36527`](https://help.prusa3d.com/article/loadcell-bad-configuration-31527-core-one-35527-core-one-l-36527-core-one-indx-26527-mk4s-13527-mk4-27527-mk3-9s-21527-mk3-9_405749) | Loadcell bad configuration |
| [`36528`](https://help.prusa3d.com/article/loadcell-timeout-31528-core-one-35528-core-one-l-26528-mk4s-36528-core-one-indx-13528-mk4-27528-mk3-9s-21528-mk3-9_405757) | Loadcell timeout |

Alle drei sind Wägezellenfehler. Störungen zeigen sich eher als fehlgeschlagene
Messung oder als Zeitüberschreitung denn als Konfigurationsfehler.

## Details

Der INDX erfasst den Kontakt mit dem Druckbett über eine Wägezelle, und deren Signal
teilt sich einen Kabelbaum mit der Leistungsversorgung des Heizelements. In diesem
Kabelbaum ist das Leistungspaar verdrillt, was den größten Teil seiner abgestrahlten
Störungen aufhebt, das Signalpaar der Wägezelle jedoch nicht — es ist dem, was das
Heizelement tut, also vergleichsweise ungeschützt ausgesetzt. Ist diese Störung groß
genug, wertet die Firmware sie als Kontaktereignis.

Das verräterische Merkmal ist, *wie stark* das Verhalten danebenliegt. Ein mechanisches
oder ein Offset-Problem lässt die Düse etwas zu hoch oder etwas zu tief abtasten. Ein
störungsbedingter Fehlkontakt lässt sie anhalten, während die Düse offensichtlich nicht
einmal in die Nähe der Druckplatte gekommen ist — ein Abstand, den man quer durch den
Raum sieht, und keiner, den man mit Papier ausmisst. Wenn Sie einen Abtastvorgang
beobachten und denken „es ist ja nicht einmal nahe herangekommen“, dann ist
wahrscheinlich diese Seite Ihr Fehlerbild.

Berichtete Symptome dieser Gruppe:

- Das Abtasten wird abgeschlossen, während die Düse sichtbar von der Druckplatte
  entfernt ist
- Fehlschlagende Selbsttests der Wägezelle
- Z-Homing oder Abtasten, das **erst bei heißem Hotend** fehlschlägt — ein starker
  Hinweis, weil er auf das Heizelement als Störquelle deutet
- Falsche Z-Kollisionsfehler
- Wiederholte Versuche beim Bed-Leveling und ungewöhnlich lange Mesh-Zeiten
- Eine erste Schicht, die nicht haftet oder Filament zu einem Klumpen hochzieht, weil
  die Maschine das Bett höher wähnt, als es ist

Nicht jeder fehlgeschlagene Selbsttest ist eine Störung. In einem Bericht
([#5468](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5468)) gab der
Wägezellentest in der ersten Kalibrierung nach dem Umbau eines C1 zum C1+ (Gen 2) mit
INDX, unter 6.9.0, nie seine Pieptöne aus und wies das Drücken zurück, gemeldet entweder
als verfrühtes Drücken oder als verrauschtes Signal; nachdem der Besitzer den Assistenten
abgebrochen und neu gestartet hatte, bestand er sofort. Der Besitzer vermutete, dass der
in der Firmware vor INDX eingestellte Lautlos-Modus übernommen worden war. Prusa
antwortete, der Umbau setze den Drucker nach eigenem Kenntnisstand auf
Werkseinstellungen zurück, und der Fehler lasse sich nicht nachstellen. Das ist ein
einzelner, ungeklärter Bericht, `provisional`, aber ein zweiter Versuch kostet nichts:
Schlägt der Selbsttest beim ersten Durchlauf nach einem Umbau fehl, führen Sie ihn noch
einmal aus, bevor Sie von einer Störung ausgehen.

### Was Sie versuchen können

1. **Setzen Sie einen aufklappbaren Ferritkern auf das Hauptkabel des Werkzeugkopfs**,
   nahe dem Ende an der Controllerplatine. Das ist die Abhilfe mit der meisten
   unabhängigen Bestätigung, und sie wird inzwischen auch vom Herstellersupport
   vorgeschlagen. Ein einfacher aufklappbarer Kern außen um das Kabel hat bei mehreren
   Maschinen genügt.
2. **Wenn ein einfacher Kern nicht ausreicht**, haben hartnäckige Fälle darauf
   angesprochen, das Kabel statt eines einzelnen Durchgangs mit mehreren Windungen durch
   einen höherwertigen Ringkern zu führen. TODO(verify): die konkrete
   Ferrit-Materialgüte und die Anzahl der Windungen. Berichtet im Summary-Thread zu
   häufigen Problemen; hier nicht unabhängig bestätigt.
3. **Kalibrieren Sie anschließend neu oder setzen Sie auf Werkseinstellungen zurück.**
   An mehreren Maschinen schien der Ferrit nichts zu bewirken, bis die gespeicherten
   Kalibrierdaten verworfen wurden — durch ein Zurücksetzen auf Werkseinstellungen oder
   eine vollständige Neukalibrierung —, weil der Drucker noch mit Werten arbeitete, die
   er bei verrauschtem Signal aufgenommen hatte. Wenn Sie einen Kern anbringen und sich
   nichts ändert, tun Sie dies, bevor Sie schließen, dass der Kern nicht geholfen hat.
4. **Achten Sie auf die Position.** Mindestens eine berichtete Position — am Stecker der
   Erweiterungsplatine des Controllers statt am Hauptkabel — hat das Problem
   verschlimmert. Wenn Ihre erste Position die Lage verschlechtert, versetzen Sie den
   Kern, statt den Ansatz aufzugeben.

!!! tip "Störungen von einer tatsächlich defekten Wägezelle unterscheiden"
    Ein Ferritkern behandelt elektrische Störungen. Er behebt keine defekte Wägezelle,
    und beide stellen sich fast identisch dar. Ein Besitzer hat sie sauber getrennt:
    Sein Abtastfehler **folgte einem Ersatz-Werkzeugkopf** über einen Tausch hinweg,
    während der ursprüngliche Kopf jedes Mal einwandfrei homte, auf einer neueren
    Controllerplatine. Störeinkopplung ist eine Eigenschaft der Maschine und ihrer
    Verkabelung; ein Fehler, der mit dem Werkzeugkopf mitwandert, sitzt im Werkzeugkopf.
    Siehe [diagonale Streifenbildung](diagonal-banding.md), wo dieser Tausch beschrieben
    ist. Wenn Ihre Platine neueren Datums ist und der Fehler mit dem Kopf mitwandert,
    wenden Sie sich an den Hersteller, statt Ferrite zu kaufen.

!!! note "Eine dritte Ursache: Homing, das nach bestandener Kalibrierung fehlschlägt"
    Firmware 6.9.1, am 2026-09-25 als stabile Version erschienen, nennt eine
    Homing-Korrektur für Drucker, die ihre erste Homing-Kalibrierung bestanden, beim
    späteren erneuten Homing aber scheiterten. Die von Prusa beschriebene Änderung
    betrifft die Motorströme. Die
    [Release Notes](https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.9.1)
    nennen keine Achse, doch die einzige Änderung an Motorströmen im Firmware-Repository
    zwischen der Beta und der stabilen Version
    ([Vergleich](https://github.com/prusa3d/Prusa-Firmware-Buddy/compare/v6.9.1-beta...v6.9.1))
    betrifft das diagonale XY-Homing, nicht das Z-Abtasten mit der Wägezelle. Die Notes
    sagen zudem nichts über die Wägezelle oder das Heizelement; das ist also ein von
    dieser Seite getrennter Fehler und keine Behebung für ihn. Passen Ihre Homing-Fehler
    zu dieser Beschreibung statt zum Muster oben — Fehlschlag nur bei heißem Hotend, die
    Düse hält sichtbar vor der Druckplatte an —, aktualisieren Sie die Firmware, bevor
    Sie einen Ferrit anbringen. Das stützt sich allein auf die Release Notes und das
    Firmware-Repository des Herstellers, `provisional`: Bisher hat kein Besitzer
    berichtet, dass die Korrektur seine Homing-Fehler behoben hat.

Wenn nichts davon hilft, insbesondere wenn der Fehler nur bei eingeschalteter Heizung
auftritt und Sie eine frühe Platinenrevision haben, führt der Weg über einen
Hardwaretausch beim Hersteller. Ein Besitzer berichtete stattdessen von Erfolg damit,
die Verkabelung am Controllerstecker in geerdete Abschirmfolie zu wickeln, was mit
derselben Grundursache vereinbar ist.

TODO(verify): die Rohwertbereiche der Wägezelle, die eine gesunde von einer betroffenen
Maschine unterscheiden. Der Summary-Thread nennt für beide je ein Band an Ruhewerten, und
diese Zahlen würden diese Seite weit diagnostischer machen — sie müssen aber vor einer
Veröffentlichung gegen die Firmware geprüft werden, denn ein Leser wird anhand von ihnen
entscheiden, ob seine Maschine defekt ist.

!!! note "Das ist eine Abmilderung, keine Behebung"
    Der Hersteller hat den Ferrit als Behelfslösung und nicht als Behebung beschrieben,
    und eine firmwareseitige Verbesserung der Wägezellenauswertung ist Berichten zufolge
    in Arbeit. Weder die Release Notes zu 6.9.0 noch die zu 6.9.1 beschreiben eine
    Änderung daran, wie das Wägezellensignal gefiltert oder bewertet wird. Die
    [Release Notes zu 6.9.1-beta](https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.9.1-beta)
    geben der Werkzeug-Offset-Kalibrierung allerdings mehr Versuche beim Z-Abtasten. Die
    Notes der stabilen Version wiederholen das nicht, aber die stabile 6.9.1 baut auf
    dieser Beta auf: Im Firmware-Repository fügt sie dem Beta-Tag
    [15 Commits](https://github.com/prusa3d/Prusa-Firmware-Buddy/compare/v6.9.1-beta...v6.9.1)
    hinzu, von denen keiner den Code der Werkzeug-Offset-Kalibrierung betrifft. Das
    ergibt sich aus der Release-Historie, nicht aus den Notes. Mehr Wiederholungen geben
    einem verrauschten Antippen mehr Gelegenheiten,
    durchzugehen; gegen das Rauschen selbst tun sie nichts. Wenn Sie dies deutlich nach
    dem oben genannten Datum lesen, prüfen Sie, ob eine neuere Firmware das Problem
    behoben hat, bevor Sie Hardware ergänzen.

## Verifizierung

`reported` (mehrfach berichtet) — unabhängig voneinander in mehr als einem Thread von
verschiedenen Besitzern beschrieben.

In [Düse berührt beim Abtasten das Bett nicht](https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/nozzle-not-touching-bed-during-probing/)
berichtet ein Besitzer von einem Abtastvorgang, bei dem die Düse weit über der
Druckplatte blieb, an einer Maschine, die alle Einrichtungskalibrierungen bestanden
hatte; nach dem Anbringen eines Ferritkerns am Hauptkabel bestätigt er, dass das Abtasten
korrekt zu arbeiten begann. Ein zweiter Besitzer im selben Thread berichtet von einem
Vorfall mit zu hohem Abtasten und brachte vorsorglich einen Kern an, ohne Verschlechterung.
Der Mechanismus, die Bestätigung durch den Hersteller und die Ringkern-Variante stammen aus
der [Zusammenfassung häufiger Probleme](https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/a-summary-of-common-indx-problems/),
einer Verdichtung einer inzwischen offline genommenen Community-Wissensdatenbank.

Wo die Quellen schwächer sind: Der in der Zusammenfassung beschriebene kontrollierte
A/B-Test (Fehlschlag ohne Kern, Funktion mit Kern, erneuter Fehlschlag nach Entfernen)
ist dort aus zweiter Hand berichtet und im Forumsbestand nicht gesondert nachweisbar. Die
Wertebänder der Wägezelle und die Ferritspezifikationen haben nur eine Quelle und werden
oben zurückgehalten. Der Bericht zum Selbsttest beim ersten Durchlauf ist ein einzelnes
Issue, das Prusa nicht nachstellen konnte, und die Homing-Korrektur stützt sich auf die
Release Notes und das Firmware-Repository des Herstellers, nicht auf Berichte von
Besitzern.

## Verwandte Seiten

- [Werkzeug-Offset-Kalibrierung schlägt fehl](offset-sensor-board-failure.md) — anderer
  Sensor, anderer Fehler, oft mit diesem verwechselt
- [Oozing verdirbt Bettabtastung und Werkzeugkalibrierung](oozing-during-probing-and-calibration.md)
  — eine völlig andere Ursache mit überlappendem Symptom, die auszuschließen sich lohnt.
  Wenn sich vor dem Kontakt Material an der Düse ansammelt, ist es die andere.
- [Werkzeug-Offset-Kalibrierung schlägt fehl: Bett in Z nicht ausgerichtet](tool-offset-bed-z-alignment.md)
  — ein mechanischer Fehler, der an einer Maschine für Wägezellen-Störungen gehalten
  wurde; ein Ferritkern hat dagegen nichts ausgerichtet
- [Wen Sie kontaktieren](support-and-warranty-path.md) — falls es zu einer
  Ersatzteilanfrage kommt: zuerst Diagnose von Prusa, dann die Hardware von Bondtech.
- [Montagehinweise](../reference/assembly-notes.md) — wenn der Wägezellentest seit dem
  Aufbau der Maschine instabil war und nie funktioniert hat, behandeln Sie es als
  Aufbaufrage, bevor Sie es als Störungsfrage behandeln.
