---
title:        Diagonale Bänderung auf den Druckwänden
confidence:   reported
updated:      2026-11-08
author:       hyiger
printer:      Core One
toolhead:     INDX
hotend:       CHT high-flow
nozzle:       0.4mm reported
firmware:     unknown on the reporting machines; 7.0.0, 7.0.1 and 8.0.0 release notes and 6.9.2 and 8.0.0 source checked
sources:
  - https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/diagonal-banding-2/
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/bondtech-nozzle-hardening-debacle-how-does-this-affect-prusa-indx-orders/
  - https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/a-summary-of-common-indx-problems/
  - https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/upgrade-core1-to-indx-gen2/
  - https://help.prusa3d.com/downloads/core-one-indx
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v7.0.0
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v7.0.1
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v8.0.0
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/include/marlin/Configuration_COREONE.h
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.2/include/marlin/Configuration_COREONE.h
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/lib/Marlin/Marlin/src/module/planner.cpp
superseded_by:
source_sha:   85e36646176aef170eb28032b80515a68e67b6c8edd29dbb404ddebb78df5a9b
---
# Diagonale Bänderung auf den Druckwänden

## Zusammenfassung

Ein regelmäßiges, reproduzierbares diagonales Muster auf senkrechten Wänden, dessen
Richtung sich umkehrt, je nachdem ob die Perimeter im Uhrzeigersinn oder gegen den
Uhrzeigersinn verlaufen, deutet auf den Extruder hin und nicht auf die Bewegungsmechanik.
Es gibt einen Test aus zwei Drucken, der die Frage in etwa einer Stunde und ohne jede
Demontage klärt; er lohnt sich, bevor Sie einen Supportfall eröffnen. Eine schwach
ausgeprägte Form dieses Artefakts scheint für einen Extruder mit zwei Antriebsrädern
normal zu sein; eine deutlich ausgeprägte ist ein Hardwarefehler, und die berichtete
Abhilfe ist ein Austausch des Werkzeugkopfs — noch keine verlässliche, denn bis Anfang
November hatten vier Besitzer Ersatzköpfe erhalten, zwei davon in der neueren
spritzgegossenen Ausführung, die das Problem nicht behoben (alle im selben Thread, daher
`provisional`). Am 7. November gab ein Besitzer die Erklärung des Herstellers wieder:
kleine Toleranzen im Antriebsstrang, die sich in einer Einheit aufsummieren und
inzwischen enger gefasst wurden (die Wiedergabe eines einzelnen Besitzers, ohne bekannte
öffentliche Stellungnahme des Herstellers, daher `provisional`). Über einen Kopf, der
nach den engeren Toleranzen gefertigt wurde, hat noch kein Besitzer berichtet.

## Details

### Warum die Bänderung diagonal verläuft

Das ist der Teil, der den Fehler erkennbar macht, und es lohnt sich, ihn zu verstehen,
bevor Sie irgendetwas testen.

Wenn etwas im Extruder die geförderte Filamentmenge einmal pro Zahnradumdrehung
verändert, fällt diese Abweichung auf jeder Lage an eine bestimmte Stelle des Perimeters.
Die Länge eines Perimeters ist aber fast nie ein exaktes Vielfaches des pro
Zahnradumdrehung vorgeschobenen Filaments — der Defekt landet daher auf jeder folgenden
Lage an einer etwas anderen Stelle. Stapelt man diese Lagen, reihen sich die Versätze zu
einer Diagonalen.

Daraus folgen zwei Dinge, und beide sind diagnostisch verwertbar:

- Das Muster ist **regelmäßig und reproduzierbar**, nicht zufällig.
- Es **wechselt die Richtung** mit der Perimeterrichtung, denn eine Umkehr der
  Fahrtrichtung kehrt um, in welche Richtung der Defekt um das Bauteil wandert.

Ein Besitzer, der dasselbe Phänomen bereits von einem Nextruder kannte, führte es auf ein
an einem Extruderzahnrad haftendes Filamentbruchstück zurück, das genau diese Abweichung
einmal pro Umdrehung erzeugt.

### Testen Sie, bevor Sie einen Schluss ziehen

Die als Lösung markierte Antwort im Thread ist ein Protokoll aus zwei Drucken, und sie ist
das Wertvollste auf dieser Seite. Sie trennt die Extrusion von der Bewegung:

**Druck eins**

1. Starten Sie ein **neues Projekt in PrusaSlicer mit den Standardprofilen**. Übernehmen
   Sie nicht Ihre eigene Abstimmung — es geht um eine saubere Ausgangsbasis.
2. Fügen Sie einen **Quader** hinzu.
3. **Drehen Sie ihn um 45° um Z.** Das ist wesentlich: bei 45° werden das X- und das
   Y-Antriebssystem jeweils getrennt von unterschiedlichen Wänden beansprucht.
4. Schalten Sie den **Vasenmodus** ein.
5. Drucken Sie ihn.

Liegt dieser Fehler vor, sehen Sie deutliche diagonale Bänderung auf **allen vier Wänden**.

**Druck zwei**

Identisch zum ersten, mit genau einer Änderung: **erhöhen Sie die Breite des äußeren
Perimeters leicht** gegenüber dem Standardwert. Verschieben Sie den Quader nicht. Ändern
Sie sonst nichts.

Liegt dieser Fehler vor, **verschieben sich Abstand und Winkel der Bänderung** — subtil,
aber unverkennbar.

