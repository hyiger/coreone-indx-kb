---
title:        Probing schlägt fehl oder die Düse berührt das Bett nie — Rauschen im Wägezellensignal
confidence:   reported
updated:      2026-10-18
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
  - https://forum.prusa3d.com/forum/ceske-forum-obecna-diskuze-oznameni-a-novinky/core-one-indx-tool-offset-out-of-bounds-36130-loadcell-test-issue/
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
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5548
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5526
  - https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/gantry-squaring-failing/
  - https://help.prusa3d.com/downloads/core-one-indx
superseded_by:
source_sha:   59c45ee96eeab8dfb68f6c5b74a54cc6c04e269bcb3aa13f2ea9b0dcc8e41c2e
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
vollständig behoben war. Besitzer haben seither weitere Quellen benannt, darunter die
Verkabelung der Bettheizung und die LED-Statusleiste; sie werden unten behandelt und
sind schwächer belegt. Ein Selbsttest der Wägezelle, der direkt nach einem
Werkzeugwechsel Rauschen meldet (möglicherweise auch nach einem, den der Test selbst
vornimmt), kann eine andere Sache sein: Rauschen vom Extrudermotor, das ein Issue darauf
zurückführte, dass der Motor nach einem Werkzeugwechsel eingeschaltet bleibt, und das
ein zweites unter 7.0.0 gemessen hat. Lesen Sie dazu den Abschnitt unten, bevor Sie
dafür Hardware kaufen.

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
- Eine Werkzeug-Offset-Kalibrierung, die beim Start eines Drucks fehlschlägt, aber
  besteht, wenn sie für sich allein aus dem Menü gestartet wird. Besitzer beschreiben
  sowohl die Heizungen als auch die LED-Statusleiste beim Lauf aus dem Menü als
  ausgeschaltet, daher passt dieses Muster zu mehr als einer Quelle; siehe den
  Abschnitt zu weiteren Quellen weiter unten
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
erprobtes Ergebnis.

