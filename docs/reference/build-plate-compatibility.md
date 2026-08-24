---
title:        Build plate compatibility after the INDX conversion
confidence:   provisional
updated:      2026-08-24
author:       hyiger
printer:      Core One
toolhead:     INDX
hotend:       unknown
nozzle:       unknown
firmware:     unknown
sources:
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/update-kind-of/
superseded_by:
---

# Build plate compatibility after the INDX conversion

!!! warning "Single thread — read the caveat"
    Several owners report this independently and two posted photographs, but all of it
    comes from one forum thread. That is not enough to call it `reported` under this
    site's rules. The physical evidence is good; the sample is narrow.

## Summary

Oversized third-party flex sheets — the larger plates sold for Bambu-class machines —
stop fitting once the INDX tool docks are installed. The plate's front overhang runs
into the parts mounted on the docks. The trap is that these sheets fit a stock Core One
perfectly well, so if you are converting a printer you already use, your everyday sheet
may quietly stop being usable on the day you finish the build.

## Detail

The INDX docks occupy space at the front of the machine that was previously clear.
Plates cut for a larger bed footprint overhang into that space, and the overhang meets
the nozzle seal and anti-ooze parts carried on the docks. One owner circulated a
photograph showing a plate in contact with several of the middle docks.

This is geometry, not firmware. No update will retire it.

**Why it catches people.** Nothing about the conversion suggests your build surface is
affected, and the sheet in question has been fitting the same printer without complaint.
Owners describe these as their go-to plates, which is precisely why the incompatibility
is worth knowing about before you start rather than after.

### What owners did about it

Two routes, both reported first-hand:

- **Fit a plate made for the Prusa footprint.** The simplest answer, and the one to
  reach for first. One owner bought a correctly sized plate and kept the oversized ones
  as spares.
- **Trim the overhang.** Two owners cut theirs down and reported it going easily. A
  rotary cutting disc did the job; the existing holes in the plate served as a
  reference for keeping the cut straight, followed by a deburring pass. A sheet-metal
  guillotine was suggested as a cleaner alternative for anyone with access to one.

    Scoring and snapping was raised and doubted — spring steel does not break along a
    scored line the way thinner sheet does. Nobody reported trying it successfully.

!!! danger "No cut dimension is published here"
    TODO(verify): how much of the overhang needs to come off. **No figure was published
    in the source thread**, and none is invented here.

    This is a cut you cannot undo, on a part that sits directly under a moving
    toolhead, so a wrong number ruins the plate at best. If you trim, measure against
    your own machine with the docks installed rather than working from any figure you
    read online — including this page. Deburr afterwards; a raw cut edge on a sheet you
    handle every print is worth a minute of attention.

    Consider whether a correctly sized plate is simply the better answer. It is
    reversible, it costs less than a ruined sheet, and it removes the question.

## Verification

`provisional` — multiple independent reporters, but a single thread.

Within that thread the evidence is better than the tier suggests. One owner first
raised the interference as a suspicion, and it was then supported by a photograph of a
plate touching the docks, by a second owner who had already cut theirs and posted the
result, and by a third who confirmed the same method and added the technique of using
the plate's holes to guide a straight cut. A fourth sidestepped it by buying a plate in
the Prusa size. That is four owners converging, which would ordinarily read as solid.

What holds it at `provisional` is that this site requires corroboration across
*different* threads, and every one of these reports sits in the same discussion. It is
also worth noting the thread in question is overwhelmingly shipping and order chatter —
this finding surfaced only by reading all of it, and it was one of just two durable
technical items to survive review out of that entire thread.

What would move it to `reported`: a single report from any other thread, or a vendor
statement about plate clearance with the docks fitted.

## Related

- [Assembly notes](assembly-notes.md) — worth reading before you start the conversion,
  since this is a "find out on day one" problem
