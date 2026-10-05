---
title:        Dock calibration rejects some or all docks
confidence:   reported
updated:      2026-10-04
author:       hyiger
printer:      Core One, Core One+ (Gen 2)
toolhead:     INDX
hotend:       unknown
nozzle:       unknown
firmware:     6.9.0, 6.9.1-beta, 6.9.1
sources:
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5444
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5445
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5491
  - https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/toolhead-docking-calibration-fails/
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/coreone-with-mmu-upgrade-to-indx/
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/lib/Marlin/Marlin/src/module/prusa/indx_dock_position_defaults.hpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/lib/Marlin/Marlin/src/module/prusa/toolchanger_utils.h
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/lib/Marlin/Marlin/src/module/prusa/toolchanger_utils_indx.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/src/feature/indx_dock_calibration/indx_dock_calibration.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/src/feature/indx_dock_calibration/screen_dock_calibration.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/src/common/printer_variant/coreone.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/src/common/printer_variant/coreone.hpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.0/src/common/printer_variant/coreone.hpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/src/persistent_stores/store_instances/config_store/store_definition.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/src/gui/screen_printer_setup.hpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/src/gui/MItem_hardware.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.9.1
superseded_by:
---

# Dock calibration rejects some or all docks

!!! warning "One cause is confirmed twice; the others rest on one machine or one thread"
    A belt-type setting that does not match the fitted belts has stopped dock calibration
    on a large, unchanging Y error on two machines, reported in two unrelated places:
    every dock in one report, and in the other a Y reading that would not move.
    Correcting it, directly or through the printer variant, fixed both. That part is
    `reported`. A dock row that fails only at one end, blamed on gantry skew, comes from
    one unresolved machine. The slack-belt fix rests on one owner, and the belt and
    homing advice for a failing first dock comes from a single forum thread. Those parts
    are `provisional` and are marked where they appear.

## Summary

Dock calibration measures where each dock actually is, then accepts the measurement only
if it falls inside a narrow window around a position compiled into the firmware. It
records each dock's measured position, but only if it lies within that window, so it
cannot adapt to a machine whose docks sit outside it. So when docks are rejected,
*which* docks fail, and in which direction, is the clue:

- **Docks off in Y by the same amount** — or just the first dock, if calibration
  never gets further. X was within tolerance in both reports (on every dock in #5444).
  Check that the printer's
  **1.5GT Belts** setting matches the belts physically fitted. Two owners fixed it by
  matching the belt setting to the hardware, one directly and one via the printer variant. A third, with a
  smaller uniform shift the other way, fixed it by tightening slack belts instead (one
  owner, `provisional`).
- **The error grows steadily along the row, so only docks at one end fail.** The row is
  straight but rotated against the X axis. A Prusa developer suspects an out-of-square
  gantry; the one owner with this pattern has not resolved it. `provisional`.
- **The first dock fails and nothing else looks wrong.** Owners in one thread point at
  slack belts, gantry squareness and homing calibration. `provisional`.

## Error codes that lead here

| Code | What the printer shows |
|---|---|
| [`36136`](https://help.prusa3d.com/article/calibrate-dock-from-menu-17136-xl-36136-core-one-indx_1037195) | Calibrate dock from menu |

`36136` sends you to run dock calibration from the Calibrations menu. If that
calibration then rejects a dock, this is the page.

## Detail

### What the calibration checks against

The firmware holds an expected position for every dock: its own X for each dock, and on
the Core One a single Y shared by all of them. The Core One L has its own figures, and the
source marks its Y as still needing validation on more printers.

During dock calibration, a measurement outside a fixed window around its expected
position fails that dock. The failure screen shows the measured and expected values and
offers a retry. Without a retry, the dock is marked uncalibrated, its tool is disabled,
and the wizard ends there, leaving any later docks unmeasured. A measurement inside the
window is stored and used from then on. Separately, the firmware stops with a
toolchanger error rather than use any stored dock position that falls outside the
window.

TODO(verify): the expected dock positions and the width of the acceptance window. The
expected positions are compile-time constants in indx_dock_position_defaults.hpp; the
window, a per-axis offset plus a slack for display rounding, is in toolchanger_utils.h.
Both were read at the 6.9.1 tag and are withheld until checked against a machine.

Two consequences follow. A machine whose docks are all shifted by the same amount cannot
pass, however accurately it measures them. And because one Y serves every dock, a row
that is perfectly straight but slightly rotated fails only at the end furthest from the
expected line.

The wizard's reading is consistent: in the first report below, a manual check agreed
with it closely. In that case, though, both were made with the same wrong belt scaling,
so the agreement rules out a measuring fault, not a configuration one.

The reporter of the first case says the machine could neither run other calibrations
nor print while the docks stood rejected. That is one account; the firmware disabling
the tool of an uncalibrated dock is consistent with it.

### Docks rejected by the same amount in Y: the belt setting

On an original Core One converted with the INDX kit, every dock measured short in Y by
the same distance, while X was within tolerance on every dock
([#5444](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5444)). A factory reset
and a fresh flash changed nothing. A Prusa developer pointed to the belt-type setting as
the likely cause, and so it proved: the machine had the older 2GT belts while the
firmware was set for 1.5GT. Changing the setting to match and rerunning dock calibration
passed every dock.

The owner explains that the reset did not help because the setup wizard asks again
which printer variant you have, and giving the same answer put the same belt setting
back. Prusa's firmware source fits that account. Its printer setup screen lists the
variant and, separately, the belt setting, and the two are tied together: of the three
Core One variants (Core One, Core One+ and Core One+ Gen2), only the Gen2 one switches
the 1.5GT belt setting on, along with other features of that edition, and choosing
either earlier variant switches it off. By default the firmware applies the Gen2 variant
on first run and after a factory reset, at both the 6.9.0 and 6.9.1 tags, which fits
the developer's remark below that the default is 1.5GT. A machine without the Gen 2
upgrade has to be set back after any reset.

Why the error appears in Y: the belt setting changes the X/Y steps per millimeter the
firmware uses, so on the wrong belts every move is scaled by a small fixed percentage.
The error grows with distance from home, and the docks sit at the far end of the Y
travel. Same-sized Y error on every dock is the signature. The setting changes X steps
as well, but #5444 found X within tolerance on all five docks, so X error is not part of
the reported signature.

Both reports had the 1.5GT setting on 2GT belts. The head then moves further than the
firmware counts, and the docks read short of their expected Y, nearer to home. By the
same arithmetic, the opposite mismatch would put them beyond it; this is the page's own
inference, and neither report covers that case.

TODO(verify): how large that uniform shift is at the docks. A figure is worked through in
#5444; it is withheld as an offset magnitude until measured here.

A second owner, in an unrelated forum thread, hit the same wall: docking failed with a
Y reading that would not move whatever they tried, and the figure they quote is
essentially the one in #5444
([toolhead docking calibration fails](https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/toolhead-docking-calibration-fails/)).
Their printer was configured as a Gen 2 machine although none of the Gen 2 parts, which
include the newer belts, had been fitted yet. Selecting a non-Gen 2 printer
variant in the system settings, which per the source above also switches off the 1.5GT
belt setting, let dock calibration pass, on the second run. The variant change switched
off the other Gen 2 features along with the belt setting, so on its own it does not
single out the belts; the Y figure matching #5444's is what points to them.

They believe flashing the firmware for the conversion switched the configuration to
Gen 2 by itself. A separate owner, in
[another thread](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/coreone-with-mmu-upgrade-to-indx/),
saw the same right after flashing the INDX firmware: the printer had assumed the Gen 2
belts were fitted, correctly in their case, though it could not have known. Prusa's
source applies the Gen2 variant on a first run, which would explain both. That flashing
the INDX firmware counts as a first run is inferred from the source, not confirmed.

**Which belts do you have?** The Gen 2 upgrade brings the 1.5GT belts. According to the
Prusa developer on #5444, the firmware defaults to 1.5GT, and a Core One+ without the
Gen 2 upgrade most likely has 2GT; the original Core One in that report had 2GT as well.
If in doubt, count teeth
over a measured length: a 1.5GT belt has a third more teeth than a 2GT belt over the
same distance.

The printer itself warns, when you change the setting, that the wrong choice causes
dimensional and homing errors and that some calibrations will be reset. Prusa's source
shows which: changing it resets the homing, belt-tuning, gantry-squareness and X/Y axis
self-test results. So restart if the printer asks you to, then rerun the calibration
sequence from the start rather than dock calibration alone. The same setting is the
first thing to rule out for tool offset calibration too; see
[tool offset calibration fails](offset-sensor-board-failure.md).

**Not every uniform shift is the belt setting.** `provisional` — one owner. In the same
forum thread, an owner whose docks all came out off in Y by one smaller, shared amount,
and beyond the expected Y rather than short of it, fixed it by tightening belts that had
been far too slack, with no change to the belt setting mentioned. Their belts rang at
the right pitch even while loose. They tightened them well past that point, then
alternated between squaring the gantry and retuning the belts until neither disturbed
the other, and finally reran every calibration from the start, after which dock
calibration passed. That is one owner's method, not Prusa's procedure: follow Prusa's
belt-tension guide, and do not over-tension.

### Error that grows along the row: a rotated dock line

`provisional` — one machine, unresolved.

On an eight-dock Core One+ (Gen 2) on 6.9.1-beta, the owner reports the belt setting
correct for their Gen 2 belts, and three runs per dock repeated almost exactly
([#5491](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5491)). The measured Y
crept steadily from the first dock to the last, on a near-perfect straight line. The
last two docks fell outside the window and the one before them sat on its edge. The
owner inspected the tool holders, and every dock sat on the same line, which rules out
a single dock out of place.

The owner had first ruled out squareness by measuring printed squares, but had already
noticed, before Prusa replied, that one side sat further out even with the gantry
nominally square. A Prusa developer read it as a gantry that is not square and pointed
to the squareness wizard new in 6.9.1. Run on that machine, the wizard reported skew
well outside the tolerance the developer then quoted, above which homing is said to
become unreliable. The owner says squaring the gantry by the guide makes gantry
calibration fail, while skewing it so one side shows a gap lets that pass and breaks
everything else. After weeks with support it was still unresolved on 29 September 2026.

TODO(verify): the gantry squareness tolerance the Prusa developer quoted on #5491, and
whether the 6.9.1 wizard judges against the same figure. Withheld as an assembly
setting.

The owner has asked Prusa to validate docks against a line fitted through the measured
docks, rather than one fixed Y, so a uniformly rotated row could pass while a single
displaced dock would still stand out. That request is open and labeled as an INDX
enhancement, with no commitment from Prusa.

### The first dock fails, nothing else obviously wrong

`provisional` — several owners, but all in one forum thread.

The [same forum thread](https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/toolhead-docking-calibration-fails/)
collects the advice owners gave and the fixes that worked:

- **During the manual step**, the head should fully enclose the tool, with the two front
  faces flush, and you should keep holding it there through the first button press.
- **Nothing in the way**: the fence sitting flush with the frame, the waste bin
  clear, and full travel available to the head.
- **Belts and homing.** Another owner, describing what is likely the same calibration
  (they call it tool calibration), only got it to pass after more belt work and redoing
  the homing calibration. The slack-belt account above comes from this thread too.
- **The tuning tool.** One owner says Prusa's belt-tuning app gives no target guidance
  for INDX belts, Gen 2 or otherwise, so tension ends up set by trial; another found the
  app worked on the original belts but was unsure its targets suit the newer ones.

One owner posted on 30 September 2026 that five attempts at retuning the belts,
realigning the gantry and rerunning the homing calibration had not brought the first
dock's Y into range, with no reply yet. They do not say whether they checked the belt
setting raised earlier in the same thread.

## What to do

**Just flashed the INDX firmware?** On a machine without the Gen 2 belts, check the
**1.5GT Belts** setting before running any calibration.

**Read the numbers before changing anything.** The failure screen shows the measured and
expected position of the dock it rejected. Note which docks fail and how far off each
one is in X and in Y. The pattern points to the cause far better than any single
reading.

**Docks out by the same amount in Y, or the wizard stopped at the first dock with a Y
error: check the belt setting first.** It costs nothing, and it is the only cause on
this page with two confirmed fixes behind it. Identify the belts first, by counting
teeth as above. Then set the **1.5GT Belts** toggle itself to match them; choose a
printer variant only if every part of that edition matches what is fitted. Rerun the
calibrations from the start, since the change resets several of them. If the setting
was already right, belt tension is next.

**Error growing along the row: check squareness.** On 6.9.1, run the gantry squareness
wizard. If it reports significant skew, treat the dock failure as a symptom of that
rather than something to fix at the docks.

**Neither pattern:** work through belt tension, gantry squareness and homing
calibration, then rerun the calibrations from the start rather than retrying the dock
step alone.

**Still stuck:** contact support with the measured values for every dock. See
[who to contact](support-and-warranty-path.md).

## Verification

`reported` for the belt-type cause: two owners, in two unrelated places — a firmware bug
report and a forum thread — each fixed a dock calibration stuck on a large, unchanging Y error by
changing the belt or Gen 2 configuration to match the hardware. In the bug report a
Prusa developer identified the cause before the owner confirmed it.

**First-party.** How the firmware validates a dock — fixed expected positions, one shared
Y on the Core One, a fixed window, and what happens to a dock that falls outside it —
comes from Prusa's public firmware source, read at the 6.9.1 release tag. The tie
between printer variant and belt setting, the Gen2 variant as the first-run and
factory-reset default, and the calibrations a belt-setting change resets come from the
same source. The warning text for the belt setting is the printer's own. An earlier
request ([#5445](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5445)) to
validate docks against a reference measured on the machine was closed as not planned.
Relaying the team's view, the developer judged it a large job for a small gain at the
current stage of development, while not dismissing the idea, once the belt setting had
explained the original case.

`provisional`: the rotated-row case is one machine; the owner reports being unable to
square the gantry by the guide without breaking gantry calibration, and support has not
yet resolved it. The belt-tension and homing advice comes from several owners, but all
in one thread, and the slack-belt fix is a single owner's account.

Still unverified: whether flashing the INDX firmware counts as the first run that
applies the Gen2 default, which would explain both owners who found their printer set
for Gen 2; and whether any Core One left the factory with a dock row far enough out of
line that no squaring brings it inside the window.

## Related

- [Tool offset calibration fails](offset-sensor-board-failure.md) — the same belt
  setting is worth ruling out there first
- [Phantom tools and park failures](tool-detection-ringdown-decay.md) — when docking
  calibrates but pickup or park still fails
- [Build plate compatibility](../reference/build-plate-compatibility.md) — tools knocked
  out of their docks while calibration passes
- [Who to contact](support-and-warranty-path.md)