Der Verfasser des Protokolls erwartet eine leichte Verschiebung. Der einzige andere
Besitzer, der bisher von beiden Drucken berichtet hat, sah eine weit größere: Auf Druck
zwei rückten die Diagonalen eng zusammen, zwischen je zwei Linien von Druck eins
erschienen zwei neue, und das Muster war schwerer zu erkennen und zu fotografieren.
Werten Sie einen schwächer gebänderten Druck zwei also nicht als Heilung. Entscheidend
ist, dass sich das Muster überhaupt ändert — auch eine große Änderung deutet auf die
Extrusion. Das ist ein einzelner Durchlauf; wie groß die Verschiebung ausfallen sollte,
ist daher offen.

TODO(verify): die Standardbreite des äußeren Perimeters und der Wert, auf den sie zu
ändern ist. Jede moderate Erhöhung erfüllt den Zweck, da der Test darauf beruht, dass sich
das Muster *ändert*, und nicht auf einer bestimmten Breite; die oben beschriebene Methode
ist also auch ohne diese Werte vollständig. Die Zahlen werden bis zur Verifikation
zurückgehalten, weil es Slicer-Einstellungen sind.

**Warum das funktioniert.** Zwischen den beiden Drucken fährt der Werkzeugkopf nahezu
denselben Weg mit nahezu denselben Geschwindigkeiten ab — die XY-Bewegung ist im
Wesentlichen identisch. Nur die Extrusion unterscheidet sich. Ändert sich also die
Bänderung, kann die Ursache nicht in der XY-Bewegungsmechanik liegen, und Sie haben
Riemen, Führungen, Schrittmotoren und Portalausrichtung in einem Schritt ausgeschlossen.
Das sind eine Menge teurer Verdächtiger, die zwei Testwürfel aus dem Rennen nehmen.

**Zwei Köpfe vergleichen.** Ein Besitzer, der gerade einen Ersatzkopf erhalten hatte,
stellte fest, dass ein üblicher VFA-Testdruck (Vertical Fine Artifacts) dasselbe Muster
zeigt, womöglich deutlicher, und stellte Drucke davon aus identischem G-Code ein
(`provisional`, ein einzelner Bericht). Eine feste Testdatei dieser Art eignet sich für
einen Vorher-nachher-Vergleich zweier Köpfe, ersetzt das Protokoll aber nicht: Ein
einzelner Druck kann Extrusion und Bewegung nicht voneinander trennen.

### Was das ausschließt, und was zuerst verfolgt wurde

Der Verfasser des Threads hat die frühen Theorien ausdrücklich zurückgezogen und die Leser
gebeten, alles vor der als Lösung markierten Antwort zu ignorieren. Festhaltenswert, weil
es die naheliegenden ersten Vermutungen sind und sich hier alle als Sackgasse erwiesen
haben:

- **Bauteilkühlung** — eine plausible Theorie, denn ungleichmäßige Kühlung erzeugt
  tatsächlich Bänderung.
- **Feuchtes Filament** — einschließlich des besonderen Falls einer ungleichmäßig
  getrockneten Spule, die eine überzeugend ähnliche Bänderung erzeugt.
- **Nicht zusammenpassende Düse und Profil** — etwa wenn eine Düsengeometrie verbaut ist,
  während für eine andere gesliced wird.

Keine davon erklärte ein Muster, das über verschiedene Materialien hinweg bestehen blieb
und der Perimeterrichtung folgte. Wenn Ihre Bänderung *doch* auf das Trocknen des
Filaments reagiert, haben Sie ein anderes und weit billigeres Problem.

Allerdings ist eine allgemeine Verbesserung durch Trocknen nicht dasselbe wie eine
Bänderung, die auf das Trocknen reagiert. Ein Besitzer, nach dessen Angabe gründlich
getrocknetes Filament seine Drucke erheblich verbessert, fand die diagonalen Linien
dennoch auf einem kürzlich gedruckten Teil. Feuchtes Filament und dieser Fehler können
womöglich gleichzeitig vorliegen; eine Verbesserung durch Trocknen spricht den Extruder
für sich genommen also nicht frei (`provisional`: ein einzelner Bericht, selbst
diagnostiziert an einer Maschine, an der dieser Besitzer zudem ein Werkzeug meldet, das
klickt und Schritte verliert, und dieser Besitzer hat nicht über einen Durchlauf des
Protokolls berichtet).

### Prüfen Sie zuerst das Billige

Bevor Sie einen Austausch verfolgen, **prüfen und reinigen Sie die Extruderzahnräder**.
Ein an einem Zahn haftendes Filamentbruchstück erzeugt genau die oben beschriebene
Abweichung einmal pro Umdrehung, und es kostet nichts, das auszuschließen.

### Ein Teil der Bänderung ist systembedingt

Mehrere Besitzer im Thread berichten von einer schwach ausgeprägten Form auf glänzenden
Filamenten — einer beschreibt sie als etwas, das man nicht mehr übersehen kann, sobald man
es einmal bemerkt hat. Der Konsens unter ihnen ist, dass Dual-Drive-Extruder in dieser
Preisklasse generell eine gewisse periodische Extrusionssignatur zeigen, und dass die
Single-Drive-Bauweise des Nextruders der Grund dafür ist, dass Besitzer sie dort nicht
gesehen haben. Ein neuerer Besitzer, der sie an seinem ersten Funktionsteil mit ebenen
Flächen bemerkte, druckte dieselben zwei Teile auf einem Core One ohne INDX und auf dem
INDX und fand den Unterschied frappierend (ein einzelner Bericht).

Der Hersteller scheint es ähnlich zu sehen. Der Besitzer hinter dem unten beschriebenen
Behelf mit dem Distanzstück gab eine Support-Antwort wieder, die seinen Fall zwar als
schlimm anerkannte, aber festhielt, ein gewisses Maß an Ungleichmäßigkeit gehöre zur
Funktionsweise eines Dual-Drive-Extruders. Das ist die Wiedergabe einer privaten Antwort
durch einen einzelnen Besitzer, keine veröffentlichte Stellungnahme. Die Darstellung des
Herstellers vom November, die im nächsten Abschnitt behandelt wird, wiederholt das weder,
noch widerspricht sie dem: Sie erklärt, warum manche Einheiten stärker betroffen sind als
andere, und sagt nichts über einen schwachen Rest.

