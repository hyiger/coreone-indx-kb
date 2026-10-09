---
title:        Wen Sie kontaktieren — Support vs. Gewährleistung bei einem INDX-Kit
confidence:   reported
updated:      2026-10-08
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
superseded_by:
source_sha:   1935eb41a3feb457a171b52f76663a9f3fbb557c158d0e8fb4246a0ab25d7d9b
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
Woche nach der ersten Meldung wartete er noch immer.

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
per Live-Chat oder E-Mail. Ob auch Kits abgedeckt sind, die nach diesem Update bei Prusa
bestellt wurden, hat Prusa nicht gesagt.

Der Kauf von Ersatzdüsen ist eine eigene Sache. Besitzer in zwei getrennten Threads
berichten, dass sich Prusas Shop-Guthaben nicht für INDX-Düsen einsetzen lässt; diese
kommen aus dem Shop des Herstellers, gleich welche Edition Sie besitzen, und der frühere
der beiden erklärte im August, Prusa verkaufe sie nicht. Eine hängende Shop-Bestellung
ist ein Fall für ein Ticket beim Hersteller. Ein Besitzer, dessen Bestellung im Oktober
knapp drei Wochen gewartet hatte, eröffnete ein Ticket und erhielt noch am selben Tag
eine Antwort mit einer Versandschätzung. Das ist vorläufig, ein Einzelbericht, und die
Schätzung war zum Zeitpunkt des Beitrags noch nicht eingelöst.

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

Schwächer: Das Ersatzangebot über den Live-Chat und die genannte Eskalationsdauer beruhen
jeweils auf dem Bericht eines einzelnen Besitzers im Thread mit der Zusammenfassung
häufiger Probleme. Der spätere Beitrag desselben Besitzers, der Kopf sei angekommen und
eingebaut, in einem
[Thread zur Frage, ob sich das INDX-Upgrade lohnt](https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/is-it-worth-upgrading-from-core-one-to-indx/),
ist wiederum dessen eigene Schilderung und keine zweite Quelle, und keiner der beiden
Beiträge nennt, um welche Edition es sich beim Kit handelt. Dass sich Prusas Shop-Guthaben nicht für INDX-Düsen einsetzen lässt, beruht auf
zwei Besitzern in getrennten Threads, dem Thread
[nozzlegate communications](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/nozzlegate-communications/)
und einem
[Thread zu langsamen Düsenbestellungen](https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/bondtech-nozzles-dont-ship/),
nicht auf einer Aussage von Prusa; dass Prusa sie im August nicht verkaufte, beruht
allein auf dem ersten davon. Die Antwort des Herstellers am selben Tag ist ein
Einzelbericht aus dem zweiten.

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
