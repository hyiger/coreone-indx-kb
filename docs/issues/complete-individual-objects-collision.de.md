---
title:        Werkzeugkopf kollidiert mit fertigen Teilen — "Complete individual objects"
confidence:   reported
updated:      2026-11-08
author:       hyiger
printer:      Core One
toolhead:     INDX
hotend:       unknown
nozzle:       unknown
firmware:     unknown; G27 and tool change lift options read in the 6.9.1 and 8.0.0 source
sources:
  - https://github.com/prusa3d/PrusaSlicer/issues/14298
  - https://github.com/prusa3d/PrusaSlicer/issues/15672
  - https://github.com/prusa3d/PrusaSlicer/issues/15778
  - https://kb.nomadsgalaxy.com/topics/core-one/indx/issues/2
  - https://github.com/prusa3d/Prusa-Firmware-Buddy
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/src/marlin_stubs/pause/G27.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/src/marlin_stubs/pause/G27.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/src/common/mapi/parking.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/lib/Marlin/Marlin/src/module/planner.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/lib/Marlin/Marlin/src/gcode/calibrate/G28.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/src/common/marlin_server.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/lib/Marlin/Marlin/src/gcode/control/T.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/src/marlin_stubs/P.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/lib/Marlin/Marlin/src/module/prusa/toolchanger_common.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/commit/e229b682a5d9ba6420ed9613295eb19a53d50dc4
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/commit/00ae9687682b855b7ff22ad25611a4a632334a54
  - https://github.com/prusa3d/PrusaSlicer-settings-prusa-fff/blob/main/PrusaResearch/2.5.14.ini
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5571
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.4.0/src/common/feature/emergency_stop/emergency_stop.cpp
superseded_by:
source_sha:   177577f35c4cb8c11183548261bb6b0be230f0cb154885e8d4c4aab1341c0d37
---
# Werkzeugkopf kollidiert mit fertigen Teilen — "Complete individual objects"

!!! danger "Die Funktion deaktivieren, bis dies behoben ist"
    Wenn Sie mit **Complete individual objects** slicen und ein Objekt auf halber Höhe
    einen Werkzeugwechsel enthält, kann der Werkzeugkopf *unterhalb der Oberkante
    bereits fertiggestellter Objekte* über das Druckbett fahren und direkt in sie
    hineinfahren.

    Das ist nicht neu und nicht INDX-spezifisch. Prusa hat denselben Fehler an der XL
    im **März 2025** bestätigt, ein internes Ticket angelegt, und er ist über jede
    seitherige PrusaSlicer-Version hinweg offen geblieben. Der Schaden beschränkt sich
    nicht auf das ruinierte Teil — die Kollision erfolgt mit Verfahrgeschwindigkeit
    gegen ein starres, fertiges Objekt, also ist auch der Werkzeugkopf gefährdet, und
    bei mindestens einem Melder verkeilte sich die Düse in einem Teil, bis das Geräusch
    jemanden herbeirief.

    Die Funktion abzuschalten ist die einzige verlässliche Antwort. Es gibt einen
    teilweisen Workaround über die Druckreihenfolge, weiter unten beschrieben, aber
    diejenigen, die ihn nutzen, sagen klar, dass er durch Zufall funktioniert.

## Zusammenfassung

Beim sequenziellen Druck hebt die Maschine den Kopf normalerweise über alles bereits
Gebaute hinweg an, bevor sie das Druckbett überquert. Dieser Sicherheitsabstand wird
angewendet, wenn die Maschine sich *zwischen* Objekten bewegt. Er wird **nicht**
angewendet, wenn die Bewegung Teil eines Werkzeugwechsels ist, und ein Werkzeugwechsel
erzeugt genau eine solche Bewegung. Der Kopf fährt zur Dockingstation und kehrt ungefähr
auf der Höhe der Schicht zurück, die er gerade gedruckt hat — bei einem sequenziellen
Druck kann das weit unterhalb der Oberkante eines Nachbarn liegen, der vor Stunden fertig
geworden ist.

Die zugrunde liegende Einschränkung liegt im Slicer, nicht in der Maschine: Der
Algorithmus für sequenziellen Druck bildet Werkzeugwechsel-Verfahrwege überhaupt nicht
ab. Deshalb betrifft es die Werkzeugwechsler von Prusa allgemein und nicht speziell den
INDX, und deshalb ordnet die automatische Anordnung bereitwillig ein Druckbett an, das
sich so gar nicht sicher drucken lässt.

