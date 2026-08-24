---
title:        Phantom tools, "tool not detected" and park failures
confidence:   reported
updated:      2026-08-24
author:       hyiger
printer:      Core One
toolhead:     INDX
hotend:       unknown
nozzle:       unknown
firmware:     6.6.3, 6.9.0
sources:
  - https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/6-9-0-firmware-tool-docking/
  - https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/a-summary-of-common-indx-problems/
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/will-the-prusa-indxs-wave1-ship-with-fixed-induction-coils/
superseded_by:
---

# Phantom tools, "tool not detected" and park failures

## Summary

The INDX decides whether a tool is present by pinging an induction coil in the head
and measuring how the ringing dies away — the firmware calls this the *ringdown
decay* value. There is a band in the middle of the scale where the reading is
ambiguous, and in that band the firmware keeps whatever it last believed. That single
design detail explains most of the confusing behaviour in this family: why a wrong
tool state persists, why it survives a retry, and why two machines with opposite
symptoms can have the same underlying cause.

## Detail

Readings come out at one of three conclusions: clearly no tool, clearly a tool, or
ambiguous. In the ambiguous middle the firmware holds the last known state rather
than guessing. That is a sensible design, but it means a machine whose readings sit
in or near that middle band gets *sticky* wrong answers instead of intermittent ones.

TODO(verify): the low and high threshold values, and the readings that distinguish a
healthy head from a marginal one. These are quoted in the common-problems summary and
were confirmed there against firmware source, but they are deliberately withheld
here — see the warning below about why publishing them is risky. Where the firmware
exposes the live value, it is readable from the printer's sensor information screen.

### Two opposite symptoms, one mechanism

**Reads a tool that is not there (phantom tool).** The head's idle reading sits high
enough to be taken as "tool present" when the head is empty. On current firmware this
also shows up as *park* failures: an owner on 6.9.0 reports regularly getting "The
tool is still detected after parking", where the tool has in fact parked correctly
and a retry always succeeds. The machine is not failing to park; it is failing to
believe the tool has left.

**Reads no tool when one is fitted.** The mirror image: a real tool picked up from the
dock reads just below the "tool present" conclusion, so the firmware reports the tool
was not detected after pickup. A distinguishing feature is that it tends to happen
at the *same dock position* every time.

Three things influence where a given head sits:

- **Controller board revision.** Idle readings on an empty head differ systematically
  between xBuddy board revisions, while readings with a tool docked are much more
  consistent across revisions. Owners on the earliest revision are the most affected
  population.
- **Ambient temperature.** The idle floor drifts upward as the room gets warmer, so a
  machine that is fine in the morning can misbehave in the afternoon.
- **Time in service.** Several machines have settled *downward* over days of printing,
  moving from marginal to comfortably healthy without intervention. If you are close
  to the edge, running the machine may help rather than hurt.

A genuinely faulty head reads high at idle regardless of which board it is plugged
into and regardless of the cable. Where that has been tracked, board swaps and
replacement main cables changed nothing, and the resolution was a replacement
toolhead from the vendor. On at least one such unit a wire strand was found coming
away from the coil itself, and owners have raised coil wear and damaged coil wiring
as a wider quality question.

### The preheat error is probably not a separate problem

There is a preheat error that fires on first-tool pickup during Tool Offset
Calibration on affected machines. The evidence points to it being *secondary* to
detection: the firmware will not drive the heater of a tool it does not trust is
present. On one machine a toolhead replacement cleared both the detection fault and
the preheat errors together. Treat them as one complex, and chase the detection
problem rather than the heater.

!!! danger "Modified firmware thresholds — read before you go looking"
    Some owners have compiled custom firmware with the detection thresholds altered
    so their machines print again. Understand what that involves before you consider
    it. On this hardware it requires an **irreversible physical modification to the
    controller board**. It is unsupported by both companies. And it works by making
    the firmware *more willing to trust a marginal reading* — which is the correct
    move if your head is healthy and the firmware is too strict, and the wrong move
    if your head is genuinely failing, because it masks a hardware fault you would
    otherwise have replaced under warranty.

    This page does not supply threshold values or build instructions. Establish
    first, with the vendor, whether your head is faulty.

!!! warning "Firmware 6.9.0 changed this behaviour"
    The threshold model described above was documented in the 6.6.3 era. An owner
    reports new park-detection messages appearing only after updating to 6.9.0 and
    suspects the ringdown thresholds changed. Re-running dock calibration is the
    first suggestion. If you are on 6.9.0 or later, treat pre-6.9.0 numbers and
    advice as possibly stale, and check current release notes.

## Verification

`reported` — the fault family is described independently by multiple owners across
several threads and more than one firmware generation.

First-hand and current: [6.9.0 firmware, tool docking](https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/6-9-0-firmware-tool-docking/)
is an owner reporting park-detection errors that began with 6.9.0, on a machine where
parking itself always succeeds — a clean example of the detection layer disagreeing
with physical reality, and independent evidence that this family is live on current
firmware. [Will the Prusa INDXs wave1 ship with fixed induction coils?](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/will-the-prusa-indxs-wave1-ship-with-fixed-induction-coils/)
shows owners treating coil wear as a known concern ahead of the retail wave, though
that thread is speculation about quality control rather than diagnosis, and one
participant in it confuses the coil issue with the separate nozzle issue.

**Single-source, and the main caveat on this page:** the three-band threshold model,
the board-revision differences, the temperature drift, the break-in effect, and the
preheat-error relationship all come from the
[common problems summary](https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/a-summary-of-common-indx-problems/),
which condenses a community knowledge base that is now offline. That condensation is
detailed and internally consistent, but it has not been independently reproduced in
the forum corpus, and it predates 6.9.0. The explanatory mechanism should be read as
well-sourced-but-unverified rather than established.

The vendor's position, as reported there, was that the investigation remained open
between "hardware fault" and "firmware too strict". Both turned out to be real for
different machines, which is why this page leads with the mechanism instead of a fix.

## Related

- [Probing fails or nozzle never touches the bed](loadcell-emi-noise.md) — a
  different sensor and a different fault, but both are "the printer believes
  something untrue about its own state"
- [Tool offset calibration failures](offset-sensor-board-failure.md) — where the
  preheat error tends to surface
- [Blobs dragged into the print](stringing-and-wiper-calibration.md) — the other
  area 6.9.0 reworked. Owners report that change as a clear improvement, which is
  worth weighing against the park-detection regression described above.
- [Who to contact](support-and-warranty-path.md) — for a toolhead replacement
