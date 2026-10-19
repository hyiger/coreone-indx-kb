---
title:        Wen Sie kontaktieren — Support vs. Gewährleistung bei einem INDX-Kit
confidence:   reported
updated:      2026-10-18
author:       hyiger
printer:      Core One, Core One L
toolhead:     INDX
hotend:       unknown
nozzle:       unknown
firmware:     unknown
sources:
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/warranty-concern-uk/
  - https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/a-summary-of-common-indx-problems/
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/nozzlegate-communications/
  - https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/bondtech-nozzles-dont-ship/
  - https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/is-it-worth-upgrading-from-core-one-to-indx/
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/prusa-indx-update-shipping-starts-this-week/
superseded_by:
source_sha:   a3314bd296f5d3ac238289df73a3335c188ab3ae2fdb4100a8bfb038117fd48b
---
# Wen Sie kontaktieren — Support vs. Gewährleistung bei einem INDX-Kit

## Zusammenfassung

Diagnose und Ersatzteile kommen von zwei verschiedenen Unternehmen, und das Problem an
das falsche zu schicken ist mit Abstand die häufigste Art, wie Besitzer Wochen
verlieren. Bei Kits der Founders Edition hat sich unter den Besitzern folgendes Muster
durchgesetzt: den Fehler von Prusa *diagnostizieren* lassen und diese Diagnose dann zu
Bondtech tragen, um das *Teil* zu bekommen. Eröffnen Sie Ihren Fall früh, auch wenn Sie
noch nicht bereit sind, ihn weiterzuverfolgen, damit das Datum innerhalb der für Sie
geltenden Gewährleistungsfrist aktenkundig ist.

## Details

Der INDX ist ein Bondtech-Produkt, das an einen Prusa-Drucker geschraubt wird, und die
Support-Verantwortung teilt sich entlang dieser Naht statt entlang der Naht, die ein
Kunde erwarten würde. Prusas technischer Support arbeitet die Diagnose mit Ihnen durch —
dessen Werkzeuge, Logs und Firmware-Kenntnisse sind es, die die defekte Komponente
identifizieren. Bei Kits der Founders Edition besteht der Kaufvertrag jedoch mit
Bondtech, und Ersatzhardware kommt von dort. Besitzer im Forum berichten von einigem Hin
und Her zwischen beiden, bevor das klar wurde.

Die praktische Konsequenz ist eine Reihenfolge:

1. **Diagnostizieren Sie zuerst mit Prusa.** Nutzen Sie deren Supportkanäle und bewahren
   Sie den Schriftverkehr auf. Mehrere Besitzer berichten, dass ein beigefügtes Video des
   Fehlers mehr beschleunigt als jede noch so ausführliche schriftliche Beschreibung —
   ein Fehler, der sich schwer in Worte fassen lässt, ist in ein paar Sekunden Aufnahme
   oft unverkennbar.
2. **Eröffnen Sie den Fall beim Hersteller mit Prusas Befund.** Ein Ticket, das bereits
   „der Prusa-Support hat X festgestellt" enthält, kommt schneller voran als eines, das
   bei den Symptomen beginnt.
3. **Zitieren Sie beide Antworten, wenn die zwei sich widersprechen.** Besonders Defekte
   an den gedruckten Dock-Teilen wurden zwischen den beiden Unternehmen hin- und
   hergeschoben. Wenn Sie von beiden eine Stellungnahme haben, packen Sie beide ins
   Ticket, statt sie getrennt entdecken zu lassen.

Zwei Dinge sollte man vorab wissen. Prusa hat es abgelehnt, Ersatzteile für die Founders
Edition direkt zu versenden; eine Ersatzteilanfrage dorthin zu leiten ist also eine
Sackgasse, selbst wenn dort Einigkeit besteht, dass das Teil defekt ist. Und Bondtechs
Supportteam ist klein im Verhältnis zur Zahl der Kits im Feld; die berichtete
Bearbeitungsdauer reichte von über Nacht bis zu mehreren Wochen Funkstille, eine langsame
Antwort ist also nicht zwangsläufig ein verlorenes Ticket.

Gleich, bei welchem Unternehmen Ihr Fall liegt: Fragen Sie, mit welcher Bearbeitungszeit
zu rechnen ist, und haken Sie nach, wenn sie verstrichen ist. Einem Besitzer sagte
Prusas Support, ein eskalierter Fall dauere normalerweise einige Tage, und knapp eine
Woche nach der ersten Meldung wartete er noch immer. Videos helfen, erledigen aber nicht
jeden Fall schnell: Ein anderer Besitzer, bei dem Antasten und Werkzeugkalibrierung meist
fehlschlagen, berichtet, Prusas Support zehn Videos geschickt zu haben und noch immer keine
abschließende Antwort zu haben.

