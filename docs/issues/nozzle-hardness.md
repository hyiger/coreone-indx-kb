---
title:        Nozzle hardness and abrasive filaments
confidence:   reported
updated:      2026-10-25
author:       hyiger
printer:      Core One
toolhead:     INDX
hotend:       CHT high-flow, and plain-bore variants
nozzle:       0.4mm standard
firmware:     unknown
sources:
  - https://blog.prusa3d.com/prusa-core-one-gen-2-indx-shipping-has-started-complete-printers-open-for-orders_137623/
  - https://help.prusa3d.com/article/unknown-nozzle-36121-core-one-indx_1072730
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/nozzlegate-communications/
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/bondtech-nozzle-hardening-debacle-how-does-this-affect-prusa-indx-orders/
  - https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/a-summary-of-common-indx-problems/
  - https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/missing-profiles-in-slicer-for-non-0-4-nozzles-and-other-materials/
  - https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/indx-nozzles/
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/hardened-nozzle/
  - https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/bondtech-nozzles-dont-ship/
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/prusa-indx-update-shipping-starts-this-week/
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/indx-refund-voucher-doesnt-work-with-free-shipping/
superseded_by:
---

# Nozzle hardness and abrasive filaments

## Summary

The INDX was marketed with hardened nozzles rated for carbon- and glass-filled
filaments. The shipped nozzles are surface-treated rather than through-hardened, at a
hardness well below what the trade normally means by "hardened". If you bought an
INDX expecting to run abrasive filament from day one, you cannot, and the vendor has
published a remediation offer that includes a full return. Treat abrasive filament on
the current nozzles as consuming them. No abrasive-resistant replacement is on sale
yet: E3D has announced one, but it has not shipped — see *What is coming* below.

## Error codes that lead here

