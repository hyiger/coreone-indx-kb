---
title:        Oozing verdirbt Bettabtastung und Werkzeugkalibrierung
confidence:   reported
updated:      2026-11-08
author:       hyiger
printer:      Core One
toolhead:     INDX
hotend:       unknown
nozzle:       0.25mm, 0.4mm, 0.8mm reported
firmware:     unknown for most reports; source read at the v6.9.1, v6.9.2, v7.0.0 and v8.0.0 tags
sources:
  - https://forum.prusa3d.com/forum/prusa-indx-how-do-i-print-this-printing-help/petg-oozing-and-impeding-bed-probing/
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/printing-pc-on-indx-oozing-at-bed-probing-leveling/
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/psa-if-you-are-struggling-with-tool-offset-calibration-failing-non-stop-at-the-start-of-a-print-get-firmware-6-9-1/
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5483
  - https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/nozzle-cleaning-calibration-issues/
  - https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/a-summary-of-common-indx-problems/
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.9.1
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/compare/v6.9.1-beta...v6.9.1
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5494
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5505
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/lib/Marlin/Marlin/src/gcode/bedlevel/ubl/G29.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/src/feature/tool_offset_calibration/tool_offset_calibration.cpp
  - https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/bed-leveling-issues-3/
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.9.2
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/compare/v6.9.1...v6.9.2
  - https://help.prusa3d.com/downloads/core-one-indx
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.10.1
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5567
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/src/marlin_stubs/G427.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/src/marlin_stubs/M865.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v7.0.0
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v7.0.1
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v8.0.0
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/compare/v6.9.2...v8.0.0
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/src/feature/tool_offset_calibration/tool_offset_calibration.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/lib/Marlin/Marlin/src/gcode/bedlevel/ubl/G29.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/src/marlin_stubs/M865.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/ProjectOptions.cmake
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/src/gui/screen/filament/screen_filament_detail.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/commit/210606e66889cb636f93de34fcd6bf052367222f
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5568
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5577
superseded_by:
source_sha:   490cbfa2b11ecdff12277e794409eac32aa961a5af332d5e3d9afebfe1a0781a
---
# Oozing verdirbt Bettabtastung und Werkzeugkalibrierung

## Zusammenfassung

Filament, das austritt, während die Maschine abtastet oder kalibriert, bringt Material
genau dorthin, wo die Maschine eine Messung vornehmen will, und die Messung schlägt
fehl. Besitzer sind sowohl bei der Bettabtastung als auch bei der
Werkzeug-Offset-Kalibrierung darauf gestoßen, mit mehr als einer Filamentsorte. Es gibt
mehrere begünstigende Ursachen, und es lohnt sich, sie auseinanderzuhalten: Die mit den
besten Belegen aus erster Hand — ein verschmutztes Fenster des Offset-Sensors — lässt
sich zugleich am leichtesten beheben und wird am wenigsten wahrscheinlich zuerst
vermutet.

## Details

Zwei verschiedene Messungen werden durch Oozing verdorben, und sie schlagen
unterschiedlich fehl:

- **Bettabtastung.** Material sammelt sich vor oder während des Abtastvorgangs an der
  Düsenspitze an, sodass der Kontakt zu früh oder uneinheitlich erkannt wird. Besitzer
  berichten, dass die Abtastung sichtbare Ablagerungen auf dem Druckblech hinterlässt.
- **Werkzeug-Offset-Kalibrierung.** Austretendes Filament stört die korrekte Erfassung
  der Düse durch den Offset-Sensor, und die Kalibrierung schlägt fehl. Ein Besitzer
  berichtet, dass dies nach dem Wechseln von Düsengrößen bei jedem Werkzeug fehlschlug
  und er sämtliches Filament entladen, kalibrieren und dann wieder laden musste.

### Hier anfangen: das Fenster des Offset-Sensors reinigen

Die Lösung, die den maßgeblichen Thread dazu tatsächlich abgeschlossen hat, war das
Reinigen des Sensorfensters an jeder Düse. Der Besitzer berichtete, dass die
Wattestäbchen sichtbar schwarz wurden, obwohl er nicht glaubte, die Fenster berührt zu
haben, und dass ein Testdruck danach funktionierte. Das kostet ein paar Minuten und ist
der Punkt mit dem höchsten Nutzen.

Zu welchem Sensor dieses Fenster gehört, ist umstritten. Antworten im selben Thread
nennen es ein Temperaturfenster, und die [Seite zur Silikonsocke](silicone-sock-migration.md),
nach der der auf Wirbelströmen beruhende Offset-Sensor überhaupt kein optisches Fenster
hat, lässt die Zuordnung offen. Das Ergebnis der Reinigung gilt in beiden Fällen.

