---
title:        Oozing spoils bed probing and tool calibration
confidence:   reported
updated:      2026-11-08
author:       hyiger
printer:      Core One
toolhead:     INDX
hotend:       unknown
nozzle:       0.25mm, 0.4mm, 0.8mm reported
firmware:     unknown for most reports; source read at the v6.9.1, v6.9.2, v7.0.0 and v8.0.0 tags
sources:
  - https://forum.prusa3d.com/forum/prusa-indx-how-do-i-print-this-printing-help/petg-oozing-and-impeding-bed-probing/
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/printing-pc-on-indx-oozing-at-bed-probing-leveling/
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/psa-if-you-are-struggling-with-tool-offset-calibration-failing-non-stop-at-the-start-of-a-print-get-firmware-6-9-1/
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5483
  - https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/nozzle-cleaning-calibration-issues/
  - https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/a-summary-of-common-indx-problems/
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.9.1
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/compare/v6.9.1-beta...v6.9.1
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5494
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5505
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/lib/Marlin/Marlin/src/gcode/bedlevel/ubl/G29.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/src/feature/tool_offset_calibration/tool_offset_calibration.cpp
  - https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/bed-leveling-issues-3/
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.9.2
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/compare/v6.9.1...v6.9.2
  - https://help.prusa3d.com/downloads/core-one-indx
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.10.1
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5567
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/src/marlin_stubs/G427.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/src/marlin_stubs/M865.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v7.0.0
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v7.0.1
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v8.0.0
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/compare/v6.9.2...v8.0.0
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/src/feature/tool_offset_calibration/tool_offset_calibration.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/lib/Marlin/Marlin/src/gcode/bedlevel/ubl/G29.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/src/marlin_stubs/M865.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/ProjectOptions.cmake
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/src/gui/screen/filament/screen_filament_detail.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/commit/210606e66889cb636f93de34fcd6bf052367222f
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5568
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5577
superseded_by:
---

# Oozing spoils bed probing and tool calibration

## Summary

Filament that oozes while the machine is probing or calibrating puts material where
the machine is trying to take a measurement, and the measurement fails. Owners have
hit this during bed probing and during tool offset calibration, with more than one
filament type. There are several contributing causes and they are worth separating,
because the one with the best first-hand evidence — a dirty offset sensor window — is
also the easiest to fix and the least likely to be what you suspect first.

## Detail

Two different measurements get spoiled by ooze, and they fail differently:

- **Bed probing.** Material accumulates on the nozzle tip before or during the
  probing pass, so contact is detected early or inconsistently. Owners report
  probing leaving visible deposits on the sheet.
- **Tool offset calibration.** Ooze interferes with the nozzle being sensed properly
  against the offset sensor, and calibration fails. One owner reports this failing on
  every tool after swapping nozzle sizes around, and having to unload all filament,
  calibrate, then reload.

### Start here: clean the offset sensor window

The resolution that actually closed the main thread on this was cleaning the sensor
window on each nozzle. The owner reported the swabs coming away visibly black even
though they did not believe they had touched the windows, and a test print working
afterwards. This costs a few minutes and it is the highest-value thing to check.

Which sensor that window belongs to is disputed. Replies in the same thread call it a
temperature window, and the [silicone sock page](silicone-sock-migration.md), which
holds that the eddy-current offset sensor has no optical window at all, leaves the
identification open. The cleaning result stands either way.

!!! warning "Do not clean the sensor window with IPA"
    The advice relayed in the thread is to use soapy water and a cotton swab rather
    than isopropyl alcohol, on the grounds that IPA is too aggressive for that
    window. Provenance is worth stating plainly: this was described as a vendor
    recommendation circulating on Discord, and the person relaying it said openly
    that they could not point to an official source. Soapy water is the low-risk
    choice either way, so prefer it — but treat the reason as unconfirmed.

    TODO(verify): whether the vendor has published an official cleaning procedure
    for the offset sensor window.