## Details

### Was schiefgeht

Die beiden Fälle verhalten sich unterschiedlich, und dieser Unterschied ist der gesamte
Fehler.

**Beginn eines neuen Objekts — der Sicherheitsabstand wird angewendet.** Das vorherige
Objekt ist fertig, also hebt die Maschine den Kopf vor dem Verfahren auf die volle Höhe
dieses Objekts zuzüglich eines kleinen festen Sicherheitsabstands an. Sie überquert das
Druckbett sicher, senkt auf die Höhe der ersten Schicht ab und fährt fort.

**Werkzeugwechsel innerhalb eines Objekts — der Sicherheitsabstand entfällt.** Die
Maschine befindet sich auf halber Höhe von Objekt zwei. Sie springt auf die aktuelle
Schichthöhe, parkt, wechselt, spült und kehrt zurück — alles ungefähr auf dieser
Schichthöhe. Das Anheben, das den Kopf über das fertige Objekt getragen hätte, findet nie
statt. Ist Objekt eins höher als die gerade gedruckte Schicht, führt der Rückweg mitten
hindurch.

Die berichtete Erklärung lautet, dass die Berechnung des Sicherheitsabstands zur Logik
des sequenziellen Drucks gehört, die die Verfahrwege zwischen Objekten steuert, während
der Verfahrweg beim Werkzeugwechsel aus dem Toolchange-G-Code und Firmware-Makros
zusammengesetzt wird. Diese Makros arbeiten schichtrelativ — bezogen darauf, wo der Kopf
gerade ist — und wissen nichts darüber, wie hoch die fertigen Objekte auf dem Druckbett
sind. Der Firmware-Quellcode schränkt den letzten Teil ein: Die Firmware merkt sich sehr
wohl den höchsten gedruckten Punkt, und der Standard-Toolchange-Block weist sie an,
diesen Wert nicht zu nutzen (siehe unten).

TODO(verify): der feste Sicherheitsabstand, den die Maschine über der Objekthöhe
hinzufügt, wenn sie das Anheben tatsächlich ausführt. Er wird im Quell-Thread genannt,
ist aber ein Wert aus einer einzigen Quelle und wurde nicht gegen die Firmware geprüft.

### Man sieht es im Toolchange-G-Code

Diese Erklärung stammte ursprünglich aus einem Diagramm im Fehlerbericht, dessen Autor
offenlegte, dass es maschinell erzeugt wurde. Sie muss darauf nicht länger beruhen. Das
Verhalten ist in einem Standard-Toolchange-Block sichtbar, und die Firmware dokumentiert
den Parameter, der es bestimmt.

Drei Zeilen in einem Werkzeugwechsel entscheiden, wie hoch der Kopf verfährt. Aus einem
funktionierenden Profil:

```gcode
G27 W3 Z{travel_max_lift[current_extruder]} P2 R{retract_toolchange} V{...} A{...}
...
G0 Z{layer_z + 0.8} ; Lift        <- on the way into the cleaner
...
G0 Z{layer_z + 1.0} ; Lift        <- on the way back out
```

**Die beiden `G0`-Anhebungen werden aus `layer_z` berechnet** — der Höhe der gerade
gedruckten Schicht. Nicht aus der Höhe von etwas bereits Fertiggestelltem. Bei einem
gewöhnlichen Druck wachsen alle Objekte gemeinsam, die aktuelle Schicht *ist* also das
Höchste auf dem Druckbett, und das ist korrekt. Bei einem sequenziellen Druck ist es
schlicht die falsche Bezugsgröße.

**Interessant wird es beim Parken.** Der Parameter `P` von `G27` legt fest, was die
Z-Bewegung bedeutet, und die Firmware dokumentiert drei Optionen:

| `P` | Z-Verhalten |
|---|---|
| `0` | *(Standard)* Anheben auf mindestens Z **above print** |
| `1` | Absolute Bewegung auf Z — kann die Düse **nach unten** bewegen |
| `2` | Relative Bewegung um Z |

Das Profil verwendet **`P2`**, eine relative Bewegung. `P0` — der Standardwert und der
einzige, dessen Beschreibung den Druck überhaupt erwähnt — wird nicht verwendet.