Die Frage ist also nicht, *ob* das Artefakt existiert, sondern *wie stark* es ausgeprägt
ist. Schwach und nur auf glänzendem Filament im richtigen Winkel sichtbar ist zu erwarten.
Deutlich sichtbar auf allen vier Wänden eines mit Standardprofil gedruckten Testwürfels
nicht.

Ein deutlich ausgeprägter Fall ist auch keine bloße Eigenheit des Vasenmodus. Ein
Besitzer mit klarer Bänderung sieht sie an jeder unter 45° gedruckten Wand, deren Umriss
sich von Lage zu Lage nicht ändert. Mehrere Besitzer im Thread berichten, dass sie sich
an gewöhnlichen Bauteilen, bei denen die Perimeterlänge variiert, stattdessen als
allgemein ungleichmäßige, unscharf wirkende Wände zeigt — leicht feuchtem Filament oder
einem nicht abgestimmten Profil zuzuschreiben, weshalb einige von ihnen Wochen oder
Monate brauchten, um sie zu bemerken (`provisional`: ein einziger Thread). Der oben
erwähnte Besitzer, dem das Trocknen half, sah die diagonalen Linien an einem runden,
behälterförmigen Druck und beschreibt bei kleineren Drucken etwas, das eher dieser
Erscheinungsform an gewöhnlichen Bauteilen entspricht: eine Oberfläche, die wie von
einer Seite zur anderen zerkratzt wirkt.

### Was es offenbar ist

Die ausführlichste und zugleich jüngste Analyse im Thread führt es auf einen schlechten
Zahneingriff dort zurück, wo das Ritzel des Extrudermotors das erste Stirnrad des
Untersetzungsgetriebes antreibt. Die Herleitung arbeitet sich durch die
Untersetzungsverhältnisse, um zu bestimmen, wie viel Filament pro Zahn des Motorritzels
vorgeschoben wird, und findet diesen Wert im Einklang mit dem beobachteten Bandabstand —
was gezielt auf die **erste Untersetzungsstufe** deutet und nicht auf das gehobbte
Zahnrad, das das Filament greift.

Ein anderer Besitzer vermutet als eigentliche Ursache Zahnräder, die nicht perfekt rund,
nicht perfekt konzentrisch oder ungenau ausgerichtet sind, mit von Exemplar zu Exemplar
unterschiedlicher Ausprägung — was daraus eine Streuung in der Qualitätskontrolle machen
würde und keinen Konstruktionsfehler.

**Eine spätere Demontage weist auf einen anderen Fehler hin, mit Belegen dafür.** Ein
Besitzer, der das Warten auf einen zugesagten Austausch satt hatte, öffnete den Extruder
und sah sich das Tragbild am Motorritzel an. Es trug nur am oberen Ende der Welle.

Ineinandergreifende Zahnräder teilen sich nie eine Achse. Was dieses Tragbild anzeigt,
ist also nicht, dass Ritzel und erstes Zahnrad nicht koaxial wären — das ist jedes
gesunde Paar nicht —, sondern dass ihre Achsen nicht **parallel** sind: eine
Winkelabweichung über die Zahnbreite. Das ist ein anderer Fehler als ein unrundes oder
exzentrisches Zahnrad. Er widerlegt die obige Exzentrizitäts-Deutung für sich genommen
nicht, und beides könnte zusammen auftreten. Er benennt jedoch etwas, das ein Besitzer
finden und korrigieren kann, und er sagt den Artefakt bei jedem Zahneingriff voraus, den
die frühere Analyse unabhängig davon herleitete.

Eine überschlägige Rechnung aus dem Tragbild beziffert die Fehlausrichtung auf etwa 0,6°.
Woher sie stammt, ist nicht geklärt. Der Motor sitzt auf einer CNC-gefrästen Stahlplatte,
diese Fläche ist also ein unwahrscheinlicher Verursacher; die eigene Vermutung des
Besitzers ist, dass der Schwingarm nicht rechtwinklig zur Platte steht, möglicherweise
weil das Gewinde des Drehpunkts leicht schief geschnitten wurde. Bestätigt ist davon
nichts.

Für die Fehlausrichtung selbst gibt es inzwischen eine zweite, schwächere Beobachtung.
Mitte September meinte ein zweiter Besitzer, auf einem Foto seines Extruders von oben
einen leichten Winkel zwischen den Zahnrädern zu erkennen; der Besitzer des
Distanzstücks sah das ebenso, konnte es anhand des Fotos aber nicht sicher sagen. Im
Oktober berichtete derselbe Besitzer, die Zahnradachsen seien sowohl am ursprünglichen
Kopf als auch am Ersatzkopf sichtbar nicht parallel, und hielt das für einen Mangel der
Qualitätskontrolle. Das ist eine Sichtprüfung an einem montierten Extruder, keine
Messung, und sie stammt aus demselben Thread (`provisional`).

Trifft es zu, rückt das den Fehler in ein anderes Licht: kein schlecht gefertigtes
Zahnrad, sondern eine Toleranzkette, die auf perfekter Fertigung beruht und keine
Nachstellmöglichkeit bietet, wenn diese ausbleibt.

