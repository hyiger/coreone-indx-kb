---
title:        Kommentierter G-Code für Start, Schichtwechsel und Werkzeugwechsel
confidence:   measured
updated:      2026-08-25
author:       hyiger
printer:      Core One
toolhead:     INDX
hotend:       unknown
nozzle:       unknown
firmware:     6.9.0+16311
sources:
  - https://github.com/prusa3d/Prusa-Firmware-Buddy
  - https://help.prusa3d.com/article/buddy-firmware-specific-g-code-commands_633112
  - https://reprap.org/wiki/G-code
  - https://docs.duet3d.com/User_manual/Reference/Gcodes
  - https://blog.prusa3d.com/better-prints-easier-use-prusa-xl-core-one-l-and-core-one-gen-2-our-big-product-update_137539/
  - https://github.com/SimplyPrint/slicer-profiles-db
superseded_by:
source_sha:   8e9c763ca92d487634a305737982d433808d7303baf6228de5bd2a733259e5fc
---
# Kommentierter G-Code für Start, Schichtwechsel und Werkzeugwechsel

!!! info "Dies ist das Serienprofil, wortgetreu wiedergegeben"
    Alles Folgende ist Prusas eigenes PrusaSlicer-Profil für den Core One INDX auf
    Firmware 6.9.0 — keine Anpassung. Wenn Sie 6.9.0 einsetzen, ist das genau das, was
    Sie bereits haben, bevor Sie irgendetwas ändern.

    Genau deshalb lohnt die Lektüre. Die Werte sind die ausgelieferten Voreinstellungen
    und nicht die Abstimmung eines einzelnen Anwenders; wer versteht, was jeder Block
    tut, weiß, was die Maschine bei jedem Druck tatsächlich tut, und hat eine
    Ausgangsbasis, gegen die sich eigene Änderungen vergleichen lassen.

    Das Verhalten der Befehle ist gegen den Quellcode der Prusa-Firmware verifiziert. Das
    Profil selbst ändert sich zwischen Firmware-Versionen, prüfen Sie also die oben
    genannte Version gegen Ihre — das Profil von 6.6.3 wich an mehreren Stellen von
    diesem ab.

## Worum es sich handelt

Fünf Blöcke, die den gesamten Lebenszyklus eines Drucks abdecken:

| Block | Läuft | Bewirkt |
|---|---|---|
| Start | Einmal, vor dem Druck | Vorabprüfungen, Referenzfahrt, Werkzeugkalibrierung, Durchwärmen, Mesh Bed Leveling, Reinigen und Vorfüllen |
| Vor dem Schichtwechsel | Bei jeder Schicht | Setzt den Extruder zurück, senkt die Beschleunigung mit zunehmender Höhe |
| Nach dem Schichtwechsel | Bei jeder Schicht | Steuerung des Dock-Lüfters, nur auf Schicht 1 und 3 |
| Werkzeugwechsel | Bei jedem Werkzeugwechsel | Parken, Wechseln, Spülen oder Abwischen, Fortsetzen |
| Ende | Einmal, am Schluss | Abkühlen, Parken, Deaktivieren |

Sie sind nicht unabhängig voneinander. Der Start-Block setzt globale Variablen, die die
anderen vier lesen, und eine Zeile ganz am Ende des Start-Blocks verändert stillschweigend,
was der *erste* Werkzeugwechsel tut. Diese Kopplung wird an der Stelle benannt, an der sie
auftritt.

## Start-G-Code

### Globale Variablen und die Antasttemperatur

```gcode
{
global retract_toolchange = 8;
global tool_init = (0,0,0,0,0,0,0,0);
global used_tools = 0 ;
global low_temp_types = "PLA|PVA|BVOH|FLEX|TPU|TPE|PVB";
}

; number of used tools
{if is_extruder_used[0]}{used_tools = used_tools + 1}{endif}
{if is_extruder_used[1]}{used_tools = used_tools + 1}{endif}
{if is_extruder_used[2]}{used_tools = used_tools + 1}{endif}
{if is_extruder_used[3]}{used_tools = used_tools + 1}{endif}
{if is_extruder_used[4]}{used_tools = used_tools + 1}{endif}
{if is_extruder_used[5]}{used_tools = used_tools + 1}{endif}
{if is_extruder_used[6]}{used_tools = used_tools + 1}{endif}
{if is_extruder_used[7]}{used_tools = used_tools + 1}{endif}

{local probe_temp = "" + ((filament_notes[initial_tool]=~/.*MBL160.*/) ? 160 : (filament_notes[initial_tool]=~/.*HT_MBL10.*/) ? (first_layer_temperature[initial_tool] - 10) : (filament_type[initial_tool] == "PC" or filament_type[initial_tool] == "PA") ? (first_layer_temperature[initial_tool] - 55) : (filament_type[initial_tool] == "FLEX") ? 170 : (filament_type[initial_tool]=~/.*PET.*/) ? 170 : 170) + "";}
```

Nichts davon erzeugt G-Code. Es läuft im Slicer und legt den Zustand an, den der Rest des
Profils ausliest.

**Die vier globalen Variablen** bleiben über alle Blöcke des Drucks hinweg erhalten; nur
deshalb können der Schichtwechsel- und der Werkzeugwechsel-Block sie überhaupt sehen:

- `retract_toolchange` — zusätzlicher Rückzug beim Parken eines Werkzeugs, später von
  `G27 R` und von der Deretract-Länge auf dem Weg zurück referenziert.
- `tool_init` — ein Array mit acht Plätzen, einer je Werkzeug, alle beginnend bei null.
  Der Platz eines Werkzeugs springt auf `1`, sobald es zum ersten Mal gereinigt und
  vorgefüllt wurde. Der Werkzeugwechsel-Block verzweigt darüber; siehe den Hinweis zur
  Kopplung am Ende des Start-Blocks.
- `used_tools` — ein Zähler, aufgebaut durch die acht folgenden Zeilen. Der Block nach dem
  Schichtwechsel macht seinen gesamten Dock-Lüfter-Abschnitt von `used_tools > 1`
  abhängig, ein Druck mit einem einzigen Werkzeug überspringt ihn also vollständig.
- `low_temp_types` — eine Regex-Alternation der Materialien, die als
  Niedrigtemperatur-Materialien behandelt werden. Hier definiert, verwendet nur im Block
  nach dem Schichtwechsel. **Wenn Sie diese Zeile entfernen, geht jener Block kaputt** —
  mit einer undefinierten Variablen, was beim Lesen der beiden Blöcke für sich genommen
  nicht ersichtlich ist.

**Die Antasttemperatur** ist eine Kette von Bedingungen, die die Düsentemperatur bestimmt,
die die Maschine während des Antastens des Betts hält. Sie liest der Reihe nach: eine
Übersteuerung aus den Filamentnotizen, eine zweite notizbasierte Übersteuerung relativ zur
Temperatur der ersten Schicht, eine niedrigere Temperatur für PC und PA, einen festen Wert
für FLEX, einen festen Wert für alles PET-Artige und schließlich einen Standardwert. Die
Hülle `"" + ... + ""` erzwingt eine Zeichenkette als Ergebnis, damit es später in `M109`
eingesetzt werden kann.

