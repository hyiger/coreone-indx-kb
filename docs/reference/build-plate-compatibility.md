---
title:        Build plate compatibility after the INDX conversion
confidence:   reported
updated:      2026-09-12
author:       hyiger
printer:      Core One
toolhead:     INDX
hotend:       unknown
nozzle:       unknown
firmware:     unknown
sources:
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/update-kind-of/
  - https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/sometimes-tools-dont-stay-in-dock/
superseded_by:
---

# Build plate compatibility after the INDX conversion

## Summary

Oversized third-party flex sheets — the larger plates sold for Bambu-class machines —
stop fitting once the INDX tool docks are installed. The plate's front overhang runs
into the parts mounted on the docks. The trap is that these sheets fit a stock Core One
perfectly well, so if you are converting a printer you already use, your everyday sheet
may quietly stop being usable on the day you finish the build.

It does not always look like a fit problem. The same interference can nudge tools out of
their docks once a print is under way while every calibration passes, which reads as a
docking fault rather than a plate that is too big — and it is not confined to oversized
sheets, because a plate with a different edge profile can do it as well.

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

### It can look like a docking fault

In a separate thread, an owner whose tools were not staying put in their docks — with
dock calibration passing — got two unrelated answers, both pointing at the plate. One
owner had traced that symptom to a larger-than-stock plate catching the wipers carried
on the docks, and added that bent or upside-down wipers are worth checking too.
Another had watched tools get knocked out of their docks after a print started on a
third-party plate whose profile differs from the stock one, again with calibration
passing.

The second case is the one to notice, because that plate was never described as
oversized. What matters is what sits under the docks, not only the footprint. If tools
are being disturbed in their docks, rule the plate out before suspecting magnets or dock
calibration — see [tool detection and park failures](../issues/tool-detection-ringdown-decay.md).

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

`reported` — independent owners, across two different threads.

The [original thread](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/update-kind-of/)
established the interference: one owner raised it, a photograph showed a plate
touching the docks, and two more owners had already trimmed theirs, while a fourth
bought a correctly sized plate. That was held at `provisional`, because every one of
those reports sat in the same discussion.

A second, unrelated [thread about tools not staying docked](https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/sometimes-tools-dont-stay-in-dock/)
has since supplied the cross-thread corroboration this page said it was waiting for.
Two owners there independently put the symptom down to a non-stock plate interfering
with the dock area. That meets this site's bar for `reported`.

It also widens the finding a little. The new reports describe a different presentation
— tools disturbed in their docks, rather than a plate that visibly will not fit — and
one involves a plate nobody described as oversized. The mechanism is unchanged; the
range of symptoms and of affected plates is broader than the original thread showed.

Still unverified: how much of an overhang has to come off, which no source gives, and
whether any particular third-party plate is safe with the docks fitted.

## Related

- [Assembly notes](assembly-notes.md) — worth reading before you start the conversion,
  since this is a "find out on day one" problem
