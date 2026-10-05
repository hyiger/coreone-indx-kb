---
title:        Tool unlocks or ejects from the head
confidence:   provisional
updated:      2026-10-04
author:       hyiger
printer:      Core One
toolhead:     INDX
hotend:       unknown
nozzle:       unknown
firmware:     unknown
sources:
  - https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/a-summary-of-common-indx-problems/
  - https://forum.prusa3d.com/forum/postid/804782/
  - https://forum.prusa3d.com/forum/prusa-indx-how-do-i-print-this-printing-help/filament-stuck-with-asa-pla-support/
superseded_by:
---

# Tool unlocks or ejects from the head

!!! warning "Two ejection reports, one teardown, and two stuck-tool reports with different suspects"
    Two owners describe the active tool coming loose from the toolhead. One of them
    opened the head and found a physical cause on their own machine. That is strong
    evidence for that unit and says nothing yet about how common the defect is. A third
    owner in the same thread reports the opposite fault, a tool that will not release,
    and a fourth, in a separate thread, had a tool stuck in the head with its filament,
    not the lock, as the suspect. `provisional`.

## Summary

On some INDX toolheads the active tool works loose from the head — sometimes dropping
out entirely — when the extruder runs backward. It tends to strike during filament
loading and nozzle cleaning, where a retraction follows forward extrusion, and it can
leave the printer unable to recover by itself. One owner traced it to a gear in the
toolhead's locking train with its last tooth missing or malformed. The remedy they
expect is a replacement gear or a replacement toolhead from the vendor.

## Detail

### How the lock is understood to work

The tool is held by a locking pin driven through a small gear train from the extruder
motor. The owners' understanding is that a magnet at the dock shifts part of that
gearing, so reversing the extruder there releases the tool instead of retracting
filament — and that away from a dock, reversing should only ever retract. That is how
the owners in the thread describe it, not vendor documentation, but it is what makes
the failure below make sense.

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
load and cleaning sequence.

### A second owner, less clear-cut

In the same thread another owner reports the tool ejecting from the head during filament
unload near the wiper — with PLA every time, across several brands, but not with PETG
in the same nozzle. They ruled out friction in the PTFE path and tried a hotter nozzle.
They have not opened their toolhead, so whether this is the same gear defect is
unknown. A pattern that depends on the material is not what a missing gear tooth alone
would predict, and this page does not assume the two share a cause.

### A third owner, the opposite fault

Later in the same thread a third owner reports the reverse: the tool stays locked in the
head when it should be released at its dock. Their suspect, which they flag as a guess,
is the small wire that the dock magnet moves. On their head it seems to slip out of the
notch it should sit in and ride up onto the gear, and it has a lot of side-to-side play.
Nudging it back by hand gives a click, and the next Retry then releases the tool; in one
six-color print they had to do that three times. With the head's cover taken off
completely the tool would not release at all — they think the bare head then presses on
the dock's magnet part — so they refitted the stock cover loosely to keep the wire within
reach. They allow that a faulty gear like the first owner's could be the real cause.

This is a lock that fails to open rather than one that opens when it should not, so it
is not the symptom the rest of this page describes. It is recorded here because it
involves the same locking train — the first owner, too, had tools that would not
release as well as tools that fell out.

### A separate thread: a tool stuck in the head, filament suspected

In a [separate thread](https://forum.prusa3d.com/forum/prusa-indx-how-do-i-print-this-printing-help/filament-stuck-with-asa-pla-support/),
an owner printing ASA with PLA as the support material reports that after a few dozen
tool changes the PLA tool stopped parking, which ended the print. The tool stayed in
the head, and the owner took it out by hand with a slight twist and some force. The
strand remained in the nozzle; the stretch the extruder drive grips was tangled,
though not melted. They put it down to heat: the warm chamber ASA needs, and perhaps the rapid tool
changes, softening the PLA high up in the tool. The PLA was already a heat-resistant
grade. The owner asked whether PETG would do better as the support, and the one reply
agreed; no outcome has been posted.

That is the third owner's symptom, a tool that will not leave the head, with a
different suspect, and nobody opened the head. Whether the tangled strand is what held
the tool in, or followed from a release that failed for another reason, is not
established. It is recorded because it points to a cause outside the locking train
that is cheap to rule out, particularly on mixed-material prints in a warm chamber.

### Recovery can loop

When a tool jammed in the head, the first owner found the printer stuck retrying the
dock with only Retry and Abort on offer. After a reboot it reported a tool present
without knowing which one, and went straight back to trying to dock it — which kept
them away from the "Release Stuck Tool" menu item. When they did try that item, the
gears ground and nothing moved.

## What to do

**Contact support early, and film it.** A tool releasing when the extruder is turned
backward by hand is the kind of evidence that settles the question. The owner here had
an escalated ticket open well before finding the cause. See
[who to contact](support-and-warranty-path.md).

**Expect a hardware fix.** No firmware or settings change can put a tooth back on a
gear. The realistic outcomes are a replacement gear with instructions for taking the
toolhead apart, or a replacement toolhead. The third owner above, whose fault is the
opposite one (a tool that stays locked), says Prusa's live chat told them a replacement
head would be sent; it is a single second-hand report, it names no defect, and no
outcome has been posted.

**Ask before you open the head.** Dismantling the toolhead may complicate a warranty
claim the vendor would otherwise honor. And rule out the simpler reasons a tool comes
loose first: a plate or wiper fouling the docks, covered under
[build plate compatibility](../reference/build-plate-compatibility.md), and dock
calibration, covered under
[tool detection and park failures](tool-detection-ringdown-decay.md). If a tool will
not leave the head, look at the filament where the extruder drive grips it before
suspecting the lock; that rests on the single report from the separate thread above.

## Verification

`provisional` — three owners in one thread, and a physical cause found on one machine
only; one owner reports only the opposite fault, a tool that will not release; a fourth
owner, in a separate thread, reports a stuck tool and suspects the filament.

The teardown is first-hand and specific: a named component, a described failure, and a
reproduction that isolates the mechanism by driving the extruder by hand. For that one
toolhead it is about as conclusive as a forum report gets. What it does not establish is
how widespread the defect is — one bad gear, or a batch.

The second owner's report shares the symptom but not, so far, the cause, and its
PLA-only pattern is a reason for caution before treating the two as one fault.

The third owner's report comes from the same thread, describes the opposite fault, and
suspects a different part, so it does not bear on the tier. The replacement head they
say they were promised is their own account rather than the vendor's, and it names no
defect, so it is not the vendor statement asked for below.

The separate-thread report is a single account with no teardown. It describes a tool
that would not leave the head rather than one that fell out, and blames softened
filament rather than any part of the head, so it neither raises the tier nor counts as
a second report of the third owner's fault.

The teardown post was still awaiting moderation on the forum when this page was first
written; it has since been published, and the link shows it. The owner's video and a set
of explanatory animations they found are deliberately not linked: the video sits on a
personal drive, and the animations are on Reddit, which this site does not cite.

What would move this to `reported`: the same missing or deformed tooth found in a
second toolhead, reported in a different thread — or a vendor statement acknowledging
the defect.

## Related

- [Tool detection and park failures](tool-detection-ringdown-decay.md) —
  the other ways a tool fails to stay put
- [Build plate compatibility](../reference/build-plate-compatibility.md) — plates
  that knock tools out of their docks
- [Who to contact](support-and-warranty-path.md)
