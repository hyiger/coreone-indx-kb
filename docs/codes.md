---
title:        Tool offset calibration error codes
confidence:   provisional
updated:      2026-10-25
author:       hyiger
printer:      Core One, Core One L
toolhead:     INDX
hotend:       unknown
nozzle:       unknown
firmware:     stock firmware reports all of these as 36130 through 6.9.2 (source-checked); 7.0.0 still shows 36130 for at least the 36193 failure (one report); 7.0.1 and 8.0.0 unknown; the 3619x codes need firmware built from hyiger/Prusa-Firmware-Buddy
sources:
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/src/feature/tool_offset_calibration/tool_offset_calibration.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/lib/Marlin/Marlin/src/feature/contactless_offset/contactless_offset.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5482
  - https://github.com/hyiger/Prusa-Firmware-Buddy/blob/master/lib/Prusa-Error-Codes/yaml/buddy-error-codes.yaml
  - https://help.prusa3d.com/article/tool-offset-failed-36130-core-one-indx_1089016
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/lib/Prusa-Error-Codes/yaml/buddy-error-codes.yaml
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.6.3/src/feature/tool_offset_calibration/tool_offset_calibration.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5500
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.9.1-beta
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.9.2
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/compare/v6.9.1...v6.9.2
  - https://help.prusa3d.com/downloads/core-one-indx
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5548
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5526
  - https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/tool-offset-calibration-failing/
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5518
  - https://github.com/prusa3d/Prusa-Error-Codes/blob/9e609385d1c18cc080bcfaaf2bd1d6a7cd7cf5ad/yaml/buddy-error-codes.yaml
  - https://github.com/prusa3d/Prusa-Error-Codes/commit/a88544c7628067f03c768a26624000c463e971b6
  - https://github.com/prusa3d/Prusa-Error-Codes/commit/8a502d03acc0c5bf3ba524d68c6e10bd4c8d1acf
  - https://github.com/prusa3d/Prusa-Error-Codes/commit/bc278daf0a10e6657048416623a9e2e7f7845643
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

