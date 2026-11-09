---
title:        Only one nozzle size has a slicer profile
confidence:   reported
updated:      2026-10-25
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
  - https://github.com/prusa3d/PrusaSlicer-settings-prusa-fff/blob/main/PrusaResearch/2.5.11.ini
  - https://github.com/prusa3d/PrusaSlicer-settings-prusa-fff/issues/48
  - https://github.com/prusa3d/PrusaSlicer/releases/tag/version_3.0.0-alpha11
  - https://github.com/prusa3d/PrusaSlicer-settings-prusa-fff/blob/main/PrusaResearch/index.idx
  - https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/firmware-and-slicer-update-to-use-other-nozzles-than-0-4hf/
  - https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/prusa-slicer-does-not-load-other-filaments/
  - https://forum.prusa3d.com/forum/prusa-indx-how-do-i-print-this-printing-help/printing-flex-material-on-indx-prusa-core-one-2-generation/
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.9.1
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.9.2
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/compare/v6.9.1...v6.9.2
  - https://forum.prusa3d.com/forum/prusa-indx-how-do-i-print-this-printing-help/3d-fuel-pctg-pro-profile-for-indx/
  - https://github.com/prusa3d/PrusaSlicer/blob/version_2.9.6/src/slic3r/GUI/MainFrame.cpp
  - https://github.com/prusa3d/PrusaSlicer-settings-prusa-fff/blob/main/PrusaResearch/2.5.12.ini
  - https://help.prusa3d.com/downloads/core-one-indx
  - https://github.com/prusa3d/PrusaSlicer/blob/version_3.0.0-alpha12/resources/presets/prusa-research-fff/PrusaResearch/preset-tool-coreone-indx.yaml
  - https://github.com/OrcaSlicer/OrcaSlicer/tree/v2.5.0-alpha/resources/profiles/Prusa/machine
  - https://github.com/OrcaSlicer/OrcaSlicer/blob/v2.5.0-alpha/docs/HLSD/prusa-indx-profiles.md
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/where-are-all-the-print-profiles/
  - https://forum.prusa3d.com/forum/prusa-indx-how-do-i-print-this-printing-help/nylon-with-indx/
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/set-colormix-colors-in-prusaslicer/
  - https://github.com/Zsoldier/PrusaSlicer-OpenPrintTagImport
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/flex-filament-stuck-and-cannot-dock-tool/
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/indx-review/
  - https://github.com/prusa3d/PrusaSlicer-settings-prusa-fff/blob/main/PrusaResearch/2.5.13.ini
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/i-printed-tpu-on-my-indx/
superseded_by:
---

# Only one nozzle size has a slicer profile

## Summary

PrusaSlicer 2.9.6, the current stable release, offers the INDX exactly one nozzle
variant: high-flow 0.4mm. Buy a 0.25, 0.5, 0.6, 0.8 or 1.0mm nozzle and there is no
profile to select for it there. This is not a case of profiles being thin or unpolished —
the other sizes are not offered at all. The 3.0 alphas choose nozzles differently, but
in the newest of them, alpha 12, the INDX profile has live named print presets for that
same nozzle only, and owners who tried the alphas found no other size either (see below).
OrcaSlicer's first INDX profiles, in its 2.5.0 alpha of 16 October, likewise cover only
the high-flow 0.4mm. Two requests to add the sizes are open upstream, the first since
July 2026; neither has had a response from Prusa, only more commenters asking for the same.
Prusa's latest profile bundle, 2.5.13 of 22 October 2026, still declares only that one
variant, though 2.5.11 and 2.5.12 before it added more groundwork for other sizes, none of
it reachable.

The material side has moved since this page was first written: flexible filament and
BVOH gained INDX slicer presets in September, and PVA a generic one in October with
bundle 2.5.12. HIPS still has none. Printer-side PVA and BVOH presets, announced for
firmware 6.9.1 but left out of it, arrived with 6.9.2 on 7 October and carry over into
7.0.0 (the 7.0.1 and 8.0.0 notes do not mention them); those are the printer's own
presets, not slicer profiles.

