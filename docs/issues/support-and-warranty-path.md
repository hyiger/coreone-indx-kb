---
title:        Who to contact — support vs warranty on an INDX kit
confidence:   reported
updated:      2026-10-08
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
  - https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/bondtech-nozzles-dont-ship/
  - https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/is-it-worth-upgrading-from-core-one-to-indx/
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

Whichever company holds your case, ask what turnaround to expect and chase it once
that has passed. One owner was told by Prusa's support that an escalated case normally
takes a few days, and was still waiting close to a week after first reporting the fault.

One owner whose tools repeatedly failed to release at the dock — see
[tools unlocking or ejecting](tool-unlocks-or-ejects.md) — reports that Prusa's live
chat offered to send a whole replacement toolhead. In a
[later thread on another topic](https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/is-it-worth-upgrading-from-core-one-to-indx/)
the same owner says the new head came from Prusa a few days after a short online chat,
and that they fitted it. Neither post says which edition the kit is or where it was
bought, so the account neither confirms nor contradicts the Founders Edition pattern
above. It is one owner telling their own case twice, not a second source: treat it as a
single report, `provisional`.

### Nozzle compensation and spare nozzles

The shipped INDX nozzles are hardened only at the surface, not all the way through,
and compensation is offered for that; the background, the options and their limits are
on the [nozzle hardness](nozzle-hardness.md) page. Compensation is handled by whoever
sold you the kit. Founders Edition owners claim from the vendor, through its contact form.
Prusa's August update went to customers who already had kit orders in, the initial
batches, and says that Prusa handles their compensation itself: store credit, sent as an
emailed voucher, or a cash refund instead. If the store-credit voucher has not arrived a
few days after the kit, ask Prusa's tech support; to take the cash refund in place of
credit, ask Prusa's support by live chat or email. Prusa has not said whether kits
ordered from it after that update are covered.

Buying spare nozzles is a separate matter. Owners in two separate threads report that
Prusa store credit cannot be used for INDX nozzles, which come from the vendor's shop
whichever edition you own; the earlier of the two explained in August that Prusa did
not sell them. A stalled shop order is a ticket to the vendor. One owner in October,
whose order had waited nearly three weeks, opened a ticket and had a reply with a
dispatch estimate the same day. That is provisional, a single report, and the estimate
had not yet been tested when it was posted.

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
threads. Prusa's handling of nozzle compensation for kits already on order from it in
August is first-party: Prusa's August update to those customers, quoted in the
nozzlegate communications thread.

Weaker: the live-chat replacement offer and the quoted escalation time each rest on a
single owner's report in the common problems summary thread. The same owner's later
post that the head arrived and was fitted, in a
[thread on whether the INDX upgrade is worth it](https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/is-it-worth-upgrading-from-core-one-to-indx/),
is that owner's account again rather than a second source, and neither post says which
edition the kit is. That Prusa store credit cannot be used for INDX nozzles rests on
two owners in separate threads, the
[nozzlegate communications](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/nozzlegate-communications/)
thread and a
[thread on slow nozzle orders](https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/bondtech-nozzles-dont-ship/),
not on a statement from Prusa; that Prusa did not sell them as of August rests on the
first of those alone. The same-day vendor reply is a single report from the second.

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
