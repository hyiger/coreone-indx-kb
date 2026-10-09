---
title:        Dock-Kalibrierung lehnt einige oder alle Docks ab
confidence:   reported
updated:      2026-10-08
author:       hyiger
printer:      Core One, Core One+, Core One+ (Gen 2)
toolhead:     INDX
hotend:       unknown
nozzle:       unknown
firmware:     6.9.0, 6.9.1-beta, 6.9.1
sources:
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5444
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5445
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5491
  - https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/toolhead-docking-calibration-fails/
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/coreone-with-mmu-upgrade-to-indx/
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/lib/Marlin/Marlin/src/module/prusa/indx_dock_position_defaults.hpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/lib/Marlin/Marlin/src/module/prusa/toolchanger_utils.h
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/lib/Marlin/Marlin/src/module/prusa/toolchanger_utils_indx.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/src/feature/indx_dock_calibration/indx_dock_calibration.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/src/feature/indx_dock_calibration/screen_dock_calibration.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/src/common/printer_variant/coreone.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/src/common/printer_variant/coreone.hpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.0/src/common/printer_variant/coreone.hpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/src/persistent_stores/store_instances/config_store/store_definition.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/src/gui/screen_printer_setup.hpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/src/gui/MItem_hardware.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/src/feature/indx_gantry_squareness/indx_gantry_squareness.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/src/feature/indx_gantry_squareness/indx_gantry_squareness.hpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/src/feature/indx_gantry_squareness/screen_gantry_squareness.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.9.1
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.9.2
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/compare/v6.9.1...v6.9.2
superseded_by:
source_sha:   417723c49da6f26025b89ac5a80dc34ccfba2f51d9ea6aa613bf27ddead946d5
---
# Dock-Kalibrierung lehnt einige oder alle Docks ab

!!! warning "Eine Ursache ist zweifach bestätigt; die übrigen stützen sich auf eine Maschine oder einen Thread"
    Eine Riemeneinstellung, die nicht zu den eingebauten Riemen passt, hat die
    Dock-Kalibrierung an zwei Maschinen an einem großen, unveränderlichen Fehler in Y
    scheitern lassen, gemeldet an zwei voneinander unabhängigen Stellen: in einem Bericht
    an jedem Dock, im anderen als Y-Messwert, der sich nicht verändern ließ. Die
    Einstellung zu korrigieren, direkt oder über die Druckervariante, behob beides. Dieser
    Teil ist `reported`. Eine Dock-Reihe, die nur an einem Ende scheitert und einem
    schiefen Portal zugeschrieben wird, stammt von einer einzigen, ungelösten Maschine.
    Die Behebung durch Nachspannen zu lockerer Riemen stützt sich auf einen Besitzer, und die Hinweise
    zu Riemen und Homing bei einem scheiternden ersten Dock stammen aus einem einzigen
    Forenthread. Diese Teile sind `provisional` und dort markiert, wo sie vorkommen.

## Zusammenfassung

Die Dock-Kalibrierung misst, wo jedes Dock tatsächlich sitzt, und akzeptiert die Messung
nur, wenn sie in ein enges Fenster um eine in die Firmware einkompilierte Position fällt.
Sie speichert die gemessene Position jedes Docks, aber nur, wenn diese innerhalb des
Fensters liegt; an eine Maschine, deren Docks außerhalb davon sitzen, kann sie sich also
nicht anpassen. Werden Docks abgelehnt, liegt der Hinweis deshalb darin, *welche* Docks
scheitern und in welche Richtung:

