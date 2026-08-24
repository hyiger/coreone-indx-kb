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
    Drafts covering tool detection, loadcell noise, offset sensor failures, oozing
    during probing, nozzle hardness, the filament guide bore, and the support route
    are written and awaiting review. They appear here once their claims and any
    numbers have been checked by a human.
