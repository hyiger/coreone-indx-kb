---
title:        Fehlgeschlagenes Entladen und Auswerfen — zu enge Bohrung der Filamentführung
confidence:   provisional
updated:      2026-09-25
author:       hyiger
printer:      Core One
toolhead:     INDX
hotend:       unknown
nozzle:       unknown
firmware:     unknown
sources:
  - https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/a-summary-of-common-indx-problems/
  - https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/nozzle-stuck-with-filament/
superseded_by:
source_sha:   16f15fa56d01c8882e0a979a613399f92d6966ea2ce3f585ec9bced61ac02c99
---
# Fehlgeschlagenes Entladen und Auswerfen — zu enge Bohrung der Filamentführung

!!! warning "Einzelquelle für die Ursache — als Hinweis behandeln, nicht als Anleitung"
    Die Erklärung auf dieser Seite stammt aus einem einzigen Thread, der selbst eine
    Verdichtung einer inzwischen offline genommenen Community-Wissensdatenbank ist. Ein
    weiterer Besitzer hat inzwischen in einem anderen Thread ein ähnliches Symptom
    beschrieben, aber niemand im Forum hat die Ursache bestätigt. Es wird veröffentlicht,
    weil das Symptom charakteristisch genug ist, um es wiederzuerkennen, nicht weil die
    Abhilfe gesichert wäre.

## Zusammenfassung

Berichten zufolge wurde eine Charge des gedruckten Filamentführungsteils, das über der
Düse sitzt, mit einer engeren Bohrung als vorgesehen ausgeliefert — enger, als das
aufgequollene Ende eines Filamentstrangs benötigt, um wieder nach oben hindurchzupassen.
Die Folge ist, dass das Entladen oder Auswerfen von Filament an einem betroffenen
Werkzeug häufig fehlschlägt, während der Druck durch dasselbe Werkzeug normal
funktioniert. Wenn bei Ihnen das Entladen fehlschlägt, die Drucke aber in Ordnung sind,
ist das hier wissenswert. Wenden Sie sich für ein Ersatzteil an den Hersteller.

## Details

Das Verwirrende an diesem Fehler ist die Asymmetrie. Filament durch die Führung nach
unten zu fördern und damit zu drucken funktioniert, weil das Filament in die leichte
Richtung läuft und nicht verformt ist. Beim Entladen wird das Filament wieder nach oben
gezogen, und die Spitze, die in einer heißen Düse gestanden hat, ist leicht aufgequollen
— sie muss die engste Stelle des Weges also in ihrem dicksten Zustand passieren. Ist die
Bohrung zu eng, verklemmt sich die aufgequollene Spitze und das Entladen oder Auswerfen
bricht ab. An betroffenen Werkzeugen schlägt dies Berichten zufolge bei einem großen Teil
der Versuche fehl, nicht nur gelegentlich.

Die berichtete Erklärung ist ein übersprungener Nachbearbeitungsschritt und kein
Konstruktionsfehler. Die betroffene Hälfte des Werkzeugs wird im Lasersinterverfahren
gefertigt, wodurch der innere Filamentweg in genau der Größe bleibt, in der er aus der
Maschine kommt, statt in einer kontrollierten. Diese Bohrung auf einen definierten
Durchmesser zu bringen ist im Werk ein eigener Arbeitsgang — ein Bohrer oder eine
Reibahle wird durch den Weg geführt — und betroffene Werkzeuge sind solche, die ohne ihn
ausgeliefert wurden. Der Umfang wird als gering beschrieben: eine Handvoll, die
durchgerutscht ist, nicht eine ganze Produktionsserie.

### Was zu tun ist

**Fragen Sie zuerst beim Hersteller nach einem Ersatzteil.** Es handelt sich um einen
Fertigungsfehler an einem gedruckten Verschleißteil, und die berichtete Position des
Herstellers ist, dass die fertige Bohrung größer sein soll als das, was ausgeliefert
wurde. Damit ist es sein Teil, das er zu ersetzen hat. Siehe
[wen Sie kontaktieren](support-and-warranty-path.md).

### Zur Abhilfe aus der Community

Die berichtete Abhilfe aus der Community entspricht dem Schritt im Werk: einen Bohrer
von der Kupplungsseite her von Hand durch die Bohrung zu drehen, um sie auf den
vorgesehenen Durchmesser zu öffnen. Berichten zufolge hat sie bei jedem dokumentierten
Versuch funktioniert.

