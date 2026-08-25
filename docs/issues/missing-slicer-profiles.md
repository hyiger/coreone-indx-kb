---
title:        Only one nozzle size has a slicer profile
confidence:   reported
updated:      2026-08-25
author:       hyiger
printer:      Core One
toolhead:     INDX
hotend:       CHT high-flow
nozzle:       0.4mm is the only variant offered
firmware:     unknown
sources:
  - https://github.com/prusa3d/PrusaSlicer-settings-prusa-fff/issues/45
  - https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/missing-profiles-in-slicer-for-non-0-4-nozzles-and-other-materials/
superseded_by:
---

# Only one nozzle size has a slicer profile

## Summary

PrusaSlicer offers the INDX exactly one nozzle variant: high-flow 0.4mm. Buy a 0.25,
0.5, 0.6, 0.8 or 1.0mm nozzle and there is no profile to select for it. This is not a
case of profiles being thin or unpolished — the other sizes are not offered at all. A
request to add them has been open upstream since July 2026 with no response.

Variable nozzle sizes across tools was a headline capability for this toolchanger, so
it is worth knowing before you buy nozzles, and particularly before you take store
credit as nozzle compensation.

## Detail

### What is actually in the bundle

This is checkable rather than a matter of report. Prusa publishes its profile bundle,
and in the current release both INDX printer models — the four-tool and the eight-tool —
declare a single variant:

```ini
variants = HF0.4
```

That single line is the constraint. A variant is what PrusaSlicer offers you when you
add the printer; with only one declared, no other nozzle size can be selected, whatever
material profiles may exist behind it.

The bundle does contain a large number of INDX-scoped filament entries, and some of the
internal inheritance templates reference wider extrusion widths. So there is groundwork.
What is missing is the printer-side variant declaration that would make any of it
reachable.

### Materials

The same upstream request also asks for materials. Checking the bundle:

- **FLEX** appears in INDX-scoped templates, so there is at least partial groundwork.
- **HIPS** does not appear in any INDX-scoped section.
- **TPU**, **PVA** and **BVOH** likewise do not.

The user-facing default material list for both INDX models is the usual PLA and PETG
family at the one available variant.

That matters beyond convenience: HIPS and the soluble materials are what you would reach
for to print support interfaces on a toolchanger, which is a large part of why someone
buys one.

### Why this compounds the nozzle compensation

The vendor's remediation for the nozzle hardness issue offers store credit at a higher
rate than cash, and credit naturally suggests buying more nozzles. One owner deciding
between the two pointed out the circularity: they had never tried other nozzle sizes,
because there are no profiles for them.

So credit-for-nozzles is worth less than the headline rate suggests until this is
resolved. Consider that when choosing. See [nozzle hardness](nozzle-hardness.md).

### What you can do

Not much, directly — this is upstream configuration, not something a setting on your
machine changes.

- **Add your voice to the open request.** It is
  [issue 45 in Prusa's FFF settings repository](https://github.com/prusa3d/PrusaSlicer-settings-prusa-fff/issues/45),
  open since 31 July 2026 with no comments and no response at the time of writing. An
  issue with one reporter and no engagement is easy to leave unattended; several owners
  saying which sizes and materials they actually need is harder to.
- **Buy nozzles on the assumption you cannot use them yet**, or wait. If you are
  choosing compensation, this is an argument for cash over credit unless you are content
  to hold the hardware.

TODO(verify): whether a custom profile can be made to work for another nozzle size by
hand, and what breaks if you try. Nobody in the sources has reported attempting it, and
this page will not speculate — the toolchanger's purge and calibration behavior is
tied to the profile in ways that are not obvious.

## Verification

`reported`, and the load-bearing part is stronger than that tier requires.

**The central claim is verified, not reported.** That only `HF0.4` is offered comes from
reading Prusa's own published profile bundle, where both INDX printer models declare that
one variant. That is first-party published data, in the same class as a firmware release
note — not somebody's account of their machine.

**The impact is reported**, by four owners in
[one forum thread](https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/missing-profiles-in-slicer-for-non-0-4-nozzles-and-other-materials/),
one of whom bought 0.5 and 1.0mm nozzles before discovering they could not be used, and
another who raised it while weighing the nozzle compensation. The
[upstream request](https://github.com/prusa3d/PrusaSlicer-settings-prusa-fff/issues/45)
is a second venue, though it was filed by the same person who started the forum thread,
so it is a cross-post rather than independent corroboration.

**Where this is weaker than it looks.** Whether FLEX is genuinely usable is unclear: the
templates exist in the bundle but that is not the same as a selectable, tested profile,
and no owner in the sources reports having printed with it. Treat the material findings
above as a description of what is in the file rather than of what works.

This will date quickly. It is a configuration gap that a profile release closes in a
single update, so check the current bundle before acting on it.

## Related

- [Nozzle hardness](nozzle-hardness.md) — the compensation this interacts with
- [Annotated profile G-code](../gcode/indx-profile-gcode.md) — what a profile carries,
  and why the per-tool nozzle declaration matters
