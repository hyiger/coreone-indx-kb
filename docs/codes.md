---
title:        Tool offset calibration error codes
confidence:   provisional
updated:      2026-09-25
author:       hyiger
printer:      Core One, Core One L
toolhead:     INDX
hotend:       unknown
nozzle:       unknown
firmware:     stock firmware reports all of these as 36130; the 3619x codes need firmware built from hyiger/Prusa-Firmware-Buddy
sources:
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/src/feature/tool_offset_calibration/tool_offset_calibration.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/lib/Marlin/Marlin/src/feature/contactless_offset/contactless_offset.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5482
  - https://github.com/hyiger/Prusa-Firmware-Buddy/blob/master/lib/Prusa-Error-Codes/yaml/buddy-error-codes.yaml
  - https://help.prusa3d.com/article/tool-offset-failed-36130-core-one-indx_1089016
superseded_by:
---

# Tool offset calibration error codes

## Summary

Stock firmware shows one screen, 36130, for eleven different ways tool offset
calibration can fail, and that screen always tells you to clean the nozzle and the
sensor. Firmware built from
[hyiger/Prusa-Firmware-Buddy](https://github.com/hyiger/Prusa-Firmware-Buddy) splits
the eleven into nine screens. 36130 keeps the one failure its message fits, the sensor
sweep not finding the nozzle, and 36190 to 36197 name the rest. The QR code on each of
those screens opens its section on this page.

On stock firmware you only ever see 36130, but the [serial log](#stock-firmware) still
says which of these it was.

On the Core One L the codes start with 35 instead of 36: 35130, and 35190 to 35197.
Each section below covers both.

| Code | The screen starts with | What failed |
|---|---|---|
| [36130](#36130) | Tool offset calibration failed | The sensor sweeps ran, but did not locate the nozzle |
| [36190](#36190) | The tool is not detected as picked | The printer does not consider the tool picked |
| [36191](#36191) | Nozzle cleaning before tool offset calibration failed | A cleaning sequence did not finish |
| [36192](#36192) | Probing the bed for tool offset calibration failed | A touch on the sheet was rejected |
| [36193](#36193) | Probing the tool offset sensor failed | The touch on the sensor board was rejected |
| [36194](#36194) | The tool offset sensor sent no usable data | No sweep produced sensor data that could be analyzed |
| [36195](#36195) | The toolhead board restarted | The INDX head board restarted during the sweeps |
| [36196](#36196) | The nozzle did not cool down enough | The nozzle stayed above the probing temperature limit |
| [36197](#36197) | Homing failed during tool offset calibration | Homing before the measurement failed |

## How the calibration runs

It helps to know the order of the steps, because each code is one of them failing.

At the start of a print, the printer works through the tools the print uses, one at a
time. It picks the tool and cleans it in the nozzle cleaner. A print that uses a
single tool stops there, because there is no offset between tools to measure.
Otherwise the tool touches the sheet at a point on a line near its front edge, the
first tool touching both ends of that line, and the differences between those touches
give the tools' Z offsets. From the calibration menu there is no cleaning and no touch
on the sheet: you clean the nozzles yourself, and the Z offsets are left for the next
print to measure.

Last, the tool is measured over the offset sensor. The nozzle touches down on the
sensor board just beside the coil, to find the height of the sensor surface. It is
then swept back and forth over the coil, along X and along Y, at two speeds. The
sensor reading peaks as the tip passes over the coil, and the firmware works out the
nozzle position from where the peaks fall. Each sweep gets a confidence score, and
both axes need a confident sweep. The firmware retries each axis a limited number of
times, and when a sweep along Y finds nothing it shifts the sweep sideways and tries
again.

Retry on a failed measurement over the sensor cleans the tool again and measures it
again. Retry on the other screens starts over from the first tool. Abort stops the
print, or ends the calibration from the menu.

## 36130 · 35130 · Tool offset failed {#36130}

<span id="35130"></span>

**What failed.** The sweeps ran, and the sensor delivered data, but no sweep located
the nozzle with enough confidence. Something is spoiling the sensor's view of the
nozzle tip. This is the case the on-screen advice was written for, and the QR code on
this screen still goes to Prusa's own article.

**What to do.**

1. Clean the nozzle tip, then the sensor window. How to clean the window, and what not
   to use on it, is on [oozing during probing](issues/oozing-during-probing-and-calibration.md).
2. Unload the filament from the tool so that nothing oozes during the measurement.
   [Prusa's article for this code](https://help.prusa3d.com/article/tool-offset-failed-36130-core-one-indx_1089016)
   gives the same advice.
3. Check that the sensor board sits flat and secure. The sweeps search a limited area
   around where the sensor is expected, so a board that has shifted can leave the coil
   outside it. That is a reading of the firmware, not a reported case.
4. If it still fails, go to [contactless offset sensor](issues/offset-sensor-board-failure.md).

On stock firmware, 36130 can be any of the codes below.

## 36190 · 35190 · Tool not picked {#36190}

<span id="35190"></span>

**What failed.** Before cleaning and measuring a tool, the firmware checks that the
tool it has just picked is the one it considers selected. The measurement also needs
the tool's nozzle temperature, which the INDX head can only read from a tool it has
picked. One of those checks failed: the tool change reported success, but the printer
does not consider the tool picked.

**What to do.**

1. Look at the head. If the tool is not on it, or not seated, press Abort, put the
   tool back in its dock, pick it with Control > Pick/Park Tool, and start again.
2. If the tool is on the head and seated, the head is misreading it. See
   [phantom tools and park failures](issues/tool-detection-ringdown-decay.md).

## 36191 · 35191 · Nozzle cleaning failed {#36191}

<span id="35191"></span>

**What failed.** One of the cleaning sequences before the measurement did not finish:
ejecting the last blob, purging and wiping, or the final clean at the probing
temperature. The firmware abandons a sequence when its motion is stopped part-way;
the screen does not say what stopped it. An aborted print never shows this screen, and
neither does the calibration menu, which does not clean.

**What to do.**

1. Check the nozzle cleaner and the waste bin for anything that could block the head:
   a full bin, or a pellet or strand caught in the wiper.
2. Press Retry.
3. If cleaning keeps failing, see [wiper, purge and blobs](issues/stringing-and-wiper-calibration.md)
   for how the cleaner is calibrated.

## 36192 · 35192 · Bed probing failed {#36192}

<span id="35192"></span>

**What failed.** One of the touches on the sheet was not accepted, even after the
probe's own retries. This only happens at the start of a print that uses more than
one tool.

**What to do.**

1. Clean the nozzle tip and the front edge of the sheet. Material on the tip is the
   usual reason a touch is rejected, see
   [oozing during probing](issues/oozing-during-probing-and-calibration.md).
2. Keep the door closed. With the Door Sensor setting on, opening the door while the
   printer probes stops the move, and the interrupted touch counts as failed.
3. If the tip and the sheet are clean, run Z Alignment Calibration. A bed carriage
   that binds gets touches on the sensor rejected, see
   [bed not aligned in Z](issues/tool-offset-bed-z-alignment.md); a touch on the sheet
   is presumably rejected the same way, but no one has reported that yet.
4. If the nozzle stops short of the sheet where you can see the gap, see
   [loadcell noise](issues/loadcell-emi-noise.md).

## 36193 · 35193 · Sensor probing failed {#36193}

<span id="35193"></span>

**What failed.** The touch on the sensor board, which finds the height of the sensor
surface before the sweeps, was not accepted, even after the probe's own retries.

**What to do.**

1. Clean the nozzle tip and the sensor board.
2. Keep the door closed, for the same reason as under [36192](#36192).
3. If both are clean and nothing is loaded, run Z Alignment Calibration. This is the
   failure described on [bed not aligned in Z](issues/tool-offset-bed-z-alignment.md).
4. If the nozzle stops short of the sensor, see [loadcell noise](issues/loadcell-emi-noise.md).

## 36194 · 35194 · No offset sensor data {#36194}

<span id="35194"></span>

**What failed.** The printer records the sensor's readings during every sweep, and a
sweep only counts if that recording can be analyzed: the sensor has to start
streaming, report no fault, drop no samples and deliver enough of them. Not one sweep
in the whole search produced a recording that could be analyzed. The sensor, its
board or its link to the printer is not delivering data.

If the sensor delivers data only some of the time, the printer shows 36130 instead,
so a link that drops out now and then can still look like a dirty nozzle.

**What to do.** This is the fault on
[contactless offset sensor](issues/offset-sensor-board-failure.md): check the cable
and its connectors, capture a serial log, and check the LED on the sensor board. The
log names the reason each sweep failed, see [below](#stock-firmware).

## 36195 · 35195 · Toolhead board restarted {#36195}

<span id="35195"></span>

**What failed.** While sweeping, the firmware watches the INDX head board's restart
counter. A board that restarts mid-scan spoils every reading after it, so the scan is
abandoned.

**What to do.**

1. Check that the toolhead cable is fully seated at both ends, and look along its path
   for strain or damage.
2. Press Retry.
3. If it happens again, capture a serial log and contact support, see
   [who to contact](issues/support-and-warranty-path.md).

## 36196 · 35196 · Nozzle too hot {#36196}

<span id="35196"></span>

**What failed.** The sweeps need the nozzle below a probing temperature limit that is
fixed in firmware. Before sweeping, the printer lowers the nozzle target and waits for
it to cool, running the print fan to help. The wait gives up when the temperature
stops falling, and here it gave up with the nozzle still above the limit.

**What to do.**

1. Check that the print fan spins.
2. Let the nozzle cool, then press Retry.

## 36197 · 35197 · Homing failed {#36197}

<span id="35197"></span>

**What failed.** Each measurement starts by homing any axis that needs it, and homing
failed. A failed homing usually stops the printer with its own homing error first.
During a print, crash recovery can handle a homing failure instead, which is how this
screen can appear.

**What to do.** Check that nothing blocks the bed or the head, then press Retry. If
homing keeps failing, follow Prusa's article for the axis: the ones the printer's own
homing error screens link, for [Z](https://prusa.io/36301), [X](https://prusa.io/36304)
and [Y](https://prusa.io/36305).

## Telling them apart on stock firmware {#stock-firmware}

Stock firmware shows 36130 for all of these, and so does this firmware on printers
other than the INDX. The serial log says which one it was: the line logged just before
the dialog appears. How to capture the log is on
[contactless offset sensor](issues/offset-sensor-board-failure.md).

| The log says | Code on this firmware |
|---|---|
| `is not the selected tool, cannot clean` | [36190](#36190) |
| `Measurement failed: Nozzle has no valid temperature` | [36190](#36190) |
| `cleaning failed (step` or `Nozzle cleaning failed`, with no line about the selected tool before it | [36191](#36191) |
| `Z probe failed for tool` or `Z probe failed at reference-line end` | [36192](#36192) |
| `Measurement failed: Initial probing failed, sensor Z is NaN` | [36193](#36193) |
| `INDX puppy reset during XY scan; aborting FSM` | [36195](#36195) |
| `Measurement failed: Nozzle too hot for probing` | [36196](#36196) |
| `Measurement failed: Homing failed` | [36197](#36197) |
| `Measurement failed: Tool offset FSM finished without high confidence in both axes`, or `exceeded iteration limit` | [36130](#36130), or [36194](#36194) if every sweep before it failed |

A failed sweep logs `scan 'nozzle-offset-x' failed:` or `scan 'nozzle-offset-y' failed:`
followed by the reason. The reasons that mean the sensor delivered nothing usable are
`Failed to get first sensor sample`, `Sensor reported hardware failure`,
`Sensor samples overflow` and `Insufficient samples for analysis`. On this firmware,
when every sweep failed like that, the last line reads
`Measurement failed: Tool offset FSM got no analyzable sensor data` instead.

## Verification

`provisional`. What each code means is read from the firmware source: each section
names a check the firmware makes and the code this firmware shows when that check
fails, and the log lines are taken from the stock source at the 6.9.1 tag. That part
is only as reliable as the reading of the source, which is linked above.

What to do about each code is the author's reading of those checks. Where a section
sends you to another page, that page's own tier applies. The rest has not been tested
on hardware, and no owner has reported the split codes yet. If one of these screens
led you to a fix, or a step here did nothing, that report is what moves this page up a
tier. See [contributing](contributing.md).

The split codes exist only in firmware built from the fork. Reporting the failing step
instead of one generic dialog was proposed upstream in
[firmware issue 5482](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5482). A
Prusa developer replied on 23 September 2026 that the vendor is already working on it,
with no delivery date. Whatever stock firmware ends up showing need not match the codes
on this page.

## Related

- [Contactless offset sensor](issues/offset-sensor-board-failure.md): 36194, and 36130
  when cleaning has not helped
- [Bed not aligned in Z](issues/tool-offset-bed-z-alignment.md): 36193, and possibly
  36192
- [Oozing during probing](issues/oozing-during-probing-and-calibration.md): 36130,
  36192 and 36193
- [Phantom tools and park failures](issues/tool-detection-ringdown-decay.md): 36190
- [Wiper, purge and blobs](issues/stringing-and-wiper-calibration.md): 36191
- [Loadcell noise](issues/loadcell-emi-noise.md): 36192 and 36193
- [Who to contact](issues/support-and-warranty-path.md): 36194 and 36195
