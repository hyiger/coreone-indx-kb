---
title:        Werkzeug entriegelt sich oder fällt aus dem Kopf
confidence:   provisional
updated:      2026-11-10
author:       hyiger
printer:      Core One
toolhead:     INDX
hotend:       unknown
nozzle:       unknown
firmware:     unstated on most reporting machines; 6.9.1-beta, 6.9.2, 7.0.1 and 8.0.0 where stated; lock, park and stuck-nozzle code source-checked at 6.9.2 and 8.0.0
sources:
  - https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/a-summary-of-common-indx-problems/
  - https://forum.prusa3d.com/forum/postid/804782/
  - https://forum.prusa3d.com/forum/prusa-indx-how-do-i-print-this-printing-help/filament-stuck-with-asa-pla-support/
  - https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/is-it-worth-upgrading-from-core-one-to-indx/
  - https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/indx-toolhead-looses-tool-when-unloading-filament-and-blobs-after-every-colorchange/
  - https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/tool-dropping/
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/flex-filament-stuck-and-cannot-dock-tool/
  - https://help.prusa3d.com/article/nozzle-tool-remains-attached-to-the-print-head-core-one-indx_1077657
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5532
  - https://help.prusa3d.com/downloads/core-one-indx
  - https://help.prusa3d.com/article/hotend-thermal-runaway-36204-indx_1088706
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/solved-tpu-tangling-at-the-extruder-after-indx-tool-changes-the-nozzle-was-too-cold-during-cleaning/
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v7.0.0
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v7.0.1
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v8.0.0
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/compare/v6.9.2...v8.0.0
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/lib/Marlin/Marlin/src/module/prusa/toolchanger_indx.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/src/feature/indx_tool_lock_hack/indx_tool_lock_hack.hpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/src/feature/indx_tool_lock_hack/indx_tool_lock_hack.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/src/marlin_stubs/M1984.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/src/gui/MItem_tools.hpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/src/common/mapi/parking.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/src/common/mapi/feedrates/standard_feedrates_indx.cpp
  - https://github.com/prusa3d/PrusaSlicer-settings-prusa-fff/blob/main/PrusaResearch/2.5.13.ini
superseded_by:
source_sha:   0bf92b69b88a14c203aad7c7646d034508ca251a9aec6e1b1f1341b2e890e649
---
# Werkzeug entriegelt sich oder fällt aus dem Kopf

!!! warning "Sechs Berichte über ausgeworfene Werkzeuge in drei Threads, eine Demontage und Berichte über festsitzende Werkzeuge mit unterschiedlich vermuteter Ursache"
    Sechs Besitzer beschreiben, dass sich das aktive Werkzeug aus dem Werkzeugkopf löst,
    vier davon in einem Thread, einer von diesen nur mit der Aussage, er habe dasselbe
    Problem wie ein anderer, und je einer in zwei anderen Threads. Einer öffnete den Kopf
    und fand an seiner eigenen Maschine eine physische Ursache. Die Besitzer in den anderen
    Threads öffneten ihre ebenfalls und beschreiben eine Verriegelung, die nicht hält,
    nennen aber kein beschädigtes Teil. Die Demontage ist ein starker Beleg für dieses eine
    Exemplar und sagt noch nichts darüber, wie verbreitet der Defekt ist. Andere Besitzer
    berichten den umgekehrten Fehler, ein Werkzeug, das sich nicht freigeben lässt: einer,
    im ersten Thread, verdächtigt die Verriegelung, Besitzer in zwei weiteren Threads
    verdächtigen Filament, das sich im Antrieb verfangen hat. `provisional`.

## Zusammenfassung

An manchen INDX-Werkzeugköpfen löst sich das aktive Werkzeug aus dem Kopf — und fällt
mitunter ganz heraus —, sobald der Extruder rückwärts läuft. Meist trifft es beim Laden
und Entladen des Filaments und bei der Düsenreinigung, wo auf das Vorwärtsextrudieren
ein Rückzug folgt, und der Drucker kann sich danach womöglich nicht selbst erholen. Ein
Besitzer führte es auf ein Zahnrad im Verriegelungsgetriebe des Werkzeugkopfs zurück,
dem der letzte Zahn fehlt oder das verformt ist. Als Abhilfe erwartet er ein
Ersatzzahnrad oder einen Ersatz-Werkzeugkopf vom Hersteller. Ein weiterer Besitzer
sieht in einem anderen Thread dieselbe Freigabe an seinem eigenen Werkzeugkopf und
bringt sie zudem mit Klecksen nach jedem Werkzeugwechsel in Verbindung; nach seiner
Aussage bestätigte der Support ein Problem am Werkzeugkopf und bot einen Ersatzkopf
an. Ein dritter Besitzer verliert in einem dritten Thread bei jedem Entladen das
Werkzeug und hat noch keine Ursache gefunden.

## Im Einzelnen

### Wie die Verriegelung vermutlich funktioniert

