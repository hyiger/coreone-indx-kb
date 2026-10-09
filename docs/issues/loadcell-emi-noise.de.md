---
title:        Probing schlägt fehl oder die Düse berührt das Bett nie — Rauschen im Wägezellensignal
confidence:   reported
updated:      2026-10-08
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
  - https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/bed-leveling-issues-3/
  - https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/loadcell-noise-and-mesh-bed-levelling/
  - https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/core-one-indx-tool-offset-out-of-bounds-36130-loadcell-test-issue/
  - https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/loadcell-test-tool-crash-on-calibration/
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5518
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/lib/Marlin/Marlin/src/module/probe.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/src/common/selftest/selftest_loadcell_indx.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.0/src/common/selftest/selftest_loadcell_indx.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/lib/Marlin/Marlin/src/module/prusa/toolchanger_indx.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5520
  - https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/homing-shows-early-endstop-detected-message/
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/lib/Marlin/Marlin/src/module/prusa/homing_corexy.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.9.2
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/compare/v6.9.1...v6.9.2
superseded_by:
source_sha:   ca258e7325a6910a24fd976feab5d06e03f40903510bf2200b7f669a1e9eb173
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
vollständig behoben war. Ein Selbsttest der Wägezelle, der direkt nach einem
Werkzeugwechsel Rauschen meldet (möglicherweise auch nach einem, den der Test selbst
vornimmt), kann eine andere Sache sein, mit einer vermuteten Ursache in der Firmware;
lesen Sie dazu den Abschnitt unten, bevor Sie dafür Hardware kaufen.

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

### Ein verrauschter Selbsttest ist nicht immer eine Störung