Ein Besitzer, bei dem sich Werkzeuge am Dock wiederholt nicht aus dem Kopf lösten — siehe
[Werkzeug entriegelt sich oder fällt aus dem Kopf](tool-unlocks-or-ejects.md) — berichtet,
dass Prusas Live-Chat angeboten habe, einen kompletten Ersatz-Werkzeugkopf zu schicken.
In einem
[späteren Thread zu einem anderen Thema](https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/is-it-worth-upgrading-from-core-one-to-indx/)
schreibt derselbe Besitzer, der neue Kopf sei wenige Tage nach einem kurzen Online-Chat
von Prusa gekommen und eingebaut worden. Keiner der beiden Beiträge nennt die Edition des
Kits oder, wo es gekauft wurde; der Bericht bestätigt das oben beschriebene Muster der
Founders Edition also weder, noch widerlegt er es. Es ist ein Besitzer, der seinen
eigenen Fall zweimal schildert, keine zweite Quelle: Behandeln Sie ihn als Einzelbericht,
`provisional`.

### Düsenentschädigung und Ersatzdüsen

Die ausgelieferten INDX-Düsen sind nur an der Oberfläche gehärtet, nicht durchgehend,
und dafür wird eine Entschädigung angeboten; Hintergrund, Optionen und deren Grenzen
stehen auf der Seite zur [Düsenhärte](nozzle-hardness.md). Die Entschädigung wickelt
ab, wer Ihnen das Kit verkauft hat. Besitzer der Founders Edition stellen ihren Anspruch beim Hersteller,
über dessen Kontaktformular. Prusas Update vom August ging an Kunden, die ihre
Kit-Bestellung schon aufgegeben hatten, also an die ersten Chargen, und besagt, dass
Prusa deren Entschädigung selbst abwickelt: Shop-Guthaben, verschickt als Gutschein per
E-Mail, oder stattdessen eine Barerstattung. Ist der Gutschein für das Shop-Guthaben
einige Tage nach Eintreffen des Kits nicht da, wenden Sie sich an Prusas technischen
Support; wenn Sie statt Guthaben die Barerstattung möchten, fragen Sie Prusas Support
per Live-Chat oder E-Mail. Ein dem Kit beiliegender gedruckter Hinweis nennt dieselbe
Erwartung von einigen Tagen, laut einem Besitzer, der die E-Mail danach nicht finden
konnte. Durchsuchen Sie Ihr Postfach, bevor Sie nachhaken: Ein anderer Besitzer im
selben Thread berichtet, dass seine mit einem Betreff kam, der sie als
INDX-Entschädigungsgutschein bezeichnet, was sich leichter finden lässt als alles, was
nur unter Prusas Namen eingeht. Beides stammt aus einem einzigen Thread, ist also
vorläufig. Ob auch Kits abgedeckt sind, die nach diesem Update bei Prusa bestellt
wurden, hat Prusa nicht gesagt.

Der Kauf von Ersatzdüsen ist eine eigene Sache. INDX-Düsen kommen aus dem Shop des
Herstellers, gleich welche Edition Sie besitzen. Stand Mitte Oktober ließ sich Prusas
Shop-Guthaben nicht für sie einsetzen, weil Prusas Shop sie nicht führte; das berichten
Besitzer in drei getrennten Threads, der früheste im August. Ein Besitzer erwartet, dass
Prusa sie irgendwann führt, und derselbe Besitzer gibt von Prusa wieder, dass der
Gutschein eine Gültigkeitsfrist hat; beides ist ein vorläufiger Einzelbericht und wird
auf der Seite zur [Düsenhärte](nozzle-hardness.md) behandelt. Eine hängende
Shop-Bestellung ist ein Fall für ein Ticket beim Hersteller. Ein Besitzer, dessen
Bestellung im Oktober knapp drei Wochen gewartet hatte, eröffnete ein Ticket und erhielt
noch am selben Tag eine Antwort mit einer Versandschätzung; die Bestellung ging wie
geschätzt Anfang der folgenden Woche hinaus und kam einen Tag später an. Das bleibt
vorläufig, ein Einzelbericht. Mitte Oktober sahen andere Besitzer im selben Thread, dass
im Oktober aufgegebene Bestellungen innerhalb von ein bis zwei Wochen versandt wurden.

### Zur Dauer der Gewährleistung — prüfen Sie das selbst

Die Gewährleistungsdauer wird im Forum uneinheitlich angegeben und hängt von der Region
und davon ab, bei wem Sie gekauft haben. **Diese Seite nennt bewusst keine Dauer**, weil
eine falsche Angabe hier dazu führen könnte, dass jemand die eigene Frist verpasst.

