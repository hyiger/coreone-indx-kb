# Core One INDX Knowledge Base

Community reference for the Bondtech INDX toolchanger on the Prusa Core One.

!!! info "Every page states its evidence level"
    **measured** — someone ran the test and recorded the result, with hardware
    and method documented. **reported** — multiple independent users describe
    the same thing. **provisional** — one report, plausible, unverified.

    Check the level before acting on a number. A `provisional` nozzle
    temperature is a starting point, not a setting.

## Sections

- **[Calibration](calibration/index.md)** — per-filament and per-nozzle values, with
  the hardware and method they were measured on.
- **[Issues](issues/index.md)** — known faults, causes, and fixes.
- **[G-code](gcode/index.md)** — start, end, layer change, and toolchange blocks;
  placeholder syntax; firmware behavior.
- **[Reference](reference/index.md)** — hardware specs, tool numbering, assembly notes.

## Hardware matters more than you'd expect

Calibration values are specific to a filament **and** a nozzle **and** often a
printer. An extrusion multiplier measured on a 0.4mm Diamondback does not
transfer to a 0.6mm CHT. Every page states its hardware; if yours differs, treat
the value as a starting point and re-verify.

## Superseded pages

Firmware changes and Bondtech ships revisions. When something stops being true
the page stays up with a banner and a pointer to what replaced it, because
people arrive from stale search results and need to know they have.

## Contributing

See [Contributing](contributing.md). Corrections are welcome, especially ones that
move a page from `provisional` to `measured`.

Content is CC BY-SA 4.0. Fork it — this exists because the last community INDX
resource went offline, and it should be trivially possible to keep it alive
without me.