- **Docks in Y um denselben Betrag daneben** — oder nur das erste Dock, wenn die
  Kalibrierung nie weiter kommt. X lag in beiden Berichten innerhalb der Toleranz (in
  #5444 an jedem Dock). Prüfen Sie, ob die Einstellung **1.5GT Belts** des Druckers zu
  den tatsächlich eingebauten Riemen passt. Zwei Besitzer behoben es, indem sie die
  Riemeneinstellung an die Hardware anglichen, einer direkt und einer über die
  Druckervariante. Ein dritter, mit einer kleineren gleichmäßigen Verschiebung in die
  andere Richtung, behob es stattdessen durch Nachspannen zu lockerer Riemen (ein
  Besitzer, `provisional`).
- **Der Fehler wächst stetig entlang der Reihe, sodass nur die Docks an einem Ende
  scheitern.** Die Reihe ist gerade, aber gegenüber der X-Achse verdreht. Ein
  Prusa-Entwickler vermutet ein nicht rechtwinkliges Portal; der eine Besitzer mit diesem
  Muster hat es nicht gelöst. `provisional`.
- **Das erste Dock scheitert, und sonst wirkt nichts falsch.** Besitzer in einem Thread
  verweisen auf lockere Riemen, die Rechtwinkligkeit des Portals und die
  Homing-Kalibrierung. `provisional`.

## Fehlercodes, die hierher führen

| Code | Anzeige am Drucker |
|---|---|
| [`36136`](https://help.prusa3d.com/article/calibrate-dock-from-menu-17136-xl-36136-core-one-indx_1037195) | Calibrate dock from menu |

`36136` fordert Sie auf, die Dock-Kalibrierung aus dem Menü Calibrations zu starten.
Lehnt diese Kalibrierung dann ein Dock ab, sind Sie auf dieser Seite richtig.

## Im Einzelnen

### Wogegen die Kalibrierung prüft

Die Firmware hält für jedes Dock eine erwartete Position vor: ein eigenes X für jedes
Dock und an der Core One ein einziges Y, das alle gemeinsam nutzen. Die Core One L hat
eigene Werte, und der Quellcode vermerkt, dass ihr Y noch an weiteren Druckern validiert
werden muss.

Während der Dock-Kalibrierung lässt eine Messung außerhalb eines festen Fensters um die
erwartete Position das betreffende Dock scheitern. Der Fehlerbildschirm zeigt den
gemessenen und den erwarteten Wert und bietet einen erneuten Versuch an. Ohne erneuten
Versuch wird das Dock als nicht kalibriert markiert, sein Werkzeug deaktiviert, und der
Assistent endet an dieser Stelle, sodass alle späteren Docks ungemessen bleiben. Eine
Messung innerhalb des Fensters wird gespeichert und fortan verwendet. Unabhängig davon
hält die Firmware mit einem Werkzeugwechsler-Fehler an, statt eine gespeicherte
Dock-Position zu verwenden, die außerhalb des Fensters liegt.

TODO(verify): die erwarteten Dock-Positionen und die Breite des Akzeptanzfensters. Die
erwarteten Positionen sind Konstanten zur Kompilierzeit in
indx_dock_position_defaults.hpp; das Fenster, ein Versatz je Achse plus ein Spielraum
für Rundungen in der Anzeige, steht in toolchanger_utils.h. Beides wurde beim Git-Tag
6.9.1 gelesen und bleibt zurückgehalten, bis es an einer Maschine geprüft ist.

Daraus folgen zwei Dinge. Eine Maschine, deren Docks alle um denselben Betrag verschoben
sind, kann nicht bestehen, so genau sie diese auch misst. Und weil ein einziges Y für
alle Docks gilt, scheitert eine Reihe, die vollkommen gerade, aber leicht verdreht ist,
nur an dem Ende, das am weitesten von der erwarteten Linie entfernt liegt.

Die Messung des Assistenten deckt sich mit einer Gegenprobe: Im ersten Bericht unten
stimmte eine Prüfung von Hand eng mit ihr überein. In jenem Fall wurden beide allerdings
mit derselben falschen Riemenskalierung vorgenommen; die Übereinstimmung schließt also
einen Messfehler aus, nicht aber einen Konfigurationsfehler.

Der Melder des ersten Falls sagt, die Maschine habe weder andere Kalibrierungen ausführen
noch drucken können, solange die Docks abgelehnt blieben. Das ist ein einzelner Bericht;
dass die Firmware das Werkzeug eines nicht kalibrierten Docks deaktiviert, passt dazu.

### Docks in Y um denselben Betrag abgelehnt: die Riemeneinstellung

An einer ursprünglichen, mit dem INDX-Kit umgebauten Core One wurde jedes Dock in Y um
dieselbe Strecke zu kurz gemessen, während X an jedem Dock innerhalb der Toleranz lag
([#5444](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5444)). Ein Zurücksetzen
auf Werkseinstellungen und ein frisches Flashen änderten nichts. Ein Prusa-Entwickler
nannte die Riemeneinstellung als wahrscheinliche Ursache, und so erwies es sich: Die
Maschine hatte die älteren 2GT-Riemen, während die Firmware auf 1.5GT eingestellt war.
Nachdem die Einstellung passend geändert und die Dock-Kalibrierung erneut ausgeführt
worden war, bestand jedes Dock.

Der Besitzer erklärt, warum das Zurücksetzen nicht half: Der Einrichtungsassistent fragt
erneut, welche Druckervariante man hat, und dieselbe Antwort stellte dieselbe
Riemeneinstellung wieder her. Prusas Firmware-Quellcode passt zu dieser Darstellung.
Sein Bildschirm für die Druckereinrichtung führt die Variante und, getrennt davon, die
Riemeneinstellung auf, und beide sind aneinander gekoppelt: Von den drei
Core-One-Varianten (Core One, Core One+ und Core One+ Gen2) schaltet nur die
Gen2-Variante die 1.5GT-Riemeneinstellung ein, zusammen mit weiteren Merkmalen dieser
Ausführung, und die Wahl einer der beiden früheren Varianten schaltet sie aus.
Standardmäßig setzt die Firmware beim ersten Start und nach einem Zurücksetzen auf
Werkseinstellungen, das die Hardwarekonfiguration löscht, die Gen2-Variante, sowohl beim Git-Tag 6.9.0 als auch bei 6.9.1, was
zu der unten wiedergegebenen Bemerkung des Entwicklers passt, der Standard sei 1.5GT.
Eine Maschine ohne das Gen-2-Upgrade muss nach jedem Zurücksetzen wieder umgestellt
werden.

Warum der Fehler in Y auftritt: Die Riemeneinstellung ändert die Schritte pro Millimeter
für X und Y, mit denen die Firmware rechnet, sodass auf den falschen Riemen jede
Bewegung um einen kleinen festen Prozentsatz skaliert wird. Der Fehler wächst mit dem
Abstand von der Home-Position, und die Docks sitzen am fernen Ende des Y-Verfahrwegs. Ein
gleich großer Y-Fehler an jedem Dock ist das Erkennungsmerkmal. Die Einstellung ändert
auch die X-Schritte, doch #5444 fand X an allen fünf Docks innerhalb der Toleranz; ein
X-Fehler gehört also nicht zum gemeldeten Erkennungsmerkmal.

In beiden Berichten war die 1.5GT-Einstellung aktiv, obwohl 2GT-Riemen eingebaut waren.
Der Kopf fährt dann weiter, als die Firmware zählt, und die Docks werden vor ihrem
erwarteten Y gemessen, näher an der Home-Position. Nach derselben Rechnung lägen sie bei
der umgekehrten Fehlkombination jenseits davon; das ist ein Schluss dieser Seite, und
keiner der beiden Berichte deckt diesen Fall ab.

TODO(verify): wie groß diese gleichmäßige Verschiebung an den Docks ist. In #5444 wird
ein Wert durchgerechnet; er bleibt als Betrag eines Versatzes zurückgehalten, bis er hier
gemessen ist.

Ein zweiter Besitzer stieß in einem davon unabhängigen Forenthread auf dieselbe Hürde:
Das Andocken scheiterte mit einem Y-Messwert, der sich durch nichts, was er versuchte,
verändern ließ, und der Wert, den er nennt, ist im Wesentlichen der aus #5444
([Docking-Kalibrierung des Werkzeugkopfs schlägt fehl](https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/toolhead-docking-calibration-fails/)).
Sein Drucker war als Gen-2-Maschine konfiguriert, obwohl noch keines der Gen-2-Teile, zu
denen die neueren Riemen gehören, eingebaut war. Die Wahl einer Druckervariante ohne
Gen 2 in den Systemeinstellungen, die laut dem oben genannten Quellcode auch die
1.5GT-Riemeneinstellung ausschaltet, ließ die Dock-Kalibrierung bestehen, beim zweiten
Durchlauf. Der Wechsel der Variante schaltete mit der Riemeneinstellung auch die übrigen
Gen-2-Merkmale aus und hebt deshalb für sich genommen die Riemen nicht als Ursache
hervor; erst die Übereinstimmung des Y-Werts mit #5444 weist auf sie hin.

Er glaubt, das Flashen der Firmware für den Umbau habe die Konfiguration von selbst auf
Gen 2 umgestellt. Ein weiterer Besitzer erlebte in
[einem anderen Thread](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/coreone-with-mmu-upgrade-to-indx/)
dasselbe direkt nach dem Flashen der INDX-Firmware: Der Drucker hatte angenommen, die
Gen-2-Riemen seien eingebaut — in seinem Fall zu Recht, auch wenn der Drucker das nicht
wissen konnte. Prusas Quellcode setzt beim ersten Start die Gen2-Variante, was beides
erklären würde. Dass das Flashen der INDX-Firmware als erster Start zählt, ist aus dem
Quellcode erschlossen, nicht bestätigt.

**Welche Riemen haben Sie?** Das Gen-2-Upgrade bringt die 1.5GT-Riemen mit. Laut dem
Prusa-Entwickler in #5444 ist die Firmware standardmäßig auf 1.5GT eingestellt, und eine
Core One+ ohne das Gen-2-Upgrade hat höchstwahrscheinlich 2GT; die ursprüngliche Core One
in jenem Bericht hatte ebenfalls 2GT. Zählen Sie im Zweifel die Zähne auf einer
abgemessenen Länge: Ein 1.5GT-Riemen hat auf derselben Strecke ein Drittel mehr Zähne
als ein 2GT-Riemen.

Der Drucker selbst warnt beim Ändern der Einstellung, dass die falsche Wahl Maß- und
Homing-Fehler verursacht und dass einige Kalibrierungen zurückgesetzt werden. Prusas
Quellcode zeigt, welche: Die Änderung setzt die Ergebnisse von Homing, Riemenabstimmung,
Rechtwinkligkeit des Portals und X/Y-Achsen-Selbsttest zurück. Starten Sie also neu,
wenn der Drucker Sie dazu auffordert, und führen Sie dann die Kalibrierfolge von Anfang
an erneut aus, statt nur die Dock-Kalibrierung. Dieselbe Einstellung ist auch bei der
Werkzeug-Offset-Kalibrierung das Erste, was auszuschließen ist; siehe
[Werkzeug-Offset-Kalibrierung schlägt fehl](offset-sensor-board-failure.md).

**Nicht jede gleichmäßige Verschiebung ist die Riemeneinstellung.** `provisional` — ein
Besitzer. Im selben Forenthread behob ein Besitzer, dessen Docks alle um einen kleineren,
gemeinsamen Betrag in Y danebenlagen, und zwar jenseits des erwarteten Y statt davor, das
Problem, indem er viel zu lockere Riemen nachspannte; eine Änderung der
Riemeneinstellung erwähnt er nicht. Seine Riemen klangen schon im lockeren Zustand in
der richtigen Tonhöhe. Er spannte sie deutlich darüber hinaus, wechselte dann zwischen
dem Rechtwinkligstellen des Portals und dem erneuten Abstimmen der Riemen ab, bis keines
das andere mehr störte, und führte schließlich jede Kalibrierung von Anfang an erneut
aus, wonach die Dock-Kalibrierung bestand. Das ist die Methode eines Besitzers, nicht
Prusas Verfahren: Folgen Sie Prusas Anleitung zur Riemenspannung, und spannen Sie die
Riemen nicht zu stark.

### Fehler, der entlang der Reihe wächst: eine verdrehte Dock-Linie

`provisional` — eine Maschine, ungelöst.

An einer Core One+ (Gen 2) mit acht Docks unter 6.9.1-beta gibt der Besitzer an, dass die
Riemeneinstellung für seine Gen-2-Riemen korrekt war und dass sich drei Durchläufe je
Dock fast exakt wiederholten
([#5491](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5491)). Das gemessene Y
wanderte stetig vom ersten bis zum letzten Dock, auf einer nahezu perfekten Geraden. Die
letzten beiden Docks fielen aus dem Fenster, und das davor lag auf dessen Rand. Der
Besitzer prüfte die Werkzeughalter, und jedes Dock saß auf derselben Linie, was ein
einzelnes verschobenes Dock ausschließt.

Der Besitzer hatte die Rechtwinkligkeit zunächst durch Ausmessen gedruckter Quadrate
ausgeschlossen, aber schon vor Prusas Antwort bemerkt, dass eine Seite selbst bei
nominell rechtwinkligem Portal weiter außen saß. Ein Prusa-Entwickler deutete es als
nicht rechtwinkliges Portal und verwies auf den in 6.9.1 neuen Assistenten zur
Rechtwinkligkeit des Portals. An dieser Maschine ausgeführt, meldete der Assistent eine
Schiefstellung weit außerhalb der Toleranz, die der Entwickler daraufhin nannte und
oberhalb derer das Homing unzuverlässig werden soll. Der Besitzer sagt, das Portal nach
der Anleitung rechtwinklig auszurichten lasse die Portalkalibrierung scheitern, während
ein Verziehen, bei dem eine Seite einen Spalt zeigt, diese bestehen lasse und alles
andere zunichtemache. Nach Wochen mit dem Support war es am 29. September 2026 noch
immer ungelöst.

Am 8. Oktober 2026 meldete sich der Entwickler mit Rückfragen statt mit einer Lösung. Er
fragte, was der Besitzer mit einer scheiternden Portalkalibrierung meine, sagte, er
könne nicht nachvollziehen, wie ein verzogenes Portal sie bestehen lassen sollte, und
fragte, ob vor der Prüfung der Rechtwinkligkeit die Düsen aus den Docks 1 und 8 genommen
worden seien, wie es der Assistent verlangt. Als diese Seite aktualisiert wurde, stand
die Antwort des Besitzers noch aus.

TODO(verify): die Toleranz für die Rechtwinkligkeit des Portals, die der Prusa-Entwickler
in #5491 nannte. Der Assistent in 6.9.1 prüft gegen denselben Wert, eine Konstante in
indx_gantry_squareness.hpp, die auch sein Ergebnisbildschirm anzeigt. Als
Montageeinstellung zurückgehalten.

Wie der Assistent misst, ist für diesen Austausch von Belang. Laut Prusas Quellcode in
6.9.1 führt er zuerst ein Homing aus, fährt dann den leeren Kopf in die beiden äußersten
Docks, bis er blockiert, und wertet den Unterschied der beiden Haltepunkte in Y als
Schiefstellung. Er verlangt, dass die Docks 1 und 8 vorher geleert werden. Schlägt die
Messung selbst fehl, fordert er dazu auf, das zu prüfen; eine Schiefstellung über der
Grenze beantwortet er dagegen mit der Aufforderung, das Portal nach der Anleitung
auszurichten. Daraus folgt, dass der Assistent die Rechtwinkligkeit an der Dock-Reihe
misst: Er erfasst dieselbe Neigung, die die Dock-Kalibrierung ablehnt, und kann für sich
genommen ein schiefes Portal nicht von einer Dock-Reihe unterscheiden, die gegenüber
einem rechtwinkligen Portal aus der Linie liegt. Lägen die Docks dieser Maschine aus der
Linie, würde ein nach der Anleitung rechtwinklig ausgerichtetes Portal den Assistenten
scheitern lassen und ein den Docks folgend verzogenes ihn bestehen lassen, was zur
Schilderung des Besitzers passt, sofern mit der von ihm erwähnten Portalkalibrierung
dieser Assistent gemeint ist; um genau diese Klarstellung hat der Entwickler gebeten.
Das ist die Lesart dieser Seite aus dem Quellcode, nicht Prusas Erklärung, und niemand
hat sie an der Maschine geprüft.

Der Besitzer hat Prusa gebeten, Docks gegen eine Linie zu validieren, die durch die
gemessenen Docks gelegt wird, statt gegen ein festes Y, sodass eine gleichmäßig verdrehte
Reihe bestehen könnte, während ein einzelnes verschobenes Dock weiterhin auffiele. Diese
Anfrage ist offen und als INDX-Erweiterung gekennzeichnet, ohne Zusage von Prusa.

### Das erste Dock scheitert, sonst ist nichts offensichtlich falsch

`provisional` — mehrere Besitzer, aber alle in einem Forenthread.

[Derselbe Forenthread](https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/toolhead-docking-calibration-fails/)
sammelt die Ratschläge der Besitzer und die Lösungen, die funktionierten:

- **Beim manuellen Schritt** sollte der Kopf das Werkzeug vollständig umschließen, mit
  bündigen vorderen Flächen, und Sie sollten ihn beim ersten Tastendruck weiterhin dort
  halten.
- **Nichts im Weg**: der Zaun („Fence“) bündig mit dem Rahmen,
  der Abfallbehälter frei und der volle Verfahrweg für den Kopf verfügbar.
- **Riemen und Homing.** Ein weiterer Besitzer, der vermutlich dieselbe Kalibrierung
  beschreibt (er nennt sie Werkzeugkalibrierung), brachte sie erst nach weiterer Arbeit
  an den Riemen und einer erneuten Homing-Kalibrierung zum Bestehen. Der Bericht über die
  lockeren Riemen oben stammt ebenfalls aus diesem Thread.
- **Das Abstimmwerkzeug.** Ein Besitzer sagt, Prusas App zur Riemenabstimmung gebe für
  INDX-Riemen, ob Gen 2 oder nicht, keine Zielwerte vor, sodass die Spannung durch
  Ausprobieren eingestellt werde; ein anderer fand, dass die App mit den ursprünglichen
  Riemen funktionierte, war sich aber unsicher, ob ihre Zielwerte zu den neueren passen.

Ein Besitzer schrieb am 30. September 2026, dass fünf Versuche, die Riemen neu
abzustimmen, das Portal neu auszurichten und die Homing-Kalibrierung erneut auszuführen,
das Y des ersten Docks nicht in den zulässigen Bereich gebracht hätten; eine Antwort gibt
es bisher nicht. Ob er die weiter oben im selben Thread angesprochene Riemeneinstellung
geprüft hat, sagt er nicht.

## Was zu tun ist

**Gerade die INDX-Firmware geflasht?** Prüfen Sie an einer Maschine ohne die
Gen-2-Riemen die Einstellung **1.5GT Belts**, bevor Sie irgendeine Kalibrierung
ausführen.

**Lesen Sie die Werte ab, bevor Sie etwas ändern.** Der Fehlerbildschirm zeigt die
gemessene und die erwartete Position des abgelehnten Docks. Notieren Sie, welche Docks
scheitern und wie weit jedes in X und in Y danebenliegt. Das Muster verweist weit besser
auf die Ursache als jeder einzelne Messwert.

**Docks in Y um denselben Betrag daneben, oder der Assistent hielt beim ersten Dock mit
einem Y-Fehler an: Prüfen Sie zuerst die Riemeneinstellung.** Das kostet nichts, und es
ist die einzige Ursache auf dieser Seite, hinter der zwei bestätigte Behebungen stehen.
Bestimmen Sie zuerst die Riemen, durch Zählen der Zähne wie oben beschrieben. Stellen Sie
dann den Schalter **1.5GT Belts** selbst passend dazu ein; wählen Sie eine
Druckervariante nur, wenn jedes Teil dieser Ausführung dem Eingebauten entspricht.
Führen Sie die Kalibrierungen von Anfang an erneut aus, da die Änderung mehrere davon
zurücksetzt. War die Einstellung bereits richtig, ist als Nächstes die Riemenspannung an
der Reihe.

**Fehler, der entlang der Reihe wächst: Prüfen Sie die Rechtwinkligkeit.** Führen Sie
unter 6.9.1 oder 6.9.2 den Assistenten zur Rechtwinkligkeit des Portals aus, nachdem Sie
wie verlangt die Düsen aus den Docks 1 und 8 genommen haben. Meldet er eine deutliche
Schiefstellung, richten Sie zuerst das Portal nach der Anleitung rechtwinklig aus, und
behandeln Sie das Scheitern der Docks als wahrscheinliches Symptom davon. Da der
Assistent an denselben Docks misst, ist er keine unabhängige Prüfung der Docks; lässt er
sich durch ein Ausrichten des Portals nach der Anleitung nicht zufriedenstellen, teilen
Sie das dem Support mit, zusammen mit den Dock-Werten.

**Keines der beiden Muster:** Arbeiten Sie Riemenspannung, Rechtwinkligkeit des Portals
und Homing-Kalibrierung durch, und führen Sie dann die Kalibrierungen von Anfang an
erneut aus, statt nur den Dock-Schritt zu wiederholen.

**Weiterhin keine Lösung:** Wenden Sie sich mit den gemessenen Werten jedes Docks an den
Support. Siehe [wen Sie kontaktieren](support-and-warranty-path.md).

## Überprüfung

`reported` für die Ursache Riementyp: Zwei Besitzer an zwei voneinander unabhängigen
Stellen — einem Fehlerbericht zur Firmware und einem Forenthread — behoben jeweils eine
Dock-Kalibrierung, die an einem großen, unveränderlichen Y-Fehler festhing, indem sie die
Riemen- oder Gen-2-Konfiguration an die Hardware anpassten. Im Fehlerbericht benannte
ein Prusa-Entwickler die Ursache, bevor der Besitzer sie bestätigte.

**Erstanbieter.** Wie die Firmware ein Dock validiert — feste erwartete Positionen, ein
gemeinsames Y an der Core One, ein festes Fenster und was mit einem Dock geschieht, das
außerhalb davon liegt —, stammt aus Prusas öffentlichem Firmware-Quellcode, gelesen beim
Release-Tag 6.9.1. Die Kopplung zwischen Druckervariante und Riemeneinstellung, die
Gen2-Variante als Standard beim ersten Start und nach einem Zurücksetzen auf
Werkseinstellungen, das die Hardwarekonfiguration löscht, sowie die Kalibrierungen, die eine Änderung der Riemeneinstellung
zurücksetzt, stammen aus demselben Quellcode, ebenso, wie der Assistent zur
Rechtwinkligkeit des Portals misst und an welcher Grenze er das Bestehen festmacht. Die
am 7. Oktober 2026 veröffentlichte Firmware 6.9.2 ergänzt 6.9.1 um die
Filament-Voreinstellungen für PVA und BVOH und um nichts weiter, was einen INDX betrifft
([Vergleich](https://github.com/prusa3d/Prusa-Firmware-Buddy/compare/v6.9.1...v6.9.2)),
sodass alles, was hier beim Git-Tag 6.9.1 gelesen wurde, für sie unverändert gilt. Der
Warntext zur Riemeneinstellung ist der des Druckers selbst. Eine frühere Anfrage
([#5445](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5445)), Docks gegen
eine an der Maschine gemessene Referenz zu validieren, wurde als nicht geplant
geschlossen. Der Entwickler gab die Sicht des Teams wieder und hielt es beim derzeitigen
Entwicklungsstand für viel Aufwand bei geringem Nutzen, ohne die Idee zu verwerfen,
nachdem die Riemeneinstellung den ursprünglichen Fall erklärt hatte.

`provisional`: Der Fall der verdrehten Reihe ist eine Maschine; der Besitzer berichtet,
das Portal nicht nach der Anleitung rechtwinklig ausrichten zu können, ohne die
Portalkalibrierung scheitern zu lassen, der Support hat es noch nicht gelöst, und die
Rückfragen des Entwicklers sind unbeantwortet. Die Hinweise zu Riemenspannung und Homing
stammen von mehreren Besitzern, aber alle aus einem Thread, und die Behebung durch
Nachspannen zu lockerer Riemen ist der Bericht eines einzelnen Besitzers.

Noch nicht geprüft: ob das Flashen der INDX-Firmware als der erste Start zählt, der den
Gen2-Standard setzt, was beide Besitzer erklären würde, die ihren Drucker auf Gen 2
eingestellt vorfanden; ob die Docks 1 und 8 leer waren, als der Besitzer den Assistenten
ausführte; ob die Schiefstellung, die der Assistent an der Maschine mit der verdrehten
Reihe meldet, im Portal oder in der Dock-Reihe selbst liegt; und ob eine Core One das
Werk mit einer Dock-Reihe verlassen hat, die so weit aus der Linie liegt, dass kein
Rechtwinkligstellen sie ins Fenster bringt.

## Verwandte Seiten

- [Werkzeug-Offset-Kalibrierung schlägt fehl](offset-sensor-board-failure.md) — es lohnt
  sich, dort zuerst dieselbe Riemeneinstellung auszuschließen
- [Phantom-Werkzeuge und Park-Fehler](tool-detection-ringdown-decay.md) — wenn die
  Dock-Kalibrierung gelingt, das Aufnehmen oder Parken aber weiterhin scheitert
- [Kompatibilität der Druckplatten](../reference/build-plate-compatibility.md) —
  Werkzeuge, die aus ihren Docks gestoßen werden, während die Kalibrierung besteht
- [Input-Shaper-Kalibrierung bricht mit „Measurement failed“ ab](input-shaper-measurement-failed.md)
  — eine weitere Kalibrierung, bei der die Riemeneinstellung die erste Prüfung ist
- [Wen Sie kontaktieren](support-and-warranty-path.md)