| Code | What the printer shows |
|---|---|
| [`36121`](https://help.prusa3d.com/article/unknown-nozzle-36121-core-one-indx_1072730) | Unknown nozzle |
| [`36122`](https://help.prusa3d.com/article/unknown-nozzle-36122-core-one-indx_1072738) | Unknown nozzle |

These fire when the nozzle fitted does not match what the sliced file declared —
the per-tool declaration that also carries the abrasive and high-flow flags.

## Detail

### What was promised and what shipped

Marketing for the passive tools described hardened steel construction with abrasive
resistance sufficient for carbon fiber, glass fiber and glow-in-the-dark filaments
without meaningful wear, and listed hardened nozzles as standard equipment. That
wording was later removed from shop listings, and the vendor published an admission
that the shipped nozzles are nitrocarburized — a surface treatment — at roughly
30–32 HRC.

For context on why owners consider that a material difference rather than a quibble:
the community position, argued at length in the threads, is that "hardened" in this
industry conventionally implies something in the region of 50–60 HRC, and that a
buyer could reasonably have read the marketing that way. A surface treatment in the
low thirties is much closer to untreated stainless than to a hardened nozzle.

Compounding it, the high-flow insert is plain brass. So even setting the body
treatment aside, filled filaments will erode the flow geometry. And retail packaging
and product pages still carried the original hardened claim when this became public.
One owner whose spare nozzles, ordered from the vendor's shop in mid-July, arrived in
late September reports that they were still described as hardened.

### Why fully hardened nozzles are genuinely hard here

This is worth understanding, because it explains why the fix is slow rather than
merely withheld. The INDX heats its nozzles by induction. Conventional hardening
works by quenching steel into a martensitic structure, and that structure has
substantially lower magnetic permeability — it is a poor magnetic conductor, and so
it resists the rapid magnetic flux that induction heating depends on. A fully
hardened nozzle and efficient induction heating pull against each other.

The vendor's account is that the planned fully hardened version could not be
machined reliably. Owners have noted that at least one other induction-based
toolchanger does ship hardened steel nozzles, so the constraint is evidently not
absolute — but it is a real engineering tension rather than a purely commercial one.

### What the vendor's own wear testing found

On 30 August 2026 the vendor published the results of its wear testing on the shipped
nozzles, alongside the announcement that Gen 2 machines were shipping. It is the first
first-party statement of what these nozzles will actually take, as opposed to what they
were specified to be, and it is more useful than anything preceding it on this page.

Three things come out of it.

**The hardening question is settled from the vendor's side.** These nozzles carry a
hardened surface over an unhardened body, which the vendor attributes to how Bondtech
specified them. That is no longer something inferred from marketing copy and its
retraction; it is stated plainly by the party that ships them.

**Non-abrasive printing is not affected.** Everything unfilled behaves as it would on a
standard Core One nozzle, and the vendor's list is broad enough to be worth grouping:
the everyday four (PLA, PETG, ABS, ASA); the flexibles (TPU, TPE); the soluble and
support materials (PVA, BVOH, HIPS); and the unfilled engineering plastics — nylon, PP,
PBT, PC and PC blends. If you do not run filled or abrasive filament, this page's
problem is not yours.

**For abrasives, there is now a service life rather than a warning.** Per nozzle, the
vendor's present estimates are:

| Filament | Approximate life per nozzle |
|---|---|
| PETG-CF | 10 kg |
| PC-CF | 5 kg |
| highly abrasive glow-type | 0.5 kg |

The vendor is also candid about the limit: if a printer's whole job is abrasive
filament, what ships today is not the right answer for it.

Two caveats worth carrying. The vendor describes these as current figures from testing
that is still running, with a fuller write-up promised — so they may move. And they
reported the results as better than their own initial accelerated tests suggested, which
is a statement about their earlier testing rather than independent confirmation.

### What to do now

**Turn the printer's "nozzle hardened" setting off**, in the all-tools menu. This
matters practically: with it off, slicing an abrasive-material profile will raise a
warning rather than proceeding silently. It is the one setting change that protects
you from your own muscle memory.

**Treat carbon- and glass-filled filament as at-your-own-risk**, and prefer a
plain-bore nozzle over the high-flow geometry for filled materials — the plain bore
has less fine internal structure to erode.

**Consider the remediation offer.** The vendor published options that include store
credit per nozzle, a smaller cash refund per nozzle, or returning the Founders
Edition kit outright for a full refund at no cost. Claims go through the vendor's
contact form with your order number and your chosen option.

TODO(verify): the credit and refund amounts per nozzle and per kit, the return
window, and whether an installed and used kit is still returnable. Every one of these
is a figure or a deadline where being wrong costs the reader money or a missed
window — get them from the vendor's own current statement, not from this page.
Separately, Prusa published an extended return period for initial-batch kit orders;
TODO(verify) that length too.

**If your kit is one of Prusa's initial-batch orders, the claim goes to Prusa.**
Prusa's August update went to customers who already had kit orders in, and says that
Prusa, not the vendor, handles their compensation: Prusa Store credit, or a smaller cash
refund, set per kit and scaled to its tool count. Those customers were the initial
batches: Prusa reopened kit orders only afterward, in its
[20 August announcement](https://blog.prusa3d.com/prusa-core-one-gen-2-indx-shipping-has-started-complete-printers-open-for-orders_137623/),
for owners who had missed the first batch. The credit arrives as an emailed voucher,
sent in waves that follow the shipping batches; if yours has not appeared a few days
after the kit arrived, Prusa's tech support is the contact. Cash instead of credit is
requested from Prusa's support by live chat or email. The same update also gave the
initial-batch orders the hardware for the Core One+ Gen 2 upgrade (new belts, belt
pulleys and thermal expansion joints), at Prusa's own expense.

Prusa has not published whether kits ordered from it after that update are covered.
One owner whose order apparently fell after the spring wave asked Prusa's support about
the Gen 2 hardware and relays the reply in Prusa's
[shipping update thread](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/prusa-indx-update-shipping-starts-this-week/):
the free upgrade belonged to the spring orders alone, making amends to them for the late
shipping and for the nozzle hardness, and orders placed from August on, a second wave,
do not get it free. The same owner says that new orders now come with the Gen 2
hardware alongside the INDX; whether its cost is in the price has not been confirmed.
That may not hold for every new order: Prusa's 20 August announcement lists separate
conversion kit versions for the CORE One+ and the CORE One+ (Gen 2), to be matched to
the printer, without saying what each contains, and one more owner in the shipping
update thread wrote in August that the INDX could be ordered with or without the Gen 2
upgrade. The reply as relayed says nothing about credit or cash for the later orders, so
that part of the question stays open. Provisional: one owner's relay of a private email.

TODO(verify): Prusa's credit and cash amounts for each kit size, from Prusa's August
update to its kit customers as relayed in the nozzlegate communications thread.

Weigh one limit before taking Prusa's credit for nozzles. As of mid-October, Prusa's
store credit could not buy INDX spares or replacements, because Prusa's shop did not
stock them; owners say so in three separate threads. One noted in August that Prusa did
not sell them. Another, in October, counts the credit's not being usable among the costs
of a nozzle order from the vendor's own shop, along with import fees. Later in the month the same owner adds that Prusa still had no INDX nozzles to
offer, and understands, without being sure of it, that the credit cannot be spent at
Prusa's US reseller, so using it means ordering from Prusa directly, with shipping and
import costs on top; this is that owner's reading alone, unconfirmed. A third, in
mid-October, had hoped to spend the credit on extra sizes and found none in Prusa's
shop. The first writes in the
[nozzlegate communications](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/nozzlegate-communications/)
thread, the second in a
[thread on slow nozzle orders](https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/bondtech-nozzles-dont-ship/),
and the third in Prusa's
[shipping update thread](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/prusa-indx-update-shipping-starts-this-week/).

The third owner expects INDX nozzles to reach Prusa's shop once the pre-order backlog
clears; the post does not make clear whether Prusa said so. The timing, perhaps spring,
is that owner's own guess. The same owner also asked Prusa how long its voucher stays
valid, and relays the answer: there is a limit, so check it before holding credit back
for nozzles Prusa may stock later. Whether Prusa's voucher carries the vendor's other
conditions, described below, is only partly known; see the report that follows. This is
provisional, one owner's post and their relay of a private answer.

TODO(verify): the validity period of Prusa's compensation voucher — relayed by one owner
in Prusa's shipping update thread as Prusa's answer to a question; no published statement
of it has been found.

Prusa's voucher, like the vendor's, did not pay for shipping in the one case reported so
far, that of an owner who spent theirs in late October, in a
[thread on the voucher and free shipping](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/indx-refund-voucher-doesnt-work-with-free-shipping/).
That owner hit a second snag as well. Prusa's store was running a sale with free
shipping above an order minimum, and entering the voucher brought the shipping charge
back; the owner took this to mean that the share of the order the voucher paid for did
not count toward that minimum. Prusa's support, reached by live chat, settled it the
same day by adding the shipping charge to the voucher's value. Shipping was still billed
separately, with the voucher covering only the goods, so the outcome matched free
shipping in value but not in form. A Prusa representative in the thread had pointed them
to support, adding that more than one voucher on an order can make one offer displace
another; this owner had used only one. The order left a little of the voucher unspent,
and the post does not say what became of it, so whether Prusa's voucher, like the
vendor's, is used up in a single order has not been reported. Provisional: one owner,
one order.

**How a claim to the vendor goes, from owners who have filed one.** Its contact form
has no category that obviously fits, and owners report submitting under the generic
"other" request type. Expect an automated acknowledgment immediately and then a wait — one
owner reports writing a week earlier, being acknowledged, and still having no substantive
reply. Another filed the day this was written and says much the same. So file early, keep
your own record of what you asked for, and do not read silence as refusal.

You can also ask for a **mix** of credit and cash rather than all of one. At least one
owner did, wanting enough credit to buy a genuinely hardened nozzle once one exists.

**Read the voucher conditions before you settle on credit.** The store credit offered
to Founders Edition owners is issued as a voucher, and on 24 September the vendor set
out the conditions attached to it by email to at least two owners — provisional: those
two relay their private emails in one thread, and no published statement of these terms
has been found. The voucher does not pay for shipping. It is redeemed in a single order,
and any part of it that order leaves unspent is forfeited. One of the two adds that it
comes off the price before VAT, so that, as that owner understands it, tax falls only on
what remains, and that it lapses after a fixed period. Those conditions cut against the
mixed plan above: credit held back for a hardened nozzle has to be spent in one go,
before it lapses, on a part that has no release date yet.

TODO(verify): the voucher's validity period — relayed by one owner in the nozzlegate
communications thread as the vendor's answer; no published statement of it has been
found.

One owner asked for cash after these conditions came out and says the vendor agreed at
once; others in the thread say they will now ask for cash too. That post does not say
whether the owner had already filed for credit, so whether a credit choice already
submitted can still be changed has not been established. Two questions raised there
went unanswered: whether the same conditions apply to credit on kits bought from
Prusa, and whether a cash refund returns to the original payment method. The validity
limit on Prusa's voucher, relayed above, and one owner's report that it did not pay for
shipping, each from another thread, answer the first only in part.

!!! note "Store credit buys nozzles you may not be able to use yet"
    Worth knowing before you choose credit over cash: PrusaSlicer currently offers the
    INDX only a single nozzle variant, so other sizes have no profile to print with.
    One owner making exactly this decision put it plainly — they had never tried other
    sizes because there are no profiles for them, which makes credit-for-more-nozzles a
    weaker proposition than it looks — both INDX printer models declare a single nozzle
    variant in Prusa's published profile bundle, so no other size is selectable. See
    [missing slicer profiles](missing-slicer-profiles.md).

    Delivery was slow and uneven through early October, and has picked up since. Two
    owners who ordered spare nozzles from the vendor's shop in mid-July report them
    shipping or arriving only in late September, in the
    [spare nozzles thread](https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/indx-nozzles/).
    In a
    [later thread](https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/bondtech-nozzles-dont-ship/),
    two owners who had ordered in mid-September were still waiting in early October,
    about three weeks on. The vendor told one that the nozzles still had to be
    assembled, and told the other, after a support ticket, that the order was queued to
    be picked and shipped within about a week; a third owner had meanwhile received
    plain-bore nozzles within three days. Both waiting orders then shipped: the
    ticketed one early the following week, as the vendor had estimated, arriving a day
    later, and the first in mid-October, about a month after it was placed. Orders
    placed in October went out within one to two weeks, by the accounts of three more
    owners there, and one of those orders included a plain-bore nozzle. By mid-October
    two owners there said the 0.4mm and 0.6mm nozzles looked readily available. Two
    later reports, neither giving an order date, point both ways: one more owner there
    said in late October that theirs took about three weeks to arrive, and is waiting
    for profiles before using them; and in the spare nozzles thread another reported an
    order that shipped within a few days and reached the US days after that, with import
    tariffs adding to the cost. The first waiting owner still believes plain-bore
    nozzles were what held orders up, and had warned that the shop can show nozzles in
    stock that are not ready to ship; no pattern by type is established. The vendor's
    explanations are each relayed by one owner. When the first waiting owner's nozzles
    arrived, they found no PrusaSlicer profile for them, as described above.

    The nozzles' outside finish has also differed between deliveries, by two owners'
    accounts in that thread. One received in mid-October looked smooth, which its owner
    took for an updated body; another owner describes two received around the start of
    October as rough-textured. Beyond the look, neither says what changed, and nothing
    in the thread points to a change in the steel or its hardness. Provisional: one
    thread.

Be aware the adequacy of the compensation is disputed. At least one owner worked
through the arithmetic and found the offered credit represents a substantially
smaller uplift than the hardened-over-standard premium in the vendor's own store and
at other nozzle manufacturers. That is a community calculation, not a vendor figure,
but it is a reasonable thing to check for yourself before accepting an option.

### What is coming

Two replacements from outside Bondtech are in the works. Neither is on sale, and
neither has a published price.

**E3D.** E3D's involvement was public by the end of July 2026: an owner in the
[nozzle hardening debacle thread](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/bondtech-nozzle-hardening-debacle-how-does-this-affect-prusa-indx-orders/)
linked a post from E3D's own account, and others there took it to mean that Bondtech
was now working with E3D on the nozzles. In late August E3D made it official: it is
developing an abrasive-resistant variant for the INDX, and could not yet give a
release date. An owner relayed that statement in the nozzlegate thread, and in a
[separate thread](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/hardened-nozzle/)
another owner notes Bondtech posting about the same collaboration. At a US trade show
in late September one owner spoke with an E3D engineer and reported back the
following. It is provisional — a single owner's notes from a conversation, in one
thread, not a published specification:

- a possible January timeframe (presumably 2027), offered tentatively;
- 0.4mm and 0.6mm high-flow CHT nozzles first;
- all-steel construction, assembled from several steel alloys so that induction
  heating still works, with a titanium heat break and a coating the owner noted as
  "obsidian", presumably E3D's Obxidian (the owner was unsure whether that name
  referred to the coating or the nozzle itself);
- on release, simultaneous availability from E3D itself, from Prusa and from Bondtech;
- no problem with the eddy-current offset sensor, according to the engineer. The
  owner's first post said the opposite and was corrected the same day as a
  dictation error, so if you see that first version quoted, it is the retracted one.

The same owner reports that, according to E3D staff, Bondtech's own INDX
demonstration printer at the show was fitted with the E3D nozzle. If accurate, the
part exists in working form, but it has not shipped. The first sizes reported are
high-flow only; no plain-bore variant was mentioned.

**Diamond.** A third-party diamond-nozzle manufacturer has confirmed an
INDX-compatible variant. Notably, the diamond is doped to keep it detectable by the
eddy-current offset sensor — a fully non-conductive tip would be invisible to that
sensor, which is a real design constraint on any replacement nozzle. Timing was
described in months rather than weeks, and nothing firmer has surfaced in the threads
since.

!!! note "Two separate defects are often discussed alongside this"
    A number of nozzles have shipped already obstructed, and independent teardowns
    found machining swarf inside — a fragment of steel sitting in the mixing chamber
    in one case, and debris across the exit channel in another. That is a
    manufacturing defect,
    not a wear or hardness problem, and the vendor replaces affected nozzles. There
    is also a separate undersized filament-guide bore affecting unloading, covered on
    [its own page](filament-guide-bore-unload-failure.md).

## Verification

`reported` — this is the best-corroborated topic in the corpus. The two principal
threads, [nozzlegate communications](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/nozzlegate-communications/)
and [Bondtech nozzle hardening debacle](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/bondtech-nozzle-hardening-debacle-how-does-this-affect-prusa-indx-orders/),
together run to several hundred posts across roughly fifty distinct participants, and
both quote the original marketing copy, the vendor's published admission, and the
vendor's remediation statement directly.

Strongly sourced: the marketing claim and its removal, the surface-treatment nature
and hardness figure, the brass insert, the existence and structure of the remediation
offer, and the induction/permeability explanation — all appear as quoted vendor
material in the threads rather than as owner inference. So does Prusa's handling of
compensation for its initial-batch kit orders, Gen 2 upgrade hardware included,
quoted from its August update to those customers; that kit orders reopened only after
that update, in separate versions for the CORE One+ and the CORE One+ (Gen 2), is
Prusa's own announcement.

!!! note "Why hardness figures appear here when other numbers do not"
    This site withholds calibration values, temperatures and print settings until a
    human has verified them on hardware. A hardness rating is a different kind of
    number: it is a published material property, not a value anyone dials into a
    slicer or a drill, so being wrong about it misinforms rather than damages
    hardware. The lower figure is the vendor's own published admission; the higher
    one is the industry convention owners are measuring it against, not a
    specification of any shipped part. Both are cited. Please do not strip them —
    without them the central claim of this page cannot be checked.

    The nozzle service-life figures added on 30 August fall under the same reasoning.
    A kilogram-per-nozzle wear estimate is not a value anyone dials into anything; it
    is the vendor's published guidance on when a consumable is spent, and it is cited
    to the announcement it came from.

Weaker: the hardness figure a buyer "should" have expected is a community norm rather
than a published standard. The compensation-adequacy arithmetic is one owner's
calculation. The voucher conditions are second-hand, relayed from vendor emails by
two owners in a single thread, the VAT treatment and expiry from only one of them. The
diamond-nozzle timeline is a third-party statement of intent. That E3D is developing an
INDX nozzle is corroborated in three threads, but every detail of it — timeframe, sizes,
construction, sensor compatibility, where it will be sold, the booth demonstration —
rests on one owner's notes from a trade-show conversation. Slow spare-nozzle delivery
through early October is reported in two threads by four owners, but one of those
threads also has a quick delivery, and the vendor's reasons for the delays are each one
owner's relay. The faster shipping since, and the change in the nozzles' outside
finish, rest on owners in that one later thread. A quick delivery in the spare
nozzles thread and a three-week one in that later thread, neither giving an order
date, cannot be placed on either side of early October. The "hardened" description on
delivered spares comes from a single thread. That Prusa's credit could not buy INDX
nozzles, because Prusa's shop did not stock them, rests on three owners in three
separate threads, not on a statement from Prusa: the August owner for August, and two
owners for mid-October. The expectation that Prusa will stock them later is one owner's,
not clearly from Prusa, and the validity limit on Prusa's voucher is that owner's relay.
That the credit cannot be spent at Prusa's US reseller is one owner's hedged
understanding. That Prusa's voucher did not pay for shipping, or, as that owner read
it, count toward a free-shipping minimum, is one owner's report of one order. That the
free Gen 2 hardware was for the spring orders only is another owner's relay of a
private reply from Prusa's support, and that new orders come with that hardware is the
same owner's observation; that the INDX could be ordered with or without the upgrade is
one further owner's post from August.

Where the sources disagree: owners differ sharply on whether the remediation is
adequate, and on how much practical impact the hardness actually has for someone who
prints few abrasives. Both positions are argued in good faith in the threads. This
page deliberately does not take a side on the commercial question — only on the
technical fact that these nozzles are not hardened in the conventional sense.

## Related

- [Undersized filament guide bore](filament-guide-bore-unload-failure.md)
- [Who to contact](support-and-warranty-path.md) — the claims and returns route
- [Tool offset calibration](offset-sensor-board-failure.md) — why nozzle
  conductivity matters to the sensor
