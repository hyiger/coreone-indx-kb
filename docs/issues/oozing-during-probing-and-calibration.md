---
title:        Oozing spoils bed probing and tool calibration
confidence:   reported
updated:      2026-09-16
author:       hyiger
printer:      Core One
toolhead:     INDX
hotend:       unknown
nozzle:       0.25mm, 0.4mm, 0.8mm reported
firmware:     unknown
sources:
  - https://forum.prusa3d.com/forum/prusa-indx-how-do-i-print-this-printing-help/petg-oozing-and-impeding-bed-probing/
  - https://forum.prusa3d.com/forum/prusa-indx-how-do-i-print-this-printing-help/printing-pc-on-indx-oozing-at-bed-probing-leveling/
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/psa-if-you-are-struggling-with-tool-offset-calibration-failing-non-stop-at-the-start-of-a-print-get-firmware-6-9-1/
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5483
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

There is a reported firmware and slicer behavior where the temperature used for
pre-print bed probing is derived from the filament assigned to **tool 1**, not from
the tool actually doing the probing. If a high-temperature material is assigned to
T1, everything probes hot and oozes, regardless of what is loaded elsewhere.

The reported workaround is elegant if it holds: it is enough to *declare* a
low-temperature filament in T1 in the slicer — the physical filament does not have to
be there — which would explain why jobs sliced from profiles that assume a
low-temperature material never showed the problem. On the stock profile this site
reproduces, though, the rule is keyed to the print's initial tool rather than to T1 — see
the PC section below before relying on it. There is also a start-G-code
approach that forces the probing temperature before the mesh bed leveling block, by
replacing the generated temperature command with a fixed one.

TODO(verify): the probing temperature to force, and the exact G-code command and
argument to use. Also TODO(verify): the reduction one owner used successfully on a
non-INDX Core One for the same symptom, quoted as a range rather than a single figure.
No temperature is published on this page until someone has confirmed it on hardware.

Two further reported details in this area, worth knowing before you go hunting: a
slicer configuration update corrected how that temperature is worked out, for most
materials — though one engineering material still probes hot; and the temperature used for tool offset
calibration is fixed in firmware and cannot be changed from G-code, so this workaround
does not help that failure mode. That second detail is still single-source. There is
also a sibling slicer trap in which the **bed** temperature follows T1 in the same way.

**The engineering material is PC.** A [second owner](https://forum.prusa3d.com/forum/prusa-indx-how-do-i-print-this-printing-help/printing-pc-on-indx-oozing-at-bed-probing-leveling/) hit this with PC Blend and
described it from the other end: probing ran hot enough to ooze onto the sheet and fail
leveling, and lowering the nozzle temperature by hand on the next attempt cured it
outright. That moved "at least one engineering material still probes hot" off a single
report and gave it a name, and it has not stayed with one owner since. A further owner in
the same thread, another in a [separate thread](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/psa-if-you-are-struggling-with-tool-offset-calibration-failing-non-stop-at-the-start-of-a-print-get-firmware-6-9-1/), and a
[firmware issue](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5483) all describe PC Blend failing bed probing until the
temperature comes down.

**Where the temperature comes from.** There is **no dedicated probing-temperature field**
in the slicer, but there is a rule. The stock printer start G-code works out the probing
temperature from the filament of the print's **initial tool** — the first tool the print
actually uses — and gives PC and PA a case of their own: a
fixed offset below the first-layer temperature. The annotated profile reproduces that
expression in its section on globals and the probe temperature — see
[annotated profile G-code](../gcode/indx-profile-gcode.md). It is the rule these owners
keep running into.

**Initial tool, not T1.** That expression reads the filament of `initial_tool`, which is
not the T1 behavior reported further up. The two select the same filament only when a
print starts on T1. On a print that starts on another tool they point at different
presets — so on this profile, declaring a low-temperature filament in T1 will not help a
print that begins on T3; the filament to look at is the one your print starts with.
Whether the earlier T1 report describes an older profile or a different machine state is
not established.

**6.9.1-beta does not change it.** The beta lowered the temperature used for *tool offset
calibration* — a different step, and one that firmware controls. The bed-probing temperature comes from
the slicer profile, so owners on the beta still see PC Blend probe hot.

**Adjusting it.** One owner widened the PC offset in the printer's start G-code and the
failures stopped. The catch, which they pointed out themselves, is that a printer
configuration update replaces the start G-code, so the edit has to be redone after each
one. The same expression also checks the initial tool's filament notes for an override
marker before it ever reaches the PC case, which suggests a per-filament route that would
survive those updates — but that is a reading of the profile, not something an owner has
reported testing. And the slicer's own **oozing-prevention option did not help**, so
reaching for it first will cost you a print.

TODO(verify): these accounts state the temperature PC probed at, the lower ones that
worked, and the adjusted offset. None of them is published here. Forum posts and a bug
report are not the hardware confirmation this page requires before a temperature goes on
it — but they are leads, and they are the same figure the marker above is asking for.

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