For the failures on this page, stock firmware only ever shows 36130, but the
[serial log](#stock-firmware) still says which of these it was. That is checked against
the source up to 6.9.2, the last release whose source is published. Between
21 September and 5 October 2026, before 6.9.2 came out, Prusa added codes of its own
for some of these failures to its public error code list, and 6.9.2 still shows only
36130. A code being on that list does not mean a release shows it. One report on 7.0.0
still shows 36130 for the failure under 36193. Whether 7.0.0 shows any of Prusa's new
codes, or a later release does, is not known; see the verification section at the end
of this page.

On the Core One L the codes start with 37 instead of 36: 37130, and 37190 to 37197.
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

After the last tool, the printer compares the tools' offsets with one another, and
stops if the Z offsets, the XY offsets or the sensor position they imply are out of
line. Stock firmware gives those checks codes of their own: 36131 Unsafe Z Tool Offset,
36133 Unsafe XY Tool Offset and 36134 Unsafe Sensor Position, or 37131, 37133 and 37134
on the Core One L. This page does not cover them. Retry on them starts over from the
first tool.

**Which tool is on the head.** In the stock source, every calibration failure screen
first parks the head at the front, with the nozzle within reach. A failure during one
tool's steps comes up with that tool still on the head, unless the failure is that the
printer is unsure which tool it holds (36130 on stock firmware, 36190 with the split
codes). The comparison checks come after the last tool, so
the tool on the head is then the last one measured, which need not be the one whose
offset was out of line. One owner on stock 6.9.1 reports the screen coming up with a
clean tool on the head while the tool calibrated before it was the one carrying
material, and says earlier firmware presented the dirty tool
([firmware issue 5500](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5500)).
The report gives no code. The owner calls it a Z offset error, and if it was 36131 the
order above would explain it. So would material the earlier tool left on the sensor
board, where each tool touches down. Neither reading has been confirmed.

The order of the steps and checks is the same in the
[6.6.3 source](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.6.3/src/feature/tool_offset_calibration/tool_offset_calibration.cpp).
One documented change does bear on the report. Since
[6.9.1-beta](https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.9.1-beta),
the release notes say, calibration makes up to 10 attempts at its Z probing instead
of 3. In the
[6.9.1 source](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/lib/Marlin/Marlin/src/feature/contactless_offset/contactless_offset.cpp)
that is the touch on the sensor board. The touches on the sheet, which give the Z
offsets, are not part of that change, and the extra attempts only try again: a touch
the probe rejects is still not accepted. A tool with material on it therefore gets
more chances at an accepted touch on the sensor board, and so at finishing its own
steps, where before it was likelier to run out of attempts and stop on its own screen.
If the material had also thrown off its touch on the sheet, that would then show only
in the Z comparison, with the last tool measured on the head. That is a reading of
the source, not a confirmed cause. If a screen leaves you looking at a clean tool,
check the tools measured before it too.

## 36130 · 37130 · Tool offset failed {#36130}

<span id="37130"></span>

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

## 36190 · 37190 · Tool not picked {#36190}

<span id="37190"></span>

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

## 36191 · 37191 · Nozzle cleaning failed {#36191}

<span id="37191"></span>

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

## 36192 · 37192 · Bed probing failed {#36192}

<span id="37192"></span>

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
   [loadcell noise](issues/loadcell-emi-noise.md), and the two noise sources owners
   have reported for this calibration under [36193](#36193).

## 36193 · 37193 · Sensor probing failed {#36193}

<span id="37193"></span>

**What failed.** The touch on the sensor board, which finds the height of the sensor
surface before the sweeps, was not accepted, even after the probe's own retries.

**What to do.**

1. Clean the nozzle tip and the sensor board.
2. Keep the door closed, for the same reason as under [36192](#36192).
3. If both are clean and nothing is loaded, run Z Alignment Calibration. This is the
   failure described on [bed not aligned in Z](issues/tool-offset-bed-z-alignment.md).
4. If the nozzle stops short of the sensor, or this passes from the calibration menu
   but fails once a print starts, see [loadcell noise](issues/loadcell-emi-noise.md).
   Owners have reported two noise sources for this calibration. One is the extruder
   motor. An owner on 7.0.0 logged this failure at print start and measured much more
   noise on the loadcell with that motor energized, though not during the failing
   touch itself, and found that switching its driver off before the probe made the
   failures rare, a workaround rather than a fix
   ([firmware issue 5548](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5548)).
   A second owner on that issue had the probing pass first time with the same change,
   after several failures; that is one attempt.
   A separate report on 6.9.1 traces noise in the loadcell self-test after a toolchange
   to the same motor being left on
   ([firmware issue 5518](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5518)).
   The other is the bed's status light, which one owner describes as lit during a print
   and not during a calibration from the menu. On stock firmware, one owner who switched
   it off from the menu, and another who also fitted ferrite beads, report that their
   failures stopped
   ([firmware issue 5526](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5526),
   [tool offset thread](https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/tool-offset-calibration-failing/)).
   The first of them has since summed up on
   [firmware issue 5518](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5518)
   what fixed their printer completely: twisting the supply wires in the head's harness,
   ferrite cores on the cables of the bed and chamber lights, and a lower probing
   temperature in the start G-code. Switching the light off is not on that list, though
   they think the bed light's cable was the likeliest source, so their result does not
   show that switching it off is needed.
   A third, on firmware issue 5526, found that ferrite beads did not help and that
   switching the light off has so far seemed to help every time. The opener of
   firmware issue 5548 has since said that their start now switches the light off as
   well as the motor, and that this has been very reliable so far
   ([firmware issue 5518](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5518));
   that result does not separate the two sources.

## 36194 · 37194 · No offset sensor data {#36194}

<span id="37194"></span>

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

## 36195 · 37195 · Toolhead board restarted {#36195}

<span id="37195"></span>

**What failed.** While sweeping, the firmware watches the INDX head board's restart
counter. A board that restarts mid-scan spoils every reading after it, so the scan is
abandoned.

**What to do.**

1. Check that the toolhead cable is fully seated at both ends, and look along its path
   for strain or damage.
2. Press Retry.
3. If it happens again, capture a serial log and contact support, see
   [who to contact](issues/support-and-warranty-path.md).

## 36196 · 37196 · Nozzle too hot {#36196}

<span id="37196"></span>

**What failed.** The sweeps need the nozzle below a probing temperature limit that is
fixed in firmware. Before sweeping, the printer lowers the nozzle target and waits for
it to cool, running the print fan to help. The wait gives up when the temperature
stops falling, and here it gave up with the nozzle still above the limit.

**What to do.**

1. Check that the print fan spins.
2. Let the nozzle cool, then press Retry.

## 36197 · 37197 · Homing failed {#36197}

<span id="37197"></span>

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
is only as reliable as the reading of the source, which is linked above. The codes and
titles of the comparison checks are from the stock
[error code list](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/lib/Prusa-Error-Codes/yaml/buddy-error-codes.yaml)
at the same tag. The report of a clean tool on the head is a single owner's. Two more
owners have since said on the same issue that they see the same, without saying which
part, and the vendor has not replied. The attempt counts are from the 6.9.1-beta
release notes, and which touch they apply to is read from the source at the 6.9.1 tag.
Of the two noise sources under 36193, the extruder motor rests on one owner's
measurements for this calibration and a second owner's single attempt, both on firmware
issue 5548. The first of them now switches the status light off too, so their latest
result, which they call very reliable so far, does not isolate the motor. Separately,
firmware issue 5518 reports the same motor upsetting the loadcell self-test; its opener
suspects, but has not shown, a link to failures at print start. The status light rests
on two owners on stock firmware, on firmware issue 5526 and in a forum thread, who
report that switching it off, alone or together with ferrite beads, ended their
failures, and on a third on the issue, who does not give their firmware and found
ferrite beads alone did not help. The first of those two has since credited their
complete fix, on firmware issue 5518, to rewiring, ferrite cores on the light cables
and a lower probing temperature, without listing switching the light off, though they
think the bed light's cable was the likeliest source, so their result does not show
that switching it off is needed.
The opener of firmware issue 5526 tested the light on firmware they had
modified, which this page does not rely on.

What to do about each code is the author's reading of those checks. Where a section
sends you to another page, that page's own tier applies. The rest has not been tested
on hardware, and no owner has reported the split codes yet. If one of these screens
led you to a fix, or a step here did nothing, that report is what moves this page up a
tier. See [contributing](contributing.md).

The split codes exist only in firmware built from the fork. Reporting the failing step
instead of one generic dialog was proposed upstream in
[firmware issue 5482](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5482). A
Prusa developer replied on 23 September 2026 that the vendor is already working on it,
with no delivery date. It is not in
[6.9.2](https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.9.2), released
on 7 October 2026, which on the INDX
[changes only](https://github.com/prusa3d/Prusa-Firmware-Buddy/compare/v6.9.1...v6.9.2)
the filament presets: stock 6.9.2 still shows 36130 for every failure on this page, and
logs the same lines as 6.9.1.
[7.0.0](https://help.prusa3d.com/downloads/core-one-indx), published on Prusa's
downloads page on 15 October 2026, does not list it either: its notes say nothing about
tool offset calibration errors. Its source is not yet published, so its log lines cannot be checked
against this page. One owner on 7.0.0 reports the 36130 screen together with the log
line this page maps to 36193
([firmware issue 5548](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5548)),
so for that failure at least, both are unchanged. Neither 7.0.1, published on
19 October 2026 with a single fix for a startup hang, nor 8.0.0, published on
22 October 2026, lists it. The 8.0.0 notes do change error screens in general, taking
off the printer's hash and the signature markers and making the QR code simpler, but
say nothing about tool offset calibration errors. Whatever stock firmware ends up
showing need not match the codes on this page.

Prusa's own codes for some of these failures are already in its public
[error code list](https://github.com/prusa3d/Prusa-Error-Codes/blob/9e609385d1c18cc080bcfaaf2bd1d6a7cd7cf5ad/yaml/buddy-error-codes.yaml).
Two were added on 21 September 2026
([commit](https://github.com/prusa3d/Prusa-Error-Codes/commit/a88544c7628067f03c768a26624000c463e971b6))
and marked approved on 2 October
([commit](https://github.com/prusa3d/Prusa-Error-Codes/commit/8a502d03acc0c5bf3ba524d68c6e10bd4c8d1acf)):
36144 Sensor Not Found, for the offset sensor not being found at the height the printer
expects, and 36145 Sensor Failure, for the sensor going silent during the measurement.
A third, 36146 Tool Not Picked, followed on 5 October
([commit](https://github.com/prusa3d/Prusa-Error-Codes/commit/bc278daf0a10e6657048416623a9e2e7f7845643))
and is not yet marked approved. Its commit describes it as a tool pickup failed report
that leaves the motors on, so it may be a general pickup check rather than one specific
to this calibration. All three were added before 6.9.2 was released on 7 October, and
6.9.2 does not show them. On the Core One L they are 37144, 37145 and 37146. The
September change also rewords 36134 Unsafe Sensor Position: instead of asking for a
clean nozzle and sensor, it now says the sensor may have been knocked out of place.
Going by their descriptions alone, 36144 is closest to 36193 on this page, 36145 to
36194 and 36146 to 36190, but which checks raise them cannot be read until the source is
published. The notes for 7.0.0, 7.0.1 and 8.0.0 do not mention them, and no owner has
reported seeing one, so which release shows them, if any does yet, is not known.

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