Ein getrenntes Issue, [#5548](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5548),
berichtet denselben Effekt unter 7.0.0, vom Besitzer einer weiteren Gen-2-Maschine mit
acht Werkzeugen. Nach einer gewöhnlichen Werkzeugaufnahme meldet der Selbsttest dort oft
Rauschen, ohne dass jemand die Düse berührt; ein erneuter Versuch kann minutenlang
verrauscht bleiben, während Abbrechen und ein frisch gestarteter Test ihn ruhig machen
können. Bei stillstehendem Kopf mit kaltem Werkzeug und ohne eingeschaltete Heizung
zeichnete der Besitzer die Wägezelle auf, während der Extrudermotor erst aus-, dann ein-
und dann wieder ausgeschaltet war: Bei eingeschaltetem Motor war das Rauschen etwa
dreimal so hoch.

Ob derselbe Motor auch das Abtasten beim Start eines Drucks stört, ist offen. Der
Abtastcode schaltet den Motor zuvor aus, und doch haben Besitzer in beiden Issues erlebt,
dass das Abtasten beim Druckstart direkt nach einer Werkzeugaufnahme fehlschlug. Der
erste Berichtende sah die Werkzeug-Offset-Kalibrierung fehlschlagen, wenn ihr ein
Werkzeugwechsel vorausging, und brachte Drucke in Gang, indem er vor dem Druck das
Startwerkzeug auswählte und eine Referenzfahrt ausführte. Der Besitzer, der den Kopf
gehört hatte, bekam später vom Prusa-Support ein Ersatzkabel für den Kopf, was nichts
änderte; er startet Drucke inzwischen so: das erste Werkzeug über das Menü Steuerung
(Control) von Hand aufnehmen, den Wägezellentest starten, ihn nach dem Fehlschlag
abbrechen und erst dann den Druck starten, sodass unmittelbar vor der Referenzfahrt keine
Aufnahme mehr erfolgt. Beim Besitzer unter 7.0.0 brechen Drucke beim Abtasten des
Offset-Sensors mit der Wägezelle mit 36130 ab; der Motor war nach Abschluss der
Düsenreinigung aus, seinen Zustand während des fehlschlagenden Abtastens konnte der
Besitzer aber nicht aufzeichnen. Keiner von ihnen hat gezeigt, dass dort der Motor die
Ursache ist, und der erste Berichtende sagt das auch selbst. Der Besitzer unter 7.0.0
hat das Makro für die Düsenreinigung durch eine eigene Fassung auf dem USB-Stick
ersetzt, die den Motor vor diesem Abtasten ausschaltet, und dem Start-G-Code Zeilen
hinzugefügt, die den Treiber danach wiederherstellen; er berichtet von weit weniger
fehlgeschlagenen Starts, wenn auch nicht von keinen mehr. Das Makro schreibt die
Konfiguration des Motortreibers direkt, niemand sonst hat es geprüft, und es wird hier
nicht wiedergegeben.

Der Effekt auf den Selbsttest stützt sich nun auf zwei getrennte Issues und ist damit
`reported`. Die Lesart des Codes dahinter stammt vom ersten Berichtenden und von dieser
Seite, nicht von Prusa, und die Verbindung zu Fehlschlägen beim Druckstart ist
`provisional`. Prusa hatte bis zum oben genannten Datum in keinem der beiden Issues
geantwortet. 6.9.2 ändert über Filament-Voreinstellungen hinaus nichts, was einen INDX
betrifft, und die
[Release Notes zu 7.0.0](https://help.prusa3d.com/downloads/core-one-indx) nennen keine
Änderung am Wägezellen-Selbsttest oder am Extrudermotor nach einem Werkzeugwechsel; das
zweite Issue zeigt den Effekt unter 7.0.0.
In der Praxis: Meldet der
Selbsttest nach einem Werkzeugwechsel Rauschen, oder wenn der Test zuerst ein Werkzeug
aufnehmen musste, führen Sie eine Referenzfahrt aller Achsen aus, nicht nur in X und Y,
oder brechen Sie den Test ab, und starten Sie ihn erneut, bevor Sie eine Störung oder
die Wägezelle verdächtigen.

Ob ein verrauschter Selbsttest auch verrauschtes Abtasten bedeutet, ist nicht geklärt.
Der zweite Besitzer der beiden früheren Berichte und ein dritter, in
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
diesem Grund fehlschlägt, bedeutet also für sich genommen nicht, dass das Abtasten
verrauscht ist, auch wenn die Berichte zum Druckstart oben das offenlassen. Keiner der
beiden Besitzer hat geprüft, ob dies auf den eigenen Drucker zutraf.

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

### Weitere Quellen, die Besitzer gefunden haben

Ein Ferrit am Hauptkabel des Werkzeugkopfs behandelt einen Weg, auf dem die Störung
eindringt. Besitzer im
[Thread zur Werkzeug-Offset-Kalibrierung](https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/tool-offset-calibration-failing/)
und in [#5526](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5526) haben seither
weitere gefunden. Jede stützt sich auf wenige Besitzer, von denen die meisten mehrere
Dinge gleichzeitig geändert haben; alle sind daher `provisional`.

- **Die Verkabelung der Bettheizung.** Ein Besitzer, dessen INDX schon beim allerersten
  Druck an der Werkzeug-Offset-Kalibrierung scheiterte, nahm die beiden Heizleitungen im
  Kabelkasten auf der Rückseite aus dem Hauptbündel heraus (nach der beschriebenen
  Führung offenbar die der Bettheizung), verdrillte sie miteinander und setzte
  Ferritdrosseln dort, wo sie an die Controllerplatine gehen, gleichzeitig mit Drosseln
  an den Kabeln von Werkzeugkopf und Offset-Sensor; seitdem funktioniert es. Ein anderer
  Besitzer, dessen Wägezellen-Selbsttest zeitweise Rauschen mit scharfen Spitzen im
  Balkendiagramm meldete, verdrillte die Leitungen der Bettheizung, setzte Drosseln an
  sie und an den Kabelbaum des Werkzeugkopfs und hielt die Kabel getrennt und frei von
  Schleifen; danach beruhigte sich der Test, und die Fehlschläge hörten auf.
- **Die Stromleitungen des Werkzeugkopfs.** Ein dritter Besitzer verdrillte die Plus- und
  Masseleitungen des INDX-Kabelbaums zum Werkzeugkopf auf der ganzen Länge paarweise,
  wofür die Kontakte am Stecker auf der Controllerseite einzeln gelöst werden mussten;
  das beseitigte die meisten seiner Kalibrierfehler. Ein Kontakt, der an der falschen
  Position wieder eingesetzt wird, kann die Elektronik beschädigen; das ist also kein
  erster Schritt. Der Abschnitt „Details“ oben sagt, das Leistungspaar im Kabelbaum sei
  verdrillt; dieser Besitzer verdrillte die Paare selbst, was nahelegt, dass sie bei ihm
  nicht verdrillt waren, während der zweite Besitzer oben seine als bereits verdrillt
  beschreibt; die Kabelbäume können sich also unterscheiden.
- **Die LED-Statusleiste.** In
  [#5526](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5526) führte ein
  Besitzer unter 6.9.1 Fehlschläge der Werkzeug-Offset-Kalibrierung während Drucken auf
  die RGB-Statusleiste zurück, den LED-Streifen, dessen Farbe dem Zustand des Druckers
  folgt; er nennt ihn die Bett-LED. Das Wägezellenrauschen stieg, sobald der Streifen
  leuchtete, und fiel wieder, wenn er dunkel wurde. In diesem Bericht schlug die
  Kalibrierung innerhalb eines Drucks fehl, wo der Streifen leuchtet, und bestand, wenn
  sie aus dem Menü gestartet wurde, wo er es nicht tut. Ein großer Teil der Tests dieses
  Besitzers lief auf einer selbst veränderten Firmware, auf die sich diese Seite nicht
  stützt. Der Besitzer, der die Stromleitungen des Werkzeugkopfs verdrillt hatte, hatte
  unter der unveränderten 6.9.2 danach noch gelegentlich einen Fehlschlag; das
  Ausschalten des Streifens (die Option RGB Status Bar, in den Einstellungen oder während
  eines Drucks unter Tune > Lights) beendete das, und später setzte er Ferritperlen auf
  die Kabel sowohl der Bett-LED als auch der Kammerbeleuchtung und hat seitdem keine
  Probleme mehr. Ein weiterer Besitzer schaltete die LEDs aus und setzte gleichzeitig
  Ferrite auf jedes Kabel, das er erreichen konnte, und auch seine Fehlschläge hörten auf.
  Den Streifen auszuschalten kostet nichts und lässt sich leicht rückgängig machen; das
  macht es zu einem günstigen Test, bevor Sie die Verkabelung öffnen.

Das Muster, im Druck fehlzuschlagen und aus dem Menü zu bestehen, passt sowohl zu den
Heizungen als auch zum Streifen, weil Besitzer beide beim Lauf aus dem Menü als
ausgeschaltet beschreiben; der Besitzer, der die Stromleitungen verdrillt hatte, deutete
es zunächst als Störung durch die Heizung. Außerhalb der eigenen Tests des Besitzers mit
dem Streifen hat niemand die beiden an einer Maschine auseinandergehalten.

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
    [führte das Problem schließlich auf ein defektes Teil zurück](https://forum.prusa3d.com/forum/ceske-forum-obecna-diskuze-oznameni-a-novinky/core-one-indx-tool-offset-out-of-bounds-36130-loadcell-test-issue/),
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
    betrifft die Motorströme; ein Prusa-Entwickler erklärte später in
    [#5520](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5520), sie solle
    verhindern, dass bei manchen Druckern die Riemen beim Homing durchrutschen, weil der
    Motor, der die Position hält, dem anschlagenden Motor nicht standhalten konnte. Die
    [Release Notes](https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.9.1)
    nennen keine Achse, doch die einzige Änderung an Motorströmen im Firmware-Repository
    zwischen der Beta und der stabilen Version
    ([Vergleich](https://github.com/prusa3d/Prusa-Firmware-Buddy/compare/v6.9.1-beta...v6.9.1))
    betrifft das diagonale XY-Homing, nicht das Z-Abtasten mit der Wägezelle. Die Notes
    sagen zudem nichts über die Wägezelle oder das Heizelement; das ist also ein von
    dieser Seite getrennter Fehler und keine Behebung für ihn. Passen Ihre Homing-Fehler
    zu dieser Beschreibung statt zum Muster oben — Fehlschlag nur bei heißem Hotend, die
    Düse hält sichtbar vor der Druckplatte an —, aktualisieren Sie die Firmware, bevor
    Sie einen Ferrit anbringen, lesen Sie aber zuerst den nächsten Absatz. Das stützt
    sich allein auf die Release Notes, das Firmware-Repository des Herstellers und diese
    Erklärung, `provisional`: Bisher hat kein Besitzer berichtet, dass die Korrektur
    seine Homing-Fehler behoben hat.

    Besitzer berichten von etwas, das wie eine Nebenwirkung derselben Änderung aussieht,
    in [#5520](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5520), in einem
    [Forumsthread](https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/homing-shows-early-endstop-detected-message/)
    und in [einem weiteren](https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/gantry-squaring-failing/):
    Seit 6.9.1 zeigt das Homing mehrmals die Meldung `Endstop early trigger` und dauert
    länger. Bei manchen wird es trotzdem abgeschlossen, und Drucke laufen normal; bei
    anderen schlägt die Homing-Kalibrierung fehl, was die Einrichtung stoppt. Die
    Homing-Kalibrierung nach dem Update erneut auszuführen, Prusas erster Vorschlag, half
    nicht; die Rückkehr zur 6.9.1-Beta oder zu 6.9.0 beendete es bei jedem Besitzer,
    der berichtet, es versucht zu haben, und mehrere führten danach die
    Homing-Kalibrierung erneut aus. Prusa gibt an, dies an den Druckern, an denen die
    Änderung getestet wurde, nicht gesehen zu haben, hat erklärt, den Berichten
    nachzugehen, und hat Besitzer, die es betrifft, gebeten, vorerst bei der früheren
    Firmware zu bleiben; der Kommentar nennt 6.9.1, während die Besitzer zur 6.9.1-Beta
    oder zu 6.9.0 zurückgekehrt waren. Mit beiden verzichtet man auch auf den
    Assistenten zur Rechtwinkligkeit des Portals, der laut dem Vergleich oben erst nach
    der Beta hinzukam. Zwei Besitzer sagen, dass sich 7.0.0 genauso verhält, und die
    [Release Notes zu 7.0.0](https://help.prusa3d.com/downloads/core-one-indx) nennen
    keine Änderung an den Homing-Strömen. Im
    [Quellcode von 6.9.1](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/lib/Marlin/Marlin/src/module/prusa/homing_corexy.cpp)
    kennzeichnet diese Meldung eine Messfahrt beim X/Y-Homing, die zu früh angehalten hat
    und wiederholt wird; die Messung gibt erst auf, wenn die Wiederholungen ausgeschöpft
    sind. Sie stammt vom X/Y-Homing, nicht von der Wägezelle, und ist kein Zeichen einer
    Störung. Mehrere Besitzer, im Issue und in zwei getrennten Forumsthreads, machen die
    Meldung und die Wirkung der Rückkehr zu `reported`; dass der niedrigere Strom sie
    verursacht, ist eine Schlussfolgerung.

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
    also auch nichts an dem, was diese Seite beschreibt.
    [7.0.0](https://help.prusa3d.com/downloads/core-one-indx), veröffentlicht am
    2026-10-15, nennt nichts dazu, wie das Wägezellensignal gefiltert oder bewertet
    wird, und ebenso wenig zum Selbsttest, zum Extrudermotor nach einem Werkzeugwechsel
    oder zur Statusleiste. Prusa hatte den Quellcode bis zum oben genannten Datum nicht
    auf GitHub veröffentlicht; was die Version ändert, ist also nur aus diesen Notes und
    von Besitzern bekannt: Der Effekt des Extrudermotors wurde unter ihr gemessen. Wenn
    Sie dies deutlich nach dem oben genannten Datum lesen, prüfen Sie, ob eine neuere
    Firmware das Problem behoben hat, bevor Sie Hardware ergänzen.

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
nachstellen. Der Effekt des Extrudermotors auf den Selbsttest findet sich inzwischen in
zwei getrennten Issues, eines davon unter 7.0.0, und ein weiterer Besitzer im ersten
bestätigt den Teil mit Abbrechen und zweitem Versuch; der Firmware-Quellcode ist damit
vereinbar, aber Prusa hat ihn nicht bestätigt, keiner der beiden früheren Besitzer hat
ihn geprüft, und seine Verbindung zu Fehlschlägen beim Druckstart ist unbewiesen. Die
Referenzfahrt vor dem zweiten Versuch, die
Prüfung mit wiederholtem Mesh, die Reklamation beim Hersteller und der Fall der Werkzeugerkennung
unter „Verwandte Seiten“ sind jeweils ein einzelner Bericht. Keiner dieser Besitzer hat
einen Ferrit angebracht; sie stärken oder schwächen die Argumente dafür also nicht. Die
Verkabelung der Bettheizung und die Stromleitungen des Werkzeugkopfs stammen aus einem
Forumsthread, die Statusleiste aus einem Issue und demselben Thread, wobei die Tests des
ersten Besitzers teils auf veränderter Firmware liefen; die Besitzer haben meist mehrere
Dinge gleichzeitig geändert. Die Homing-Meldung zum frühen Auslösen berichten mehrere
Besitzer in einem Issue und zwei Forumsthreads. Die Homing-Korrektur stützt sich auf die
Release Notes, das Firmware-Repository des Herstellers und die Erklärung eines
Entwicklers, nicht auf Berichte von Besitzern.

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
