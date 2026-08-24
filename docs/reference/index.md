---
title:        Reference
confidence:   unknown
updated:      2026-08-24
author:       hyiger
printer:      unknown
toolhead:     unknown
hotend:       unknown
nozzle:       unknown
firmware:     unknown
sources:      []
superseded_by:
---

# Reference

Hardware specifications, tool numbering, assembly notes, and the vocabulary the rest
of the site assumes.

## Pages

- **[Assembly notes](assembly-notes.md)** — what builders wish they had known before
  starting the conversion: what to print and stage in advance, the handful of steps
  that consistently catch people out, and the dock magnets.
- **[Build plate compatibility](build-plate-compatibility.md)** — oversized
  third-party sheets stop clearing the tool docks once they are fitted, even though
  they fit a stock Core One perfectly well.
- **[Hardware](hardware.md)** — components, revisions, and what each sensor
  actually does.

## What belongs here

Durable facts about the machine rather than findings about how it misbehaves.
Component names and revisions, sensor types and what they measure, tool numbering and
dock positions, connector and cable identification, firmware version history.

The test for whether something belongs here rather than in
[Issues](../issues/index.md) is whether it would still be true on a machine that is
working perfectly. "The offset sensor is eddy-current based" is reference. "The offset
sensor board fails on roughly this many kits" is an issue.

## Why this section carries weight

A lot of INDX troubleshooting depends on naming the right part. Two different sensors
are involved in setting a machine up, they fail with overlapping symptoms, and owners
routinely chase the wrong one — which costs days. Getting the vocabulary right is not
pedantry here; it is the thing that makes the rest of the site usable.

Firmware version strings matter for the same reason. Behaviour has changed across
releases, so a finding without a version attached may be describing a machine that no
longer exists.