TODO(verify): die angegebene Gewährleistungsfrist für Käufe außerhalb der EU, die
gesetzliche Frist in der EU und die Rechtslage im Vereinigten Königreich nach dem
EU-Austritt. Stammt aus dem Thread „Warranty Concern (UK)", in dem die Teilnehmer
Besitzer sind, die über Verbraucherrecht nachdenken, und nicht Personen, die qualifiziert
wären, es darzulegen — einer von ihnen empfiehlt ausdrücklich, stattdessen eine
Verbraucherschutzorganisation zu fragen.

Worauf man sich verlassen kann: **Bei wem Sie gekauft haben, bestimmt, wessen
Gewährleistung gilt**, und das ist nicht immer derjenige, der das Paket verschickt hat.
Kits der Founders Edition wurden bei Bondtech gekauft, auch wenn Prusa die technische
Seite übernimmt; der Vertrag — und alle daran hängenden gesetzlichen Rechte — läuft also
auf Bondtech. Wenn Sie eine verbindliche Antwort für Ihr Land brauchen, fragen Sie Ihre
nationale Verbraucherschutzstelle, kein Druckerforum. Eröffnen Sie Ihren Fall in jedem
Fall früh, damit das Meldedatum festgehalten ist.

## Überprüfung

`reported` — die Aufteilung zwischen Support und Gewährleistung wird unabhängig in der
[Zusammenfassung häufiger Probleme](https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/a-summary-of-common-indx-problems/)
beschrieben und von Besitzern bestätigt, die im Thread
[Warranty Concern (UK)](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/warranty-concern-uk/)
reale Fälle durcharbeiten, der das Muster aus technischem Support beim einen und
Ersatzteilen beim anderen Unternehmen unabhängig bestätigt. Erfahrungen mit Eskalationen
und Bearbeitungszeiten werden in den beiden großen
[nozzlegate](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/nozzlegate-communications/)-Threads
berichtet. Dass Prusa die Düsenentschädigung für Kits abwickelt, die im August bereits bei
Prusa bestellt waren, stammt aus erster Hand: aus Prusas Update vom August an diese
Kunden, zitiert im Thread „nozzlegate communications“.

Schwächer: Das Ersatzangebot über den Live-Chat, die genannte Eskalationsdauer und der
Fall mit den zehn Videos beruhen jeweils auf dem Bericht eines einzelnen Besitzers im
Thread mit der Zusammenfassung häufiger Probleme. Der spätere Beitrag des Besitzers mit
dem Live-Chat-Angebot, der Kopf sei angekommen und eingebaut, in einem
[Thread zur Frage, ob sich das INDX-Upgrade lohnt](https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/is-it-worth-upgrading-from-core-one-to-indx/),
ist wiederum dessen eigene Schilderung und keine zweite Quelle, und keiner der beiden
Beiträge nennt, um welche Edition es sich beim Kit handelt. Dass sich Prusas
Shop-Guthaben nicht für INDX-Düsen einsetzen ließ, weil Prusas Shop sie nicht führte,
beruht auf drei Besitzern in drei getrennten Threads, dem Thread
[nozzlegate communications](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/nozzlegate-communications/),
einem
[Thread zu langsamen Düsenbestellungen](https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/bondtech-nozzles-dont-ship/)
und Prusas
[Thread zu Versand-Updates](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/prusa-indx-update-shipping-starts-this-week/),
nicht auf einer Aussage von Prusa; für August beruht es allein auf dem ersten davon. Die
Antwort des Herstellers am selben Tag und der Versand der Bestellung wie geschätzt sind
der Bericht eines einzelnen Besitzers aus dem zweiten, in dem der seither schnellere
Versand von mehreren Besitzern stammt. Der beiliegende Hinweis und der Betreff der
Gutschein-E-Mail stammen von zwei Besitzern im dritten. Die Erwartung, dass Prusa
INDX-Düsen später führen wird, stammt von einem einzelnen Besitzer und nicht erkennbar
von Prusa; die Gültigkeitsfrist von Prusas Gutschein ist dessen Wiedergabe, beides in
eben diesem dritten Thread.

Wo die Quellen sich widersprechen: bei der Gewährleistungsdauer. Der UK-Thread kommt zu
keinem Ergebnis, und seine Teilnehmer sagen das deutlich. Behandeln Sie jede Dauerangabe
im Forum als unbestätigt.

Diese Seite beschreibt einen Support-Ablauf, keinen Rechtsanspruch. Nichts hiervon ist
eine Rechtsberatung.

## Verwandte Seiten

- [Fehlgeschlagene Werkzeug-Offset-Kalibrierung](offset-sensor-board-failure.md) — der
  häufigste Fehler, der in einer Ersatzteilanfrage endet
- [Düsenhärte](nozzle-hardness.md) — der rückgaberechtliche Kontext speziell zum
  Düsenproblem
