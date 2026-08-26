---

source_sha:   2db04a5448084e437f84f24de6ef6a0726bfd6c894b1121652558ad00b269f06
---
# Core One INDX Wissensdatenbank

Referenz der Community für den Bondtech-INDX-Werkzeugwechsler am Prusa Core One.

!!! info "Jede Seite nennt ihre Belegstufe"
    **measured** (gemessen) — jemand hat den Test durchgeführt und das Ergebnis
    festgehalten, mit dokumentierter Hardware und Methode. **reported** (berichtet)
    — mehrere unabhängige Anwender beschreiben dasselbe. **provisional**
    (vorläufig) — ein einzelner Bericht, plausibel, unbestätigt.

    Prüfen Sie die Stufe, bevor Sie nach einer Zahl handeln. Eine als
    `provisional` eingestufte Düsentemperatur ist ein Ausgangspunkt, keine
    Einstellung.

## Bereiche

- **[Kalibrierung](calibration/index.md)** — Werte pro Filament und pro Düse, mit
  der Hardware und der Methode, an der sie gemessen wurden.
- **[Probleme](issues/index.md)** — bekannte Fehler, Ursachen und Abhilfen.
- **[G-Code](gcode/index.md)** — Start-, End-, Schichtwechsel- und
  Werkzeugwechselblöcke; Platzhaltersyntax; Firmware-Verhalten.
- **[Referenz](reference/index.md)** — Hardware-Spezifikationen, Werkzeugnummerierung, Montagehinweise.

## Die Hardware zählt mehr, als man erwartet

Kalibrierwerte gelten für ein bestimmtes Filament **und** eine bestimmte Düse
**und** oft auch einen bestimmten Drucker. Ein Extrusionsmultiplikator, der an
einer 0.4mm Diamondback gemessen wurde, lässt sich nicht auf eine 0.6mm CHT
übertragen. Jede Seite nennt ihre Hardware; weicht Ihre davon ab, behandeln Sie
den Wert als Ausgangspunkt und überprüfen Sie ihn erneut.

## Überholte Seiten

Firmware ändert sich, und Bondtech liefert Revisionen aus. Wenn etwas nicht mehr
zutrifft, bleibt die Seite mit einem Hinweisbanner und einem Verweis auf das,
was sie ersetzt hat, bestehen — denn Leser gelangen über veraltete Suchergebnisse
hierher und müssen wissen, dass es so ist.

## Mitwirken

Siehe [Mitwirken](contributing.md). Korrekturen sind willkommen, besonders solche,
die eine Seite von `provisional` nach `measured` heben.

Die Inhalte stehen unter CC BY-SA 4.0. Forken Sie sie — dieses Projekt existiert,
weil die letzte INDX-Ressource der Community offline gegangen ist, und es soll
ohne Weiteres möglich sein, es auch ohne mich am Leben zu erhalten.
