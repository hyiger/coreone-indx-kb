---
title:        Issues
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

# Issues

Known faults on the INDX, what causes them, and what has actually fixed them.

Pages here lead with the **mechanism** rather than the fix. That is deliberate:
several INDX faults look alike from the outside and have completely different
causes, and a reader who understands why a symptom happens can tell their fault
apart from the one that merely resembles it.

## How to read a page here

Check the `confidence` field before acting. A `provisional` page is one person's
experience written down so the next person recognises it — not a procedure.

Where a page withholds a number behind a `TODO(verify)` marker, that is intentional.
Thresholds, temperatures, dimensions and deadlines are verified against hardware or
against the vendor before they are published here, because a wrong one costs the
reader a part, a print, or a warranty window.

## Pages

- **[Probing fails or nozzle never touches the bed](loadcell-emi-noise.md)** —
  electrical interference in the loadcell signal makes the printer think it has
  touched the bed while the nozzle is still well clear.
- **[Tool offset calibration fails](offset-sensor-board-failure.md)** — the
  contactless offset sensor returns no samples, so calibration has nothing to work
  with. Usually the sensor board.

These two are worth reading together. They involve **different sensors** and have
different fixes, but they are routinely confused with each other, and chasing the
wrong one costs days. The quickest way to tell them apart: loadcell noise makes
probing stop with the nozzle visibly nowhere near the sheet; an offset sensor fault
shows up during tool offset calibration and leaves bed probing working.

## Fault families

The faults reported so far group into a few families:

- **Detection** — the printer believing something untrue about which tool is
  present, or whether it has parked.
- **Sensing** — probing and offset calibration failing, whether from electrical
  noise, contamination, or a failed sensor board.
- **Nozzles and consumables** — hardness and abrasive wear, factory defects,
  filament path obstructions.
- **Support and process** — who to contact for what, and in what order.

!!! note "Pages in preparation"
    Further pages covering tool detection and park failures, oozing during probing,
    nozzle hardness, the filament guide bore, and the support and warranty route are
    drafted and awaiting review. They appear here once their claims and any numbers
    have been checked by a human.