Interessant ist, *warum* es sie gibt: Beim Antasten soll die Düse heiß genug sein, um
maßlich nicht aus dem Rahmen zu fallen, aber kühl genug, um nicht auf das Druckblech zu
sabbern, während die Wägezelle den Kontakt zu erfassen versucht. Sabbern während des
Antastens ist ein bekannter Fehlerfall — siehe
[Sabbern verdirbt das Antasten des Betts](../issues/oozing-during-probing-and-calibration.md).

### Vorabprüfungen

```gcode
M862.3 P "COREONEINDX" ; printer model check
M862.5 P2 ; g-code level check
M862.6 P"Input shaper" ; FW feature check
M862.6 P"INDX lock" ; FW feature check
M115 U6.9.0+16311

M591 S0 ; disable stuck detection

M555 X{(min(print_bed_max[0], first_layer_print_min[0] + 32) - 32)} Y{(max(0, first_layer_print_min[1]) - 4)} W{((min(print_bed_max[0], max(first_layer_print_min[0] + 32, first_layer_print_max[0])))) - ((min(print_bed_max[0], first_layer_print_min[0] + 32) - 32))} H{((first_layer_print_max[1])) - ((max(0, first_layer_print_min[1]) - 4))}

; inform about nozzle diameter
{if (is_extruder_used[0])}M862.1 T0 P{nozzle_diameter[0]} A{(filament_abrasive[0] ? 1 : 0)} F{(nozzle_high_flow[0] ? 1 : 0)}{endif}
{if (is_extruder_used[1])}M862.1 T1 P{nozzle_diameter[1]} A{(filament_abrasive[1] ? 1 : 0)} F{(nozzle_high_flow[1] ? 1 : 0)}{endif}
{if (is_extruder_used[2])}M862.1 T2 P{nozzle_diameter[2]} A{(filament_abrasive[2] ? 1 : 0)} F{(nozzle_high_flow[2] ? 1 : 0)}{endif}
{if (is_extruder_used[3])}M862.1 T3 P{nozzle_diameter[3]} A{(filament_abrasive[3] ? 1 : 0)} F{(nozzle_high_flow[3] ? 1 : 0)}{endif}
{if (is_extruder_used[4])}M862.1 T4 P{nozzle_diameter[4]} A{(filament_abrasive[4] ? 1 : 0)} F{(nozzle_high_flow[4] ? 1 : 0)}{endif}
{if (is_extruder_used[5])}M862.1 T5 P{nozzle_diameter[5]} A{(filament_abrasive[5] ? 1 : 0)} F{(nozzle_high_flow[5] ? 1 : 0)}{endif}
{if (is_extruder_used[6])}M862.1 T6 P{nozzle_diameter[6]} A{(filament_abrasive[6] ? 1 : 0)} F{(nozzle_high_flow[6] ? 1 : 0)}{endif}
{if (is_extruder_used[7])}M862.1 T7 P{nozzle_diameter[7]} A{(filament_abrasive[7] ? 1 : 0)} F{(nozzle_high_flow[7] ? 1 : 0)}{endif}

G90 ; use absolute coordinates
M83 ; extruder relative mode
```

Die Familie `M862.x` bildet Kompatibilitätsschranken. Sie vergleichen, was die Datei
erwartet, mit dem, was die Maschine tatsächlich ist, und brechen den Druck ab, statt ihn
später teuer scheitern zu lassen:

- `M862.3 P"COREONEINDX"` — Druckermodell. Für die falsche Maschine gesliced, bleibt es
  hier stehen.
- `M862.5 P2` — Stufe des G-Code-Dialekts.
- `M862.6 P"<feature>"` — ein benanntes Firmware-Feature muss vorhanden sein. Zwei sind
  hier erforderlich: Input Shaping und die INDX-Verriegelung.
- `M862.1` — werkzeugspezifische Düsendeklaration, einmal je verwendetem Werkzeug
  wiederholt: `T` das Werkzeug, `P` sein Durchmesser, `A` ob das zugewiesene Filament
  abrasiv ist, `F` ob die Düse High-Flow ist. Das versetzt die Firmware in die Lage,
  Einspruch zu erheben, wenn ein abrasives Filament durch eine Düse laufen soll, die nicht
  als dafür geeignet gekennzeichnet ist — siehe
  [Düsenhärte](../issues/nozzle-hardness.md), warum dieses Flag an dieser Maschine wichtig
  ist.

`M115 U…` deklariert die Firmware-Version, für die die Datei erzeugt wurde.

`M591 S0` deaktiviert die Erkennung von festsitzendem Filament für den Druck. Diese
Erkennung arbeitet, indem sie den Gegendruck der Extrusion über die Wägezelle ausliest —
denselben Sensor, der laut Prusa in einer künftigen Firmware Pressure Advance kalibrieren
soll. Warum das INDX-Profil sie zum Druckstart abschaltet, ist nicht geklärt.

`M555` deklariert den Druckbereich, abgeleitet aus dem Begrenzungsrahmen der ersten Schicht
zuzüglich Rand. Die Firmware nutzt ihn, um zu wissen, welcher Teil des Betts relevant ist —
am sichtbarsten daran, dass Mesh Bed Leveling diesen Bereich antastet statt des gesamten
Blechs.

`G90` / `M83` stellen die Positionierung für Bewegungen auf absolut und für den Extruder
auf relativ. Jeder `E`-Wert ab hier ist eine Differenz, kein Zielwert.

### Referenzfahrt, Werkzeugvorbereitung und Kalibrierung

```gcode
M140 S{first_layer_bed_temperature[initial_tool]} ; set bed temp

{if chamber_minimal_temperature[initial_tool] == 0}
  M141 S{chamber_temperature[initial_tool]} ; set nominal chamber temp
{endif}

; Home XY
G28 XY

; Pick tool for Z homing
{if is_extruder_used[0]}T0 S1 L2 D0
{elsif is_extruder_used[1]}T1 S1 L2 D0
{elsif is_extruder_used[2]}T2 S1 L2 D0
{elsif is_extruder_used[3]}T3 S1 L2 D0
{elsif is_extruder_used[4]}T4 S1 L2 D0
{elsif is_extruder_used[5]}T5 S1 L2 D0
{elsif is_extruder_used[6]}T6 S1 L2 D0
{elsif is_extruder_used[7]}T7 S1 L2 D0
{endif}

M104 S120

; Home Z
G28 Z

G0 Z40 F10000
M190 R{first_layer_bed_temperature[initial_tool]} ; wait for bed temp
; try picking tools used in print
G1 F10000
```

Die Sollwerte für Bett und Kammer gehen zuerst hinaus, damit das Aufheizen alles Folgende
überlappt. `M140` und `M141` setzen Zielwerte, ohne zu warten; erst `M190` weiter unten
blockiert.

Die Kammer-Zeile ist bedingt. Deklariert das Filament eine *Mindest*-Kammertemperatur, wird
sie hier übersprungen, weil ein eigener Abschnitt weiter unten diesen Fall behandelt.

