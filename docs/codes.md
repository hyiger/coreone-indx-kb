---
title:        Tool offset calibration error codes
confidence:   provisional
updated:      2026-11-08
author:       hyiger
printer:      Core One, Core One L
toolhead:     INDX
hotend:       unknown
nozzle:       unknown
firmware:     stock firmware reports all of these as 36130 through 7.0.1 (source-checked); stock 8.0.0 splits them over 36130, 36144, 36145 and 36146 (source-checked, not yet reported on hardware); the 3619x codes need firmware built from hyiger/Prusa-Firmware-Buddy
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
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v7.0.0
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v7.0.1
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v8.0.0
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/compare/v6.9.2...v7.0.1
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/compare/v6.9.2...v8.0.0
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/src/feature/tool_offset_calibration/tool_offset_calibration.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/lib/Marlin/Marlin/src/feature/contactless_offset/contactless_offset.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/src/common/tool_offset_failure_reason.hpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/src/common/marlin_server_types/fsm/tool_offsets_calibration_mapper.hpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/src/feature/tool_offset_wizard/screen_tool_offset_wizard.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/src/module/contactless_offset/src/contactless_offset/can_remote_sensor.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/lib/Prusa-Error-Codes/yaml/buddy-error-codes.yaml
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/8-0-0-firmware-for-prusa-core-one-gen-2-indx-core-one-indx/
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5577
superseded_by:
---

# Tool offset calibration error codes

## Summary

