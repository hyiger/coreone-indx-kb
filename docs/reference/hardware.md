---
title:        Hardware
confidence:   unknown
updated:      2026-08-28
author:       hyiger
printer:      Core One, Core One L
toolhead:     INDX
hotend:       unknown
nozzle:       unknown
firmware:     unknown
sources:
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/core-one-l-with-indx-now-available-assembled-and-upgrade/
superseded_by:
---

# Hardware

!!! warning "Stub"
    This page is a placeholder. It exists to prove the template, the front matter
    convention and the navigation work end to end. No specifications have been
    recorded yet, and nothing below has been verified **except** the machines the
    INDX is offered for, which is sourced.

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

Sourced from the vendor's [dated announcement](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/core-one-l-with-indx-now-available-assembled-and-upgrade/) of 27 August 2026, which is what
fixes the availability and the shipping date. The product listings for the
[assembled printer](https://www.prusa3d.com/en/product/prusa-core-one-l-indx-8-tool/) and
the [conversion kit](https://www.prusa3d.com/product/indx-8-tool-conversion-kit-for-core-one-l/)
are given as convenience links only — storefront copy changes, so they are not the
citation. Unlike the rest of this page, that paragraph is sourced.

## Verification

`unknown` — nothing else on this page has been checked. No component specification,
revision identifier or measurement should be taken from here until this notice is
removed and the confidence field is set.

## Related

- [Reference index](index.md)
- [Issues](../issues/index.md) — where failures of these components are documented