`G28 XY` fährt die beiden Achsen an ihre Referenz, die kein eingesetztes Werkzeug
benötigen. Die Z-Referenzfahrt benötigt eines, denn Z wird gefunden, indem die Düse das
Bett berührt — also wird zuerst ein Werkzeug aufgenommen. Die `elsif`-Kette wählt das
verwendete Werkzeug mit der niedrigsten Nummer, welches auch immer das ist.

`M104 S120` setzt vor der Z-Referenzfahrt ein maßvolles Düsenziel. Warm genug, dass
Rückstände an der Spitze weich sind statt ein harter Klumpen unter dem Taster, kühl genug,
um nicht zu sabbern, während die Maschine arbeitet.

Nach der Referenzfahrt fährt `G0 Z40` das Bett frei, und `M190 R…` wartet, bis das Bett
seine Temperatur erreicht. Das ist die längste einzelne Wartezeit im gesamten Startvorgang.

```gcode
{local perimeter_flow_rate = 1.0 * (external_perimeter_speed > 0 ? external_perimeter_speed : (perimeter_speed > 0 ? perimeter_speed : 100)) * (layer_height * (external_perimeter_extrusion_width - layer_height) + 3.14159 * (layer_height/2) * (layer_height/2))}

{if (is_extruder_used[0] and filament_type[0] != "FLEX")}M574 S0 V35 T{temperature[0]} F{ (filament_max_volumetric_speed[0] > 0 ? min(perimeter_flow_rate, filament_max_volumetric_speed[0]) : perimeter_flow_rate ) / (3.14159 / 4 * filament_diameter[0] * filament_diameter[0]) }{endif}
```

*(einmal je Werkzeug wiederholt, `S0` bis `S7` — hier ist nur die erste Zeile gezeigt)*

`perimeter_flow_rate` wird einmal berechnet und von allen acht Zeilen weiterverwendet. Es
ist der volumetrische Fluss, der sich aus den Einstellungen der äußeren Perimeterlinie
ergibt: Geschwindigkeit multipliziert mit der Querschnittsfläche einer Extrusion,
modelliert als Rechteck mit halbkreisförmigen Enden. Die Rückfallkette bewirkt, dass der
Wert auf die Perimetergeschwindigkeit und dann auf eine Konstante zurückfällt, statt null
zu ergeben, wenn eine Geschwindigkeit nicht gesetzt ist.

Jede `M574`-Zeile rechnet diesen volumetrischen Wert dann in einen linearen
Filamentvorschub um, indem sie durch die Querschnittsfläche des Filaments teilt, begrenzt
durch die maximale volumetrische Geschwindigkeit des Materials, sofern eine gesetzt ist.
FLEX ist ausgenommen.

Beachten Sie die Einheit. Jede Eingangsgröße oben ist in mm pro Sekunde angegeben, `F` wird
also in mm Filament pro Sekunde ausgegeben. Ein `F` in Marlin ist immer mm pro Minute. Was
auch immer diesen Wert verarbeitet, verwendet nicht die übliche Vorschubkonvention — ein
weiteres Indiz dafür, dass `M574` ein herstellereigener Befehl mit eigener Konvention ist.

!!! note "M574 ist nicht implementiert — die Firmware ignoriert es"
    `M574` hat in der Prusa-Buddy-Firmware keinen Handler. Das ist gegen das Release-Tag
    `v6.9.0` geprüft — die Version, auf die dieses Profil zielt — sowie gegen jedes Objekt
    in der Historie des öffentlichen Repositorys, mit `M572` und `M575` als
    Positivkontrollen, um zu belegen, dass die Suche findet, was tatsächlich vorhanden ist.
    Marlin liegt unter `lib/Marlin` im Baum selbst und nicht als Submodul, dieselbe Suche
    deckt also die Marlin-Ebene mit ab.

    Was die Maschine damit tut, folgt aus dem Rückfallpfad des Parsers. Prusas eigener
    Dispatcher lehnt den Befehl ab, Marlins Verzweigung erreicht
    `default: parser.unknown_command_error()`, und `queue.ok_to_send()` läuft danach
    trotzdem. Der Drucker protokolliert also `Unknown command:` mit der betreffenden Zeile,
    antwortet mit `ok` und fährt fort — kein Fehler, keine Pause, nichts auf dem Display.
    Acht ignorierte Zeilen pro Druck, eine je verwendetem Nicht-FLEX-Werkzeug.

    *Dieser Absatz ist aus dem Firmware-Quellcode abgeleitet, nicht aus einem
    aufgezeichneten Log.* Öffentlich scheint es keine Terminal- oder Log-Aufzeichnung eines
    echten INDX zu geben, der `M574` empfängt, und im Firmware- oder Slicer-Tracker von
    Prusa wurde dazu nie ein Issue eröffnet.

    Eine Einschränkung dieser Aussage: Prusa entwickelt nicht öffentlich und veröffentlicht
    Release-Tags. Belegt ist damit, dass die Firmware, **die Sie einsetzen**, keinen
    Handler hat — nicht, dass nirgends einer existiert.

!!! warning "Eine Suche nach M574 führt in die Irre"
    `M574` ist keine unbelegte Nummer. Sowohl das RepRap-G-Code-Register als auch
    RepRapFirmware weisen sie der Endschalter-Konfiguration zu, wo `S` einen
    Endschaltertyp auswählt und `V`, `T` und `F` als Parameter überhaupt nicht existieren.
    Fast alles, was eine Suche nach "M574" liefert, beschreibt Endschalter an einem Duet
    und hat mit diesem Befehl nichts zu tun.

