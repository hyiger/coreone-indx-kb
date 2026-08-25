---
title:        Diagonal banding across print walls
confidence:   reported
updated:      2026-08-24
author:       hyiger
printer:      Core One
toolhead:     INDX
hotend:       CHT high-flow
nozzle:       0.4mm reported
firmware:     unknown
sources:
  - https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/diagonal-banding-2/
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/bondtech-nozzle-hardening-debacle-how-does-this-affect-prusa-indx-orders/
  - https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/a-summary-of-common-indx-problems/
superseded_by:
---

# Diagonal banding across print walls

## Summary

A regular, repeatable diagonal pattern across vertical walls, which reverses direction
depending on whether perimeters run clockwise or counterclockwise, points at the extruder
rather than the motion system. There is a two-print test that settles it in about an
hour without any disassembly, and it is worth running before you open a support case.
A faint version of this artifact appears to be normal for a dual-gear extruder; a
pronounced one is a hardware fault, and the reported remedy is a replacement toolhead.

## Detail

### Why the banding is diagonal

This is the part that makes the fault recognisable, and it is worth understanding
before you test anything.

If something in the extruder varies the amount of filament delivered once per gear
revolution, that variation lands at one specific point on each layer's perimeter. But
the length of a perimeter is almost never an exact multiple of the filament advanced
per gear revolution — so the defect lands at a slightly different place on each
successive layer. Stack those layers and the offsets line up into a diagonal.

Two consequences follow, and both are diagnostic:

- The pattern is **regular and repeatable**, not random.
- It **changes direction** with the perimeter direction, because reversing the
  direction of travel reverses which way the defect walks around the part.

An owner with prior experience of the same phenomenon on a Nextruder traced it to a
fragment of filament stuck to an extruder gear, producing exactly this once-per-
revolution variation.

### Test it before you conclude anything

The thread's accepted answer is a two-print protocol, and it is the most valuable
thing on this page. It isolates extrusion from motion:

**Print one**

1. Start a **new project in PrusaSlicer using stock profiles**. Do not carry over
   your own tuning — the point is a clean baseline.
2. Add a **box**.
3. **Rotate it 45° about Z.** This matters: at 45° the X and Y motor systems are each
   exercised separately by different walls.
4. Turn on **vase mode**.
5. Print it.

If you have this fault, you will see clear diagonal banding on **all four walls**.

**Print two**

Identical to the first, changing exactly one thing: **increase the external perimeter
width slightly** from the stock default. Do not move the box. Do not change anything
else.

If you have this fault, the **pitch and angle of the banding will shift** — subtly,
but unmistakably.

TODO(verify): the stock external perimeter width and the value to change it to. Any
modest increase serves the purpose, since the test depends on the pattern *changing*
rather than on a particular width, so the method above is complete without them. The
figures are withheld pending verification because they are slicer settings.

**Why this works.** Between the two prints the toolhead traces very nearly the same
path at very nearly the same speeds — the XY motion is essentially identical. Only the
extrusion differs. So if the banding changes, the cause cannot be in the XY motion
system, and you have eliminated belts, rails, steppers and gantry alignment in one
step. That is a lot of expensive suspects ruled out by two test cubes.

### What this rules out, and what people chased first

The thread's author explicitly retracted the early theories and asked readers to
disregard everything before the accepted answer. Worth recording, because these are
the natural first guesses and all of them were dead ends here:

- **Part cooling** — a plausible theory, since inconsistent cooling does band prints.
- **Wet filament** — including the specific case of a spool dried unevenly, which
  produces convincingly similar banding.
- **Nozzle and profile mismatch** — such as running one nozzle geometry while slicing
  for another.

None of these accounted for a pattern that survived across materials and tracked
perimeter direction. If your banding *does* respond to drying the filament, you have a
different and much cheaper problem.

### Check the cheap thing first

Before pursuing a replacement, **inspect and clean the extruder gears**. A fragment of
filament adhering to a gear tooth produces precisely the once-per-revolution variation
described above, and it costs nothing to rule out.

### Some banding is inherent

Several owners in the thread report seeing a faint version on glossy filaments — one
describing it as the sort of thing you cannot unsee once noticed. The consensus among
them is that dual-drive extruders at this price point generally show some periodic
extrusion signature, and that the single-drive design of the Nextruder is why owners
did not see it there.

