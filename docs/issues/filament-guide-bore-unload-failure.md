---
title:        Unload and eject failures — undersized filament guide bore
confidence:   provisional
updated:      2026-09-25
author:       hyiger
printer:      Core One
toolhead:     INDX
hotend:       unknown
nozzle:       unknown
firmware:     unknown
sources:
  - https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/a-summary-of-common-indx-problems/
  - https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/nozzle-stuck-with-filament/
superseded_by:
---

# Unload and eject failures — undersized filament guide bore

!!! warning "Single source for the cause — treat as a lead, not a procedure"
    The explanation on this page comes from one thread, which is itself a condensation
    of a community knowledge base that is now offline. One other owner has since
    described a similar symptom in a separate thread, but nobody in the forum has
    confirmed the cause. It is published because the symptom is distinctive enough to
    be worth recognizing, not because the fix is established.

## Summary

A batch of the printed filament-guide part that sits above the nozzle is reported to
have shipped with its bore narrower than intended — narrower than the swollen end of
a filament strand needs in order to pass back up through it. The result is that
unloading or ejecting filament fails much of the time on an affected tool, while
printing through that same tool works normally. If your unloads fail but your prints
are fine, this is worth knowing about. Contact the vendor for a replacement part.

## Detail

The confusing part of this failure is the asymmetry. Feeding filament down through
the guide and printing with it works, because the filament is going the easy
direction and is not deformed. Unloading pulls the filament back up, and the tip that
has been sitting in a hot nozzle is slightly swollen — so it has to pass back through
the narrowest point in the path in its fattest state. If the bore is undersized, the
swollen tip jams and the unload or eject aborts. On affected tools this is reported
to fail on a large fraction of attempts rather than occasionally.

The reported explanation is a skipped finishing step rather than a design fault. The
affected half of the tool is produced by laser sintering, which leaves the internal
filament path at whatever size it comes out of the machine rather than a controlled one.
Bringing that bore to a defined diameter is a separate operation at the factory — a
drill or reamer run through the path — and affected tools are ones that shipped without
it. The scale is described as small: a handful escaping rather than a whole production
run.

### What to do

**Ask the vendor for a replacement part first.** This is a manufacturing defect in a
consumable printed component, and the reported vendor position is that the finished
bore is supposed to be larger than what shipped. That makes it their part to replace.
See [who to contact](support-and-warranty-path.md).

### About the community fix

The reported community fix mirrors the factory step: hand-twisting a drill bit
through the bore from the coupler end to open it to the intended diameter. It is
reported to have worked on every tracked attempt.

!!! danger "This page will not give you the dimensions"
    TODO(verify): the as-shipped bore diameters measured on affected parts, the
    intended finished diameter, and the drill size used. These are withheld
    deliberately.

    This is the case in the whole knowledge base where a wrong number does the most
    damage. The modification is **irreversible** — you cannot un-drill a hole. Drill
    it undersized and you have not fixed anything; drill it oversized and you have
    ruined a part that guides filament into a hot nozzle, on a machine where that
    part's alignment matters. The warranty position on a self-modified part is also
    unresolved, so doing this may forfeit the free replacement you were entitled to.

    If you decide to do it anyway, get the dimensions from the vendor or from the
    linked source thread and confirm them against your own part with calipers — not
    from this page.

## Verification

`provisional` — one source for the cause, not reproduced; one further report of the
symptom, with the cause unconfirmed.

The source for the cause is the [common problems summary](https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/a-summary-of-common-indx-problems/).
The account there is specific and internally plausible — it names a measured range, an
intended diameter, a vendor confirmation, and a success rate — but specificity is not
corroboration.

A search of the full forum corpus for unload and eject failures turns up one other
thread that fits, in
[the first-prints troubleshooting board](https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/nozzle-stuck-with-filament/).
An owner describes a single tool on which every unload fails and the strand has to be
pulled free by hand, while a print that uses only that tool runs normally and the
machine's other tools are fine. That resembles the signature this page describes, but it
stops short of corroboration. The owner reported no measurement of the bore and never said
what fixed it, although the thread was later marked solved. The undersized-bore
explanation offered in that thread came from this site's author, so it is not an
independent diagnosis. And the account departs from this page in one respect: the
Summary here says printing through an affected tool is unaffected, whereas there the
tool printed normally only when no tool changes were involved — with changes, its
filament jammed or got through only after several attempts.

Another owner in the same thread could never load one of their tools at all. A load
that never succeeds is not what this mechanism predicts, and a nozzle blocked from the
factory (see [nozzle hardness](nozzle-hardness.md)) would explain it as well, so it is
not counted here.

A second account has since been relayed from the vendor's Discord, independent of the
forum thread. It agrees on the mechanism — a finishing pass that brings the sintered
bore to a defined size, omitted on a small number of tools before shipping — and is
what establishes that the part is laser-sintered. That venue has no citable permalink
and this site does not cite Discord, so it is recorded here as corroboration **a reader
cannot check**, and the tier does not move. Two agreeing accounts in two venues
strengthen the mechanism; they are not the two linkable sources `reported` requires.

What would still move this to `reported`: a second owner, in a citable venue, who ties
unload failures on a tool that prints normally to the bore itself — by measuring it, or
by the fault clearing once the bore is finished or the part replaced. A similar symptom
alone, like the one above, is not enough. If you have that, it is the most useful thing
you could add to this page.

## Related

- [Nozzle hardness](nozzle-hardness.md) — the other nozzle-adjacent manufacturing
  defects, including nozzles blocked from the factory
- [Who to contact](support-and-warranty-path.md)
