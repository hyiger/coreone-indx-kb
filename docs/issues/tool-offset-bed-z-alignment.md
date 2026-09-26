---
title:        Tool offset calibration fails: bed not aligned in Z
confidence:   provisional
updated:      2026-09-25
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
  the outside. The owner fitted a ferrite core on that theory. It made no difference.
- **It looks like a bad sensor board.** The sensor board page describes calibration
  failing part way through the tool sequence with the stopping point moving between
  attempts. This presents the same way. The difference is in the log: a sensor board
  fault gets no sample at all, while this fault gets samples and rejects them.
- **Nothing in the normal flow points at the bed.** The firmware offers Z Alignment
  Calibration on its own only when a bed leveling pass finds the surface out of plane
  by more than a fixed margin. A carriage that is racked by less than that prints
  acceptably and never triggers the offer, and tool offset calibration does not level
  the bed at all.

### What to do

1. **Run Z Alignment Calibration**, under Control, then Calibrations & tests. The
   procedure homes Z, drives the bed to the bottom of its travel and pushes a short
   distance past the hard stop, so that the Z drive skips against the frame until the
   carriage sits square. That is what resets the alignment. The owner described what
   they did as moving the bed to the bottom of the printer to reset the level, which
   is the step this procedure performs.
2. **Run tool offset calibration again.** On the reported machine the failure was gone
   afterwards.
3. **If it still fails**, the vendor's uneven bed article says to move the bed down,
   loosen the trapezoid nuts and check that they travel freely on the lead screws.
   After that, capture a serial log and go to the
   [sensor board page](offset-sensor-board-failure.md).

!!! tip "Telling the three apart from the serial log"
    Three faults share this error code, and the log separates them. No sample at all
    points at the [sensor board](offset-sensor-board-failure.md). Samples taken and
    rejected with `angle_after` mean something is giving way under the nozzle:
    filament on the tip, or the bed carriage. With the tips clean and nothing loaded,
    that leaves the carriage. Clean and unload before you read anything into the log,
    because [ooze](oozing-during-probing-and-calibration.md) is rejected the same way.

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
both at the 6.9.1-beta tag. What Z Alignment Calibration is for, and the menu path,
are from the vendor's
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