Die Option, die den Sicherheitsabstand berücksichtigt, existiert also in der Firmware,
und der Werkzeugwechsel-Pfad nutzt sie nicht. Das ist eine erheblich festere Grundlage
als „ein Diagramm legt nahe, dass die Makros schichtrelativ arbeiten“, und jeder kann es
nachprüfen: Öffnen Sie Ihren eigenen Toolchange-G-Code und sehen Sie nach, worauf sich
diese drei Zeilen beziehen.

!!! warning "Das benennt den Mechanismus. Es liefert keine Lösung."
    Es liegt nahe, aus der obigen Tabelle zu schließen, dass ein Wechsel von `P2` auf
    `P0` das Problem löst. Widerstehen Sie dem, bis jemand geklärt hat, was die Firmware
    mit „above print“ meint. Bezieht sich das nur auf das gerade entstehende Objekt,
    ändert `P0` für diesen Fall nichts. Bezieht es sich auf alles Fertiggestellte,
    könnte es die Antwort sein. Der Firmware-Quellcode äußert sich inzwischen dazu,
    siehe unten, aber nur auf dem Papier: Niemand hat es auf einem sequenziellen
    Druckbett ausprobiert.

    Die beiden `G0`-Anhebungen blieben ohnehin schichtrelativ, `P0` allein könnte also
    nicht die ganze Geschichte sein.

    TODO(verify): ob `G27 P0` bei einem sequenziellen Druck in der Praxis über bereits
    fertiggestellte Objekte hinweghebt oder nur über das gerade in Arbeit befindliche.
    Die Lesart des Quellcodes unten sagt, dass es über sie hinweghebt; das ist
    ungeprüft.

