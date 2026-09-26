---
title:        Werkzeug-Offset-Kalibrierung schlägt fehl — kontaktloser Offset-Sensor
confidence:   reported
updated:      2026-09-25
author:       hyiger
printer:      Core One
toolhead:     INDX
hotend:       unknown
nozzle:       unknown
firmware:     6.9.0 for the calibration regression, addressed in 6.9.1-beta and carried into 6.9.1; the board fault is not version-specific
sources:
  - https://help.prusa3d.com/article/tool-offset-failed-36130-core-one-indx_1089016
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5442
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.9.1-beta
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.9.1
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/compare/v6.9.1-beta...v6.9.1
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5473
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/commit/df2b2eb4b2e9161ff3ae50a364d3e389b17684a3
  - https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/nozzle-cleaning-calibration-issues/
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/offset-sensor-failure/
  - https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/tool-offset-calibration-failing/
  - https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/a-summary-of-common-indx-problems/
superseded_by:
source_sha:   98e21f4e953356e4e92517c2f639006279f1549b8d1d89a5dfbb2714df642489
---
# Werkzeug-Offset-Kalibrierung schlägt fehl — kontaktloser Offset-Sensor

## Zusammenfassung

Wenn die Tool Offset Calibration wiederholt fehlschlägt und die Fehlermeldung nichts
Brauchbares mitteilt, liegt meistens eine defekte Platine des kontaktlosen
Offset-Sensors vor und kein Montagefehler. Reinigen Sie zuerst den Sensor, denn ein
Filamentkrümel darauf erzeugt genau denselben Fehler. Hilft die Reinigung nicht,
besteht die von mehreren Besitzern berichtete Lösung im Austausch der Sensorplatine —
und die Riemenspannung, die der Support unter Umständen vorschlägt, hat keinen
einzigen berichteten Fall behoben.

