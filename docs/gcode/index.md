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

Two cases, and they are treated differently.

A **snippet** — a few lines offered as something to adopt — is advice, and every numeric
argument in it is a print setting subject to the usual rule: verified on hardware before
publication, or named with its argument withheld.

A **complete profile**, reproduced verbatim and annotated, is an artifact rather than
advice. Its literals are part of what is being documented and are reproduced as they
stand. Such a page is tiered `measured`, states which firmware version the profile came
from, and says whether it is the shipped default or somebody's customisation — those are
very different claims. Do not extract a value out of one and present it as a
recommendation: reproducing a default is describing what the machine does, whereas
recommending it is advice, and advice needs the verification advice requires.

## Pages

- **[Annotated start, layer and toolchange G-code](indx-profile-gcode.md)** — a complete
  working INDX profile reproduced verbatim and annotated line by line, with every
  command checked against the firmware source that implements it.
