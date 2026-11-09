---
title:        Wen Sie kontaktieren — Support vs. Gewährleistung bei einem INDX-Kit
confidence:   reported
updated:      2026-11-08
author:       hyiger
printer:      Core One, Core One L
toolhead:     INDX
hotend:       unknown
nozzle:       unknown
firmware:     not version-specific; 8.0.0 for the two diagnostic screens noted under Detail
sources:
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/warranty-concern-uk/
  - https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/a-summary-of-common-indx-problems/
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/nozzlegate-communications/
  - https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/bondtech-nozzles-dont-ship/
  - https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/is-it-worth-upgrading-from-core-one-to-indx/
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/prusa-indx-update-shipping-starts-this-week/
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/indx-refund-voucher-doesnt-work-with-free-shipping/
  - https://blog.prusa3d.com/prusa-core-one-gen-2-indx-shipping-has-started-complete-printers-open-for-orders_137623/
  - https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/bondtech-indx-conversion-kit-assembly-pain-points-prep-notes/
  - https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/diagonal-banding-2/
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/bondtech-nozzle-hardening-debacle-how-does-this-affect-prusa-indx-orders/
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/indx-woes-and-a-shoutout-to-prusa-support/
  - https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/are-you-happy-with-your-indx-purchase/
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v8.0.0
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/src/gui/screen_menu_cyphal_info.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/src/feature/tool_offset_calibration/tool_offset_calibration.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/src/feature/tool_offset_wizard/screen_tool_offset_wizard.cpp
superseded_by:
source_sha:   9f4985972db89a889daaad5af768a5d85b0d797777c288ebe231692ba4337b92
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

