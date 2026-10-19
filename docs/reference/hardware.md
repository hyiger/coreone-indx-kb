---
title:        Hardware
confidence:   unknown
updated:      2026-10-18
author:       hyiger
printer:      Core One, Core One Plus, Core One L
toolhead:     INDX
hotend:       unknown
nozzle:       unknown
firmware:     unknown
sources:
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/core-one-l-with-indx-now-available-assembled-and-upgrade/
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/prusa-core-one-gen-2-indx-shipping-has-started-complete-printers-open-for-orders/
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/prusa-indx-update-shipping-starts-this-week/
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.9.1
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.9.2
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
2026.

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
7 October 2026, names the same two. Firmware 7.0.0 for the INDX, dated 15 October 2026,
had by 18 October appeared only on Prusa's downloads page, not as a GitHub release.
There it sits under a single Core One INDX entry, on a page headed for the Core One/+
INDX, and its notes do not list the two generations separately. The same page carries
a separate 7.0.0 for the Core One L+, dated 5 October 2026, whose notes do not mention
the INDX at all. None of these releases names an INDX-equipped Core One L. Take the
same care between generations as between models wherever a finding involves the belts,
their pulleys or the bed's expansion joints, which are among the parts Gen 2 changes.

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
fixes the availability and the shipping date. The product listings for the
[assembled printer](https://www.prusa3d.com/en/product/prusa-core-one-l-indx-8-tool/) and
the [conversion kit](https://www.prusa3d.com/product/indx-8-tool-conversion-kit-for-core-one-l/)
are given as convenience links only — storefront copy changes, so they are not the
citation. The Gen 2 details come from Prusa's own
[launch post for the Gen 2 INDX](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/prusa-core-one-gen-2-indx-shipping-has-started-complete-printers-open-for-orders/)
and its [shipping announcement](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/prusa-indx-update-shipping-starts-this-week/),
and the firmware naming from the
[6.9.1](https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.9.1) and
[6.9.2](https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.9.2) releases
and, for 7.0.0, from Prusa's
[downloads page](https://help.prusa3d.com/downloads/core-one-indx) as it stood on
18 October 2026. The difference in Founders Edition kits is what their owners report, in
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
    expressly not evidence. And 5 November 2026 is a **stated intention** at the time of
    the announcement, not a date that has passed — treat the shipping claim as a plan,
    and the availability claim as true of August 2026 rather than of whenever you are
    reading this. The Gen 2 paragraph rests on more — Prusa's own posts and release
    notes — and so does the kit-size paragraph, with owners in two separate threads and
    that edition's own guide for the Founders Edition, and Prusa's guide for Prusa's
    kit, but both sit in this section and take its tier. The 7.0.0 naming rests on a
    downloads page that Prusa edits in place, not on a tagged release, and should be
    checked again once a GitHub release appears.

## Verification

`unknown` — nothing else on this page has been checked. No component specification,
revision identifier or measurement should be taken from here until this notice is
removed and the confidence field is set.

## Related

- [Reference index](index.md)
- [Issues](../issues/index.md) — where failures of these components are documented