Through 7.0.1, stock firmware shows one screen, 36130, for eleven different ways tool
offset calibration can fail, and that screen always tells you to clean the nozzle and
the sensor. Stock 8.0.0 adds three codes of its own for some of them, 36144 Sensor Not
Found, 36145 Sensor Failure and 36146 Tool Not Picked, and leaves the rest on 36130,
which now names the affected tool; see [what stock 8.0.0 shows](#stock-800).
Firmware built from
[hyiger/Prusa-Firmware-Buddy](https://github.com/hyiger/Prusa-Firmware-Buddy) splits
the eleven into nine screens. 36130 keeps the one failure its message fits, the sensor
sweep not finding the nozzle, and 36190 to 36197 name the rest. The QR code on each of
those screens opens its section on this page. The fork's split predates the 8.0.0
release and is not the one 8.0.0 adopted. The sections below are organized by the
fork's codes, and each says what stock firmware shows for that failure.

On every stock release, the [serial log](#stock-firmware) still says which of these
failures it was. Prusa published the source of 7.0.0, 7.0.1 and 8.0.0 on
3 November 2026. Up to and including 7.0.1, every failure on this page shows 36130 and
logs the same lines as 6.9.2. 8.0.0 changes both the screens and the log lines. Prusa
added its new codes to its public error code list between 21 September and
5 October 2026, before 6.9.2 came out, but only 8.0.0 shows them. No owner has
reported one of the new screens yet.

On the Core One L the codes start with 37 instead of 36: 37130, 37144 to 37146, and
37190 to 37197. Each section below covers both.

| Code | The screen starts with | What failed | Stock 8.0.0 shows |
|---|---|---|---|
| [36130](#36130) | Tool offset calibration failed | The sensor sweeps ran, but did not locate the nozzle | 36130, or 36145 if a sweep failed on a fault the sensor flagged |
| [36190](#36190) | The tool is not detected as picked | The printer does not consider the tool picked | 36146, or 36130 for the temperature check |
| [36191](#36191) | Nozzle cleaning before tool offset calibration failed | A cleaning sequence did not finish | 36130 |
| [36192](#36192) | Probing the bed for tool offset calibration failed | A touch on the sheet was rejected | 36130 |
| [36193](#36193) | Probing the tool offset sensor failed | The touch on the sensor board was rejected | 36144 |
| [36194](#36194) | The tool offset sensor sent no usable data | No sweep produced sensor data that could be analyzed | 36145 if the sensor flagged a fault, otherwise 36130 |
| [36195](#36195) | The toolhead board restarted | The INDX head board restarted during the sweeps | 36145 |
| [36196](#36196) | The nozzle did not cool down enough | The nozzle stayed above the probing temperature limit | 36130 |
| [36197](#36197) | Homing failed during tool offset calibration | Homing before the measurement failed | 36130, when a screen comes up at all |

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

Through 7.0.1, Retry on a failed measurement over the sensor cleans the tool again and
measures it again. Retry on the other screens starts over from the first tool. From
8.0.0, Retry on any failure in one tool's steps asks for that tool again, which picks it
only if the printer no longer considers it selected, then cleans it again during a print
and measures that tool only; the tools already measured keep their results
([8.0.0 source](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/src/feature/tool_offset_calibration/tool_offset_calibration.cpp)).
Abort stops the print, or ends the calibration from the menu. No release retries on
its own: the printer waits at the screen until you choose. One owner has asked for an
automatic clean and retry instead
([firmware issue 5577](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5577),
open).

After the last tool, the printer compares the tools' offsets with one another, and
stops if the Z offsets, the XY offsets or the sensor position they imply are out of
line. Stock firmware gives those checks codes of their own: 36131 Unsafe Z Tool Offset,
36133 Unsafe XY Tool Offset and 36134 Unsafe Sensor Position, or 37131, 37133 and 37134
on the Core One L. This page does not cover them. Retry on them starts over from the
first tool, on 8.0.0 as before.

**Which tool is on the head.** In the stock source, every calibration failure screen
first parks the head at the front, with the nozzle within reach. A failure during one
tool's steps comes up with that tool still on the head, unless the failure is that the
printer is unsure which tool it holds (36130 on stock firmware through 7.0.1, 36146 on
8.0.0, 36190 with the fork's codes). The comparison checks come after the last tool, so
the tool on the head is then the last one measured, which need not be the one whose
offset was out of line. One owner on stock 6.9.1 reports the screen coming up with a
clean tool on the head while the tool calibrated before it was the one carrying
material, and says earlier firmware presented the dirty tool
([firmware issue 5500](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5500)).
The report gives no code. The owner calls it a Z offset error, and if it was 36131 the
order above would explain it. So would material the earlier tool left on the sensor
board, where each tool touches down. Neither reading has been confirmed.

From 8.0.0 the screen says which tool to look at, with limits. In the source, 36130
and 36146 name the tool whose step failed. The 36131 and 36133 screens name the tool
that lies furthest out, the one whose removal would narrow the spread the most, but
only when at least three tools were measured; with two there is no majority to measure
against, and no tool is named. 36134, 36144 and 36145 name no tool
([screen definitions](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/src/feature/tool_offset_wizard/screen_tool_offset_wizard.cpp)).
The 8.0.0 release notes say every failure screen, unsafe measurements included, shows
the affected tool. In the source that holds for 36130 and 36146; 36131 and 36133 name
a tool only with three or more tools measured, and 36134, 36144 and 36145 name none.
The tool on the head after a comparison check is still the last one measured. A 36131
on 8.0.0 in a print with three or more tools would name the outlier, but no owner has
reported one yet.

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

## What stock 8.0.0 shows {#stock-800}

From 8.0.0, a failure in one tool's steps ends on one of four screens, each with Retry
and Abort. Which failure gets which screen is decided in one place in the
[calibration source](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/src/feature/tool_offset_calibration/tool_offset_calibration.cpp),
from the
[failure reasons](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/src/common/tool_offset_failure_reason.hpp)
the measurement reports, and the codes come from the
[screen-to-code mapping](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/src/common/marlin_server_types/fsm/tool_offsets_calibration_mapper.hpp)
and the
[error code list](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/lib/Prusa-Error-Codes/yaml/buddy-error-codes.yaml)
at the 8.0.0 tag. On the Core One L, read 37 for 36.

| Code | Title | Shown when | What to do |
|---|---|---|---|
| 36130 | Tool Offset Failed | A cleaning sequence did not finish, a touch on the sheet was rejected, the nozzle stayed too hot or reported no temperature, homing failed, or the sweeps ran without locating the nozzle | The log says which; see [below](#stock-firmware) |
| 36144 | Sensor Not Found | The touch on the sensor board was rejected | [36193](#36193) |
| 36145 | Sensor Failure | The head board restarted during the sweeps, or the sweeps gave up after at least one of them failed on a fault the sensor itself flagged | [36195](#36195) or [36194](#36194), even if the sensor flagged a fault in only some of the sweeps |
| 36146 | Tool Not Picked | The tool about to be cleaned or measured is not the one the printer considers selected | [36190](#36190) |

The 36130 text still asks for a clean nozzle and sensor, though on 8.0.0 that screen
also covers cleaning, sheet probing, temperature and homing failures. The 36145 text
blames the sensor or its cable, which does not fit a head board restart; the log tells
the two apart.

Three points in the source are worth knowing, all of them readings rather than
observed outcomes:

- A failed sweep counts against the sensor only when the sensor flagged a fault or
  dropped samples during it. A sweep that times out waiting for its first sample with
  no such flag, or gets too few samples to analyze, does not. A sensor that sends
  nothing at all would therefore end on 36130, not 36145
  ([measurement source](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/lib/Marlin/Marlin/src/feature/contactless_offset/contactless_offset.cpp),
  [sensor link](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/src/module/contactless_offset/src/contactless_offset/can_remote_sensor.cpp)).
- The list describes 36144 as the sensor not being found at the expected height. The
  check for a touch far below the sensor surface is on the XL's two-coil path only, so
  on the INDX the rejected touch is the only thing that raises it.
- In 8.0.0 only this calibration raises 36146. It is not a general check on tool
  pickup.

From the calibration menu, if the printer cannot pick any tool before the calibration
starts, 8.0.0 shows 36138 Tool pickup failed, a code the toolchanger also uses outside
this calibration. This page does not cover it.

## 36130 · 37130 · Tool offset failed {#36130}

<span id="37130"></span>

*Stock firmware through 7.0.1 shows 36130 here. Stock 8.0.0 shows 36130 too, unless
one of the sweeps failed on a fault the sensor flagged, in which case it shows
[36145](#stock-800).*

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

On stock firmware through 7.0.1, 36130 can be any of the codes below. On 8.0.0 it can
still be 36191, 36192, 36196 or 36197, the temperature check under 36190, or a 36194
failure the sensor did not flag itself.

## 36190 · 37190 · Tool not picked {#36190}

<span id="37190"></span>

*Fork code. Stock firmware shows 36130 here through 7.0.1. Stock 8.0.0 shows
[36146](#stock-800), or 36130 when the failing check is the nozzle temperature.*

**What failed.** Before cleaning and measuring a tool, the firmware checks that the
tool it has just picked is the one it considers selected. The measurement also needs
the tool's nozzle temperature, which the INDX head can only read from a tool it has
picked. One of those checks failed: the tool change reported success, but the printer
does not consider the tool picked.

**What to do.**

1. Look at the head. If the tool is not on it, or not seated, press Abort, put the
   tool back in its dock, pick it with Control > Pick/Park Tool, and start again. On
   8.0.0, once the tool sits in its dock again, Retry picks it.
2. If the tool is on the head and seated, the head is misreading it. See
   [phantom tools and park failures](issues/tool-detection-ringdown-decay.md).

## 36191 · 37191 · Nozzle cleaning failed {#36191}

<span id="37191"></span>

*Fork code. Stock firmware shows 36130 here, 8.0.0 included.*

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

*Fork code. Stock firmware shows 36130 here, 8.0.0 included.*

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

*Fork code. Stock firmware shows 36130 here through 7.0.1, and
[36144 Sensor Not Found](#stock-800) on 8.0.0.*

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
   A further owner in that thread, who does not give their firmware, reports that the
   first run after switching it off was neither slow nor failed, in this calibration and
   in bed leveling.
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

*Fork code. Stock firmware shows 36130 here through 7.0.1. Stock 8.0.0 shows
[36145 Sensor Failure](#stock-800) when a sweep failed on a fault the sensor flagged,
and 36130 otherwise.*

**What failed.** The printer records the sensor's readings during every sweep, and a
sweep only counts if that recording can be analyzed: the sensor has to start
streaming, report no fault, drop no samples and deliver enough of them. Not one sweep
in the whole search produced a recording that could be analyzed. The sensor, its
board or its link to the printer is not delivering data.

If the sensor delivers data only some of the time, the printer shows 36130 instead,
so a link that drops out now and then can still look like a dirty nozzle. Stock 8.0.0
draws the line elsewhere. There, one sweep that fails on a fault the sensor flagged is
enough for 36145 once the measurement gives up, while a sensor that sends nothing at
all, and so flags nothing, ends on 36130. That is a reading of the 8.0.0 source.

**What to do.** This is the fault on
[contactless offset sensor](issues/offset-sensor-board-failure.md): check the cable
and its connectors, capture a serial log, and check the LED on the sensor board. The
log names the reason each sweep failed, see [below](#stock-firmware).

## 36195 · 37195 · Toolhead board restarted {#36195}

<span id="37195"></span>

*Fork code. Stock firmware shows 36130 here through 7.0.1, and
[36145 Sensor Failure](#stock-800) on 8.0.0.*

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

*Fork code. Stock firmware shows 36130 here, 8.0.0 included.*

**What failed.** The sweeps need the nozzle below a probing temperature limit that is
fixed in firmware. Before sweeping, the printer lowers the nozzle target and waits for
it to cool, running the print fan to help. The wait gives up when the temperature
stops falling, and here it gave up with the nozzle still above the limit.

**What to do.**

1. Check that the print fan spins.
2. Let the nozzle cool, then press Retry.

## 36197 · 37197 · Homing failed {#36197}

<span id="37197"></span>

*Fork code. Stock firmware shows 36130 here, 8.0.0 included, when a screen comes
up at all.*

**What failed.** Each measurement starts by homing any axis that needs it, and homing
failed. A failed homing usually stops the printer with its own homing error first.
During a print, crash recovery can handle a homing failure instead, which is how this
screen can appear.

**What to do.** Check that nothing blocks the bed or the head, then press Retry. If
homing keeps failing, follow Prusa's article for the axis: the ones the printer's own
homing error screens link, for [Z](https://prusa.io/36301), [X](https://prusa.io/36304)
and [Y](https://prusa.io/36305).

## Telling them apart on stock firmware {#stock-firmware}

Stock firmware through 7.0.1 shows 36130 for all of these, and so does the fork on
printers other than the INDX. Stock 8.0.0 shows one of [four codes](#stock-800). Either
way, the serial log says which failure it was: the line logged just before the dialog
appears. How to capture the log is on
[contactless offset sensor](issues/offset-sensor-board-failure.md).

### 6.9.x to 7.0.1

These lines are taken from the 6.9.1 source and are unchanged through 7.0.1
([compare](https://github.com/prusa3d/Prusa-Firmware-Buddy/compare/v6.9.2...v7.0.1)).
The fork logs them too.

| The log says | Fork code |
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
`Sensor samples overflow` and `Insufficient samples for analysis`. On the fork,
when every sweep failed like that, the last line reads
`Measurement failed: Tool offset FSM got no analyzable sensor data` instead.

### 8.0.0

In 8.0.0 the measurement logs its own reason without the `Measurement failed:` prefix,
and the calibration then adds `XY offset measurement failed for tool`. A failure
before the measurement is followed by `could not be prepared`
([compare](https://github.com/prusa3d/Prusa-Firmware-Buddy/compare/v6.9.2...v8.0.0)).

| The log says | Stock 8.0.0 shows | Section |
|---|---|---|
| `is not the selected tool, cannot clean`, `failed: no tool selected` or `Selected tool must be picked` | 36146 | [36190](#36190) |
| `Nozzle has no valid temperature` | 36130 | [36190](#36190) |
| `could not be prepared (step`, with no line about the selected tool before it | 36130 | [36191](#36191) |
| `Z probe failed for tool` or `Z probe failed at reference-line end` | 36130 | [36192](#36192) |
| `Initial probing failed, sensor Z is NaN` | 36144 | [36193](#36193) |
| `INDX puppy reset during XY scan; aborting FSM`, then `Tool offset FSM aborted: hardware failure` | 36145 | [36195](#36195) |
| `Nozzle too hot for probing` | 36130 | [36196](#36196) |
| `Homing failed` | From `ContactlessOffset`, 36130 when a screen comes up at all; from `ToolOffsetCalib`, at the start, no calibration screen | [36197](#36197) |
| `Tool offset FSM finished without high confidence in both axes` or `Tool offset FSM exceeded iteration limit` | 36145 if the sensor flagged a fault in a sweep before it (usually logged as `Sensor reported hardware failure` or `Sensor sample overflow`), otherwise 36130 | [36194](#36194) or [36130](#36130) |

Each log line names the part of the firmware that wrote it, which is how the two
`Homing failed` lines differ.
The sweep lines are as before. `Failed to get first sensor sample` counts toward 36145
only when the sensor had also flagged a fault, which the log does not show on that
line. After a comparison check, `Z offset spread too large` or
`XY offset spread too large` is followed by `Biggest outlier on` and the tool, when
three or more tools were measured.

## Verification

`provisional`. What each code means is read from the firmware source: each section
names a check the firmware makes and the code the fork shows when that check
fails, and the log lines are taken from the stock source at the 6.9.1 tag. A comparison
of the 6.9.2 and 7.0.1 tags finds the same failure handling and the same log lines.
What stock 8.0.0 shows, and what it logs, is read from the source at the 8.0.0 tag. No
owner has yet reported an 8.0.0 failure screen, so none of that has been seen on a
printer. All of it is only as reliable as the reading of the source, which is linked
above. The codes and titles of the comparison checks are from the stock
[error code list](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/lib/Prusa-Error-Codes/yaml/buddy-error-codes.yaml)
at the 6.9.1 tag, and are the same at the 8.0.0 tag. The report of a clean tool on the
head is a single owner's. Two more owners have since said on the same issue that they
see the same, without saying which part, and the vendor has not replied. The attempt
counts are from the 6.9.1-beta release notes, and which touch they apply to is read
from the source at the 6.9.1 tag.
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
that switching it off is needed. A further owner in the same forum thread reports one
good run after switching it off, without giving their firmware; being in the same
thread, it does not count as a further source toward this page's tier.
The opener of firmware issue 5526 tested the light on firmware they had
modified, which this page does not rely on.

What to do about each code is the author's reading of those checks. Where a section
sends you to another page, that page's own tier applies. The rest has not been tested
on hardware, and no owner has reported the fork's codes, or the new 8.0.0 screens, yet.
If one of these screens led you to a fix, or a step here did nothing, that report is
what moves this page up a tier. See [contributing](contributing.md).

The fork's codes exist only in firmware built from the fork. Reporting the failing step
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
tool offset calibration errors, and neither do the
[detailed notes](https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v7.0.0)
published with its source. Nor does 7.0.1, published on 19 October 2026 with a single
fix for a startup hang
([notes](https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v7.0.1)). Their
source, public since 3 November 2026, still sends every failure on this page to the one
36130 warning and logs the same lines as 6.9.2
([compare](https://github.com/prusa3d/Prusa-Firmware-Buddy/compare/v6.9.2...v7.0.1)).
That matches one owner's report on 7.0.0 of the 36130 screen together with the log
line this page maps to 36193
([firmware issue 5548](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5548)).

8.0.0, published on the downloads page on 22 October 2026, at first did not appear to
include it either. Neither the downloads page nor the
vendor's
[forum announcement](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/8-0-0-firmware-for-prusa-core-one-gen-2-indx-core-one-indx/)
mentions it, and both describe only the general change to error screens, which drops
the printer's hash and the signature markers and simplifies the QR code. The
[GitHub release notes](https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v8.0.0),
published with the source on 3 November 2026, do list it, tagged for the INDX and the
XL+: a failed tool is now measured again on its own instead of restarting the whole
calibration, and each failure gets its own screen with a code and the affected tool.
The source bears that out, with the qualifications under
[what stock 8.0.0 shows](#stock-800) and in the paragraph above it on which tool the
screen names.
The change is in none of the earlier tags: 7.0.1 still has no screen for any single
failure. Firmware issue 5482 is still open and no commit links to it, but some of the
8.0.0 commits that make the change, though not all, carry the internal reference the
developer gave there
([compare](https://github.com/prusa3d/Prusa-Firmware-Buddy/compare/v6.9.2...v8.0.0)).
Stock 8.0.0's split is not the fork's. It has three new codes where the fork has
eight, and it keeps cleaning, sheet probing, temperature and homing failures on 36130.

Prusa's own codes for some of these failures were already in its public
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
Going by their descriptions alone, 36144 looked closest to 36193 on this page, 36145
to 36194 and 36146 to 36190, though which checks raise them could not be read until
the source was published. The 8.0.0 source settles it, under
[what stock 8.0.0 shows](#stock-800): 36144 is the 36193 failure, 36145 covers 36195
and parts of 36194 and 36130, and 36146 is 36190 without its temperature check. 36146
is raised only by this calibration, so it is not the general pickup check its commit
description suggested. The list at the 8.0.0 tag still marks it not approved, a flag
the list's own README describes as of no real use, and 8.0.0 raises it all the same.
The list at the 7.0.0 tag already carries 36144, 36145 and the reworded 36134, but
nothing in 7.0.0 or 7.0.1 raises the first two. The 8.0.0 notes describe the new
screens without giving their codes.

## Related

- [Contactless offset sensor](issues/offset-sensor-board-failure.md): 36194 (36145 on
  stock 8.0.0), and 36130 when cleaning has not helped
- [Bed not aligned in Z](issues/tool-offset-bed-z-alignment.md): 36193 (36144 on stock
  8.0.0), and possibly 36192
- [Oozing during probing](issues/oozing-during-probing-and-calibration.md): 36130,
  36192 and 36193
- [Phantom tools and park failures](issues/tool-detection-ringdown-decay.md): 36190
  (36146 on stock 8.0.0)
- [Wiper, purge and blobs](issues/stringing-and-wiper-calibration.md): 36191
- [Loadcell noise](issues/loadcell-emi-noise.md): 36192 and 36193
- [Who to contact](issues/support-and-warranty-path.md): 36194 and 36195 (36145 on
  stock 8.0.0)
