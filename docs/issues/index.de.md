---
title:        Probleme
confidence:   unknown
updated:      2026-08-24
author:       hyiger
printer:      unknown
toolhead:     unknown
hotend:       unknown
nozzle:       unknown
firmware:     unknown
sources:      []
superseded_by:
source_sha:   a3bfa0859145e13f23967b56c19bb8011997e1b96469f983a5782d44c4184c2c
---
# Probleme

Bekannte Fehler am INDX, wodurch sie entstehen und was sie tatsächlich behoben hat.

Die Seiten hier beginnen mit dem **Mechanismus** statt mit der Abhilfe. Das ist
Absicht: Mehrere INDX-Fehler sehen von außen gleich aus und haben völlig
verschiedene Ursachen, und wer versteht, warum ein Symptom auftritt, kann den
eigenen Fehler von dem unterscheiden, der ihm lediglich ähnelt.

## Wie eine Seite hier zu lesen ist

Prüfen Sie das Feld `confidence`, bevor Sie handeln. Eine `provisional`-Seite
(vorläufig) ist die aufgeschriebene Erfahrung einer einzelnen Person, damit die
nächste sie wiedererkennt — keine Anleitung.

Wenn eine Seite eine Zahl hinter einer `TODO(verify)`-Markierung zurückhält, ist das
beabsichtigt. Schwellenwerte, Temperaturen, Maße und Fristen werden an der Hardware
oder beim Hersteller überprüft, bevor sie hier veröffentlicht werden, denn ein
falscher Wert kostet den Leser ein Bauteil, einen Druck oder eine Gewährleistungsfrist.

## Beginnen Sie beim Symptom

**Die Maschine beschädigt den Druck oder sich selbst**

- [Werkzeugkopf kollidiert mit fertigen Teilen](complete-individual-objects-collision.md) —
  Slicen mit *Complete individual objects* bei mehr als einem verwendeten Werkzeug kann den
  Kopf durch Teile fahren lassen, die er bereits fertiggestellt hat. Auf Prusas Toolchangern
  seit März 2025 offen und unbehoben. Schalten Sie die Funktion ab.

**Der Drucker widerspricht der Realität darüber, welches Werkzeug wo ist**

- [Phantomwerkzeuge, "tool not detected" und fehlgeschlagenes Parken](tool-detection-ringdown-decay.md)
  — ein Werkzeug, das nicht da ist, wird als vorhanden gemeldet, ein Werkzeug, das da ist,
  wird als fehlend gemeldet, oder ein korrekt geparktes Werkzeug wird als weiterhin
  angedockt gemeldet.

**Abtasten oder Kalibrierung schlägt fehl**

- [Abtasten schlägt fehl oder die Düse berührt das Bett nie](loadcell-emi-noise.md) —
  elektrische Störungen im Signal der Wägezelle lassen den Drucker glauben, er habe
  aufgesetzt, während die Düse noch deutlich frei steht.
- [Werkzeug-Offset-Kalibrierung schlägt fehl](offset-sensor-board-failure.md) — der
  berührungslose Offsetsensor liefert keine Messwerte, sodass die Kalibrierung keine
  Grundlage hat. Meist die Sensorplatine.
- [Oozing verdirbt Bettabtastung und Werkzeugkalibrierung](oozing-during-probing-and-calibration.md)
  — Material dort, wo die Maschine eine Messung vornehmen will. Beginnen Sie damit, das
  Fenster des Offsetsensors zu reinigen.

**Fehler treten am gedruckten Teil auf**

- [In den Druck geschleppte Materialklumpen — Düsenwischer und Purge](stringing-and-wiper-calibration.md)
  — Material, das beim Werkzeugwechsel aus dem Purge-Bereich mitgeführt wird. Weitgehend
  behoben mit Firmware 6.9.0, die das Ausrichten des Wischers automatisiert hat, das zuvor
  von Hand erfolgte.
- [Diagonales Banding an Druckwänden](diagonal-banding.md) — ein regelmäßiges Muster, das
  sich mit der Richtung der Perimeter umkehrt. Es gibt einen Test mit zwei Drucken, der
  zeigt, ob es am Extruder oder am Bewegungssystem liegt, bevor Sie einen Supportfall eröffnen.

**Düsen und der Filamentweg**

