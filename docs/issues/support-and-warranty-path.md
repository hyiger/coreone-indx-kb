---
title:        Who to contact — support vs warranty on an INDX kit
confidence:   reported
updated:      2026-08-24
author:       hyiger
printer:      Core One, Core One L
toolhead:     INDX
hotend:       unknown
nozzle:       unknown
firmware:     unknown
sources:
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/warranty-concern-uk/
  - https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/a-summary-of-common-indx-problems/
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/nozzlegate-communications/
superseded_by:
---

# Who to contact — support vs warranty on an INDX kit

## Summary

Diagnosis and replacement parts come from two different companies, and sending your
problem to the wrong one is the single most common way owners lose weeks. For
Founders Edition kits the pattern owners have converged on is: get the fault
*diagnosed* by Prusa, then take that diagnosis to Bondtech to get the *part*. Open
your case early even if you are not ready to act on it, so the date is on record
inside whatever warranty window applies to you.

## Detail

The INDX is a Bondtech product bolted onto a Prusa printer, and support
responsibility splits along that seam rather than along the seam a customer would
expect. Prusa's technical support will work through diagnosis with you — their
tooling, logs and firmware knowledge are what identify the failing component. But
for Founders Edition kits the purchase contract is with Bondtech, and replacement
hardware comes from them. Owners on the forum describe a good deal of back-and-forth
between the two before this became clear.

The practical consequence is an order of operations:

1. **Diagnose with Prusa first.** Use their support channels and keep the
   transcript. Multiple owners report that attaching a video of the failure speeds
   things up more than any amount of written description — a fault that is hard to
   put into words is often unmistakable in a few seconds of footage.
2. **Open the vendor case carrying Prusa's findings.** A ticket that already
   contains "Prusa support identified X" moves faster than one that starts from
   symptoms.
3. **Quote both answers when the two disagree.** Defects in the printed dock parts
   in particular have been bounced between the two companies. If you have a position
   from each, put both in the ticket rather than letting them be discovered
   separately.

Two things to know going in. Prusa has declined to ship Founders Edition
replacement parts directly, so routing a parts request to them is a dead end even
when they agree the part is faulty. And Bondtech's support team is small relative to
the number of kits in the field; reported turnaround has ranged from overnight to
several weeks of silence, so a slow reply is not necessarily a lost ticket.

### On warranty length — verify this yourself

Warranty duration is stated inconsistently across the forum and varies by region and
by who you bought from. **This page deliberately does not state a duration**, because
a wrong figure here could cause someone to miss their own window.

TODO(verify): the stated warranty period for non-EU purchases, the EU statutory
period, and the UK position after leaving the EU. Sourced from the Warranty Concern
(UK) thread, where the participants are owners reasoning about consumer law rather
than anyone qualified to state it — one of them explicitly recommends asking a
consumer-rights organization instead.

What is safe to act on: **who you bought from determines whose warranty applies**,
and that is not always who shipped the box. Founders Edition kits were purchased from
Bondtech even though Prusa handles the technical side, so the contract — and any
statutory rights that attach to it — runs to Bondtech. If you need a definitive
answer for your country, ask your national consumer-rights body, not a printer forum.
Open your case early regardless, so the report date is recorded.

## Verification

`reported` — the support/warranty split is described independently in the
[common problems summary](https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/a-summary-of-common-indx-problems/)
and corroborated by owners working through real cases in the
[Warranty Concern (UK)](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/warranty-concern-uk/)
thread, which independently confirms the pattern of technical support from one
company and parts replacement from the other. Escalation experience and turnaround
times are reported across the two large
[nozzlegate](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/nozzlegate-communications/)
threads.

Where the sources disagree: warranty duration. The UK thread reaches no conclusion
and its participants say so plainly. Treat every duration figure on the forum as
unverified.

This page describes a support process, not a legal entitlement. Nothing here is
legal advice.

## Related

- [Tool offset calibration failures](offset-sensor-board-failure.md) — the most
  common fault that ends in a parts request
- [Nozzle hardness](nozzle-hardness.md) — the return-policy context for the nozzle
  issue specifically