**Die Darstellung des Herstellers, wiedergegeben am 7. November** (`provisional`: die
Wiedergabe eines einzelnen Besitzers, und die darauf aufbauende Deutung unten erbt diese
Einstufung). Ein Besitzer stellte eine dem Hersteller zugeschriebene Mitteilung ein, ohne
zu sagen, auf welchem Weg sie ihn erreicht hatte; darin erklärt der Hersteller seine
Untersuchung für abgeschlossen. Demnach liegt die Ursache in einer Toleranzkette im
Antriebsstrang. Kein einzelnes Teil lag außerhalb seiner Toleranz, doch bei einer
betroffenen Einheit lagen mehrere Maße am weiten Ende ihres Bereichs, und zusammengenommen
zeigten sich die Abweichungen als das periodische Muster. Die Einheiten erhielten
unterschiedliche Kombinationen, was der Hersteller als Grund dafür nennt, dass manche
stärker betroffen sind als andere. Nach eigener Aussage hat er den zulässigen Bereich
dieser Maße inzwischen verengt und meldet durch die Änderung eine deutliche Verbesserung.

Das stützt die obige Deutung als Toleranzkette ebenso wie die Beobachtung, dass die
Ausprägung von Exemplar zu Exemplar schwankt. In einem Punkt korrigiert es zudem die
Deutung als Streuung der Qualitätskontrolle: Wenn jedes Teil seiner Spezifikation
entsprach, hätte eine Prüfung der einzelnen Teile dies nicht aufgedeckt. Nach dieser
Darstellung waren die Grenzen selbst zu weit für die Art, wie die Teile zusammenwirken,
was es eher zu einem Problem der konstruktiven Toleranzen macht als zu einer Streuung
fehlerhafter Teile (eine Schlussfolgerung aus der Wortwahl des Herstellers, nicht seine
Aussage; im Thread wird über genau diesen Punkt in beide Richtungen gestritten). Was die
Darstellung nicht leistet, ist die Benennung des Teils oder der Maße; sie bestätigt also
weder die Schiefstellung des Ritzels, die die Demontage fand, noch die Schlussfolgerung
der Analyse zur ersten Stufe, und sie schließt beides auch nicht aus. Es ist die
Wiedergabe einer an einen betroffenen Besitzer gerichteten Mitteilung durch einen
einzelnen Besitzer, und ob sie nur an diesen Besitzer oder breiter ging, ist nicht
gesagt; eine öffentliche Stellungnahme des Herstellers ist dieser Seite nicht bekannt.
Ende Oktober hatte der Prusa-Support einem anderen Besitzer lediglich mitgeteilt, die
Zahnräder seien schuld, ohne zu sagen, welche.

TODO(verify): dieselbe Demontage berichtet von einer Abweichung zwischen den
Extruderschritten je Millimeter, die aus der Toolboard-Dokumentation des Herstellers
folgen, und dem, was die Firmware verwendet. Die Zahlen werden hier zurückgehalten, weil
Extruderschritte/mm ein Kalibrierwert sind und ein falscher jeden Druck unbemerkt
verschlechtert — das Gegenteil des Distanzstücks, dessen Ergebnis sofort sichtbar ist.
Der seit dem 3. November öffentliche Quellcode von 8.0.0 und schon der von 6.9.2 zeigen,
dass der Wert der Firmware gar nicht übereinstimmen soll. In 8.0.0 liegt der
INDX-Standardwert bewusst unter den Schritten/mm, die genau die vom G-Code verlangte
Länge liefern würden; er tritt an die Stelle einer Flussreduktion, die früher im
Start-G-Code des Slicers stand
([Quellcode](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/include/marlin/Configuration_COREONE.h)).
6.9.2 verwendete denselben Standardwert, bezeichnete ihn ebenfalls als bewusste Änderung
und glich die eigenen Extruderbewegungen der Firmware beim Werkzeugwechsel bereits dafür
aus
([Quellcode](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.2/include/marlin/Configuration_COREONE.h));
8.0.0 dehnt den Ausgleich auf die Erfassung des Filamentverbrauchs und auf
Extruderbewegungen aus dem Menü Move Axis aus, Letzteres in seinen Versionshinweisen
aufgeführt. 6.9.2 war hier nicht in sich stimmig: Der Kommentar in der von der Demontage
zitierten Passage nennt einen Wert für exakte Förderung, während der darunter stehende
Ausgleich beim Werkzeugwechsel aus einem anderen berechnet wird. 8.0.0 löst das auf, indem
es den Wert für exakte Förderung nur einmal festlegt, gleich dem, den der Ausgleich in
6.9.2 verwendete. Der Wert von 8.0.0 für exakte Förderung beim INDX entspricht allerdings
auch nicht dem, den die Demontage aus der Dokumentation des Herstellers abgeleitet hat,
und nichts Veröffentlichtes erklärt diesen Unterschied. So
oder so handelt es sich um einen gleichmäßigen Faktor darauf, wie viel Filament gefördert
wird, nicht darauf, wie gleichmäßig; für sich genommen könnte er kein periodisches Muster
erzeugen, und als Spur zur Bänderung taugt er nicht mehr (eine Schlussfolgerung aus dem
Quellcode, keine Messung).

TODO(verify): die Übersetzungsverhältnisse, der Filamentvorschub pro Ritzelzahn und der
daraus erwartete Bandabstand. Der Besitzer, der sie hergeleitet hat, bezeichnete eine der
Eingangsgrößen als Schätzung, daher werden die Zahlen zurückgehalten; die
*Schlussfolgerung* — ein Bandabstand, der einem Zahn der ersten Untersetzungsstufe
entspricht — ist der berichtbare Teil und kommt ohne sie aus.

### Wie es behoben wird

Bei einem deutlich ausgeprägten Fall ist der berichtete Weg ein **Austausch des
Werkzeugkopfs** über den Hersteller, da der Fehler zum Zeitpunkt der Abfassung nicht auf
ein einzeln austauschbares Teil eingegrenzt war. Auch bei dieser Aktualisierung ist er es
noch nicht: Die wiedergegebene Darstellung des Herstellers macht Toleranzen im
Antriebsstrang verantwortlich und nennt kein Teil. Siehe
[wen Sie kontaktieren](support-and-warranty-path.md).

