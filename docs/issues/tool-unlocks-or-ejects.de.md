---
title:        Werkzeug entriegelt sich oder fällt aus dem Kopf
confidence:   provisional
updated:      2026-10-08
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
superseded_by:
source_sha:   184c3a990626fc977d14921977f9468469a66747c6f71457b475711b35a5a489
---
# Werkzeug entriegelt sich oder fällt aus dem Kopf

!!! warning "Zwei Berichte über ausgeworfene Werkzeuge, eine Demontage und zwei über festsitzende Werkzeuge mit unterschiedlich vermuteter Ursache"
    Zwei Besitzer beschreiben, dass sich das aktive Werkzeug aus dem Werkzeugkopf löst.
    Einer von ihnen öffnete den Kopf und fand an seiner eigenen Maschine eine physische
    Ursache. Das ist ein starker Beleg für dieses Exemplar und sagt noch nichts darüber,
    wie verbreitet der Defekt ist. Ein dritter Besitzer im selben Thread berichtet den
    umgekehrten Fehler, ein Werkzeug, das sich nicht freigeben lässt, und ein vierter, in
    einem anderen Thread, hatte ein im Kopf festsitzendes Werkzeug und verdächtigt dabei
    sein Filament, nicht die Verriegelung. `provisional`.

## Zusammenfassung

An manchen INDX-Werkzeugköpfen löst sich das aktive Werkzeug aus dem Kopf — und fällt
mitunter ganz heraus —, sobald der Extruder rückwärts läuft. Meist trifft es beim Laden
des Filaments und bei der Düsenreinigung, wo auf das Vorwärtsextrudieren ein Rückzug
folgt, und der Drucker kann sich danach womöglich nicht selbst erholen. Ein Besitzer
führte es auf ein Zahnrad im Verriegelungsgetriebe des Werkzeugkopfs zurück, dem der
letzte Zahn fehlt oder das verformt ist. Als Abhilfe erwartet er ein Ersatzzahnrad oder
einen Ersatz-Werkzeugkopf vom Hersteller.

## Im Einzelnen

### Wie die Verriegelung vermutlich funktioniert

Das Werkzeug wird von einem Verriegelungsstift gehalten, den ein kleines Getriebe vom
Extrudermotor aus antreibt. Nach dem Verständnis der Besitzer verschiebt ein Magnet am
Dock einen Teil dieses Getriebes, sodass ein Rückwärtslauf des Extruders dort das
Werkzeug freigibt, statt Filament zurückzuziehen — und abseits eines Docks sollte ein
Rückwärtslauf stets nur zurückziehen. So beschreiben es die Besitzer im Thread, nicht die
Dokumentation des Herstellers, aber erst dadurch ergibt der folgende Fehler Sinn.

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

### Ein dritter Besitzer, der umgekehrte Fehler

Weiter hinten im selben Thread berichtet ein dritter Besitzer das Umgekehrte: Das
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

### Ein anderer Thread: ein im Kopf festsitzendes Werkzeug, Filament unter Verdacht

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

Das ist das Symptom des dritten Besitzers, ein Werkzeug, das den Kopf nicht verlässt,
mit einem anderen Verdacht, und niemand hat den Kopf geöffnet. Ob der verknäuelte Strang
das Werkzeug festgehalten hat oder die Folge einer Freigabe war, die aus anderem Grund
scheiterte, ist nicht geklärt. Es steht hier, weil es auf eine Ursache außerhalb des
Verriegelungsgetriebes hinweist, die sich leicht ausschließen lässt, besonders bei
Drucken mit mehreren Materialien in einer warmen Kammer.

### Die Wiederherstellung kann in einer Schleife hängen

Als ein Werkzeug im Kopf festsaß, fand der erste Besitzer den Drucker in einer Schleife
aus Andockversuchen, mit nur Retry und Abort zur Wahl. Nach einem Neustart meldete er
ein vorhandenes Werkzeug, ohne zu wissen welches, und versuchte sofort wieder, es
anzudocken — womit der Menüpunkt „Release Stuck Tool“ unerreichbar blieb. Als er diesen
Menüpunkt einmal ausprobierte, knirschten die Zahnräder, und nichts bewegte sich.

## Was zu tun ist

**Wenden Sie sich früh an den Support, und filmen Sie es.** Ein Werkzeug, das sich löst,
wenn der Extruder von Hand rückwärts gedreht wird, ist genau die Art Beleg, die die Frage
klärt. Der Besitzer hier hatte längst ein eskaliertes Ticket offen, bevor er die Ursache
fand. Siehe [wen Sie kontaktieren](support-and-warranty-path.md).

