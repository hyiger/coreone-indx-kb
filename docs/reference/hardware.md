---
title:        Hardware
confidence:   unknown
updated:      2026-08-24
author:       hyiger
printer:      Core One
toolhead:     INDX
hotend:       unknown
nozzle:       unknown
firmware:     unknown
sources:      []
superseded_by:
---

# Hardware

!!! warning "Stub"
    This page is a placeholder. It exists to prove the template, the front matter
    convention and the navigation work end to end. Nothing below has been verified,
    and no specifications have been recorded yet.

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

## Machines the INDX ships on

The INDX is sold both as a conversion kit for a machine you already own and factory
fitted to a complete printer. As of August 2026 the vendor lists it for the Core One
and, newly, for the larger Core One L — the latter as an assembled eight-tool printer
or as a conversion kit for an existing L, with shipping stated to begin 5 November
2026.

This matters for reading the rest of this site. Pages here record the machine a finding
came from in their `printer:` front matter, and a finding from a Core One does not
automatically transfer to an L: the build volume differs, and the assembly notes
describe a chassis that is not the same one.

Sourced from the vendor's own announcement and product listings:
[assembled](https://www.prusa3d.com/en/product/prusa-core-one-l-indx-8-tool/) ·
[conversion kit](https://www.prusa3d.com/product/indx-8-tool-conversion-kit-for-core-one-l/).
Unlike the rest of this page, that paragraph is sourced rather than a placeholder.

## Verification

`unknown` — nothing else on this page has been checked. No component specification,
revision identifier or measurement should be taken from here until this notice is
removed and the confidence field is set.

## Related

- [Reference index](index.md)
- [Issues](../issues/index.md) — where failures of these components are documented
