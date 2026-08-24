---
title:        Oozing spoils bed probing and tool calibration
confidence:   reported
updated:      2026-08-24
author:       hyiger
printer:      Core One
toolhead:     INDX
hotend:       unknown
nozzle:       0.25mm, 0.4mm, 0.8mm reported
firmware:     unknown
sources:
  - https://forum.prusa3d.com/forum/prusa-indx-how-do-i-print-this-printing-help/petg-oozing-and-impeding-bed-probing/
  - https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/nozzle-cleaning-calibration-issues/
  - https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/a-summary-of-common-indx-problems/
superseded_by:
---

# Oozing spoils bed probing and tool calibration

## Summary

Filament that oozes while the machine is probing or calibrating puts material where
the machine is trying to take a measurement, and the measurement fails. Owners have
hit this during bed probing and during tool offset calibration, with more than one
filament type. There are several contributing causes and they are worth separating,
because the one with the best first-hand evidence — a dirty offset sensor window — is
also the easiest to fix and the least likely to be what you suspect first.

## Detail

Two different measurements get spoiled by ooze, and they fail differently:

- **Bed probing.** Material accumulates on the nozzle tip before or during the
  probing pass, so contact is detected early or inconsistently. Owners report
  probing leaving visible deposits on the sheet.
- **Tool offset calibration.** Ooze interferes with the nozzle being sensed properly
  against the offset sensor, and calibration fails. One owner reports this failing on
  every tool after swapping nozzle sizes around, and having to unload all filament,
  calibrate, then reload.

### Start here: clean the offset sensor window

The resolution that actually closed the main thread on this was cleaning the sensor
window on each nozzle. The owner reported the swabs coming away visibly black even
though they did not believe they had touched the windows, and a test print working
afterwards. This costs a few minutes and it is the highest-value thing to check.

!!! warning "Do not clean the sensor window with IPA"
    The advice relayed in the thread is to use soapy water and a cotton swab rather
    than isopropyl alcohol, on the grounds that IPA is too aggressive for that
    window. Provenance is worth stating plainly: this was described as a vendor
    recommendation circulating on Discord, and the person relaying it said openly
    that they could not point to an official source. Soapy water is the low-risk
    choice either way, so prefer it — but treat the reason as unconfirmed.

    TODO(verify): whether the vendor has published an official cleaning procedure
    for the offset sensor window.

!!! warning "Clean it, but do not polish it"
    A later caution in the same thread is worth heeding: the sensor face is meant to
    be matte, and should not end up shiny or reflective. Be sparing. The goal is to
    lift filament debris off it, not to bring up a shine.

    One caveat on that advice — the owner giving it describes the sensor as infrared,
    whereas the offset sensor is elsewhere described as eddy-current based. Those are
    different sensing principles and it is not clear which component is meant. The
    practical instruction is sound either way: remove the debris, stop there.

### Dry the filament

Suggested early and repeatedly for PETG in particular: moisture makes filament
stringy and encourages it to stick to the nozzle. This is standard practice rather
than an INDX-specific finding, and it was offered as a first guess rather than a
confirmed cause in these threads — but the INDX is reported to be more
moisture-sensitive than the Nextruder it replaces, so it is worth ruling out before
chasing anything more complicated.

### The probe temperature may not be the one you expect

There is a reported firmware and slicer behaviour where the temperature used for
pre-print bed probing is derived from the filament assigned to **tool 1**, not from
the tool actually doing the probing. If a high-temperature material is assigned to
T1, everything probes hot and oozes, regardless of what is loaded elsewhere.

The reported workaround is elegant if it holds: it is enough to *declare* a
low-temperature filament in T1 in the slicer — the physical filament does not have to
be there — which would explain why jobs sliced from profiles that assume a
low-temperature material never showed the problem. There is also a start-G-code
approach that forces the probing temperature before the mesh bed levelling block, by
replacing the generated temperature command with a fixed one.

TODO(verify): the probing temperature to force, and the exact G-code command and
argument to use. Also TODO(verify): the reduction one owner used successfully on a
non-INDX Core One for the same symptom, quoted as a range rather than a single figure.
No temperature is published on this page until someone has confirmed it on hardware.

Two further reported details in this area, both single-source and both worth knowing
before you go hunting: a slicer configuration update corrected the derivation for
most materials but at least one engineering material still probes hot; and the
temperature used for tool offset calibration is fixed in firmware and cannot be
changed from G-code, so this workaround does not help that failure mode. There is
also a sibling slicer trap in which the **bed** temperature follows T1 in the same
way.

### If none of that helps

If probing fails with the nozzle plainly nowhere near the sheet — a gap you can see
rather than one you would measure — that is a different fault entirely and ooze is
not your problem. See [loadcell noise](loadcell-emi-noise.md). If tool offset
calibration fails regardless of cleanliness and filament state, see
[offset sensor board failure](offset-sensor-board-failure.md).

## Verification

`reported` — the symptom is reported independently by different owners with different
materials.

[PETG oozing and impeding bed probing](https://forum.prusa3d.com/forum/prusa-indx-how-do-i-print-this-printing-help/petg-oozing-and-impeding-bed-probing/)
is the primary thread: the original poster reports PETG oozing enough to spoil bed
probing, and a second owner independently reports the same class of failure with PLA
across every tool during calibration. The thread is marked answered, and its accepted
answer is the sensor-window cleaning, confirmed first-hand by the person who had the
problem. That is the strongest evidence on this page.

Single-source and unverified: the tool-1 temperature derivation, the
declare-a-cool-filament workaround, the G-code override, the slicer configuration
fix, and the hard-coded calibration temperature all come from the
[common problems summary](https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/a-summary-of-common-indx-problems/),
a condensation of a now-offline community knowledge base. None of it is separately
confirmed in the forum corpus, and no numbers from it are reproduced here.

Where the sources disagree: drying was offered confidently as the likely cause for
PETG, but the case that was actually resolved was resolved by cleaning, not drying.
Do not assume moisture just because the filament is PETG — when the question was put
to the original poster directly, they replied that they had been printing straight
from a filament dryer, which rules moisture out for that case entirely.

## Related

- [Probing fails or nozzle never touches the bed](loadcell-emi-noise.md)
- [Tool offset calibration fails](offset-sensor-board-failure.md)
- [Phantom tools and park failures](tool-detection-ringdown-decay.md)
- [Blobs dragged into the print](stringing-and-wiper-calibration.md) — the same
  problem of material in the wrong place, but occurring at tool changes rather than
  during probing. If your deposits appear at tool swaps, start there instead.
