---
title:        Toolhead collides with finished parts — "Complete individual objects"
confidence:   provisional
updated:      2026-08-24
author:       hyiger
printer:      Core One
toolhead:     INDX
hotend:       unknown
nozzle:       unknown
firmware:     unknown
sources:
  - https://kb.nomadsgalaxy.com/topics/core-one/indx/issues/2
superseded_by:
---

# Toolhead collides with finished parts — "Complete individual objects"

!!! danger "Turn the feature off until this is fixed"
    If you slice with **Complete individual objects** and any object contains a tool
    change part-way up, the toolhead can travel across the plate *below the top of
    objects it has already finished* and drive straight into them.

    There is no setting to correct it and no firmware fix as of late August 2026. The
    only mitigation reported is to stop using the feature. Damage is not limited to the
    ruined part — the collision is into a rigid finished object at travel speed, so the
    toolhead is at risk too.

## Summary

Sequential printing normally lifts the head clear of everything already built before
crossing the plate. That clearance is applied when the machine moves *between* objects.
It is reportedly **not** applied when the move is part of a tool change, and a tool
change in the middle of an object produces exactly that kind of move. The head goes to
the dock and comes back at roughly the height of the layer it was printing, which on a
sequential print may be far below the top of a neighbour that finished hours ago.

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

### Recognising it

- You are slicing with **Complete individual objects**.
- At least one object has a **tool change part-way up** — a colour swap mid-object, not
  merely different tools on different objects.
- Objects differ enough in height, or are ordered such that a finished one stands taller
  than the layer being printed elsewhere.
- The damage appears at a **tool change**, not at a layer change or at the start of an
  object.

If your tool changes only ever happen *between* whole objects, you are probably not
exposed — but the reporter says plainly they are unsure about that case, so do not treat
it as safe on this page's authority.

### What to do

**Disable Complete individual objects** for any plate where an object contains a tool
change. That is the only mitigation reported.

If you need both sequential printing and multi-colour parts, the honest answer today is
that you cannot have them together on this machine — print the multi-colour parts
normally, all objects rising together, and reserve sequential printing for single-tool
plates.

!!! warning "Do not try to patch this in the start G-code"
    It is tempting to add a lift to the toolchange sequence. The travel that collides
    is generated inside the firmware's own macros rather than in the sliced file, so
    editing the sliced G-code does not reliably reach it — and a wrong lift on a
    machine that parks and purges at a station is its own hazard. Wait for a fix.

## Verification

`provisional` — one thread, one detailed reporter, no independent corroborating source.

The [source report](https://kb.nomadsgalaxy.com/topics/core-one/indx/issues/2) is
unusually well evidenced for a single thread. It carries video of the collision,
screenshots, and the G-code file that produced it, and it walks through the specific
travel moves in that file — showing the clearance lift present where a new object
begins and absent at a mid-object tool change. Three owners mark themselves as affected.
The thread is open, and the reporter states that prior discussion happened on the
vendor's Discord and that the problem was escalated to Prusa, with no fix released.

**Two things hold this at provisional rather than higher.** It is a single thread on a
single site, where this knowledge base requires corroboration across different sources.
And the root-cause diagram in that thread is disclosed by its author as
machine-generated — so the *observation* (the head travels low and collides) rests on
video and G-code and is solid, while the *explanation* of why is an interpretation
layered on top of that evidence and has not been confirmed against firmware source by
anyone. This page follows that explanation because it fits the evidence, not because it
has been independently verified.

No versions are recorded. The thread names neither a firmware nor a slicer version,
which matters here: without one, nobody reading later can tell whether a fix has landed.

What would move this to `reported`: a second owner describing the same collision in a
different thread, a firmware issue filed against it, or a vendor statement. Note that
the Prusa firmware tracker has nothing on it under this description — the entries there
matching the feature name concern other printers and predate the INDX.

## Related

- [Blobs dragged into the print](stringing-and-wiper-calibration.md) — the other place
  tool-change motion damages a print, by a completely different mechanism
- [Phantom tools and park failures](tool-detection-ringdown-decay.md) — also concerns
  what happens around a park, though it is a detection fault rather than a motion one
