---
title:        Werkzeug-Offset-Kalibrierung schlägt fehl — kontaktloser Offset-Sensor
confidence:   reported
updated:      2026-11-08
author:       hyiger
printer:      Core One
toolhead:     INDX
hotend:       unknown
nozzle:       unknown
firmware:     6.9.0 for the calibration regression, addressed in 6.9.1-beta and carried into 6.9.1, 6.9.2, 7.0.0, 7.0.1 and 8.0.0 (source-checked); first owner reports on 7.0.0; the 7.0.0 startup hang fixed in 7.0.1 and 8.0.0; no reports yet on 8.0.0; the board fault is not version-specific
sources:
  - https://help.prusa3d.com/article/tool-offset-failed-36130-core-one-indx_1089016
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5442
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.9.1-beta
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.9.1
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/compare/v6.9.1-beta...v6.9.1
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.9.2
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/compare/v6.9.1...v6.9.2
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5473
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/commit/df2b2eb4b2e9161ff3ae50a364d3e389b17684a3
  - https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/nozzle-cleaning-calibration-issues/
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/offset-sensor-failure/
  - https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/tool-offset-calibration-failing/
  - https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/a-summary-of-common-indx-problems/
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5500
  - https://forum.prusa3d.com/forum/ceske-forum-obecna-diskuze-oznameni-a-novinky/core-one-indx-tool-offset-out-of-bounds-36130-loadcell-test-issue/
  - https://help.prusa3d.com/downloads/core-one-indx
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5548
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5526
  - https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/indx-firmware-7-0-0-stuck-on-reset/
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5544
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5567
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5518
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v7.0.0
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v7.0.1
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v8.0.0
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/compare/v6.9.2...v7.0.0
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/compare/v7.0.0...v7.0.1
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/compare/v7.0.0...v8.0.0
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/src/puppy/tool_offset_sensor/src/main.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/commit/852dedffe929cf95ea5031c9e8a8e234f1536d9d
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/commit/ebe27870c752655f48de9af57bc28e6f337c0e3d
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5585
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/lib/Prusa-Error-Codes/yaml/buddy-error-codes.yaml
superseded_by:
source_sha:   e644d4389673bd5f9fe1bbf077dddea82028bc3fc561d004c080b53610a3a389
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
    Assistenten zur Rechtwinkligkeit des Portals und eine Behebung beim Referenzieren
    und sagen nichts zur Werkzeug-Offset-Kalibrierung.
    Die Änderungen der Beta sind trotzdem enthalten: Im Firmware-Repository ist das Tag
    der stabilen Version das Beta-Tag plus
    [15 weitere Commits](https://github.com/prusa3d/Prusa-Firmware-Buddy/compare/v6.9.1-beta...v6.9.1),
    und keiner davon berührt den Code der Werkzeug-Offset-Kalibrierung oder des
    Offset-Sensors. Das stammt aus dem Repository, nicht aus den Versionshinweisen, und
    nichts in der stabilen Version wird als weitere Behebung dieses Fehlers beschrieben.
    [6.9.2](https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.9.2),
    erschienen am 7. Oktober 2026, enthält denselben Code. Am INDX
    [ändert sie nichts](https://github.com/prusa3d/Prusa-Firmware-Buddy/compare/v6.9.1...v6.9.2)
    außer den Filament-Presets für PVA und BVOH, die in den Versionshinweisen zu 6.9.1
    angekündigt waren, in jener Version selbst aber fehlten.
    [7.0.0](https://help.prusa3d.com/downloads/core-one-indx), am 15. Oktober 2026 auf
    Prusas Download-Seite veröffentlicht, sagt in ihren Versionshinweisen nichts zur
    Werkzeug-Offset-Kalibrierung oder zum Offset-Sensor. Prusa veröffentlichte ihren
    Quellcode am 3. November 2026 auf GitHub, zusammen mit dem von 7.0.1 und 8.0.0, und
    [er behält die Änderungen von 6.9.1 bei](https://github.com/prusa3d/Prusa-Firmware-Buddy/compare/v6.9.2...v7.0.0):
    Die Takt- und Spuleneinstellungen des Sensorchips und die Art, wie die Kalibrierung
    ihre Temperaturen wählt, sind dieselben wie in 6.9.2. Was 7.0.0 auf der Sensorseite
    ändert, ist, wie die eigene Firmware der Sensorplatine den Chip ausliest, siehe den
    Hinweis weiter unten. Die Hinweise führen eine verbesserte Reinigung durch
    den Düsenabstreifer auf, gekennzeichnet als erstmals mit 6.10.1 ausgeliefert; der
    einzige Bericht seither, der das, was die Reinigung an den Düsen des INDX
    zurücklässt, mit fehlschlagenden Kalibrierungen in Verbindung bringt, fasst 7.0.0
    und 6.9.2 zusammen, beide deutlich schlechter als 6.9.0, ohne die beiden zu
    vergleichen oder die geänderte Reinigung zu erwähnen, siehe unten. Laut Quellcode
    erreicht dieser Punkt den INDX nicht: Nozzle Wiper heißt in der Firmware der leichtere
    Abstreifer von Druckern ohne INDX, sein Code wird für den INDX nicht gebaut, und die
    eigenen Reinigungsabläufe des INDX sind dieselben wie in 6.9.2, siehe
    [In den Druck geschleppte Blobs](stringing-and-wiper-calibration.md).
    [7.0.1](https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v7.0.1),
    veröffentlicht auf Prusas Download-Seite am 19. Oktober 2026, führt eine einzige
    Behebung auf, für das weiter
    unten auf dieser Seite beschriebene Hängenbleiben beim Start, und
    [ihr Quellcode](https://github.com/prusa3d/Prusa-Firmware-Buddy/compare/v7.0.0...v7.0.1)
    unterscheidet sich von 7.0.0 allein durch diese Behebung.
    [8.0.0](https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v8.0.0),
    veröffentlicht auf Prusas Download-Seite am 22. Oktober 2026, ist die erste Version
    seit der Beta, deren
    Hinweise diese Kalibrierung am INDX erwähnen. Ihre ausführlichen Hinweise auf GitHub,
    die mehr sagen als die Download-Seite, nennen zwei Änderungen: Scheitert ein
    Werkzeug, wiederholt die Kalibrierung dieses Werkzeug, statt von vorn zu beginnen,
    und jede Art von Fehlschlag hat einen eigenen Bildschirm, der das Werkzeug nennt und
    einen Fehlercode angibt. Der Quellcode bestätigt das Erste, aber nicht als Änderung
    für den Fehler auf dieser Seite: Von 6.9.0 bis 7.0.1 hat Retry nach einer
    gescheiterten Messung über dem Sensor dieses Werkzeug bereits für sich allein erneut
    gemessen. Was 8.0.0 auf ein Werkzeug beschränkt, ist Retry nach den übrigen
    Fehlschlägen in den Schritten eines Werkzeugs, etwa einer Reinigung, die nicht zu Ende
    lief, oder einer verworfenen Berührung der Druckplatte beim Druckstart; dort begann
    Retry den Durchlauf bisher ab dem ersten Werkzeug neu. Retry nach den Prüfungen, die
    am Ende die Werkzeuge miteinander vergleichen, tut das weiterhin. Das Zweite trifft
    nur zum Teil zu: Mehrere Arten von Fehlschlag teilen sich einen Bildschirm, und die
    Bildschirme Sensor Not Found und Sensor Failure nennen kein Werkzeug. Welcher
    Fehlschlag welchen Code erhält, steht unter [Fehlercodes](../codes.md#stock-800). Im
    [Quellcode](https://github.com/prusa3d/Prusa-Firmware-Buddy/compare/v7.0.0...v8.0.0)
    sind die Chipeinstellungen, die Firmware der Sensorplatine und die Temperaturwahl
    dieselben wie in 7.0.0. Eine weitere Änderung dort steht nicht in den Hinweisen: Die
    Abtastfahrten über den Sensor werden jetzt genauso ausgeführt wie gewöhnliche
    Bewegungen, folgen also dem Bettnetz und beginnen zu einem bekannten Zeitpunkt, was
    laut
    [ihrem Commit](https://github.com/prusa3d/Prusa-Firmware-Buddy/commit/ebe27870c752655f48de9af57bc28e6f337c0e3d)
    einen kleinen zeitlichen Versatz aus Messungen entfernt, die an der Bewegung
    ausgerichtet sind. Das ist eine Lesart des Codes, kein beobachtetes Ergebnis, und zur
    Kalibrierung unter 8.0.0 hat noch kein Besitzer berichtet. Zur Düsenreinigung nennen
    die Hinweise zwei Punkte: Der Extruder bewegt flexible Filamente beim Reinigen
    schneller als bisher, und die Kalibrierung des Düsenreinigers am INDX ist genauer. Was
    der zweite Punkt ändert, hat diese Seite nicht geprüft.

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

    **Auch die stabile Version läuft laut dem ersten Bericht nicht fehlerfrei.** Ein
    Besitzer einer Maschine mit acht Werkzeugen meldet in
    [Firmware-Issue 5500](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5500),
    dass die Kalibrierung beim Druckstart unter 6.9.1 bei Drucken mit mehreren
    Werkzeugen weiterhin oft fehlschlägt, so oft, dass jedem solchen Druck langes
    Reinigen der Düsen von Hand vorausgeht. Er führt das auf Material zurück, das das
    Spülen an den Düsen hinterlässt; nach seiner Aussage ist es unter 6.9.0 wie unter
    6.9.1 zu viel, und es haftet nach dem Abstreifen oft noch an der Düse. Das ist Material an der
    Spitze, die Ursache, die die Meldung auf dem Bildschirm nennt; über die
    Sensoraussetzer oder eine defekte Platine sagt es nichts. Er meldet außerdem, dass
    der Fehlerbildschirm das falsche Werkzeug zum Reinigen präsentiert, siehe
    [Fehlercodes](../codes.md). Zwei weitere Besitzer haben dem Issue inzwischen
    hinzugefügt, dass sie dasselbe sehen, einer an einer Gen-2-Maschine mit vier
    Werkzeugen und einer, für den ASA, das stärker haftet, kaum noch druckbar ist,
    beide ohne weitere Angaben. Das Issue ist offen, ohne Antwort des Herstellers.

    **Ein Besitzer sagt, die niedrigere Temperatur mache es mit PETG schlimmer.**
    `provisional`, ein einzelner Bericht. An einer Gen-2-Maschine meldet er in
    [Firmware-Issue 5567](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5567),
    dass nach Abschluss der Reinigung, kurz vor dem Abtasten, noch PETG an der Düse
    haftet und das einen zu hohen Z-Offset und fehlschlagendes Abtasten ergibt. Unter
    6.9.0 kam das gelegentlich vor; unter 6.9.2 und 7.0.0 findet er es deutlich
    häufiger, und die Rückkehr zu 6.9.0 hilft spürbar, ohne es zu beseitigen. Er führt
    das auf die niedrigere Kalibriertemperatur zurück, die mit 6.9.1 kam: Bei dieser
    Temperatur ist an der Spitze verbliebenes PETG hart geworden und verfälscht die
    Messung deshalb stärker. Er ergänzt, dass der Standard-Start-G-Code diese
    Kalibrierung vor der eigenen Düsenreinigung des Drucks ausführt, und schlägt vor,
    zuerst zu reinigen. Die Kalibrierung reinigt jedes Werkzeug vor dem Messen weiterhin
    selbst; gewünscht ist also eine zusätzliche Reinigung davor. Falls er recht hat,
    wirkt bei einem klebrigen Material die niedrigere Temperatur, also die gegen das
    Nachsickern gerichtete Hälfte der Behebung des Herstellers, ihrem eigenen Zweck
    entgegen. Geprüft hat das niemand, und der Hersteller hat nicht geantwortet. Auch
    hier ist es Material an der Spitze, nicht die Platine.

    **Die ersten Berichte zu 7.0.0 weisen nicht auf die Platine.** Jeder ist ein
    Einzelbericht. Ein Besitzer im
    [Thread zur Werkzeug-Offset-Kalibrierung](https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/tool-offset-calibration-failing/),
    der mit der Beta und der stabilen Version von 6.9.1 keine Fehlschläge hatte, sah die
    Kalibrierung beim ersten Druck nach dem Update scheitern und beim ersten erneuten
    Versuch gelingen; er war nicht am Drucker, als es fehlschlug. Ein anderer, mit einer
    Gen-2-Maschine mit acht Werkzeugen, meldet in
    [Firmware-Issue 5548](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5548),
    dass Drucke mit mehreren Werkzeugen unter 7.0.0 oft schon beim Start mit 36130
    anhalten. Sein Log verortet das bei der Berührung auf der Sensorplatine, noch vor
    jeder Abtastfahrt über den Sensor, also bei einer Messung der Wägezelle, und er
    vermutet Störungen an der Wägezelle, die nach seinen Messungen zunehmen, wenn der
    Extrudermotor bestromt ist. Später berichtet er, dass das Abschalten des
    Extrudertreibers vor dem Abtasten die Fehler an seinem Drucker selten gemacht hat,
    eine Umgehung, keine Behebung. Sein späteres Setup schaltet zusätzlich die
    Statusleuchte am Bett aus, was er in
    [Firmware-Issue 5518](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5518)
    als bisher sehr zuverlässig beschreibt; dieses Ergebnis trennt Motor und Leuchte
    nicht. Ein zweiter Besitzer in Firmware-Issue 5548, mit einer Maschine mit acht
    Werkzeugen, an der bisher keine Firmware die Kalibrierung zuverlässig gemacht hat,
    schaltete nur den Extrudertreiber ab, und das Abtasten gelang nach mehreren
    Fehlschlägen beim ersten Versuch; das ist ein einziger Versuch, und seine Firmware
    nennt er nicht. Siehe
    [Fehlercodes](../codes.md#36193) und [Wägezellen-Störungen](loadcell-emi-noise.md).

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
    Das Ergebnis dieser Wiederholung hat der Melder nicht nachgereicht; die einzige
    Antwort im Issue ist ein automatischer Hinweis, der es als veraltet markiert.

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

    **7.0.0 und 8.0.0 behalten diese Einstellungen bei und ändern die Fehlerbehandlung
    darum herum.** Die Sensorplatine hat eine eigene Firmware, die in die
    Drucker-Firmware eingebaut ist und von ihr aus auf die Platine geflasht wird. In
    7.0.0 und 8.0.0 richtet
    [diese Firmware](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/src/puppy/tool_offset_sensor/src/main.cpp)
    den Chip genau so ein wie 6.9.1; die Taktänderung bleibt also bestehen. Was
    [7.0.0 neu schreibt](https://github.com/prusa3d/Prusa-Firmware-Buddy/compare/v6.9.2...v7.0.0),
    ist ihre Leseschleife. Sie prüft jetzt die Fehlerflags des Chips, bevor sie einen
    Messwert übernimmt, wertet einen Lesevorgang als gescheitert, wenn nicht jeder
    genutzte Kanal einen Wert geliefert hat, und schaltet den Chip ab, wenn seine
    Einrichtung fehlschlägt. Wie bisher setzt sich die Platine nach mehreren
    fehlgeschlagenen Lesevorgängen in Folge selbst zurück. 8.0.0 enthält dieselbe
    Platinen-Firmware. Das ist die Behandlung rund um den Fehler beim ersten Messwert,
    nicht seine Ursache, und der Code allein zeigt nicht, was sie an einer Platine
    ändert, die auf diese Weise ausfällt. Berichtet hat das auch noch kein Besitzer.

## Fehlercodes, die hierher führen

| Code | Anzeige am Drucker |
|---|---|
| [`36130`](https://help.prusa3d.com/article/tool-offset-failed-36130-core-one-indx_1089016) | Tool offset failed |
| [`36136`](https://help.prusa3d.com/article/calibrate-dock-from-menu-17136-xl-36136-core-one-indx_1037195) | Calibrate dock from menu |
| [`36145`](../codes.md#stock-800) | Sensor Failure (Standard-Firmware 8.0.0) |
| [`36194`](../codes.md#36194) | The tool offset sensor sent no usable data |

`36130` behandelt diese Seite. Es ist auch der Code, zu dem die Firmware ihren eigenen
Hilfeartikel verlinkt — jenen Artikel, der dem Besitzer, der die 6.9.0-Regression
meldet, nach eigener Aussage nicht weitergeholfen hat.

`36194` gibt es nur in Firmware, die aus hyiger/Prusa-Firmware-Buddy gebaut ist; sie
meldet diesen Fehler mit einem eigenen Code, wenn keine Abtastfahrt brauchbare Daten
vom Sensor erhalten hat. Mit der Standard-Firmware bis 7.0.1 ist derselbe Fehler
`36130`; unter [Fehlercodes](../codes.md#stock-firmware) steht, wie man ihn im seriellen
Log erkennt. Die Standard-Firmware 8.0.0 zeigt `36145`, wenn die Abtastfahrten
aufgegeben wurden, nachdem mindestens eine an einem vom Sensor gemeldeten Fehler oder
an Messwerten gescheitert war, die die Hauptplatine nicht erreichten, oder wenn die
Kopfplatine während der Abtastfahrten neu gestartet ist, und weiterhin `36130`, wenn der
Sensor gar nichts gesendet hat, siehe
[was die Standard-Firmware 8.0.0 anzeigt](../codes.md#stock-800).
Das ist eine Lesart des Quellcodes; noch kein Besitzer hat einen der beiden Bildschirme
gemeldet.

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
- **Nicht jeder Hardwarefall endet bei der Sensorplatine.** `provisional`, ein
  einzelner Bericht.
  [Ein Besitzer](https://forum.prusa3d.com/forum/ceske-forum-obecna-diskuze-oznameni-a-novinky/core-one-indx-tool-offset-out-of-bounds-36130-loadcell-test-issue/)
  hatte unter 6.6.0 und 6.6.1 bei jedem Start eines Drucks 36130, obwohl die
  Kalibrierung selbst durchlaufen konnte, und sein Wägezellentest zeigte instabile
  Werte, registrierte nach dem Wegklicken der Warnung aber weiterhin einen Druck auf die
  Düse. Riemenspannung und wiederholte Kalibrierung halfen nicht. Der Fehler lag
  schließlich in dem Teil, das er Werkzeughalter nennt; er reklamierte es beim
  Hersteller, und seitdem funktioniert alles. Welches Teil das ist, sagt der Beitrag
  nicht. Dieselbe Aufteilung, bei der die Kalibrierung gelingt und der Druckstart
  scheitert, ist oben als Zeichen der 6.9.0-Regression genannt; hier trat sie vor
  dieser Version auf und war Hardware.
- **Gelingt sie aus dem Menü und scheitert beim Druckstart, passt das auch zu
  Wägezellen-Störungen.** `provisional`, Besitzer in einem Forenthread und in einem
  Issue, die meist mehreres zugleich geändert haben. Besitzer im
  [Thread zur Werkzeug-Offset-Kalibrierung](https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/tool-offset-calibration-failing/)
  beseitigten Fehlschläge beim Druckstart, indem sie Versorgungs- und Heizleitungen neu
  verlegten und verdrillten und Ferritkerne anbrachten. Einer von ihnen hatte auf
  Standard-Firmware 6.9.2 nach der Neuverdrahtung noch vereinzelte Fehlschläge. Er las
  [Firmware-Issue 5526](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5526),
  dessen Ersteller die Statusleuchte am Bett verantwortlich macht, gestützt auf Tests
  mit einer selbst veränderten Firmware, schaltete die Leuchte im Menü aus und hatte
  danach keine Fehlschläge mehr. Anschließend brachte er zusätzlich Ferritperlen an den
  Kabeln der Bett- und der Kammerbeleuchtung an, und seine neueste Zusammenfassung in
  [Firmware-Issue 5518](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5518)
  führt seine vollständige Behebung auf die Neuverdrahtung, diese Perlen und eine
  niedrigere Abtasttemperatur im Start-G-Code zurück. Das Ausschalten der Leuchte steht
  nicht auf dieser Liste, obwohl er das Kabel der Bettbeleuchtung für die
  wahrscheinlichste Quelle hält; sein Ergebnis zeigt also nicht, dass das Ausschalten
  nötig ist. Ein weiterer
  Besitzer im Thread schaltete die Leuchten aus und brachte zugleich Ferritperlen an,
  und auch seine Fehlschläge hörten auf. Noch ein Besitzer stellte in Firmware-Issue
  5526 fest, dass Ferritperlen nicht halfen und das Ausschalten der Leuchte bisher
  anscheinend jedes Mal hilft; seine Firmware nennt er nicht. Zwei weitere Besitzer im
  Thread haben seither die Leuchte ausgeschaltet, einer nennt dabei die
  Bettbeleuchtung, und keiner erwähnt eine weitere Änderung zur selben Zeit. Bei
  einem liefen Werkzeug-Offset-Kalibrierung und Bettnivellierung danach zum ersten Mal,
  ohne sich in die Länge zu ziehen oder zu scheitern. Beim anderen, dessen Bettnivellierung immer
  wieder neu ansetzte und scheiterte, verlief die Nivellierung bei einem Druck sauber.
  Keiner der beiden
  nennt seine Firmware. Zusammen mit dem Besitzer in Issue 5526 macht das das
  Ausschalten der Leuchte, ohne dass daneben eine weitere Änderung berichtet wird, zu
  `reported`, aus zwei Quellen, als etwas,
  das geholfen hat; warum es hilft, ist nicht geklärt. Nach Angaben eines
  Besitzers leuchtet sie während eines Drucks, bei einer
  Kalibrierung aus dem Menü aber nicht. Das ist der andere Sensor, siehe
  [Wägezellen-Störungen](loadcell-emi-noise.md).
- **Ein Start, der unter 7.0.0 beim Offset-Sensor hängen bleibt, ist ein eigenes
  Problem, behoben in 7.0.1.** `reported`, zwei Quellen. Mehrere Besitzer berichten
  unter 7.0.0, dass der Drucker beim Hochfahren in der Phase des Offset-Sensors stehen
  bleibt, nachdem sie ihn zurückgesetzt hatten, während ein Druck startete oder ein
  Werkzeug am Kopf war
  ([Thread](https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/indx-firmware-7-0-0-stuck-on-reset/)),
  und der Besitzer, der
  [Firmware-Issue 5544](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5544)
  eröffnet hat, beschreibt dasselbe Hängenbleiben bei jedem Start, nachdem er den
  Drucker während einer Kollision beim Z-Homing zurückgesetzt hatte. Jedem Bericht,
  der sagt, wie es begann, geht ein Zurücksetzen voraus, und keine der beiden Quellen
  weist auf die Sensorplatine. Prusas Versionshinweise zu
  [7.0.1](https://help.prusa3d.com/downloads/core-one-indx), veröffentlicht am
  19. Oktober 2026, führen eine einzige Änderung auf: eine Behebung für Core One
  INDX-Drucker, die beim Start auf dem Bildschirm hängen bleiben, der den
  Werkzeug-Offset-Sensor als bereit meldet. Die ausführlichen
  [Hinweise zu 8.0.0](https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v8.0.0)
  nennen dieselbe Behebung, und der Quellcode zeigt, dass sie gar nicht im Code des
  Sensors liegt. Die einzige Codeänderung in 7.0.1, die auch 8.0.0 enthält,
  [behebt eine Verklemmung](https://github.com/prusa3d/Prusa-Firmware-Buddy/commit/852dedffe929cf95ea5031c9e8a8e234f1536d9d)
  in der Prüfung, die vergleicht, ob der Kopf ein Werkzeug erkennt, mit dem Werkzeug, das
  der Drucker zuletzt als aufgenommen gespeichert hat. Bei einer Abweichung öffnet diese
  Prüfung einen Dialog und wartet auf eine Antwort, und laut ihrem Commit konnte sie das
  tun, bevor der Bildschirm bereit war, ihn anzuzeigen. Die Bereit-Meldung des Sensors
  ist der letzte Schritt des Startbildschirms, dort bliebe der Drucker also stehen;
  dieser letzte Teil ist die Lesart dieser Seite. Der Besitzer, der den Thread eröffnet
  hat, berichtet, er habe das Hängenbleiben erneut herbeigeführt und 7.0.1 behebe es. Kein
  Besitzer hat gesagt, ob oder wie er 7.0.1 auf einen Drucker gebracht hat, der bereits
  hing. Die Flash-Vorgänge auf hängenden Druckern, die Besitzer beschreiben, waren
  Downgrades: Zwei Besitzer brachten ihre Drucker wieder zum Starten, indem sie 6.9.2
  flashten, einer davon mit einem erzwungenen Flashen, und ein dritter, dessen erster
  Versuch eines Downgrades am selben Startbildschirm stehen geblieben war, bekam 6.9.1
  installiert, indem er Reset drückte und dann den Drehknopf gedrückt hielt, bis die
  Installation begann. Zwei andere stellten fest, dass die Rückkehr nicht half, und ein
  Zurücksetzen auf Werkseinstellungen half niemandem, der es versuchte. Drei Besitzer,
  zwei im Thread und der eine im Issue, kamen ohne neue Firmware weiter, indem sie
  einmal mit abgezogenem INDX-Kabel starteten, am INDX-Hauptstecker oder am
  xBuddy-Board. Im Thread lauten die Schritte: bei ausgeschaltetem Drucker abziehen,
  einmal einschalten, ausschalten, wieder anschließen und erneut einschalten. Der
  Bericht im Issue sagt nicht, ob der Drucker beim Abziehen ausgeschaltet war; schalten
  Sie ihn aus, bevor Sie einen der beiden Stecker abziehen. Ein Start, der abbricht,
  weil die INDX-Kopfplatine zu kalt ist, ist etwas anderes: Ein Besitzer bittet in
  [Firmware-Issue 5585](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5585)
  darum, den Start trotzdem abschließen zu lassen, damit die Bettheizung die Platine
  aufwärmen kann. Die Firmware hat einen
  [Rotbildschirm-Fehler, 36274](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/lib/Prusa-Error-Codes/yaml/buddy-error-codes.yaml),
  für eine Kopfplatine unterhalb ihres zulässigen Bereichs; der Bericht sagt nicht, ob
  der Besitzer diesen Fehler gesehen hat und welche Firmware er verwendet.

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
der Besitzer weist durchgängig auf die Platine, mit einer Ausnahme: ein einzelner
Besitzer, bei dem der Fehler in dem lag, was er Werkzeughalter nennt
([Thread](https://forum.prusa3d.com/forum/ceske-forum-obecna-diskuze-oznameni-a-novinky/core-one-indx-tool-offset-out-of-bounds-36130-loadcell-test-issue/)),
dort, wo er erscheint, als `provisional` markiert.

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
stabile 6.9.1 sowie die darauf folgende 6.9.2 enthalten denselben Code, was die
Release-Tags zeigen und die Versionshinweise nicht sagen. Damit ist dieser Code die
veröffentlichte Behebung des Herstellers, keine nachgewiesene Heilung: Ein Besitzer im
Bericht sah mit der Beta weiterhin gelegentliche Fehlschläge, und der erste Besitzer,
der zur stabilen Version berichtet, in einem eigenen Issue, sieht die Kalibrierung bei
Drucken mit mehreren Werkzeugen weiterhin oft scheitern und führt das auf Spülmaterial
an den Düsen zurück. Die Versionshinweise zu 7.0.0 und 7.0.1 sagen nichts dazu. Ihr
Quellcode und der von 8.0.0, veröffentlicht am 3. November 2026, behalten die
Sensoreinstellungen und Kalibriertemperaturen von 6.9.1 bei, was die Tags zeigen. Die
Wiederholung je Werkzeug in 8.0.0 steht in deren ausführlichen Hinweisen und im
Quellcode, doch nach einer gescheiterten Messung über dem Sensor wiederholte schon der
Quellcode von 6.9.0 bis 7.0.1 dieses Werkzeug allein; 8.0.0 tut dasselbe nun auch nach
den übrigen Fehlschlägen in den Schritten eines Werkzeugs. Der in den Hinweisen
genannte eigene Bildschirm mit Werkzeugangabe für jede Art von Fehlschlag trifft dort
nur zum Teil zu. Berichtet hat über beides noch niemand. Die
ersten beiden Berichte zu
7.0.0, einer im Forum und einer im Issue-Tracker, beschreiben jeweils einen Fehlschlag
beim Druckstart, und keiner wird auf die Sensorplatine zurückgeführt. Ein dritter, in
einem anderen Issue, macht die niedrigere Kalibriertemperatur für an der Düse
verbliebenes PETG verantwortlich; das ist ein einzelner Bericht. Zu 8.0.0 gibt es noch
keine. Das Hängenbleiben beim Start unter 7.0.0 stützt sich auf den Forenthread und das
Issue, die dort verlinkt sind, wo es erscheint; dass 7.0.1 es behebt, beruht auf Prusas
Versionshinweisen und dem Test eines Besitzers, und was die Behebung ändert, stammt aus
ihrem Commit, den auch 8.0.0 enthält. Dass das Ausschalten der Leuchte, ohne dass
daneben eine weitere Änderung berichtet wird, geholfen hat, stützt sich auf zwei Besitzer im Thread zur
Werkzeug-Offset-Kalibrierung und einen in Issue 5526.

Der Hinweis auf die Referenzfrequenz des LDC1612 ist ein separater Einzelbericht eines
anderen Besitzers und ist dort, wo er erscheint, als `provisional` markiert. Der eigene
Commit des Herstellers bestätigt, dass der Takt über der Grenze des Chips lag, und
ändert ihn zusammen mit mehreren anderen Sensoreinstellungen, sagt aber nichts darüber,
ob das die Fehlschläge dieses Besitzers verursacht hat. Dass 7.0.0 und 8.0.0 diese
Einstellungen beibehalten und die Leseschleife der Sensorplatine überarbeiten, stammt
aus dem Vergleich ihrer Tags mit dem von 6.9.2.

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
- [Dock-Kalibrierung lehnt einige oder alle Docks ab](dock-calibration-rejects-docks.md) —
  dort ist eine nicht passende 1.5GT-Riemeneinstellung das Erste, was zu prüfen ist
- [Wen Sie kontaktieren](support-and-warranty-path.md) — so kommen Sie an das Ersatzteil:
  Diagnose von Prusa, Hardware von Bondtech, und eröffnen Sie den Fall früh genug, dass
  das Datum in Ihren Garantiezeitraum fällt.
