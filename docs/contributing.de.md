---

source_sha:   08a1f39455166889daf2d48f4acf03213a039879f41d16f0e6df8503163ed2a0
---
# Mitwirken

Diese Wissensdatenbank existiert, weil die frühere INDX-Ressource der Community
vom Netz gegangen ist. Das Ziel ist Beständigkeit: einfaches Markdown in Git,
kein gehosteter Dienst, der auslaufen kann, von jedem forkbar, falls auch dieses
Projekt zum Stillstand kommt.

## Belegstufen

Jede Seite deklariert in ihrem Front Matter eine `confidence`-Stufe. Das ist die
mit Abstand wichtigste Konvention hier, und sie ist es, die dies von einer
Forensuche unterscheidet.

| Stufe | Bedeutet | Erfordert |
|---|---|---|
| `measured` | Jemand hat den Test durchgeführt und das Ergebnis festgehalten | Hardware, Methode, Datum, wer |
| `reported` | Mehrere unabhängige Anwender berichten dasselbe | Mindestens zwei verlinkte Quellen |
| `provisional` | Einzelner Bericht, plausibel, unbestätigt | Quellenlink, ausdrücklicher Vorbehalt |

Eine Seite darf Stufen nicht stillschweigend vermischen. Trägt eine Seite einen
`measured`-Wert und einen `provisional`-Wert, kennzeichnen Sie die vorläufige
Aussage direkt im Text.

**Veröffentlichen Sie niemals eine Zahl ohne Stufe.** Ein Kalibrierwert ohne
Quelle ist schlimmer als gar keine Seite — jemand wird danach handeln.

## Was nicht in dieses Repository gehört

- **Wörtliche Forenbeiträge.** Foreninhalte sind urheberrechtlich durch ihren
  Verfasser geschützt. Extrahieren Sie die Erkenntnis, formulieren Sie sie in
  eigenen Worten und verlinken Sie den Thread.
- **Discord-Inhalte**, sofern die Server-Administratoren nicht zugestimmt haben
  und die Teilnehmer nicht anonymisiert sind. Öffentliche Foren und private
  Support-Server sind zweierlei.
- **Rohe Crawl-Ausgaben.** Die liegen in einem separaten Arbeits-Repository und
  sind hier durch gitignore ausgeschlossen.
- **Screenshots, die Benutzernamen oder persönliche Angaben enthalten.**

## Fakten und Formulierung

Fakten sind nicht urheberrechtlich schützbar. „Das 0.6mm-INDX-Profil benötigt X“
darf jeder frei feststellen. Der Satz, den jemand geschrieben hat, um das zu
sagen, nicht. Neu formulieren, dann zitieren.

## Überholte Informationen

Firmware ändert sich; Bondtech liefert Revisionen aus. Wenn eine Erkenntnis nicht
mehr zutrifft, löschen Sie die Seite nicht — fügen Sie dem Front Matter ein Feld
`superseded_by` und oben auf der Seite ein Hinweisbanner hinzu. Leser gelangen
über veraltete Suchergebnisse hierher und müssen das wissen.

## Seitenvorlage

Kopieren Sie `docs/_template.md`. Füllen Sie jedes Front-Matter-Feld aus.
`unknown` ist ein zulässiger Wert; ein fehlendes Feld nicht.

## Prüfung

Kalibrierwerte werden von Menschen überprüft. Keine Ausnahmen, unabhängig davon,
wie der Entwurf entstanden ist.
