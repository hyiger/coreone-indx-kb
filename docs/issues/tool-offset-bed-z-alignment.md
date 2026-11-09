---
title:        Tool offset calibration fails: bed not aligned in Z
confidence:   provisional
updated:      2026-10-25
author:       hyiger
printer:      Core One
toolhead:     INDX
hotend:       unknown
nozzle:       unknown
firmware:     6.9.1-beta on the reported machine; the mechanism is not version-specific
sources:
  - https://help.prusa3d.com/article/tool-offset-failed-36130-core-one-indx_1089016
  - https://help.prusa3d.com/article/uneven-bed-31111-core-one-35111-core-one-l-36111-core-one-indx_856294
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1-beta/src/common/probe_analysis.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1-beta/src/marlin_stubs/G162.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/compare/v6.9.1-beta...v6.9.1
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/compare/v6.9.1...v6.9.2
  - https://help.prusa3d.com/downloads/core-one-indx
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5526
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5518
superseded_by:
---

# Tool offset calibration fails: bed not aligned in Z

## Summary

Tool offset calibration can fail with the same error code as a faulty offset sensor
board on a machine where the nozzle tips are clean, the sensor is clean and no
filament is loaded, because the bed is out of alignment in Z. One owner on 6.9.1-beta
had calibration fail on a different tool from one run to the next, and a ferrite core
on the toolhead cable changed nothing. The owner moved the bed to the bottom of its
travel to reset its level, which is what Z Alignment Calibration does, and the failure
went away. Z Alignment Calibration costs nothing and cannot make anything worse, so
run it before you suspect the sensor board or the loadcell.

## Error codes that lead here

