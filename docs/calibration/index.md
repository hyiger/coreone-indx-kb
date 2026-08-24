---
title:        Calibration
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
---

# Calibration

Per-filament and per-nozzle values, each recorded with the hardware and the method
it was measured on.

!!! danger "Every number here is human-verified before it is published"
    No calibration value reaches this site from a forum thread, from a plausible
    inference, or from a tool. Someone runs the test, records the result, and states
    the hardware they ran it on.

    This is the rule the site will not bend on. A wrong nozzle temperature published
    under someone's name causes a clog on a stranger's printer.

## Why hardware context is mandatory

A calibration value is specific to a filament **and** a nozzle **and** often a
printer. An extrusion multiplier measured on a 0.4mm Diamondback does not transfer
to a 0.6mm CHT — different geometry, different heat transfer, different flow. The
high-flow nozzle geometry used on the INDX in particular moves heat differently from
the Nextruder many owners are coming from.

So every page here states `printer`, `toolhead`, `hotend`, `nozzle` and `firmware` in
its front matter. If yours differs on any of those, treat the value as a starting
point and re-verify it rather than dialling it in.

## What belongs here

- Extrusion multiplier, pressure advance, shrinkage compensation, maximum volumetric
  speed — with the test used to derive them.
- Temperature ranges that were actually swept, not the ones on the spool label.
- Retraction figures, with the note that these are strongly machine-specific.

## What does not

Values copied from another site, from a slicer default, or from a forum post that
did not describe its method. Those are leads for someone to test, not entries.

!!! note "Empty for now"
    Nothing here yet. Calibration is the slowest section to fill precisely because
    of the verification rule, and that is the intended trade-off.

    Contributions that move a value from `provisional` to `measured` — by running
    the test and documenting the hardware — are the most valuable thing anyone can
    add. See [contributing](../contributing.md).