Variable nozzle sizes across tools was a headline capability for this toolchanger, so
it is worth knowing before you buy nozzles, and particularly before you take store
credit as nozzle compensation.

## Detail

### What is actually in the bundle

This is checkable rather than a matter of report. Prusa publishes its profile bundle,
and in the current release
([2.5.13](https://github.com/prusa3d/PrusaSlicer-settings-prusa-fff/blob/main/PrusaResearch/2.5.13.ini),
checked on 25 October 2026) both INDX printer models — the four-tool and the
eight-tool — declare a single variant:

```ini
variants = HF0.4
```

That single line is the constraint. A variant is what PrusaSlicer offers you when you
add the printer; with only one declared, PrusaSlicer 2.9.6 offers no other nozzle size,
whatever material profiles may exist behind it.

The variant is high-flow, so a standard-flow nozzle has no variant either, even at
0.4mm. That now matters in practice. In the original thread, one owner reported in
September that their 0.25mm nozzle from the vendor had arrived: Prusa Connect accepted
0.25mm as the tool's nozzle size, but PrusaSlicer 2.9.6 and the 3.0 alpha they tried
offered no preset for it. This page's author replied in the same thread that
standard-flow 0.4 and 0.25 INDX profiles appeared in one 3.0 alpha and were gone from the
next, and another owner there found no way to change the nozzle size in the alpha at all.
That the profiles appeared rests on the author's own report, not an independent one, and
is unverified here, but it makes the 3.0 series worth checking as well as the 2.5.x bundle.
One thing narrows that report: the author placed those profiles in alpha 10, seen before public
release, and Prusa's notes for alpha 11 of 1 September call it
[the first public 3.0 alpha](https://github.com/prusa3d/PrusaSlicer/releases/tag/version_3.0.0-alpha11);
no owner in the sources has found the profiles in a public alpha. Separately, in October a
further owner in the thread, who holds both of those sizes and an HF0.6, agreed that the
profiles are gone again, without saying whether they had seen them.

Prusa's [alpha 11 notes](https://github.com/prusa3d/PrusaSlicer/releases/tag/version_3.0.0-alpha11)
also describe a different mechanism in 3.0: the nozzle size and high-flow status are
chosen per tool in the printer profile rather than declared as printer variants. What
limits the INDX there is therefore which nozzle values its 3.0 profile carries presets
for, not a `variants =` line. In alpha 12, published on 21 September and still the
newest 3.0 alpha on 25 October, the file holding the INDX's
[per-tool print presets](https://github.com/prusa3d/PrusaSlicer/blob/version_3.0.0-alpha12/resources/presets/prusa-research-fff/PrusaResearch/preset-tool-coreone-indx.yaml)
has live named print presets for a high-flow 0.4mm nozzle only; those for high-flow 0.5,
0.6 and 0.8 and for a standard 0.25 are there, commented out, though the shared base
block at the top of the file already carries values for nozzles from 0.25 to 0.8mm.
That agrees with what owners found in
the alphas. This page has not checked the 3.0 filament presets, or run the alpha to see
what its interface offers.

Another slicer is no way around it yet. The owner who opened the third thread described
below asked whether OrcaSlicer had anything for the INDX. Its
[2.5.0 alpha](https://github.com/OrcaSlicer/OrcaSlicer/tree/v2.5.0-alpha/resources/profiles/Prusa/machine),
published on 16 October, adds four- and eight-tool INDX printers, each with a single
high-flow 0.4mm nozzle preset; OrcaSlicer's
[notes on them](https://github.com/OrcaSlicer/OrcaSlicer/blob/v2.5.0-alpha/docs/HLSD/prusa-indx-profiles.md)
say they are translated from Prusa's 2.5.10 bundle.

Later in September, in a separate thread, another owner reported
that the vendor now ships standard nozzles in 0.4 and 0.25mm and asked when firmware and
PrusaSlicer would support them. The replies, all from other owners, added to the queue
rather than answering it: the starter of the original thread said a number of Founders
Edition buyers ordered 0.25 and 0.6mm nozzles with their kits and have yet to see
profiles for them, or for HIPS; one owner holds 0.25 and 0.8mm nozzles; another, still
assembling their kit, has four 0.25mm nozzles lined up for it. Neither Prusa nor the
vendor had replied by 4 October. That the vendor sells a standard 0.4mm nozzle rests
mainly on the opening report. In the original thread, one owner said in August they
planned to spend vendor store credit on standard (non-CHT) 0.4 nozzles, and the October
owner above holds one but does not say where it came from. A second account came in
mid-October from a commenter on the
[first upstream request](https://github.com/prusa3d/PrusaSlicer-settings-prusa-fff/issues/45),
who says the vendor sent them standard 0.25 and 0.4 nozzles some weeks before; nothing in
the sources ties them to either forum thread.

On 18 October a further owner opened a
[third thread](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/where-are-all-the-print-profiles/):
they run an eight-tool INDX, bought 0.25, 0.6 and 0.8mm nozzles, and found no profile
for any of them.

The bundle does contain a large number of INDX-scoped filament entries, and some of the
internal inheritance templates reference wider extrusion widths. So there is groundwork.
Most of it is switched off, though. Over a thousand INDX filament entries sit in the
file commented out, so PrusaSlicer never loads them: base entries with no nozzle in their
names, other materials and brands at HF0.4 (a few of them Prusament), copies for the
high-flow 0.5, 0.6 and 0.8, copies for standard-flow 0.6 and 0.8, and two for 0.25,
Prusament PLA and, since 2.5.11, Prusament PETG. None is named for a standard 0.4, but
more than half of the base entries carry compatibility conditions that exclude high-flow
nozzles, so they match a standard 0.4 among other standard sizes; since 2.5.11 about a
hundred of them, all built on the PLA or PETG templates, match a standard 0.4 and no
other size. (Until October this page said there were no standard
0.4 entries at all; that held only for the names.) Only twenty INDX filament presets
are live (nineteen until 2.5.12), all named for HF0.4, though the two flexible presets'
conditions check only for a 0.4 nozzle, not for high flow. Print presets are further
along: since bundle 2.5.8, six live INDX print presets target 0.25 and 0.3mm nozzles
with no high-flow condition, and printer presets for 0.25, HF0.6 and HF0.8, one each
for the four- and eight-tool models, sit in the file commented out. None of it can be
reached yet, since no live filament preset matches those sizes. For every size but
HF0.4, what is missing first is the printer-side variant declaration; without it,
switching those entries on would still leave nothing to select them with.

Bundle 2.5.11, published on 2 October, is listed in the changelog only for the HT
hotend on the Core One and the larger Core One L, and changes nothing selectable on the
INDX: the same nineteen filament, ten print and two printer presets are live as in
2.5.10. Its INDX changes are all internal or switched off: new filament templates for
PLA and PETG at a 0.25mm nozzle, which the two 0.25 entries now build on; the narrowing
to a standard 0.4 described above; filled-in Prusament PLA and PETG entries for HF0.6;
and the print templates for high-flow 0.5, 0.6 and 0.8mm nozzles, renamed to mark them
as high-flow (the names their commented-out print presets already pointed to) and with
some values revised, though their conditions still check only the nozzle diameter. The
printer-side declaration is still missing, so none of it can be reached either.

Bundle 2.5.12, published on 15 October, the day firmware 7.0.0 came out, leaves the
nozzle side where it was. Both models still declare only `HF0.4`, the same ten print and
two printer presets are live, and the commented-out entries are unchanged in number. Its
[changelog](https://github.com/prusa3d/PrusaSlicer-settings-prusa-fff/blob/main/PrusaResearch/index.idx)
lists three INDX items: a reworked tool change script, covered on the
[annotated G-code page](../gcode/indx-profile-gcode.md); a new firmware version notice;
and a Generic PVA preset, the one selectable addition (see below). Underneath, it adds
shared templates for 0.6 and 0.8mm nozzles, which the existing PLA, PETG, ABS, PC, PA,
FLEX and PP templates for those sizes now build on; only switched-off presets use those
templates. It also begins separate templates whose
conditions name Core One L INDX models, which the bundle does not declare as printers.
None of that can be reached on a Core One INDX.

Bundle 2.5.13, published on 22 October, the day firmware 8.0.0 came out, again leaves the
nozzle side alone: the same single `HF0.4` variant, and the same twenty filament, ten
print and two printer presets live. Its
[changelog](https://github.com/prusa3d/PrusaSlicer-settings-prusa-fff/blob/main/PrusaResearch/index.idx)
lists an updated INDX layer script, which fixes the profile's dock-fan test so that it
takes in PETG (see the [annotated G-code page](../gcode/indx-profile-gcode.md)), and
another firmware version notice. Underneath, it revises one value in the shared template
for 0.8mm nozzles, which only switched-off presets use, and adds two more commented-out
entries, Prusament PA11 at HF0.4 for the Core One INDX and for a Core One L INDX. The
first follows the same pattern as the owner's hand-made entry in the nylon thread
described below, with a Core One nylon preset as the parent and the bundle's INDX nylon
template on top. Prusa's parent is its Core One preset for Prusament PA11, where the
owner's was a different nylon with a second INDX template, for PA6, added; Prusa's entry
also overrides several settings with values of its own. Switched off, it adds nothing
you can select; nylon still has no live INDX preset.

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
- **HIPS** is still absent as of 2.5.13. As in 2.5.7, INDX entries for it exist, but
  only among the commented-out ones. PVA was in the same position until 2.5.12.

**Since bundle 2.5.12** (committed 15 October 2026), per the same changelog and the file:

- **PVA** has one live INDX preset, Generic PVA, at HF0.4. It is built on the Verbatim
  BVOH INDX preset with a few values of its own; its own filament start G-code also
  calls `M906 P2`. The commented-out INDX entries for a branded PVA stay switched off.

The user-facing default material list for both INDX models was described here as the
usual PLA and PETG family, which understated it even in August. As of 2.5.13 it takes
in PLA, PETG, ASA, the PC Blends and Woodfill, and since 2.5.9 TPU 95A, all at the one
available variant; neither soluble material is on it.

**Printer-side PVA and BVOH presets are a different thing, and arrived with firmware
6.9.2.** The [6.9.1 release](https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.9.1)
of 25 September listed them as new, then struck the item because a process error had left
them out of the build. [6.9.2](https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.9.2),
released on 7 October, adds them, and a
[comparison of the two release tags](https://github.com/prusa3d/Prusa-Firmware-Buddy/compare/v6.9.1...v6.9.2)
shows nothing else in it that reaches an INDX. Presets of that kind are the printer's own
filament entries, used when you load a spool at the machine, and do not add a print
profile to PrusaSlicer. So 6.9.2 left BVOH covered at both ends and PVA only at the
printer; since bundle 2.5.12, PVA is covered at both ends too. Firmware 7.0.0 of 15
October keeps the presets, which its
[release notes](https://help.prusa3d.com/downloads/core-one-indx) mark as carried over
from 6.9.2. The notes for 7.0.1 and 8.0.0 do not mention them.

That matters beyond convenience: HIPS and the soluble materials are what you would reach
for to print support interfaces on a toolchanger, which is a large part of why someone
buys one. BVOH and, since 2.5.12, PVA now cover the soluble case at the one nozzle size;
HIPS does not yet.

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

A third way around that catch came up in October, on one owner's report in a
[thread about nylon](https://forum.prusa3d.com/forum/prusa-indx-how-do-i-print-this-printing-help/nylon-with-indx/),
a material with no live INDX preset. Rather than widen a Core One preset, they wrote their
own INDX entry that lists a Core One nylon preset and then the bundle's INDX templates
for nylon as its parents, the same layering Prusa's INDX presets use, so the INDX start
G-code comes with it. They did not say how they loaded it into PrusaSlicer. Their first
print with it failed on a spool that jammed in its dry box, nothing to do with the
profile; the next, a day later, they called a success. That is one print by one owner,
and their settings are not reproduced here.

Two other routes came up in early October, each on one owner's report. The first is a
profile someone else has shared. In October one owner tried to load an INDX filament
profile shared in a [forum thread](https://forum.prusa3d.com/forum/prusa-indx-how-do-i-print-this-printing-help/3d-fuel-pctg-pro-profile-for-indx/)
through File > Import > Import Config, and got a project with nearly every field reading
default. The profile's author, who is this page's author, replied by pointing to Import
Config Bundle in the same menu instead; whether that worked for the asker was not
reported.
[PrusaSlicer's own menu](https://github.com/prusa3d/PrusaSlicer/blob/version_2.9.6/src/slic3r/GUI/MainFrame.cpp)
describes the two differently: Import Config loads a single exported configuration, and
Import Config Bundle loads a set of presets. The owner in the
[flexible-filament thread](https://forum.prusa3d.com/forum/prusa-indx-how-do-i-print-this-printing-help/printing-flex-material-on-indx-prusa-core-one-2-generation/)
had likewise failed to import an .ini found on the forum, without saying how. The second
route came from another owner in that thread in October: an OpenPrintTag importer for
PrusaSlicer, shared on Reddit, which they said works for them, PrusaSlicer 3 included.
The same line goes on to say they then could not find filaments, and the post does not
make clear in which slicer that was or what failed. They did not say which filaments they
used it for, or how its presets are matched to the INDX, and this page has not tried it.
Ten days later, in a
[thread about ColorMix colors](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/set-colormix-colors-in-prusaslicer/),
the same owner linked an OpenPrintTag importer's GitHub repository, presumably the same
tool, and recommended it again for PrusaSlicer 2 and 3; that is the same person, not a
second report. The
[README there](https://github.com/Zsoldier/PrusaSlicer-OpenPrintTagImport) answers the matching question: each imported preset
starts from a filament preset you choose for the target printer and keeps that preset's
printer compatibility and filament G-code, replacing only what OpenPrintTag supplies,
such as temperatures and color. On the INDX that means building on one of the HF0.4
presets, so it can add brands but not nozzle sizes.
None of these routes gives you a profile Prusa has tested.

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

- **Add your voice to the open requests.** The first is
  [issue 45 in Prusa's FFF settings repository](https://github.com/prusa3d/PrusaSlicer-settings-prusa-fff/issues/45),
  open since 31 July 2026 for sizes and materials. It had no comment at all until
  October, when two further commenters added theirs, one asking whether other sizes and
  non-CHT nozzles were coming and one saying their standard nozzles from the vendor
  still had nothing to run on; Prusa had not responded by 25 October. The second,
  [issue 48](https://github.com/prusa3d/PrusaSlicer-settings-prusa-fff/issues/48), was
  filed on 29 September by someone else and asks for the nozzle sizes alone, listing
  0.25, 0.5, 0.6, 0.8 and 1.0; its only comment is the first of those commenters
  repeating the question, and it too had no response from Prusa by 25 October. An issue
  with one reporter and no engagement is easy to leave unattended; several owners saying
  which sizes and materials they actually need is harder to. Note that the September
  material presets arrived with issue 45 untouched, and the 0.25 groundwork in 2.5.11 and
  Generic PVA in 2.5.12 without Prusa answering either issue, so their silence says
  little about progress either way.
- **Take bundle updates as they come.** The INDX presets ship in the profile bundle, not
  with the slicer: the bundle series that carries them requires PrusaSlicer 2.9.6, the
  current release on Prusa's downloads page, and each new bundle reaches it as a
  configuration update rather than a new slicer version.
- **Buy nozzles on the assumption you cannot use them yet**, or wait. That holds for
  PrusaSlicer 2.9.6; OrcaSlicer's 2.5.0 alpha, going by its preset files, ships no
  preset for other sizes either, and nobody in the sources reports trying one in it.
  For the 3.0 alphas it rests on owners' reports and on the alpha 12 profile file, which
  this page has read but not run. If you are choosing compensation, this is an argument
  for cash over credit unless you are content to hold the hardware.

TODO(verify): whether a custom profile can be made to work for another nozzle size by
hand, and what breaks if you try. Nobody in the sources has reported a working attempt.
At the end of September two owners said they meant to try, one for 0.25mm nozzles and
one for 0.25 and 0.8mm nozzles and HIPS; neither had reported back by 4 October. The
nearest thing to an outcome so far is the October owner with an eight-tool INDX, who
built a profile, apparently for the 0.8mm nozzle, and could not get it to show up for one
of their tools, without saying how they built it. Until someone reports more, this page
will not speculate — the toolchanger's purge and calibration behavior is tied to the
profile in ways that are not obvious.

## Verification

`reported`, and the load-bearing part is stronger than that tier requires.

**The central claim is verified, not reported.** That only `HF0.4` is offered comes from
reading Prusa's own published profile bundle, where both INDX printer models declare that
one variant. That is first-party published data, in the same class as a firmware release
note — not somebody's account of their machine. It was re-read at 2.5.13 on 25 October
2026, as were the material presets, the commented-out entries and the compatibility
conditions described above. The 3.0 alpha 12 print-preset file and OrcaSlicer's 2.5.0
alpha printer presets were read on 18 October, in their published source, and neither
slicer had a newer release by 25 October; neither was run.

**The impact is reported**, by six owners in
[one forum thread](https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/missing-profiles-in-slicer-for-non-0-4-nozzles-and-other-materials/),
one of whom bought 0.5 and 1.0mm nozzles before discovering they could not be used,
another who raised it while weighing the nozzle compensation, and two who hold 0.25mm
nozzles with no preset to select. (This page said four until October; the two with
0.25mm nozzles posted after it was first written.) The
[first upstream request](https://github.com/prusa3d/PrusaSlicer-settings-prusa-fff/issues/45)
is a second venue, though it was filed by the same person who started the forum thread,
so it is a cross-post rather than independent corroboration. The
[second](https://github.com/prusa3d/PrusaSlicer-settings-prusa-fff/issues/48) comes from
a different person; nothing in the sources ties it to anyone in either thread. A
[separate thread](https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/firmware-and-slicer-update-to-use-other-nozzles-than-0-4hf/),
started in September by a different owner, asks when the standard-flow nozzles the
vendor now ships will be supported. The opening post is a question rather than an
account of hitting the gap on a machine. Of the three owners who replied, two had
already posted in the original thread; the third, whose 0.25mm nozzles are waiting on
profiles, is still building their kit. It shows the same gap from a second direction,
but adds only two new owners: the one who asked, and the one still building. A
[third thread](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/where-are-all-the-print-profiles/),
opened on 18 October, adds one more owner who bought other sizes and found nothing to
select. The only reply from anyone other than the opener came from this page's author;
the opener's follow-up added that none of Prusa's profiles for other printers had been
carried over to the INDX. On the upstream requests, two further commenters in October
added their own need, one of them on both issues; nothing in the sources ties either to
the forum threads.

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

**The further routes are provisional.** The hand-written nylon entry rests on one owner
in [one thread](https://forum.prusa3d.com/forum/prusa-indx-how-do-i-print-this-printing-help/nylon-with-indx/)
and one successful print; that the INDX templates it names exist is checked against the
bundle, and nothing else about it is. The failed import rests on one owner in
[one thread](https://forum.prusa3d.com/forum/prusa-indx-how-do-i-print-this-printing-help/3d-fuel-pctg-pro-profile-for-indx/),
and the suggested alternative came from this page's author, so it has no independent
confirmation and was never reported to work; whether the flexible-filament owner's
failed import had the same cause is unknown. The OpenPrintTag importer rests on one
owner's word that it works for them, PrusaSlicer 3 included, alongside an unclear remark
in the same post about then not finding filaments; their second recommendation, in
another thread, is the same owner again. What is checked here is how PrusaSlicer's own
menu describes the two import entries, and what the importer's README says it keeps
from the base preset; the importer itself has not been run.

**Where this is weaker than it looks.** Whether FLEX is genuinely usable is unclear: the
templates exist in the bundle but that is not the same as a selectable, tested profile,
and at first no owner in the sources reported having printed with it. Treat the material
findings above as a description of what is in the file rather than of what works. Since 2.5.9 the
flexible and BVOH presets are selectable, which settles the first half of that. The
second half was open until mid-October, when owners in three threads reported printing
flexible filament on the INDX, with mixed results; in two of those threads an owner
names the INDX preset they used. In the
[flexible-filament thread](https://forum.prusa3d.com/forum/prusa-indx-how-do-i-print-this-printing-help/printing-flex-material-on-indx-prusa-core-one-2-generation/),
one owner printed a third-party TPU using the Prusament TPU 95A preset: the first attempt
clogged in the extruder, and after clearing the tool with PLA, a second attempt at a
different layer height, on a PLA base, worked. In a
[thread discussing a published review of the INDX](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/indx-review/),
another owner said a run of multicolor prints in a third-party TPU on the stock CHT
nozzle had gone without trouble, using what they called the generic profiles, and a
day later repeated that TPU had worked for them; they did not say which flex preset
they chose. In a
[thread about a tool that would not dock](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/flex-filament-stuck-and-cannot-dock-tool/),
two owners had a tool stuck on the head with flexible filament jammed around its extruder
gears, one of them while using the Generic FLEX preset. On 24 October, in a
[thread about printing TPU on the INDX](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/i-printed-tpu-on-my-indx/),
a further owner said in passing that they have no trouble printing Prusament TPU 95A,
while asking how to print a softer TPU; the thread is about the INDX, but they named
neither the machine nor the preset. It had opened in August, before the INDX flex
presets existed, with another owner printing a third-party TPU on a standard 0.4 nozzle
the printer did not yet recognize, using a filament profile copied from their
single-tool Core One. None of the threads settles whether the presets are sound; they
show that flex on the INDX can work and can also jam. The successes with the presets
available come from two owners in two threads, enough to call it reported that flex can
print on the INDX, and a third owner implies one; only one of them names the preset, so
anything about the presets themselves stays provisional. The jams come from three owners
across two threads, counting the first owner's first attempt. Firmware 8.0.0,
released on 22 October, slows flexible filament less during nozzle cleaning than earlier
releases did, per its [notes](https://help.prusa3d.com/downloads/core-one-indx); every
report above except the one of 24 October predates it, and that one does not say which
firmware it was on. Nobody in the sources reports printing BVOH or PVA with the presets
yet.

This will date quickly. It is a configuration gap that a profile release closes in a
single update, so check the current bundle before acting on it. It already has, in part:
the material list moved within a month of this page, while the nozzle variants have
not.

## Related

- [Nozzle hardness](nozzle-hardness.md) — the compensation this interacts with
- [Annotated profile G-code](../gcode/indx-profile-gcode.md) — what a profile carries,
  and why the per-tool nozzle declaration matters