**Was der Firmware-Quellcode zeigt.** Prusas Firmware-Quellcode, gelesen bei den Git-Tags
6.9.1 und 8.0.0, klärt, was „above print“ bedeutet, und die Logik ist in beiden gleich.
Die Firmware führt für den gesamten Druck eine einzige Höchstmarke: das höchste Z, das
irgendeine extrudierende Bewegung im Druckbereich erreicht hat. Nur der Beginn eines
Drucks und das Referenzieren von Z setzen sie zurück. `G27 P0` behandelt sein Z als
Abstand über dieser Marke
([`G27`](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/src/marlin_stubs/pause/G27.cpp),
[Parken](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/src/common/mapi/parking.cpp)).
Ebenso das eigene Anheben der Firmware bei einem Werkzeugwechsel. Der Parameter `L` des
Park-Befehls `P0` und von `T` wählt es aus, und jede Einstellung außer `L0` hebt den
Kopf mindestens bis zu dieser Marke an; die Voreinstellung, ein volles Anheben, legt
noch einen Abstand darauf
([`T`](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/lib/Marlin/Marlin/src/gcode/control/T.cpp),
[Anheben beim Werkzeugwechsel](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/lib/Marlin/Marlin/src/module/prusa/toolchanger_common.cpp)).
Bei einem sequenziellen Druckbett sollte die Marke auf dem höchsten bis dahin fertigen
Objekt stehen bleiben, es sei denn, etwas zwischen den Objekten referenziert Z, was
diese Seite nicht geprüft hat. Der Standard-Block nutzt keins von beidem. Er parkt mit
`P2`, und sowohl `P0 S1 L0 D0` als auch `T{next_extruder} S1 L0 D0` übergeben `L0`,
kein Anheben. `P0` fährt den Kopf nach dem Parken nie zurück, und das `S1` an
`T{next_extruder}` weist die Firmware ebenfalls an, nicht zurückzufahren, sodass der
Rückweg zum Druck aus der geslicten Datei kommt. Bundle
2.5.14, Stand 8. November 2026, enthält diese Zeilen und die beiden `G0`-Anhebungen
weiterhin unverändert ([Profil](https://github.com/prusa3d/PrusaSlicer-settings-prusa-fff/blob/main/PrusaResearch/2.5.14.ini)).
Kurz gesagt: Die Firmware hat den Sicherheitsabstand, nach dem diese Seite sucht, und das
Profil fordert ihn nicht an. Das ist die Lesart dieser Seite aus dem Code, kein
beobachtetes Ergebnis, und sie macht `G27 P0` oder ein Anheben mit `L2` aus den Gründen
im Kasten oben nicht zur Lösung.

Der kommentierte Block, aus dem diese Zeilen stammen, mit Erläuterung der übrigen
Werkzeugwechsel-Sequenz, findet sich unter
[kommentierter G-Code des Profils](../gcode/indx-profile-gcode.md).

!!! danger "Eine Kollision hält den Druck möglicherweise nicht an"
    Der XL-Melder weist darauf hin, dass die Kollisionserkennung auf seiner Maschine
    standardmäßig deaktiviert ist, weil bei der geführten Einrichtung Phase Stepping
    aktiviert wird und beides sich gegenseitig ausschließt. Das Ergebnis war in seinem
    Fall, dass sich die Düse in das Teil verkeilte und dort schleifend verharrte, bis
    jemand es hörte — statt dass der Drucker einen Fehler erkannt und angehalten hätte.

    Ob dieselbe Voreinstellung für einen Core One INDX gilt, ist **nicht belegt**. Falls
    ja, ist der Fehlerfall hier schlimmer als ein ruiniertes Teil: Nichts stoppt die
    Maschine.

    TODO(verify): ob die Kollisionserkennung auf dem Core One INDX standardmäßig
    deaktiviert ist und ob ihre Aktivierung eine Werkzeugwechsel-Kollision erkennen
    würde. Das sollte man vor einem sequenziellen Mehrwerkzeug-Druck klären, nicht
    danach.

### Woran man es erkennt

- Sie slicen mit **Complete individual objects**.
- Auf dem Druckbett wird irgendwo mehr als ein Werkzeug verwendet.
- Die Objekte unterscheiden sich ausreichend in der Höhe oder sind so angeordnet, dass
  ein fertiges Objekt höher steht als die gerade an anderer Stelle gedruckte Schicht.
- Der Schaden tritt bei einem **Werkzeugwechsel** auf, nicht bei einem Schichtwechsel
  und nicht zu Beginn eines Objekts.

!!! danger "Werkzeugwechsel zwischen ganzen Objekten sind ebenfalls nicht sicher"
    Eine frühere Fassung dieser Seite legte nahe, dass man wahrscheinlich nicht betroffen
    sei, wenn Werkzeugwechsel ausschließlich *zwischen* ganzen Objekten stattfinden —
    ein Objekt je Material statt eines Wechsels auf halber Höhe. Der INDX-Melder war in
    diesem Punkt unsicher, und die Seite sagte das auch.

    **Der XL-Thread entscheidet die Frage andersherum.** Sein ursprünglicher Fall ist
    genau ein Objekt je Material ohne Wechsel innerhalb eines Objekts, und es kommt zur
    Kollision. Das ist der gründlicher dokumentierte der beiden Berichte, behandeln Sie
    Werkzeugwechsel zwischen Objekten also als betroffen.

    Ein Wechsel innerhalb eines Objekts ist keine Voraussetzung. Mehrere Werkzeuge auf
    einem sequenziell gedruckten Druckbett schon.

### Auf der XL seit März 2025 offen

Der INDX-Bericht ist nicht die erste Sichtung. Derselbe Fehler wurde im **März 2025** für
die Prusa XL gegen PrusaSlicer gemeldet, mit derselben Funktion und mehreren Extrudern,
und dieser Thread ist der besser dokumentierte der beiden.

Was er belegt:

- **Prusa hat ihn am Tag der Meldung bestätigt**, ein internes Ticket angelegt und
  angekündigt, dass er in einer kommenden Version behoben werde.
- **Er ist weiterhin offen.** Melder bestätigen ihn für PrusaSlicer 2.9.1, 2.9.2 und
  2.9.3, mit Kommentaren bis ins Jahr 2026.
- **Rund sieben unabhängige Besitzer** berichten, davon betroffen gewesen zu sein, alle
  auf XL-Geräten mit mehreren Werkzeugen.
- **Der Slicer warnt nicht.** Die automatische Anordnung legt ein sequenzielles
  Mehrwerkzeug-Druckbett an und sagt nichts zu Kollisionen. Er warnt *zwar*, dass man
  Kollisionen durch die Anordnung vermeiden solle — aber diese Prüfung berücksichtigt
  keine Werkzeugwechsel.
- **Die Vorschau zeigt es nicht.** Werkzeugwechsel-Bewegungen werden in der
  Bewegungsvorschau nicht gezeichnet, man kann also nicht durch Hinsehen prüfen, ob ein
  Druckbett sicher ist.

Der in diesem Thread beschriebene Mechanismus deckt sich mit dem, was der G-Code zeigt:
Werkzeugwechsel-Verfahrwege sind schlicht nicht Teil dessen, worüber der sequenzielle
Algorithmus überhaupt nachdenkt.

Die praktische Folge für INDX-Besitzer ist, dass dies kein neuer Fehler ist, der
demnächst behoben sein dürfte. Es ist eine bekannte, bestätigte, seit Langem unbehobene
Einschränkung der Funktion auf Prusa-Werkzeugwechslern, die der INDX nun geerbt hat.

### Was zu tun ist

**Deaktivieren Sie Complete individual objects** für jedes Druckbett, auf dem ein Objekt
einen Werkzeugwechsel enthält. Das ist die einzige verlässliche Antwort.

Wenn Sie sowohl sequenziellen Druck als auch mehrfarbige Teile brauchen, lautet die
ehrliche Antwort heute, dass sich beides nicht sicher verbinden lässt — drucken Sie die
mehrfarbigen Teile normal, alle Objekte gemeinsam wachsend, und behalten Sie den
sequenziellen Druck Druckbetten mit einem einzigen Werkzeug vor.

!!! warning "Der Workaround von vorn nach hinten verringert das Risiko. Er behebt nichts."
    XL-Besitzer berichten, dass sie die Objekte **von vorn nach hinten** anordnen, damit
    der Verfahrweg beim Werkzeugwechsel nichts bereits Fertiggestelltes überqueren muss.
    Mehrere sagen, das habe für ihre Drucke ausgereicht.

    Lesen Sie den Rest des Threads, bevor Sie sich darauf verlassen. Dieselben Leute
    beschreiben es als etwas, das „durch Zufall“ funktioniert, und merken an, dass es nur
    für bestimmte Teilegeometrien und Anordnungen gilt. Es versagt außerdem bei
    Unterbrechungen: Ein Filamentende oder eine Pause kann das Werkzeug vorn am
    Druckbett auf einer Höhe positionieren, die beim Fortsetzen zur Kollision führt, was
    als eigener offener Fehler gemeldet ist.

    **Und es ist ein Ratschlag für die XL.** Von vorn nach hinten funktioniert dort
    wegen der Lage der Docks der XL relativ zum Druckbett. Die Dock-Anordnung des INDX
    ist nicht dieselbe, ob also dieselbe Reihenfolge das Risiko auf einem Core One
    verringert, hat niemand belegt. Gehen Sie nicht davon aus, dass die Richtung
    übertragbar ist.

    Also: nützlich, um das Risiko bei einem Druck zu senken, den Sie beaufsichtigen,
    aber keine Grundlage dafür, einen langen sequenziellen Mehrwerkzeug-Auftrag
    unbeaufsichtigt laufen zu lassen.

!!! warning "Versuchen Sie nicht, das im Start-G-Code zu flicken"
    Es liegt nahe, der Werkzeugwechsel-Sequenz ein Anheben hinzuzufügen. Eine frühere
    Fassung dieses Kastens sagte, der kollidierende Verfahrweg entstehe in den Makros der
    Firmware selbst, außer Reichweite der geslicten Datei. Die Lesart des Quellcodes oben
    sagt für den Standard-Block etwas anderes: Er weist die Firmware an, weder anzuheben
    noch zurückzufahren, die beteiligten Höhen werden also doch im geslicten G-Code
    festgelegt. Der Rat gilt aus anderen Gründen weiter. Niemand hat eine Änderung
    getestet, eine Änderung am Toolchange-Block wirkt auf jeden Werkzeugwechsel in jedem
    Druck, und ein falsches Anheben auf einer Maschine, die an einer Station parkt und
    spült, ist eine eigene Gefahr. Warten Sie auf eine Behebung.

## Verifizierung

`reported` (gemeldet) — zwei Threads auf zwei Websites, zusammen rund acht unabhängige
Melder, einer der Threads von Prusa bestätigt.

Der [Ursprungsbericht](https://kb.nomadsgalaxy.com/topics/core-one/indx/issues/2) ist für
einen einzelnen Thread ungewöhnlich gut belegt. Er enthält ein Video der Kollision,
Screenshots und die G-Code-Datei, die sie erzeugt hat, und er geht die konkreten
Verfahrbewegungen in dieser Datei durch — und zeigt, dass das Anheben zum
Sicherheitsabstand dort vorhanden ist, wo ein neues Objekt beginnt, und bei einem
Werkzeugwechsel innerhalb eines Objekts fehlt. Drei Besitzer melden sich als betroffen.
Der Thread ist offen, und der Melder gibt an, dass die Diskussion zuvor im Discord des
Herstellers stattfand und das Problem an Prusa eskaliert wurde, ohne dass eine Behebung
veröffentlicht worden wäre.

Diese Seite war bei der ersten Fassung `provisional` (vorläufig), gestützt auf einen
einzigen INDX-Bericht. Zwei Dinge haben das geändert.

**Der Mechanismus hängt nicht mehr von einer Deutung ab.** Die Erklärung beruhte
ursprünglich auf einem Diagramm im INDX-Bericht, dessen Autor offenlegte, dass es
maschinell erzeugt wurde. Das ist nicht mehr der Fall: Die schichtrelativen Anhebungen
sind in jedem Standard-Toolchange-Block sichtbar, und der Parameter `P` von `G27` ist im
Firmware-Quellcode dokumentiert, wobei `P0` als Anheben über den Druck beschrieben ist
und `P2` — die tatsächlich verwendete Option — als schlichte relative Bewegung. Beides
lässt sich in wenigen Minuten am eigenen Profil überprüfen. Siehe
[kommentierter G-Code des Profils](../gcode/indx-profile-gcode.md). Eine Lesart des
Quellcodes bei den Git-Tags 6.9.1 und 8.0.0, oben beschrieben, geht einen Schritt
weiter: „above print“ ist eine Höchstmarke über den ganzen Druck, und das eigene Anheben
der Firmware beim Werkzeugwechsel nutzt sie ebenfalls, doch der Standard-Block verzichtet
auf beides. Das ist eine Erstanbieterquelle, aber eine Lesart von Code, kein beobachtetes
Ergebnis. Eine Firmware-Änderung in der Nähe dieses Pfads erreicht ihn nicht: Die
Firmware führt ihren eigenen Rückweg nach einem Werkzeugwechsel um den Düsenreiniger
herum, eine Änderung, die schon in 6.9.0 und in jeder späteren INDX-Version enthalten ist
([Commit](https://github.com/prusa3d/Prusa-Firmware-Buddy/commit/e229b682a5d9ba6420ed9613295eb19a53d50dc4),
[6.9-Linie](https://github.com/prusa3d/Prusa-Firmware-Buddy/commit/00ae9687682b855b7ff22ad25611a4a632334a54)),
doch der Standard-Block weist sie an, gar nicht zurückzufahren, und die Änderung betrifft
den Weg in X und Y, nicht die Höhe.

**Auf einer anderen Maschine sind unabhängige Berichte aufgetaucht.**
[PrusaSlicer-Issue 14298](https://github.com/prusa3d/PrusaSlicer/issues/14298)
dokumentiert denselben Fehler an der Prusa XL ab März 2025, mit rund sieben
verschiedenen Besitzern, die ihn in den folgenden dreizehn Monaten über drei
Slicer-Versionen hinweg gemeldet haben. Prusa hat noch am selben Tag reagiert, ein
internes Ticket angelegt, und das Issue ist weiterhin offen.

**Zur Frage, ob XL-Berichte als Bestätigung taugen.** Es handelt sich um einen anderen
Werkzeugwechsler, und Hardware-Befunde von einer XL ließen sich nicht auf einen INDX
übertragen. Dieser hier schon, weil die Einschränkung im Slicer und nicht in der Maschine
liegt — dieselbe Funktion, im selben Slicer, die den Verfahrweg beim Werkzeugwechsel
nicht berücksichtigt. Was der XL-Thread bestätigt, ist der Mechanismus und die Tatsache,
dass er unbehoben bleibt, nicht irgendetwas über INDX-Hardware. Der Fehler selbst
beruht nicht länger auf einer einzigen Quelle; die INDX-Seite folgt weiter unten.

**Es hat inzwischen den Slicer-Tracker des INDX selbst erreicht, zweimal.** Im September
2026 eröffnete ein INDX-Besitzer [PrusaSlicer-Issue 15672](https://github.com/prusa3d/PrusaSlicer/issues/15672), das beschreibt,
wie der Werkzeugkopf in Mehrfarbobjekte fährt, und reproduzierte es auf einer Alpha von
PrusaSlicer 3.0 — die nächste Hauptversion des Slicers behebt es also noch nicht. Tage
später eröffnete ein anderer Besitzer [PrusaSlicer-Issue 15778](https://github.com/prusa3d/PrusaSlicer/issues/15778), nachdem der
Werkzeugkopf beim ersten Werkzeugwechsel eines Auftrags mit vier Objekten unter
PrusaSlicer 2.9.6 ein fertiges Teil getroffen hatte, mit angehängter Projektdatei.

Nur das zweite davon ist ein neuer Beleg. Das erste verweist auf dieselbe
Community-Darstellung, die diese Seite bereits zitiert; es ist also diese Quelle, die in
den Tracker getragen wurde, und keine unabhängige Sichtung. Das zweite stammt von einem
unbeteiligten Besitzer, und erst dadurch ist die INDX-Seite mehr als ein einzelner
Bericht.

Beide Issues haben sich seither weiterentwickelt. Der Melder von Issue 15778 schloss es
wenige Minuten nach dem Anlegen als Duplikat von Issue 15672 und stellte dort dieselbe
Projektdatei ein, sodass beide INDX-Sichtungen nun in einem Issue liegen, das weiterhin
offen ist. Am Tag nach der Eröffnung von Issue 15672 hieß es in einer Antwort von Prusa,
der Fall sei in Prusas internem Tracker erfasst worden — derselbe Schritt, den Prusa
beim XL-Bericht unternommen hatte. Am 17. September 2026 ergänzten zwei weitere
Kommentatoren, dass sie den Fehler ebenfalls erlebt hatten: einer bei einem zweifarbigen
Auftrag, bei dem ein Farbwechsel während des zweiten Objekts den Kopf geradewegs zum
Dock schickte, quer durch das erste, der andere mit dem Hinweis, dass sich das Werkzeug
vom Kopf gelöst habe. Keiner der beiden nennt den eigenen Drucker, obwohl sich das Issue
eigens auf die Core One INDX bezieht; sie verleihen der INDX-Seite daher Gewicht, ohne
bestätigte INDX-Sichtungen zu sein.

Versionen sind nun festgehalten — 2.9.6 und eine Alpha von 3.0 —, sodass ein späterer
Leser erkennen kann, ob eine Behebung eingespielt wurde. Im Firmware-Tracker von Prusa
findet sich für den INDX weiterhin nichts dazu; die dortigen Einträge, die auf den Namen
der Funktion passen, betreffen die XL und liegen zeitlich vor dem INDX, was dazu passt,
dass der Fehler im Slicer liegt. Ein neuerer Eintrag vom 24. Oktober 2026 betrifft einen
anderen Fehler an einer Core One ohne INDX unter Firmware 6.4.0: Das Öffnen der Tür
während des zweiten Objekts eines sequenziellen Drucks schickte den Kopf beim Anfahren
der Home-Position in das erste
([#5571](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5571)). Das passt zum
Parken der Firmware beim Öffnen der Tür, das den Kopf bei 6.4.0 zur Seite fährt, ohne
ihn zuvor über fertige Objekte anzuheben
([Quellcode](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.4.0/src/common/feature/emergency_stop/emergency_stop.cpp)).
Es ist kein Werkzeugwechsel, und es ist ein einzelner Bericht.

## Verwandte Seiten

- [Kommentierter G-Code des Profils](../gcode/indx-profile-gcode.md) — der vollständige
  Werkzeugwechsel-Block, aus dem diese drei Zeilen stammen, mit Kommentaren
- [In den Druck geschleppte Blobs](stringing-and-wiper-calibration.md) — die andere
  Stelle, an der Werkzeugwechsel-Bewegung einen Druck beschädigt, über einen völlig
  anderen Mechanismus
- [Phantom-Werkzeuge und Parkfehler](tool-detection-ringdown-decay.md) — betrifft
  ebenfalls das, was rund um einen Parkvorgang geschieht, ist aber ein Erkennungs- und
  kein Bewegungsfehler
