---
title:        Verrutschen der Silikonsocke über den Temperatursensor
confidence:   provisional
updated:      2026-10-25
author:       hyiger
printer:      Core One
toolhead:     INDX
hotend:       unknown
nozzle:       unknown
firmware:     unknown
sources:
  - https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/indx-maintenance/
  - https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/nozzle-wiper-vs-indx-offset-sensor/
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/problems-with-nozzle-socks/
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/filament-blobs-can-tear-the-silicon-sock-on-indx-nozzles/
  - https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/missing-layers-5/
  - https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/bondtech-nozzles-dont-ship/
  - https://help.prusa3d.com/article/hotend-thermal-runaway-36204-indx_1088706
  - https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/core-1-indx-generic-petg-preset-hotend-thermal-runaway-error/
superseded_by:
source_sha:   fb232a9af4b7ec4a9519fa78b4cfdb7fddfc9458f07c68c287062c53c07759cb
---
# Verrutschen der Silikonsocke über den Temperatursensor

!!! warning "Eine aus einzelnen Berichten zusammengesetzte Kette"
    Jedes Glied dieser Kette wird von jemandem berichtet. Die **Kette als Ganzes** —
    verrutschte Socke führt zu Überhitzung, führt zu Anbackungen, führt zum Fehlschlagen
    der Kalibrierung — stammt aus einem einzigen Bericht. Lesen Sie den Abschnitt
    Überprüfung, bevor Sie sie als gesichert behandeln.

## Zusammenfassung

Die Silikonsocke einer INDX-Düse kann so weit aus ihrer Sitzposition nach oben wandern,
dass sie das rechteckige Messfeld an der Düse teilweise verdeckt, offenbar das Ziel, an
dem der Werkzeugkopf die Temperatur der Düse abliest (Prusas Artikel zum Thermal Runaway
fordert dazu auf, ein „measuring pad“ sauber zu halten, setzt diese Bezeichnung aber
nicht ausdrücklich mit diesem Rechteck gleich). Bei
teilweise verdecktem Messfeld läuft die Düse heißer als vorgegeben. Bei der PET-Familie,
nach der Erfahrung des Autors dieser Seite vor allem bei PCTG, backt die überschüssige
Hitze Filament an der Düsenspitze fest, und die entstehende Ablagerung reicht aus, um
die Werkzeug-Offset-Kalibrierung scheitern zu lassen.

Die Abhilfe ist trivial, sobald man weiß, wonach zu suchen ist: die Socke wieder nach
unten setzen. Der Grund, davon zu wissen, ist, dass sämtliche Symptome auf etwas anderes
hindeuten — auf die Düse, auf das Filament oder auf den Offset-Sensor.

## Nicht der Offset-Sensor

**Es handelt sich um einen Temperatursensor, nicht um den Werkzeug-Offset-Sensor.** Das
sind unterschiedliche Bauteile mit unterschiedlichen Messprinzipien, und die
Unterscheidung ist wichtig, weil das Symptom — fehlgeschlagene Offset-Kalibrierung — auf
das falsche Bauteil deutet.

Der Autor dieser Seite hat das verdeckte Teil in mehr als einem Thread teils als
IR-Fenster und teils als Rechteck des Temperatursensors beschrieben. Beide
Beschreibungen sind thermischer Natur. Der
Werkzeug-Offset-Sensor ist an anderer Stelle als wirbelstrombasiert dokumentiert, und
Wirbelstrommessung hat kein optisches Fenster, das verdeckt werden könnte. Siehe
[Ausfall der Offset-Sensorplatine](offset-sensor-board-failure.md) zu diesem Bauteil.

