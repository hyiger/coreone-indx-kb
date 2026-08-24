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

## Start with the symptom

**The machine damages the print, or itself**

- [Toolhead collides with finished parts](complete-individual-objects-collision.md) —
  slicing with *Complete individual objects* while an object contains a mid-object tool
  change can drive the head through parts it has already finished. Turn the feature off
  until it is fixed.

**The printer disagrees with reality about which tool is where**

- [Phantom tools, "tool not detected" and park failures](tool-detection-ringdown-decay.md)
  — a tool that isn't there is reported present, a tool that is there is reported
  missing, or a tool that parked correctly is reported still attached.

**Probing or calibration fails**

- [Probing fails or nozzle never touches the bed](loadcell-emi-noise.md) —
  electrical interference in the loadcell signal makes the printer believe it has
  touched down while the nozzle is still well clear.
- [Tool offset calibration fails](offset-sensor-board-failure.md) — the contactless
  offset sensor returns no samples, so calibration has nothing to work with. Usually
  the sensor board.
- [Oozing spoils bed probing and tool calibration](oozing-during-probing-and-calibration.md)
  — material where the machine is trying to take a measurement. Start by cleaning the
  offset sensor window.

**Defects appear on the printed part**

- [Blobs dragged into the print — nozzle wiper and purge](stringing-and-wiper-calibration.md)
  — material carried out of the purge area at tool changes. Largely addressed by
  firmware 6.9.0, which automated the wiper alignment that used to be done by hand.
- [Diagonal banding across print walls](diagonal-banding.md) — a regular pattern that
  reverses with perimeter direction. There is a two-print test that tells you whether
  it is the extruder or the motion system, before you open a support case.

**Nozzles and the filament path**

- [Nozzle hardness and abrasive filaments](nozzle-hardness.md) — the shipped nozzles
  are not hardened in the conventional sense. What that means for filled filaments,
  and the vendor's remediation offer.
- [Unload and eject failures](filament-guide-bore-unload-failure.md) — printing works
  but unloading fails. *Single source — read the caveat before acting.*

**Process**

- [Who to contact](support-and-warranty-path.md) — diagnosis and replacement parts
  come from two different companies, and sending your problem to the wrong one is the
  most common way owners lose weeks.

## Three faults that look alike

Probing and calibration failures are the ones people misdiagnose most, because three
unrelated causes present through the same two error paths. The quickest discriminators:

| What you see | Likely page |
|---|---|
| Probing stops with the nozzle **visibly** nowhere near the sheet | [Loadcell noise](loadcell-emi-noise.md) |
| Bed probing is fine, but **tool offset calibration** fails | [Offset sensor](offset-sensor-board-failure.md) |
| Material is building on the nozzle, deposits left on the sheet | [Oozing](oozing-during-probing-and-calibration.md) |
| Failures follow a **firmware update** rather than appearing gradually | [Tool detection](tool-detection-ringdown-decay.md) |

Chasing the wrong one of these costs days, which is why each page opens by saying how
to tell it apart from its neighbours.
