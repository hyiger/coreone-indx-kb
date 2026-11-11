---
title:        Dock calibration rejects some or all docks
confidence:   reported
updated:      2026-11-10
author:       hyiger
printer:      Core One, Core One+, Core One+ (Gen 2)
toolhead:     INDX
hotend:       unknown
nozzle:       unknown
firmware:     6.9.0, 6.9.1-beta, 6.9.1; 6.9.2, 7.0.0, 7.0.1 and 8.0.0 by source comparison
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
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/src/feature/indx_gantry_squareness/indx_gantry_squareness.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/src/feature/indx_gantry_squareness/indx_gantry_squareness.hpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/src/feature/indx_gantry_squareness/screen_gantry_squareness.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.9.1
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.9.2
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/compare/v6.9.1...v6.9.2
  - https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/gantry-squaring-failing/
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5520
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/tree/v6.9.1-beta/src/feature
  - https://help.prusa3d.com/downloads/core-one-indx
  - https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/indx-firmware-7-0-0-stuck-on-reset/
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v7.0.0
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v7.0.1
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v8.0.0
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/8-0-0-firmware-for-prusa-core-one-gen-2-indx-core-one-indx/
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/compare/v6.9.2...v8.0.0
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/commit/856993e7a5223eefe05f16252669b18d92cdac26
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/commit/e0bb99ac6505d18e606b4561c2315d2c12632633
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/commit/596d5330f3a5afde6b6eaefa6f60e9cb12882074
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/src/feature/indx_dock_calibration/indx_dock_calibration.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/src/feature/indx_gantry_squareness/indx_gantry_squareness.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/src/feature/indx_gantry_squareness/screen_gantry_squareness.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/lib/Marlin/Marlin/src/module/prusa/indx_dock_position_defaults.hpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/lib/Marlin/Marlin/src/module/prusa/toolchanger_utils.h
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/lib/Marlin/Marlin/src/module/prusa/toolchanger_utils_indx.cpp
superseded_by:
---

# Dock calibration rejects some or all docks

!!! warning "One cause is confirmed twice; the others rest on one machine or one thread"
    A belt-type setting that does not match the fitted belts has stopped dock calibration
    on a large, unchanging Y error on two machines, reported in two unrelated places:
    every dock in one report, and in the other a Y reading that would not move.
    Correcting it, directly or through the printer variant, fixed both. That part is
    `reported`. A dock row that fails only at one end, blamed on gantry skew, comes from
    one unresolved machine, and a squareness wizard held back by the docks themselves
    from one other. The slack-belt fix for a uniform shift rests on one owner, and the
    belt and homing advice for a failing first dock comes from several owners, all in a
    single forum thread. An account of the opposite belt mismatch, Gen 2 belts with the
    setting left off, comes from one owner. Those parts are `provisional` and are marked
    where they appear.

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
  slack belts, gantry squareness and homing calibration. Two later owners in the same
  thread got dock calibration to pass by tightening the belts a step at a time between
  attempts, though neither described a first-dock-only failure: one found every dock
  off, after a stuck tool and repeated homing failures (compare the slack-belt case in
  the first bullet). `provisional`.

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
source marks its Y as still needing validation on more printers; that Y changed in 7.0.0
and still carries the same note at 8.0.0.

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
Both were read at the 6.9.1 tag, are unchanged for the Core One at 8.0.0, and are
withheld until checked against a machine.

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

