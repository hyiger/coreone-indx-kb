---
title:        Hardware
confidence:   unknown
updated:      2026-11-08
author:       hyiger
printer:      Core One, Core One Plus, Core One L
toolhead:     INDX
hotend:       unknown
nozzle:       unknown
firmware:     release naming checked for 6.9.1, 6.9.2, 7.0.0, 7.0.1, 8.0.0 and 8.0.1; otherwise unknown
sources:
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/core-one-l-with-indx-now-available-assembled-and-upgrade/
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/prusa-core-one-gen-2-indx-shipping-has-started-complete-printers-open-for-orders/
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/prusa-indx-update-shipping-starts-this-week/
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.9.1
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.9.2
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v7.0.0
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v7.0.1
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v8.0.0
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v8.0.1
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/src/common/printer_variant/printer_variant.hpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/CMakeLists.txt
  - https://help.prusa3d.com/downloads/core-one-indx
  - https://help.prusa3d.com/guide/4-indx-toolhead-side-filament-sensors_1096247
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/update-kit-from-indx-4t-to-8t/
  - https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/sourcing-tool-dock-hardware/
superseded_by:
---

# Hardware

!!! warning "Stub"
    This page is a placeholder. It exists to prove the template, the front matter
    convention and the navigation work end to end. No specifications have been
    recorded yet, and nothing below has been verified **except** the machines the
    INDX is offered for, which carries its own tier inline.

## Summary

Reference for the physical components of an INDX-equipped Core One: what each part
is called, what each sensor measures, and which revision you have.

## Detail

Intended contents, none of it written yet:

- **Toolhead** — the smart head, its induction coil, and how tool presence is
  sensed.
- **Tools and docks** — numbering, dock positions, magnets and mounting hardware.
- **Sensors** — the loadcell used for Z contact against the bed, and the separate
  contactless inductive sensor used for tool offsets. These are distinct parts with
  distinct failure modes and are frequently confused.
- **Controller** — board revisions and how to identify yours, since some reported
  behavior differs by revision.
- **Cabling** — the main toolhead loom and its connectors.
- **Nozzles** — geometries, materials and surface treatments.

## Machines the INDX is offered for

The INDX is sold both as a conversion kit for a machine you already own and factory
fitted to a complete printer. As of August 2026 the vendor lists it for the Core One
and, newly, for the larger Core One L — the latter as an assembled eight-tool printer
or as a conversion kit for an existing L, with shipping stated to begin 5 November
2026. That date has passed with no delivery reported in the announcement thread. On
27 October owners there relayed emails placing their orders in batches due to start on
30 November or, for a later batch, around 14 December; as of 5 November, two owners of
the conversion kit for the L, one of whom ordered on the first day, had been given no
batch at all.

This matters for reading the rest of this site. Pages here record the machine a finding
came from in their `printer:` front matter, and a finding from a Core One does not
automatically transfer to an L: the build volume differs, and the assembly notes
describe a chassis that is not the same one.

On the Core One itself, Prusa sells the complete INDX printer as the Core One+ (Gen 2),
a revision whose changes include new belts, belt pulleys and thermal expansion joints.
It comes assembled or as a kit, in four- or eight-tool form, and Prusa also shipped
the Gen 2 parts with the first batch of its INDX conversion kits, so a converted
Core One may be of either generation. The release notes name them
separately: stable firmware 6.9.1, published 25 September 2026, lists the Core One+
(Gen 2) INDX and the Core One/+ INDX as the machines it supports, and 6.9.2, published
7 October 2026, names the same two. Firmware 7.0.0, 7.0.1 and 8.0.0 reached Prusa's
downloads page first, dated there 15, 19 and 22 October 2026, under a single Core One
INDX entry whose notes did not separate the generations. GitHub releases for all three
followed on 3 November 2026, and those do name the two. 7.0.1, a single fix for a freeze
at startup, is for the Core One+ (Gen 2) INDX and the Core One/+ INDX alone. 7.0.0 and
8.0.0 are each one release for Prusa's whole range, whose list of machines carries the
Core One+ (Gen 2) INDX and the Core One INDX beside the plain Core One+ (Gen 2) and
Core One, the Core One L+ and Core One L, and the rest. Each of the three ships one INDX
firmware file for both generations, and 7.0.0 and 8.0.0 carry a separate file for the
plain Core One; in the source, the generation is a set of switches in the hardware
configuration rather than a separate build (see the
[assembly notes](assembly-notes.md)). 8.0.1, released the same day, is
for the XL and MINI families only, which leaves 8.0.0 the newest INDX firmware as of
8 November 2026. Prusa's notes for 7.0.0 and 7.0.1 say both were published mainly for
completeness and to make their source available, and point owners straight to 8.0.0.
The jump from 7 to 8 within a few weeks follows from a versioning policy that the 7.0.0
notes introduce, under which the first number goes up with every release branched off
the main line of development.

