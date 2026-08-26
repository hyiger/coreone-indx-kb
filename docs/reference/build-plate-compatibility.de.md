---
title:        Kompatibilität der Druckplatten nach dem INDX-Umbau
confidence:   provisional
updated:      2026-08-24
author:       hyiger
printer:      Core One
toolhead:     INDX
hotend:       unknown
nozzle:       unknown
firmware:     unknown
sources:
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/update-kind-of/
superseded_by:
source_sha:   fd8dd8c5ed5f0aaf103c98ca3b8c282e2ff56c1742f6d7ab3dc49de594eb5649
---
# Kompatibilität der Druckplatten nach dem INDX-Umbau

!!! warning "Ein einziger Thread — den Vorbehalt beachten"
    Mehrere Besitzer berichten dies unabhängig voneinander, und zwei haben Fotos
    veröffentlicht, doch alles stammt aus einem einzigen Forumsthread. Das reicht nach
    den Regeln dieser Website nicht aus, um es als `reported` (mehrfach berichtet)
    einzustufen. Die physischen Belege sind gut; die Stichprobe ist schmal.

## Zusammenfassung

Übergroße Federstahlbleche von Drittanbietern — die größeren Platten, die für Maschinen
der Bambu-Klasse verkauft werden — passen nicht mehr, sobald die INDX-Werkzeugdocks
montiert sind. Der vordere Überstand der Platte stößt gegen die an den Docks montierten
Teile. Die Tücke liegt darin, dass diese Bleche auf eine unveränderte Core One
einwandfrei passen: Wer also einen Drucker umbaut, den er bereits nutzt, dessen
Alltagsblech kann an dem Tag, an dem der Umbau fertig ist, klammheimlich unbrauchbar
werden.

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

`provisional` (vorläufig) — mehrere unabhängige Meldende, aber ein einziger Thread.

Innerhalb dieses Threads sind die Belege besser, als die Stufe vermuten lässt. Ein
Besitzer brachte die Kollision zunächst als Verdacht vor; gestützt wurde sie dann durch
ein Foto einer Platte, die die Docks berührt, durch einen zweiten Besitzer, der seine
bereits zugeschnitten und das Ergebnis gezeigt hatte, und durch einen dritten, der
dieselbe Methode bestätigte und die Technik ergänzte, die Löcher der Platte zur Führung
eines geraden Schnitts zu nutzen. Ein vierter umging das Problem, indem er eine Platte
im Prusa-Format kaufte. Das sind vier übereinstimmende Besitzer, was gewöhnlich als
belastbar gelten würde.

Auf `provisional` gehalten wird es dadurch, dass diese Website eine Bestätigung über
*verschiedene* Threads hinweg verlangt, und jede dieser Meldungen steht in derselben
Diskussion. Erwähnenswert ist auch, dass der betreffende Thread überwiegend aus
Versand- und Bestellgeplauder besteht — dieser Befund kam nur durch vollständiges Lesen
zutage, und er war eines von lediglich zwei dauerhaften technischen Ergebnissen, die
aus diesem gesamten Thread die Prüfung überstanden haben.

Was es auf `reported` heben würde: eine einzige Meldung aus einem beliebigen anderen
Thread oder eine Herstelleraussage zum Freiraum für Platten bei montierten Docks.

## Verwandte Themen

- [Hinweise zum Zusammenbau](assembly-notes.md) — vor dem Beginn des Umbaus lesenswert,
  da dies ein Problem der Sorte „am ersten Tag herausfinden“ ist
