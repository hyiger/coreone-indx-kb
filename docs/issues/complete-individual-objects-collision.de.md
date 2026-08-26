---
title:        Werkzeugkopf kollidiert mit fertigen Teilen — "Complete individual objects"
confidence:   reported
updated:      2026-08-24
author:       hyiger
printer:      Core One
toolhead:     INDX
hotend:       unknown
nozzle:       unknown
firmware:     unknown
sources:
  - https://github.com/prusa3d/PrusaSlicer/issues/14298
  - https://kb.nomadsgalaxy.com/topics/core-one/indx/issues/2
  - https://github.com/prusa3d/Prusa-Firmware-Buddy
superseded_by:
source_sha:   e3fa6ce57125d55071d3dc6caa9f3ff8b8f2766366a8fe81147a86a0d0addf69
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
sind.

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
    könnte es die Antwort sein. Niemand hat das geprüft.

    Die beiden `G0`-Anhebungen blieben ohnehin schichtrelativ, `P0` allein könnte also
    nicht die ganze Geschichte sein.

    TODO(verify): ob `G27 P0` bei einem sequenziellen Druck bereits fertiggestellte
    Objekte berücksichtigt oder nur das gerade in Arbeit befindliche.

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
    Es liegt nahe, der Werkzeugwechsel-Sequenz ein Anheben hinzuzufügen. Der
    kollidierende Verfahrweg entsteht in den Makros der Firmware selbst und nicht in der
    geslicten Datei, das Bearbeiten des geslicten G-Codes erreicht ihn daher nicht
    zuverlässig — und ein falsches Anheben auf einer Maschine, die an einer Station parkt
    und spült, ist eine eigene Gefahr. Warten Sie auf eine Behebung.

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
[kommentierter G-Code des Profils](../gcode/indx-profile-gcode.md).

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
dass er unbehoben bleibt, nicht irgendetwas über INDX-Hardware. Die INDX-Sichtung bleibt
ein einzelner Bericht; was nicht länger auf einer einzigen Quelle beruht, ist der Fehler
selbst.

Es sind keine Versionen festgehalten. Der Thread nennt weder eine Firmware- noch eine
Slicer-Version, was hier ins Gewicht fällt: Ohne eine solche Angabe kann niemand, der
später liest, erkennen, ob eine Behebung eingespielt wurde.

Was die Seite weiter stärken würde: ein zweiter INDX-Besitzer, der die Kollision meldet,
oder ein INDX-spezifisches Ticket im Tracker des Slicers. Das bestehende XL-Issue ist der
naheliegende Ort dafür — es hat bereits Prusas Aufmerksamkeit und ein internes Ticket,
und ein Bericht, der denselben Fehler an einem zweiten Werkzeugwechsler zeigt, ist für
Prusa nützlicher als ein neuer Thread. Da der Mechanismus überprüfbar ist, kann ein
solcher Bericht auf genau den Parameter zeigen, statt Symptome zu beschreiben. Zu
beachten: Im Firmware-Tracker von Prusa findet sich unter dieser Beschreibung nichts —
die dortigen Einträge, die auf den Namen der Funktion passen, betreffen andere Drucker
und liegen zeitlich vor dem INDX.

## Verwandte Seiten

- [Kommentierter G-Code des Profils](../gcode/indx-profile-gcode.md) — der vollständige
  Werkzeugwechsel-Block, aus dem diese drei Zeilen stammen, mit Kommentaren
- [In den Druck geschleppte Blobs](stringing-and-wiper-calibration.md) — die andere
  Stelle, an der Werkzeugwechsel-Bewegung einen Druck beschädigt, über einen völlig
  anderen Mechanismus
- [Phantom-Werkzeuge und Parkfehler](tool-detection-ringdown-decay.md) — betrifft
  ebenfalls das, was rund um einen Parkvorgang geschieht, ist aber ein Erkennungs- und
  kein Bewegungsfehler