!!! info "Woher es stammt und das Feature, das Prusa angekündigt hat"
    Es gibt keinen Commit zu finden. `M574` hat in keinem öffentlichen Git-Repository von
    Prusa je existiert — die Zeile wird außerhalb davon im Herstellerprofil-Bundle
    ausgeliefert und nicht im Quellcode des Slicers. Sie tauchte erstmals im
    [PrusaResearch-Bundle 2.5.0](https://files.prusa3d.com/?latest=slicer-profiles&lng=en)
    am 26. Juni 2026 auf,
    dem Bundle, das die Profile für den Core One INDX hinzufügte, und wurde in 2.5.7 am
    20. August 2026 neu geschrieben. Sie ist INDX-exklusiv — nicht XL, nicht MK4, nicht der
    einfache Core One — es gibt also kein älteres Werkzeugwechsler-Ökosystem, in dem sie
    bereits dokumentiert wäre.

    Sie hat ein Geschwister. Dasselbe Bundle gibt `M573 R` in seinem Filament-Start-G-Code
    aus, in der Zeile unmittelbar nachdem `M572` Pressure Advance setzt. Das `R` trägt
    keinen Wert und ist kein nicht ausgewerteter Platzhalter; es ist ein wörtliches,
    nacktes Flag, identisch in allen dreizehn INDX-Filamentprofilen seit ihrer ersten
    Auslieferung. `M573` fehlt in der Firmware ebenso.

    Am 13. August 2026 hat Prusa
    [angekündigt](https://blog.prusa3d.com/better-prints-easier-use-prusa-xl-core-one-l-and-core-one-gen-2-our-big-product-update_137539/),
    den einzelnen festen Pressure-Advance-Wert durch ein flussabhängiges Modell zu
    ersetzen, dessen Parameter die **Wägezelle vor jedem Druck automatisch misst**,
    zusammen mit neuen, extrusionsbewussten Beschleunigungsgrenzen, die verhindern, dass
    der Drucker schnellere Flussänderungen verlangt, als der Extruder liefern kann. Die
    Ankündigung bezeichnet die Arbeiten als in interner Erprobung und nennt kein
    Veröffentlichungsdatum, keine Firmware-Version und **keinen G-Code-Befehl**.

    `M574` trägt je Werkzeug eine Zieltemperatur und die Extrusionsrate der **äußeren
    Perimeterlinie** — nicht das Maximum des Drucks, das der Infill übertreffen würde. Zwei
    Details lassen das absichtlich erscheinen. Dass ausgerechnet äußere Perimeterlinien
    herangezogen werden, deutet auf etwas hin, das sich mit dem Bereich befasst, in dem die
    Oberflächenqualität entschieden wird — genau dort zeigen sich
    Pressure-Advance-Artefakte. Und der Ausdruck rechnet volumetrischen Fluss in einen
    *Filament*-Vorschub um und verwirft damit die natürliche Einheit für alles Thermische —
    der Wärmebedarf skaliert mit dem Volumen, ein Heizermodell würde also mm³/s verlangen.
    Filament-mm/s ist die Einheit der Extruderkinematik und die von Pressure Advance
    selbst.

    Die Profile liegen zudem etwa sieben Wochen vor der Ankündigung. **Doch keine Quelle
    verbindet beides.** Diese Lesart wird festgehalten, weil sie die plausibelste
    verfügbare ist, nicht weil sie belegt wäre; sie passt außerdem mindestens ebenso gut
    zur Hälfte der Ankündigung über die Beschleunigungsgrenzen wie zu der über die
    Kalibrierung.

    TODO(verify): wofür `M574` und `M573 R` da sind und was `S`, `V`, `T` und `F` jeweils
    bedeuten. `S` ist ein Werkzeugindex und `T` eine Temperatur — erschlossen aus der
    Aufrufstelle, eine Lesart, die man locker halten sollte, da Marlins eigene Konvention
    die umgekehrte ist: `S` für Temperatur und `T` für Werkzeug. Das feste `V35` hat keine
    belegte Bedeutung und wird hier bewusst nicht erraten.

```gcode
G427 R2 P3 ; Calibrate all used and mapped tools

T{initial_tool} S1 L0 D0
```

`G427` führt die vollständige Werkzeug-Offset-Kalibrierung für jedes zugeordnete Werkzeug
durch: Es ermittelt, welche physischen Werkzeuge der Druck benötigt, kalibriert jedes in
XYZ und schreibt die Ergebnisse in Laufzeitvariablen und in das EEPROM.

Beide Parameter dienen der Genauigkeit. `R` ist der zufällige Versatz in Millimetern, der
beim Z-Antasten jedes Werkzeugs auf X und Y angewendet wird, damit nicht jeder
Antastvorgang exakt an derselben Stelle landet. `P` gibt an, wie viele Z-Antastungen je
Punkt genommen und gemittelt werden. `R2 P3` bedeutet also: um zwei versetzen, über drei
mitteln.

Das ist der Schritt, der an Maschinen mit defektem Offset-Sensor fehlschlägt — siehe
[Werkzeug-Offset-Kalibrierung schlägt fehl](../issues/offset-sensor-board-failure.md).

`T{initial_tool} S1 L0 D0` nimmt dann das Werkzeug auf, mit dem der Druck tatsächlich
beginnt.

### Kammer-Aufheizen, Durchwärmen und Mesh Bed Leveling

```gcode
{if chamber_minimal_temperature[initial_tool] != 0}
  ; Min chamber temp section
  M104 S0
  M140 S115 ; set bed temp for chamber heating
  G1 Z10 F720 ; set bed position
  G1 X242 Y0 F4800 ; set print head position
  M191 S{chamber_minimal_temperature[initial_tool]} ; wait for minimal chamber temp
  M141 S{chamber_temperature[initial_tool]} ; set nominal chamber temp
  M140 S{first_layer_bed_temperature[initial_tool]} ; set bed temp
{endif}

{if first_layer_bed_temperature[initial_tool] <= 60}M106 S70{endif}
G0 Z40 F10000
M104 S{if is_nil(idle_temperature[initial_tool])}100{else}{idle_temperature[initial_tool]}{endif}
M190 R{first_layer_bed_temperature[initial_tool]} ; wait for bed temp
M107

G29 G ; absorb heat

M109 S{probe_temp} ; wait for temp
```

Der Kammer-Abschnitt ist das Gegenstück zur Bedingung weiter oben: Er läuft nur für
Filamente, die eine Mindest-Kammertemperatur deklarieren. Die Technik besteht darin, das
Bett heiß zu fahren und den Kopf tief und seitlich zu parken, das Bett also als
Kammerheizung zu nutzen, und dann mit `M191` zu warten, bis die Kammer hochkommt, bevor das
eigentliche Bett-Ziel wiederhergestellt wird.

Davon abgesehen bekommt ein niedriges Bett-Ziel etwas Bauteillüfter, damit es sich
einpendelt, die Düse fällt während des Wartens auf eine Ruhetemperatur, und `M107` schaltet
den Lüfter vor dem Antasten ab.

`G29 G` ist ein Durchwärm-Schritt — er hält an, während die Maschine ins thermische
Gleichgewicht kommt, was wichtig ist, weil das Antasten an einem kalten Rahmen und das
Drucken an einem heißen unterschiedliche Ergebnisse liefern.

`M109 S{probe_temp}` bringt die Düse dann auf die ganz am Anfang der Datei ermittelte
Antasttemperatur und wartet darauf.

```gcode
;
; MBL
;
M84 E ; turn off E motor
G29 P1 ; invalidate mbl & probe print area
;G29 P1 X150 Y0 W100 H20 C ; probe near purge place
G29 P3.2 ; interpolate mbl probes
G29 P3.13 ; extrapolate mbl outside probe area
G29 A ; activate mbl

G0 Z1 ; add Z clearance

M569 S0 E ; set spreadcycle mode for extruder
G92 E0 ; reset extruder position
```

Mesh Bed Leveling in Stufen. `M84 E` nimmt zuerst den Strom vom Extrudermotor, damit er
nicht kriechen und eine Messung stören kann. `G29 P1` verwirft ein vorhandenes Netz und
tastet den Druckbereich ab — den Bereich, den `M555` weiter oben deklariert hat. `P3.2`
interpoliert zwischen den angetasteten Punkten, `P3.13` extrapoliert das Netz über den
angetasteten Bereich hinaus nach außen, damit Fahrbewegungen außerhalb des Druckbereichs
weiterhin ein definiertes Z haben, und `G29 A` aktiviert das Ergebnis.

Die auskommentierte Zeile ist eine Alternative, die stattdessen in der Nähe des
Spülbereichs antastet.

`M569 S0 E` versetzt den Extrudertreiber in spreadcycle statt stealthchop — weniger leise,
dafür berechenbareres Drehmoment, was bei einem Extruder eher gefragt ist als bei einer
Portalachse.

### Erstes Werkzeug reinigen und vorfüllen

```gcode
;-------Clean and prime initial tool------
{
local speed_tc = min(travel_speed, 350.0) * 60;
local deretract_length = 1.6;
local target_temp = first_layer_temperature[initial_tool];
local eject_temp = max(160,target_temp - 60);
local filament_area = 3.14 * filament_diameter[initial_tool] * filament_diameter[initial_tool] / 4.0;
local purge_mm = 12 / filament_area;
local purge_speed_fast = 60.0 * min(6,max(1.5,0.6*filament_max_volumetric_speed[initial_tool]/filament_area));
local purge_speed_slow = 60.0 * min(3,max(1.5,0.3*filament_max_volumetric_speed[initial_tool]/filament_area));
local tc_deretract_speed = 60.0 * min(20,max(5,deretract_speed[initial_tool]));
}

M83
G1 F{speed_tc}
M204 S7000
M104 S{eject_temp+15}
G12 S90 ; enter cleaner
M109 C{eject_temp} ; Skip residency
M104 S{target_temp + 5}
G12 S30 ; eject poop
M106 S{255 / 100 * max_fan_speed[initial_tool]}
M906 P1 ; Set extruder current
M109 C{target_temp}
M104 S{target_temp}
G1 E{deretract_length} F{tc_deretract_speed}

G91 ; use relative coordinates
M83 ; extruder relative mode
M572 S0.0 ; Disable PressureAdvance

;FLUSH_START
G1 X-0.2 E{0.15 * purge_mm} F{0.20 / (0.15 * purge_mm) * purge_speed_slow}
G1 X0.40 E{0.30 * purge_mm} F{0.40 / (0.30 * purge_mm) * purge_speed_slow}
G1 Y-0.5 E{0.10 * purge_mm} F{0.50 / (0.10 * purge_mm) * purge_speed_slow}
G1 Y-0.5 E{0.10 * purge_mm} F{0.50 / (0.10 * purge_mm) * purge_speed_fast}
G1 X-0.4 E{0.20 * purge_mm} F{0.40 / (0.20 * purge_mm) * purge_speed_fast}
G1 Y1.00 E{0.18 * purge_mm} F{1.00 / (0.18 * purge_mm) * purge_speed_fast}
G1 X0.20 E{0.05 * purge_mm} F{0.20 / (0.05 * purge_mm) * purge_speed_fast}
G1 Y0.20 E{0.02 * purge_mm} F{0.20 / (0.02 * purge_mm) * purge_speed_slow}
;FLUSH_END

M400
M906 P0 ; Revert extruder current
G1 Y0 E-{retract_length[initial_tool] + 0.04} F{retract_speed[initial_tool] * 60}
{e_retracted[initial_tool] = retract_length[initial_tool] + retract_restart_extra_toolchange[initial_tool]}
G1 Y5 F{speed_tc}

{tool_init[initial_tool] = 1}
G90 ; use absolute coordinates
M83 ; extruder relative mode
G12 S91 ; Exit cleaning station
G0 Z1.2 ; Lift
G4 S0
M221 S100 ; set flow to 100%
```

Dieser Abschnitt spiegelt bewusst den Werkzeugwechsel-Block, damit das erste Werkzeug den
Druck in demselben Zustand beginnt wie ein eingewechseltes.

**Die Reinigungsstation** wird über `G12` mit einem Untercode angesteuert. `S90` fährt
hinein, `S30` wirft das angesammelte Spülmaterial aus, `S91` fährt hinaus. Alles zwischen
`S90` und `S91` geschieht mit an der Station geparktem Kopf und nicht über dem Bett.

**Das zweistufige Temperaturvorgehen** ist der Teil, der zum Nachahmen taugt. `eject_temp`
liegt deutlich unter der Drucktemperatur. Die Düse wird vor dem Auswerfen *herunter*
gefahren, weil sich etwas abgekühltes Material als fester Klumpen von der Spitze löst,
statt Fäden zu ziehen. Erst nach dem Auswurf geht es auf Drucktemperatur hinauf.

Praktikabel wird das durch `M109 C` statt `M109 S`. Die `C`-Form wartet, bis die Temperatur
erreicht ist, überspringt aber die Haltezeit, die ein normales `M109 S` erzwingt, sodass
jede dieser Wartezeiten Sekunden statt Dutzende von Sekunden kostet. Der Kommentar im
Profil sagt genau das.

**`M906 P1` … `M906 P0`** hebt den Strom des Extrudermotors für das Spülen an und setzt ihn
danach zurück, weil das schnelle Fördern eines großen Volumens dem Motor mehr abverlangt
als das Drucken.

**Das Spülmuster** besteht aus acht kurzen Bewegungen in X und Y, die jeweils einen
angegebenen Bruchteil von `purge_mm` extrudieren. Die Vorschübe sind berechnet statt fest:
Jeder ist *Strecke ÷ Extrusion ÷ Geschwindigkeit*, was die lineare Geschwindigkeit des
Kopfes an die Extrusion koppelt, damit das Spülmaterial gleichmäßig abgelegt wird, statt
sich zu dehnen oder zu stauchen. Das Muster wechselt die Richtung, um den Strang
aufzubrechen.

`M572 S0.0` deaktiviert Pressure Advance für das Spülen — dessen ganzer Zweck ist das
Glätten von Übergängen, was unerwünscht ist, wenn absichtlich ein festes Volumen gefördert
wird.

`M400` wartet, bis die Bewegungswarteschlange leergelaufen ist, bevor der Strom
zurückgesetzt wird, damit die Änderung nicht mitten in einer Bewegung greift.

!!! important "Die letzte interessante Zeile ist `{tool_init[initial_tool] = 1}`"
    Damit wird das Startwerkzeug als bereits gereinigt und vorgefüllt markiert. Nichts in
    diesem Block verwendet das — wohl aber der Werkzeugwechsel-Block, und dort ändert es
    das Verhalten auf zwei Arten.

    Ein Werkzeug, dessen `tool_init` noch `0` ist, erhält eine feste Deretract-Länge statt
    der berechneten und wird zwingend über den Pfad der Reinigungsstation geführt, **selbst
    wenn ein Wipe Tower konfiguriert ist**. Das ist Absicht: Ein nie vorgefülltes Werkzeug
    braucht eine ordentliche Spülung, und ein Wipe Tower ist nicht der Ort dafür.

    Diese eine Zuweisung ist also der Unterschied dazwischen, ob sich der erste
    Werkzeugwechsel wie ein normaler verhält oder wie eine Erstinitialisierung. Wenn Sie
    diesen Abschnitt umschreiben, übernehmen Sie diese Zeile.

## Vor dem Schichtwechsel

```gcode
;BEFORE_LAYER_CHANGE
G92 E0.0
;[layer_z]
{if layer_z > 150}
M201 X{interpolate_table(layer_z, (0,7000), (150,7000), (200,4500), (270,2000))} Y{interpolate_table(layer_z, (0,7000), (150,7000), (200,4500), (270,2000))}
{endif}
```

`G92 E0.0` setzt den Positionszähler des Extruders bei jeder Schicht zurück und hält die
Zahlen damit klein.

Der Rest ist die interessanteste Idee im Profil: **die Beschleunigung wird verringert, je
höher der Druck wird**. `interpolate_table` nimmt die aktuelle Schichthöhe und interpoliert
zwischen den angegebenen Punkten, sodass die Beschleunigung in X und Y bis zu einer
Schwelle konstant bleibt und danach stetig zum oberen Ende des Bauraums hin abfällt.

Die Begründung ist mechanisch. Ein hohes Teil ist ein Hebel — je höher es wird, desto
stärker lenkt eine gegebene Beschleunigung seine Spitze aus und desto mehr federt auch der
Rahmen der Maschine. Die Beschleunigung mit der Höhe zu senken, tauscht Druckzeit gegen
Genauigkeit genau dort, wo sich der Tausch lohnt, und lässt niedrige Drucke unangetastet.

Die Bedingung `{if layer_z > 150}` bewirkt, dass unterhalb des konstanten Bereichs
überhaupt nichts ausgegeben wird; ein niedriger Druck trägt also keinen zusätzlichen
G-Code.

Das knüpft an eine verbreitete Einschätzung in der Community an, wonach die
Serienbeschleunigungen dieser Maschine für ihre Motoren hoch liegen, und an
[diagonale Bänderung](../issues/diagonal-banding.md), wo Extrusions- und
Bewegungsartefakte auseinandergehalten werden müssen.

## Nach dem Schichtwechsel

```gcode
;AFTER_LAYER_CHANGE
;[layer_z]

; dock fan control
{if layer_num == 1 or layer_num == 3}
  M106 P6 S0 ; dock fan off (baseline)
  {if used_tools > 1}
    ;PET-family (PET/PETG/*-CF...)/CPE/PCTG - dock fan 100 from 3rd layer
    {if layer_num == 3 and ((is_extruder_used[0] and filament_type[0]=~/(PET|CPE|PCTG)/) or ...)}
      M106 P6 S100
    {endif}

    ;low-temp materials - dock fan 100% (S255) from 1st layer (uses global low_temp_types)
    {if (is_extruder_used[0] and one_of(filament_type[0], ~low_temp_types)) or ...}
      M106 P6 S255
    {endif} ; PLA wins by order
  {endif}
{endif}
```

*(die werkzeugspezifischen Bedingungen sind gekürzt — jede entfaltet sich auf alle acht
Werkzeuge)*

`M106 P6` spricht den **Dock-Lüfter** an, nicht den Bauteillüfter. Der `P`-Index wählt
einen Lüfter aus, und Index 6 ist der Dock-Lüfter, den es nur bei INDX-Aufbauten gibt. Ein
bloßes `M106 S…` an anderer Stelle im Profil meint den Bauteillüfter.

Die Logik greift nur auf Schicht 1 und 3 und nur, wenn mehr als ein Werkzeug im Einsatz ist
— ein Druck mit einem einzigen Werkzeug hat nichts im Dock, das gekühlt werden müsste.

Im Einzelnen:

- **Schicht 1** — Grundzustand aus, dann wird der PET-Zweig übersprungen, weil er
  Schicht 3 voraussetzt; es kann also nur der Niedrigtemperatur-Zweig greifen.
  Niedrigtemperatur-Materialien bekommen den Dock-Lüfter ab der allerersten Schicht auf
  voller Leistung.
- **Schicht 3** — Grundzustand aus, dann kann der PET-Zweig den Dock-Lüfter auf
  Teilleistung setzen, und der Niedrigtemperatur-Zweig kann das anschließend mit voller
  Leistung überschreiben.

Diese Reihenfolge ist beabsichtigt, und der Kommentar im Profil hält sie fest: *PLA wins by
order*. Wo eine Platte beides mischt, ist die Niedrigtemperatur-Einstellung diejenige, die
übrig bleibt.

!!! note "`S100` sind nicht 100 Prozent"
    `M106` nimmt einen PWM-Wert von 0 bis 255 entgegen, `S255` ist also volle Leistung und
    `S100` rund 39 %. Der Kommentar am PET-Zweig lautet "dock fan 100" und meint den
    Rohwert — es ist leicht, das als Prozentangabe zu lesen und daraus zu schließen, beide
    Zweige täten dasselbe. Das tun sie nicht.

Niedrigtemperatur-Materialien brauchen die Dock-Kühlung deshalb am frühesten, weil sie am
dichtesten an der Umgebungstemperatur erweichen; bei einem Werkzeug, das neben einer
beheizten Kammer in seinem Dock steht, ist das Risiko am größten, dass das Filament darin
weich wird.

## Werkzeugwechsel

```gcode
  G1 F{speed_tc}
  M204 S7000

  G27 W3 Z{travel_max_lift[current_extruder]} P2 R{retract_toolchange} V{tc_retract_speed/60} A{travel_slope[current_extruder]}
  P0 S1 L0 D0

  T{next_extruder} S1 L0 D0

  M104 S{eject_temp+15}
  G12 S90 ; enter cleaner
  G0 Z{layer_z + 0.8} ; Lift
  M109 C{eject_temp} ; Skip residency
  M104 S{target_temp + 5}
```

Der darüberliegende Vorbereitungsblock (aus Platzgründen gekürzt) berechnet dieselben
lokalen Variablen wie der Vorfüll-Abschnitt, dazu einige Verzweigungen: Ein konfiguriertes
Spülvolumen von null fällt auf ein festes Volumen zurück, ein explizit angegebenes
Spülvolumen oder eine explizit angegebene Geschwindigkeit übersteuert den berechneten Wert,
FLEX bekommt eigene Rückzugs- und Deretract-Geschwindigkeiten, und — wie oben beschrieben —
ein nicht initialisiertes Werkzeug erhält eine feste Deretract-Länge und wird zwingend über
den Pfad der Reinigungsstation geführt.

Es gibt außerdem eine Übersteuerung für die erste Schicht: Liegt die Schicht auf oder unter
der Höhe der ersten Schicht, wird die Zieltemperatur die Temperatur der ersten Schicht
statt der normalen.

**`G27` ist der Parkbefehl**, und seine Parameter lohnen genaues Lesen:

| Parameter | Bedeutung |
|---|---|
| `W3` | Die vordefinierte **Werkzeug-Parkposition** verwenden (nur Werkzeugwechsler) |
| `Z…` | Z-Anteil der Parkposition |
| `P2` | Z-Aktion: **relative Bewegung um Z** |
| `R…` | Strecke, um die während der Parkbewegungen zurückgezogen wird |
| `V…` | Vorschub des Rückzugs, unabhängig vom Vorschub der Bewegung |
| `A…` | Die Z-Bewegung *parallel* zu XY ausführen, in diesem Winkel, bis das Ziel-Z erreicht ist |

Der Parameter `A` ist ein netter Kniff — statt erst anzuheben und dann zu fahren, steigt
der Kopf während der Fahrt auf einer Schräge, was schneller ist.

`P0 S1 L0 D0` legt dann das aktuelle Werkzeug in seinem Dock ab, und
`T{next_extruder} S1 L0 D0` nimmt das neue auf.

```gcode
    G12 S30 ; eject poop
    M106 S{255 / 100 * max_fan_speed[next_extruder]}
    M906 P1 ; Set extruder current
    M109 C{target_temp}
    M104 S{target_temp}
    G1 E{deretract_length} F{tc_deretract_speed}

    G91 ; use relative coordinates
    M83 ; extruder relative mode
    M572 S0.0 ; Disable PressureAdvance

    ;FLUSH_START
    G1 X-0.2  E{0}                F{1200}
    G1 X0.40  E{0.15 * purge_mm}  F{0.40 / (0.15 * purge_mm) * purge_speed_slow}
    G1 Y-1.20 E{0.35 * purge_mm}  F{1.20 / (0.35 * purge_mm) * purge_speed_fast}
    G1 X-0.4  E{0.20 * purge_mm}  F{0.40 / (0.20 * purge_mm) * purge_speed_fast}
    G1 Y1.20  E{0.25 * purge_mm}  F{1.20 / (0.25 * purge_mm) * purge_speed_fast}
    G1 X0.20  E{0.05 * purge_mm}  F{0.20 / (0.05 * purge_mm) * purge_speed_fast}
    ;FLUSH_END

    M400
    M906 P0 ; Revert extruder current
    G1 Y0 E-{retract_length[next_extruder] + 0.04} F{retract_speed[next_extruder] * 60}
    G1 Y5 F{speed_tc}
```

Der Pfad über die Reinigungsstation, der genommen wird, wenn kein Wipe Tower vorhanden ist
oder das ankommende Werkzeug nie vorgefüllt wurde. Er hat dieselbe Gestalt wie die
Vorfüll-Sequenz im Start-Block: kalt auswerfen, Lüfter an, Strom hoch, auf Temperatur
kommen, Deretract, in einem berechneten Muster spülen, zurückziehen, Strom zurück.

Der Wipe-Tower-Pfad gibt stattdessen eine Folge von `G750`-Bewegungen aus, die die
Wipe-Tower-Sequenz mit der Geometrie des Turms ausführen, und lässt die Station ganz aus.

```gcode
  G90 ; use absolute coordinates
  M83 ; extruder relative mode
  G12 S91 ; Exit cleaning station
  G0 Z{layer_z + 1.0} ; Lift
  G4 S0
```

!!! danger "Beide Hübe in diesem Block sind schichtrelativ"
    `G0 Z{layer_z + 0.8}` auf dem Hinweg und `G0 Z{layer_z + 1.0}` auf dem Rückweg werden
    beide aus der *aktuellen Schichthöhe* berechnet. Keiner von beiden berücksichtigt die
    Höhe von etwas, das auf der Platte bereits fertig ist. Das Parken selbst nutzt `P2`,
    eine relative Z-Bewegung, und nicht `P0`, die als "raise to at least Z above print"
    dokumentierte Option.

    Bei einem gewöhnlichen Druck wachsen alle Objekte gemeinsam, die aktuelle Schicht ist
    also das Höchste auf dem Bett, und das genügt. Bei einem **sequenziellen Druck** nicht:
    Ein fertiges Objekt kann weit über der Schicht stehen, die anderswo gerade gedruckt
    wird, und eine aus der aktuellen Schicht berechnete Fahrbewegung führt geradewegs
    hindurch.

    Das ist der Mechanismus hinter
    [Werkzeugkopf kollidiert mit fertigen Teilen](../issues/complete-individual-objects-collision.md).
    Wer diesen Block liest, sieht es so konkret, wie es der Fehlerbericht aus der Community
    nicht zeigen konnte: Die abstandsbewusste Option existiert in der Firmware, und dieses
    Profil verwendet sie nicht.

    **Das ist kein Lösungsvorschlag.** Ob `P0` das tatsächlich beheben würde, hängt davon
    ab, was die Firmware unter "above print" versteht — ob sie die Höhen fertiggestellter
    Objekte verfolgt oder nur die aktuelle —, und das ist nicht geklärt. Es ist das, was
    zuerst zu untersuchen ist, keine Änderung, die man blind vornimmt.

    TODO(verify): ob `G27 P0` bei einem sequenziellen Druck fertiggestellte Objekte
    berücksichtigt und ob die beiden Hübe `G0 Z{layer_z + …}` abstandsbewusst gemacht
    werden können.

## End-G-Code

```gcode
{if layer_z < max_print_height}G1 Z{z_offset+min(max_layer_z+1, max_print_height)} F720 ; Move print head up{endif}

; turn off extruder heaters
{if is_extruder_used[0]}M104 T0 S0{endif}
{if is_extruder_used[1]}M104 T1 S0{endif}
{if is_extruder_used[2]}M104 T2 S0{endif}
{if is_extruder_used[3]}M104 T3 S0{endif}
{if is_extruder_used[4]}M104 T4 S0{endif}
{if is_extruder_used[5]}M104 T5 S0{endif}
{if is_extruder_used[6]}M104 T6 S0{endif}
{if is_extruder_used[7]}M104 T7 S0{endif}

M140 S0 ; turn off heatbed
M141 S0 ; disable chamber control
M107 ; turn off fan
M106 P6 S0 ; turn off dock fan

P0 S1 ; park tool

G1 X242 Y205 F10200 ; park
G4 ; wait
M572 S0 ; reset PA
M221 S100 ; reset flow percentage
M84 X Y E ; disable motors
M77 ; stop print timer
; max_layer_z = [max_layer_z]
```

Zuerst fährt das Bett weg, abgesichert, damit es nicht über das Maximum der Maschine
hinauszugehen versucht.

Die Heizungen werden je Werkzeug abgeschaltet statt global — `M104 T<n> S0` spricht ein
bestimmtes Werkzeug an, und nur tatsächlich verwendete Werkzeuge werden angefasst. Danach
Bett, Kammer, Bauteillüfter und Dock-Lüfter.

`P0 S1` bringt das Werkzeug in sein Dock zurück. Ein am Ende auf dem Kopf verbliebenes
Werkzeug hieße, den nächsten Druck in einem unerwarteten Zustand zu beginnen.

`G4` ohne Argument wartet, bis die Warteschlange leergelaufen ist. `M572 S0` und `M221 S100`
setzen Pressure Advance und Fluss zurück, damit ein späterer Druck sie nicht erbt —
sinnvoll, weil beide in der Firmware über Drucke hinweg bestehen bleiben.

`M84 X Y E` deaktiviert die Motoren für X, Y und Extruder, lässt Z aber bewusst bestromt,
damit das Bett seine Position hält, statt abzusacken.

## Befehlsreferenz

Verhalten gegen den Quellcode der Prusa-Firmware verifiziert, sofern nicht anders vermerkt.

| Befehl | Was er tut |
|---|---|
| `M862.1 T P A F` | Werkzeugspezifische Düsendeklaration: Werkzeug, Durchmesser, Abrasiv-Flag, High-Flow-Flag |
| `M862.3 P"model"` | Schranke für das Druckermodell |
| `M862.5 P<n>` | Schranke für die Stufe des G-Code-Dialekts |
| `M862.6 P"feature"` | Schranke für ein erforderliches Firmware-Feature |
| `M115 U<ver>` | Deklariert die Firmware-Version, auf die die Datei zielt |
| `M555 X Y W H` | Deklariert den Druckbereich |
| `M591 S<0\|1>` | Erkennung von festsitzendem Filament aus/ein |
| `G28 XY` / `G28 Z` | Referenzfahrt der genannten Achsen |
| `T<n> S L D` | Ein Werkzeug auswählen |
| `P0 S1 [L D]` | Das aktuelle Werkzeug in seinem Dock parken |
| `G27 W Z P R V A` | Den Kopf parken; Parameter siehe Tabelle oben |
| `G427 R P` | Werkzeug-Offset-Kalibrierung; `R` Versatz in mm, `P` gemittelte Antastungen |
| `G29 G` | Durchwärmen / Wärme aufnehmen |
| `G29 P1` | Das Netz verwerfen und den Druckbereich antasten |
| `G29 P3.2` | Zwischen den angetasteten Punkten interpolieren |
| `G29 P3.13` | Das Netz über den angetasteten Bereich hinaus extrapolieren |
| `G29 A` | Das Netz aktivieren |
| `G12 S90` | Die Reinigungsstation anfahren |
| `G12 S30` | Angesammeltes Spülmaterial auswerfen |
| `G12 S91` | Die Reinigungsstation verlassen |
| `G750 Y F A` | Wipe-Tower-Bewegung |
| `M104 S` / `M104 T<n> S` | Düsenziel setzen, aktuelles oder benanntes Werkzeug, ohne Warten |
| `M109 S` | Düsenziel setzen und warten, einschließlich Haltezeit |
| `M109 C` | Düsenziel setzen und warten, **ohne Haltezeit** |
| `M140 S` / `M190 R` | Bett-Ziel / auf das Bett warten |
| `M141 S` / `M191 S` | Kammer-Ziel / auf die Kammer warten |
| `M106 S` | Bauteillüfter, PWM 0–255 |
| `M106 P6 S` | **Dock-Lüfter**, PWM 0–255 |
| `M107` | Bauteillüfter aus |
| `M204 S` | Beschleunigung setzen |
| `M201 X Y` | Maximale Beschleunigung je Achse setzen |
| `M221 S` | Flussprozentsatz |
| `M572 S` | Pressure Advance; `S0` deaktiviert |
| `M569 S0 E` | Extrudertreiber auf spreadcycle |
| `M906 P<0\|1>` | Extruderstrom: zum Spülen angehoben, danach zurückgesetzt |
| `M400` | Warten, bis die Bewegungswarteschlange leergelaufen ist |
| `M84 [axes]` | Die genannten Motoren deaktivieren |
| `M77` | Den Drucktimer stoppen |
| `M262 P B` | Pin-Richtung am IO-Expander — `B0` Ausgang, `B1` Eingang |
| `M264 P B` | Pin-Pegel am IO-Expander — `B0` low, ungleich null high |
| `M574 S V T F` | **Nicht implementiert** — kein Handler; als unbekannt protokolliert und übersprungen |

## Verifikation

`measured` (gemessen) — dies ist Prusas ausgeliefertes Profil für Firmware 6.9.0,
wortgetreu wiedergegeben statt rekonstruiert, und das Verhalten jedes Befehls wurde gegen
den Firmware-Handler geprüft, der ihn implementiert, statt aus Standard-Marlin
angenommen zu werden.

Diese Herkunft rechtfertigt die Stufe. Es sind nicht die Einstellungen eines einzelnen
Besitzers, die zufällig funktioniert haben; es sind die Voreinstellungen des Herstellers,
mit denen jeder INDX auf dieser Firmware startet. Die Werte sind daher in einem Sinn
allgemeingültig, in dem es die übrigen Zahlen dieser Website nicht sind — und nur deshalb
stehen sie hier überhaupt, wo die Website Druckeinstellungen sonst zurückhält, bis sie
jemand auf Hardware verifiziert hat.

Wo sich die Bedeutung eines Befehls nicht klären ließ, ist das als solches gekennzeichnet
und nicht geraten. `M574` ist der einzige in diesem Zustand, und die Unterscheidung ist
wichtig: Sein *Fehlen* in der Firmware ist inzwischen nach demselben Maßstab belegt wie das
Vorhandensein der übrigen Befehle — geprüft gegen das Release-Tag v6.9.0 und gegen jedes
Objekt in der Historie des öffentlichen Repositorys, mit Positivkontrollen. Wozu er gedacht
war, ist weiterhin unbekannt und wird an Ort und Stelle markiert statt rekonstruiert.
Prusas Ankündigung einer Pressure-Advance-Kalibrierung über die Wägezelle vom August 2026
stammt aus erster Hand und ist belegt, aber nichts Veröffentlichtes verbindet sie mit
diesem Befehl; die Seite hält beides bewusst auseinander.

`M262` und `M264` verdienen eine Anmerkung. Sie werden häufig als Befehle für die
Kammerbeleuchtung beschrieben, und das Profil, aus dem sie stammen, hat sie so bezeichnet.
Das sind sie nicht: Die Firmware implementiert sie als generische Operationen eines
I2C-GPIO-Expanders — eine Pin-Richtung konfigurieren, einen Pin-Pegel schreiben. Was ein
bestimmter Pin steuert, hängt davon ab, was der Besitzer daran angeschlossen hat. Alles,
was Sie lesen und was sie als Beleuchtungsbefehl behandelt, beschreibt eine Konvention,
nicht den Befehl.

*Nicht* verifiziert ist, ob diese Voreinstellungen *gut* sind. Sie sind das, was Prusa
ausliefert, was sie als Beschreibung maßgeblich macht und nichts darüber aussagt, ob ein
bestimmter Wert für Ihr Filament oder Ihr Teil optimal ist. Mehrere davon sind unter
Besitzern umstritten — sowohl die Serientemperaturen als auch die Serienbeschleunigungen
kommen im Forum als zu hoch für diesen Werkzeugkopf zur Sprache. Eine Voreinstellung
wiederzugeben heißt nicht, sie zu befürworten.

Statisch ist das Profil ebenfalls nicht. Es ändert sich über Firmware-Versionen hinweg: Die
Fassung von 6.6.3 hatte im Ausdruck für die Antasttemperatur einen falsch geschriebenen
Variablennamen, verwendete einen anderen Offset für PC und PA, ließ die globale Variable
`low_temp_types` weg, von der der Block nach dem Schichtwechsel abhängt, und enthielt
Befehle für die Kammerbeleuchtung, die diese Fassung weglässt. Weicht Ihre Firmware von der
Version im Front Matter ab, rechnen Sie mit Unterschieden.

## Verwandte Seiten

- [Werkzeugkopf kollidiert mit fertigen Teilen](../issues/complete-individual-objects-collision.md)
  — die schichtrelativen Hübe des Werkzeugwechsel-Blocks im Zusammenhang
- [Sabbern verdirbt das Antasten des Betts](../issues/oozing-during-probing-and-calibration.md) —
  warum die Antasttemperatur so berechnet wird, wie sie berechnet wird
- [Werkzeug-Offset-Kalibrierung schlägt fehl](../issues/offset-sensor-board-failure.md) —
  was passiert, wenn `G427` nicht durchlaufen kann
- [Blobs, die in den Druck geschleppt werden](../issues/stringing-and-wiper-calibration.md) —
  das Spül- und Reinigungsverhalten, das diese Blöcke ansteuern
