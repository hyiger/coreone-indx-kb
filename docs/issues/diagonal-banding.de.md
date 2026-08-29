---
title:        Diagonale Bänderung auf den Druckwänden
confidence:   reported
updated:      2026-08-29
author:       hyiger
printer:      Core One
toolhead:     INDX
hotend:       CHT high-flow
nozzle:       0.4mm reported
firmware:     unknown
sources:
  - https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/diagonal-banding-2/
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/bondtech-nozzle-hardening-debacle-how-does-this-affect-prusa-indx-orders/
  - https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/a-summary-of-common-indx-problems/
superseded_by:
source_sha:   afc012e869c2c6a1d92a693212352248cb015b323f301b2390c80734ae5525f8
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
Abhilfe ist ein Austausch des Werkzeugkopfs.

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
gesehen haben.

Die Frage ist also nicht, *ob* das Artefakt existiert, sondern *wie stark* es ausgeprägt
ist. Schwach und nur auf glänzendem Filament im richtigen Winkel sichtbar ist zu erwarten.
Deutlich sichtbar auf allen vier Wänden eines mit Standardprofil gedruckten Testwürfels
nicht.

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

**Eine spätere Demontage widerspricht der Konzentrizitäts-Deutung und hat Belege
dafür.** Ein Besitzer, der das Warten auf einen zugesagten Austausch satt hatte, öffnete
den Extruder und sah sich das Tragbild am Motorritzel an. Es trug nur am oberen Ende der
Welle, was besagt, dass Ritzel und erstes Zahnrad nicht koaxial sind — gegeneinander
verkippt statt exzentrisch. Das ist ein anderer Fehler als ein unrundes oder außermittiges
Zahnrad, und er sagt genau das voraus, was die frühere Analyse fand: einen Artefakt bei
jedem Zahneingriff.

Eine überschlägige Rechnung aus dem Tragbild beziffert die Fehlausrichtung auf etwa 0,6°.
Woher sie stammt, ist nicht geklärt. Der Motor sitzt auf einer CNC-gefrästen Stahlplatte,
diese Fläche ist also ein unwahrscheinlicher Verursacher; die eigene Vermutung des
Besitzers ist, dass der Schwingarm nicht rechtwinklig zur Platte steht, möglicherweise
weil das Gewinde des Drehpunkts leicht schief geschnitten wurde. Bestätigt ist davon
nichts.

Trifft es zu, rückt das den Fehler in ein anderes Licht: kein schlecht gefertigtes
Zahnrad, sondern eine Toleranzkette, die auf perfekter Fertigung beruht und keine
Nachstellmöglichkeit bietet, wenn diese ausbleibt.

TODO(verify): dieselbe Demontage berichtet von einer Abweichung zwischen den
Extruderschritten je Millimeter, die aus der Toolboard-Dokumentation des Herstellers
folgen, und dem, was die Firmware verwendet. Die Zahl wird hier zurückgehalten, weil
Extruderschritte/mm ein Kalibrierwert sind und ein falscher jeden Druck unbemerkt
verschlechtert — das Gegenteil des Distanzstücks, dessen Ergebnis sofort sichtbar ist.
Festgehalten, weil es ein echter Hinweis ist, nicht weil es geklärt wäre: Es steht in
einer Randbemerkung eines einzelnen Beitrags, und niemand hat bestätigt, dass die beiden
Angaben tatsächlich voneinander abweichen.

TODO(verify): die Übersetzungsverhältnisse, der Filamentvorschub pro Ritzelzahn und der
daraus erwartete Bandabstand. Der Besitzer, der sie hergeleitet hat, bezeichnete eine der
Eingangsgrößen als Schätzung, daher werden die Zahlen zurückgehalten; die
*Schlussfolgerung* — ein Bandabstand, der einem Zahn der ersten Untersetzungsstufe
entspricht — ist der berichtbare Teil und kommt ohne sie aus.

### Wie es behoben wird

Bei einem deutlich ausgeprägten Fall ist der berichtete Weg ein **Austausch des
Werkzeugkopfs** über den Hersteller, da der Fehler zum Zeitpunkt der Abfassung nicht auf
ein einzeln austauschbares Teil eingegrenzt war. Siehe
[wen Sie kontaktieren](support-and-warranty-path.md).

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

