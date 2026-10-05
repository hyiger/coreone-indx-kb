---
title:        Hardware
confidence:   unknown
updated:      2026-09-25
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
(Gen 2) INDX and the Core One/+ INDX as the machines it supports. Take the same care
between generations as between models wherever a finding involves the belts, their
pulleys or the bed's expansion joints, which are among the parts Gen 2 changes.

**Four tools or eight.** Prusa's listing describes the two kit sizes as sharing the
Smart Head and docking hardware and differing only in how many passive tools come with
them. Owners of four-tool Founders Edition kits report one more difference in theirs,
and it matters if you expand later: the second side filament sensor, which serves tools
five to eight, was not in the box. Whether Prusa's own four-tool kit leaves it out too
rests so far on one owner's second-hand statement; Prusa now sells that sensor
separately, which fits, but is not a report. The [assembly notes](assembly-notes.md)
cover what adding tools involves.

Sourced from the vendor's [dated announcement](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/core-one-l-with-indx-now-available-assembled-and-upgrade/) of 27 August 2026, which is what
fixes the availability and the shipping date. The product listings for the
[assembled printer](https://www.prusa3d.com/en/product/prusa-core-one-l-indx-8-tool/) and
the [conversion kit](https://www.prusa3d.com/product/indx-8-tool-conversion-kit-for-core-one-l/)
are given as convenience links only — storefront copy changes, so they are not the
citation. The Gen 2 details come from Prusa's own
[launch post for the Gen 2 INDX](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/prusa-core-one-gen-2-indx-shipping-has-started-complete-printers-open-for-orders/)
and its [shipping announcement](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/prusa-indx-update-shipping-starts-this-week/),
and the firmware naming from the
[6.9.1 release](https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.9.1).
The difference in Founders Edition kits is what their owners report, in
[a thread on growing a four-tool kit](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/update-kit-from-indx-4t-to-8t/)
and in [one on sourcing dock hardware](https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/sourcing-tool-dock-hardware/).
The second-hand statement about Prusa's kit is in the first of those, and so is the
listing's wording, as an owner relayed it rather than taken from the storefront.

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
    notes — and so does the Founders Edition half of the kit-size paragraph, with
    owners in two separate threads, but both sit in this section and take its tier.
    What that paragraph says about Prusa's own four-tool kit is one owner's second-hand
    statement, provisional on its own account.

## Verification

`unknown` — nothing else on this page has been checked. No component specification,
revision identifier or measurement should be taken from here until this notice is
removed and the confidence field is set.

## Related

- [Reference index](index.md)
- [Issues](../issues/index.md) — where failures of these components are documented