Firmware 8.0.0, dated 22 October 2026, says of the dock measurement in its
[release notes](https://help.prusa3d.com/downloads/core-one-indx) only that the head now
approaches the dock more gently. Prusa published the 8.0.0 source on 3 November 2026,
and it shows what changed
([commit](https://github.com/prusa3d/Prusa-Firmware-Buddy/commit/856993e7a5223eefe05f16252669b18d92cdac26)).
Once you have placed the head at the dock and confirmed, the calibration backs off a
little, then drives the head further into the dock until it stops, and that stopping
point is what the dock's position is worked out from. In 8.0.0 the X and Y motors run at
a reduced current for that one push and go back to their normal current afterward. The
speed, distance and direction of the push are as before. A comment beside the change
gives the reason: at full current, the push bends the front plate, presumably the one
the docks are mounted on. So what changed is the force, at the very move the reading
comes from. The expected positions, the window and every other step of the measurement are
unchanged for the Core One.

TODO(verify): the reduced XY motor current 8.0.0 uses for the push into the dock, a
constant in indx_dock_calibration.cpp at the 8.0.0 tag. Withheld as a motor current.

If the plate gave under the old push, the head would have stopped further in than the
dock really sits, and a gentler push could shift readings slightly. That is this page's
inference: the source gives no size for the effect, and no owner has yet said whether
docks that failed on earlier firmware pass on 8.0.0, or the reverse. The same release
also lowers the bed further before this calibration, so there is more room for your
hands during the manual step
([commit](https://github.com/prusa3d/Prusa-Firmware-Buddy/commit/596d5330f3a5afde6b6eaefa6f60e9cb12882074));
that leaves the measurement itself alone.

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
on first run and after a factory reset that clears the hardware configuration, at both
the 6.9.0 and 6.9.1 tags, which fits
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

`provisional` — one owner. The opposite mismatch has since been described, in the
[gantry squaring thread](https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/gantry-squaring-failing/).
Their warning is that an INDX machine given the Gen 2 upgrade needs the belt setting
switched to 1.5GT by hand afterward. That fits the source as long as a non-Gen 2
variant had been chosen and was left in place: the setting follows the printer variant,
not the belts fitted (after a factory reset, and possibly after flashing, the default is
the Gen2 variant, with the setting on). Leave it off, they say, and the squareness
wizard fails on 6.9.2 and later, while older firmware instead reports the Y axis off by
an amount they quote. Prusa's source shows the wizard unchanged between 6.9.1, where it
first appears, and 6.9.2
([compare](https://github.com/prusa3d/Prusa-Firmware-Buddy/compare/v6.9.1...v6.9.2)),
so the version boundary they describe is not explained by the wizard itself. They do not
say which calibration showed that figure, whether the wizard failed on its skew reading
or could not measure at all, or what the sign of their figure is measured against, so
the account neither confirms nor contradicts the direction inferred above.

TODO(verify): the Y error one owner reports, on firmware older than 6.9.2, for 1.5GT
belts with the setting off, from the gantry squaring thread. Withheld as an offset
magnitude.

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

On 8 October 2026 the developer came back with questions rather than a fix. They asked
what the owner means by gantry calibration failing, said they could not see how skewing
the gantry would let it pass, and asked whether the nozzles had been taken out of docks
1 and 8 before the squareness check, as the wizard instructs. The owner had not answered
when this page was updated.

TODO(verify): the gantry squareness tolerance the Prusa developer quoted on #5491. The
6.9.1 wizard passes against the same figure, a constant in indx_gantry_squareness.hpp
that its result screen also shows, unchanged at 8.0.0. Withheld as an assembly setting.

How the wizard measures bears on that exchange. Prusa's 6.9.1 source shows it homing
first, then driving the empty head into the two outermost docks until it stalls, and
taking the difference between the two stopping points in Y as the skew. It asks for
docks 1 and 8 to be emptied beforehand, and if the measurement itself fails, it asks you
to check that they are; a skew reading over the limit instead tells you to align the
gantry by the guide. It follows that the wizard judges square against the dock row: it
reads the same tilt that dock calibration rejects, and by itself it cannot tell a skewed
gantry from a dock row sitting out of line with a square one. Were this machine's docks
out of line, squaring the gantry by the guide would fail the wizard and skewing it to
follow the docks would pass, which matches the owner's account, if the gantry
calibration they mention is this wizard, something the developer has asked them to
clarify. That is this page's reading of the source, not Prusa's explanation, and nobody
has checked it on the machine.

Firmware 8.0.0 changes what the wizard does with a skew over the limit, though not how
it measures it
([commit](https://github.com/prusa3d/Prusa-Firmware-Buddy/commit/e0bb99ac6505d18e606b4561c2315d2c12632633)).
Its GitHub release notes say it now guides you through realigning the gantry. In the
source, instead of ending on a pointer to the guide, it asks you, with the motors still
off from the measurement, to push the head to the back, look for a gap between the
gantry and the belt tensioner at either end, and use the guide, whose code stays on
screen, if there is one. It then measures again, as often as it takes, with docks 1
and 8 kept empty throughout. The measuring method, the two docks it uses and its limit
are as at 6.9.1.
The check it adds, the gantry seated against both tensioners, is a mechanical one that
involves no dock. So on 8.0.0, a skew reading that survives that check finding no gap at
either end would itself be a clue: the wizard would be measuring something other than
the gantry, such as a dock row out of line or something holding the head back, as in the
next section. That is this page's reading of the source; nobody has reported running the
8.0.0 wizard on this machine.

The owner has asked Prusa to validate docks against a line fitted through the measured
docks, rather than one fixed Y, so a uniformly rotated row could pass while a single
displaced dock would still stand out. That request is open and labeled as an INDX
enhancement, with no commitment from Prusa.

### The squareness wizard held back by the docks

`provisional` — one owner, one thread.

A second report on the squareness wizard comes from another machine, and there the docks
themselves were plainly involved. On an original Core One fitted with the Gen 2 and INDX
upgrades in one go, the wizard failed with a skew many times beyond its limit, and one
that changed widely from run to run ([gantry squaring failing](https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/gantry-squaring-failing/)).
Watching it, the owner saw the head stop short on the left, against the spring-loaded
buttons of docks 1 and 2, while on the right it traveled all the way in, every time.
Neither button felt stiffer than the one on dock 8, and nothing else was in the way.
With docks 1 and 2 taken off, the wizard passed.

That fits how the wizard measures, described above: it takes wherever the head stalls as
that dock's position, so anything that holds the head back on one side reads as skew.
This is the page's reading of the source, unchanged in this respect through 8.0.0,
alongside one owner's account; why the buttons stopped the head on that machine was not
established, and whether anything similar played a part on the rotated-row machine is
not known. A later post in the same thread, from another owner, points at the belt
setting instead (see the belt section above); nobody said whether that applied to this
machine.

Another owner suggested checking that the plate the docks are mounted on sits flush at
both ends, and swapping docks 1 and 8 to see whether the fault moves with the dock. The
reporter did not say whether they tried either.

After the belts were retuned, the same machine went on to fail the homing calibration
with an early endstop trigger, a separate homing fault tracked in
[#5520](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5520). The owner cleared
that by going back to 6.9.1-beta. That release predates the squareness wizard, so the
downgrade settled the homing fault but says nothing about the wizard's reading. On
8 November 2026 #5520 was still open. Two owners there reported the same homing fault on
7.0.0, two more affected owners posted logs from 7.0.1, one of them saying the fault
remains, and several later commenters report it still present on 8.0.0, none of them in
connection with dock calibration. The 7.0.1 and 8.0.0 release notes, the detailed
GitHub ones included, say nothing about homing. On 10 November a Prusa developer posted
an 8.0.2-alpha build there whose homing calibration chooses the motor current itself,
and one owner's log from it read as fixed; the
[loadcell page](loadcell-emi-noise.md) has the details. Nobody has yet said whether it
changes anything for dock calibration. Another owner there reports dock
calibration stalling on their printer, which has the homing fault too: on 6.9.2 they had
hardly been able to get beyond the fourth dock, and after going back to 6.9.0, where the
homing fault was milder but still present, they got through the dock step. They do not
say that the homing fault caused the dock failures, and another commenter suspects that
machine has more than the motor fault, since most owners with the fault seem to pass
every calibration on 6.9.1-beta. That is one owner (`provisional`), and they do not say
how the docks failed.

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
dock's Y into range. They do not say whether they checked the belt setting raised
earlier in the same thread, and they have not posted since.

The next posts, on 11 October 2026, describe a slower way to tighten. An owner whose dock
calibration had gone wrong across the board, after a tool got stuck and homing kept
failing, tightened both belt tensioners a little at a time, rerunning dock calibration
on a single tool after each step until it passed. They caution that the answer might
instead lie in loosening, and warn against over-tightening. A second owner then got all
eight docks through the same way. Neither describes a failure confined to the first
dock: the first had every dock off (compare the slack-belt account above, though they
give no direction or amount), and the second does not say how theirs failed, so this
does not show that a lone failing first dock yields to the same treatment. That is
a way of searching for a tension, not a target for one, and it is still one thread:
`provisional`. Prusa's belt-tension guide remains the reference, and since tension
feeds into the other calibrations, rerunning them from the start once the docks pass is
this page's suggestion; neither owner says whether they did.

TODO(verify): the size of each tightening step and the total tensioner rotation one
owner needed, from the toolhead docking calibration thread. Withheld as a tensioning
setting.

## What to do

**Just flashed the INDX firmware, or just fitted the Gen 2 belts?** Check the
**1.5GT Belts** setting against the belts actually fitted before running any
calibration. Flashing can switch it on for a machine without them; fitting them leaves
it as it was (one owner's warning for the second case, `provisional`).

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

**Error growing along the row: check squareness.** On 6.9.1 or later, run the gantry
squareness wizard, with the nozzles taken out of docks 1 and 8 as it asks. Prusa's
source shows it measuring the same way from 6.9.1 through 8.0.0; 8.0.0 adds the guided
realignment described above. The INDX handbook revision of 22 October 2026, on the same
[downloads page](https://help.prusa3d.com/downloads/core-one-indx), lists the wizard
among its additions, so Prusa now documents it. One owner reports it crashing to an
internal error on 7.0.x (`provisional`, see Verification). If the wizard reports
significant skew, square the gantry by the guide first and treat the dock failure as
most likely a symptom of that. Because the wizard measures against those same docks, it
is not an independent check on them; if squaring the gantry by the guide will not
satisfy it, or on 8.0.0 it keeps reporting skew after its own check finds no gap at
either end, tell support that, along with the dock values. If the skew it reports is
implausibly large, or jumps between runs, watch where the head stops at each end before
touching the gantry: on one machine the dock buttons were stopping it short
(`provisional`, see above).

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
between printer variant and belt setting, the Gen2 variant as the default on first run and
after a factory reset that clears the hardware configuration, and the calibrations a belt-setting change resets come from the
same source, as do how the gantry squareness wizard measures and the limit it passes
against. Firmware 6.9.2, released on 7 October 2026, adds the PVA and BVOH filament
presets to 6.9.1 and nothing else that reaches an INDX
([compare](https://github.com/prusa3d/Prusa-Firmware-Buddy/compare/v6.9.1...v6.9.2)),
so everything read here at the 6.9.1 tag holds for it unchanged. Firmware 7.0.0
(15 October 2026), 7.0.1 (19 October) and 8.0.0 (22 October) first came with only the
short notes on the [downloads page](https://help.prusa3d.com/downloads/core-one-indx).
On 3 November 2026 Prusa published their source along with detailed release notes
([7.0.0](https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v7.0.0),
[7.0.1](https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v7.0.1),
[8.0.0](https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v8.0.0)).
Compared with 6.9.2
([compare](https://github.com/prusa3d/Prusa-Firmware-Buddy/compare/v6.9.2...v8.0.0)),
the dock validation, the Core One's expected positions and window, the tie between
variant and belt setting, the calibrations a belt change resets, and the squareness
wizard's measurement and limit are the same in all three, so what was read at 6.9.1
holds for them. 7.0.0 and 7.0.1 change nothing on this page beyond internal
reorganization, apart from the Core One L's expected Y; 7.0.1's one listed fix is for a
hang at startup. 8.0.0 makes the three changes described above: the gentler push into
the dock, the wizard's guided realignment, and a lower bed for the calibrations where
you reach inside. The
[forum announcement](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/8-0-0-firmware-for-prusa-core-one-gen-2-indx-core-one-indx/)
of 8.0.0 lists the first and the last, but
only the GitHub notes mention the guided realignment. The INDX handbook revision posted
on the downloads page on the same day as 8.0.0 lists the squareness wizard among its
additions. The squareness wizard is absent from the
[6.9.1-beta source](https://github.com/prusa3d/Prusa-Firmware-Buddy/tree/v6.9.1-beta/src/feature),
which is why a downgrade to that release cannot speak to it. The warning text for
the belt setting is the printer's own. An earlier
request ([#5445](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5445)) to
validate docks against a reference measured on the machine was closed as not planned.
Relaying the team's view, the developer judged it a large job for a small gain at the
current stage of development, while not dismissing the idea, once the belt setting had
explained the original case.

`provisional`: the rotated-row case is one machine; the owner reports being unable to
square the gantry by the guide without breaking gantry calibration, support has not yet
resolved it, and the developer's follow-up questions are unanswered. The squareness
wizard held back by the dock buttons is one owner in one thread, and the dock step that
could hardly get beyond the fourth dock alongside the homing fault is one owner on
#5520. The wizard crashing on 7.0.x is one owner in
[another forum thread](https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/indx-firmware-7-0-0-stuck-on-reset/):
after updating to 7.0.0 or 7.0.1, which they name together, they saw the squareness
test stop on an internal error screen once the head reached tool 8's position, and they
say they are going back to 6.9.2. The wizard's own source files are identical in 6.9.2,
7.0.0 and 7.0.1, though code around them changed, so the source does not show where
such a crash would come from. 8.0.0 reworks how the wizard handles its results; whether
the crash happens there, or on other machines, is not known. The belt-tension and
homing advice comes from several owners, but all in one thread, including the two who
tightened in steps until the docks passed, and the slack-belt fix for a uniform shift is
a single owner's account, as is the opposite belt mismatch in the gantry squaring
thread.

Still unverified: whether flashing the INDX firmware counts as the first run that
applies the Gen2 default, which would explain both owners who found their printer set
for Gen 2; whether docks 1 and 8 were empty in the owner's wizard runs; whether the
skew the wizard reports on the rotated-row machine lies in the gantry or in the dock row
itself; why the dock buttons stopped the head short on the machine whose wizard passed
only with docks 1 and 2 removed; whether the gentler push in 8.0.0 moves dock readings
enough to change which docks pass; whether the 8.0.0 wizard's gap check tells a skewed
gantry from a dock row out of line in practice; and whether any Core One left the
factory with a dock row far enough out of line that no squaring brings it inside the
window.

## Related

- [Tool offset calibration fails](offset-sensor-board-failure.md) — the same belt
  setting is worth ruling out there first
- [Phantom tools and park failures](tool-detection-ringdown-decay.md) — when docking
  calibrates but pickup or park still fails
- [Build plate compatibility](../reference/build-plate-compatibility.md) — tools knocked
  out of their docks while calibration passes
- [Input shaper calibration stops with "Measurement failed"](input-shaper-measurement-failed.md)
  — another calibration where the belt setting is the first check
- [Who to contact](support-and-warranty-path.md)
