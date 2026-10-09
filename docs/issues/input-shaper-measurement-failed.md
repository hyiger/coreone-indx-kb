---
title:        Input shaper calibration stops with "Measurement failed"
confidence:   provisional
updated:      2026-10-08
author:       hyiger
printer:      Core One / Core One+ with INDX, mostly Founders Edition; one Founders Edition with the Gen 2 upgrade
toolhead:     INDX (one report is an 8-tool head; the rest do not say)
hotend:       unknown
nozzle:       unknown
firmware:     6.9.0 and 6.9.1-beta; one report also on 6.6.3
sources:
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5436
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.6.0
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.6.3
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.9.0
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.9.1
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/compare/v6.9.0...v6.9.1
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.9.2
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/compare/v6.9.1...v6.9.2
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/src/feature/factory_reset/factory_reset.hpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/src/feature/factory_reset/factory_reset.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/src/gui/screen/screen_factory_reset.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/src/persistent_stores/store_instances/config_store/store_definition.hpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/src/persistent_stores/store_instances/config_store/store_definition.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/src/common/printer_variant/coreone.hpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/src/gui/MItem_hardware.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.6.3/src/persistent_stores/store_instances/config_store/store_definition.hpp
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/coreone-with-mmu-upgrade-to-indx/
  - https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/toolhead-docking-calibration-fails/
superseded_by:
---

# Input shaper calibration stops with "Measurement failed"

!!! warning "One open issue, several reporters, no cause found"
    Every report of the failure comes from a single GitHub issue. Several INDX owners
    have added their own reports to it, but one issue is one source, and Prusa has not
    yet said what is wrong. `provisional`.

## Summary

On INDX printers running firmware 6.9.0 or the 6.9.1 beta, the Input Shaper
calibration can stop at its first measurement with "Measurement failed." even though the
accelerometer has just calibrated without complaint. Prusa is investigating and the
issue is open; nothing in the 6.9.1 release notes addresses it, and 6.9.2, released on
7 October 2026, changes only the printer's filament presets. No report yet says whether
the stable 6.9.1 release, which came out after most of these reports, or 6.9.2 is
affected; the latest report gives no firmware version. A Prusa developer's
first check was the **1.5GT Belts** setting, which must match the belts actually on the
printer. Going back to firmware 6.6.3 got the calibration working for two owners. A
third saw it fail on 6.6.3 as well, and only got it through after also resetting
"Common Misconfigurations".

## Detail

### What owners see

The sequence is the same in each detailed report: the accelerometer calibration
completes, then the first axis measurement — X, where the axis is named — fails with
"Measurement failed." Phase stepping calibration still works on the one printer where
it was mentioned.