None of these releases names an INDX-equipped Core One L. The L and L+ get one firmware
file in 7.0.0 and in 8.0.0, without INDX in its name, and the downloads page gave the
L+ its own 7.0.0 and 8.0.0 entries and, as of 8 November 2026, lists the plain L with
those same two entries and their shared L/L+ files; none of their notes mention the
INDX. That page offers no INDX firmware for the L either, though its site menu
links to a Core One L+ INDX printer in the shop. Prusa's firmware source does carry an
INDX build target for the Core One L, present in 6.9.1 and still in 8.0.0; that shows
the work exists, not when firmware for it will ship. Take the same care between
generations as between models wherever a finding involves the belts, their pulleys or
the bed's expansion joints, which are among the parts Gen 2 changes.

**Four tools or eight.** Prusa's listing describes the two kit sizes as sharing the
Smart Head and docking hardware and differing only in how many passive tools come with
them. Owners of four-tool Founders Edition kits report one more difference in theirs,
and it matters if you expand later: the second side filament sensor, which serves tools
five to eight, was not in the box. Prusa's own four-tool kit leaves it out too:
Prusa's assembly guide tells a four-tool builder that only the left sensor board, the
one with two connectors, is in the box, and the Founders Edition guide says the same
of its kit. Prusa now sells the right-hand sensor separately. The
[assembly notes](assembly-notes.md) cover what adding tools involves.

Sourced from the vendor's [dated announcement](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/core-one-l-with-indx-now-available-assembled-and-upgrade/) of 27 August 2026, which is what
fixes the availability and the shipping date; the batches owners were given, and the
kit orders still without one, are from later posts in the same thread, as the owners
relay them. The product listings for the
[assembled printer](https://www.prusa3d.com/en/product/prusa-core-one-l-indx-8-tool/) and
the [conversion kit](https://www.prusa3d.com/product/indx-8-tool-conversion-kit-for-core-one-l/)
are given as convenience links only — storefront copy changes, so they are not the
citation. The Gen 2 details come from Prusa's own
[launch post for the Gen 2 INDX](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/prusa-core-one-gen-2-indx-shipping-has-started-complete-printers-open-for-orders/)
and its [shipping announcement](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/prusa-indx-update-shipping-starts-this-week/),
and the firmware naming from the GitHub releases for
[6.9.1](https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.9.1),
[6.9.2](https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.9.2),
[7.0.0](https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v7.0.0),
[7.0.1](https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v7.0.1),
[8.0.0](https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v8.0.0) and
[8.0.1](https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v8.0.1) and the
firmware files attached to them, the last four published 3 November 2026. The October
dates and the L+ entries are from Prusa's
[downloads page](https://help.prusa3d.com/downloads/core-one-indx) as it stood on 18 and
25 October 2026, and the plain L's listing and the lack of INDX firmware for the L from the
same page on 8 November 2026. That the generation is a set of hardware-configuration
switches is from the [8.0.0 source](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/src/common/printer_variant/printer_variant.hpp),
and the build target for the L from its
[CMakeLists.txt](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/CMakeLists.txt),
checked against the 6.9.1 tag. The difference in Founders Edition kits is what their
owners report, in
[a thread on growing a four-tool kit](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/update-kit-from-indx-4t-to-8t/)
and in [one on sourcing dock hardware](https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/sourcing-tool-dock-hardware/).
That Prusa's four-tool kit lacks the sensor too is stated in the
[side filament sensor chapter](https://help.prusa3d.com/guide/4-indx-toolhead-side-filament-sensors_1096247)
of Prusa's guide; the same chapter of the Founders Edition guide says the same of the
Founders Edition kit, which also confirms the owners' reports. The listing's wording
is as an owner relayed it in the thread on growing a four-tool kit, rather than taken
from the storefront.

!!! note "`provisional` — this section only"
    The page as a whole is an unverified stub and declares `confidence: unknown`. This
    section is the exception and carries its own tier, so it is not published outside
    the site's confidence model.

    `provisional` is the honest level for the Core One L: one source supports it, the
    vendor's announcement. The product listings are convenience links and are
    expressly not evidence. And 5 November 2026 was a **stated intention** at the time of
    the announcement; it has now passed with no delivery reported, and the batch dates
    owners have since been given are what they relay from the vendor's emails, in that
    same thread, so they too are plans rather than dates kept. Treat the availability
    claim as true of August 2026 rather than of whenever you are reading this. The Gen 2
    paragraph rests on more — Prusa's own posts and release notes — and so does the
    kit-size paragraph, with owners in two separate threads and that edition's own guide
    for the Founders Edition, and Prusa's guide for Prusa's kit, but both sit in this
    section and take its tier. The naming of 7.0.0, 7.0.1 and 8.0.0 now rests on their
    tagged GitHub releases, as that of 6.9.1 and 6.9.2 does; only their October dates
    and the L+ and L entries come from the downloads page, which Prusa edits in place.
    The build target for the L is a reading of the source, not a product announcement.

## Verification

`unknown` — nothing else on this page has been checked. No component specification,
revision identifier or measurement should be taken from here until this notice is
removed and the confidence field is set.

## Related

- [Reference index](index.md)
- [Issues](../issues/index.md) — where failures of these components are documented
