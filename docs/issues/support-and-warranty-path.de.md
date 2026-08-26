---
title:        Wen Sie kontaktieren — Support vs. Gewährleistung bei einem INDX-Kit
confidence:   reported
updated:      2026-08-24
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
superseded_by:
source_sha:   8be570c219550b7c52cf598e07fc530f9a42a33508ce3d00e6f8de97e0ca6edd
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
berichtet.

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
