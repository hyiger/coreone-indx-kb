---
title:        Only one nozzle size has a slicer profile
confidence:   reported
updated:      2026-09-25
author:       hyiger
printer:      Core One
toolhead:     INDX
hotend:       CHT high-flow
nozzle:       0.4mm is the only variant offered
firmware:     unknown
sources:
  - https://github.com/prusa3d/PrusaSlicer-settings-prusa-fff/issues/45
  - https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/missing-profiles-in-slicer-for-non-0-4-nozzles-and-other-materials/
  - https://github.com/prusa3d/PrusaSlicer-settings-prusa-fff/blob/main/PrusaResearch/2.5.10.ini
  - https://github.com/prusa3d/PrusaSlicer-settings-prusa-fff/blob/main/PrusaResearch/index.idx
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/firmware-and-slicer-update-to-use-other-nozzles-than-0-4hf/
  - https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/prusa-slicer-does-not-load-other-filaments/
  - https://forum.prusa3d.com/forum/prusa-indx-how-do-i-print-this-printing-help/printing-flex-material-on-indx-prusa-core-one-2-generation/
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.9.1
superseded_by:
---

# Only one nozzle size has a slicer profile

## Summary

PrusaSlicer offers the INDX exactly one nozzle variant: high-flow 0.4mm. Buy a 0.25,
0.5, 0.6, 0.8 or 1.0mm nozzle and there is no profile to select for it. This is not a
case of profiles being thin or unpolished — the other sizes are not offered at all. A
request to add them has been open upstream since July 2026 with no response. Prusa's
latest profile bundle, 2.5.10 of 17 September 2026, still declares only that one
variant.

The material side has moved since this page was first written: flexible filament and
BVOH gained INDX slicer presets in September. HIPS and PVA still have none; the PVA and
BVOH presets new in firmware 6.9.1 live on the printer and are not slicer profiles.

Variable nozzle sizes across tools was a headline capability for this toolchanger, so
it is worth knowing before you buy nozzles, and particularly before you take store
credit as nozzle compensation.

## Detail

### What is actually in the bundle