!!! warning "Das Sensorfenster nicht mit IPA reinigen"
    Der im Thread weitergegebene Rat lautet, Seifenwasser und ein Wattestäbchen zu
    verwenden statt Isopropylalkohol, mit der Begründung, IPA sei für dieses Fenster
    zu aggressiv. Die Herkunft gehört klar benannt: Dies wurde als eine auf Discord
    kursierende Herstellerempfehlung beschrieben, und die Person, die sie weitergab,
    sagte offen, dass sie keine offizielle Quelle nennen könne. Seifenwasser ist
    ohnehin die risikoärmere Wahl, ihm ist also der Vorzug zu geben — die Begründung
    sollte jedoch als unbestätigt gelten.

    TODO(verify): ob der Hersteller ein offizielles Reinigungsverfahren für das
    Fenster des Offset-Sensors veröffentlicht hat.

!!! warning "Reinigen, aber nicht polieren"
    Eine spätere Warnung im selben Thread ist beachtenswert: Die Sensorfläche soll
    matt sein und darf am Ende nicht glänzend oder spiegelnd wirken. Gehen Sie
    sparsam vor. Ziel ist es, Filamentrückstände abzunehmen, nicht Glanz zu erzeugen.

    Ein Vorbehalt zu diesem Rat — der Besitzer, der ihn gibt, beschreibt den Sensor
    als infrarotbasiert, während der Offset-Sensor an anderer Stelle als
    wirbelstrombasiert beschrieben wird. Das sind unterschiedliche Messprinzipien,
    und es ist nicht klar, welche Komponente gemeint ist. Die praktische Anweisung
    trägt in beiden Fällen: die Rückstände entfernen und es dabei belassen.

### Das Filament trocknen

Früh und wiederholt vorgeschlagen, insbesondere für PETG: Feuchtigkeit lässt Filament
Fäden ziehen und begünstigt, dass es an der Düse haften bleibt. Das ist gängige Praxis
und keine INDX-spezifische Erkenntnis, und in diesen Threads wurde es als erste
Vermutung und nicht als bestätigte Ursache geäußert — der INDX gilt Berichten zufolge
jedoch als feuchtigkeitsempfindlicher als der Nextruder, den er ersetzt, weshalb es
sich lohnt, dies auszuschließen, bevor man Komplizierterem nachjagt.

### Rückstände, die die Reinigung vor der Kalibrierung hinterlässt

