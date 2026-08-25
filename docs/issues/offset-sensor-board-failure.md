---
title:        Tool offset calibration fails — contactless offset sensor
confidence:   reported
updated:      2026-08-25
author:       hyiger
printer:      Core One
toolhead:     INDX
hotend:       unknown
nozzle:       unknown
firmware:     6.9.0 for the calibration regression; the board fault is not version-specific
sources:
  - https://help.prusa3d.com/article/tool-offset-failed-36130-core-one-indx_1089016
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5442
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/offset-sensor-failure/
  - https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/tool-offset-calibration-failing/
  - https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/a-summary-of-common-indx-problems/
superseded_by:
---

# Tool offset calibration fails — contactless offset sensor

## Summary

Tool Offset Calibration failing repeatedly, with an error message that tells you
nothing useful, is most often a faulty contactless offset sensor board rather than
anything you have assembled wrongly. Clean the sensor first, because a fleck of
filament on it produces exactly the same failure. If cleaning does not fix it, the
resolution reported by multiple owners is a replacement sensor board — and belt
tension, which support may suggest, has not fixed a single reported case.

!!! important "Before you suspect the board: are you on 6.9.0?"
    An open bug report against the firmware describes tool offset calibration failing
    repeatedly **after upgrading to 6.9.0**, on a machine where it had been working.
    A second owner confirms the same. It affects all nozzles, and re-running the
    calibration wizard succeeds only after several retries.

    That matters here because it presents almost identically to the hardware fault
    this page is about, and the fix is completely different. If your calibration was
    fine before an update and started failing after one, you are more likely looking
    at this than at a failed sensor board — and replacing hardware will not help.

    The report is open and unresolved at the time of writing, so there is no fix to
    point at yet beyond retrying. Check the issue for the current state before
    starting an RMA. The firmware also links an official help article for this error
    code, which the reporter says did not resolve it for them.

## Error codes that lead here

| Code | What the printer shows |
|---|---|
| [`36130`](https://help.prusa3d.com/article/tool-offset-failed-36130-core-one-indx_1089016) | Tool offset failed |
| [`36136`](https://help.prusa3d.com/article/calibrate-dock-from-menu-17136-xl-36136-core-one-indx_1037195) | Calibrate dock from menu |

`36130` is this page. It is also the code the firmware links its own help
article for, which the owner reporting the 6.9.0 regression says did not resolve
their case.

## Detail

Two different sensors are involved in setting up an INDX, and knowing which one has
failed saves a great deal of wasted effort. The loadcell handles Z contact against
the bed. A separate contactless inductive sensor on its own small PCB handles tool
offsets. In this failure mode the loadcell Z-probe passes fine; it is the contactless
sensor that returns no readings at all, so calibration has nothing to work with.

The firmware log carries a distinctive fingerprint — an error naming the contactless
offset routine together with a failure to obtain a first sensor sample. That log line
is the single most useful thing you can capture, because the on-screen message is
generic and the on-screen suggestion to clean the nozzle is misleading.

What makes this fault confusing:

- **The tool number where it fails is not diagnostic.** Owners report failing on the
  first tool, and others report getting several tools in before failing, with the
  stopping point moving between attempts and no changes in between. Different
  stopping points do not mean different problems.
- **Swapping tools around does not help**, and neither does re-seating the tools.
  Several owners worked through permutations before concluding the sensor was at
  fault.
- **Belt tension is a red herring here.** It is a reasonable first guess and support
  has suggested it, but owners who squared and re-tensioned the gantry thoroughly
  report no change. Do not spend a night on it before capturing a log.
- **Cable continuity testing good does not clear the sensor.** One owner checked the
  cable, found it electrically fine, and the board was still the fault. Cable
  replacements on their own have not fixed reported cases.

### What to do, in order

1. **Clean the sensor itself**, not just the nozzle. A small piece of filament debris
   sitting on the sensor face causes an identical failure, and this is the one cause
   you can fix yourself in a minute.
2. **Capture a firmware log over the USB-C serial connection** and keep it. This is
   the evidence that gets a support case resolved quickly — at least one owner
   reports the vendor confirming the board as faulty specifically on the strength of
   submitted logs. TODO(verify): the serial baud rate to configure. It is stated in
   the summary thread, but a reader will type it into a terminal, so it needs
   checking first.
3. **Check the LED on the sensor PCB.** If it keeps blinking rapidly once a
   calibration has already failed, that points at the board itself — the rapid
   pattern is only meant to appear while the sensor's microcontroller is being
   flashed. Seeing it outside of a firmware update is a strong signal.
4. **Open a support case.** The reported route is diagnosis with Prusa first, then a
   Bondtech ticket for the replacement board, carrying Prusa's findings with it. A
   ticket that already says what Prusa identified moves faster than one starting from
   symptoms. Open it early even if you are not ready to act, so the date is on record
   — see [who to contact](support-and-warranty-path.md).

The sensor works on eddy currents, which is worth knowing for two reasons: it is why
a non-conductive nozzle tip is a design constraint for future nozzle variants, and it
is why surface contamination on the sensor matters as much as it does.

A board-to-board comparison reported in the summary found that a failing unit and a
working unit were the same hardware revision from the same production batch, so this
looks like unit-level variance rather than a bad batch you could identify from a
serial number.

!!! warning "One suggestion in the threads is not a repair"
    Reflow-oven reworking of the sensor board was floated by an owner as something
    they might try. There is no report of anyone doing it successfully, and it would
    almost certainly end any warranty claim on the part. Get the board replaced.

## Verification

`reported` — two independent threads, two different owners, both ending at board
replacement.

[Offset sensor failure](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/offset-sensor-failure/)
documents calibration failing on the first tool and establishes the support route
that owners converged on. [Tool offset calibration failing](https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/tool-offset-calibration-failing/)
is a separate owner with a different-looking presentation — failing partway through
the tool sequence, intermittently — who worked through belt tension and tool swaps
without improvement, verified cable continuity as good, and reports the vendor
confirming the PCB as the fault after reviewing submitted logs. That two dissimilar
symptom patterns resolve to the same component is the most useful thing on this page.

The log fingerprint, the LED diagnostic, the eddy-current mechanism, and the
same-batch comparison come from the
[common problems summary](https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/a-summary-of-common-indx-problems/),
a condensation of a now-offline community knowledge base. Those specifics are
single-source and have not been separately confirmed in the forum corpus.

Where the sources disagree: support's own first suggestions varied between cable and
board, and in one case belt tension was raised. Owner experience points consistently
at the board.

**Added since first publication.** The 6.9.0 calibration regression comes from the
[firmware issue tracker](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5442),
which is a stronger class of source than the forum for firmware behavior — it is
first-party, versioned and reproducible. Two owners report it. It is an open issue, so
it may be fixed, reclassified, or turn out to be something else; treat the section
above as current-as-of-writing rather than settled.

## Related

- [Probing fails or nozzle never touches the bed](loadcell-emi-noise.md) — the other
  sensor, frequently confused with this one
- [Assembly notes](../reference/assembly-notes.md) — if this is failing on a
  freshly built machine that has never calibrated successfully, check the build
  first: this is one of the two selftest failures that recur on new conversions
- [Who to contact](support-and-warranty-path.md) — getting the replacement part:
  diagnosis from Prusa, hardware from Bondtech, and open the case early enough that
  the date falls inside your warranty window.