Dieser Weg kann dauern. Mitte September berichtete ein anderer Besitzer, ihm sei
mitgeteilt worden, der Hersteller untersuche zurückgesandte Werkzeugköpfe, um den Fehler
zu verstehen, bevor er diesem Besitzer eine neue Einheit schickt — damit nicht erneut
eine mit demselben Problem hinausgeht. Das legt nahe, dass die Ursache noch nicht
eingegrenzt war. Der Besitzer hinter dem unten beschriebenen Behelf mit dem Distanzstück
berichtete von drei Wochen ohne Rückmeldung, nachdem ihm ein Austausch angeboten worden
war; der parallel eingeschaltete Prusa-Support habe zunächst eine Ursache in der
Bewegungsmechanik gesucht und dann eine Werksreparatur angeboten. Jeder dieser Berichte
stammt von einem einzelnen Besitzer über seinen eigenen Support-Fall.

Ende September zogen die beiden Support-Wege in verschiedene Richtungen. Der Besitzer,
dem mitgeteilt worden war, der Hersteller halte Austauschköpfe zurück, wiederholte diese
frühere Antwort: Der Hersteller erkenne den Fehler an, arbeite noch an einer Lösung und
werde keine neue Einheit verschicken, bevor er sich ihrer sicher sei. Dennoch erhielt
ein Besitzer über Prusa einen Austauschkopf — eine spritzgegossene Ausführung, die er
einer neueren Charge zuordnete —, und dieser zeigte erneut die diagonalen Linien. Der
Verfasser des Protokolls deutete an, der Unterschied könne daran liegen, dass inzwischen
Prusa die meisten dieser Fälle bearbeite; das ist eine Vermutung, und keines der beiden
Unternehmen hat das gesagt. Ein weiterer Besitzer mit einem offenen Prusa-Fall erhielt
eine E-Mail, laut der Prusa in vergleichbaren Fällen eine mögliche Ursache auf der Seite
des Werkzeugkopfs gesehen habe; darin wurde nach seiner Firmware gefragt und eine
Abhilfe in Aussicht gestellt, ohne sie zu beschreiben. Der nächste Kontakt, Ende
September, bestand aus routinemäßigen Fragen zur Fehlersuche an der Bewegungsmechanik,
die nach Ansicht dieses Besitzers den ersten Chat weitgehend wiederholten. Auch dies ist
jeweils die Darstellung eines einzelnen Besitzers, und keine davon benennt ein Teil.

Auch der Oktober brachte kein benanntes Teil. Der Besitzer mit dem offenen Prusa-Fall
erhielt einen neuen Kopf, der die Bänderung nicht beseitigte, aber veränderte: ein
einzelnes Band, wo der ursprüngliche zwei zeigte, möglicherweise ein stärkeres. Der
Prusa-Support ließ diesen Besitzer erneut die Riemen abstimmen und verwies ihn dann auf
den E-Mail-Verlauf zurück, da der Fall bei den INDX-Spezialisten von Prusa liegt. Ein
anderer Besitzer erhielt einen Austauschkopf in der neueren spritzgegossenen
Ausführung, stellte fest, dass er nicht half und es nach seiner Ansicht sogar
verschlimmerte, berichtete, der Support habe sich daraufhin nicht mehr gemeldet, und
wartete Mitte Oktober auf einen zweiten Austauschkopf.
Ein weiterer Besitzer gab an, der Support habe ihn auf eine Liste von Besitzern gesetzt,
die auf eine Lösung warten. Jeder dieser Berichte stammt von einem einzelnen Besitzer,
alle aus demselben Thread, und keiner benennt ein Teil.

Ende Oktober gab es weder ein benanntes Teil noch viel Neues. Der Besitzer, dem
mitgeteilt worden war, Austauschköpfe würden erst verschickt, wenn der Hersteller sich
einer Lösung sicher sei, wartete am 24. Oktober noch immer: Der Hersteller hatte
erklärt, an einer Lösung zu arbeiten, doch eine Bitte um einen Zwischenstand war seit
zwei Wochen unbeantwortet geblieben, obwohl der Hersteller demselben Besitzer in dieser
Zeit zweimal wegen einer ab Werk verstopften Düse geantwortet hatte. Dieser Besitzer
wartet lieber, als auf einen Kopf zu setzen, der womöglich denselben Fehler hat. Ein
anderer Besitzer, seit mehr als sechs Wochen betroffen, gab an, offizielle Stellen hätten
sich seit einem Monat nicht mehr zu einer Lösung geäußert. Der Besitzer, der Mitte
Oktober auf einen zweiten Austauschkopf wartete, hatte sich seither nicht mehr gemeldet;
ob der Kopf eingetroffen ist oder geholfen hat, ist unbekannt. Der Besitzer mit dem
offenen Prusa-Fall sagte lediglich, der Support nehme die Sache ernst. Jeder dieser
Berichte stammt von einem einzelnen Besitzer, alle aus demselben Thread, und keiner
benennt ein Teil.

Anfang November kam die oben beschriebene Darstellung des Herstellers. Sie gelangte über
den Besitzer in den Thread, dem mitgeteilt worden war, Austauschköpfe würden erst
verschickt, wenn der Hersteller sich einer Lösung sicher sei, und mit ihr kam ein Plan,
von dem dieser Besitzer aus zweiter Hand von anderen betroffenen Besitzern gehört hatte:
Besitzer der Founders Edition, die den Fehler gemeldet hatten und warteten, sollten einen
neuen Werkzeugkopf erhalten, dieser Besitzer eingeschlossen, während sich Besitzer, die
über Prusa gekauft haben, an Prusa wenden. Derselbe Besitzer erwartete, dass jüngere
Lieferungen die Änderung bereits enthalten, wies aber darauf hin, dass die Mitteilung des
Herstellers erst wenige Tage alt war, und vermutete, Prusa verschicke womöglich noch
Austauschköpfe aus Beständen, die vor den engeren Toleranzen gefertigt wurden. Beides sind
Vermutungen; keines der beiden Unternehmen hat das gesagt.