Mit Firmware 8.0.0 liefert Ihnen der Drucker selbst zwei weitere Dinge, die Sie Prusas
Support zeigen können. Eine fehlgeschlagene Werkzeug-Offset-Kalibrierung sagt Ihnen mehr
darüber, was schiefgegangen ist. Prusas
[Versionshinweise](https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v8.0.0)
geben jeder Art von Fehler einen eigenen Bildschirm mit dem Fehlercode und dem betroffenen
Werkzeug; der
[Quellcode der Kalibrierung](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/src/feature/tool_offset_calibration/tool_offset_calibration.cpp)
ist enger gefasst. Von den Fehlern in den Schritten eines Werkzeugs haben ein nicht
aufgenommenes Werkzeug, ein nicht gefundener Sensor und ein Sensorausfall je einen eigenen
Code, alle übrigen zeigen weiterhin 36130. Die
[beiden Sensor-Bildschirme](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/src/feature/tool_offset_wizard/screen_tool_offset_wizard.cpp)
nennen kein Werkzeug, die anderen beiden schon; siehe
[was die Standard-Firmware 8.0.0 zeigt](../codes.md#stock-800). So oder so sagt ein Foto
des Bildschirms mehr als eine Beschreibung. Und ein neuer Bildschirm „Cyphal Info“, unter
Info und dann Version Info, listet die Zusatzplatinen am CAN-Bus des Druckers auf; öffnet
man einen Eintrag, zeigt er die Node-ID und den Zustand dieser Platine. Prusa beschreibt
ihn als vor allem eine Diagnosehilfe für den Kontakt mit dem Support. Im
[Quellcode](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/src/gui/screen_menu_cyphal_info.cpp)
ist der Werkzeug-Offset-Sensor eine der Platinen, die er aufführen kann.

Zwei Dinge sollte man vorab wissen. Prusa hat es abgelehnt, Ersatzteile für die Founders
Edition direkt zu versenden; eine Ersatzteilanfrage dorthin zu leiten ist also eine
Sackgasse, selbst wenn dort Einigkeit besteht, dass das Teil defekt ist. Und Bondtechs
Supportteam ist klein im Verhältnis zur Zahl der Kits im Feld; die berichtete
Bearbeitungsdauer reichte von über Nacht bis zu mehreren Wochen Funkstille, eine langsame
Antwort ist also nicht zwangsläufig ein verlorenes Ticket. Die Größe des Teams und die
zwischen beiden Unternehmen hin- und hergeschobenen Dock-Teile stammen allein aus der
Zusammenfassung der Community, einer Zusammenstellung des Autors dieser Website; die
abgelehnten Ersatzteilsendungen und die Spanne der Bearbeitungsdauer berichten auch
Besitzer in anderen Threads.

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
von Prusa gekommen und eingebaut worden. Das ist ein Besitzer, der seinen eigenen Fall
zweimal schildert, keine zweite Quelle, doch zwei weitere Besitzer in zwei weiteren
Threads berichten inzwischen dasselbe Ergebnis. Der eine, dessen Kopf sich zunehmend
verklemmte, bis er kein Werkzeug mehr freigeben oder aufnehmen konnte, schreibt, Prusas
Live-Chat sei zu dem Schluss gekommen, der Kopf sei beschädigt oder defekt, und habe Ersatz
geschickt, mit dem er wieder druckt, in einem
[Thread mit Lob für Prusas Support](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/indx-woes-and-a-shoutout-to-prusa-support/).
Der andere schrieb dem Support mit einem Video, in dem der Kopf beim Entladen ein Werkzeug
verliert, und berichtet, umgehend einen Ersatzkopf erhalten zu haben; die Kalibrierung
laufe seither einwandfrei, in einem
[Thread mit der Frage, ob Besitzer mit dem INDX zufrieden sind](https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/are-you-happy-with-your-indx-purchase/);
dieser Beitrag nennt das Unternehmen nicht. Ein kompletter Ersatzkopf für einen Kopf, der
seine Werkzeuge nicht hält oder nicht freigibt, ist damit `reported`: drei Besitzer in
vier Threads. Keiner der Beiträge nennt die Edition des Kits oder, wo es gekauft wurde; sie
bestätigen das oben beschriebene Muster der Founders Edition also weder, noch widerlegen
sie es.

Der Besitzer mit dem verklemmten Kopf ergänzt eine Faustregel: Wenn Sie ein festsitzendes
Werkzeug mehr als einmal von Hand über die Rückseite des Kopfes lösen müssen, hören Sie
auf, wenden Sie sich an den Support und halten Sie jedes Ereignis fest, damit der Fall
dokumentiert ist. Das ist der Rat eines einzelnen Besitzers, `provisional`.

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
wurden, hat Prusa nicht veröffentlicht. Ein Besitzer, dessen Bestellung offenbar nach
der Frühjahrswelle lag, gibt eine Antwort von Prusas Support wieder, die nur einen Teil
davon berührt: Die Gen-2-Upgrade-Hardware, die das Update vom August den Bestellungen
der ersten Chargen kostenlos zusagte, galt allein den Frühjahrsbestellungen, und
Bestellungen ab August bekommen sie nicht kostenlos. Derselbe Besitzer sagt, dass neue
Bestellungen diese Hardware inzwischen zusammen mit dem INDX enthalten; ob deren Kosten
im Preis stecken, ist nicht bestätigt. Das muss allerdings nicht für jede Bestellung
gelten: Prusas
[Ankündigung vom 20. August](https://blog.prusa3d.com/prusa-core-one-gen-2-indx-shipping-has-started-complete-printers-open-for-orders_137623/)
nennt getrennte Kit-Versionen für den CORE One+ und den CORE One+ (Gen 2). Das ist eine
einzelne, vorläufige Wiedergabe, und sie sagt nichts über Guthaben oder Bargeld; sie
wird auf der Seite zur [Düsenhärte](nozzle-hardness.md) behandelt.

Auch Probleme beim Einlösen von Prusas Gutschein sind ein Fall für Prusas Support. Ein
Besitzer, bei dem der Gutschein den kostenlosen Versand einer Shop-Aktion von der
Bestellung verdrängte, sprach das per Live-Chat an, und der Support löste es noch am
selben Tag, indem er den Wert des Gutscheins um die Versandkosten erhöhte; die
Einzelheiten, auch dass der Gutschein keine Versandkosten deckte, stehen auf der Seite
zur [Düsenhärte](nozzle-hardness.md). Vorläufig, ein Einzelbericht.

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

`reported` — die Aufteilung zwischen Support und Gewährleistung beschreiben Besitzer, die
reale Fälle durcharbeiten, mindestens drei von ihnen, in vier getrennten Threads. Im Thread
[Warranty Concern (UK)](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/warranty-concern-uk/)
legt ein Besitzer das Muster aus technischem Support beim einen und Ersatzteilen beim
anderen Unternehmen dar, und im
[Thread zum Härtungsdebakel der Düsen](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/bondtech-nozzle-hardening-debacle-how-does-this-affect-prusa-indx-orders/)
kommt derselbe Besitzer von Prusas Triage zu einem Garantieersatz von Bondtech, der am
nächsten Morgen bestätigt wurde. Im
[Thread zu Schwachstellen bei der Montage](https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/bondtech-indx-conversion-kit-assembly-pain-points-prep-notes/)
berichten Besitzer, wie Prusas Support defekte Offset-Sensoren an Kits der Founders Edition
diagnostizierte und sie dann für das Teil an Bondtech verwies, und im
[Thread zur diagonalen Bänderung](https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/diagonal-banding-2/)
wartet einer von ihnen darauf, dass Prusas Support den Extruder als Ursache bestätigt,
bevor er ein Ticket bei Bondtech eröffnet. Die
[Zusammenfassung häufiger Probleme](https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/a-summary-of-common-indx-problems/)
legt dasselbe Muster dar, ihr Eröffnungsbeitrag ist aber eine Zusammenstellung des Autors
dieser Website und zählt daher nicht als unabhängige Quelle; frühere Fassungen dieser Seite
zählten sie als solche. Erfahrungen mit Eskalationen
und Bearbeitungszeiten werden in den beiden großen
[nozzlegate](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/nozzlegate-communications/)-Threads
berichtet. Dass Prusa die Düsenentschädigung für seine Kit-Bestellungen der ersten
Chargen abwickelt, stammt aus erster Hand: aus Prusas Update vom August an diese
Kunden, zitiert im Thread „nozzlegate communications“. Dasselbe gilt für die getrennten
Kit-Versionen für den CORE One+ und den CORE One+ (Gen 2), laut Prusas Ankündigung
vom 20. August, und für die beiden Bildschirme in 8.0.0, laut Prusas Versionshinweisen,
wobei die Fehler mit eigenem Code, die Bildschirme, die ein Werkzeug nennen, und die Liste
der Platinen aus dem Quellcode gelesen sind. Bei den ersten beiden ist der Quellcode enger
gefasst als die Versionshinweise, und diese Seite folgt dem Quellcode.

Ebenfalls `reported`: ein kompletter Ersatzkopf für einen Kopf, der seine Werkzeuge nicht
hält oder nicht freigibt, berichtet von drei Besitzern in vier Threads. Es sind der
Besitzer mit dem Live-Chat-Angebot im Thread mit der Zusammenfassung häufiger Probleme und,
mit demselben Fall noch einmal, in einem
[Thread zur Frage, ob sich das INDX-Upgrade lohnt](https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/is-it-worth-upgrading-from-core-one-to-indx/),
ein Besitzer im Thread mit Lob für Prusas Support und einer im Thread mit der Frage, ob
Besitzer mit dem INDX zufrieden sind, der das Unternehmen nicht nennt. Kein Beitrag nennt,
um welche Edition es sich beim Kit handelt.

Schwächer: Die Größe von Bondtechs Supportteam, die zwischen beiden Unternehmen hin- und
hergeschobenen Dock-Teile und der Rat, ein Video sei der größte Beschleuniger, beruhen auf
der Zusammenfassung des Autors dieser Website; zum Video ergänzt ein Besitzer im Thread
mit der Frage, ob Besitzer mit dem INDX zufrieden sind, dass auf ein Video umgehend ein
Ersatzkopf folgte. Die genannte Eskalationsdauer und der Fall mit den zehn Videos beruhen
jeweils auf dem Bericht eines einzelnen Besitzers im Thread mit der Zusammenfassung
häufiger Probleme. Der Rat, nach mehr als einem manuellen Lösen eines festsitzenden
Werkzeugs aufzuhören, stammt allein von dem Besitzer im Thread mit Lob für Prusas Support.
Dass sich Prusas
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
eben diesem dritten Thread. Dort steht auch die von einem anderen Besitzer
wiedergegebene Antwort des Supports, nach der die kostenlose Gen-2-Hardware nur den
Frühjahrsbestellungen galt, zusammen mit dessen Hinweis, dass neue Bestellungen die
Hardware inzwischen enthalten. Die Behandlung des Gutscheins an der Kasse und der Chat, der
sie löste, sind der Bericht eines einzelnen Besitzers in einem
[Thread zum Gutschein und zum kostenlosen Versand](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/indx-refund-voucher-doesnt-work-with-free-shipping/).

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
