---
title:        Who to contact — support vs warranty on an INDX kit
confidence:   reported
updated:      2026-10-25
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
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/prusa-indx-update-shipping-starts-this-week/
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/indx-refund-voucher-doesnt-work-with-free-shipping/
  - https://blog.prusa3d.com/prusa-core-one-gen-2-indx-shipping-has-started-complete-printers-open-for-orders_137623/
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
Footage helps, but it does not settle every case quickly: another owner, whose printer
fails bed probing and tool calibration on most attempts, reports having sent Prusa's
support ten videos and still having no final answer.

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
credit, ask Prusa's support by live chat or email. A printed note packed with the kit
sets the same few-day expectation, according to one owner who could not find the email
afterward. Search your mail before you chase it: another owner in the same thread
reports that theirs arrived with a subject line calling it an INDX compensation voucher,
which is easier to find than anything sent under Prusa's name alone. Both are from one
thread, so provisional. Prusa has not published whether kits ordered from it after that
update are covered. One owner whose order apparently fell after the spring wave relays
a reply from Prusa's support that touches only part of it: the Gen 2 upgrade hardware
that the August update promised the initial-batch orders free was for the spring orders
alone, and orders placed from August on do not get it free. The same owner says new
orders now come with that hardware alongside the INDX; whether its cost is in the price
has not been confirmed. That may not hold for every order, though: Prusa's
[20 August announcement](https://blog.prusa3d.com/prusa-core-one-gen-2-indx-shipping-has-started-complete-printers-open-for-orders_137623/)
lists separate kit versions for the CORE One+ and the CORE One+ (Gen 2).
That is a single provisional relay, and it says nothing about credit or cash; it is
covered on the [nozzle hardness](nozzle-hardness.md) page.

Trouble spending Prusa's voucher is a question for Prusa's support too. One owner whose
voucher knocked a store sale's free shipping off their order raised it over live chat,
and support settled it the same day by adding the shipping charge to the voucher's
value; the details, including that the voucher did not pay for shipping, are on the
[nozzle hardness](nozzle-hardness.md) page. Provisional, a single report.

Buying spare nozzles is a separate matter. INDX nozzles come from the vendor's shop
whichever edition you own. As of mid-October, Prusa store credit could not be used for
them, because Prusa's shop did not stock them; owners in three separate threads report
this, the earliest in August. One owner expects Prusa to stock them eventually, and the
same owner relays from Prusa that its voucher has a validity limit; both are a single
provisional report, covered on the [nozzle hardness](nozzle-hardness.md) page. A
stalled shop order is a ticket to the vendor. One owner in October, whose order had
waited nearly three weeks, opened a ticket and had a reply with a dispatch estimate the
same day; the order shipped early the following week, as estimated, and arrived a day
later. That is still provisional, a single report. By mid-October, other owners in the
same thread were seeing orders placed that month ship within one to two weeks.

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
threads. Prusa's handling of nozzle compensation for its initial-batch kit orders is
first-party: Prusa's August update to those customers, quoted in the nozzlegate
communications thread. So are the separate kit versions for the CORE One+ and the CORE
One+ (Gen 2), from Prusa's 20 August announcement.

Weaker: the live-chat replacement offer, the quoted escalation time and the ten-video
case each rest on a single owner's report in the common problems summary thread. The
live-chat owner's later post that the head arrived and was fitted, in a
[thread on whether the INDX upgrade is worth it](https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/is-it-worth-upgrading-from-core-one-to-indx/),
is that owner's account again rather than a second source, and neither post says which
edition the kit is. That Prusa store credit could not be used for INDX nozzles, because
Prusa's shop did not stock them, rests on three owners in three separate threads, the
[nozzlegate communications](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/nozzlegate-communications/)
thread, a
[thread on slow nozzle orders](https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/bondtech-nozzles-dont-ship/)
and Prusa's
[shipping update thread](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/prusa-indx-update-shipping-starts-this-week/),
not on a statement from Prusa; for August it rests on the first of those alone. The
same-day vendor reply, and the order's shipping as estimated, are a single owner's
report from the second, where the faster shipping since comes from several owners. The
packed note and the voucher email's subject line come from two owners in the third.
The expectation that Prusa will stock INDX nozzles later is one owner's, not clearly
from Prusa, and the validity limit on Prusa's voucher is that owner's relay, both in
that same third thread. So is the support reply limiting the free Gen 2 hardware to the
spring orders, relayed by another owner there, along with that owner's note that new
orders now include the hardware. The voucher's handling at checkout, and
the chat that resolved it, are one owner's report in a
[thread on the voucher and free shipping](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/indx-refund-voucher-doesnt-work-with-free-shipping/).

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