!!! warning "Ein Besitzer, eine Maschine, und ein invasiver Eingriff"
    `provisional`, inline auf einer ansonsten mit `reported` bewerteten Seite. Dies ist
    ein einzelner Erfahrungsbericht aus erster Hand. Niemand hat ihn reproduziert, der
    Hersteller hat sich nicht dazu geäußert, und die obigen Dicken sind das, was an
    **einem** Werkzeugkopf funktioniert hat — wenn die Fehlausrichtung tatsächlich eine
    Toleranzkette ist, streut sie von Exemplar zu Exemplar, und Ihrer braucht
    möglicherweise ein anderes Maß oder gar keines.

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
    der die Bänderung beseitigte, aber mit einem **anderen Fehler** ankam — einer
    unzuverlässigen Wägezelle, wobei Referenzfahrt und Antasten übermäßig lange dauerten
    und die meisten Drucke mit der Aufforderung, Z neu zu kalibrieren, gar nicht erst
    starteten.

    Zwei Dinge machen diesen Fall lehrreich. Der Fehler **folgte dem Werkzeugkopf** über
    den Tausch hinweg, während der ursprüngliche Werkzeugkopf jedes Mal einwandfrei
    referenzierte, und die Steuerplatine der Maschine war neueren Datums. Genau diese
    Kombination unterscheidet einen echten Hardwarefehler von der durch elektrische
    Störungen verursachten Variante desselben Symptoms — siehe
    [Störungen an der Wägezelle](loadcell-emi-noise.md), wo ein Ferritkern die übliche
    Antwort ist. Ein Ferrit behandelt Störungen; eine defekte Wägezelle repariert er nicht.

    Prüfen Sie an jedem Austauschkopf Antasten und Referenzfahrt, bevor Sie ihm einen
    langen Druck anvertrauen.

## Verifikation

`reported` (gemeldet) — aber lesen Sie die Einschränkung, denn die Belege sind über die
Aussagen dieser Seite hinweg ungleich verteilt.

**Gut belegt.** Das Artefakt selbst wird von fünf verschiedenen Teilnehmern im
[Thread zur diagonalen Bänderung](https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/diagonal-banding-2/)
beschrieben, von massiv bis kaum wahrnehmbar auf glänzendem Filament; das Phänomen ist
also nicht die Einbildung einer einzelnen Person. Der Thread ist als beantwortet markiert
und umfasst 79 Beiträge. Das Zwei-Druck-Protokoll ist seine als Lösung markierte Antwort,
verfasst von dem Besitzer, der das Problem unter Beteiligung des Herstellers und des
Prusa-Supports bearbeitet hat, und die Begründung, warum es Extrusion von Bewegung trennt,
ist in sich schlüssig.

**Einzelquelle.** Der schwere Fall, das Ergebnis mit dem Austausch-Werkzeugkopf und der
nachfolgende Wägezellenfehler sind allesamt die Erfahrung eines einzelnen Besitzers. Die
[Zusammenfassung häufiger Probleme](https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/a-summary-of-common-indx-problems/)
verzeichnet unabhängig davon einen schweren Bänderungsfall, den der Hersteller als defekte
Extrudereinheit bestätigt hat, was die Schlussfolgerung stützt, aber durchaus denselben
Fall beschreiben kann und nicht einen zweiten.

**Analyse, keine Messung.** Die Erklärung über den Zahneingriff ist die Berechnung eines
einzelnen Besitzers, veröffentlicht kurz bevor diese Seite entstand, ohne dass der
Hersteller bis dahin reagiert hätte. Sie ist stimmig und konkret, aber sie wurde von
niemandem bestätigt, der Zugang zu den Teilen hat. Behandeln Sie sie als die beste
verfügbare Hypothese.

**Ein Vorbehalt zur zweiten Quelle.** Die Bänderungsdiskussion im
[Thread zur Düsenhärtung](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/bondtech-nozzle-hardening-debacle-how-does-this-affect-prusa-indx-orders/)
ist *derselbe* Besitzer, der das Problem in einem anderen Thread anspricht; sie ist also
keine unabhängige Meldung des Fehlers. Ihren Platz hier verdient sie aus einem anderen
Grund: dort lieferte ein anderer Besitzer aus früherer Nextruder-Erfahrung den Mechanismus
mit dem anhaftenden Filamentbruchstück, der im gesamten Material die klarste Erklärung
dafür ist, warum die Bänderung diagonal verläuft, und aus dem sich die billige Prüfung
durch Zahnradreinigung ergibt.

Was diese Seite stärken würde: ein zweiter Besitzer, der das Zwei-Druck-Protokoll
durchführt und das Ergebnis meldet, sowie eine Aussage des Herstellers, die das konkrete
Teil benennt.

## Verwandte Seiten

- [In den Druck geschleppte Blobs](stringing-and-wiper-calibration.md) — die andere Seite
  zur Druckqualität; die Ursache ist eine andere, doch beides zeigt sich als Oberflächenfehler
- [Antasten schlägt fehl oder die Düse berührt das Bett nie](loadcell-emi-noise.md) —
  relevant, wenn ein Austausch-Werkzeugkopf einen Antastfehler mitbringt
- [Wen Sie kontaktieren](support-and-warranty-path.md) — der Weg zum Austausch
