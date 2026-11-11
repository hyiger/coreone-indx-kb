---
title:        Tool unlocks or ejects from the head
confidence:   provisional
updated:      2026-11-10
author:       hyiger
printer:      Core One
toolhead:     INDX
hotend:       unknown
nozzle:       unknown
firmware:     unstated on most reporting machines; 6.9.1-beta, 6.9.2, 7.0.1 and 8.0.0 where stated; lock, park and stuck-nozzle code source-checked at 6.9.2 and 8.0.0
sources:
  - https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/a-summary-of-common-indx-problems/
  - https://forum.prusa3d.com/forum/postid/804782/
  - https://forum.prusa3d.com/forum/prusa-indx-how-do-i-print-this-printing-help/filament-stuck-with-asa-pla-support/
  - https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/is-it-worth-upgrading-from-core-one-to-indx/
  - https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/indx-toolhead-looses-tool-when-unloading-filament-and-blobs-after-every-colorchange/
  - https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/tool-dropping/
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/flex-filament-stuck-and-cannot-dock-tool/
  - https://help.prusa3d.com/article/nozzle-tool-remains-attached-to-the-print-head-core-one-indx_1077657
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5532
  - https://help.prusa3d.com/downloads/core-one-indx
  - https://help.prusa3d.com/article/hotend-thermal-runaway-36204-indx_1088706
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/solved-tpu-tangling-at-the-extruder-after-indx-tool-changes-the-nozzle-was-too-cold-during-cleaning/
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v7.0.0
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v7.0.1
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v8.0.0
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/compare/v6.9.2...v8.0.0
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/lib/Marlin/Marlin/src/module/prusa/toolchanger_indx.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/src/feature/indx_tool_lock_hack/indx_tool_lock_hack.hpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/src/feature/indx_tool_lock_hack/indx_tool_lock_hack.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/src/marlin_stubs/M1984.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/src/gui/MItem_tools.hpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/src/common/mapi/parking.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/src/common/mapi/feedrates/standard_feedrates_indx.cpp
  - https://github.com/prusa3d/PrusaSlicer-settings-prusa-fff/blob/main/PrusaResearch/2.5.13.ini
superseded_by:
---

# Tool unlocks or ejects from the head

!!! warning "Six ejection reports in three threads, one teardown, and stuck-tool reports with different suspects"
    Six owners describe the active tool coming loose from the toolhead, four of them in
    one thread, one of those only by saying they have the same problem as another, and
    one in each of two separate threads. One opened the head and found a physical
    cause on their own machine. The owners in the separate threads opened theirs too and
    describe a lock that does not hold, but name no damaged part. The teardown is
    strong evidence for that one unit and says nothing yet about how common the defect
    is. Other owners report the opposite fault, a tool that will not release: one, in
    the first thread, suspects the lock, and owners in two further threads suspect
    filament caught in the drive. `provisional`.

## Summary

On some INDX toolheads the active tool works loose from the head — sometimes dropping
out entirely — when the extruder runs backward. It tends to strike during filament
loading, unloading and nozzle cleaning, where a retraction follows forward extrusion,
and it can leave the printer unable to recover by itself. One owner traced it to a gear
in the toolhead's locking train with its last tooth missing or malformed. The remedy
they expect is a replacement gear or a replacement toolhead from the vendor. Another
owner, in a separate thread, sees the same release in their own toolhead and also ties
it to blobs after every tool change; they say support confirmed a toolhead problem and
offered a replacement head. A third owner, in a third thread, loses the tool on every
unload and has not yet found a cause.

## Detail

### How the lock is understood to work