| Code | What the printer shows |
|---|---|
| [`36130`](https://help.prusa3d.com/article/tool-offset-failed-36130-core-one-indx_1089016) | Tool offset failed |
| [`36193`](../codes.md#36193) | Probing the tool offset sensor failed |

It is the same code as the [offset sensor board fault](offset-sensor-board-failure.md).
The on-screen message tells you to check that the nozzle is clean. If you have done
that and nothing is loaded, this page is the next thing to rule out.

Firmware built from hyiger/Prusa-Firmware-Buddy reports a rejected touch on the sensor
as `36193` instead, so there this fault no longer shares a code with the sensor board.

## Detail

Tool offset calibration on the INDX takes two kinds of measurement. The contactless
sensor reads the nozzle position in X and Y without touching it. The Z measurement is
a physical touch: the bed rises until the nozzle rests on the sensor housing and the
loadcell registers contact. On the Core One every Z move is a bed move, so that touch
depends on the bed carriage traveling freely on its lead screws.

The firmware does not accept a touch on the strength of the contact alone. It holds
position briefly after contact and checks that the measured force stays steady. If
the force keeps changing while nothing is supposed to be moving, the sample is thrown
out. In the serial log that shows as a probe classified as not OK, naming the feature
`angle_after` with a negative value. The calibration retries a fixed number of times
for each tool and then stops with the code above.

A bed carriage whose sides are out of step binds slightly on its guides. When the
nozzle presses down on it, the binding carriage settles instead of holding still, so
the force at the nozzle eases off after contact. That is exactly the pattern the check
rejects. It also fits the failure moving between tools from one run to the next: each
tool makes contact at a slightly different bed height, and a racked carriage does not
bind the same way at every height.

What makes this fault easy to misread:

- **The nozzle is clean and nothing is loaded**, so the ooze explanation does not
  apply and the on-screen advice leads nowhere.
- **It looks like interference.** Failures that come and go, on different tools, on a
  machine that passes its loadcell selftest, are what a noise problem looks like from
  the outside, and on other machines noise has been the cause, see
  [loadcell noise](loadcell-emi-noise.md). The owner fitted a ferrite core on that
  theory. It made no difference. The tip below says how to tell the two apart.
- **It looks like a bad sensor board.** The sensor board page describes calibration
  failing part way through the tool sequence with the stopping point moving between
  attempts. This presents the same way. The difference is in the log: a sensor board
  fault gets no sample at all, while this fault gets samples and rejects them.
- **Nothing in the normal flow points at the bed.** The firmware offers Z Alignment
  Calibration on its own only when a bed leveling pass finds the surface out of plane
  by more than a fixed margin. A carriage that is racked by less than that prints
  acceptably and never triggers the offer, and tool offset calibration does not level
  the bed at all.
  [7.0.0](https://help.prusa3d.com/downloads/core-one-indx), published on 15 October
  2026, lists automatic Z-axis alignment on an uneven bed among its new features. Its
  notes do not say what triggers it, and its source is not yet published. If it takes
  the place of that offer, a carriage racked by less than the margin would presumably
  still be left alone. That is an inference. The notes for 7.0.1 and for 8.0.0,
  published on 19 and 22 October 2026, add nothing about it, and no owner has reported
  on the new behavior yet.

### What to do

1. **Run Z Alignment Calibration**, under Control, then Calibrations & tests. The
   procedure homes Z, drives the bed to the bottom of its travel and pushes a short
   distance past the hard stop, so that the Z drive skips against the frame until the
   carriage sits square. That is what resets the alignment. The owner described what
   they did as moving the bed to the bottom of the printer to reset the level, which
   is the step this procedure performs. Run it by hand on 7.0.0 and later too: nothing
   in their notes says the automatic alignment covers this case.
2. **Run tool offset calibration again.** On the reported machine the failure was gone
   afterwards.
3. **If it still fails**, the vendor's uneven bed article says to move the bed down,
   loosen the trapezoid nuts and check that they travel freely on the lead screws.
   After that, capture a serial log and go to the
   [sensor board page](offset-sensor-board-failure.md).

!!! tip "Telling them apart"
    Several faults share this error code, and the serial log separates three of them.
    No sample at all points at the [sensor board](offset-sensor-board-failure.md).
    Samples taken and rejected with `angle_after` mean something is giving way under
    the nozzle: filament on the tip, or the bed carriage. With the tips clean and
    nothing loaded, that leaves the carriage. Clean and unload before you read anything
    into the log, because [ooze](oozing-during-probing-and-calibration.md) is rejected
    the same way.
    [Noise on the loadcell](loadcell-emi-noise.md) gets touches rejected too, and this
    page has no log from stock firmware showing which check rejects them, so go by when
    and how it fails instead. In the reports on that page, noise fails the calibration
    at print start while it passes from the menu, and the nozzle can be seen stopping
    short. One owner on stock 6.9.2 ended the failures that rewiring had left by
    switching the bed's status light off from the menu
    ([firmware issue 5526](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5526)).
    Their latest summary, on
    [firmware issue 5518](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5518),
    credits their complete fix to the rewiring, ferrite cores on the cables of the bed
    and chamber lights and a lower probing temperature in the start G-code. Switching
    the light off is not on that list, though they think the bed light's cable was the
    likeliest source, so their result does not show that switching it off is needed. A
    second owner on issue
    5526, for whom ferrite beads did not help, reports that switching the light off has
    so far seemed to help every time. `provisional`, two owners on one issue.

## Verification

`provisional`: one machine, one owner, and the report reached the author directly
while helping with the diagnosis rather than through a public thread, so there is no
link for the report itself. What is on record: on 6.9.1-beta, tool offset calibration
failed repeatedly with the failing tool changing between runs, with clean nozzle tips,
a clean sensor board and no filament loaded. The log showed touches being taken and
rejected with `angle_after`. A ferrite core on the toolhead cable made no difference.
After the owner moved the bed to the bottom of its travel to reset its level, the
failure went away.

The mechanism above is the author's reading of the firmware's probe classifier against
that log. It fits, but it has not been confirmed by the vendor or reproduced on another
machine. The firmware references are the classifier in
[probe_analysis.cpp](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1-beta/src/common/probe_analysis.cpp)
and the alignment procedure in
[G162.cpp](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1-beta/src/marlin_stubs/G162.cpp),
both at the 6.9.1-beta tag. Neither file changed in the
[stable 6.9.1](https://github.com/prusa3d/Prusa-Firmware-Buddy/compare/v6.9.1-beta...v6.9.1)
or in [6.9.2](https://github.com/prusa3d/Prusa-Firmware-Buddy/compare/v6.9.1...v6.9.2),
which on the INDX changes only the filament presets, so the reading applies to both.
Prusa has not yet published the source of
[7.0.0](https://help.prusa3d.com/downloads/core-one-indx), 7.0.1 or 8.0.0, so whether
either file changed in them cannot be checked. The 7.0.0 notes list automatic Z-axis
alignment on an uneven bed and say nothing about tool offset calibration; the notes for
7.0.1 and 8.0.0 mention neither. The status-light reports are from one owner on stock
6.9.2 and a second who does not give their firmware, both on
[firmware issue 5526](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5526);
the first of them later summed up their complete fix on
[firmware issue 5518](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5518).
The opener of issue 5526 also logged which check rejected the touches, but on firmware
they had modified, so this page does not use it. What Z Alignment Calibration is for,
and the menu path, are from the vendor's
[uneven bed article](https://help.prusa3d.com/article/uneven-bed-31111-core-one-35111-core-one-l-36111-core-one-indx_856294).

If your machine matches this and Z alignment fixes it, that second report is what
moves this page to `reported`. See [contributing](../contributing.md).

## Related

- [Tool offset calibration fails: contactless offset sensor](offset-sensor-board-failure.md).
  Same error code. Go there if Z alignment changes nothing, and capture a log first.
- [Probing fails or nozzle never touches the bed](loadcell-emi-noise.md). The
  interference fault this one was mistaken for.
- [Oozing spoils bed probing and tool calibration](oozing-during-probing-and-calibration.md).
  The other reason a touch gets rejected. Rule it out by cleaning and unloading first.
