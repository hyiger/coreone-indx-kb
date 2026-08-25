---
title:        Toolhead collides with finished parts — "Complete individual objects"
confidence:   reported
updated:      2026-08-24
author:       hyiger
printer:      Core One
toolhead:     INDX
hotend:       unknown
nozzle:       unknown
firmware:     unknown
sources:
  - https://github.com/prusa3d/PrusaSlicer/issues/14298
  - https://kb.nomadsgalaxy.com/topics/core-one/indx/issues/2
  - https://github.com/prusa3d/Prusa-Firmware-Buddy
superseded_by:
---

# Toolhead collides with finished parts — "Complete individual objects"

!!! danger "Turn the feature off until this is fixed"
    If you slice with **Complete individual objects** and any object contains a tool
    change part-way up, the toolhead can travel across the plate *below the top of
    objects it has already finished* and drive straight into them.

    This is not new and it is not INDX-specific. Prusa acknowledged the same fault on
    the XL in **March 2025**, raised an internal ticket, and it remains open across
    every PrusaSlicer release since. Damage is not limited to the ruined part — the
    collision is into a rigid finished object at travel speed, so the toolhead is at
    risk too, and at least one reporter had a nozzle jam into a part until the noise
    brought someone running.

    Turning the feature off is the only reliable answer. There is a partial workaround
    involving print order, covered below, but the people using it say plainly that it
    works by coincidence.

## Summary

Sequential printing normally lifts the head clear of everything already built before
crossing the plate. That clearance is applied when the machine moves *between* objects.
It is **not** applied when the move is part of a tool change, and a tool change produces
exactly that kind of move. The head goes to the dock and comes back at roughly the
height of the layer it was printing, which on a sequential print may be far below the
top of a neighbour that finished hours ago.

The underlying limitation is in the slicer rather than the machine: the sequential
printing algorithm does not model tool-change travel at all. That is why it affects
Prusa's toolchangers generally rather than the INDX specifically, and why auto-arrange
cheerfully lays out a plate it cannot actually print safely.

## Detail

### What goes wrong

The two cases behave differently, and the difference is the whole bug.

**Starting a new object — clearance is applied.** The previous object is finished, so
the machine raises the head to that object's full height plus a small fixed clearance
before travelling. It crosses the plate safely, drops to first-layer height, and
carries on.

**Changing tool inside an object — clearance is skipped.** The machine is part-way up
object two. It hops to the current layer height, parks, swaps, purges, and returns —
all at around that layer height. The lift that would have carried it over the finished
object never happens. If object one is taller than the layer currently being printed,
the return travel goes through it.

The reported explanation is that the clearance calculation belongs to the
sequential-printing logic, which governs inter-object travel, while tool-change travel
is assembled from the toolchange G-code and firmware macros. Those macros work in
layer-relative terms — where the head is now — and have no knowledge of how tall the
finished objects on the plate are.

TODO(verify): the fixed clearance the machine adds above an object's height when it
does apply the lift. It is named in the source thread but is a single-source figure and
has not been checked against firmware.

### You can see it in the toolchange G-code

That explanation originally came from a diagram in the bug report whose author disclosed
it as machine-generated. It no longer has to rest on that. The behaviour is visible in a
stock toolchange block, and the firmware documents the parameter that governs it.

Three lines in a toolchange decide how high the head travels. From a working profile:

```gcode
G27 W3 Z{travel_max_lift[current_extruder]} P2 R{retract_toolchange} V{...} A{...}
...
G0 Z{layer_z + 0.8} ; Lift        <- on the way into the cleaner
...
G0 Z{layer_z + 1.0} ; Lift        <- on the way back out
```

**The two `G0` lifts are computed from `layer_z`** — the height of the layer currently
being printed. Not from the height of anything already finished. On an ordinary print
every object rises together, so the current layer *is* the tallest thing on the plate and
this is correct. On a sequential print it is simply the wrong reference.

**The park is where it gets interesting.** `G27`'s `P` parameter selects what the Z
movement means, and the firmware documents three options:

| `P` | Z behaviour |
|---|---|
| `0` | *(default)* Raise to at least Z **above print** |
| `1` | Absolute move to Z — may move the nozzle **down** |
| `2` | Relative move by Z |

