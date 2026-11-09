---
title:        Tool offset calibration fails: bed not aligned in Z
confidence:   provisional
updated:      2026-11-08
author:       hyiger
printer:      Core One
toolhead:     INDX
hotend:       unknown
nozzle:       unknown
firmware:     6.9.1-beta on the reported machine; the mechanism is not version-specific; the classifier, the uneven-bed check and the manual Z alignment source-checked through 8.0.0
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
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v7.0.0
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v8.0.0
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/lib/Marlin/Marlin/src/gcode/bedlevel/ubl/G29.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/src/marlin_stubs/G162.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/src/common/probe_analysis.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/compare/v6.9.2...v7.0.0
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/compare/v7.0.0...v8.0.0
  - https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/tool-offset-calibration-failing/
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
| [`36144`](../codes.md#stock-800) | Sensor Not Found (stock 8.0.0) |
| [`36193`](../codes.md#36193) | Probing the tool offset sensor failed |

Through 7.0.1 it is the same code as the
[offset sensor board fault](offset-sensor-board-failure.md).
The on-screen message tells you to check that the nozzle is clean. If you have done
that and nothing is loaded, this page is the next thing to rule out.

Firmware built from hyiger/Prusa-Firmware-Buddy reports a rejected touch on the sensor
as `36193` instead, so there this fault no longer shares a code with the sensor board.
Stock 8.0.0 separates them too: in its source a touch on the sensor that is still
rejected after the probe's retries ends on `36144` Sensor Not Found, from the menu or at
print start. Its text reads as if the sensor were missing or at the wrong height, and
asks you to check that it is fitted and seated, advice that does not fit this fault. The
board fault ends on `36145` or `36130`, see
[what stock 8.0.0 shows](../codes.md#stock-800). At print start, though, each tool of a
print that uses more than one first touches the sheet, and a touch rejected there still
ends on `36130`, the same code as the board fault, see [bed probing](../codes.md#36192).
That is a reading of the source; no owner has yet reported this fault on 8.0.0.

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
for each tool and then stops with the code above, on a screen with Retry and Abort.
Retry repeats only the tool that failed. That was already so before 8.0.0, which
changes the screen and its code for this fault, see above.

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
  [7.0.0](https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v7.0.0),
  published on Prusa's downloads page on 15 October 2026, lists automatic Z-axis
  alignment on an uneven bed among its new features, and its source, published on 3 November 2026, shows what that
  means. The trigger is the same check as before, during
  [bed leveling](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/lib/Marlin/Marlin/src/gcode/bedlevel/ubl/G29.cpp),
  with the same margin as in 6.9.2. What changed is the response. Instead of offering
  Z Alignment Calibration straight away, the printer now runs the alignment once by
  itself and levels the bed again; the offer appears only if that automatic run could
  not finish or the bed is still out of plane afterwards. The automatic run makes sure
  Z is homed, then gives up if the bed stops well short of the bottom, as it would
  against something in the way. Nothing else calls it: tool offset calibration still
  does not.
  So a carriage racked by less than the margin is still left alone, which the source
  now shows rather than this page inferring it. 8.0.0 carries the same code, and no
  owner has reported on the new behavior yet.

### What to do

1. **Run Z Alignment Calibration**, under Control, then Calibrations & tests. The
   procedure homes Z, drives the bed to the bottom of its travel and pushes a short
   distance past the hard stop, so that the Z drive skips against the frame until the
   carriage sits square. That is what resets the alignment. The owner described what
   they did as moving the bed to the bottom of the printer to reset the level, which
   is the step this procedure performs. Run it by hand on 7.0.0 and later too: the
   automatic alignment runs only after bed leveling has found the bed out of plane,
   which this fault need not reach.
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
    so far seemed to help every time. `provisional`, two owners on one issue. Two owners
    in the
    [tool offset thread](https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/tool-offset-calibration-failing/)
    have since switched the light off, one naming the bed light, and mention no other
    change made at the same time. One of them had this calibration and bed leveling run
    for the first time without dragging on or failing, the other had one print's bed
    leveling go cleanly; neither gives their firmware. That makes switching the light
    off, with no other change reported alongside it, `reported`, from two sources, as
    something that helped.

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
The source of 7.0.0, 7.0.1 and 8.0.0, published on 3 November 2026, allows the same
check for them.
[In 7.0.0](https://github.com/prusa3d/Prusa-Firmware-Buddy/compare/v6.9.2...v7.0.0) the
only change to the
[classifier](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/src/common/probe_analysis.cpp)
is that it no longer returns a best-effort height for a rejected touch, which nothing on
the INDX used, so it rejects the same touches. The
[alignment procedure](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/src/marlin_stubs/G162.cpp)
was reworked to add the automatic run described above; done by hand it still drives the
bed to the bottom and pushes past the stop. 7.0.1 changes neither file, and
[8.0.0](https://github.com/prusa3d/Prusa-Firmware-Buddy/compare/v7.0.0...v8.0.0)
changes neither those two nor the bed leveling check. The new 8.0.0 failure screens and
codes are from its
[detailed notes](https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v8.0.0)
and source; no owner has reported one for this fault. The status-light reports are
from one owner on stock 6.9.2 and a second who does not give their firmware, both on
[firmware issue 5526](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5526);
the first of them later summed up their complete fix on
[firmware issue 5518](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5518). Two
more owners, in the tool offset forum thread, report switching the light off and
mention no other change made at the same time.
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