!!! important "Bevor Sie die Platine verdächtigen: Läuft bei Ihnen 6.9.0?"
    Ein inzwischen geschlossener [Fehlerbericht zur Firmware](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5442) beschreibt, dass die
    Werkzeug-Offset-Kalibrierung **nach dem Upgrade auf 6.9.0** wiederholt fehlschlägt,
    an Maschinen, an denen sie zuvor funktioniert hat. Es sind längst nicht mehr zwei
    Berichte: Der Bericht zog einen stetigen Zustrom von Besitzern an, an Vier- wie
    an Achtwerkzeug-Maschinen, darunter neu aufgebaute Gen-2-Geräte, die bei der
    Montage jede Kalibrierung bestanden haben. Betroffen sind mehrere Werkzeuge und
    nicht nur eines, und der Kalibrierassistent gelingt oft, während die Prüfung beim
    Druckstart weiterhin scheitert.

    Das ist hier von Belang, weil es sich fast identisch zu dem Hardwarefehler
    darstellt, um den es auf dieser Seite geht, die Abhilfe aber eine völlig andere
    ist. Wenn Ihre Kalibrierung vor einem Update einwandfrei lief und danach
    fehlzuschlagen begann, liegt eher dieser Fall vor als eine defekte Sensorplatine —
    und ein Hardwaretausch hilft dann nicht.

    **Der stärkste Beleg dafür, dass es die Firmware ist:** Mehrere Besitzer berichten,
    dass die Rückkehr zu 6.6.3 die Kalibrierung wieder zuverlässig macht und dass der
    Fehler mit 6.9.0 zurückkehrt.

    **Ein Downgrade steht aber nicht jeder Maschine offen.** Die Unterstützung für die
    neueren 1.5-GT-Riemen kam *mit* 6.9.0; ein damit ausgerüsteter Drucker hat also
    keine ältere Firmware, die ihre Geometrie kennt. Ein Besitzer im Thread konnte nur
    deshalb zurückgehen, weil er zuvor die ursprünglichen Riemen wieder eingebaut
    hatte. Sind Ihre die neuen, ist ein Downgrade nicht die Abhilfe — es tauscht einen
    Kalibrierfehler gegen eine Mechanik, die die Firmware nicht abbildet.

    **Ein Teil der Ursache ist durch die Behebung des Herstellers nun bestätigt.** Die
    Versionshinweise der Beta nennen zwei Änderungen, die genau auf diesen Fehler zielen:
    Die Werkzeug-Offset-Kalibrierung läuft bei niedrigerer Temperatur, und die
    Kommunikation zwischen Offset-Sensor und Hauptplatine wurde neu konfiguriert, um
    Aussetzer zu verhindern. Das Erste ist die Sicker-Erklärung, auf die sich die
    Besitzer geeinigt hatten — die Düse sickert, während sie für die Kalibrierung erwärmt
    wird, und die Ablagerung verdirbt die Messung, weshalb die Meldung auf dem Bildschirm
    dazu auffordert, die Düse auf Sauberkeit zu prüfen. Das Zweite hatte der Thread nicht
    erkannt. Die Sicker-Hälfte ist derselbe Mechanismus wie bei
    [Nachsickern beim Abtasten](oozing-during-probing-and-calibration.md), mit dem dort
    genannten Unterschied: Die Kalibriertemperatur ist in der Firmware fest hinterlegt,
    sodass die slicerseitigen Workarounds jener Seite sie nie erreichen konnten. Es
    brauchte eine Firmware-Änderung.

    **Eine Konfigurationsfalle, die zuerst auszuräumen ist.** 6.9.0 brachte
    Unterstützung für die neueren 1.5-GT-Riemen. Wenn Ihre Maschine sie nicht hat, muss
    diese Option ausgeschaltet sein — sie verändert die Geometrie spürbar. Mehrere
    Besitzer prüften das und fanden ihre Einstellungen bereits korrekt; es ist also
    nicht die ganze Erklärung, aber kostenlos auszuschließen.

    **Es gibt eine Behebung des Herstellers.** Nach Untersuchungen mit
    Hinweisen von Besitzern aus dem Bericht und interner Verfolgung des Fehlers
    veröffentlichte der Hersteller am 10. September 2026
    [6.9.1-beta](https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.9.1-beta)
    für die Core One INDX. Neben den Änderungen an Temperatur und Kommunikation erhöht
    sie die Zahl der Z-Antastversuche bei der Werkzeug-Offset-Kalibrierung von 3 auf 10
    und führt eine Behebung für die Wiederaufnahme der Offset-Messung auf. Die
    Kalibriertemperaturen selbst stehen in den Versionshinweisen und werden hier nicht
    wiederholt. Mehrere Besitzer im Bericht sagen, die Kalibrierung gelinge nun beim
    ersten Versuch, wo sie zuvor jedes Mal gescheitert war, und der Besitzer, der ihn
    eröffnet hat, sagt inzwischen, die Beta behebe es bei ihm und der Bericht könne
    geschlossen werden. Ein Prusa-Entwickler schloss ihn am 23. September 2026 mit der
    Begründung, dass die meisten Besitzer, die den ursprünglichen Fehler hatten, ihn
    offenbar los seien. Der abschließende Kommentar nennt keine Version und geht nicht auf
    den unten erwähnten Besitzer ein, der mit der Beta weiterhin gelegentliche
    Fehlschläge meldete; wer ein ähnliches Problem oder ein anderes Problem mit den
    Werkzeug-Offsets hat, soll einen neuen Bericht eröffnen und dabei auf diesen
    verweisen, falls er damit zusammenhängt. Die Temperatur beim Abtasten des Betts
    berührt die Behebung nicht; die stammt aus dem Slicer-Profil und nicht aus der
    Firmware — siehe
    [Nachsickern beim Abtasten](oozing-during-probing-and-calibration.md).

    **Sie ist jetzt in einer stabilen Version.** Der Hersteller veröffentlichte
    [6.9.1](https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.9.1) als
    stabile Version am 25. September 2026. Deren Versionshinweise nennen einen
    Assistenten zur Rechtwinkligkeit des Portals, Voreinstellungen für PVA und BVOH und
    eine Behebung beim Referenzieren und sagen nichts zur Werkzeug-Offset-Kalibrierung.
    Die Änderungen der Beta sind trotzdem enthalten: Im Firmware-Repository ist das Tag
    der stabilen Version das Beta-Tag plus
    [15 weitere Commits](https://github.com/prusa3d/Prusa-Firmware-Buddy/compare/v6.9.1-beta...v6.9.1),
    und keiner davon berührt den Code der Werkzeug-Offset-Kalibrierung oder des
    Offset-Sensors. Das stammt aus dem Repository, nicht aus den Versionshinweisen, und
    nichts in der stabilen Version wird als weitere Behebung dieses Fehlers beschrieben.

    Die Beta war nicht bei allen fehlerfrei, und die Hinweise zur stabilen Version
    erwähnen nichts vom Folgenden. Ein Besitzer stellt fest, dass die Kalibrierung
    zuverlässig gelingt, die Düsen aber merklich schmutziger herauskommen. Ein anderer
    berichtet von weiterhin auftretenden, wenn auch selteneren Fehlschlägen, und
    [ein dritter](https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/nozzle-cleaning-calibration-issues/)
    stellte fest, dass die Beta Filamentfäden an die Düse zog und das Z-Antasten scheitern
    ließ, und kam mit der Rückkehr besser zurecht — vermutet dahinter aber seine eigene
    Abstreifer-Einstellung. Keiner dieser Berichte ist über den jeweiligen Melder hinaus
    bestätigt. Ein mit der Beta gemeldeter Thermal Runaway wurde von seinem Melder
    zurückgezogen, der angab, ihn mit denselben Dateien auch unter der älteren Version
    reproduziert zu haben, und eher sein Modell als die Beta in Verdacht hatte.

    Für Besitzer mit den neueren Riemen löst die Behebung außerdem das oben beschriebene
    Dilemma: 6.9.1 ist INDX-Firmware, die die 1.5-GT-Unterstützung behält, sodass der
    Schritt nach vorn den Downgrade als Ausweg ersetzt, und seit der stabilen Version
    heißt das nicht mehr, eine Beta zu installieren. Die Firmware verweist auf einen
    offiziellen Hilfeartikel zu diesem Fehlercode, der ihn laut Besitzern nicht behoben
    hat.

!!! note "Ein Hinweis: Manche Ausfälle der Offset-Sensorplatine könnten eine Takteinstellung sein"
    `provisional` — ein einzelner Bericht, und sein Verfasser sagt, er sei noch nicht bewiesen.

    Ein Besitzer, bei dem der Sensorfehler beim ersten Messwert unter 6.6.3 wie unter
    6.9.0 auftrat, tauschte nahezu alles im Signalweg, ohne ihn zu beseitigen: zwei
    Offset-Sensorplatinen, mehrere Kabel, darunter eines außerhalb des Druckers verlegt,
    zwei Hauptplatinen, die Motoren, den Schlitten und das Netzteil. Beseitigt wurde er
    ganz ohne Hardware. Ein Firmware-Build, der den Teiler des Referenztakts am
    LDC1612-Chip des Offset-Sensors verdoppelte — womit die Referenzfrequenz von 40 MHz auf
    20 MHz sank —, brachte alle acht Werkzeuge beim ersten Versuch durch die Kalibrierung.

    Die Begründung lässt sich am Datenblatt des Chips prüfen, das die Referenzfrequenz im
    Einkanalbetrieb, den der INDX nutzt, auf 35 MHz begrenzt — unter dem, was die
    Standard-Firmware bis einschließlich 6.9.0 einstellte. Ist das die Ursache, würden
    Exemplare mit etwas weniger Reserve sporadisch ausfallen, während die meisten
    weiterlaufen; das würde auch
    erklären, warum eine Ersatzplatine denselben Fehler bei manchen Besitzern behebt, ohne
    dass der Fehler je weit verbreitet war.

    Behandeln Sie es als Hinweis, nicht als Behebung: eine Maschine, ein eigener Build,
    ein Ergebnis, das der Melder noch wiederholte, und eine Darstellung, die nach eigener
    Angabe mit einem KI-Assistenten verfasst wurde. Siehe
    [Firmware-Issue 5473](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5473).

    **Der Hersteller hat dieselbe Taktänderung vorgenommen.** Der Quellcode von
    6.9.1-beta, und damit die stabile 6.9.1, halbiert den Referenztakt des Sensors. Der
    [Commit](https://github.com/prusa3d/Prusa-Firmware-Buddy/commit/df2b2eb4b2e9161ff3ae50a364d3e389b17684a3)
    nennt als Grund die Einkanal-Grenze aus dem Datenblatt und ist auf einen Zeitpunkt
    vor der Eröffnung von Firmware-Issue 5473 datiert; 6.6.3 und 6.9.0 betrieben den
    Chip beide mit 40 MHz. Die
    Versionshinweise erwähnen die Änderung nicht, ob sie also das ist, was dort
    Kommunikationsbehebung heißt, ist nicht angegeben. Damit ist die Prämisse geklärt,
    nicht die Heilung: Noch kein Besitzer hat berichtet, ob die Standard-Firmware 6.9.1
    den Fehler beim ersten Messwert an einer Maschine beseitigt, die ihn hatte. Ein
    solcher Bericht würde den Takt auch nicht eindeutig als Ursache ausweisen. Der Build
    des Melders änderte nur den Referenzteiler, der Commit des Herstellers dagegen teilt
    zusätzlich den Eingangstakt des Sensors, betreibt die Spule mit einem festen,
    niedrigeren Strom bei abgeschalteter automatischer Amplitudenkorrektur und ändert,
    welche Amplituden- und Schwingungsabriss-Fehler gemeldet werden. Beseitigt die
    Standard-Firmware 6.9.1 den Fehler, kann jede dieser Änderungen der Grund sein. Wenn
    Ihre Platine unter 6.9.0 oder älter auf diese Weise ausfällt, kostet ein Update
    nichts und lohnt sich, bevor Sie sie austauschen.

## Fehlercodes, die hierher führen

| Code | Anzeige am Drucker |
|---|---|
| [`36130`](https://help.prusa3d.com/article/tool-offset-failed-36130-core-one-indx_1089016) | Tool offset failed |
| [`36136`](https://help.prusa3d.com/article/calibrate-dock-from-menu-17136-xl-36136-core-one-indx_1037195) | Calibrate dock from menu |
| [`36194`](../codes.md#36194) | The tool offset sensor sent no usable data |

`36130` behandelt diese Seite. Es ist auch der Code, zu dem die Firmware ihren eigenen
Hilfeartikel verlinkt — jenen Artikel, der dem Besitzer, der die 6.9.0-Regression
meldet, nach eigener Aussage nicht weitergeholfen hat.

`36194` gibt es nur in Firmware, die aus hyiger/Prusa-Firmware-Buddy gebaut ist; sie
meldet diesen Fehler mit einem eigenen Code, wenn keine Abtastfahrt brauchbare Daten
vom Sensor erhalten hat. Mit der Standard-Firmware ist derselbe Fehler `36130`; unter
[Fehlercodes](../codes.md#stock-firmware) steht, wie man ihn im seriellen Log erkennt.

## Details

An der Einrichtung eines INDX sind zwei verschiedene Sensoren beteiligt, und zu wissen,
welcher von beiden ausgefallen ist, erspart sehr viel vergebliche Mühe. Die Wägezelle
erfasst den Z-Kontakt mit dem Druckbett. Für die Werkzeug-Offsets ist ein separater
kontaktloser Induktivsensor auf einer eigenen kleinen Platine zuständig. Bei diesem
Fehlerbild läuft das Z-Probing über die Wägezelle einwandfrei durch; es ist der
kontaktlose Sensor, der überhaupt keine Messwerte liefert, sodass der Kalibrierung die
Grundlage fehlt.

Das Firmware-Log trägt einen charakteristischen Fingerabdruck — einen Fehler, der die
kontaktlose Offset-Routine benennt, zusammen mit einem fehlgeschlagenen Abgriff eines
ersten Sensormesswerts. Diese Logzeile ist das Nützlichste, was Sie festhalten können,
denn die Meldung auf dem Display ist generisch und der dort angezeigte Hinweis, die
Düse zu reinigen, führt in die Irre.

Was diesen Fehler verwirrend macht:

- **Die Werkzeugnummer, bei der es fehlschlägt, ist nicht aussagekräftig.** Manche
  Besitzer berichten von einem Fehlschlag beim ersten Werkzeug, andere kommen mehrere
  Werkzeuge weit, bevor es fehlschlägt, wobei die Abbruchstelle zwischen den Versuchen
  wandert, ohne dass zwischendurch etwas geändert wurde. Unterschiedliche
  Abbruchstellen bedeuten nicht unterschiedliche Probleme.
- **Werkzeuge untereinander zu tauschen hilft nicht**, und erneutes Einsetzen der
  Werkzeuge ebenso wenig. Mehrere Besitzer haben Permutationen durchprobiert, bevor sie
  auf den Sensor als Ursache schlossen.
- **Die Riemenspannung ist hier eine falsche Fährte.** Sie ist eine naheliegende erste
  Vermutung und wurde vom Support vorgeschlagen, doch Besitzer, die das Portal gründlich
  ausgerichtet und die Riemen neu gespannt haben, berichten von keiner Änderung.
  Verbringen Sie damit keine Nacht, bevor Sie ein Log aufgezeichnet haben.
- **Ein bestandener Durchgangstest des Kabels entlastet den Sensor nicht.** Ein Besitzer
  prüfte das Kabel, fand es elektrisch einwandfrei — und die Platine war dennoch die
  Ursache. Ein bloßer Kabeltausch hat in den berichteten Fällen nichts behoben.

### Vorgehen, der Reihe nach

1. **Reinigen Sie den Sensor selbst**, nicht nur die Düse. Ein kleiner Filamentrückstand
   auf der Sensorfläche verursacht ein identisches Fehlerbild, und dies ist die eine
   Ursache, die Sie in einer Minute selbst beheben können.
2. **Zeichnen Sie über die serielle USB-C-Verbindung ein Firmware-Log auf** und bewahren
   Sie es auf. Das ist der Nachweis, der einen Supportfall schnell zum Abschluss bringt
   — mindestens ein Besitzer berichtet, dass der Hersteller die Platine ausdrücklich auf
   Grundlage eingereichter Logs als defekt bestätigt hat. TODO(verify): die
   einzustellende serielle Baudrate. Sie steht im Summary-Thread, aber ein Leser wird
   sie in ein Terminal eintippen, daher muss sie zuerst geprüft werden.
3. **Prüfen Sie die LED auf der Sensorplatine.** Wenn sie weiterhin schnell blinkt,
   nachdem eine Kalibrierung bereits fehlgeschlagen ist, deutet das auf die Platine
   selbst hin — das schnelle Muster soll nur erscheinen, während der Mikrocontroller des
   Sensors geflasht wird. Es außerhalb eines Firmware-Updates zu sehen, ist ein
   deutliches Signal.
4. **Eröffnen Sie einen Supportfall.** Der berichtete Weg ist zuerst die Diagnose bei
   Prusa und danach ein Bondtech-Ticket für die Ersatzplatine, das die Befunde von Prusa
   mitführt. Ein Ticket, das bereits benennt, was Prusa festgestellt hat, kommt schneller
   voran als eines, das bei den Symptomen beginnt. Eröffnen Sie ihn früh, auch wenn Sie
   noch nicht handeln wollen, damit das Datum aktenkundig ist — siehe
   [wen Sie kontaktieren](support-and-warranty-path.md).

Der Sensor arbeitet mit Wirbelströmen, was aus zwei Gründen wissenswert ist: Es ist der
Grund, weshalb eine nichtleitende Düsenspitze für künftige Düsenvarianten eine
konstruktive Einschränkung darstellt, und es ist der Grund, weshalb Verschmutzung der
Sensoroberfläche so stark ins Gewicht fällt.

Ein in der Zusammenfassung berichteter Vergleich zweier Platinen ergab, dass ein
defektes und ein funktionierendes Exemplar dieselbe Hardware-Revision aus derselben
Produktionscharge waren; es sieht also nach Streuung auf Exemplarebene aus und nicht
nach einer schlechten Charge, die sich anhand einer Seriennummer erkennen ließe.

!!! warning "Ein Vorschlag aus den Threads ist keine Reparatur"
    Ein Besitzer brachte ins Gespräch, die Sensorplatine im Reflow-Ofen nachzuarbeiten.
    Es gibt keinen Bericht darüber, dass das jemand erfolgreich getan hätte, und es
    würde jeden Garantieanspruch auf das Teil mit ziemlicher Sicherheit beenden. Lassen
    Sie die Platine austauschen.

## Verifizierung

`reported` (mehrfach berichtet) — zwei unabhängige Threads, zwei verschiedene Besitzer,
beide endend beim Austausch der Platine.

[Ausfall des Offset-Sensors](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/offset-sensor-failure/)
dokumentiert eine Kalibrierung, die beim ersten Werkzeug fehlschlägt, und legt den
Support-Weg fest, auf den sich die Besitzer verständigt haben.
[Werkzeug-Offset-Kalibrierung schlägt fehl](https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/tool-offset-calibration-failing/)
stammt von einem anderen Besitzer mit einem anders aussehenden Erscheinungsbild —
Fehlschlag mitten in der Werkzeugfolge, sporadisch —, der Riemenspannung und
Werkzeugtausch ohne Verbesserung durchprobierte, den Kabeldurchgang als einwandfrei
nachwies und berichtet, dass der Hersteller nach Durchsicht eingereichter Logs die
Platine als Ursache bestätigte. Dass zwei unähnliche Symptommuster auf dasselbe Bauteil
hinauslaufen, ist das Nützlichste auf dieser Seite.

Der Log-Fingerabdruck, die LED-Diagnose, der Wirbelstrom-Mechanismus und der Vergleich
innerhalb derselben Charge stammen aus der
[Zusammenfassung häufiger Probleme](https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/a-summary-of-common-indx-problems/),
einer Verdichtung einer inzwischen offline genommenen Community-Wissensdatenbank. Diese
Einzelheiten haben nur eine Quelle und wurden im Forumsbestand nicht gesondert bestätigt.

Wo die Quellen sich widersprechen: Die ersten Vorschläge des Supports schwankten zwischen
Kabel und Platine, und in einem Fall wurde die Riemenspannung angeführt. Die Erfahrung
der Besitzer weist durchgängig auf die Platine.

**Seit der Erstveröffentlichung ergänzt.** Die Kalibrierungsregression unter 6.9.0 stammt
aus dem [Firmware-Issue-Tracker](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5442),
der für Firmware-Verhalten eine stärkere Quellenklasse ist als das Forum — er ist
herstellereigen, versioniert und reproduzierbar. Aus zwei Berichten ist ein langer Thread
unabhängiger Melder an beiden Maschinengrößen geworden, von denen mehrere das Problem
durch ein Downgrade gelöst haben. Dieser wechselseitige Test — scheitert unter 6.9.0,
funktioniert unter 6.6.3, scheitert erneut unter 6.9.0 — ist es, was die Regression selbst
gut belegt macht.

Die *Ursache* ist nun teilweise geklärt. Wo diese Seite zuvor nur die Annäherung der
Besitzer an die Sicker-Erklärung hatte, nennen die Versionshinweise der Beta eine
niedrigere Kalibriertemperatur und eine Behebung von Kommunikationsaussetzern des
Offset-Sensors, und der Entwickler im Bericht sagte, beides habe eine Rolle gespielt.
Das ist der Hersteller, der beitragende Ursachen benennt, keine veröffentlichte
Ursachenanalyse. Die Behebung ist inzwischen keine Beta mehr. Der Bericht wurde am 23.
September 2026 aufgrund der Rückmeldungen von Besitzern zur Beta geschlossen, und die
stabile 6.9.1 enthält denselben Code, was die Release-Tags zeigen und die
Versionshinweise nicht sagen. Damit ist sie die veröffentlichte Behebung des
Herstellers, keine nachgewiesene Heilung: Ein Besitzer im Bericht sah mit der Beta
weiterhin gelegentliche Fehlschläge, und zur stabilen Version hat noch kein Besitzer
berichtet.

Der Hinweis auf die Referenzfrequenz des LDC1612 ist ein separater Einzelbericht eines
anderen Besitzers und ist dort, wo er erscheint, als `provisional` markiert. Der eigene
Commit des Herstellers bestätigt, dass der Takt über der Grenze des Chips lag, und
ändert ihn zusammen mit mehreren anderen Sensoreinstellungen, sagt aber nichts darüber,
ob das die Fehlschläge dieses Besitzers verursacht hat.

## Verwandte Seiten

- [Bett in Z nicht ausgerichtet](tool-offset-bed-z-alignment.md) — derselbe Fehlercode
  an einer sauberen Maschine ohne geladenes Filament; eine kostenlose Kalibrierung, die
  vor dem Verdacht auf die Platine auszuführen ist
- [Probing schlägt fehl oder die Düse berührt das Bett nie](loadcell-emi-noise.md) — der
  andere Sensor, häufig mit diesem verwechselt
- [Montagehinweise](../reference/assembly-notes.md) — wenn dies an einer frisch
  aufgebauten Maschine fehlschlägt, die noch nie erfolgreich kalibriert hat, prüfen Sie
  zuerst den Aufbau: Dies ist einer der beiden Selbsttest-Fehler, die bei Neuumbauten
  immer wieder auftreten
- [Wen Sie kontaktieren](support-and-warranty-path.md) — so kommen Sie an das Ersatzteil:
  Diagnose von Prusa, Hardware von Bondtech, und eröffnen Sie den Fall früh genug, dass
  das Datum in Ihren Garantiezeitraum fällt.