[GitHub #5436](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5436) was opened
by a Founders Edition owner on 6.9.0 who said the failure began with the new firmware
and that reflashing 6.6.3 made it go away. Others followed:

- one owner with no further detail;
- an owner on 6.9.1-beta, with the printer set to Core One+ and the 1.5GT Belts option
  off, for whom going back to 6.6.3 also fixed it;
- a Founders Edition owner for whom it failed on 6.6.3, 6.9.0 and 6.9.1-beta alike,
  although 6.6.3 had calibrated fine a month earlier. They had unloaded filament, let
  the printer cool, retensioned the belts, checked that the gantry was square, and ruled
  out vibration from outside;
- most recently, an owner of an 8-tool Founders Edition with the Gen 2 upgrade and its
  1.5GT belts.

### Where the reports disagree

The opener and the owner on 6.9.1-beta both say reflashing 6.6.3 cured it. The owner
who retensioned the belts, whose printer had calibrated on 6.6.3 a month before, says it
failed on 6.6.3 too. That owner later got it working by flashing 6.6.3 again **and**
resetting "Common Misconfigurations", so for them it is not known which of the two did
it. This page records both accounts and does not pick one.

"Common Misconfigurations" is one of the items on the printer's **Factory Reset**
screen (`Settings > System > Factory Reset`), and the "Fix Common Misconfigurations"
preset there resets that item and keeps every other one, the hardware configuration
included, so the belt setting survives it. The firmware source describes what the
preset clears as experimental settings and similar tweaks that may cause trouble. In
practice it clears stored overrides such as the X/Y steps per millimeter, motor currents
and microstepping, and it also returns homing sensitivity and the PID values to their
defaults. Whether that reset alone clears the failure on 6.9.x, without a downgrade, has
not been reported.

### What Prusa has said

A Prusa developer pointed out that 6.9 is the first firmware with support for 1.5GT
belts. If that option is switched on for a printer that does not have those belts, the
motion is scaled for the wrong belt, which they said could spoil the measurement. The
two owners who answered had it switched off, and neither said they had 1.5GT belts, so
that does not explain their failures. The developer then asked for a log: turn on
`Settings > System > Save Logs To File`, run the calibration until it fails, and turn
logging off again before removing the USB drive, so the file is written out completely.
Two owners attached logs, and Prusa said it is tracking the problem internally.

Neither the 6.9.1 release notes nor the titles of the commits between 6.9.0 and 6.9.1
mention input shaping or the accelerometer. The only input shaper source file that
changed between the two tags is a small refactor of how filter names are looked up.
On the INDX, 6.9.2 changes nothing but the PVA and BVOH filament presets, which the
6.9.1 notes had announced and which that release left out. 6.9.2 touches no input
shaper or accelerometer code.

Earlier, Prusa's notes for 6.6.0, the first INDX firmware, listed occasional errors in
the Input Shaper and Phase Stepping calibrations as a known issue, which a restart and
a second attempt would usually clear. The notes for 6.6.3, 6.9.0 and 6.9.1 do not
repeat it, and nobody in #5436 says whether they tried a restart.

## What to do

**Check the belt setting first.** The **1.5GT Belts** item in the printer's hardware
settings has to match the belts on the machine: on for 1.5GT belts, off for the
original ones. Looking costs nothing, and it is the one check Prusa has named.

Do not assume it is right. Two owners, in separate forum threads, found that after
flashing the INDX firmware the printer had assumed the Gen 2 belts were fitted. For
[one](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/coreone-with-mmu-upgrade-to-indx/)
that was correct. The
[other](https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/toolhead-docking-calibration-fails/)
had not yet fitted the Gen 2 parts, and dock calibration then failed; see
[dock calibration rejects some or all docks](dock-calibration-rejects-docks.md) and the
[assembly notes](../reference/assembly-notes.md). This issue's opener, who had come
from 6.6.3, found the option off. Prusa's firmware source fits both: the stored default
is off, but a first run, or a factory reset that clears the hardware configuration,
applies the Gen 2 variant and switches it on. That flashing the INDX firmware counts as
a first run is inferred, not confirmed. By the same reading, a printer updated in place
from 6.6.3, which had no belt setting at all, keeps it off even if Gen 2 belts have been
fitted since. That too is an inference from the source; the latest reporter, who has
those belts, did not say how theirs is set.

Change the setting only once you know which belts are fitted; the
[dock calibration](dock-calibration-rejects-docks.md) page describes telling them apart
by counting teeth. The printer warns when you change it, and Prusa's source shows that
the change resets the homing, belt-tuning, gantry-squareness and X/Y self-test results.
So restart if asked, and rerun the calibrations from the start before trying input
shaper again. If it was already right, leave it.

**Restart and try again.** It costs nothing, and it was Prusa's advice for the input
shaper errors listed as a known issue in 6.6.0. `provisional` — nobody has reported
whether it helps with this failure on 6.9.x.

**Capture a log and add it to #5436** rather than opening a new issue, following the
logging steps above. Say which belts you have and which printer the firmware thinks it
is.

**If you try the Common Misconfigurations reset**, use only the Fix Common
Misconfigurations preset and leave every other item on Keep. It cannot be undone, and it
discards the overrides and tuned values listed above. Do not use Full Reset, the hard
reset at the bottom of the list, or any selection that resets HW Configuration: those
bring back the first-run Gen 2 default, belt setting included, which on a printer with
the original belts creates the mismatch the developer warned about. Check the 1.5GT
Belts item again after any reset.

**Weigh a downgrade carefully.** Going back to 6.6.3 worked for two owners with the
1.5GT option off, but not for a third until they also reset Common Misconfigurations.
It also gives up what came later, including the 6.9.1 homing fix and gantry squareness
wizard. On a Gen 2 printer, or any printer with 1.5GT belts, it is likely no option at
all: Prusa released 6.6.3 for the Core One INDX and the Core One+ INDX, and support for
the Gen 2 hardware and the 1.5GT belts begins with 6.9.0. So 6.6.3 would run those
belts at the original belts' steps per millimeter: the same kind of mismatch the
developer warned about, in the other direction. That is an inference from the release
notes and the firmware source; nobody has reported trying it.

## Verification

`provisional` — one GitHub issue. Several owners describe the same failure in it, but
reports gathered in one place are not independent confirmation. One of the five adds
nothing beyond agreeing, and two (the opener and the latest) give little detail; the
latest does not say how its 1.5GT Belts setting is set. The disagreement over whether
6.6.3 alone fixes it is unresolved. No report yet says whether stable 6.9.1, or 6.9.2,
is affected. Rechecked on 8 October 2026, the issue had no comments newer than the
latest report.

The two reports about the belt setting in the assembly notes concern the setting and
dock calibration; neither reported this failure. The two forum threads in the sources
are cited only for those belt-setting reports. No forum thread among those collected
for this site reports the failure.

**First-party.** The Factory Reset presets, what the Common Misconfigurations item
covers, the belt setting's stored default, the Gen 2 variant applied on a first run and
after a hardware-configuration reset, and what changing the belt setting resets all come
from Prusa's firmware source at the 6.9.1 tag; that 6.6.3 has no belt setting comes from
the source at that tag. That 6.9.2 changes only the filament presets comes from
[comparing its tag with 6.9.1's](https://github.com/prusa3d/Prusa-Firmware-Buddy/compare/v6.9.1...v6.9.2).
The warning shown when the belt setting changes is the printer's own. The known issue
with input shaper calibration errors is from Prusa's 6.6.0 release notes.

What would move this forward: Prusa naming a cause or shipping a fix, or a report in a
separate thread or issue.

## Related

- [Dock calibration rejects some or all docks](dock-calibration-rejects-docks.md) — the
  same belt setting; how to tell which belts you have and what changing it resets
- [Who to contact](support-and-warranty-path.md) — if a downgrade is not an option and
  the issue stays open
- [Assembly notes](../reference/assembly-notes.md) — the hardware configuration screen
  after the first flash, including the belt setting