This is checkable rather than a matter of report. Prusa publishes its profile bundle,
and in the current release
([2.5.10](https://github.com/prusa3d/PrusaSlicer-settings-prusa-fff/blob/main/PrusaResearch/2.5.10.ini),
re-checked on 25 September 2026) both INDX printer models — the four-tool and the
eight-tool — declare a single variant:

```ini
variants = HF0.4
```

That single line is the constraint. A variant is what PrusaSlicer offers you when you
add the printer; with only one declared, no other nozzle size can be selected, whatever
material profiles may exist behind it.

The variant is high-flow, so a standard-flow nozzle has no variant either, even at
0.4mm. That now matters in practice. In the original thread, one owner reported in
September that their 0.25mm nozzle from the vendor had arrived: Prusa Connect accepted
0.25mm as the tool's nozzle size, but PrusaSlicer 2.9.6 and the 3.0 alpha they tried
offered no preset for it. This page's author replied in the same thread that
standard-flow 0.4 and 0.25 INDX profiles appeared in one 3.0 alpha and were gone from the
next, and another owner there found no way to change the nozzle size in the alpha at all.
That the profiles appeared rests on the author's own report, not an independent one, and
is unverified here, but it makes the 3.0 series worth checking as well as the 2.5.x bundle.
Later that month, in a separate thread, another owner reported
that the vendor now ships standard nozzles in 0.4 and 0.25mm and asked when firmware and
PrusaSlicer would support them; nobody had answered at the time of writing. The
standard 0.4mm part rests on that single report.

The bundle does contain a large number of INDX-scoped filament entries, and some of the
internal inheritance templates reference wider extrusion widths. So there is groundwork.
Most of it is switched off, though. Over a thousand INDX filament entries sit in the
file commented out, so PrusaSlicer never loads them: base entries tied to no nozzle,
other materials and brands at HF0.4 (a few of them Prusament), copies for the high-flow
0.5, 0.6 and 0.8, and copies for standard-flow 0.6 and 0.8 plus a single 0.25. There
are none for a standard 0.4, not even switched off. Only nineteen INDX filament presets
are live, all named for HF0.4, though the two flexible presets' conditions check only for
a 0.4 nozzle, not for high flow. Print presets are further along: since bundle 2.5.8, six
live INDX print presets target 0.25 and 0.3mm nozzles with no high-flow condition, and
printer presets for 0.25, HF0.6 and HF0.8, one each for the four- and eight-tool models,
sit in the file commented out. None of it can be reached yet, since no
live filament preset matches those sizes. For every size but HF0.4, what is missing
first is the printer-side variant declaration; without it, switching those entries on would
still leave nothing to select them with.

### Materials

The same upstream request also asks for materials, and here the bundle has moved.

**As first written (bundle 2.5.7, August 2026) — only what PrusaSlicer loads, templates
as well as presets; partly superseded:**

- **FLEX** appears in INDX-scoped templates, so there is at least partial groundwork.
- **HIPS** does not appear in any INDX-scoped section.
- **TPU**, **PVA** and **BVOH** likewise do not.

Those bullets were accurate only for what PrusaSlicer loads: 2.5.7 already
carried commented-out INDX entries for HIPS, TPU, PVA and BVOH.

**Since bundle 2.5.9** (committed 8 September 2026), per its
[changelog](https://github.com/prusa3d/PrusaSlicer-settings-prusa-fff/blob/main/PrusaResearch/index.idx)
and the file itself:

- **Flexibles** now have live INDX presets: Prusament TPU 95A and Generic FLEX. TPU 95A
  has also joined the default material list for both models. Their filament start
  G-code calls `M906 P2`, the FLEX extruder-current profile that firmware 6.9.0 added.
- **BVOH** has two, both for third-party spools (Verbatim and Fiberlogy). Their start
  G-code calls `M906 P2` too.
- **HIPS** and **PVA** are still absent as of 2.5.10. As in 2.5.7, INDX entries for
  both exist, but only among the commented-out ones.

The user-facing default material list for both INDX models was described here as the
usual PLA and PETG family, which understated it even in August. As of 2.5.10 it takes
in PLA, PETG, ASA, the PC Blends and Woodfill, and since 2.5.9 TPU 95A, all at the one
available variant.

**Firmware 6.9.1 adds PVA and BVOH on the printer, which is not the same thing.** The
[stable release](https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.9.1)
of 25 September lists PVA and BVOH filament presets as new. Those are the printer's own
filament entries, used when you load a spool at the machine; they do not add a print
profile to PrusaSlicer. So BVOH is now covered at both ends, while PVA can be loaded on
the printer but still has no INDX preset to slice it with.

That matters beyond convenience: HIPS and the soluble materials are what you would reach
for to print support interfaces on a toolchanger, which is a large part of why someone
buys one. BVOH now covers the soluble case at the one nozzle size; HIPS and PVA do not
yet.

### Other brands' filament presets

The commented-out entries also explain why a filament installed through PrusaSlicer's
configuration wizard may not be offered for the INDX's tools. One owner installed
several third-party brands that way and found none of them offered for the INDX, though
they appeared elsewhere in the slicer; so far that is the only report for other brands.
Earlier in September, in a separate thread, another owner met the same wall with
flexible filaments: installed through the wizard, yet not selectable on the INDX. That
was three days before bundle 2.5.9 added two INDX flex presets, Prusament TPU 95A and
Generic FLEX, so flexible filament now has presets to select on the INDX, though other
brands' flex entries remain switched off like the rest. The bundle bears both reports
out: its filament presets each carry a compatibility condition naming the printer
models and nozzle they apply to.
The ordinary Core One presets name Core One models, which the INDX does not match, and
the INDX copies that would match are the ones switched off.

The owner with other brands got going by saving the generic preset of the same
material under a new name and entering the filament maker's values into it. Loosening a
Core One preset's compatibility condition to take in the INDX is the other route, with
one catch visible in the file: the INDX presets are not the Core One presets relabeled.
They layer INDX-specific templates on top and replace the filament start G-code, so a
widened Core One preset brings its Core One G-code with it. Either way, the result is a
hand-made profile, not a tested one.

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
  open since 31 July 2026 and still without a comment or response on 25 September. An
  issue with one reporter and no engagement is easy to leave unattended; several owners
  saying which sizes and materials they actually need is harder to. Note that the
  September material presets arrived without the issue being touched, so its silence
  says little about progress either way.
- **Take bundle updates as they come.** The INDX presets ship in the profile bundle, not
  with the slicer: the bundle series that carries them requires PrusaSlicer 2.9.6, the
  current release on Prusa's downloads page, and each new bundle reaches it as a
  configuration update rather than a new slicer version.
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
note — not somebody's account of their machine. It was re-read at 2.5.10 on 25 September
2026, as were the material presets, the commented-out entries and the compatibility
conditions described above.

**The impact is reported**, by four owners in
[one forum thread](https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/missing-profiles-in-slicer-for-non-0-4-nozzles-and-other-materials/),
one of whom bought 0.5 and 1.0mm nozzles before discovering they could not be used, and
another who raised it while weighing the nozzle compensation. The
[upstream request](https://github.com/prusa3d/PrusaSlicer-settings-prusa-fff/issues/45)
is a second venue, though it was filed by the same person who started the forum thread,
so it is a cross-post rather than independent corroboration. A
[separate thread](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/firmware-and-slicer-update-to-use-other-nozzles-than-0-4hf/),
started in September by a different owner, asks when the standard-flow nozzles the
vendor now ships will be supported. That is a question, not an account of hitting the
gap on a machine, but it shows the same gap from a second, independent direction.

**The symptom is reported; the other-brands case is provisional.** Two owners in two
threads found that filaments installed through the wizard could not be selected on the
INDX: one with
[other brands](https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/prusa-slicer-does-not-load-other-filaments/),
and, earlier, one with
[flexible filaments](https://forum.prusa3d.com/forum/prusa-indx-how-do-i-print-this-printing-help/printing-flex-material-on-indx-prusa-core-one-2-generation/).
The second concerns a material that had no live INDX preset at the time and names no
brand, so it corroborates the symptom rather than the brand list. That third-party
brands specifically are affected rests on one owner. The mechanism behind both is read
from the bundle, not taken from either thread.

**Where this is weaker than it looks.** Whether FLEX is genuinely usable is unclear: the
templates exist in the bundle but that is not the same as a selectable, tested profile,
and no owner in the sources reports having printed with it. Treat the material findings
above as a description of what is in the file rather than of what works. Since 2.5.9 the
flexible and BVOH presets are selectable, which settles the first half of that; the
second half stands, since no owner in the sources reports printing TPU, FLEX or BVOH
with them on an INDX.

This will date quickly. It is a configuration gap that a profile release closes in a
single update, so check the current bundle before acting on it. It already has, in part:
the material list moved within a month of this page, while the nozzle variants have
not.

## Related

- [Nozzle hardness](nozzle-hardness.md) — the compensation this interacts with
- [Annotated profile G-code](../gcode/indx-profile-gcode.md) — what a profile carries,
  and why the per-tool nozzle declaration matters
