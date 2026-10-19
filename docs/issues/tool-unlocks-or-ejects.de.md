---
title:        Werkzeug entriegelt sich oder fällt aus dem Kopf
confidence:   provisional
updated:      2026-10-18
author:       hyiger
printer:      Core One
toolhead:     INDX
hotend:       unknown
nozzle:       unknown
firmware:     unknown
sources:
  - https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/a-summary-of-common-indx-problems/
  - https://forum.prusa3d.com/forum/postid/804782/
  - https://forum.prusa3d.com/forum/prusa-indx-how-do-i-print-this-printing-help/filament-stuck-with-asa-pla-support/
  - https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/is-it-worth-upgrading-from-core-one-to-indx/
  - https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/indx-toolhead-looses-tool-when-unloading-filament-and-blobs-after-every-colorchange/
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/flex-filament-stuck-and-cannot-dock-tool/
  - https://help.prusa3d.com/article/nozzle-tool-remains-attached-to-the-print-head-core-one-indx_1077657
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5532
  - https://help.prusa3d.com/downloads/core-one-indx
superseded_by:
source_sha:   f05fbfb140080a12d36ea528a022839ec4ea356d2c7456eb687e42e272f537aa
---
# Werkzeug entriegelt sich oder fällt aus dem Kopf

!!! warning "Drei Berichte über ausgeworfene Werkzeuge in zwei Threads, eine Demontage und Berichte über festsitzende Werkzeuge mit unterschiedlich vermuteter Ursache"
    Drei Besitzer beschreiben, dass sich das aktive Werkzeug aus dem Werkzeugkopf löst,
    zwei davon in einem Thread und der dritte in einem anderen. Einer öffnete den Kopf und
    fand an seiner eigenen Maschine eine physische Ursache. Der Besitzer im anderen Thread
    öffnete seinen ebenfalls und meint, die Verriegelung schließe nicht vollständig, nennt
    aber kein beschädigtes Teil. Die Demontage ist ein starker Beleg für dieses eine
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
an.

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
Einzelwerkzeugdrucke scheiterten beim anfänglichen Laden und Reinigen.

### Ein zweiter Besitzer, weniger eindeutig

Im selben Thread berichtet ein anderer Besitzer, dass das Werkzeug beim Entladen des
Filaments nahe dem Abstreifer aus dem Kopf fällt — mit PLA jedes Mal, bei mehreren
Marken, mit PETG in derselben Düse aber nicht. Er schloss Reibung im PTFE-Weg aus und
versuchte eine heißere Düse. Seinen Werkzeugkopf hat er nicht geöffnet; ob es derselbe
Zahnraddefekt ist, ist also unbekannt. Ein vom Material abhängiges Muster ist nicht das,
was ein fehlender Zahn allein erwarten ließe, und diese Seite nimmt nicht an, dass beide
dieselbe Ursache haben.

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

### Die Wiederherstellung kann in einer Schleife hängen

Als ein Werkzeug im Kopf festsaß, fand der erste Besitzer den Drucker in einer Schleife
aus Andockversuchen, mit nur Retry und Abort zur Wahl. Nach einem Neustart meldete er
ein vorhandenes Werkzeug, ohne zu wissen welches, und versuchte sofort wieder, es
anzudocken — womit der Menüpunkt „Release Stuck Tool“ unerreichbar blieb. Als er diesen
Menüpunkt einmal ausprobierte, knirschten die Zahnräder, und nichts bewegte sich.

Ein [Firmware-Fehlerbericht](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5532),
den der zweite Besitzer aus dem Thread zum flexiblen Filament am Tag seines
festsitzenden Werkzeugs einreichte, beschreibt eine weitere Sackgasse. Nachdem ein
Entladen fehlgeschlagen war, fragte ein zweiter Entladeversuch nach dem Filamenttyp und
wartete dann darauf, dass die Düse aufheizt, was sie nie tat; auch parken ließ sich das
Werkzeug nicht. Der Bericht bezieht sich auf 6.9.2 und war am 18. Oktober 2026 noch
offen. Die Versionshinweise zu Firmware 7.0.0 nennen weder hierzu noch zur
Andock-Schleife noch zum Menüpunkt „Release Stuck Tool“ eine Änderung.

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
vom 15. Oktober 2026 nennen nichts zur Werkzeugverriegelung. Sie verlegen allerdings die
Positionen für das Laden und Entladen von Filament auf den kalibrierten Versatz des
Düsenreinigers. Die Hinweise bringen das nicht mit diesem Fehler in Verbindung, und noch
hat kein Besitzer berichtet, ob es das Auswerfen nahe dem Abstreifer verändert, das der
zweite Besitzer beschreibt.

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
Filament-Berichte aus anderen Threads oben.

## Überprüfung

`provisional` — drei Besitzer berichten, dass sich das Werkzeug löst, zwei in einem
Thread und einer in einem anderen; eine physische Ursache wurde nur an einer Maschine
gefunden, und der Besitzer im anderen Thread, der seinen Kopf ebenfalls geöffnet hat,
nennt kein beschädigtes Teil. Ein Besitzer berichtet nur den umgekehrten Fehler, ein
Werkzeug, das sich nicht freigeben lässt; Besitzer in zwei weiteren Threads melden ein
festsitzendes Werkzeug und verdächtigen das Filament.

Die Demontage ist ein Bericht aus erster Hand und konkret: ein benanntes Bauteil, ein
beschriebener Fehler und eine Reproduktion, die den Mechanismus isoliert, indem der
Extruder von Hand angetrieben wird. Für diesen einen Werkzeugkopf ist das so schlüssig,
wie ein Forenbericht nur sein kann. Nicht belegt ist, wie verbreitet der Defekt ist —
ein schlechtes Zahnrad oder eine ganze Charge.

Der Bericht des zweiten Besitzers teilt das Symptom, bisher aber nicht die Ursache, und
sein reines PLA-Muster ist ein Grund zur Vorsicht, bevor man beides als einen Fehler
behandelt.

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
dritten Besitzers. Der Firmware-Bericht zum hängenden Entladen stammt von einem der
Besitzer mit flexiblem Filament und ist daher keine eigene Quelle.

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