So the question is not *whether* the artifact exists but *how pronounced* it is.
Faint and only visible on glossy filament at the right angle is expected. Clearly
visible across all four walls of a stock-profile test cube is not.

### What it appears to be

The most detailed analysis in the thread, and the most recent, attributes it to poor
meshing where the extruder motor's pinion drives the first spur gear in the
reduction train. The reasoning works through the reduction ratios to establish how much
filament advances per tooth of the motor pinion, and finds that figure consistent with
the observed band spacing — which points at the **first reduction stage** specifically
rather than at the hobbed gear that grips the filament.

Another owner suggests the underlying cause is gears that are not perfectly round,
not perfectly concentric, or imperfectly aligned, with severity varying unit to unit —
which would make this a quality-control spread rather than a design flaw.

TODO(verify): the gear ratios, the filament advance per pinion tooth, and the
resulting expected band pitch. The owner who derived these described one input as an
estimate, so the numbers are withheld; the *conclusion* — band spacing matching one
tooth of the first reduction stage — is the reportable part and needs none of them.

### Getting it fixed

For a pronounced case the reported route is a **toolhead replacement** through the
vendor, since at the time of writing the fault had not been narrowed to an
individually replaceable part. See [who to contact](support-and-warranty-path.md).

!!! warning "Check the replacement before you celebrate"
    The owner whose case drives this page received a replacement toolhead that cured
    the banding but arrived with a **different fault** — an unreliable loadcell, with
    homing and probing taking excessively long and most prints failing to start with a
    prompt to recalibrate Z.

    Two things make that case instructive. The fault **followed the toolhead** across
    the swap while the original toolhead homed perfectly every time, and the machine's
    controller board was recent. That combination is what distinguishes a genuine
    hardware fault from the electrical-interference version of the same symptom — see
    [loadcell noise](loadcell-emi-noise.md), where a ferrite core is the usual answer.
    A ferrite treats interference; it will not fix a bad loadcell.

    Run a probing and homing check on any replacement head before you commit a long
    print to it.

## Verification

`reported` — but read the qualification, because the evidence is uneven across the
claims on this page.

**Well supported.** The artifact itself is described by five different participants in
[the diagonal banding thread](https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/diagonal-banding-2/),
ranging from severe to barely perceptible on glossy filament, so the phenomenon is not
one person's imagination. The thread is marked answered and runs to 78 posts. The
two-print protocol is its accepted answer, written by the owner who worked the problem
with vendor and Prusa support involvement, and the reasoning for why it isolates
extrusion from motion is sound on its own terms.

**Single-source.** The severe case, the replacement-toolhead outcome, and the
follow-on loadcell fault are all one owner's experience. The
[common problems summary](https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/a-summary-of-common-indx-problems/)
independently records a severe banding case as vendor-confirmed to be a defective
extruder unit, which corroborates the conclusion but may well be describing the same
case rather than a second one.

**Analysis, not measurement.** The gear-meshing explanation is one owner's calculation,
posted shortly before this page was written, with the vendor not yet having responded.
It is coherent and specific, but it has not been confirmed by anyone with access to
the parts. Treat it as the best available hypothesis.

**A caution on the second source.** The banding discussion in the
[nozzle hardening thread](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/bondtech-nozzle-hardening-debacle-how-does-this-affect-prusa-indx-orders/)
is the *same* owner raising the problem in another thread, so it is not an independent
report of the fault. It earns its place here for a different reason: it is where
another owner supplied the stuck-filament-fragment mechanism from prior Nextruder
experience, which is the clearest explanation in the corpus of why the banding is
diagonal, and which yields the cheap gear-cleaning check.

What would strengthen this page: a second owner running the two-print protocol and
reporting the result, and any vendor statement identifying the specific part.

## Related

- [Blobs dragged into the print](stringing-and-wiper-calibration.md) — the other
  print-quality page; unrelated cause, but both show up as surface defects
- [Probing fails or nozzle never touches the bed](loadcell-emi-noise.md) — relevant if
  a replacement toolhead brings a probing fault with it
- [Who to contact](support-and-warranty-path.md) — the replacement route