!!! danger "Diese Seite nennt Ihnen die Maße nicht"
    TODO(verify): die an betroffenen Teilen gemessenen Bohrungsdurchmesser im
    Auslieferungszustand, der vorgesehene Enddurchmesser und die verwendete Bohrergröße.
    Diese Angaben werden bewusst zurückgehalten.

    Dies ist der Fall in der gesamten Wissensdatenbank, in dem eine falsche Zahl den
    größten Schaden anrichtet. Die Änderung ist **irreversibel** — ein Loch lässt sich
    nicht zurückbohren. Bohren Sie zu klein, haben Sie nichts behoben; bohren Sie zu
    groß, haben Sie ein Teil ruiniert, das Filament in eine heiße Düse führt, an einer
    Maschine, bei der die Ausrichtung dieses Teils zählt. Auch die Gewährleistungslage
    bei einem selbst veränderten Teil ist ungeklärt, sodass Sie damit den kostenlosen
    Ersatz verwirken können, der Ihnen zugestanden hätte.

    Wenn Sie sich dennoch dafür entscheiden, holen Sie die Maße beim Hersteller oder aus
    dem verlinkten Quell-Thread und prüfen Sie sie mit einem Messschieber an Ihrem
    eigenen Teil nach — nicht von dieser Seite.

## Überprüfung

`provisional` — eine Quelle für die Ursache, nicht reproduziert; ein weiterer Bericht
des Symptoms, ohne bestätigte Ursache.

Die Quelle für die Ursache ist die [Zusammenfassung häufiger Probleme](https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/a-summary-of-common-indx-problems/).
Der dortige Bericht ist konkret und in sich plausibel — er nennt einen gemessenen
Bereich, einen vorgesehenen Durchmesser, eine Bestätigung des Herstellers und eine
Erfolgsquote — aber Konkretheit ist keine Bestätigung.

Eine Suche im gesamten Forumsbestand nach Fehlern beim Entladen und Auswerfen findet
einen weiteren passenden Thread, im
[Board zur Fehlersuche bei ersten Drucken](https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/nozzle-stuck-with-filament/).
Ein Besitzer beschreibt ein einzelnes Werkzeug, an dem jedes Entladen fehlschlägt und der
Strang von Hand herausgezogen werden muss, während ein Druck, der nur dieses Werkzeug
nutzt, normal läuft und die übrigen Werkzeuge der Maschine in Ordnung sind. Das ähnelt dem
Muster, das diese Seite beschreibt, aber es reicht nicht als Bestätigung. Der Besitzer
hat keine Messung der Bohrung gemeldet und nie gesagt, was das Problem behoben hat,
obwohl der Thread später als gelöst markiert wurde. Die Erklärung mit der zu engen
Bohrung, die in diesem Thread angeboten wurde, stammt vom Autor dieser Website und ist
daher keine unabhängige Diagnose. Und der Bericht weicht in einem Punkt von dieser Seite
ab: Der Abschnitt „Zusammenfassung“ auf dieser Seite sagt, dass der Druck durch ein
betroffenes Werkzeug nicht beeinträchtigt ist, während dort das Werkzeug nur dann normal druckte, wenn keine
Werkzeugwechsel beteiligt waren — mit Wechseln verklemmte sich sein Filament oder kam
erst nach mehreren Versuchen durch.

Ein anderer Besitzer im selben Thread konnte eines seiner Werkzeuge nie laden. Ein
Laden, das nie gelingt, ist nicht das, was dieser Mechanismus erwarten lässt, und eine
ab Werk verstopfte Düse (siehe [Düsenhärte](nozzle-hardness.md)) würde es ebenso gut
erklären; es wird hier daher nicht gezählt.

Inzwischen wurde ein zweiter Bericht aus dem Discord des Herstellers weitergegeben,
unabhängig vom Forums-Thread. Er stimmt im Mechanismus überein — ein
Nachbearbeitungsgang, der die gesinterte Bohrung auf ein definiertes Maß bringt, bei
einer kleinen Zahl von Werkzeugen vor der Auslieferung ausgelassen — und er ist es, der
belegt, dass das Teil lasergesintert ist. Dieser Ort hat keinen zitierbaren Permalink,
und diese Website zitiert kein Discord, daher wird er hier als Bestätigung festgehalten,
**die ein Leser nicht überprüfen kann**, und die Stufe ändert sich nicht. Zwei
übereinstimmende Berichte an zwei Orten stärken den Mechanismus; sie sind nicht die zwei
verlinkbaren Quellen, die `reported` verlangt.

Was diese Seite noch auf `reported` heben würde: ein zweiter Besitzer an einem
zitierbaren Ort, der fehlgeschlagene Entladevorgänge an einem normal druckenden Werkzeug
auf die Bohrung selbst zurückführt — durch eine Messung oder dadurch, dass der Fehler
verschwindet, sobald die Bohrung nachbearbeitet oder das Teil ersetzt ist. Ein
ähnliches Symptom allein, wie das oben, genügt nicht. Wenn Sie das haben, ist es das
Nützlichste, was Sie dieser Seite hinzufügen können.

## Verwandte Seiten

- [Düsenhärte](nozzle-hardness.md) — die übrigen düsennahen Fertigungsfehler,
  einschließlich ab Werk verstopfter Düsen
- [Wen Sie kontaktieren](support-and-warranty-path.md)