The profile uses **`P2`**, a relative move. `P0` — the default, and the only one whose
description mentions the print at all — is not used.

So the clearance-aware option exists in the firmware, and the toolchange path does not
take it. That is a considerably firmer footing than "a diagram suggests the macros are
layer-relative", and it is checkable by anyone: open your own toolchange G-code and look
at what those three lines reference.

!!! warning "This identifies the mechanism. It does not hand you a fix."
    It is tempting to read the table above and conclude that changing `P2` to `P0` solves
    it. Resist that until someone establishes what the firmware means by "above print".
    If it tracks only the object currently being built, `P0` changes nothing for this
    case. If it tracks everything completed, it may be the answer. Nobody has checked.

    The two `G0` lifts would also still be layer-relative regardless, so `P0` alone
    could not be the whole story.

    TODO(verify): whether `G27 P0` accounts for objects already completed on a
    sequential print, or only the one in progress.

The annotated block these lines come from, with the rest of the toolchange sequence
explained, is at [annotated profile G-code](../gcode/indx-profile-gcode.md).

!!! danger "A collision may not stop the print"
    The XL reporter notes that crash detection is disabled by default on their
    machine, because phase stepping is enabled during guided setup and the two are
    mutually exclusive. The result in their case was that the nozzle jammed into the
    part and stayed there, grinding, until someone heard it — rather than the
    printer detecting a fault and stopping.

    Whether the same default applies to a Core One INDX is **not established**. If
    it does, the failure mode here is worse than a ruined part: nothing halts the
    machine.

    TODO(verify): whether crash detection is disabled by default on the Core One
    INDX, and whether enabling it would catch a toolchange collision. Worth checking
    before running a sequential multi-tool print, not after.

### Recognising it

- You are slicing with **Complete individual objects**.
- More than one tool is in use anywhere on the plate.
- Objects differ enough in height, or are ordered such that a finished one stands taller
  than the layer being printed elsewhere.
- The damage appears at a **tool change**, not at a layer change or at the start of an
  object.

!!! danger "Tool changes between whole objects are not safe either"
    An earlier version of this page suggested that if your tool changes only ever happen
    *between* whole objects — one object per material, rather than a swap part-way up —
    you were probably not exposed. The INDX reporter was unsure on that point and the
    page said so.

    **The XL thread settles it the other way.** Its original case is precisely one object
    per material with no mid-object swaps, and it crashes. That is the more thoroughly
    documented of the two reports, so treat between-object tool changes as exposed.

    A mid-object swap is not a precondition. Multiple tools on a sequential plate is.

### It has been open on the XL since March 2025

The INDX report is not the first sighting. The same fault was filed against PrusaSlicer
in **March 2025** for the Prusa XL, using the same feature with multiple extruders, and
that thread is the better documented of the two.

What it establishes:

- **Prusa acknowledged it the day it was filed**, raised an internal ticket, and said it
  would be addressed in an upcoming release.
- **It is still open.** Reporters confirm it across PrusaSlicer 2.9.1, 2.9.2 and 2.9.3,
  with comments running into 2026.
- **Roughly seven independent owners** have reported hitting it, all on multi-tool XLs.
- **The slicer gives no warning.** Auto-arrange will lay out a multi-tool sequential
  plate and say nothing about collisions. It *does* warn that you should arrange to
  avoid collisions — but that check does not consider tool changes.
- **The preview will not show you.** Tool-change moves are not drawn in the motion
  preview, so you cannot verify a plate is safe by looking at it.

The mechanism as stated in that thread matches what the G-code shows: tool-change travel
is simply not part of what the sequential algorithm reasons about.

The practical consequence for an INDX owner is that this is not a new bug likely to be
fixed shortly. It is a known, acknowledged, long-unfixed limitation of the feature on
Prusa toolchangers, which the INDX has now inherited.

### What to do

**Disable Complete individual objects** for any plate where an object contains a tool
change. That is the only reliable answer.

If you need both sequential printing and multi-colour parts, the honest answer today is
that you cannot safely have them together — print the multi-colour parts normally, all
objects rising together, and reserve sequential printing for single-tool plates.

