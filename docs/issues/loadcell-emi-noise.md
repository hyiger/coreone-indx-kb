---
title:        Probing fails or nozzle never touches the bed — loadcell noise
confidence:   reported
updated:      2026-08-24
author:       hyiger
printer:      Core One
toolhead:     INDX
hotend:       unknown
nozzle:       unknown
firmware:     unknown
sources:
  - https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/nozzle-not-touching-bed-during-probing/
  - https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/a-summary-of-common-indx-problems/
  - https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/tool-offset-calibration-failing/
superseded_by:
---

# Probing fails or nozzle never touches the bed — loadcell noise

## Summary

If bed probing behaves as though the nozzle has already touched down while it is
still obviously well clear of the sheet, the likely cause is electrical
interference in the loadcell signal rather than anything mechanical. The vendor has
acknowledged interference from the heater as the working theory. The community fix,
which vendor support now also recommends, is a clamp-on ferrite core on the main
toolhead cable close to where it enters the controller board. Several owners report
this resolving the fault outright.

## Detail

The INDX senses bed contact through a loadcell, and the signal from it shares a
cable loom with the power that drives the heater. In that loom the power pair is
twisted, which cancels most of its radiated noise, but the loadcell's signal pair is
not — so it is comparatively exposed to whatever the heater is doing. When that
noise is large enough, the firmware reads it as a contact event.

The tell-tale is *how wrong* the behaviour is. A mechanical or offset problem makes
the nozzle probe slightly too high or too low. Noise-driven false contact makes it
stop while the nozzle is plainly nowhere near the sheet — a gap you can see across
the room, not one you would measure with paper. If you are watching a probing pass
and thinking "it hasn't even got close", this page is probably your fault.

Symptoms reported in this family:

- Probing completes with the nozzle visibly clear of the sheet
- Loadcell self-test failures
- Z homing or probing that fails **only once the hotend is hot** — a strong hint,
  because it points at the heater as the noise source
- False Z-collision errors
- Repeated bed-levelling retries, and unusually long mesh times
- A first layer that does not stick, or that drags filament up into a blob, because
  the machine believes the bed is higher than it is

### What to try

1. **Fit a clamp-on ferrite core to the main toolhead cable**, positioned near the
   controller board end. This is the fix with the most independent confirmation, and
   it is now what vendor support suggests. A plain clamp-on core over the outside of
   the cable has been enough for several machines.
2. **If a plain core is not enough**, stubborn cases have responded to routing the
   cable through a higher-grade toroid for several turns instead of a single pass.
   TODO(verify): the specific ferrite material grade and the number of turns.
   Reported in the common-problems summary thread; not independently confirmed here.
3. **Recalibrate or factory-reset afterwards.** On several machines the ferrite
   appeared to do nothing until the stored calibration data was discarded — by a
   factory reset or a full recalibration — because the printer was still working from
   figures it had captured while the signal was noisy. If you fit a core and nothing
   changes, do this before concluding the core did not help.
4. **Mind the placement.** At least one reported position — at the controller's
   extension-board connector rather than on the main cable — made the problem worse.
   If your first placement degrades things, move it rather than abandoning the idea.

!!! tip "How to tell interference from a genuinely bad loadcell"
    A ferrite core treats electrical interference. It will not fix a failed loadcell,
    and the two present almost identically. One owner separated them cleanly: their
    probing fault **followed a replacement toolhead** across a swap while the original
    head homed perfectly every time, on a recent controller board. Interference is a
    property of the machine and its wiring; a fault that travels with the toolhead is
    in the toolhead. See [diagonal banding](diagonal-banding.md), where that swap is
    described. If your board is recent and the fault moves with the head, go to the
    vendor rather than buying ferrites.

If none of that helps, particularly if the failure happens only with the heater on
and you are on an early board revision, the path is hardware replacement through the
vendor. One owner reported success wrapping the wiring at the controller connector in
grounded shielding foil instead, which is consistent with the same root cause.

TODO(verify): the raw loadcell value ranges that distinguish a healthy machine from
an affected one. The summary thread quotes an idle-value band for each, and those
numbers would make this page far more diagnostic — but they need checking against
firmware before being published, because a reader will use them to decide whether
their machine is faulty.

!!! note "This is a mitigation, not a cure"
    The vendor has described the ferrite as a stopgap rather than a fix, and a
    firmware-side improvement to loadcell handling is reportedly in progress. If you
    are reading this well after the date above, check whether a newer firmware has
    addressed it before adding hardware.

## Verification

`reported` — independently described in more than one thread by different owners.

In [Nozzle not touching bed during probing](https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/nozzle-not-touching-bed-during-probing/)
an owner reports probing running with the nozzle far above the sheet on a machine
that had passed all its setup calibrations; after fitting a ferrite core to the main
cable they confirm probing began working correctly. A second owner in the same thread
reports one probe-too-high incident and fitted a core pre-emptively without
regression. The mechanism, the vendor's acknowledgement, and the toroid variant come
from the [common problems summary](https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/a-summary-of-common-indx-problems/),
which is a condensation of a now-offline community knowledge base.

Where the sources are weaker: the controlled A/B test described in the summary
(failing without a core, working with one, failing again on removal) is reported
second-hand there and is not separately visible in the forum corpus. The loadcell
value bands and ferrite specifications are single-source and withheld above.

## Related

- [Tool offset calibration fails](offset-sensor-board-failure.md) — separate
  sensor, separate fault, often confused with this one
- [Oozing spoils bed probing and tool calibration](oozing-during-probing-and-calibration.md)
  — a completely different cause with an overlapping symptom, worth ruling out. If
  material is accumulating on the nozzle before contact, that is the other one.
- [Who to contact](support-and-warranty-path.md) — if it comes to a parts request:
  diagnosis from Prusa first, then the hardware from Bondtech.