`reported`, dass die Rückstände die Messung verderben; `provisional` für den zu hoch
ausfallenden Z-Offset, der auf einem einzigen Bericht beruht. Bevor die
Werkzeug-Offset-Kalibrierung ein Werkzeug vermisst, spült, kühlt und wischt sie dessen
Düse; was das Wischen nicht erfasst, sitzt also an der Düse, wenn sie vermessen wird. Ein INDX-Besitzer, der im Oktober einen
Bericht zu 6.9.2 und 7.0.0 einreichte, fand unter 6.9.0 hin und wieder PETG an der Düse,
bevor sie angetastet wurde, unter den beiden späteren Versionen dagegen oft, und führte
einen zu hoch ausfallenden Z-Offset darauf zurück
([#5567](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5567)). Die Rückkehr zu
6.9.0 half deutlich, behob es aber nicht. Die Verschlechterung führt er auf die
niedrigere Kalibriertemperatur zurück, die mit 6.9.1 kam und bei der übrig gebliebenes
PETG vollständig hart ist. Anfang November beschrieb ein Kommentator einer separaten
Anfrage ([#5568](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5568)) denselben
Fehler mit PCTG: Wenn er nicht vor jedem Druck einen Klumpen von der Düse entfernt,
scheitert die Prüfung des Z-Offsets, auch bei einer frischen Düse. Er nennt weder
Maschine noch Firmware, auch wenn die Anfrage den INDX betrifft, und sagt nicht, in
welche Richtung der Offset abwich. Der Firmware-Quellcode, den Prusa für 7.0.0, 7.0.1 und
8.0.0 am 3. November veröffentlicht hat, zeigt, dass sich daran bis 8.0.0 nichts geändert
hat: Die Reinigung durchläuft dieselben Schritte in derselben Reihenfolge und kühlt auf
dieselbe gedeckelte Temperatur ab wie unter 6.9.2 (siehe *Überprüfung*). Im Quellcode
gehört der Eintrag zu 7.0.0 über eine verbesserte Reinigung durch den Nozzle Wiper,
übernommen aus der Firmware
[6.10.1](https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.10.1) für XL und
XL+, zum Wischer-Zubehör von Druckern ohne INDX, und die geringere Verlangsamung flexibler
Filamente in 8.0.0 ändert, wie schnell der Extruder sie fördert, nicht die Reihenfolge
der Reinigung oder ihre Temperatur. Andere Besitzer melden dieselben Rückstände und führen
sie auf die Reihenfolge der Reinigung oder auf ihre Temperatur zurück; diese Belege sind
unter *Rückstände nach der Reinigung vor der Kalibrierung* auf der Seite
[In den Druck geschleppte Blobs](stringing-and-wiper-calibration.md) gesammelt.

### Die Abtasttemperatur ist möglicherweise nicht die erwartete

Es gibt ein berichtetes Verhalten von Firmware und Slicer, bei dem die Temperatur für
die Bettabtastung vor dem Druck aus dem Filament abgeleitet wird, das **Werkzeug 1**
zugewiesen ist, und nicht aus dem Werkzeug, das die Abtastung tatsächlich ausführt. Ist
T1 ein Hochtemperaturmaterial zugewiesen, tastet alles heiß ab und sickert, unabhängig
davon, was anderswo geladen ist.

Der berichtete Workaround ist elegant, sofern er trägt: Es genügt, im Slicer für T1 ein
Niedertemperatur-Filament zu *deklarieren* — das physische Filament muss gar nicht
vorhanden sein —, was erklären würde, warum Aufträge, die aus Profilen mit einem
angenommenen Niedertemperaturmaterial gesliced wurden, das Problem nie zeigten. Im Standardprofil, das diese
Website wiedergibt, ist die Regel allerdings an das Startwerkzeug des Drucks gebunden und
nicht an T1 — lesen Sie den PC-Abschnitt weiter unten, bevor Sie sich darauf verlassen. Es
gibt außerdem einen Ansatz über den Start-G-Code, der die Abtasttemperatur vor dem Block für
das Mesh Bed Leveling erzwingt, indem der erzeugte Temperaturbefehl durch einen festen
ersetzt wird.

TODO(verify): die zu erzwingende Abtasttemperatur sowie den genauen G-Code-Befehl und
das zugehörige Argument. Außerdem TODO(verify): die Absenkung, die ein Besitzer beim
gleichen Symptom auf einer Core One ohne INDX erfolgreich verwendet hat, angegeben als
Bereich statt als Einzelwert. Auf dieser Seite wird keine Temperatur veröffentlicht,
bevor sie jemand auf der Hardware bestätigt hat.

Zwei weitere berichtete Einzelheiten in diesem Bereich, die man kennen sollte, bevor man
auf die Suche geht: Ein Konfigurationsupdate des Slicers hat die Ableitung für die
meisten Materialien korrigiert, mindestens ein Konstruktionsmaterial tastet jedoch
weiterhin heiß ab; und die Temperatur für die Werkzeug-Offset-Kalibrierung ist in der
Firmware fest hinterlegt und lässt sich nicht per G-Code ändern, weshalb dieser
Workaround gegen diesen Fehlerfall nicht hilft. Der Firmware-Quellcode bestätigt die
zweite Einzelheit nur zum Teil. Vom Git-Tag v6.9.1 bis v8.0.0 legt die Kalibrierung ihre
Abtasttemperaturen selbst fest, auf oder unter einer fest eingebauten Obergrenze, und
der Kalibrierbefehl `G427` liest kein Temperaturargument, sodass kein G-Code die
Abtasttemperatur über diese Obergrenze anheben kann. Darunter folgt die Temperatur
der Z-Abtastung dem Vorheizwert des Filaments, das in diesem Werkzeug geladen ist, und
`M865` kann diesen Wert sowie die Temperatur, bei der das Werkzeug spült, bei einem
benutzerdefinierten oder Ad-hoc-Filament ändern. Ein eingebautes Preset bleibt außer
Reichweite, doch seit 7.0.0 macht die neue Schaltfläche Customize am Drucker aus einem
geladenen Preset eine bearbeitbare Kopie nur für diesen Slot, die bis zum Entladen des
Filaments erhalten bleibt und als Ad-hoc-Filament gilt. Die Temperatur der XY-Abtastung
ist fest. Die Kalibriertemperatur ist also
gedeckelt, nicht fest: G-Code kann die Temperatur der Z-Abtastung senken, sie aber
weder anheben noch die der XY-Abtastung verschieben (siehe *Überprüfung*). Ein
Fehlerbericht vom Oktober, nach dem die niedrigere Kalibriertemperatur übrig gebliebenes
PETG verschlimmert, schlägt unter seinen Abhilfen einen Temperaturparameter für den
Kalibrierbefehl vor oder eine Temperatur, die sich wie die beim Abtasten des Betts nach
dem Filament richtet
([#5567](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5567)). Es gibt zudem
eine verwandte Slicer-Falle, bei der die **Bett**temperatur auf dieselbe Weise T1 folgt.

**Das Konstruktionsmaterial ist PC.** Ein [zweiter Besitzer](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/printing-pc-on-indx-oozing-at-bed-probing-leveling/) geriet damit an
PC Blend und beschrieb es von der anderen Seite: Die Abtastung lief heiß genug, um auf
das Blech zu sickern und das Leveling scheitern zu lassen, und ein händisches Absenken
der Düsentemperatur beim nächsten Versuch behob es vollständig. Damit stand „mindestens
ein Konstruktionsmaterial tastet weiterhin heiß ab“ nicht mehr auf einem einzigen
Bericht und bekam einen Namen, und es ist seither nicht bei einem Besitzer geblieben. Zwei
weitere Besitzer im selben Thread, einer in einem [anderen Thread](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/psa-if-you-are-struggling-with-tool-offset-calibration-failing-non-stop-at-the-start-of-a-print-get-firmware-6-9-1/) und ein
[Firmware-Issue](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5483) beschreiben alle, dass PC Blend beim Abtasten des Betts
scheitert, bis die Temperatur sinkt.

**Woher die Temperatur kommt.** Es gibt **kein eigenes Feld für die Abtasttemperatur** im
Slicer, wohl aber eine Regel. Der Standard-Start-G-Code des Druckers ermittelt die
Abtasttemperatur aus dem Filament des **Startwerkzeugs** des Drucks — des ersten
Werkzeugs, das der Druck tatsächlich nutzt — und behandelt PC und PA gesondert:
mit einem festen Abstand unter der Temperatur der ersten Schicht. Das kommentierte Profil
gibt diesen Ausdruck in seinem Abschnitt zu den globalen Variablen und der
Abtasttemperatur wieder — siehe [kommentiertes Profil](../gcode/indx-profile-gcode.md). An
diese Regel stoßen diese Besitzer immer wieder.

**Startwerkzeug, nicht T1.** Dieser Ausdruck liest das Filament von `initial_tool`, und
das ist nicht das weiter oben berichtete T1-Verhalten. Beide wählen nur dann dasselbe
Filament, wenn ein Druck auf T1 beginnt. Bei einem Druck, der auf einem anderen Werkzeug
beginnt, zeigen sie auf verschiedene Presets — in diesem Profil hilft es also nicht, für
T1 ein Niedertemperatur-Filament zu deklarieren, wenn der Druck auf T3 beginnt;
maßgeblich ist das Filament, mit dem Ihr Druck startet. Ob der frühere T1-Bericht ein
älteres Profil oder einen anderen Maschinenzustand beschreibt, ist nicht geklärt.

**Bislang nennt keine Firmware-Version hier eine Änderung.** Die 6.9.1-Beta senkte die
Temperatur für die *Werkzeug-Offset-Kalibrierung*, einen eigenen Firmware-Schritt. Die
Temperatur beim Abtasten des Betts stammt aus dem Slicer-Profil, weshalb PC Blend auch
unter der Beta weiterhin heiß abtastet, und der gegen die Beta eröffnete
[Fehlerbericht](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5483) ist
noch immer offen, ohne Antwort von Prusa. Die
[stabile Version 6.9.1](https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.9.1),
veröffentlicht am 2026-09-25, nennt einen Assistenten zum Ausrichten des Portals und eine
Korrektur beim Referenzieren — zur Abtasttemperatur nichts.
Auch die Kalibrierungsänderungen der Beta tauchen in den Versionshinweisen der stabilen
Version nicht wieder auf, enthalten sind sie trotzdem: Im Firmware-Repository ist die
stabile Version das Beta-Tag plus
[15 weitere Commits](https://github.com/prusa3d/Prusa-Firmware-Buddy/compare/v6.9.1-beta...v6.9.1),
von denen keiner die Werkzeug-Offset-Kalibrierung berührt. Das ergibt sich aus der
Release-Historie, nicht aus den Versionshinweisen. 6.9.2, erschienen am 2026-10-07,
ändert hier ebenfalls nichts: Am INDX ist es die stabile 6.9.1 plus die Filament-Presets
für PVA und BVOH, die die Versionshinweise zu 6.9.1 angekündigt, aber nicht mitgeliefert
hatten
([Vergleich](https://github.com/prusa3d/Prusa-Firmware-Buddy/compare/v6.9.1...v6.9.2)).
Firmware 7.0.0 vom 15. Oktober 2026 (laut
[Prusas Download-Seite](https://help.prusa3d.com/downloads/core-one-indx)) nennt zur
Abtasttemperatur ebenfalls nichts, und ebenso wenig 8.0.0 vom 22. Oktober, was dazu
passt, dass der Wert aus dem Slicer-Profil kommt. Auch die ausführlicheren Notes zu beiden,
die Prusa am 3. November auf GitHub gestellt hat, sagen dazu nichts. Am 18. Oktober stieß ein weiterer Kommentator des
Fehlerberichts gleich beim ersten Versuch mit PC Blend auf den Fehler, ohne Maschine
oder Firmware-Version zu nennen. Wie PC Blend unter den stabilen Versionen 6.9.1, 6.9.2,
7.0.0, 7.0.1 oder 8.0.0 abtastet, hat bislang kein Besitzer berichtet.

**Anpassen.** Ein Besitzer vergrößerte den PC-Abstand im Start-G-Code des Druckers, und
die Fehlschläge hörten auf. Der Haken, auf den er selbst hinwies: Ein
Konfigurationsupdate des Druckers ersetzt den Start-G-Code, sodass die Änderung nach
jedem Update neu vorgenommen werden muss. Derselbe Ausdruck prüft außerdem die
Filamentnotizen des Startwerkzeugs auf eine Überschreibungsmarke, bevor er überhaupt
den PC-Fall erreicht; das deutet auf einen Weg je Filament hin, der solche Updates
überstehen würde — doch das ist eine Lesart des Profils und nichts, das ein Besitzer als
getestet berichtet hat. Und die slicereigene **Option zur Sickerverhinderung half
nicht**, sodass es einen Druck kostet, zuerst danach zu greifen. Der Besitzer, der den
Fehlerbericht zu PC Blend eingereicht hat, schlägt eine Notlösung vor, die keine Datei
berührt: Sobald die Bettabtastung beginnt, die Düsentemperatur im Tune-Menü
herunterdrehen. Das ist das oben beschriebene händische Absenken, abgestimmt auf die
Abtastung, und es muss bei jedem Druck wiederholt werden.

TODO(verify): Diese Berichte nennen die Temperatur, mit der PC abgetastet wurde, die
niedrigeren, die funktionierten, und den angepassten Abstand. Nichts davon wird hier
veröffentlicht. Forenbeiträge und ein Fehlerbericht sind nicht die Hardware-Bestätigung,
die diese Seite verlangt, bevor eine Temperatur auf ihr erscheint — aber sie sind
Hinweise, und es ist dieselbe Angabe, nach der die Markierung weiter oben fragt.

### Wenn das Leveling scheitert und neu ansetzt

`provisional` für die Berichte der Besitzer — es sind wenige, und auf den ersten Blick
stimmen sie nicht überein. Der Firmware-Quellcode, weiter unten, ordnet jeden dem
Schritt zu, der fehlschlug. Ist das Bett-Leveling an einer verschmutzten Düse
gescheitert, sollten Sie nicht darauf zählen, dass der nächste
Versuch mit einer sauberen beginnt. Eine
[Funktionsanfrage](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5494)
beschreibt, wie der Kopf zum Abstreifer fährt und dann für einen weiteren Versuch zum
Bett zurückkehrt, ohne die Düse zu säubern. Ein Besitzer mit der 6.9.1-Beta fand im
[Thread zur Düsenreinigung](https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/nozzle-cleaning-calibration-issues/)
das Werkzeug im Silikon-Abstreifblock geparkt vor, wo die Düse für eine Reinigung von
Hand nicht erreichbar war; der Druck lief erst nach mehreren Wiederholungen an. Zwei
weitere Besitzer dort beschreiben etwas anderes: einen neuen Versuch, der die Düse erneut
aufheizt, spült und abstreift, selbst nachdem sie von Hand gereinigt wurde, und sie dabei
so verschmutzt, dass es wieder scheitert. Einer von ihnen nutzte ebenfalls einen
6.9.1-Build und hält es für möglich, dass seine eigene Abstreifer-Einstellung oder ein
Fehler der Wägezelle schuld ist; der andere nennt keine Version, und die Funktionsanfrage
ebenso wenig. Die Firmware-Version erklärt den Unterschied also nicht, und diese beiden
Beiträge sagen nicht, ob das Bett-Leveling oder die Werkzeug-Offset-Kalibrierung der
fehlschlagende Schritt war.

**Zwei Schritte, zwei Wiederholungen.** Gegen den Firmware-Quellcode gelesen,
widersprechen sich die Berichte nicht mehr: Sie beschreiben verschiedene Schritte.
Bekommt das Bett-Leveling keinen Messwert, parkt der Drucker den Kopf an seiner
Parkposition, die der Code innerhalb des Bereichs des Düsenreinigers verortet, fragt,
ob erneut versucht werden soll, und verlässt bei Ja den Reiniger und tastet erneut ab,
ohne dazwischen zu reinigen. Das sind die Funktionsanfrage und der Besitzer mit der
Beta. Scheitert die Werkzeug-Offset-Kalibrierung während eines Drucks, parkt der Drucker
den Kopf vorn bei abgesenktem Bett, wo die Düse erreichbar ist, und führt bei Retry die
Vorbereitung je Werkzeug erneut aus — aufheizen, spülen, abkühlen, abstreifen —, bevor
er abtastet. Nach einem gescheiterten XY-Scan betrifft das nur das fehlgeschlagene
Werkzeug; nach einer gescheiterten Z-Antastung beginnt die Wiederholung die Kalibrierung
wieder beim ersten Werkzeug, sodass jedes Werkzeug erneut spült. Das ist das erneute
Verschmutzen, das die beiden anderen Besitzer beschreiben, und es geschieht, ganz
gleich, wie gründlich die Düse gerade gereinigt wurde. Beide Pfade durchlaufen in 6.9.0,
der 6.9.1-Beta, der stabilen 6.9.1, 6.9.2, 7.0.0 und 7.0.1 dieselben Schritte (an der
Vorbereitung hat die Beta nur die Temperatur geändert, auf die sie abkühlt), weshalb die
Version die Berichte nicht trennte. Das gilt für Prusas eigene Builds; der Besitzer mit einem 6.9.1-Build
schrieb vor der stabilen Version und sagte nicht, welcher Build es war. Der Code für das
Bett-Leveling hat zwar einen Zweig, der abstreift und es erneut versucht, doch er gehört
zu einem Reinigungsdurchgang beim Abtasten, den der Standard-Start-G-Code des INDX nicht
aufruft.

In der Praxis: Ein gescheitertes Bett-Leveling reinigt die Düse nicht für Sie, und nach
einer gescheiterten Werkzeug-Offset-Kalibrierung folgt auf die Reinigung von Hand ein
erneutes Spülen. Ein
[Bericht an den Hersteller](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5505)
zur Beta bittet darum, dass die Wiederholung der Kalibrierung das Spülen auslässt und
nur wieder aufheizt und abstreift, da erneutes Spülen das Problem wieder einspeist. Ein
zweiter INDX-Besitzer reichte Ende Oktober unabhängig davon eine weitgehend gleiche
Anfrage ein ([#5577](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5577)):
Scheitert die Kalibrierung an einer verschmutzten Düse, soll der Drucker sie reinigen,
ohne etwas zu extrudieren, und es von selbst erneut versuchen, bevor er aufgibt; ein
Druck auf Retry von Hand, so seine Erfahrung, führt manchmal zum Erfolg. Beide
Anfragen sind offen und unbeantwortet, ebenso die Funktionsanfrage. Die obige
Darstellung der beiden Wiederholungen ist eine Lesart des Codes im Stand des Git-Tags
v6.9.1, nicht etwas, das ein Besitzer bestätigt hat, indem er beide Fehlschläge an einer
Maschine beobachtet hätte.

**8.0.0 wiederholt ein Werkzeug und spült es trotzdem.** Die Notes zu 8.0.0, die Prusa am
3. November auf GitHub gestellt hat und die ausführlicher sind als die Download-Seite,
sagen, dass eine Werkzeug-Offset-Kalibrierung, die an einem Werkzeug scheitert, jetzt nur
dieses Werkzeug wiederholt, mit eigenem Bildschirm und Fehlercode für jede Art von
Fehlschlag. Der Quellcode im Stand des Git-Tags v8.0.0 bestätigt die Wiederholung je
Werkzeug, nicht aber einen Bildschirm für jeden Fehlschlag: Eine gescheiterte Reinigung
und eine gescheiterte Z-Antastung teilen sich wie die meisten anderen Fehlschläge
weiterhin einen allgemeinen Bildschirm (siehe
[was die Standard-Firmware 8.0.0 zeigt](../codes.md#stock-800)). Er zeigt außerdem, was
die Wiederholung weiterhin tut. Bei Retry nimmt der Drucker das gescheiterte Werkzeug erneut
auf und führt dessen gesamte Messung von vorn aus, die Vorbereitung eingeschlossen; nur
dieses Werkzeug wird also noch einmal aufgeheizt, gespült, abgekühlt und abgestreift. Eine
gescheiterte Z-Antastung schickt die Kalibrierung nicht mehr zum ersten Werkzeug zurück.
Die Prüfungen, die erfolgen, sobald jedes Werkzeug vermessen ist, wie weit die Offsets
der Werkzeuge auseinanderliegen und wo der Sensor zu sitzen scheint, starten den ganzen
Durchgang weiterhin neu und spülen jedes Werkzeug erneut. Das Spülen, das diese Anfragen
streichen wollen, gibt es unter 8.0.0 also noch, für ein Werkzeug statt für alle; 7.0.0
und 7.0.1 wiederholen wie 6.9.2. Das Bett-Leveling tastet im Stand des Git-Tags v8.0.0
weiterhin ohne Reinigung erneut an. 7.0.0 hat ihm allerdings eine automatische
Wiederholung anderer Art hinzugefügt: Fällt das Netz zu uneben aus, führt der Drucker die Ausrichtung der Z-Achse selbst
aus, einmal, und wiederholt das Leveling; er fragt nur, wenn das scheitert. Auch auf diesem Pfad
wird die Düse nicht gereinigt. Bislang hat kein Besitzer berichtet, eine der beiden
Wiederholungen unter 8.0.0 beobachtet zu haben.

### Wenn nichts davon hilft

Um herauszufinden, ob Oozing überhaupt beteiligt ist, ließ ein Besitzer den Drucker mit
einem leeren Werkzeug abtasten, sodass nichts austreten konnte; die Abtastung schlug
genauso fehl, was Oozing für ihn ausschloss
([Thread](https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/bed-leveling-issues-3/)).
Die Ursache erwies sich als Montagefehler: Der Besitzer hatte die Bett-Abstandshalter
verwechselt und versehentlich den alten wieder eingebaut; sobald der richtige
Abstandshalter saß, funktionierte die Abtastung. Einzelbericht, doch der Test mit dem
leeren Werkzeug hat seinen Zweck erfüllt: Er schloss Oozing aus, und der Fehler war
mechanisch.

Wenn die Abtastung fehlschlägt, während die Düse offensichtlich nirgends in der Nähe
des Druckblechs ist — ein Abstand, den man sieht und nicht misst —, dann ist das ein
ganz anderer Fehler, und Oozing ist nicht Ihr Problem. Siehe
[Störeinflüsse auf die Wägezelle](loadcell-emi-noise.md). Wenn die
Werkzeug-Offset-Kalibrierung unabhängig von Sauberkeit und Filamentzustand
fehlschlägt, siehe [Ausfall der Offset-Sensorplatine](offset-sensor-board-failure.md).

## Überprüfung

`reported` (mehrfach berichtet) — das Symptom wird von verschiedenen Besitzern mit
unterschiedlichen Materialien unabhängig voneinander berichtet.

[PETG sickert und behindert die Bettabtastung](https://forum.prusa3d.com/forum/prusa-indx-how-do-i-print-this-printing-help/petg-oozing-and-impeding-bed-probing/)
ist der maßgebliche Thread: Der ursprüngliche Verfasser berichtet, dass PETG so stark
austritt, dass es die Bettabtastung verdirbt, und ein zweiter Besitzer berichtet
unabhängig davon von derselben Fehlerklasse mit PLA bei jedem Werkzeug während der
Kalibrierung. Der Thread ist als beantwortet markiert, und die angenommene Antwort ist
die Reinigung des Sensorfensters, aus erster Hand von der Person bestätigt, die das
Problem hatte. Das sind die stärksten Belege auf dieser Seite.

Aus einer einzigen Quelle und unbestätigt: Die Temperaturableitung über Werkzeug 1, der
Workaround mit dem deklarierten kühlen Filament, das Überschreiben per G-Code, die
Korrektur der Slicer-Konfiguration und die fest einprogrammierte Kalibriertemperatur
stammen sämtlich aus der
[Zusammenfassung häufiger Probleme](https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/a-summary-of-common-indx-problems/),
einer Verdichtung einer inzwischen offline genommenen Community-Wissensdatenbank.
Nichts davon ist im Forumsbestand gesondert bestätigt, und es werden hier keine Zahlen
daraus wiedergegeben. Die letzte Angabe ist inzwischen teilweise geprüft, und die
Prüfung schränkt sie ein. Ein Fehlerbericht auf GitHub stellt fest, dass sich die
Kalibriertemperatur mit 6.9.1 geändert hat, und bittet darum, sie einstellbar zu machen
([#5567](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5567)). Der
Firmware-Quellcode stützt eine gedeckelte Kalibriertemperatur, nicht eine, die sich per
G-Code nicht ändern lässt. Die
[Werkzeug-Offset-Kalibrierung](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/src/feature/tool_offset_calibration/tool_offset_calibration.cpp)
im Stand des Git-Tags v6.9.1 hält die Temperatur der Z-Abtastung auf oder unter einer
eigenen Obergrenze und die der XY-Abtastung fest, und der
[`G427`-Handler](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/src/marlin_stubs/G427.cpp)
liest nur seine Argumente für zufälligen Versatz und Wiederholungen, `R` und `P`, sodass
nichts eine der beiden anhebt. Unterhalb der Obergrenze folgt die Z-Abtastung aber dem
Vorheizwert des geladenen Filaments, und der
[`M865`-Handler](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/src/marlin_stubs/M865.cpp)
setzt diesen Wert und die Spültemperatur bei jedem benutzerdefinierten oder
Ad-hoc-Filament. Der Quellcode-Vergleich auf der Seite
[kommentiertes Profil](../gcode/indx-profile-gcode.md) stellt ebenfalls fest, dass
diese Temperatur in der Firmware gedeckelt ist. Keine der drei Dateien unterscheidet
sich zwischen den Git-Tags v6.9.1 und v6.9.2. Im Stand des
[Git-Tags v8.0.0](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/src/feature/tool_offset_calibration/tool_offset_calibration.cpp)
ermittelt die Kalibrierung ihre Temperaturen weiterhin auf dieselbe Weise, unter derselben
Obergrenze, und `G427` ist unverändert;
[`M865`](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/src/marlin_stubs/M865.cpp)
hat einen Parameter für die Farbe hinzubekommen, setzt Vorheiz- und Düsentemperatur
aber weiterhin nur bei einem Filament, das der Drucker als anpassbar behandelt. Seine
neuen Parameter für Kennungen bewirken auf einem INDX nichts: Die
[Build-Optionen](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/ProjectOptions.cmake)
schalten in diesem Stand die dafür nötige OpenPrintTag-Unterstützung nur in Builds mit
einem Werkzeug für den Core One und seine L-Variante ein. Die
Schaltfläche Customize, die ein geladenes Preset anpassbar macht, sitzt im
[Bildschirm mit den Filamentdetails](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/src/gui/screen/filament/screen_filament_detail.cpp)
und ist neu in 7.0.0; niemand hat berichtet, damit eine Kalibriertemperatur geändert zu
haben.

Das Verhalten bei Wiederholungen ist aus dem Firmware-Quellcode im Stand des Git-Tags v6.9.1 gelesen —
aus dem
[Befehl für das Bett-Leveling](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/lib/Marlin/Marlin/src/gcode/bedlevel/ubl/G29.cpp)
und der
[Werkzeug-Offset-Kalibrierung](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/src/feature/tool_offset_calibration/tool_offset_calibration.cpp)
—, und die Tags 6.9.0 und 6.9.1-Beta nehmen dieselben Wiederholungspfade. Die Beta hat
geändert, wie sie ablaufen, nicht welche Schritte sie umfassen: Die Vorbereitung je
Werkzeug kühlt weiter ab, der XY-Scan läuft kühler, und das Antasten auf der Sensorplatine
bekommt mehr Versuche, bevor es als gescheitert gilt (siehe
[Fehlercodes](../codes.md)). Es wird
festgehalten, weil es jeden Besitzerbericht in jenem Abschnitt erklärt, ohne einem davon
zu widersprechen, zeigt aber, was der Code tut, nicht was ein Besitzer beobachtet hat.
Keine der beiden Quelldateien (der Befehl für das Bett-Leveling und die
Werkzeug-Offset-Kalibrierung) unterscheidet sich zwischen den Git-Tags v6.9.1 und
[v6.9.2](https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.9.2), die
Lesart gilt also auch für 6.9.2. Prusa hat die Tags
[7.0.0](https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v7.0.0) und
[8.0.0](https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v8.0.0) am
3. November veröffentlicht. Im Stand von v7.0.0 unterscheidet sich der Befehl für das
Bett-Leveling von v6.9.2 nur im oben beschriebenen Pfad für ein unebenes Bett und die
Werkzeug-Offset-Kalibrierung nur in Code für Drucker ohne INDX und darin, dass sie die
Düse anhebt, wenn die Kalibrierung aufgibt; 7.0.0 wiederholt also wie 6.9.2.
[7.0.1](https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v7.0.1), deren
einzige Korrektur einem Hängenbleiben beim Start gilt, ändert keine der beiden Dateien. Im
Stand des Git-Tags v8.0.0 tastet der
[Befehl für das Bett-Leveling](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/lib/Marlin/Marlin/src/gcode/bedlevel/ubl/G29.cpp)
weiterhin ohne Reinigung erneut ab, und die
[Werkzeug-Offset-Kalibrierung](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/src/feature/tool_offset_calibration/tool_offset_calibration.cpp)
wiederholt nur das gescheiterte Werkzeug, Vorbereitung und Spülen eingeschlossen
([Commit](https://github.com/prusa3d/Prusa-Firmware-Buddy/commit/210606e66889cb636f93de34fcd6bf052367222f);
[Vergleich](https://github.com/prusa3d/Prusa-Firmware-Buddy/compare/v6.9.2...v8.0.0)). Wie
die frühere Lesart zeigt dies, was der Code tut, nicht was ein Besitzer beobachtet hat.

Wo die Quellen sich widersprechen: Das Trocknen wurde mit Nachdruck als wahrscheinliche
Ursache für PETG genannt, doch der Fall, der tatsächlich gelöst wurde, wurde durch
Reinigen gelöst, nicht durch Trocknen. Nehmen Sie Feuchtigkeit nicht allein deshalb an,
weil es sich um PETG handelt — als die Frage dem ursprünglichen Verfasser direkt
gestellt wurde, antwortete er, er habe unmittelbar aus einem Filamenttrockner gedruckt,
was Feuchtigkeit für diesen Fall vollständig ausschließt.

## Verwandte Themen

- [Abtastung schlägt fehl oder die Düse berührt das Bett nie](loadcell-emi-noise.md)
- [Werkzeug-Offset-Kalibrierung schlägt fehl](offset-sensor-board-failure.md)
- [Phantomwerkzeuge und Fehler beim Parken](tool-detection-ringdown-decay.md)
- [In den Druck geschleppte Klumpen](stringing-and-wiper-calibration.md) — dasselbe
  Problem von Material am falschen Ort, das jedoch bei Werkzeugwechseln auftritt und
  nicht während der Abtastung. Wenn Ihre Ablagerungen bei Werkzeugwechseln erscheinen,
  beginnen Sie dort.
