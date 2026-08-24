---
title:        G-code
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

# G-code

Start, end, layer-change and toolchange blocks; placeholder syntax; and firmware
behaviour that is not obvious from the slicer.

## Why this section exists separately

A toolchanger's G-code carries more load than a single-tool printer's. The start
block has to establish state for tools that are not mounted yet, the toolchange block
runs hundreds of times per print, and a placeholder that resolves differently than
you expect can silently change behaviour for every tool at once.

Several reported INDX faults trace back to G-code and slicer behaviour rather than
hardware — including at least one case where a value used during pre-print probing is
derived from the filament assigned to the first tool rather than the tool doing the
work. Effects like that are worth documenting precisely, because they are invisible
until you know to look.

## What belongs here

- Annotated start and end blocks, with the reason for each line rather than just the
  line.
- Placeholder syntax and what each placeholder actually resolves to.
- Firmware behaviour: which commands are honoured, which are ignored, and which
  parameters are fixed in firmware and cannot be overridden from G-code.
- Toolchange and purge sequences.

## Conventions for pages here

Paste G-code **verbatim** in fenced blocks. Do not reformat, re-indent or "tidy" it —
whitespace and ordering can matter, and a reader will copy it directly.

Any numeric argument that is a print setting rather than a structural part of the
command is subject to the same verification rule as everything else: it is checked on
hardware before it is published. A snippet may name a command while withholding its
argument pending verification.

!!! note "Empty for now"
    Nothing here yet.