!!! warning "Clean it, but do not polish it"
    A later caution in the same thread is worth heeding: the sensor face is meant to
    be matte, and should not end up shiny or reflective. Be sparing. The goal is to
    lift filament debris off it, not to bring up a shine.

    One caveat on that advice — the owner giving it describes the sensor as infrared,
    whereas the offset sensor is elsewhere described as eddy-current based. Those are
    different sensing principles and it is not clear which component is meant. The
    practical instruction is sound either way: remove the debris, stop there.

### Dry the filament

Suggested early and repeatedly for PETG in particular: moisture makes filament
stringy and encourages it to stick to the nozzle. This is standard practice rather
than an INDX-specific finding, and it was offered as a first guess rather than a
confirmed cause in these threads — but the INDX is reported to be more
moisture-sensitive than the Nextruder it replaces, so it is worth ruling out before
chasing anything more complicated.

### Residue the pre-calibration clean leaves behind

`reported` that the residue spoils the measurement; `provisional` for the Z offset coming
out too high, which rests on one report. Before tool offset calibration measures a tool it
purges, cools and wipes that tool's nozzle, so whatever the wipe misses is on the nozzle
when it is measured. One INDX owner, filing in October against 6.9.2 and 7.0.0, found
PETG left on the nozzle ahead of probing now and then on 6.9.0 and often on the two
later releases, and traced a Z offset that came out too high to it
([#5567](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5567)). Going back to
6.9.0 helped a good deal but did not cure it. They blame the worsening on the lower
calibration temperature that arrived with 6.9.1, at which leftover PETG is fully hard.
In early November a commenter on a separate request
([#5568](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5568)) described the
same failure with PCTG: unless they pick a lump off the nozzle before every print, the Z
offset check fails, on a fresh nozzle too. They name neither machine nor firmware, though
the request is for the INDX, and they do not say which way the offset was off.
The firmware source, which Prusa published for 7.0.0, 7.0.1 and 8.0.0 on 3 November,
shows that none of this changed through 8.0.0: the clean takes the same steps, in the same
order, and cools to the same capped temperature as at 6.9.2 (see *Verification*). In the
source the 7.0.0 item on improved Nozzle Wiper cleaning, carried over from the XL and XL+
firmware [6.10.1](https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.10.1),
belongs to the wiper accessory of printers without an INDX, and 8.0.0's smaller slowdown
for flexible filament changes how fast the extruder feeds it, not the order of the clean
or its temperature.
Other owners report the same residue and put it down to the order of the clean or to its
temperature; that evidence is collected under *Residue left by the clean before
calibration* on [blobs dragged into the print](stringing-and-wiper-calibration.md).

### The probe temperature may not be the one you expect

There is a reported firmware and slicer behavior where the temperature used for
pre-print bed probing is derived from the filament assigned to **tool 1**, not from
the tool actually doing the probing. If a high-temperature material is assigned to
T1, everything probes hot and oozes, regardless of what is loaded elsewhere.

The reported workaround is elegant if it holds: it is enough to *declare* a
low-temperature filament in T1 in the slicer — the physical filament does not have to
be there — which would explain why jobs sliced from profiles that assume a
low-temperature material never showed the problem. On the stock profile this site
reproduces, though, the rule is keyed to the print's initial tool rather than to T1 — see
the PC section below before relying on it. There is also a start-G-code
approach that forces the probing temperature before the mesh bed leveling block, by
replacing the generated temperature command with a fixed one.

TODO(verify): the probing temperature to force, and the exact G-code command and
argument to use. Also TODO(verify): the reduction one owner used successfully on a
non-INDX Core One for the same symptom, quoted as a range rather than a single figure.
No temperature is published on this page until someone has confirmed it on hardware.

Two further reported details in this area, worth knowing before you go hunting: a
slicer configuration update corrected how that temperature is worked out, for most
materials — though one engineering material still probes hot; and the temperature used for tool offset
calibration is fixed in firmware and cannot be changed from G-code, so this workaround
does not help that failure mode. The firmware source bears out only part of that second
detail. From the v6.9.1 tag through v8.0.0 the calibration sets its own probing
temperatures, at or below a built-in ceiling, and the calibration command `G427` reads no
temperature argument, so no G-code can raise the probing temperature above that ceiling.
Below it, the Z-probe temperature follows the preheat value of the filament loaded in
that tool, and `M865` can change that value, and the temperature the tool purges at, for
a user-defined or ad hoc filament. A built-in preset is out of its reach, but from 7.0.0
the printer's new Customize button turns a loaded preset into an editable copy for that
slot alone, kept until the filament is unloaded, and that copy counts as ad hoc. The
XY-probe temperature is fixed. So the calibration temperature is capped rather than fixed:
G-code can lower the Z-probe temperature, but cannot raise it or move the XY one (see
*Verification*). An October bug report, which holds that the lower calibration
temperature makes leftover PETG worse, suggests among its fixes a temperature parameter
for the calibration command, or a temperature that follows the filament as the
bed-probing one does
([#5567](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5567)). There is also a
sibling slicer trap in which the **bed** temperature follows T1 in the same way.

**The engineering material is PC.** A [second owner](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/printing-pc-on-indx-oozing-at-bed-probing-leveling/) hit this with PC Blend and
described it from the other end: probing ran hot enough to ooze onto the sheet and fail
leveling, and lowering the nozzle temperature by hand on the next attempt cured it
outright. That moved "at least one engineering material still probes hot" off a single
report and gave it a name, and it has not stayed with one owner since. Two further owners in
the same thread, another in a [separate thread](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/psa-if-you-are-struggling-with-tool-offset-calibration-failing-non-stop-at-the-start-of-a-print-get-firmware-6-9-1/), and a
[firmware issue](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5483) all describe PC Blend failing bed probing until the
temperature comes down.

**Where the temperature comes from.** There is **no dedicated probing-temperature field**
in the slicer, but there is a rule. The stock printer start G-code works out the probing
temperature from the filament of the print's **initial tool** — the first tool the print
actually uses — and gives PC and PA a case of their own: a
fixed offset below the first-layer temperature. The annotated profile reproduces that
expression in its section on globals and the probe temperature — see
[annotated profile G-code](../gcode/indx-profile-gcode.md). It is the rule these owners
keep running into.

**Initial tool, not T1.** That expression reads the filament of `initial_tool`, which is
not the T1 behavior reported further up. The two select the same filament only when a
print starts on T1. On a print that starts on another tool they point at different
presets — so on this profile, declaring a low-temperature filament in T1 will not help a
print that begins on T3; the filament to look at is the one your print starts with.
Whether the earlier T1 report describes an older profile or a different machine state is
not established.

**No firmware release so far lists a change here.** The 6.9.1 beta lowered the
temperature used for *tool offset calibration* — a different step, and one that firmware
controls. The bed-probing temperature comes from the slicer profile, so owners on the
beta still see PC Blend probe hot, and the
[bug report](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5483) filed against
the beta is still open, with no reply from Prusa. The
[stable 6.9.1](https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.9.1),
published 2026-09-25, lists a gantry-squaring wizard and a homing fix, and nothing about probing temperature. Its notes also do not repeat the beta's
calibration changes, but the stable carries them all the same: in the firmware
repository it is the beta tag plus
[15 further commits](https://github.com/prusa3d/Prusa-Firmware-Buddy/compare/v6.9.1-beta...v6.9.1),
none of which touches tool offset calibration. That comes from the release history, not
the notes. 6.9.2, released 2026-10-07, changes nothing here either: on the INDX it is the
stable 6.9.1 plus the PVA and BVOH filament presets that the 6.9.1 notes announced but
left out
([compare](https://github.com/prusa3d/Prusa-Firmware-Buddy/compare/v6.9.1...v6.9.2)).
Firmware 7.0.0, dated 15 October 2026 on
[Prusa's downloads page](https://help.prusa3d.com/downloads/core-one-indx), lists nothing
on probing temperature either, and nor does 8.0.0, dated 22 October, which fits the
value coming from the slicer profile. The fuller notes for both that Prusa put on GitHub
on 3 November say nothing on it either. On
18 October a further commenter on the bug report hit the failure as soon as they tried
PC Blend, without naming a machine or a firmware version. No owner has yet reported how
PC Blend probes on stable 6.9.1, 6.9.2, 7.0.0, 7.0.1 or 8.0.0.

**Adjusting it.** One owner widened the PC offset in the printer's start G-code and the
failures stopped. The catch, which they pointed out themselves, is that a printer
configuration update replaces the start G-code, so the edit has to be redone after each
one. The same expression also checks the initial tool's filament notes for an override
marker before it ever reaches the PC case, which suggests a per-filament route that would
survive those updates — but that is a reading of the profile, not something an owner has
reported testing. And the slicer's own **oozing-prevention option did not help**, so
reaching for it first will cost you a print. The owner who filed the PC Blend bug report
suggests a stopgap that touches no file: as soon as bed probing starts, turn the nozzle
temperature down from the Tune menu. It is the hand-lowered temperature described above,
timed to the probing, and it has to be repeated on every print.

TODO(verify): these accounts state the temperature PC probed at, the lower ones that
worked, and the adjusted offset. None of them is published here. Forum posts and a bug
report are not the hardware confirmation this page requires before a temperature goes on
it — but they are leads, and they are the same figure the marker above is asking for.

### When leveling fails and retries

`provisional` for the owner reports — a few of them, and on their face they do not
agree. The firmware source, below, matches each to the step that failed. Once bed
leveling has failed on a fouled nozzle, do not count on the retry starting from a clean
one. A
[feature request](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5494)
describes the head moving over to the wiper and then going back to the bed for another
attempt without scrubbing the nozzle. An owner on the 6.9.1 beta, in the
[nozzle cleaning thread](https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/nozzle-cleaning-calibration-issues/),
found the tool left parked in the silicone wiper block, out of reach for cleaning by
hand; the print went ahead only after several retries. Two other owners there describe
something different: a retry that heats, purges and wipes the nozzle again even after it
has been cleaned by hand, fouling it enough to fail once more. One of them was also on a
6.9.1 build, and allows that their own wiper setting or a loadcell fault may be to blame;
the other gives no version, and neither does the feature request. So firmware version
does not explain the difference, and those two posts do not say whether bed leveling or
tool offset calibration was the step failing.

**Two steps, two retries.** Read against the firmware source, the accounts stop
conflicting: they describe different steps. When bed leveling cannot get a reading, the
printer parks the head at its park position, which the code places inside the nozzle
cleaner area, asks whether to retry, and on a yes leaves the cleaner and probes again
with no cleaning in between. That is the feature request and the beta owner. When tool
offset calibration fails during a print, the printer parks the head at the front with
the bed lowered, where the nozzle can be reached, and on Retry runs the per-tool
preparation again — heat, purge, cool, wipe — before it probes. After a failed XY scan
that is the failing tool alone; after a failed Z probe the retry restarts calibration
from the first tool, so every tool is purged again. That is the re-fouling the other two
owners describe, and it happens however well the nozzle was just cleaned. Both paths
take the same steps in 6.9.0, the 6.9.1 beta, stable 6.9.1, 6.9.2, 7.0.0 and 7.0.1 (in
the preparation, the beta changed only the temperature it cools to), which is why version
did not separate the reports. That holds for Prusa's own builds; the owner on a 6.9.1 build posted before
the stable release and did not say which build it was. The bed-leveling code does have a branch that wipes and
retries, but it belongs to a probe-cleanup pass that the stock INDX start G-code does
not call.

In practice: a failed bed leveling will not clean the nozzle for you, and after a failed
tool offset calibration, cleaning by hand is followed by a fresh purge. An
[upstream report](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5505) against
the beta asks for the calibration retry to skip the purge and only reheat and wipe,
since purging again feeds the problem back in. A second INDX owner filed much the same
request separately in late October
([#5577](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5577)): when calibration
fails on a dirty nozzle, the printer should clean it without extruding anything and try
again by itself before giving up; pressing Retry by hand, they find, sometimes gets
through. Both requests are open and unanswered, as is the feature request. The account
of the two retries above is a reading of the code at the v6.9.1 tag, not something an
owner has confirmed by watching both failures on one machine.

**8.0.0 retries one tool, and still purges it.** The 8.0.0 notes Prusa put on GitHub on
3 November, fuller than the downloads page, say that a tool offset calibration that fails
on one tool now repeats only that tool, with a screen and error code of its own for each
kind of failure. The source at the v8.0.0 tag bears out the per-tool retry, but not a
screen for every failure: a failed clean and a failed Z probe, like most other failures,
still share one generic screen (see [what stock 8.0.0 shows](../codes.md#stock-800)). It
also shows what the retry still does. On Retry the printer picks the failed tool again and runs its whole
measurement from the start, preparation included, so that tool alone is heated, purged,
cooled and wiped once more. A failed Z probe no longer sends calibration back to the
first tool. The checks made once every tool has been measured, on how far apart the
tools' offsets lie and on where the sensor appears to sit, still restart the whole pass,
purging every tool again. So the purge these requests ask to drop is still there on
8.0.0, for one tool instead of all; 7.0.0 and 7.0.1 retry as 6.9.2 did. Bed leveling
still probes again without cleaning at the v8.0.0 tag. 7.0.0 did add one automatic retry
of another kind to it: when the mesh comes out too uneven, the printer runs the Z-axis alignment itself,
once, and levels again, asking only if that fails. Nothing on that path cleans the nozzle
either. No owner has yet reported watching either retry on 8.0.0.

### If none of that helps

To find out whether ooze is involved at all, one owner had the printer probe with an
empty tool, so that nothing could ooze; probing failed just the same, which ruled ooze
out for them ([thread](https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/bed-leveling-issues-3/)).
The cause turned out to be an assembly mistake: they had mixed up the bed spacers and
inadvertently refitted the old one; once the correct spacer was in, probing worked.
Single report, but the empty-tool test did its job: it ruled ooze out, and the fault
was mechanical.

If probing fails with the nozzle plainly nowhere near the sheet — a gap you can see
rather than one you would measure — that is a different fault entirely and ooze is
not your problem. See [loadcell noise](loadcell-emi-noise.md). If tool offset
calibration fails regardless of cleanliness and filament state, see
[offset sensor board failure](offset-sensor-board-failure.md).

## Verification

`reported` — the symptom is reported independently by different owners with different
materials.

[PETG oozing and impeding bed probing](https://forum.prusa3d.com/forum/prusa-indx-how-do-i-print-this-printing-help/petg-oozing-and-impeding-bed-probing/)
is the primary thread: the original poster reports PETG oozing enough to spoil bed
probing, and a second owner independently reports the same class of failure with PLA
across every tool during calibration. The thread is marked answered, and its accepted
answer is the sensor-window cleaning, confirmed first-hand by the person who had the
problem. That is the strongest evidence on this page.

Single-source and unverified: the tool-1 temperature derivation, the
declare-a-cool-filament workaround, the G-code override, the slicer configuration
fix, and the hard-coded calibration temperature all come from the
[common problems summary](https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/a-summary-of-common-indx-problems/),
a condensation of a now-offline community knowledge base. None of it is separately
confirmed in the forum corpus, and no numbers from it are reproduced here. The last of
them has now been partly checked, and the check narrows it. A GitHub bug report states
that the calibration temperature changed in 6.9.1 and asks for it to become adjustable
([#5567](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5567)). The firmware
source supports a capped calibration temperature, not one that cannot be changed from
G-code. The
[tool offset calibration](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/src/feature/tool_offset_calibration/tool_offset_calibration.cpp)
at the v6.9.1 tag holds its Z-probe temperature at or below a ceiling of its own and its
XY-probe temperature fixed, and the
[`G427` handler](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/src/marlin_stubs/G427.cpp)
reads only its jitter and repeat arguments, `R` and `P`, so nothing raises either one.
Below the ceiling, though, the Z probe follows the loaded filament's preheat value, and
the
[`M865` handler](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/src/marlin_stubs/M865.cpp)
sets that value, and the purge temperature, on any user-defined or ad hoc filament. The
source comparison on the [annotated profile G-code](../gcode/indx-profile-gcode.md) page
likewise finds that temperature capped in firmware. None of the three files differs
between the v6.9.1 and v6.9.2 tags. At the
[v8.0.0 tag](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/src/feature/tool_offset_calibration/tool_offset_calibration.cpp)
the calibration still works its temperatures out the same way, under the same ceiling,
and `G427` is unchanged;
[`M865`](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/src/marlin_stubs/M865.cpp)
has gained a color parameter but still sets the preheat and nozzle temperatures only on
a filament the printer treats as adjustable. Its new identifier parameters do nothing on
an INDX: the
[build options](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/ProjectOptions.cmake)
at that tag enable the OpenPrintTag support they need only on single-tool builds of the
Core One and its L variant. The Customize button
that makes a loaded preset adjustable lives in the
[filament detail screen](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/src/gui/screen/filament/screen_filament_detail.cpp)
and is new in 7.0.0; nobody has reported using it to change a calibration temperature.

The retry behavior is read from the firmware source at the v6.9.1 tag — the
[bed leveling command](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/lib/Marlin/Marlin/src/gcode/bedlevel/ubl/G29.cpp)
and the
[tool offset calibration](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/src/feature/tool_offset_calibration/tool_offset_calibration.cpp)
— and the 6.9.0 and 6.9.1 beta tags take the same retry paths. The beta changed how they
run, not which steps they take: the per-tool preparation cools further, the XY scan runs
cooler, and the touch on the sensor board gets more attempts before it counts as failed
(see [error codes](../codes.md)). It is recorded because
it accounts for every owner report in that section without contradicting any of them,
but it shows what the code does, not what an owner has watched happen.
Neither source file (the bed leveling command or the tool offset calibration) differs
between the v6.9.1 and
[v6.9.2](https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.9.2) tags, so
the reading holds for 6.9.2 as well. Prusa published the
[7.0.0](https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v7.0.0) and
[8.0.0](https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v8.0.0) tags on
3 November. At v7.0.0 the bed leveling command differs from v6.9.2 only in the uneven-bed
path described above, and the tool offset calibration only in code for printers without
an INDX and in lifting the nozzle clear when calibration gives up, so 7.0.0 retries as
6.9.2 did. [7.0.1](https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v7.0.1),
whose one fix is for a hang at startup, changes neither file. At the v8.0.0 tag the
[bed leveling command](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/lib/Marlin/Marlin/src/gcode/bedlevel/ubl/G29.cpp)
still probes again without cleaning, and the
[tool offset calibration](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/src/feature/tool_offset_calibration/tool_offset_calibration.cpp)
retries the failed tool alone, preparation and purge included
([commit](https://github.com/prusa3d/Prusa-Firmware-Buddy/commit/210606e66889cb636f93de34fcd6bf052367222f);
[compare](https://github.com/prusa3d/Prusa-Firmware-Buddy/compare/v6.9.2...v8.0.0)). As
with the earlier reading, this shows what the code does, not what an owner has watched.

Where the sources disagree: drying was offered confidently as the likely cause for
PETG, but the case that was actually resolved was resolved by cleaning, not drying.
Do not assume moisture just because the filament is PETG — when the question was put
to the original poster directly, they replied that they had been printing straight
from a filament dryer, which rules moisture out for that case entirely.

## Related

- [Probing fails or nozzle never touches the bed](loadcell-emi-noise.md)
- [Tool offset calibration fails](offset-sensor-board-failure.md)
- [Phantom tools and park failures](tool-detection-ringdown-decay.md)
- [Blobs dragged into the print](stringing-and-wiper-calibration.md) — the same
  problem of material in the wrong place, but occurring at tool changes rather than
  during probing. If your deposits appear at tool swaps, start there instead.
