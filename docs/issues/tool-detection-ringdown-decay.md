---
title:        Phantom tools, "tool not detected" and park failures
confidence:   reported
updated:      2026-08-25
author:       hyiger
printer:      Core One
toolhead:     INDX
hotend:       unknown
nozzle:       unknown
firmware:     6.6.3, 6.9.0
sources:
  - https://help.prusa3d.com/article/tool-park-failed-36127-core-one-indx_1073624
  - https://help.prusa3d.com/downloads/core-one-indx
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5392
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
design detail explains most of the confusing behavior in this family: why a wrong
tool state persists, why it survives a retry, and why two machines with opposite
symptoms can have the same underlying cause.

## Error codes that lead here

| Code | What the printer shows |
|---|---|
| [`36125`](https://help.prusa3d.com/article/tool-pickup-failed-36125-core-one-indx_1083573) | Tool pickup failed |
| [`36127`](https://help.prusa3d.com/article/tool-park-failed-36127-core-one-indx_1073624) | Tool park failed |
| [`36128`](https://help.prusa3d.com/article/retry-tool-park-36128-core-one-indx_1072357) | Retry tool park |
| [`36124`](https://help.prusa3d.com/article/tool-lost-36124-core-one-indx_1072958) | Tool lost |
| [`36123`](https://help.prusa3d.com/article/occupied-dock-36123-core-one-indx_1072788) | Occupied dock |
| [`36202`](https://help.prusa3d.com/article/hotend-preheat-error-36202-core-one-indx_1088818) | Hotend preheat error |
| [`36135`](https://help.prusa3d.com/article/toolchanger-error-17135-xl-36135-core-one-indx_399944) | Toolchanger error |

Detection faults surface as one of these. `36125` and `36127` are the two halves
of the problem this page describes — a tool that will not read as picked up, and
one that will not read as parked. `36128` is the retry that usually succeeds.

## Detail

Readings come out at one of three conclusions: clearly no tool, clearly a tool, or
ambiguous. In the ambiguous middle the firmware holds the last known state rather
than guessing. That is a sensible design, but it means a machine whose readings sit
in or near that middle band gets *sticky* wrong answers instead of intermittent ones.

### Reading the value on your own machine

The live figure is on the printer at **Info → Sensor Info → Ringdown Decay**.

Two owners have posted readings from healthy machines, and they agree closely:

| | Head empty | Tool docked |
|---|---|---|
| Machine A | 29 | 101 |
| Machine B | 27 | 103–104 |

Two machines is not a survey, so treat this as "roughly what healthy looks like"
rather than a pass mark. But they were taken independently, from the menu above, and
they land within a couple of points of each other at both ends — which is more than
the forum offered before. A reading close to these with the head empty means detection
is probably not your problem. One sitting well above them is worth investigating.

TODO(verify): whether the reading drifts once the head and coil are warm. An owner
raised this after noticing their machine misbehaved despite healthy cold readings, and
suggested someone take a reading part-way through a long job, or immediately after one,
to compare against the cold figure. Nobody has reported doing so. The community
summary separately records the idle floor rising with ambient
temperature, so the question is a reasonable one.

Prusa's own release notes for firmware 6.9.0 name the "nozzle presence" decay
threshold and give both its old and new value: it moved from **0.095 to 0.085**. Prusa
frames this as easing the upper bound in the interest of more reliable detection. That
is a first-party figure, so it is published here. Note the scale: the community
discussed these readings multiplied by a thousand, so a forum post describing a
threshold of "95" and the changelog's `0.095` are the same number.

TODO(verify): the *lower* threshold. A figure circulates on the forum but the owner
quoting it hedged it as a belief rather than a reading, and Prusa's release notes name
only the upper one. Also outstanding: how idle readings differ between controller board
revisions, which remains a community claim with no published figures behind it.

### Two opposite symptoms, one mechanism

**Reads a tool that is not there (phantom tool).** The head's idle reading sits high
enough to be taken as "tool present" when the head is empty, so the machine believes
it is holding a tool it is not.

Note that a park failure is **not** reliably a symptom of this. It looks like one —
the machine insists a tool is present after parking — but there is a separate,
better-documented cause with a different fix, covered further down. If your tool
physically parks correctly and a retry clears the error, read that section before
concluding your head is marginal.

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

    This page does not supply build instructions. **Firmware 6.9.0 has since made
    this change officially**, which removes most of the reason anyone was doing it
    by hand — update before you consider patching anything. Establish first, with the
    vendor, whether your head is faulty.

!!! important "Firmware 6.9.0 relaxed the detection threshold — what that means for you"
    Prusa's release notes for 6.9.0 record two related changes: they **eased the upper
    bound on nozzle-presence detection**, citing more reliable detection as the goal,
    and moved the decay threshold from 0.095 to 0.085.

    **If your fault was a tool reading as missing after pickup**, this is the change you
    were waiting for. Readings that previously fell just under the old bar clear the new
    one, so update before pursuing a replacement toolhead.

    **If your fault is park detection**, see the section below. An earlier version of
    this page suggested the threshold change might be causing it. Better evidence has
    since arrived and points elsewhere, so that suggestion has been withdrawn.

    Treat any pre-6.9.0 threshold figure you find on the forum as describing the old
    behavior.

### "Tool is still detected after parking" is a timing problem, not a threshold one

This deserves separating from the rest of the page, because the mechanism is
different and so is the fix.

A bug report against the firmware, filed with logs, describes parking failing to
confirm the nozzle as absent on **6.6.3**. The routine that verifies nozzle state
times out, logs that the nozzle is still detected after the park, retries, times out
again, and the toolchange fails. The tool has physically parked correctly throughout —
it releases and stays in the dock. Roughly twenty seconds later the firmware works it
out for itself and corrects its own record to "no tool", so the reading *does* settle.
It simply settles long after the verification window has closed.

Two details make this convincing. The reporter downgraded the same printer to
**6.6.2** and the problem disappeared completely, with nothing else changed. And
picking a tool up from an empty head works fine — it is specifically the park that
fails.

**Why this matters for the threshold story above:** the park failure was already
present in 6.6.3, which is *before* 6.9.0 relaxed the detection threshold. So the
threshold change cannot be its cause, and an owner reporting park messages on 6.9.0 is
most likely seeing this same longstanding bug rather than a side effect of the
relaxation. If your park fails but the tool is physically docked and a retry clears
it, you are probably looking at the settling-time problem, not a marginal head.

A second line of evidence points the same way. One of the owners who posted the
healthy readings above — comfortably clear of any threshold at both ends — is the same
owner whose machine had been reporting failed unloads. A head reading that healthy
cannot be marginal, so whatever caused their park messages was not a borderline
detection value. That is consistent with a settling-time problem and hard to reconcile
with a threshold one.

TODO(verify): the verification timeout the firmware allows, and how long the reading
actually takes to settle. Both are quoted in the linked issue, which is open and
unresolved at the time of writing.

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

**A correction.** An earlier version of this page suggested 6.9.0's relaxed threshold
might explain the "tool is still detected after parking" reports, flagged at the time as
an inference rather than a claim any source made. A firmware bug report has since shown
the park failure occurring on 6.6.3 and disappearing on a downgrade to 6.6.2 — before
the threshold moved at all. The suggestion has been withdrawn and the park behavior now
has its own section, where the evidence points at a settling-time problem instead. The
issue is open and unresolved, so that account may yet change too.

**First-party.** The 6.9.0 threshold change — both the relaxation and the specific
decay values — comes from
[Prusa's own release notes](https://help.prusa3d.com/downloads/core-one-indx), which
is the strongest class of source on this site: dated, unambiguous, and published by
the people who wrote the firmware. It also retrospectively supports the community's
threshold model, since the value Prusa names matches the figure owners had derived,
differing only by the factor of a thousand in how it was written down.

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
- [Toolhead collides with finished parts](complete-individual-objects-collision.md) —
  the other thing that can go wrong around a park and a tool change, and the more
  destructive one. Unrelated mechanism: a motion-clearance fault, not a detection one.
- [Blobs dragged into the print](stringing-and-wiper-calibration.md) — the other
  area 6.9.0 reworked. Owners report that change as a clear improvement, which is
  worth weighing against the park-detection regression described above.
- [Who to contact](support-and-warranty-path.md) — for a toolhead replacement