**Rechnen Sie mit einer Hardware-Lösung.** Keine Firmware- oder Einstellungsänderung
setzt einen Zahn wieder auf ein Zahnrad. Realistisch sind ein Ersatzzahnrad mit einer
Anleitung zum Zerlegen des Werkzeugkopfs oder ein Ersatz-Werkzeugkopf. Der dritte
Besitzer oben, dessen Fehler der umgekehrte ist (ein Werkzeug, das verriegelt bleibt),
schreibt, Prusas Live-Chat habe ihm zugesagt, einen Ersatzkopf zu schicken. In einem
[späteren Thread zu einem anderen Thema](https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/is-it-worth-upgrading-from-core-one-to-indx/)
schreibt er, der neue Kopf sei wenige Tage nach einem kurzen Online-Chat angekommen, und
er habe ihn eingebaut. Das festsitzende Werkzeug, für dessen Befreiung jedes Mal Teile
abgebaut werden mussten, schildert er in der Vergangenheitsform, sagt aber nicht
ausdrücklich, dass der neue Kopf den Fehler behoben hat. Es bleibt der Bericht eines
einzelnen Besitzers über seinen eigenen Fall, und ein Defekt wird darin nicht benannt.

**Fragen Sie, bevor Sie den Kopf öffnen.** Das Zerlegen des Werkzeugkopfs kann einen
Gewährleistungsanspruch erschweren, den der Hersteller sonst anerkennen würde. Und
schließen Sie zuerst die einfacheren Gründe aus, aus denen sich ein Werkzeug löst: eine
Platte oder ein Abstreifer, der die Docks stört, siehe
[Druckbett-Kompatibilität](../reference/build-plate-compatibility.md), und die
Dock-Kalibrierung, siehe
[Werkzeugerkennung und Parkfehler](tool-detection-ringdown-decay.md). Verlässt ein
Werkzeug den Kopf nicht, sehen Sie sich das Filament dort an, wo der Extruderantrieb es
greift, bevor Sie die Verriegelung verdächtigen; das stützt sich auf den einzelnen
Bericht aus dem anderen Thread oben.

## Überprüfung

`provisional` — drei Besitzer in einem Thread und eine physische Ursache, gefunden an
nur einer Maschine; ein Besitzer berichtet nur den umgekehrten Fehler, ein Werkzeug, das
sich nicht freigeben lässt; ein vierter Besitzer in einem anderen Thread meldet ein
festsitzendes Werkzeug und verdächtigt das Filament.

Die Demontage ist ein Bericht aus erster Hand und konkret: ein benanntes Bauteil, ein
beschriebener Fehler und eine Reproduktion, die den Mechanismus isoliert, indem der
Extruder von Hand angetrieben wird. Für diesen einen Werkzeugkopf ist das so schlüssig,
wie ein Forenbericht nur sein kann. Nicht belegt ist, wie verbreitet der Defekt ist —
ein schlechtes Zahnrad oder eine ganze Charge.

Der Bericht des zweiten Besitzers teilt das Symptom, bisher aber nicht die Ursache, und
sein reines PLA-Muster ist ein Grund zur Vorsicht, bevor man beides als einen Fehler
behandelt.

Der Bericht des dritten Besitzers stammt aus demselben Thread, beschreibt den umgekehrten
Fehler und verdächtigt ein anderes Teil; auf die Stufe wirkt er sich daher nicht aus. Die
Zusage eines Ersatzkopfs und dessen spätere Ankunft gibt er selbst wieder, nicht der
Hersteller, und dabei wird kein Defekt benannt; es ist also nicht die unten verlangte
Aussage des Herstellers. Der spätere Beitrag steht zwar in einem anderen Thread, stammt
aber von demselben Besitzer und ist daher auch keine zweite Quelle.

Der Bericht aus dem anderen Thread ist ein einzelner, ohne Demontage. Er beschreibt ein
Werkzeug, das den Kopf nicht verließ, statt eines, das herausfiel, und macht erweichtes
Filament statt eines Teils des Kopfs verantwortlich; er hebt die Stufe also nicht und
zählt auch nicht als zweiter Bericht über den Fehler des dritten Besitzers.

Der Beitrag mit der Demontage wartete noch auf Freigabe im Forum, als diese Seite zuerst
geschrieben wurde; inzwischen ist er veröffentlicht, und der Link zeigt ihn. Das Video
des Besitzers und einige erklärende Animationen, die er gefunden hat, sind bewusst nicht
verlinkt: Das Video liegt auf einem privaten Laufwerk, und die Animationen stammen von
Reddit, das diese Website nicht zitiert.

Was es auf `reported` heben würde: derselbe fehlende oder verformte Zahn in einem zweiten
Werkzeugkopf, gemeldet in einem anderen Thread — oder eine Aussage des Herstellers, die
den Defekt anerkennt.

## Verwandte Seiten

- [Werkzeugerkennung und Parkfehler](tool-detection-ringdown-decay.md) — die anderen
  Arten, auf die ein Werkzeug nicht an seinem Platz bleibt
- [Druckbett-Kompatibilität](../reference/build-plate-compatibility.md) — Platten, die
  Werkzeuge aus ihren Docks stoßen
- [Wen Sie kontaktieren](support-and-warranty-path.md)