In einem Bericht
([#5468](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5468)) gab der
Wägezellentest in der ersten Kalibrierung nach dem Umbau eines C1 zum C1+ (Gen 2) mit
INDX, unter 6.9.0, nie seine Pieptöne aus und wies das Drücken zurück, gemeldet entweder
als verfrühtes Drücken oder als verrauschtes Signal; nachdem der Besitzer den Assistenten
abgebrochen und neu gestartet hatte, bestand er sofort. Der Besitzer vermutete, dass der
in der Firmware vor INDX eingestellte Lautlos-Modus übernommen worden war. Prusa
antwortete, der Umbau setze den Drucker nach eigenem Kenntnisstand auf
Werkseinstellungen zurück, und der Fehler lasse sich nicht nachstellen. Ein zweiter
Besitzer, ebenfalls mit einem Gen-2-Umbau, beschreibt in
[einem Forumsthread](https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/bed-leveling-issues-3/)
denselben Ausgang — erst Fehlschlag, dann Erfolg beim zweiten Versuch: Der Selbsttest
meldete immer wieder ein verrauschtes Signal, bis der Besitzer ihn abbrach, den Drucker
eine Referenzfahrt (Homing) ausführen ließ und ihn erneut startete; dann bestand er.
Gemeinsam ist den beiden nur dieser Ausgang. Der erste Bericht betraf nur den ersten Durchlauf nach dem Umbau, und
die Pieptöne fehlten; der Fehlschlag beim zweiten Besitzer war nicht an einen ersten
Durchlauf gebunden: Er trat sowohl im kompletten Kalibrierablauf auf als auch, wenn der
Test allein an der kalten Maschine gestartet wurde, und der Besitzer beschreibt ein
leises Brummen beim fehlschlagenden Versuch.
Zwei Berichte an verschiedenen Stellen machen diesen Ausgang beim zweiten Versuch zu
`reported`, aber keiner der beiden erklärt ihn. Ein zweiter Versuch kostet nichts:
Schlägt der Selbsttest fehl, brechen Sie ab und führen Sie ihn noch einmal aus, bevor
Sie von einer Störung ausgehen. Der zweite Besitzer ließ den Drucker vor dem zweiten
Versuch außerdem eine Referenzfahrt ausführen; dieser Schritt stammt allein aus seinem
Bericht, `provisional`, auch wenn der folgende Bericht einen Grund nennt, warum er eine
Rolle spielen könnte.

Ein späterer Bericht bietet eine Erklärung aus der Firmware an, die auf beide passen
würde. In [#5518](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5518) stellte ein
Besitzer mit einem Gen-2-Umbau und acht Werkzeugen unter 6.9.1 fest, dass der Selbsttest
nach jedem Werkzeugwechsel als verrauscht fehlschlug und nach einer Referenzfahrt wieder
bestand, mit jedem der vier ausprobierten Werkzeuge. Der Berichtende führte das auf den
Extrudermotor zurück, der beim INDX auch die Werkzeugverriegelung betätigt: Ein
Werkzeugwechsel lässt diesen Motor eingeschaltet, und solange er eingeschaltet ist, ist
das Wägezellensignal so verrauscht, dass der Test fehlschlägt. Nur diesen Motor
einzuschalten, ohne Werkzeugwechsel, machte das Signal verrauscht; ihn nach einem
Werkzeugwechsel auszuschalten, machte es ohne Referenzfahrt wieder sauber. Eine
Referenzfahrt behebt es, weil die Referenzfahrt in Z selbst ein Abtasten des Betts ist
und das Abtasten den Extrudermotor zuvor ausschaltet; eine Referenzfahrt nur in X und Y
ließ das Rauschen bestehen. Das Bewegen von Kabeln, das Schalten von Lüftern und
Heizungen und Temperaturänderungen lösten es weder aus, noch beseitigten sie es — genau
das unterscheidet es von der Störeinkopplung durch das Heizelement, um die es im Rest
dieser Seite geht. Ein weiterer Besitzer hörte im selben Issue während des
fehlschlagenden Tests etwas aus dem Inneren des Kopfes, stellte fest, dass das Abbrechen
des Tests den Motor ausschaltete, und bestand den zweiten Versuch. Der
Firmware-Quellcode passt zur Lesart des Berichtenden: In 6.9.1 schaltet der
[Abtastcode](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/lib/Marlin/Marlin/src/module/probe.cpp)
den Extrudermotor vor dem Abtasten aus, mit einem Kommentar, dass dies das Rauschen am
Sensor verringert; der
[Wägezellen-Selbsttest des INDX](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/src/common/selftest/selftest_loadcell_indx.cpp)
tut das nicht; und der
[Werkzeugwechselcode](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/lib/Marlin/Marlin/src/module/prusa/toolchanger_indx.cpp)
stellt nach dem Betätigen der Verriegelung Motorstrom und Position des Motors wieder her,
nicht aber, ob er eingeschaltet war.

Das würde die beiden früheren Berichte erklären: ein Abbruch, der den Motor ausschaltet,
eine Referenzfahrt vor dem zweiten Versuch und das leise Brummen, das der zweite Besitzer
hörte. Keiner dieser beiden Besitzer hat das geprüft; die Verbindung ist also eine
Schlussfolgerung. Keiner der beiden sagt zudem, ob gerade ein Werkzeug gewechselt worden
war. In 6.9.1 nimmt der Selbsttest allerdings selbst ein Werkzeug auf, wenn keines
gehalten wird, und
[6.9.0](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.0/src/common/selftest/selftest_loadcell_indx.cpp),
unter dem der erste Bericht entstand, enthält denselben Schritt; diese Aufnahme würde den
Motor auf dieselbe Weise eingeschaltet lassen. Auch das ist eine Lesart des Codes, kein
erprobtes Ergebnis. Die Erklärung selbst stützt sich auf ein einziges Issue,
`provisional`; Prusa hatte dort bis zum oben genannten Datum nicht geantwortet, und 6.9.2
ändert über Filament-Voreinstellungen hinaus nichts, was einen INDX betrifft, behebt es
also nicht. In der Praxis: Meldet der
Selbsttest nach einem Werkzeugwechsel Rauschen, oder wenn der Test zuerst ein Werkzeug
aufnehmen musste, führen Sie eine Referenzfahrt aller Achsen aus, nicht nur in X und Y,
und starten Sie ihn erneut, bevor Sie eine Störung oder die Wägezelle verdächtigen.

Ob ein verrauschter Selbsttest auch verrauschtes Abtasten bedeutet, ist nicht geklärt.
Dieser zweite Besitzer und ein dritter, in
[einem eigenen Thread](https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/loadcell-noise-and-mesh-bed-levelling/),
brachten beide die Rauschmeldungen des Selbsttests mit Problemen bei der ersten Schicht
in Verbindung und fragten, ob das eine das andere verursacht. Der zweite Besitzer hat
eine Stelle auf dem Bett, an der die erste Schicht durchgehend nicht haftet, und
verdächtigt die Wägezelle, ohne Diagnose. Der dritte, dessen Selbsttest häufig Rauschen
meldet, versuchte es zu prüfen: Er ließ dasselbe Mesh-Bed-Leveling zweimal
hintereinander laufen, änderte dazwischen nichts außer der Reinigung der Druckplatte
und las die abgetasteten Werte aus. Er fand die beiden Durchläufe an jedem Punkt nah
beieinander, hielt das für innerhalb der Toleranz und fragte, ob die Rauschmeldungen
damit kein Grund zur Sorge seien. TODO(verify): die Streuung zwischen den
beiden Durchläufen, wie im Thread zu Wägezellenrauschen und Mesh-Bed-Leveling
angegeben; ein Bereich, der eine gesunde Wiederholung von einer fehlerhaften trennt,
ist hier nicht ermittelt. Jeder dieser Punkte ist ein einzelner Bericht,
`provisional`, und keiner der drei Besitzer hat einen Ferrit angebracht; zur Abhilfe
weiter unten sagen sie also weder etwas dafür noch dagegen. Ein wiederholtes Mesh kann
trotzdem eine günstige Prüfung sein, bevor Sie Hardware kaufen, aber nur, wenn es so
läuft, wie ein Druck abtastet, also mit heißem Hotend, weil die Arbeitshypothese auf
dieser Seite eine Störung durch das Heizelement ist. Der Thread sagt nicht, ob die Düse bei diesen Durchläufen
heiß war. Zwei übereinstimmende Durchläufe mit kalter Düse schließen eine Störung nicht
aus. Das ist eine Schlussfolgerung, keine erprobte Regel. Trifft die Erklärung aus
#5518 zu, gibt es einen weiteren Grund, warum beides auseinanderfallen kann: Das
Abtasten schaltet den Extrudermotor aus, der Selbsttest nicht; ein Selbsttest, der aus
diesem Grund fehlschlägt, sagt also nichts über das Abtasten. Keiner der beiden Besitzer
hat geprüft, ob dies auf den eigenen Drucker zutraf.

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

    Ein Bericht aus einem anderen Thread endete mit einer Hardwarelösung statt mit einer
    Störung als Ursache. Ein Besitzer unter 6.6.0 und 6.6.1, dessen Wägezellentest immer wieder vor instabilen
    Messwerten warnte — obwohl ein Druck auf die Düse nach dem Wegklicken der Warnung
    trotzdem registriert wurde — und dessen Drucke mit dem Werkzeug-Offset-Fehler 36130
    abbrachen,
    [führte das Problem schließlich auf ein defektes Teil zurück](https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/core-one-indx-tool-offset-out-of-bounds-36130-loadcell-test-issue/),
    das er als Werkzeughalter bezeichnet und beim Hersteller reklamiert hat; seitdem
    funktioniert alles. Auf die Warnung im Wägezellentest kommt der Beitrag nicht
    zurück; dass auch sie verschwand, folgt aus dem „alles“, ausdrücklich gesagt wird es
    nicht. Ein Ferrit wird im Beitrag nicht erwähnt. Aus dem Beitrag geht
    nicht hervor, welche Baugruppe gemeint ist, daher ist dieser Bericht `provisional`.
    Derselbe Fall erscheint unter
    [Werkzeug-Offset-Kalibrierung schlägt fehl](offset-sensor-board-failure.md).

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

    Ein Besitzer berichtet von etwas, das wie eine Nebenwirkung derselben Änderung
    aussieht, in
    [#5520](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5520) und in einem
    [Forumsthread](https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/homing-shows-early-endstop-detected-message/):
    Seit 6.9.1 zeigen sowohl die Homing-Kalibrierung als auch das normale Homing mehrmals
    die Meldung `Endstop early trigger` und dauern länger, werden aber abgeschlossen, und
    Drucke laufen normal. Der Besitzer hatte die Homing-Kalibrierung nach dem Update auf
    6.9.1 erneut ausgeführt, was Prusa als Erstes vorschlug; mit der Rückkehr zur
    6.9.1-Beta und erneuter Homing-Kalibrierung verschwand die Meldung. Prusa gibt an,
    dies an den Druckern, an denen die Änderung getestet wurde, nicht gesehen zu haben. Im
    [Quellcode von 6.9.1](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/lib/Marlin/Marlin/src/module/prusa/homing_corexy.cpp)
    kennzeichnet diese Meldung eine Messfahrt beim X/Y-Homing, die zu früh angehalten hat
    und wiederholt wird; die Messung gibt erst auf, wenn die Wiederholungen ausgeschöpft
    sind. Sie stammt vom X/Y-Homing, nicht von der Wägezelle, und ist kein Zeichen einer
    Störung. `provisional`.

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
    durchzugehen; gegen das Rauschen selbst tun sie nichts.
    [6.9.2](https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.9.2),
    erschienen am 2026-10-07, fügt die Filament-Voreinstellungen für PVA und BVOH
    hinzu, die 6.9.1 angekündigt, aber nicht enthalten hatte, und ändert sonst nichts,
    was einen INDX betrifft
    ([Vergleich](https://github.com/prusa3d/Prusa-Firmware-Buddy/compare/v6.9.1...v6.9.2)),
    also auch nichts an dem, was diese Seite beschreibt. Wenn Sie dies deutlich nach
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
oben zurückgehalten. Für den Selbsttest, der beim zweiten Versuch besteht, gibt es
inzwischen zwei Berichte an verschiedenen Stellen, und Prusa konnte den ersten nicht
nachstellen. Die Erklärung über den Extrudermotor stammt aus einem einzigen Issue, in dem
ein weiterer Besitzer den Teil mit Abbrechen und zweitem Versuch bestätigt; der
Firmware-Quellcode ist damit vereinbar, aber Prusa hat sie nicht bestätigt, und keiner
der beiden früheren Besitzer hat sie geprüft. Die Referenzfahrt vor dem zweiten Versuch, die
Prüfung mit wiederholtem Mesh, die Reklamation beim Hersteller und der Fall der Werkzeugerkennung
unter „Verwandte Seiten“ sind jeweils ein einzelner Bericht, und die Homing-Meldung zum
frühen Auslösen stammt von einem Besitzer, an zwei Stellen gepostet. Keiner dieser Besitzer hat einen Ferrit angebracht;
sie stärken oder schwächen die Argumente dafür also nicht. Die Homing-Korrektur stützt
sich auf die Release Notes und das Firmware-Repository des Herstellers, nicht auf
Berichte von Besitzern.

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
- [Phantom-Werkzeuge, „Werkzeug nicht erkannt“ und Park-Fehler](tool-detection-ringdown-decay.md)
  — wie der Kopf ein eingesetztes Werkzeug erkennt. Ein Erkennungsfehler kann den
  Wägezellentest ebenfalls stoppen, ohne ein Wägezellenfehler zu sein: In
  [einem Bericht](https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/loadcell-test-tool-crash-on-calibration/)
  unter 6.9.1 nahm der Testschritt ein Werkzeug auf und fuhr es gegen die anderen Docks,
  und der Besitzer stellte fest, dass der Drucker ein eingesetztes Werkzeug nie erkannte
  (`provisional`). Eine Prüfung der Verkabelung des Kopfes ergab nichts, und der Fall lag
  zum oben genannten Datum noch beim Prusa-Support.
