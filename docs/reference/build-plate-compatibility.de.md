---
title:        Kompatibilität der Druckplatten nach dem INDX-Umbau
confidence:   reported
updated:      2026-09-12
author:       hyiger
printer:      Core One
toolhead:     INDX
hotend:       unknown
nozzle:       unknown
firmware:     unknown
sources:
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/update-kind-of/
  - https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/sometimes-tools-dont-stay-in-dock/
superseded_by:
source_sha:   50da9cb601731a272dbee2a8ca31bff8bb9047137ab07357601a80b1718ca475
---
# Kompatibilität der Druckplatten nach dem INDX-Umbau

## Zusammenfassung

Übergroße Federstahlbleche von Drittanbietern — die größeren Platten, die für Maschinen
der Bambu-Klasse verkauft werden — passen nicht mehr, sobald die INDX-Werkzeugdocks
montiert sind. Der vordere Überstand der Platte stößt gegen die an den Docks montierten
Teile. Die Tücke liegt darin, dass diese Bleche auf eine unveränderte Core One
einwandfrei passen: Wer also einen Drucker umbaut, den er bereits nutzt, dessen
Alltagsblech kann an dem Tag, an dem der Umbau fertig ist, klammheimlich unbrauchbar
werden.

Es sieht nicht immer nach einem Passproblem aus. Dieselbe Kollision kann Werkzeuge nach
Druckbeginn aus ihren Docks schieben, während jede Kalibrierung besteht — was sich wie
ein Dockfehler liest statt wie eine zu große Platte —, und sie beschränkt sich nicht auf
übergroße Bleche, denn auch eine Platte mit anderem Randprofil kann das verursachen.

## Details

Die INDX-Docks belegen vorn an der Maschine Raum, der zuvor frei war. Platten, die für
eine größere Bettgrundfläche zugeschnitten sind, ragen in diesen Raum hinein, und der
Überstand trifft auf die Düsendichtung und die Anti-Oozing-Teile, die an den Docks
sitzen. Ein Besitzer verbreitete ein Foto, das eine Platte im Kontakt mit mehreren der
mittleren Docks zeigt.

Das ist Geometrie, nicht Firmware. Kein Update wird es aus der Welt schaffen.

**Warum es die Leute erwischt.** Nichts am Umbau legt nahe, dass die Druckoberfläche
betroffen ist, und das fragliche Blech hat auf denselben Drucker bislang anstandslos
gepasst. Besitzer beschreiben diese Platten als ihre erste Wahl — genau deshalb sollte
man von der Inkompatibilität vor dem Beginn wissen und nicht danach.

### Es kann wie ein Dockfehler aussehen

In einem anderen Thread erhielt ein Besitzer, dessen Werkzeuge nicht in ihren Docks
blieben — bei bestandener Dock-Kalibrierung —, zwei voneinander unabhängige Antworten,
die beide auf die Platte zeigten. Ein Besitzer hatte dieses Symptom auf eine größere als
die Serienplatte zurückgeführt, die die Düsenabstreifer an der Dockhalterung berührte,
und ergänzte, dass verbogene oder verkehrt herum montierte Abstreifer ebenfalls eine
Prüfung wert sind. Ein anderer hatte beobachtet, wie Werkzeuge nach Druckbeginn aus
ihren Docks gestoßen wurden, auf einer Drittanbieterplatte mit anderem Profil als die
Serienplatte, ebenfalls bei bestandener Kalibrierung.

Der zweite Fall ist der bemerkenswerte, denn jene Platte wurde nie als übergroß
beschrieben. Entscheidend ist, was unter den Docks liegt, nicht nur die Grundfläche.
Wenn Werkzeuge in ihren Docks gestört werden, schließen Sie die Platte aus, bevor Sie
Magnete oder die Dock-Kalibrierung verdächtigen — siehe
[Werkzeugerkennung und Parkfehler](../issues/tool-detection-ringdown-decay.md).

### Was Besitzer dagegen unternommen haben

Zwei Wege, beide aus erster Hand berichtet:

- **Eine Platte im Prusa-Format verwenden.** Die einfachste Antwort und die, zu der man
  zuerst greifen sollte. Ein Besitzer kaufte eine passend dimensionierte Platte und
  behielt die übergroßen als Reserve.
- **Den Überstand abtrennen.** Zwei Besitzer haben ihre Platten zugeschnitten und
  berichten, dass es leicht ging. Eine Trennscheibe erledigte die Arbeit; die
  vorhandenen Löcher in der Platte dienten als Bezug, um den Schnitt gerade zu führen,
  anschließend wurde entgratet. Eine Tafelschere wurde als sauberere Alternative für
  alle vorgeschlagen, die Zugang zu einer haben.

    Anritzen und Brechen wurde angesprochen und bezweifelt — Federstahl bricht nicht
    entlang einer angeritzten Linie, wie dünneres Blech es tut. Niemand berichtete von
    einem erfolgreichen Versuch.

!!! danger "Hier wird kein Schnittmaß veröffentlicht"
    TODO(verify): wie viel des Überstands entfernt werden muss. **Im Quellthread wurde
    kein Wert veröffentlicht**, und hier wird keiner erfunden.

    Das ist ein Schnitt, den Sie nicht rückgängig machen können, an einem Teil, das
    direkt unter einem bewegten Werkzeugkopf liegt; ein falscher Wert ruiniert die
    Platte im besten Fall. Wenn Sie zuschneiden, messen Sie an Ihrer eigenen Maschine
    mit montierten Docks, statt sich auf irgendeinen online gelesenen Wert zu stützen
    — diese Seite eingeschlossen. Entgraten Sie danach; eine rohe Schnittkante an
    einem Blech, das Sie bei jedem Druck in die Hand nehmen, ist eine Minute
    Aufmerksamkeit wert.

    Erwägen Sie, ob eine passend dimensionierte Platte nicht schlicht die bessere
    Antwort ist. Sie ist umkehrbar, sie kostet weniger als ein ruiniertes Blech, und
    sie beseitigt die Frage.

## Überprüfung

`reported` — unabhängige Besitzer, über zwei verschiedene Threads hinweg.

Der [ursprüngliche Thread](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/update-kind-of/)
belegte die Kollision: Ein Besitzer brachte sie auf, ein Foto zeigte eine Platte, die die
Docks berührte, zwei weitere Besitzer hatten ihre bereits zugeschnitten, und ein vierter
kaufte eine passend dimensionierte Platte. Das wurde auf `provisional` gehalten, weil
jede dieser Meldungen in derselben Diskussion stand.

Ein zweiter, davon unabhängiger [Thread über Werkzeuge, die nicht im Dock bleiben](https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/sometimes-tools-dont-stay-in-dock/)
hat inzwischen die Bestätigung über Threads hinweg geliefert, auf die diese Seite gewartet
hatte. Zwei Besitzer dort führten das Symptom unabhängig voneinander auf eine
Nicht-Serienplatte zurück, die den Dockbereich stört. Das erfüllt die Schwelle dieser
Website für `reported`.

Es erweitert den Befund zudem ein wenig. Die neuen Meldungen beschreiben ein anderes
Erscheinungsbild — Werkzeuge, die in ihren Docks gestört werden, statt einer Platte, die
sichtbar nicht passt —, und eine betrifft eine Platte, die niemand als übergroß
beschrieb. Der Mechanismus ist derselbe; die Bandbreite der Symptome und der betroffenen
Platten ist größer, als der ursprüngliche Thread zeigte.

Weiterhin ungeprüft: wie viel Überstand entfernt werden muss, wozu keine Quelle einen
Wert nennt, und ob eine bestimmte Drittanbieterplatte bei montierten Docks unbedenklich
ist.

## Verwandte Themen

- [Hinweise zum Zusammenbau](assembly-notes.md) — vor dem Beginn des Umbaus lesenswert,
  da dies ein Problem der Sorte „am ersten Tag herausfinden“ ist