!!! warning "The front-to-back workaround reduces exposure. It does not fix anything."
    XL owners report ordering objects **front to back**, so that tool-change travel does
    not need to cross anything already finished. Several say it has been sufficient for
    their prints.

    Read the rest of that thread before relying on it. The same people describe it as
    working "by coincidence", and note it holds only for particular part geometries and
    layouts. It also fails on interruption: a filament runout or a pause can present the
    tool at the front of the bed at a height that then collides on resume, which is
    reported as a separate open fault.

    **And it is XL advice.** Front-to-back works there because of where the XL's
    docks sit relative to the bed. The INDX's dock arrangement is not the same, so
    whether the same ordering reduces exposure on a Core One has not been
    established by anyone. Do not assume the direction transfers.

    So: useful for reducing risk on a print you will be watching, not a basis for
    leaving a long multi-tool sequential job running unattended.

!!! warning "Do not try to patch this in the start G-code"
    It is tempting to add a lift to the toolchange sequence. The travel that collides
    is generated inside the firmware's own macros rather than in the sliced file, so
    editing the sliced G-code does not reliably reach it — and a wrong lift on a
    machine that parks and purges at a station is its own hazard. Wait for a fix.

## Verification

`reported` — two threads on two sites, roughly eight independent reporters between
them, one of which Prusa has acknowledged.

The [source report](https://kb.nomadsgalaxy.com/topics/core-one/indx/issues/2) is
unusually well evidenced for a single thread. It carries video of the collision,
screenshots, and the G-code file that produced it, and it walks through the specific
travel moves in that file — showing the clearance lift present where a new object
begins and absent at a mid-object tool change. Three owners mark themselves as affected.
The thread is open, and the reporter states that prior discussion happened on the
vendor's Discord and that the problem was escalated to Prusa, with no fix released.

This page was `provisional` when first written, on a single INDX report. Two things
moved it.

**The mechanism stopped depending on interpretation.** The explanation originally rested
on a diagram in the INDX report that its author disclosed as machine-generated. It no
longer does: the layer-relative lifts are visible in any stock toolchange block, and
`G27`'s `P` parameter is documented in the firmware source, with `P0` described as
raising above the print and `P2` — the one actually used — as a plain relative move.
Anyone can check both against their own profile in a few minutes. See
[annotated profile G-code](../gcode/indx-profile-gcode.md).

**Independent reports turned up on another machine.**
[PrusaSlicer issue 14298](https://github.com/prusa3d/PrusaSlicer/issues/14298) documents
the same fault on the Prusa XL from March 2025, with around seven distinct owners
reporting it over the following thirteen months across three slicer releases. Prusa
responded the same day, raised an internal ticket, and the issue remains open.

**On treating XL reports as corroboration.** These are a different toolchanger, and
hardware findings from an XL would not transfer to an INDX. This one does, because the
limitation is in the slicer rather than the machine — the same feature, in the same
slicer, failing to account for tool-change travel. What the XL thread corroborates is
the mechanism and the fact that it goes unfixed, not anything about INDX hardware. The
INDX sighting remains a single report; what is no longer single-source is the fault
itself.

No versions are recorded. The thread names neither a firmware nor a slicer version,
which matters here: without one, nobody reading later can tell whether a fix has landed.

What would strengthen it further: a second INDX owner reporting the collision, or an
INDX-specific ticket on the slicer tracker. The existing XL issue is the natural place
to add one — it already has Prusa's attention and an internal ticket, and a report
showing the same fault on a second toolchanger is more useful to them than a fresh
thread. The mechanism being verifiable means such a report can point at the exact
parameter rather than describing symptoms. Note that
the Prusa firmware tracker has nothing on it under this description — the entries there
matching the feature name concern other printers and predate the INDX.

## Related

- [Annotated profile G-code](../gcode/indx-profile-gcode.md) — the full toolchange
  block these three lines come from, annotated
- [Blobs dragged into the print](stringing-and-wiper-calibration.md) — the other place
  tool-change motion damages a print, by a completely different mechanism
- [Phantom tools and park failures](tool-detection-ringdown-decay.md) — also concerns
  what happens around a park, though it is a detection fault rather than a motion one