Das Werkzeug wird von einem Verriegelungsstift gehalten, den ein kleines Getriebe vom
Extrudermotor aus antreibt. Nach dem Verständnis der Besitzer verschiebt ein Magnet am
Dock einen Teil dieses Getriebes, sodass ein Rückwärtslauf des Extruders dort das
Werkzeug freigibt, statt Filament zurückzuziehen — und abseits eines Docks sollte ein
Rückwärtslauf stets nur zurückziehen. So beschreiben es die Besitzer im Thread, nicht die
Dokumentation des Herstellers, aber erst dadurch ergibt der folgende Fehler Sinn. Prusas
[Artikel zum manuellen Lösen](https://help.prusa3d.com/article/nozzle-tool-remains-attached-to-the-print-head-core-one-indx_1077657)
bestätigt allerdings einen Teil davon: Die Freigabe funktioniert nur, wenn das Werkzeug an
seinem Dock ausgerichtet ist oder ein Magnet an der vorderen Kerbe sitzt, an der der
Magnet des Docks angreift; abseits davon kann das Drehen des Mechanismus am Ende nur den
Extrudermotor antreiben, während das Werkzeug verriegelt bleibt. Die Einzelheiten zu
Zahnrädern, Nocke und Stift bleiben die Darstellung der Besitzer.

Prusas Firmware-Quellcode, für 7.0.0, 7.0.1 und 8.0.0 seit dem 3. November 2026
öffentlich, bestätigt mehr vom Bild der Besitzer und schränkt einen Teil davon ein. Um ein
Werkzeug aufzunehmen, lässt der Drucker den Extruder am Dock vorwärts laufen und
verriegelt es so; um eines abzulegen, bewegt er den Extruder kurz vor und zurück, um die
Zähne auszurichten, und lässt ihn dann rückwärts laufen, um die Verriegelung zu öffnen
([Quellcode des Werkzeugwechslers](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/lib/Marlin/Marlin/src/module/prusa/toolchanger_indx.cpp)).
Ein kleines, eigens für den INDX geschriebenes Modul hält in seinen Kommentaren fest, dass
der Kopf die Verriegelung erst abschließt, wenn der Extruder noch ein wenig weiter
gefördert hat, und dass ein Rückzug davor das Werkzeug herausfallen ließe. Deshalb fügt es
vor dem ersten Rückzug nach jeder Aufnahme und ebenso nach jedem Einschalten, da es sich
den Zustand des vorigen Laufs nicht merkt, eine kurze Vorwärts-und-zurück-Bewegung ein,
falls der Extruder noch nicht weit genug gefördert hat
([Quellcode des Moduls](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/src/feature/indx_tool_lock_hack/indx_tool_lock_hack.hpp),
[Aktivierung beim Einschalten](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/src/feature/indx_tool_lock_hack/indx_tool_lock_hack.cpp)).
Prusas mitgelieferter Werkzeugwechsel-G-Code ergänzt bei einem bereits vorgefüllten
Werkzeug, wenn kein Reinigungsturm verwendet wird, einen eigenen kurzen Schub, der als
abschließende Verriegelung kommentiert ist
([Profilpaket 2.5.13](https://github.com/prusa3d/PrusaSlicer-settings-prusa-fff/blob/main/PrusaResearch/2.5.13.ini)).
Ein Rückwärtslauf abseits eines Docks zieht also konstruktionsbedingt nicht immer nur
zurück: Bei einem gerade aufgenommenen Werkzeug könnte er es freigeben, und genau das
verhindert diese Absicherung. Das Modul steht schon im veröffentlichten Quellcode von
6.6.3, und es ist ebenso wie der Ablauf von Verriegeln und Freigeben in 8.0.0 bis auf
Aufräumarbeiten derselbe wie in 6.9.2
([Vergleich](https://github.com/prusa3d/Prusa-Firmware-Buddy/compare/v6.9.2...v8.0.0)).
Das ist eine Lesart des Codes, kein beobachtetes Ergebnis, und sie räumt keinen Defekt ein.
Ein Werkzeug, das sich bei einem Rückzug löst, nachdem der Extruder bereits vorwärts
gefördert hat, wie bei der Reproduktion unten, wird durch die Lücke, die die Absicherung
abdeckt, nicht erklärt; das ist eine Schlussfolgerung aus dem Code.

### Was an einer Maschine schiefging

Der Besitzer nahm eine Seite des Werkzeugkopfs ab. Einem Zahnrad im
Verriegelungsgetriebe fehlte der letzte Zahn, oder er war verformt. Ohne diesen Zahn
erreicht der Mechanismus nie die vollständig verriegelte Stellung, sodass die Nocke, die
den Stift halten sollte, nur teilweise eingreift. Beim nächsten Rückwärtslauf des
Extruders — wie bei jedem Rückzug — dreht dieses halb eingegriffene Getriebe den Stift
wieder heraus, und das Werkzeug fällt.

Er reproduzierte es gezielt. Mit aufgenommenem Werkzeug und heißer Düse hielt das
Werkzeug, solange der Extruder vorwärts lief; die E-Achse von Hand rückwärts zu drehen,
um einen Rückzug nachzuahmen, gab es frei. Das passt dazu, wann die Fehler in der Praxis
auftreten: Ein Filamentladen gelingt, weil der Extruder vorwärts läuft, und das Werkzeug
fällt beim anschließenden Rückzug heraus.

An dieser Maschine war das nicht subtil. Über einige hundert Werkzeugwechsel hinweg
brachte der Besitzer keinen einzigen Mehrwerkzeugdruck zu Ende, und viele
Einzelwerkzeugdrucke scheiterten beim anfänglichen Laden und Reinigen. Er nutzte die
Firmware 6.9.1-beta, die die oben beschriebene Absicherung bereits enthielt.

### Ein zweiter Besitzer, weniger eindeutig

Im selben Thread berichtet ein anderer Besitzer, dass das Werkzeug beim Entladen des
Filaments nahe dem Abstreifer aus dem Kopf fällt — mit PLA jedes Mal, bei mehreren
Marken, mit PETG in derselben Düse aber nicht. Er schloss Reibung im PTFE-Weg aus und
versuchte eine heißere Düse. Seinen Werkzeugkopf hat er nicht geöffnet; ob es derselbe
Zahnraddefekt ist, ist also unbekannt. Ein vom Material abhängiges Muster ist nicht das,
was ein fehlender Zahn allein erwarten ließe, und diese Seite nimmt nicht an, dass beide
dieselbe Ursache haben.

### Eine frisch umgerüstete Maschine mit Firmware 7.0.1

Am 20. Oktober 2026 antwortete ein vierter Besitzer im selben Thread auf den ersten
Beitrag des ersten Besitzers dort und schrieb, er habe dasselbe Problem. Er hatte seinen
Drucker gerade fertig umgerüstet und die Kalibrierungen durchlaufen lassen. Die
Werkzeuge 1 und 2 luden Filament normal; bei den Werkzeugen 3 und 4 gab der Kopf ein
mahlendes Geräusch von sich, und dann löste sich das Werkzeug. Als Firmware nennt er
7.0.1. Den Kopf hat er nicht geöffnet, eine Ursache nennt er nicht, und er sagt auch
nicht, bei welchem Schritt des Ladens sich das Werkzeug löste. Wie der zweite Besitzer
steuert er das Symptom bei, nicht das Zahnrad.

Fünf Tage später antwortete ein fünfter Besitzer auf diesen Beitrag: Ihm gehe es genauso,
und schlimmer noch, er könne das Filament nicht mehr aus dem Werkzeug entladen. Nach
seiner Darstellung befreiten die Vorschläge des Supports, darunter das Werkzeug aufzuheizen
und zu entladen sowie ein Cold Pull, es nicht, und der Support habe das Werkzeug als tot
aufgegeben. Über die Zustimmung zu dem beantworteten Beitrag hinaus beschreibt er die
Freigabe selbst nicht; er steuert also einen weiteren Bericht des Symptoms bei, und eines
danach verlorenen Werkzeugs, aber keine Ursache.

### Ein anderer Thread: ein zweiter geöffneter Werkzeugkopf

In einem [anderen Thread](https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/indx-toolhead-looses-tool-when-unloading-filament-and-blobs-after-every-colorchange/),
im Folgenden der Entlade-Thread genannt, berichtet ein Besitzer, der seinen Core One auf
den INDX umgerüstet hat, dass ihm das Werkzeug beim Entladen des Filaments oft aus dem
Kopf fällt. Er nahm eine Seite des Werkzeugkopfs ab und filmte den Mechanismus. Er liest
daraus, dass die Verriegelung nie ganz schließt: Das hintere Zahnrad dreht sich nicht
weit genug, und der nach vorn führende Stift hebt sich nicht weit genug. In einem seiner
Videos gab das Zurückziehen des Filaments das Werkzeug frei, statt das Filament zu
bewegen — derselbe Auslöser, den der erste Besitzer durch Drehen der E-Achse von Hand
reproduziert hatte.

Er nennt noch ein unauffälligeres Symptom. Mehrfarbige Drucke zeigen direkt nach jedem
Werkzeugwechsel Kleckse, und er führt das auf denselben Fehler zurück: Der kurze Rückzug
nach dem Vorfüllen des neu aufgenommenen Werkzeugs lockert kurz das Werkzeug, statt das
Filament zurückzuziehen, sodass das Filament kaum oder gar nicht zurückgezogen wird.
Dieser Zusammenhang ist seine Deutung seiner eigenen Videos; sonst hat ihn niemand
berichtet.

Einen fehlenden oder verformten Zahn oder ein anderes beschädigtes Teil meldet er nicht.
Ein Prusa-Mitarbeiter im Forum riet ihm, mit den Videos zum Support zu gehen. Eine Woche
nach dem ersten Beitrag schrieb der Besitzer, der Support habe den Kopf als fehlerhaft
anerkannt und einen neuen angeboten; am 18. Oktober 2026 wartete er noch darauf.

### Ein dritter Thread: das Werkzeug geht bei jedem Entladen verloren

Am 9. November 2026 eröffnete ein weiterer Besitzer einen
[eigenen Thread](https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/tool-dropping/).
Die Core One hatte das Gen-2-Upgrade und einen INDX mit acht Werkzeugen bekommen,
und nun gibt der Kopf das Werkzeug bei jedem Entladen von Filament frei, auch während
der Kalibrierung der Filamentsensoren. Der Support ließ eine Seite des Kopfes öffnen
und die Verriegelung filmen, die sich nach dieser Schilderung zu früh löst; der Fall
wurde eskaliert, ohne Ergebnis. Ein beschädigtes Teil wird nicht genannt, und in einem
späteren Beitrag kündigt der Besitzer an, den Kopf erneut zu öffnen und nach einem
abgebrochenen Zahn zu suchen. Als Firmware wird nur die jeweils neueste Version genannt.
Zuvor waren an der Hauptplatine die Leitungen des Heizbetts von denen des
Werkzeugkopfs weggelegt worden, was laut dem Besitzer viele der anfänglichen
Fehlmeldungen beseitigte; das ist eine Maßnahme gegen Störungen wie unter
[Störungen der Wägezelle](loadcell-emi-noise.md) beschrieben, und sie hat das
Herausfallen des Werkzeugs nicht beendet.

### Ein dritter Besitzer, der umgekehrte Fehler

Weiter hinten im Thread des ersten Besitzers berichtet ein dritter Besitzer das Umgekehrte: Das
Werkzeug bleibt im Kopf verriegelt, wenn es an seinem Dock freigegeben werden sollte. Sein
Verdacht, den er selbst als Vermutung kennzeichnet, ist der kleine Draht, den der
Dock-Magnet bewegt. An seinem Kopf scheint er aus der Kerbe zu rutschen, in der er sitzen
sollte, und auf das Zahnrad aufzulaufen, und er hat deutliches seitliches Spiel. Schiebt
er ihn von Hand zurück, klickt es, und das nächste Retry gibt das Werkzeug frei; in einem
Druck mit sechs Farben musste er das dreimal tun. Bei ganz abgenommener Abdeckung des
Kopfs ließ sich das Werkzeug überhaupt nicht mehr lösen — er vermutet, dass der blanke
Kopf dann auf das Magnetteil des Docks drückt —, deshalb setzte er die Originalabdeckung
lose wieder auf, um den Draht erreichbar zu halten. Er räumt ein, dass auch ein
fehlerhaftes Zahnrad wie das des ersten Besitzers die eigentliche Ursache sein könnte.
Später berichtet er, einen Ersatzkopf eingebaut zu haben; wie weit dieser Bericht trägt,
steht unten unter „Was zu tun ist“.

Das ist eine Verriegelung, die sich nicht öffnet, und nicht eine, die sich öffnet, wenn
sie es nicht soll — also nicht das Symptom, das der Rest dieser Seite beschreibt. Es steht
hier, weil es dasselbe Verriegelungsgetriebe betrifft — auch beim ersten Besitzer gab es
neben herausfallenden Werkzeugen solche, die sich nicht freigeben ließen.

### Andere Threads: ein im Kopf festsitzendes Werkzeug, Filament unter Verdacht

In einem [anderen Thread](https://forum.prusa3d.com/forum/prusa-indx-how-do-i-print-this-printing-help/filament-stuck-with-asa-pla-support/)
berichtet ein Besitzer, der ASA mit PLA als Stützmaterial druckt, dass das PLA-Werkzeug
nach ein paar Dutzend Werkzeugwechseln nicht mehr parkte, womit der Druck zu Ende war.
Das Werkzeug blieb im Kopf, und der Besitzer nahm es von Hand mit einer leichten Drehung
und etwas Kraft heraus. Der Strang steckte noch in der Düse, aber der Abschnitt, den der
Extruderantrieb greift, war verknäuelt, wenn auch nicht geschmolzen. Der
Besitzer führt das auf Wärme zurück: Die warme Kammer, die ASA braucht, und vielleicht die
schnellen Werkzeugwechsel hätten das PLA weit oben im Werkzeug erweicht. Das PLA war
bereits eine wärmebeständige Sorte. Der Besitzer fragte, ob PETG als Stützmaterial
besser geeignet wäre, und die einzige Antwort stimmte zu; ein Ergebnis wurde nicht
gemeldet.

In [einem weiteren Thread](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/flex-filament-stuck-and-cannot-dock-tool/)
hörte ein Besitzer, der flexibles Filament druckte, den Antrieb klicken, als die
Extrusion aussetzte, und danach ließ sich das Werkzeug nicht mehr andocken. Er vermutet,
dass sich das Filament um die Zahnräder gewickelt hatte und das Werkzeug im Kopf
festhielt; den Extruder rückwärts laufen zu lassen, brachte nur weiteres Klicken. Er
befreite es mit dem veröffentlichten Verfahren von Prusa zum manuellen Lösen (siehe
„Was zu tun ist“ unten). Ein zweiter Besitzer in diesem Thread hatte denselben Fehler mit
einem gewöhnlichen TPU. Die veröffentlichten Schritte lösten sein Werkzeug zunächst nicht;
mit Hilfe des Prusa-Support-Chats gelang es dann, und er stellte fest, dass der sehr
feine Schraubendreher, den er zuerst versucht hatte, zu klein war, um den Mechanismus zu
drehen. Er ergänzt, dass sich die Seitenteile des Kopfs abnehmen lassen, sodass man
verknäueltes Filament aus den Zahnrädern ziehen kann.

Beides ist das Symptom des dritten Besitzers, ein Werkzeug, das den Kopf nicht verlässt,
mit einem anderen Verdacht. Niemand hat einen Kopf geöffnet und bestätigt, dass das
Filament das Werkzeug festhielt, und nur im ASA-Fall wurde der verknäuelte Strang
tatsächlich gesehen; dort kann er ebenso gut die Folge einer Freigabe gewesen sein, die
aus anderem Grund scheiterte. Da die Freigabe über dasselbe Getriebe vom Extrudermotor
angetrieben wird (siehe oben), ist es plausibel, dass im Antrieb festsitzendes Filament
sie blockiert, aber das ist eine Schlussfolgerung. Die Kombination steht hier, weil sie
inzwischen aus zwei voneinander unabhängigen Threads stammt und auf eine Ursache
außerhalb des Verriegelungsgetriebes hinweist, die sich leicht ausschließen lässt,
besonders bei flexiblem Filament oder bei Drucken mit mehreren Materialien in einer
warmen Kammer.

Ein [späterer Thread](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/solved-tpu-tangling-at-the-extruder-after-indx-tool-changes-the-nozzle-was-too-cold-during-cleaning/)
bietet eine mögliche Ursache für das Verknäueln flexiblen Filaments, auch wenn dabei kein
Werkzeug festsaß. Am 7. November 2026 berichtete ein Besitzer mit Firmware 8.0.0, der TPU
zusammen mit PLA druckte, dass sich das TPU am Extruder verknäuelte, sobald der Drucker zu
diesem Werkzeug zurückkehrte, und beim Spülen kaum etwas herauskam; die erste Schicht war
normal gedruckt worden. Beim Lesen seines geslicten G-Codes führte er das auf den
Reinigungsschritt des mitgelieferten Werkzeugwechsel-G-Codes zurück: Dort wird die Düse
nur auf eine verringerte Reinigungstemperatur gebracht, bevor der kurze Schub folgt, der
die Verriegelung eines bereits vorgefüllten Werkzeugs abschließt; der Schub trifft also
auf Filament, das noch nicht geschmolzen ist, und weiches TPU knickt aus. Er änderte den
Werkzeugwechsel-G-Code nur für flexibles Filament, hob die Reinigungstemperatur an,
sodass der Verriegelungsschub auf wärmeres Filament trifft, und fügte eine Pause ein,
sobald die Düse wieder Drucktemperatur hat, bevor das Filament wieder vorgeschoben wird,
und seitdem verlaufen die Werkzeugwechsel nach seinem Bericht sauber. Gleichzeitig
nahm er mehrere weitere Änderungen nur für flexibles Filament vor, ohne sie einzeln zu
testen, und bezeichnet es selbst als Vermutung, dass die Temperatur der entscheidende
Punkt sei.

TODO(verify): die Regel für die Temperatur im mitgelieferten Reinigungsschritt sowie die
angehobene Temperatur und die Pause für flexibles Filament, aus dem Thread zum
verknäuelten TPU; hier zurückgehalten.

Die Reihenfolge der Schritte, die er beschreibt, stimmt mit dem mitgelieferten
Werkzeugwechsel-G-Code in Prusas Profilpaket 2.5.13 bei ausgeschaltetem Reinigungsturm
überein, wie bei ihm, hier geprüft; dass ein kalter Schub das TPU verknäuelt, ist seine
Deutung, von einem Drucker. Ein festsitzendes Werkzeug meldet er nicht. Ein am Antrieb
ausknickender Strang ist aber genau die Art Knäuel, von dem die Besitzer mit flexiblem
Filament oben glauben, dass er ihre Werkzeuge festhielt, und dies ist das erste solche
Knäuel, das sein Besitzer auf einen bestimmten Schritt des Werkzeugwechsels zurückführt;
wissenswert ist es also, wenn Sie flexibles und steifes Filament mischen. Ob es diese
festsitzenden Werkzeuge erklärt, ist eine Schlussfolgerung. Die schnellere Handhabung
flexibler Filamente in Firmware 8.0.0 spielt dafür keine Rolle. Nach Prusas Hinweisen und
dem
[Quellcode](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/src/common/mapi/feedrates/standard_feedrates_indx.cpp)
beschleunigt diese Änderung die eigenen Extruderbewegungen der Firmware bei als flexibel
gekennzeichneten Filamenten, nicht die Extruderbewegungen, die im Werkzeugwechsel-G-Code
des Slicers stehen, und dieser Besitzer hatte 8.0.0 bereits installiert.

### Die Wiederherstellung kann in einer Schleife hängen

Als ein Werkzeug im Kopf festsaß, fand der erste Besitzer den Drucker in einer Schleife
aus Andockversuchen, mit nur Retry und Abort zur Wahl. Nach einem Neustart meldete er
ein vorhandenes Werkzeug, ohne zu wissen welches, und versuchte sofort wieder, es
anzudocken — womit der Menüpunkt „Release Stuck Tool“ unerreichbar blieb. Als er diesen
Menüpunkt einmal ausprobierte, knirschten die Zahnräder, und nichts bewegte sich.

Der Quellcode, geprüft für 6.9.2 und 8.0.0, erklärt dieses Muster, ohne einen Fehler zu
zeigen. Das Folgende gilt für beide: 8.0.0 ruft die Leerlaufprüfung an einer anderen
Stelle der Hauptschleife der Firmware auf, um eine Verklemmung zu beheben, aber unter
denselben Bedingungen
([Vergleich](https://github.com/prusa3d/Prusa-Firmware-Buddy/compare/v6.9.2...v8.0.0)).
Während eines Drucks wird ein fehlgeschlagenes
Parken zweimal automatisch wiederholt; danach bietet der Drucker Retry und Abort an.
Wenn der Drucker nicht aktiv druckt (im Leerlauf oder bei pausiertem Druck), öffnet er,
sobald er eine Düse erkennt, über die er keinen Eintrag hat, eine Abfrage, die die Docks
auflistet, und versucht, das Werkzeug im
gewählten Dock abzulegen; scheitert das, kehrt er zur Liste zurück. Der Menüpunkt, den die
Firmware „Release Stuck Nozzle“ nennt und nicht so, wie der erste Besitzer ihn
bezeichnete, führt genau diese Routine aus
([Quellcode](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/src/marlin_stubs/M1984.cpp)),
er hätte also zum selben Andockversuch geführt, nicht zu einem anderen Ausweg. In beiden
Fällen besteht die Freigabe darin, dass der Extruder am Dock rückwärts läuft; bei einem
Kopf, dessen Verriegelung oder Antrieb blockiert ist, trifft also jeder Versuch auf
dasselbe Hindernis. Das ist eine Lesart des Codes, kein Test.

Ein [Firmware-Fehlerbericht](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5532),
den der zweite Besitzer aus dem Thread zum flexiblen Filament am Tag seines
festsitzenden Werkzeugs einreichte, beschreibt eine weitere Sackgasse. Nachdem ein
Entladen fehlgeschlagen war, fragte ein zweiter Entladeversuch nach dem Filamenttyp und
wartete dann darauf, dass die Düse aufheizt, was sie nie tat; auch parken ließ sich das
Werkzeug nicht. Der Bericht bezieht sich auf 6.9.2 und war am 8. November 2026 noch
offen und unbeantwortet. Weder die Versionshinweise zu Firmware 7.0.0 noch die zu
7.0.1 vom 19. Oktober 2026, deren einzige Korrektur ein Einfrieren des Druckers beim
Start betrifft, noch die zu [8.0.0](https://help.prusa3d.com/downloads/core-one-indx)
vom 22. Oktober 2026 nennen hierzu, zur Andock-Schleife oder zum Menüpunkt für eine
festsitzende Düse eine Änderung. Ebenso wenig die ausführlicheren Hinweise, die Prusa am
3. November 2026 zusammen mit dem Quellcode auf GitHub veröffentlicht hat, zu
[7.0.0](https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v7.0.0),
[7.0.1](https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v7.0.1) und
[8.0.0](https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v8.0.0). Das
hängende Entladen selbst hat diese Seite im Quellcode nicht nachverfolgt.

Ein anderer Besitzer beschreibt eine ähnliche Sackgasse mit anderem Ausgangspunkt, in
einem Kommentar vom 22. Oktober 2026 unter
[Prusas Artikel zum Fehler „Hotend Thermal Runaway“ beim INDX](https://help.prusa3d.com/article/hotend-thermal-runaway-36204-indx_1088706).
Ein großer Klumpen an seiner Düse schien den Drucker daran zu hindern, ihre Temperatur zu
messen, und er konnte das Werkzeug nicht parken, weil nach seinem Verständnis die Düse
erst aufheizen muss, bevor der Extrudermotor rückwärts läuft, um es freizugeben. Der
Quellcode bestätigt das nicht: Die Park-Routine wartet nicht auf Wärme, und die
Extruderbewegungen, die die Verriegelung öffnen, sind von der Prüfung ausgenommen, die
kaltes Extrudieren verhindert; so wie der Code zu lesen ist, braucht die Freigabe selbst
also keine heiße Düse. Ein Fehler, der den Drucker anhält, oder ein Schritt, der zuerst
aufheizt, etwa ein Entladen, wären andere Wege in dieselbe Lage; auch das ist eine Lesart
des Codes, kein Test. Zusammen mit dem Fehlerbericht oben ist sein Kommentar dennoch ein
zweiter, davon unabhängiger Fall, in dem eine Düse, die der Drucker nicht aufheizen oder
nicht messen konnte, mit einem Werkzeug einherging, das den Kopf nicht verließ. Heizt
Ihre Düse nicht auf, ist das manuelle Lösen des Herstellers unter „Was zu tun ist“ unten
womöglich der Ausweg, nicht ein weiterer Versuch über das Menü; das ist eine
Schlussfolgerung aus diesen beiden Berichten.

## Was zu tun ist

**Wenden Sie sich früh an den Support, und filmen Sie es.** Ein Werkzeug, das sich löst,
wenn der Extruder von Hand rückwärts gedreht wird, ist genau die Art Beleg, die die Frage
klärt. Der erste Besitzer hatte längst ein eskaliertes Ticket offen, bevor er die
Ursache fand. Der Besitzer im Entlade-Thread wandte sich an den Support und erhielt
nach seiner Darstellung die Bestätigung eines Problems am Werkzeugkopf und ein
Ersatzangebot. Siehe [wen Sie kontaktieren](support-and-warranty-path.md).

**Rechnen Sie mit einer Hardware-Lösung.** Keine Firmware- oder Einstellungsänderung
setzt einen Zahn wieder auf ein Zahnrad. Realistisch sind ein Ersatzzahnrad mit einer
Anleitung zum Zerlegen des Werkzeugkopfs oder ein Ersatz-Werkzeugkopf; dem Besitzer im
Entlade-Thread wurde Letzteres angeboten. Der dritte Besitzer oben, dessen Fehler der umgekehrte ist (ein Werkzeug, das verriegelt bleibt),
schreibt, Prusas Live-Chat habe ihm zugesagt, einen Ersatzkopf zu schicken. In einem
[späteren Thread zu einem anderen Thema](https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/is-it-worth-upgrading-from-core-one-to-indx/)
schreibt er, der neue Kopf sei wenige Tage nach einem kurzen Online-Chat angekommen, und
er habe ihn eingebaut. Das festsitzende Werkzeug, für dessen Befreiung jedes Mal Teile
abgebaut werden mussten, schildert er in der Vergangenheitsform, sagt aber nicht
ausdrücklich, dass der neue Kopf den Fehler behoben hat. Es bleibt der Bericht eines
einzelnen Besitzers über seinen eigenen Fall, und ein Defekt wird darin nicht benannt.

Die [Versionshinweise zu Firmware 7.0.0](https://help.prusa3d.com/downloads/core-one-indx)
vom 15. Oktober 2026 nennen nichts zur Werkzeugverriegelung, ebenso wenig die zu 7.0.1
vom 19. Oktober 2026, deren einzige Korrektur ein Einfrieren beim Start betrifft, oder
die zu 8.0.0 vom 22. Oktober 2026, und auch die ausführlicheren Hinweise auf GitHub zu
allen dreien schweigen dazu. Wie oben beschrieben, ist der Code für Verriegeln und
Freigeben in 8.0.0 bis auf Aufräumarbeiten derselbe wie in 6.9.2. Die Hinweise zu 7.0.0
verlegen allerdings die Positionen für das Laden und Entladen von Filament auf den
kalibrierten Versatz des Düsenreinigers. Im
[Quellcode](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/src/common/mapi/parking.cpp)
verschiebt diese Änderung jene Positionen, die laut einem Kommentar dort mit den Park- und
Spülpunkten über dem Abfallbehälter zusammenfallen, um den kalibrierten Versatz des
Reinigers. Jedes Entladen geschieht also neben dem Abstreifer, und „nahe dem Abstreifer“
im Bericht des zweiten Besitzers bezeichnet keinen ungewöhnlichen Ort. Weder die Hinweise
noch der Code bringen die Änderung mit diesem Fehler in Verbindung, und noch hat kein
Besitzer berichtet, ob sie das Auswerfen beim zweiten Besitzer verändert. Der Besitzer der
frisch umgerüsteten Maschine oben hatte 7.0.1 installiert, als sich zwei seiner Werkzeuge
beim Laden lösten, sagt aber nicht, wo der Kopf dabei stand.

**Wenn ein Werkzeug im Kopf festsitzt, nutzen Sie das manuelle Lösen des Herstellers.**
Prusa veröffentlicht ein
[Verfahren für ein Werkzeug, das am Kopf hängen bleibt](https://help.prusa3d.com/article/nozzle-tool-remains-attached-to-the-print-head-core-one-indx_1077657).
In groben Zügen: Bei ausgeschaltetem, vom Netz getrenntem und abgekühltem Drucker nehmen
Sie den Bauteillüfter und seine Lüfterhaube ab, bringen den Kopf an das Dock des
Werkzeugs und drehen den Freigabemechanismus mit einem schmalen Schlitzschraubendreher
durch die Zugangsöffnung in der Mitte hinter dem Lüfter, nicht durch die rechteckige
seitliche Öffnung; ein Magnet an der vorderen Kerbe, an der der Magnet des Docks
angreift, kann helfen. Folgen Sie dem Artikel selbst und nicht dieser Zusammenfassung.
Der Artikel warnt, dass ein zu großer Schraubendreher den Mechanismus beschädigen kann,
wenn man ihn mit Gewalt einsetzt; einer der Besitzer mit flexiblem Filament oben stellte
fest, dass ein zu feiner ihn ebenso wenig dreht.

**Fragen Sie, bevor Sie den Kopf öffnen.** Das Zerlegen des Werkzeugkopfs kann einen
Gewährleistungsanspruch erschweren, den der Hersteller sonst anerkennen würde. Und
schließen Sie zuerst die einfacheren Gründe aus, aus denen sich ein Werkzeug löst: eine
Platte oder ein Abstreifer, der die Docks stört, siehe
[Druckbett-Kompatibilität](../reference/build-plate-compatibility.md), und die
Dock-Kalibrierung, siehe
[Werkzeugerkennung und Parkfehler](tool-detection-ringdown-decay.md). Verlässt ein
Werkzeug den Kopf nicht, sehen Sie sich das Filament dort an, wo der Extruderantrieb es
greift, bevor Sie die Verriegelung verdächtigen; das stützt sich auf die beiden
Filament-Berichte aus anderen Threads oben. Verknäuelt sich flexibles Filament bei
Werkzeugwechseln immer wieder, enthält der TPU-Thread oben die Abhilfe eines Besitzers
für das Knäuel selbst.

## Überprüfung

`provisional` — sechs Besitzer berichten, dass sich das Werkzeug löst, vier in einem
Thread, einer davon nur durch Zustimmung zum Beitrag eines anderen, und je einer in zwei
anderen; eine physische Ursache wurde nur an einer Maschine gefunden, und die Besitzer
in den anderen Threads, die ihre Köpfe ebenfalls geöffnet haben, nennen kein
beschädigtes Teil. Ein Besitzer berichtet nur den umgekehrten Fehler, ein
Werkzeug, das sich nicht freigeben lässt; Besitzer in zwei weiteren Threads melden ein
festsitzendes Werkzeug und verdächtigen das Filament.

Die Demontage ist ein Bericht aus erster Hand und konkret: ein benanntes Bauteil, ein
beschriebener Fehler und eine Reproduktion, die den Mechanismus isoliert, indem der
Extruder von Hand angetrieben wird. Für diesen einen Werkzeugkopf ist das so schlüssig,
wie ein Forenbericht nur sein kann. Nicht belegt ist, wie verbreitet der Defekt ist —
ein schlechtes Zahnrad oder eine ganze Charge.

Der Bericht des zweiten Besitzers teilt das Symptom, bisher aber nicht die Ursache, und
sein reines PLA-Muster ist ein Grund zur Vorsicht, bevor man beides als einen Fehler
behandelt. Auch der Bericht des vierten Besitzers im selben Thread teilt nur das
Symptom: keine Demontage, keine Ursache. Auf die Stufe wirkt er sich nicht aus, zeigt
das Symptom aber an einer frisch umgerüsteten Maschine mit 7.0.1. Der des fünften
Besitzers, wieder in jenem Thread, trägt noch weniger bei: Zustimmung zum vierten und ein
Werkzeug, das der Support danach nicht freibekam.

Prusas Firmware-Quellcode ist eine Quelle aus erster Hand und bestätigt den Mechanismus,
den die Besitzer beschreiben: Die Verriegelung wird vom Extruder angetrieben, vorwärts zum
Schließen und am Dock rückwärts zum Öffnen, und ein gerade aufgenommenes Werkzeug ist
konstruktionsbedingt erst ganz verriegelt, wenn der Extruder noch ein wenig weiter
gefördert hat, wogegen die Firmware absichert. Das ist eine Eigenschaft der Konstruktion,
kein Defekt; die Stufe hebt oder senkt es also nicht. Es ist nicht die unten verlangte
Aussage des Herstellers, und es erklärt kein Werkzeug, das bei einem Rückzug nach
vorherigem Vorwärtsfördern verloren geht; dieser letzte Punkt ist eine Schlussfolgerung
aus dem Code.

Der Entlade-Thread kommt der unten genannten Schwelle am nächsten, ohne sie zu erreichen.
Es ist ein zweiter geöffneter Werkzeugkopf, in einem anderen Thread, von einem Besitzer,
der mit dem ersten nichts zu tun hat, mit demselben Auslöser — der Extruder läuft abseits
eines Docks rückwärts — und derselben Deutung des Mechanismus, einer Verriegelung, die
nie ganz schließt. Ein fehlender oder verformter Zahn wurde aber weder gefunden noch
gemeldet. Eine Verriegelung, die nicht ganz schließt, ist das, was ein schadhafter Zahn
bewirken würde, aber nicht das Einzige, was sie bewirken könnte. Die Bestätigung und das
Ersatzangebot des Supports erreichen diese Seite nur über den eigenen Beitrag des
Besitzers und benennen keinen Defekt; wie der Ersatzkopf des dritten Besitzers sind sie
daher nicht die unten verlangte Aussage des Herstellers. Der Zusammenhang mit Klecksen
nach Werkzeugwechseln ist allein die Deutung dieses Besitzers.

Der im November eröffnete Thread ist ein dritter unabhängiger Thread für das Symptom und
ein dritter Kopf, an dem der Besitzer die Verriegelung sich lösen sah, aber wieder ohne
genanntes beschädigtes Teil; auch er erfüllt die Schwelle daher nicht. Das würde er,
wenn dieser Besitzer beim erneuten Öffnen des Kopfes einen abgebrochenen oder
verformten Zahn findet.

Für sich genommen stammt das Symptom — ein Werkzeug, das durch Rückwärtsextrusion
abseits eines Docks freigegeben wird — inzwischen von unabhängigen Besitzern in zwei
verschiedenen Threads, was für das Symptom `reported` erfüllt. Die Seite bleibt
`provisional`, weil das, was sie über das Symptom hinaus beiträgt, eine Ursache ist, und
die beruht weiterhin auf einer einzigen Demontage.

Der Bericht des dritten Besitzers stammt aus dem Thread des ersten Besitzers, beschreibt
den umgekehrten Fehler und verdächtigt ein anderes Teil; auf die Stufe wirkt er sich daher nicht aus. Die
Zusage eines Ersatzkopfs und dessen spätere Ankunft gibt er selbst wieder, nicht der
Hersteller, und dabei wird kein Defekt benannt; es ist also nicht die unten verlangte
Aussage des Herstellers. Der spätere Beitrag steht zwar in einem anderen Thread, stammt
aber von demselben Besitzer und ist daher auch keine zweite Quelle.

Die beiden Filament-Berichte, aus dem ASA-Thread und dem Thread zum flexiblen Filament,
sind voneinander und von den Berichten zur Verriegelung unabhängig, und keiner beruht auf
einer Demontage. Sie beschreiben ein Werkzeug, das den Kopf nicht verließ, statt eines,
das herausfiel, und machen Filament statt eines Teils des Kopfs verantwortlich; sie heben
die Stufe also nicht und zählen auch nicht als weitere Berichte über den Fehler des
dritten Besitzers. Der TPU-Thread ist ein dritter unabhängiger Besitzer, berichtet aber
ein Knäuel ohne festsitzendes Werkzeug; er bietet eine mögliche Ursache für das Knäuel,
von einem Drucker und mit mehreren gleichzeitig vorgenommenen Änderungen, ist für sich
genommen also `provisional` und betrifft die festsitzenden Werkzeuge nur über eine
Schlussfolgerung. Der Firmware-Bericht zum hängenden Entladen stammt von einem der
Besitzer mit flexiblem Filament und ist daher keine eigene Quelle. Der Kommentar unter
Prusas Artikel zum Thermal Runaway stammt von einem anderen Besitzer. Er ist ein
einzelner Bericht, und seine Begründung dafür, dass das Werkzeug festsaß, ist das
Verständnis dieses Besitzers, nicht etwas, das Prusas Artikel sagt; der
Firmware-Quellcode, so wie er hier gelesen wird, stützt sie nicht.

Der Beitrag mit der Demontage wartete noch auf Freigabe im Forum, als diese Seite zuerst
geschrieben wurde; inzwischen ist er veröffentlicht, und der Link zeigt ihn. Das Video
des Besitzers und einige erklärende Animationen, die er gefunden hat, sind bewusst nicht
verlinkt: Das Video liegt auf einem privaten Laufwerk, und die Animationen stammen von
Reddit, das diese Website nicht zitiert.

Was es auf `reported` heben würde: derselbe fehlende oder verformte Zahn in einem zweiten
Werkzeugkopf, gemeldet in einem anderen Thread — oder eine Aussage des Herstellers, die
den Defekt anerkennt. Ein zweiter Kopf, dessen Verriegelung nicht ganz schließt, ohne
dass ein beschädigtes Teil benannt wird, genügt allein nicht.

## Verwandte Seiten

- [Werkzeugerkennung und Parkfehler](tool-detection-ringdown-decay.md) — die anderen
  Arten, auf die ein Werkzeug nicht an seinem Platz bleibt
- [Druckbett-Kompatibilität](../reference/build-plate-compatibility.md) — Platten, die
  Werkzeuge aus ihren Docks stoßen
- [Fehlgeschlagenes Entladen wegen der Bohrung der Filamentführung](filament-guide-bore-unload-failure.md) —
  wenn das Entladen scheitert, das Werkzeug aber im Kopf bleibt
- [Wen Sie kontaktieren](support-and-warranty-path.md)