The tool is held by a locking pin driven through a small gear train from the extruder
motor. The owners' understanding is that a magnet at the dock shifts part of that
gearing, so reversing the extruder there releases the tool instead of retracting
filament — and that away from a dock, reversing should only ever retract. That is how
the owners in the thread describe it, not vendor documentation, but it is what makes
the failure below make sense. Prusa's
[manual-release article](https://help.prusa3d.com/article/nozzle-tool-remains-attached-to-the-print-head-core-one-indx_1077657)
does bear out part of it: the release works only with the tool lined up at its dock or
with a magnet at the front notch where the dock's magnet acts, and away from there,
turning the mechanism can end up driving just the extruder motor while the tool stays
locked. The gear, cam and pin detail remains the owners' account.

Prusa's firmware source, public for 7.0.0, 7.0.1 and 8.0.0 since 3 November 2026, bears
out more of the owners' picture and qualifies one part of it. To pick up a tool, the
printer runs the extruder forward at the dock to lock it; to park one, it jogs the
extruder back and forth to line up the teeth and then runs it backward to open the lock
([toolchanger source](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/lib/Marlin/Marlin/src/module/prusa/toolchanger_indx.cpp)).
A small module written for the INDX says in its comments that the head only finishes
locking once the extruder has fed a little further, and that a retraction before then
would let the tool fall off. So, ahead of the first retraction after each pickup, and
again after power-on, since it keeps no record of the previous run, it slips in a short
forward-and-back move if the extruder has not yet fed far enough
([module source](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/src/feature/indx_tool_lock_hack/indx_tool_lock_hack.hpp),
[startup arming](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/src/feature/indx_tool_lock_hack/indx_tool_lock_hack.cpp)).
Prusa's stock tool-change G-code adds its own short push, commented as the final lock, on
a tool that has already been primed, when no wipe tower is used
([profile bundle 2.5.13](https://github.com/prusa3d/PrusaSlicer-settings-prusa-fff/blob/main/PrusaResearch/2.5.13.ini)).
So, by design, reversing away from a dock does not only ever retract: on a tool just
picked up it could release it, and that guard is what stops it. The module is already in
the published source of 6.6.3, and it and the lock and release sequence are the same in
8.0.0 as in 6.9.2 apart from tidying
([comparison](https://github.com/prusa3d/Prusa-Firmware-Buddy/compare/v6.9.2...v8.0.0)).
This is a reading of the code, not an observed outcome, and it acknowledges no defect.
A tool that comes loose on a retraction after the extruder has already fed forward, as in
the reproduction below, is not explained by the gap the guard covers; that is inference
from the code.

### What went wrong on one machine

The owner took one side of the toolhead off. A gear in the locking train had its final
tooth missing or deformed. Without that tooth the mechanism never reaches the fully
locked position, so the cam that should hold the pin is only partly engaged. The next
time the extruder reverses — as it does for any retraction — that half-engaged gearing
winds the pin back out and the tool drops.

They reproduced it on purpose. With a tool picked up and the nozzle hot, running the
extruder forward kept the tool in place; turning the E axis backward by hand, to
imitate a retraction, released it. That lines up with when the failures happen in
practice: a filament load goes fine because the extruder is moving forward, and the
tool comes out on the retraction that follows.

On that machine it was not subtle. Across a few hundred tool changes the owner never
completed a multi-tool print, and many single-tool prints failed during the opening
load and cleaning sequence. They were on the 6.9.1-beta firmware, which already carried
the guard described above.

### A second owner, less clear-cut

In the same thread another owner reports the tool ejecting from the head during filament
unload near the wiper — with PLA every time, across several brands, but not with PETG
in the same nozzle. They ruled out friction in the PTFE path and tried a hotter nozzle.
They have not opened their toolhead, so whether this is the same gear defect is
unknown. A pattern that depends on the material is not what a missing gear tooth alone
would predict, and this page does not assume the two share a cause.

### A newly converted machine, on 7.0.1 firmware

On 20 October 2026 a fourth owner, replying in the same thread to the first owner's
earliest post there, wrote that they had the same problem. They had just finished
converting their printer and run its calibrations. Tools 1 and 2 loaded filament
normally; on tools 3 and 4 the head made a grinding noise and then the tool came off.
They give their firmware as 7.0.1. They have not opened the head and offer no cause,
and they do not say at which step of the load the tool came off. Like the second
owner, they add the symptom, not the gear.

Five days later a fifth owner answered that post: they were in the same position, and
worse off, because they could no longer unload the filament from the tool. By their
account support's suggestions, among them heating the tool and unloading it and a cold
pull, did not free it, and support had given the tool up as dead. Beyond agreeing with
the post they answered they do not describe the release itself, so they add another
report of the symptom, and of a tool lost after it, but no cause.

### A separate thread: a second toolhead opened

In a [separate thread](https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/indx-toolhead-looses-tool-when-unloading-filament-and-blobs-after-every-colorchange/),
called the unloading thread on the rest of this page, an owner who converted their
Core One to the INDX reports the tool often coming out of the head during filament
unloading. They took one side of the toolhead off and filmed the mechanism. Their
reading is that the lock never closes all the way: the gear at the back does not turn
far enough, and the pin that runs to the front does not rise far enough. In one of their
videos, drawing the filament back released the tool instead of moving the filament —
the same trigger the first owner reproduced by turning the E axis by hand.

They add a quieter symptom. Multi-color prints come out with blobs right after every
tool change, and they put that down to the same fault: the short retraction after the
newly picked-up tool is primed briefly loosens the tool instead of pulling the filament
back, so the filament is barely retracted, if at all. That link is their interpretation
of their own videos; nobody else has reported it.

They do not report a missing or deformed tooth, or any other damaged part. A Prusa staff
member on the forum suggested taking the videos to support. A week after the first post
the owner wrote that support had agreed the head was at fault and offered a new one,
which they were still waiting for on 18 October 2026.

### A third thread: the tool lost on every unload

On 9 November 2026 another owner opened a
[thread of their own](https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/tool-dropping/).
They had fitted the Gen 2 upgrade and an eight-tool INDX to their Core One, and now the
head lets go of the tool whenever they unload filament, including during the filament
sensor calibration. Support had them open one side of the head and film the lock, which
by their account comes undone too soon; the case had been escalated without an outcome.
They name no damaged part, and in a later post they say they plan to open the head again
to look for a broken tooth. They give their firmware only as the latest release. Earlier
they had moved the heated bed wiring away from the toolhead wiring at the main board,
which they say cleared many of the false errors they first saw; that is an interference
fix of the kind described under [loadcell noise](loadcell-emi-noise.md), and it did not
stop the tool coming out.

### A third owner, the opposite fault

Later in the first owner's thread a third owner reports the reverse: the tool stays locked in the
head when it should be released at its dock. Their suspect, which they flag as a guess,
is the small wire that the dock magnet moves. On their head it seems to slip out of the
notch it should sit in and ride up onto the gear, and it has a lot of side-to-side play.
Nudging it back by hand gives a click, and the next Retry then releases the tool; in one
six-color print they had to do that three times. With the head's cover taken off
completely the tool would not release at all — they think the bare head then presses on
the dock's magnet part — so they refitted the stock cover loosely to keep the wire within
reach. They allow that a faulty gear like the first owner's could be the real cause.
They later report fitting a replacement head; how far that account goes is covered
under "What to do" below.

This is a lock that fails to open rather than one that opens when it should not, so it
is not the symptom the rest of this page describes. It is recorded here because it
involves the same locking train — the first owner, too, had tools that would not
release as well as tools that fell out.

### Separate threads: a tool stuck in the head, filament suspected

In a [separate thread](https://forum.prusa3d.com/forum/prusa-indx-how-do-i-print-this-printing-help/filament-stuck-with-asa-pla-support/),
an owner printing ASA with PLA as the support material reports that after a few dozen
tool changes the PLA tool stopped parking, which ended the print. The tool stayed in
the head, and the owner took it out by hand with a slight twist and some force. The
strand remained in the nozzle; the stretch the extruder drive grips was tangled,
though not melted. They put it down to heat: the warm chamber ASA needs, and perhaps the rapid tool
changes, softening the PLA high up in the tool. The PLA was already a heat-resistant
grade. The owner asked whether PETG would do better as the support, and the one reply
agreed; no outcome has been posted.

In [another thread](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/flex-filament-stuck-and-cannot-dock-tool/),
an owner printing flexible filament heard the drive start clicking as extrusion
stopped, and the tool would then not dock. They believe the filament had wound around
the gears and was holding the tool in the head; running the extruder backward only
produced more clicking. They freed it with Prusa's published manual-release procedure (see "What
to do" below). A second owner in that thread hit the same fault with an ordinary TPU.
The published steps did not free their tool at first; with help from Prusa's support
chat they did, and they found the very fine screwdriver they had tried first was too
small to turn the mechanism. They add that the head's side panels come off, which gives
access to pull tangled filament out of the gears.

Both are the third owner's symptom, a tool that will not leave the head, with a
different suspect. Nobody opened a head and confirmed that the filament was what held
the tool, and only in the ASA case was the tangle actually seen; there it could equally
have followed from a release that failed for another reason. Because the release is
driven from the extruder motor through the same gearing (see above), filament jammed in
the drive blocking it is plausible, but that is inference. The pairing is recorded
because it now comes from two unrelated threads and points to a cause outside the
locking train that is cheap to rule out, particularly with flexible filament or with
mixed materials in a warm chamber.

A [later thread](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/solved-tpu-tangling-at-the-extruder-after-indx-tool-changes-the-nozzle-was-too-cold-during-cleaning/)
offers a possible cause for the flexible-filament tangle, though it involves no stuck
tool. On 7 November 2026 an owner on firmware 8.0.0, printing TPU with PLA, reported the
TPU tangling at the extruder whenever the printer returned to that tool, with next to
nothing coming out in the purge; its first layer had printed normally. Reading their
sliced G-code, they put it down to the cleaning step of the stock tool-change G-code:
there the nozzle is brought only to a reduced cleaning temperature before the short push
that finishes locking an already-primed tool, so the push meets filament that has not
melted, and soft TPU buckles. They changed the tool-change G-code for flexible filament
only, raising the cleaning temperature, so the lock push meets warmer filament, and
adding a pause once the nozzle is back at printing temperature, before the filament is
pushed back in, and report clean tool changes since. They made several other
flexible-only changes at the same time without testing them one by one, and say
themselves that the temperature being the key is a guess.

TODO(verify): the stock cleaning-step temperature rule, and the raised
flexible-filament temperature and pause, from the TPU tangling thread; withheld here.

The order of steps they describe matches the stock tool-change G-code in Prusa's profile
bundle 2.5.13 with the wipe tower off, as theirs was, checked here; that a cold push is
what tangles the TPU is their reading, from one printer. They report no stuck tool. But a
strand buckling at the drive is the kind of tangle the flexible-filament owners above
believe held their tools, and this is the first such tangle whose owner traces it to a
specific step of the tool change, so it is worth knowing if you mix flexible and rigid
filament; whether it explains those stuck tools is inference.
Firmware 8.0.0's faster handling of flexible filament does not bear on it. By Prusa's
notes and the
[source](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/src/common/mapi/feedrates/standard_feedrates_indx.cpp),
that change speeds up the firmware's own extruder moves for filaments marked flexible,
not the extruder moves written into the slicer's tool-change G-code, and this owner was
already on 8.0.0.

### Recovery can loop

When a tool jammed in the head, the first owner found the printer stuck retrying the
dock with only Retry and Abort on offer. After a reboot it reported a tool present
without knowing which one, and went straight back to trying to dock it — which kept
them away from the "Release Stuck Tool" menu item. When they did try that item, the
gears ground and nothing moved.

The source, checked at 6.9.2 and 8.0.0, accounts for that pattern without showing a bug.
What follows holds for both: 8.0.0 calls the idle check from a different point in the
firmware's main loop, to fix a deadlock, but under the same conditions
([comparison](https://github.com/prusa3d/Prusa-Firmware-Buddy/compare/v6.9.2...v8.0.0)).
During a print, a failed park is retried automatically
twice and then offers Retry and Abort. Whenever the printer is not actively printing
(idle, or with a print paused) and senses a nozzle it has no record of, it opens a
prompt that lists the docks and tries to
park the tool in the one chosen, and if that park fails it goes back to the list. The menu
item, which the firmware labels "Release Stuck Nozzle" rather than the name the first
owner gave it, runs that same routine
([source](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/src/marlin_stubs/M1984.cpp)),
so reaching it would have led to the same docking attempt, not to a different way out.
Either way the release is the extruder running backward at the dock, so on a head whose
lock or drive is jammed each attempt meets the same obstruction. That is a reading of the
code, not a test.

A [firmware bug report](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5532)
filed by the second owner in the flexible-filament thread, on the day of their stuck
tool, describes another dead end. After an unload had failed, a second unload attempt
asked for the filament type and then sat waiting for the nozzle to heat, which it never
did; the tool could not be parked either. It was filed against 6.9.2 and was still open,
with no reply, on 8 November 2026. Neither the release notes for firmware 7.0.0, nor
those for 7.0.1, dated 19 October 2026, whose single fix is for a printer freezing at
startup, nor those for [8.0.0](https://help.prusa3d.com/downloads/core-one-indx), dated
22 October 2026, list a change to this, to the docking retry loop, or to the stuck-nozzle
item. Nor do the fuller notes Prusa published on GitHub with the source on 3 November
2026, for [7.0.0](https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v7.0.0),
[7.0.1](https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v7.0.1) and
[8.0.0](https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v8.0.0). This page
has not traced the stalled unload itself through the source.

A separate owner describes a similar dead end with a different start, in a comment of
22 October 2026 under
[Prusa's article on the INDX hotend thermal runaway error](https://help.prusa3d.com/article/hotend-thermal-runaway-36204-indx_1088706).
A large blob on their nozzle seemed to be stopping the printer from reading its
temperature, and they could not park the tool, because, as they understand it, the
nozzle has to heat before the extruder motor will run backward to release it. The
source does not bear that out: the park routine does not wait for heat, and the extruder
moves that open the lock are exempted from the check that blocks cold extrusion, so as
the code reads, the release itself does not need a hot nozzle. An error that halts the
printer, or a step that heats first, such as an unload, would be other ways to end up
where they did; that too is a reading of the code, not a test. Even so, taken with the
bug report above, their comment is a second, unrelated case where a nozzle the printer
could not heat, or could not read, came with a tool that would not leave the head. If
yours will not heat, the vendor's manual release under "What to do" below may be the way
out rather than another attempt from the menu; that is inference from these two reports.

## What to do

**Contact support early, and film it.** A tool releasing when the extruder is turned
backward by hand is the kind of evidence that settles the question. The first owner had
an escalated ticket open well before finding the cause. The owner in the unloading
thread contacted support and, by their account, came away with a confirmed toolhead
problem and a replacement offer. See
[who to contact](support-and-warranty-path.md).

**Expect a hardware fix.** No firmware or settings change can put a tooth back on a
gear. The realistic outcomes are a replacement gear with instructions for taking the
toolhead apart, or a replacement toolhead; the owner in the unloading thread was offered
the latter. The third owner above, whose fault is the opposite one (a tool that stays
locked), says Prusa's live chat told them a replacement head would be sent. In a [later thread on another topic](https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/is-it-worth-upgrading-from-core-one-to-indx/)
they say the new head reached them a few days after a short online chat and that they
fitted it. They describe the stuck tool, which meant taking parts off to free it each
time, in the past tense, but do not say in so many words that the new head cured it. It
remains one owner's account of their own case, and it names no defect.

The [release notes for firmware 7.0.0](https://help.prusa3d.com/downloads/core-one-indx),
dated 15 October 2026, list nothing on the tool lock. Nor do those for 7.0.1, dated
19 October 2026, whose single fix is for a startup freeze, or those for 8.0.0, dated
22 October 2026, and the fuller notes on GitHub for all three are silent on it too. As
covered above, the lock and release code is the same in 8.0.0 as in 6.9.2 apart from
tidying. The 7.0.0 notes do move the filament load and unload positions to the
calibrated nozzle cleaner offset. In the
[source](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/src/common/mapi/parking.cpp)
that change shifts those positions, which a comment there says coincide with the park and
purge points over the waste bin, by the cleaner's calibrated offset. So every unload
happens beside the wiper, and "near the wiper" in the second owner's account does not
single out an unusual place. Neither the notes nor the code connect the change to this
fault, and no owner has yet said whether it changes the second owner's ejections. The
owner of the newly converted machine above was on 7.0.1 when two of their tools came off
during a load, but does not say where the head was at the time.

**If a tool is stuck in the head, use the vendor's manual release.** Prusa publishes a
[procedure for a tool that stays attached](https://help.prusa3d.com/article/nozzle-tool-remains-attached-to-the-print-head-core-one-indx_1077657).
In outline: with the printer off, unplugged and cooled, take off the print fan and its
shroud, bring the head to the tool's dock, and turn the release mechanism with a thin
flat screwdriver through the access hole at the center behind the fan, not the rectangular
side hole; a magnet held at the front notch where the dock's magnet acts can help.
Follow the article itself rather than this summary. The article warns that forcing a
screwdriver that is too large can damage the mechanism; one of the flexible-filament
owners above found that one that is too fine will not turn it either.

**Ask before you open the head.** Dismantling the toolhead may complicate a warranty
claim the vendor would otherwise honor. And rule out the simpler reasons a tool comes
loose first: a plate or wiper fouling the docks, covered under
[build plate compatibility](../reference/build-plate-compatibility.md), and dock
calibration, covered under
[tool detection and park failures](tool-detection-ringdown-decay.md). If a tool will
not leave the head, look at the filament where the extruder drive grips it before
suspecting the lock; that rests on the two filament reports in separate threads above.
If flexible filament keeps tangling at tool changes, the TPU thread above has one
owner's fix for the tangle itself.

## Verification

`provisional` — six owners report the tool coming loose, four in one thread, one of them
only by agreeing with another's post, and one in each of two separate threads; a physical
cause was found on one machine only, and the owners in the separate threads, who both
opened their heads, name no damaged part. One owner reports
only the opposite fault, a tool that will not release; owners in two further threads
report a stuck tool and suspect the filament.

The teardown is first-hand and specific: a named component, a described failure, and a
reproduction that isolates the mechanism by driving the extruder by hand. For that one
toolhead it is about as conclusive as a forum report gets. What it does not establish is
how widespread the defect is — one bad gear, or a batch.

The second owner's report shares the symptom but not, so far, the cause, and its
PLA-only pattern is a reason for caution before treating the two as one fault. The
fourth owner's report, in the same thread, also shares only the symptom: no teardown, no
cause. It does not bear on the tier, but it shows the symptom on a newly converted
machine running 7.0.1. The fifth owner's, again in that thread, adds still less: agreement
with the fourth, and a tool that support could not clear afterwards.

Prusa's firmware source is first-party and bears out the mechanism the owners describe:
the lock is driven by the extruder, forward to close and backward at the dock to open,
and a tool just picked up is by design not fully locked until the extruder has fed a
little further, which the firmware guards against. That is a design property, not a
defect, so it neither raises nor lowers the tier. It is not the vendor statement asked
for below, and it does not explain a tool lost on a retraction after forward feeding;
that last point is inference from the code.

The unloading thread comes closest to the bar below without meeting it. It is a second
opened toolhead, in a different thread, from an owner unconnected to the first, with the
same trigger — the extruder reversing away from a dock — and the same reading of the
mechanism, a lock that never closes fully. But no missing or deformed tooth was found or
reported. A lock that does not close fully is what a bad tooth would produce, but it is
not the only thing that could. Support's confirmation and replacement offer reach this
page only through the owner's own post and name no defect, so, like the third owner's
replacement head, they are not the vendor statement asked for below. The link to blobs
after tool changes is that owner's interpretation alone.

The thread opened in November is a third independent thread for the symptom, and a
third head whose lock its owner saw coming undone, but again with no damaged part named,
so it does not meet the bar either. It would if that owner finds a broken or deformed
tooth when they open the head again.

Taken by itself, the symptom — a tool released by reverse extrusion away from a dock —
now comes from independent owners in two different threads, which meets `reported` for
the symptom. The page stays `provisional` because what it adds beyond the symptom is a
cause, and that still rests on one teardown.

The third owner's report comes from the first owner's thread, describes the opposite
fault, and suspects a different part, so it does not bear on the tier. The replacement head they
say they were promised, and later say they received, is their own account rather than
the vendor's, and it names no defect, so it is not the vendor statement asked for below.
That later post sits in a different thread but comes from the same owner, so it is not a
second source either.

The two filament reports, from the ASA thread and the flexible-filament thread, are
independent of each other and of the lock reports, and neither involved a teardown. They
describe a tool that would not leave the head rather than one that fell out, and blame
filament rather than any part of the head, so they neither raise the tier nor count as
further reports of the third owner's fault. The TPU thread is a third independent owner,
but reports a tangle without a stuck tool; it offers a possible cause for the tangle,
from one printer and with several changes made at once, so on its own it is
`provisional`, and it bears on the stuck tools only by inference. The firmware report on
the stuck unload comes from one of the flexible-filament owners, so it is not a separate
source. The comment under Prusa's thermal runaway article is from a different owner. It
is a single account, and its reason for the tool staying put is that owner's
understanding, not anything Prusa's article says; the firmware source, as read here,
does not support it.

The teardown post was still awaiting moderation on the forum when this page was first
written; it has since been published, and the link shows it. The owner's video and a set
of explanatory animations they found are deliberately not linked: the video sits on a
personal drive, and the animations are on Reddit, which this site does not cite.

What would move this to `reported`: the same missing or deformed tooth found in a
second toolhead, reported in a different thread — or a vendor statement acknowledging
the defect. A second head whose lock does not close fully, with no damaged part
identified, is not enough on its own.

## Related

- [Tool detection and park failures](tool-detection-ringdown-decay.md) —
  the other ways a tool fails to stay put
- [Build plate compatibility](../reference/build-plate-compatibility.md) — plates
  that knock tools out of their docks
- [Unload failures from the filament guide bore](filament-guide-bore-unload-failure.md) —
  when an unload fails but the tool stays in the head
- [Who to contact](support-and-warranty-path.md)