- [Düsenhärte und abrasive Filamente](nozzle-hardness.md) — die ausgelieferten Düsen
  sind nicht im üblichen Sinne gehärtet. Was das für gefüllte Filamente bedeutet, und
  das Abhilfeangebot des Herstellers.
- [Fehlgeschlagenes Entladen und Auswerfen](filament-guide-bore-unload-failure.md) — der
  Druck funktioniert, das Entladen schlägt fehl. *Einzelquelle — lesen Sie den Vorbehalt,
  bevor Sie handeln.*
- [Nur eine Düsengröße hat ein Slicer-Profil](missing-slicer-profiles.md) — der Slicer
  bietet für den INDX nur eine Düsenvariante an, sodass andere Größen gar nicht ausgewählt
  werden können. Gut zu wissen, bevor Sie Düsen kaufen oder dafür Guthaben im Shop annehmen.

**Vorgehen**

- [Wen Sie kontaktieren](support-and-warranty-path.md) — Diagnose und Ersatzteile kommen
  von zwei verschiedenen Unternehmen, und das Problem an das falsche zu schicken ist die
  häufigste Art, wie Besitzer Wochen verlieren.

## Mit einem Fehlercode hier gelandet?

Der Block `361xx` ist die Toolchanger-Familie. Dies sind die Codes, die auf eine Seite
abgebildet werden:

| Code | Auf dem Display | Seite |
|---|---|---|
| `36121` `36122` | Unknown nozzle | [Düsenhärte](nozzle-hardness.md) |
| `36123` | Occupied dock | [Werkzeugerkennung](tool-detection-ringdown-decay.md) |
| `36124` | Tool lost | [Werkzeugerkennung](tool-detection-ringdown-decay.md) |
| `36125` | Tool pickup failed | [Werkzeugerkennung](tool-detection-ringdown-decay.md) |
| `36127` | Tool park failed | [Werkzeugerkennung](tool-detection-ringdown-decay.md) |
| `36128` | Retry tool park | [Werkzeugerkennung](tool-detection-ringdown-decay.md) |
| `36130` | Tool offset failed | [Werkzeug-Offset-Kalibrierung](offset-sensor-board-failure.md) |
| `36135` | Toolchanger error | [Werkzeugerkennung](tool-detection-ringdown-decay.md) |
| `36136` | Calibrate dock from menu | [Werkzeug-Offset-Kalibrierung](offset-sensor-board-failure.md) |
| `36202` | Hotend preheat error | [Werkzeugerkennung](tool-detection-ringdown-decay.md) |
| `36526` `36527` `36528` | Loadcell measure failed / bad configuration / timeout | [Störungen der Wägezelle](loadcell-emi-noise.md) |

Prusa veröffentlicht zu jedem Code einen Artikel, der von der jeweiligen Seite aus
verlinkt ist. Es gibt rund 104 verschiedene INDX-Codes; die obigen sind diejenigen, zu
denen diese Wissensdatenbank etwas beizutragen hat. Für alles andere ist Prusas eigener
Artikel die bessere Antwort.

## Drei Fehler, die sich gleich zeigen

Fehler beim Abtasten und Kalibrieren werden am häufigsten falsch diagnostiziert, weil
sich drei nicht zusammenhängende Ursachen über dieselben zwei Fehlerpfade äußern. Die
schnellsten Unterscheidungsmerkmale:

| Was Sie sehen | Wahrscheinliche Seite |
|---|---|
| Das Abtasten stoppt, während die Düse **sichtbar** weit vom Druckblech entfernt ist | [Störungen der Wägezelle](loadcell-emi-noise.md) |
| Die Bettabtastung funktioniert, aber die **Werkzeug-Offset-Kalibrierung** schlägt fehl | [Offsetsensor](offset-sensor-board-failure.md) |
| Material sammelt sich an der Düse, Ablagerungen bleiben auf dem Druckblech zurück | [Oozing](oozing-during-probing-and-calibration.md) |
| Die Fehler folgen auf ein **Firmware-Update**, statt allmählich aufzutreten | [Werkzeugerkennung](tool-detection-ringdown-decay.md) |

Der falschen dieser Ursachen nachzujagen kostet Tage; deshalb beginnt jede Seite damit,
wie man sie von ihren Nachbarn unterscheidet.