Die Ergebnisse mit Austauschköpfen blieben derweil schlecht. Ein weiterer Besitzer, dem
der Prusa-Support Ende Oktober mitgeteilt hatte, die Zahnräder seien schuld, erhielt
Anfang November über Prusa einen neuen Kopf und fand darauf genau dasselbe Muster, was ihn
fragen ließ, ob die Ursache woanders liegt; er gab seine Charge mit 1.7 an, ohne zu sagen,
ob sich das auf den Bausatz oder den Austauschkopf bezog. Der Besitzer mit dem offenen
Prusa-Fall wiederholte, dass sein neuer Kopf denselben Fehler in einem leicht veränderten
Muster zeige, und gab an, der Support habe seither nicht mehr geantwortet. Der Besitzer,
der Mitte Oktober auf einen zweiten Austauschkopf wartete, berichtete, dieser dritte Kopf
sei annehmbar, aber nie sauber gewesen und werde nun schlechter. Jeder dieser Berichte
stammt von einem einzelnen Besitzer, alle aus demselben Thread.

Weder die am 15. Oktober veröffentlichte Firmware 7.0.0 noch die am 22. Oktober
veröffentlichte 8.0.0 ändert an diesem Bild etwas, und ebenso wenig die dazwischen am
19. Oktober veröffentlichte 7.0.1. Die
[Hinweise auf der Download-Seite](https://help.prusa3d.com/downloads/core-one-indx) und
die ausführlicheren GitHub-Versionshinweise zu allen dreien
([7.0.0](https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v7.0.0),
[7.0.1](https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v7.0.1),
[8.0.0](https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v8.0.0)), die am
3. November zusammen mit dem Quellcode veröffentlicht wurden, nennen keine Korrektur am
Extruderantrieb oder an diesem Artefakt; 7.0.1 enthält nur eine Korrektur für ein
Einfrieren beim Start. Das passt zur Darstellung des Herstellers, die die Ursache in den
Toleranzen der Teile sieht. Am nächsten kommt dem Thema die neue Beschleunigungsgrenze für
Filament (`M204 F`) in 8.0.0, standardmäßig aktiv, mit demselben Standardwert für den
INDX wie für jeden Drucker außer dem MINI; INDX-spezifisch ist daran also nichts.
Die GitHub-Hinweise und der
[Planner-Quellcode](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/lib/Marlin/Marlin/src/module/planner.cpp)
nennen ihren Zweck: Mit Pressure Advance wird jede Änderung des Flusses zu einem abrupten
Sprung der Extrudergeschwindigkeit, daher begrenzt die Firmware bei Druckbewegungen nun,
wie schnell sich der Fluss ändern darf, und senkt dazu die Beschleunigung der gesamten
Bewegung, einschließlich der Kurvenfahrt nahe an Extrusionsbewegungen; Leerfahrten
bleiben unberührt. Das begrenzt, wie schnell sich die befohlene Förderung ändert, nicht,
wie gleichmäßig der Antriebsstrang eine gleichbleibende liefert, und nichts in den
Hinweisen oder im Code bringt sie mit periodischer Bänderung in Verbindung (eine Lektüre
des Quellcodes, kein Test). Bis zum 7. November hat kein Besitzer im Thread berichtet,
dass sie die Bänderung verändert.

#### Der Behelf mit dem Distanzstück

Ein Besitzer korrigierte die Fehlausrichtung, indem er den Motor unterlegte: die
Abstandsbolzen lösen, die den Motor halten, und eine Unterlegscheibe unter den
Abstandsbolzen **unten links** legen, von der Rückseite des Extruders aus gesehen.
Verwendet wurden gewöhnliche M3-Unterlegscheiben aus den Prusa-Bausätzen.

Die Dicke war entscheidend, und die berichteten Ergebnisse verliefen nicht monoton:

| Distanzstück | Berichtetes Ergebnis |
|---|---|
| dünne Unterlegscheibe, Dicke nicht festgehalten | verringerte die Bänderung deutlich |
| 0,45 mm oder 0,55 mm | praktisch gleichwertig, Wände nahezu sauber |
| 0,7 mm | zu viel — die diagonalen Linien kehrten zurück |

Es gibt also ein Fenster und keinen Zusammenhang nach dem Muster „mehr ist besser“ — was
zu erwarten ist, wenn das Distanzstück einen Winkel korrigiert und keinen Spalt ausgleicht.
Das beste Ergebnis des Besitzers zeigte immer noch die schwächste Bänderung, wenn man
danach suchte.

Wie lange die Korrektur hält, ist unbekannt. Der Besitzer des Distanzstücks betrachtet
es als Notbehelf, der wieder herauskommt, sobald der Hersteller das Teil korrigiert, und
seine Berichte bis Mitte September beschreiben es als weiterhin wirksam; seither hat er
sich nicht mehr geäußert. Ein anderer Besitzer hat inzwischen als persönliche Theorie
geäußert, der schiefe Zahnkontakt könne die Motorseite verschleißen und die Bänderung
zurückkehren lassen; dass dies an einem unterlegten Kopf eingetreten wäre, hat niemand
berichtet. Am nächsten kommt dem ein Austauschkopf, von dem keine Unterlegung berichtet
ist, der nach Angabe eines Besitzers anfangs annehmbar war und nun schlechter wird, ohne
dass eine Ursache genannt wird.

!!! warning "Ein Besitzer, eine Maschine, und ein invasiver Eingriff"
    `provisional`, inline auf einer ansonsten mit `reported` bewerteten Seite. Dies ist
    ein einzelner Erfahrungsbericht aus erster Hand. Niemand hat ihn reproduziert, der
    Hersteller hat sich nicht dazu geäußert (auch seine Darstellung vom November erwähnt
    ihn nicht), und die obigen Dicken sind das, was an **einem** Werkzeugkopf funktioniert
    hat. Nach der Darstellung des Herstellers, wie ein Besitzer sie wiedergab, geht der
    Fehler auf eine Toleranzkette zurück, deren Kombination von Exemplar zu Exemplar
    verschieden ist; Ihrer braucht also möglicherweise ein anderes Maß oder gar keines.

    Es bedeutet außerdem, einen Werkzeugkopf zu zerlegen, den der Hersteller andernfalls
    im Rahmen der Gewährleistung ersetzen könnte. Der Besitzer ging diesen Weg erst, als
    ein zugesagter Austausch eine Woche lang unbeantwortet blieb. **Fragen Sie zuerst
    nach dem Austausch** — siehe [wen Sie kontaktieren](support-and-warranty-path.md) —
    und behandeln Sie dies als das, was Sie tun, wenn dieser Weg stockt, nicht als
    ersten Schritt.

    Anders als eine gebohrte Öffnung ist dies umkehrbar: Die Unterlegscheibe kommt wieder
    heraus. Das ist der Grund, warum die Maße überhaupt veröffentlicht werden, und warum
    sich das Ergebnis in einem einzigen Testdruck im Vasenmodus prüfen lässt, statt
    spätere Drucke unbemerkt zu verschlechtern.

!!! warning "Prüfen Sie den Austausch, bevor Sie sich freuen"
    Der Besitzer, auf dessen Fall diese Seite beruht, erhielt einen Austausch-Werkzeugkopf,
    der die Bänderung weitgehend beseitigte, aber mit einem **anderen Fehler** ankam —
    einer unzuverlässigen Wägezelle, wobei Referenzfahrt und Antasten übermäßig lange
    dauerten und die meisten Drucke mit der Aufforderung, Z neu zu kalibrieren, gar nicht
    erst starteten. Es folgte ein weiterer Austauschkopf. Ende September beschrieb dieser
    Besitzer den inzwischen eingebauten Kopf als viel besser, aber nicht makellos: Auf
    glänzendem Filament und bei passendem Licht lassen sich die Linien noch schwach
    ausmachen.

    Zwei Dinge machen den Fall mit der Wägezelle lehrreich. Der Fehler **folgte dem
    Werkzeugkopf** über den Tausch hinweg, während der ursprüngliche Werkzeugkopf jedes
    Mal einwandfrei referenzierte, und die Steuerplatine der Maschine war neueren Datums.
    Genau diese Kombination unterscheidet einen echten Hardwarefehler von der durch
    elektrische Störungen verursachten Variante desselben Symptoms — siehe
    [Störungen an der Wägezelle](loadcell-emi-noise.md), wo ein Ferritkern die übliche
    Antwort ist. Ein Ferrit behandelt Störungen; eine defekte Wägezelle repariert er
    nicht.

    Auch die Bänderung selbst ist nicht sicher verschwunden: Wie oben beschrieben,
    behoben die Ersatzköpfe von vier anderen Besitzern sie nicht, zwei davon in der neueren
    spritzgegossenen Ausführung (`provisional`: mehrere Besitzer, aber alle im selben
    Thread).
    Prüfen Sie an jedem Austauschkopf Antasten und Referenzfahrt und führen Sie damit den
    ersten Druck des Zwei-Druck-Protokolls aus, bevor Sie ihm einen langen Druck
    anvertrauen. Reproduziert ein neuer Kopf das alte Muster exakt, führen Sie auch den
    zweiten Druck aus: Ein Muster, das sich mit der Extrusionsbreite nicht verschiebt,
    deutet vom Extruder weg (eine Schlussfolgerung aus dem Protokoll, kein berichtetes
    Ergebnis).

## Verifikation

`reported` (gemeldet) — aber lesen Sie die Einschränkung, denn die Belege sind über die
Aussagen dieser Seite hinweg ungleich verteilt.

**Gut belegt.** Das Artefakt selbst war bei der ersten Abfassung dieser Seite von fünf
verschiedenen Teilnehmern im
[Thread zur diagonalen Bänderung](https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/diagonal-banding-2/)
beschrieben worden, seitdem von mehreren weiteren, von massiv bis kaum wahrnehmbar auf
glänzendem Filament; das Phänomen ist also nicht die Einbildung einer einzelnen Person.
Der Thread ist als beantwortet markiert und umfasst 165 Beiträge. Das
Zwei-Druck-Protokoll ist seine als Lösung markierte Antwort, verfasst von dem Besitzer,
der das Problem unter Beteiligung des Herstellers und des Prusa-Supports bearbeitet hat,
und die Begründung, warum es Extrusion von Bewegung trennt, ist in sich schlüssig.

**Das Protokoll, von einem zweiten Besitzer durchgeführt.** Am 20. September 2026 druckte
ein anderer Besitzer beide Würfel und erhielt, was das Protokoll vorhersagt: deutliche
Bänderung auf dem ersten, ein verändertes Muster auf dem zweiten. Es ist der erste
berichtete Durchlauf von jemand anderem als dem Verfasser des Protokolls. Es ist ein
einzelner Durchlauf. Er bestätigt die Kernaussage (das Muster ändert sich zwischen den
beiden Drucken), zählt aber, da im selben Thread, nicht als zweite Quelle; das Ausmaß
der beobachteten Änderung wird beim Test selbst behandelt.

**Einzelquelle.** Der schwere Fall, die Ergebnisse mit den Austausch-Werkzeugköpfen und
der nachfolgende Wägezellenfehler sind allesamt die Erfahrung eines einzelnen Besitzers,
der zwei Austauschköpfe erhielt. Die
[Zusammenfassung häufiger Probleme](https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/a-summary-of-common-indx-problems/)
verzeichnet unabhängig davon einen schweren Bänderungsfall, den der Hersteller als defekte
Extrudereinheit bestätigt hat, was die Schlussfolgerung stützt, aber durchaus denselben
Fall beschreiben kann und nicht einen zweiten. Die Austauschköpfe, die die Bänderung
nicht behoben, stammen von vier weiteren Besitzern, von denen zwei die neuere
spritzgegossene Ausführung angeben, und einer davon meldet inzwischen einen zweiten
Austauschkopf, der annehmbar ist, aber schlechter wird; die Berichte sind voneinander
unabhängig, stehen aber alle im selben Thread. Insgesamt sprechen die dokumentierten
Ergebnisse eher dagegen, dass ein Austausch eine verlässliche Abhilfe ist, und keines
kommt über `provisional` hinaus. Von keinem ist bekannt, dass es einen nach den engeren
Toleranzen gefertigten Kopf betrifft.

**Analyse, keine Messung.** Die Erklärung über den Zahneingriff ist die Berechnung eines
einzelnen Besitzers, veröffentlicht kurz bevor diese Seite entstand, ohne dass der
Hersteller bis dahin reagiert hätte. Sie ist stimmig und konkret, aber sie wurde von
niemandem bestätigt, der Zugang zu den Teilen hat. Behandeln Sie sie als die beste
verfügbare Hypothese. Die im November wiedergegebene Darstellung des Herstellers passt im
Großen dazu, eine von Exemplar zu Exemplar verschiedene Toleranzkette im Antriebsstrang,
nennt aber weder eine Untersetzungsstufe noch ein Teil und bestätigt die Einzelheiten
daher nicht.

**Ein Vorbehalt zur zweiten Quelle.** Die Bänderungsdiskussion im
[Thread zur Düsenhärtung](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/bondtech-nozzle-hardening-debacle-how-does-this-affect-prusa-indx-orders/)
ist *derselbe* Besitzer, der das Problem in einem anderen Thread anspricht; sie ist also
keine unabhängige Meldung des Fehlers. Ihren Platz hier verdient sie aus einem anderen
Grund: dort lieferte ein anderer Besitzer aus früherer Nextruder-Erfahrung den Mechanismus
mit dem anhaftenden Filamentbruchstück, der im gesamten Material die klarste Erklärung
dafür ist, warum die Bänderung diagonal verläuft, und aus dem sich die billige Prüfung
durch Zahnradreinigung ergibt.

Was diese Seite stärken würde: weitere Besitzer, die das Zwei-Druck-Protokoll durchführen
und das Ergebnis melden, ein Distanzstück, das auch an einem zweiten Werkzeugkopf wirkt,
eine Aussage des Herstellers, die das konkrete Teil benennt, und ein Austauschkopf, der
nachweislich eine Korrektur enthält. Zum Zeitpunkt dieser Aktualisierung, am
8. November, hat sich nur bei der Aussage des Herstellers etwas bewegt, und auch das nur
teilweise. Niemand hat ein Ergebnis mit Distanzstück an einem anderen Werkzeugkopf
gemeldet; der Besitzer, der am 10. Oktober ankündigte, es an seinem ursprünglichen Kopf
zu versuchen, meldete sich am 7. November erneut, ohne es zu erwähnen. Einen weiteren
Durchlauf des Protokolls hat ebenfalls niemand gemeldet. Die am 7. November
wiedergegebene Darstellung des Herstellers nennt eine Ursache, eine Toleranzkette im
Antriebsstrang, und eine Änderung, engere Toleranzen, aber kein Teil, und eine
öffentliche Stellungnahme des Herstellers ist nicht bekannt; die Ende Oktober
wiedergegebene Antwort des
Prusa-Supports besagte nur, die Zahnräder seien schuld. Von keiner Charge ist bekannt,
dass sie eine Korrektur enthält. Der Hersteller nennt für die engeren Toleranzen weder
eine Charge noch ein Lieferdatum. Die beiden früher gemeldeten spritzgegossenen
Austauschköpfe behoben den Fehler nicht, ebenso wenig der Anfang November über Prusa
erhaltene Kopf eines Besitzers, der seine Charge mit 1.7 angab. Ein Besitzer mit einem
Bausatz, den er als Charge 5 bezeichnet, glaubt den Fehler zu haben, hat allerdings nicht
über einen Durchlauf des Protokolls berichtet. In
[einem anderen Thread zum Umbau](https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/upgrade-core1-to-indx-gen2/)
sah ein Besitzer eines Bausatzes aus Charge 7 bei seinen ersten Drucken keine diagonale
Bänderung, ebenfalls ohne das Protokoll. Da sich die Toleranzkette laut Hersteller von
Exemplar zu Exemplar unterscheidet, sagt eine einzelne saubere Einheit wenig über ihre
Charge aus.

## Verwandte Seiten

- [In den Druck geschleppte Blobs](stringing-and-wiper-calibration.md) — die andere Seite
  zur Druckqualität; die Ursache ist eine andere, doch beides zeigt sich als Oberflächenfehler
- [Antasten schlägt fehl oder die Düse berührt das Bett nie](loadcell-emi-noise.md) —
  relevant, wenn ein Austausch-Werkzeugkopf einen Antastfehler mitbringt
- [Wen Sie kontaktieren](support-and-warranty-path.md) — der Weg zum Austausch