Der Eröffnungsbeitrag des Wartungs-Threads, von einem anderen Besitzer, nennt das Teil
vor dem Werkzeug unabhängig davon ein Fenster zur Temperaturerfassung; der
Reinigungshinweis unter dieser Überschrift ist allerdings aus zweiter Hand
weitergegeben, und als Symptom eines verschmutzten Fensters nennt er schlechtes
Abtasten des Druckbetts, nicht einen Temperaturfehler. Nicht nur diese Seite ist
unsicher, welches Teil gemeint ist: Am 25. September 2026 fragte ein anderer Besitzer in
jenem Thread, ob das kleine Fenster, das laut dem Eröffnungsbeitrag sauber zu halten
ist, dieses Rechteck meint oder ein anderes Teil, und an diesem Tag war die Frage noch
unbeantwortet.

Prusas eigene Dokumentation kommt einer Klärung nahe, wozu das Rechteck dient. Laut
[Prusas Artikel zum Fehler „Hotend Thermal Runaway“ beim INDX](https://help.prusa3d.com/article/hotend-thermal-runaway-36204-indx_1088706)
schickt die Bildschirmmeldung des Fehlers den Besitzer zum schwarzen Rechteck am
Werkzeug, das der Artikel „heat block“ nennt, um es auf Verschmutzung zu prüfen; und
wenn der Fehler auf eine Düse beschränkt ist, soll man sich vergewissern, dass das
„measuring pad“ sauber und frei von Ablagerungen ist. Zusammengenommen, und nach der
Bezeichnung „measuring pad“, ist das Rechteck offenbar das Ziel, an dem die Temperatur
der Düse abgelesen wird; der Artikel sagt das allerdings nicht ausdrücklich und sagt
auch nicht direkt, dass beide Bezeichnungen dasselbe Teil meinen. Dass Verschmutzung darauf einen
Thermal-Runaway-Fehler auslösen kann, legt schon die Bildschirmmeldung nahe. Der
Artikel nennt das Messprinzip nicht und erwähnt die Socke nicht. Besitzer, die darunter
kommentieren, nennen den Sensor ebenso wie der Autor dieser Seite an anderer Stelle
einen Infrarotsensor; der Hersteller sagt das dort nicht.

TODO(verify): ob das Fenster, das laut dem Eröffnungsbeitrag des Wartungs-Threads
sauber zu halten ist, das Messfeld an der Düse ist oder ein anderes Teil des Kopfs, und
nach welchem Messprinzip der Temperatursensor des Werkzeugkopfs tatsächlich arbeitet.
Prusas Artikel deutet darauf hin, wozu das Messfeld dient, beschreibt aber keines von
beiden.

## Im Einzelnen

### Wandern der Socke

Berichten zufolge rutscht die Socke aus ihrer Sitzposition nach oben. Der Autor dieser
Seite fand sie in einer Position vor, in der sie den Temperatursensor teilweise
verdeckte, und erhielt als unmittelbare Folge einen Thermal-Runaway-Fehler — ein
Erfahrungsbericht aus erster Hand zur Verdeckung und ihrer unmittelbaren Konsequenz —
und hatte bis Ende August die Socke an drei Düsen einer Maschine wieder zurechtgesetzt.
Ein anderer Besitzer musste sie, als Antwort in dem [Thread](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/problems-with-nozzle-socks/), in dem der Autor
diese drei Düsen gemeldet hatte, nach nur wenigen Testdrucken an zwei Werkzeugen wieder
zurechtsetzen.

Ein dritter Besitzer hat inzwischen den ersten Bericht außer dem des Autors geliefert,
in dem eine verschobene Socke und ein Thermal-Runaway-Fehler zusammenkommen. In einem
Kommentar vom 23. Oktober 2026 unter
[Prusas Artikel zu diesem Fehler](https://help.prusa3d.com/article/hotend-thermal-runaway-36204-indx_1088706)
berichtet er, dass der Fehler auf seinem frisch umgerüsteten Drucker zwei Drucke
abgebrochen hat, beide Male am selben Werkzeug. An diesem Werkzeug fand er die Socke so
verschoben, dass sie das Messfeld teilweise verdeckte, und schob sie von Hand zurück. Ob
die Fehler damit aufgehört haben, hatte er noch nicht gemeldet. Eine verschobene Socke
über dem Messfeld wurde damit inzwischen an drei Maschinen beobachtet; dieser Besitzer
sagt nicht, ob sich seine im Betrieb verschoben hat oder nach dem Umbau nie richtig
saß. In einem
[anderen Thread](https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/missing-layers-5/)
nannte der Autor eine hochgerutschte Socke als eine mögliche Ursache für fehlende
Schichten bei einem anderen Besitzer; dieser sah nach, fand die Socke unverändert an
ihrem Platz und führte den Fehler später auf den Slicer zurück.

Warum sie wandert, ist nicht geklärt. Der Autor dieser Seite hat inzwischen das
Schrubben der Düse mit einer Messingbürste als einen Weg genannt, auf dem die Socke nach
oben gezogen wird, in einem
[Thread zu einem Thermal-Runaway-Fehler](https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/core-1-indx-generic-petg-preset-hotend-thermal-runaway-error/),
doch kein Bericht führt ein bestimmtes Verrutschen darauf zurück, und weder der
Hersteller noch die Community haben eine Ursache veröffentlicht.

Ein Thermal-Runaway-Fehler allein belegt noch keine verrutschte Socke. Im selben Thread
schloss ein Besitzer, dessen PETG-Drucke an mehr als einer Düse von diesem Fehler
abgebrochen wurden, anhand eines von ihm geposteten Fotos, dass seine Socken richtig
saßen. Nach seiner Darstellung führte der Prusa-Support es auf das generische
PETG-Profil zurück. Das Trocknen des Filaments brachte einen kleinen Druck durch, ein
größerer scheiterte aber erneut, und die Ursache war am 24. Oktober 2026 noch offen.

### Überhitzung und Anbackungen

Ein teilweise verdeckter Temperatursensor misst zu niedrig, sodass die Heizung stärker
nachregelt, um einen Sollwert zu erreichen, den die Maschine für noch nicht erreicht
hält. Die Düse läuft dann oberhalb der vorgegebenen Temperatur.

Dass Filament an INDX-Düsenspitzen anbackt, wird auch außerhalb der Kette dieser Seite
berichtet und hängt nicht davon ab, ob sie zutrifft, ist aber nur dünn belegt: Ein
anderer Besitzer beschreibt, dass vor allem PETG bereitwillig an diesen Düsen haften
bleibt, und der Autor dieser Seite berichtet dasselbe von PCTG. Der Autor führt das
teilweise auf die Geometrie der Socke zurück und merkt an, dass sie fast bis zur Spitze
reicht, sodass Ablagerungen etwas zum Anhaften finden. Früher im selben Thread sagte der
Autor allerdings, dass ein bestimmtes PCTG, das er verwendet — eine einzige Marke und
Farbe —, auf allen seinen Druckern an der Düse haften bleibt und kleine Klumpen
hinterlässt, nicht nur am INDX; zumindest für dieses Filament grenzt sein PCTG-Bericht
also weder die INDX-Düse noch ihre Socke als Ursache ab. Ein zweiter Besitzer im selben
Thread sieht ebenfalls PETG-Klumpen, ist aber nicht überzeugt, dass während des Drucks
Material an der Düse haften bleibt, und führt es stattdessen darauf zurück, dass der
Abstreifer nicht sauber zurückgelassen wird. Im selben Thread wurden beschichtete Düsen
als Material besser abweisend ins Spiel gebracht, doch ein anderer Besitzer dort sieht
keinen Unterschied: PETG setzt sich nach dessen Erfahrung an beschichteten Düsen ebenso
bereitwillig fest wie an unbeschichteten. Dieser Vergleich ist also umstritten. Wie das
Wandern im Betrieb stützt sich die Aussage zu den Anbackungen auf einen unabhängigen
Besitzer in einem Thread und ist daher für sich genommen `provisional`.

Dass Überhitzung dies verschlimmert, ist mechanistisch plausibel und entspricht dem, was
der einzige Bericht über die vollständige Kette beschreibt, ist aber eine Schlussfolgerung
und kein gemessener Zusammenhang.

### Fehlschlagen der Kalibrierung

Eine Ablagerung an der Düsenspitze verändert das, was der Offset-Sensor erfasst. Die
Werkzeug-Offset-Kalibrierung schlägt dann fehl. Das schließt an die vorhandene
Darstellung an, wonach Verschmutzung die Kalibrierung unterläuft, siehe
[Nachsickern beim Abtasten](oozing-during-probing-and-calibration.md) — ein anderer Weg
zum selben Ergebnis.

## Was zu tun ist

**Prüfen Sie die Socke, bevor Sie irgendetwas anderem nachgehen.** Wenn die
Offset-Kalibrierung an einem Werkzeug zu scheitern beginnt, das zuvor einwandfrei lief,
sehen Sie nach, ob die Socke über das Messfeld gewandert ist, bevor Sie den Sensor,
die Düse oder das Filament untersuchen. Das kostet Sekunden und ist umkehrbar. Dasselbe
gilt für einen Hotend-Thermal-Runaway-Fehler, bei dem Prusas Artikel eine hilfreiche
Grenze zieht: Bleibt der Fehler bei einer Düse, prüfen Sie deren Messfeld; wandert er
mit dem Kopf von Düse zu Düse, wenden Sie sich an den Support.

**Setzen Sie sie wieder nach unten.** Jeder Bericht über das Wandern beschreibt, dass
die Socke einfach wieder in Position geschoben wurde, und keiner brauchte dafür ein
Ersatzteil.

**Kurz ohne Socke zu drucken ist laut Hersteller unbedenklich — eine Lösung ist es
nicht.** Der After-Sales-Support des Herstellers teilte dem Autor dieser Seite direkt
mit, dass ein Werkzeug eine kurze Zeit ohne Socke laufen kann, ohne dass es ein Problem
gibt. Das geht einer früheren Warnung auf dieser Seite vor, die auf der eigenen Lesart
des Firmware-Quellcodes durch den Autor beruhte: dass die Temperaturmessung der Düse eine
montierte Socke voraussetzt und der Messwert ohne sie so weit abweichen könnte, dass ein
Thermal-Runaway-Fehler ausgelöst wird. Weit auseinander liegen beide nicht. Die Antwort
des Herstellers gilt für eine kurze Zeit, und die Befürchtung wurde nie getestet —
behandeln Sie eine fehlende Socke also als Notbehelf, bis Ersatz da ist, nicht als
Mittel gegen das Wandern oder als Dauerzustand.

**Prüfen Sie die Socken von Zeit zu Zeit.** Ohne bekannten Auslöser und ohne Behebung
ist Nachsehen der einzige Schutz. Nach einem Klumpen lohnt es sich besonders: An der
Maschine des Autors wurde ein an der Düsenspitze haftender PCTG-Klumpen so fest durch
den Abstreifer gezogen, dass die Socke riss. Nach Ansicht des Autors lohnt sich ein
Blick auch nach dem Bürsten der Spitze, aus dem oben unter „Wandern der Socke“
genannten Grund. Ersatzsocken lagen dem Bausatz nicht bei. Der Hersteller teilte dem Autor
dieser Seite inzwischen mit, dass Socken bald als Fünferpack in seinem Shop erhältlich
sein werden, zu 4,90 USD laut Angabe vom September 2026; wenige Tage später waren sie
dort gelistet, mit Stand 19. September allerdings nicht lieferbar. Mindestens eine
Bestellung ist inzwischen verschickt worden: Ein Besitzer berichtet, dass Socken, die er dort am 8. Oktober
2026 zusammen mit Düsen bestellt hatte, eine Woche später versandt wurden. Ein anderer
Besitzer erhielt vom Prusa-Support die Auskunft, dass Socken später auch im Prusa-Shop
ins Sortiment kommen; der Prusa-Shop führt
inzwischen einzelne INDX-Teile, darunter einen [Werkzeughalter mit Magneten](https://www.prusa3d.com/product/tool-holder-with-magnets-2/) und
das [Filamentsensor-Kabel für den INDX](https://www.prusa3d.com/product/filament-sensor-cable-for-indx/); Sensorplatinen und Silikonabstreifer
sollen dort ebenfalls erhältlich sein. Beim Autor dieser Seite kosteten Versand und Einfuhrabgaben ein Mehrfaches der
Socke selbst; solange keine nähere Bezugsquelle sie führt, kann eine gerissene Socke also
weiterhin Wartezeit und Kosten bedeuten.

**Reinigen Sie die Spitze, wenn bereits Material festgebacken ist.** Siehe
[Nachsickern beim Abtasten](oozing-during-probing-and-calibration.md) für die
Vorsichtsmaßnahme beim Reinigen — Ablagerungen entfernen, nicht polieren.

## Überprüfung

`provisional` — die Kette stützt sich auf einen einzigen Bericht.

Was von anderen Besitzern als dem Autor bestätigt wird:

- **Wandern der Socke, an zwei Maschinen.** Der Bericht aus erster Hand im
  [Wartungs-Thread](https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/indx-maintenance/)
  über einen genau dadurch verursachten Thermal-Runaway-Fehler stammt vom Autor selbst,
  ebenso der Bericht über die drei Düsen. Die unabhängige Bestätigung ist ein zweiter
  Besitzer in [einem späteren Thread](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/problems-with-nozzle-socks/), der die Socke an zwei Werkzeugen wieder
  zurechtsetzen musste. Jener Thread wurde vom Autor dieser Seite eröffnet, der
  bestätigende Bericht stammt aber von einem anderen Besitzer, weshalb er zählt. Ein
  unabhängiger Besitzer in einem Thread erfüllt `reported` nicht, also ist auch die
  Aussage zum Wandern für sich genommen `provisional`. Frühere Fassungen dieser Seite
  hielten den Bericht im Wartungs-Thread für den eines zweiten Besitzers und stuften das
  Wandern auf dieser Grundlage als `reported` ein; das war falsch.
- **Eine verschobene Socke über dem Messfeld, ein weiterer Besitzer.** Ein dritter
  Besitzer fand, in einem Kommentar unter
  [Prusas Artikel zum Thermal Runaway](https://help.prusa3d.com/article/hotend-thermal-runaway-36204-indx_1088706),
  eine verschobene Socke teilweise über dem Messfeld an genau dem Werkzeug, das seine
  Drucke zweimal abgebrochen hatte. Sein Drucker war frisch umgerüstet, und er sagt
  nicht, ob sich die Socke im Betrieb verschoben hat oder nie richtig saß; das ist also
  eine Verschiebung, kein Hochwandern im Betrieb. Für eine verschobene Socke über dem
  Messfeld, im Unterschied zum Wandern, gibt es damit inzwischen zwei unabhängige
  Besitzer an zwei verschiedenen Orten, doch die Aussage zum Wandern bleibt für sich
  genommen `provisional`. Prusas Artikel selbst nennt Ablagerungen auf dem Messfeld unter
  den Punkten, die bei diesem Fehler zu prüfen sind, erwähnt die Socke aber nicht; dass
  die verschobene Socke diese Fehler verursachte, ist die eigene Vermutung dieses
  Besitzers, deren Ergebnis noch nicht gemeldet ist, und diese Verbindung ist daher
  `provisional`.
- **Anbacken der PET-Familie an INDX-Düsenspitzen**, von einem anderen Besitzer im
  [Wischer-Thread](https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/nozzle-wiper-vs-indx-offset-sensor/);
  ein zweiter Besitzer dort sieht die Klumpen ebenfalls, führt sie aber auf den
  Abstreifer zurück, nicht auf die Düse. Das ist ein unabhängiger Besitzer in einem
  Thread, also ist die Aussage zu den Anbackungen für sich genommen `provisional`.
  Der Bericht zu PCTG und die Beobachtung, dass die Geometrie der Socke
  dazu beiträgt, stammen vom Autor selbst, im selben Thread, in dem er auch angibt, dass
  das eine von ihm genannte PCTG auf allen seinen Druckern haftet, nicht nur am INDX.

**Nicht** bestätigt ist die Ursachenkette, die beides verbindet: dass die Verdeckung die
Anbackungen antreibt und dass die Anbackungen die Kalibrierung scheitern lassen. Das ist
die eigene Beobachtung des Autors dieser Seite aus erster Hand, wiederholt an drei Düsen
einer Maschine — deshalb existiert diese Seite —, aber es bleiben eine Maschine und ein
Beobachter, und es wurde keine Temperatur gemessen. Beide Enden sind einzeln belegt; die
Verbindung dazwischen ist erschlossen.

Die Einschätzung, dass Düse oder Socke überarbeitet werden müssten, ist die
Schlussfolgerung dieses Autors und keine Herstellerposition; sie wird als Meinung
festgehalten, nicht als Befund. Ebenso zwei spätere Ergänzungen, beide vom Autor selbst
und von einer einzigen Maschine: die von einem Klumpen zerrissene Socke und die
Versandkosten für Ersatzteile. Ebenso die Vermutung des Autors, dass das Bürsten der
Spitze die Socke nach oben zieht. Der PETG-Fall mit Thermal Runaway im selben Thread
stammt von einem einzelnen Besitzer und ist ungelöst. Er wird nur als Warnung davor
angeführt, jeden solchen Fehler als verrutschte Socke zu deuten, nicht als Beleg zur
Socke.

Die Hinweise zum Betrieb ohne Socke und zum kommenden Fünferpack stammen vom Hersteller —
sie kamen jedoch als private Antwort an den Autor dieser Seite, sind also aus erster Hand
und für Leser dennoch nicht überprüfbar, und sind deshalb hier als `provisional`
markiert. Sie ersetzen eine frühere Warnung davor, die Socke zu entfernen, die eine nie
getestete Schlussfolgerung des Autors aus dem Firmware-Quellcode war. Was der
Prusa-Support zur Aufnahme von Socken ins Sortiment sagte, ist aus Antworten eines
anderen Besitzers in einem [vom Autor eröffneten Thread](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/filament-blobs-can-tear-the-silicon-sock-on-indx-nozzles/) weitergegeben und von
keinem der Unternehmen veröffentlicht. Dass inzwischen eine Sockenbestellung aus dem Shop
des Herstellers verschickt wurde, stützt sich auf den Beitrag eines einzelnen Besitzers
in einem
[Thread über Düsenlieferungen](https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/bondtech-nozzles-dont-ship/).

Was diese Seite auf `reported` heben würde: ein zweiter Besitzer, der die vollständige
Abfolge — verschobene Socke, dann Überhitzung, dann Anbackungen, dann fehlgeschlagene
Kalibrierung — an einem zitierbaren Ort beschreibt. Eine Messung der tatsächlichen
gegenüber der vorgegebenen Düsentemperatur bei teilweise verdecktem Sensor wäre noch
besser und würde die Mitte der Kette auf `measured` heben.

## Verwandte Seiten

- [Ausfall der Offset-Sensorplatine](offset-sensor-board-failure.md) — der
  Wirbelstromsensor, mit dem dies häufig verwechselt wird
- [Nachsickern beim Abtasten](oozing-during-probing-and-calibration.md) — Verschmutzung,
  die die Kalibrierung auf anderem Weg unterläuft
- [Düsenhärte](nozzle-hardness.md) — weitere Defekte auf Düsenebene
