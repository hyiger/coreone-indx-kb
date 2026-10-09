---
title:        Nozzle hardness and abrasive filaments
confidence:   reported
updated:      2026-10-08
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

**If your kit was already on order from Prusa in August, the claim goes to Prusa.**
Prusa's August update went to customers who already had kit orders in, the initial
batches, and says that Prusa, not the vendor, handles their compensation: Prusa Store
credit, or a smaller cash refund, set per kit and scaled to its tool count. The credit
arrives as an emailed voucher, sent in waves that follow the shipping batches; if yours
has not appeared a few days after the kit arrived, Prusa's tech support is the contact.
Cash instead of credit is requested from Prusa's support by live chat or email. Prusa
has not said whether kits ordered from it after that update are covered.

TODO(verify): Prusa's credit and cash amounts for each kit size, from Prusa's August
update to its kit customers as relayed in the nozzlegate communications thread.

Weigh one limit before taking Prusa's credit for nozzles. Prusa's store credit cannot
buy INDX spares or replacements, according to two owners: one noted in August that
Prusa did not sell them, and another, in October, counts the credit's not being usable
among the costs of a nozzle order from the vendor. Those nozzles come from the vendor's
own shop, with shipping on top, and the October owner mentions import fees as well. The
two write in separate threads, the August owner in the
[nozzlegate communications](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/nozzlegate-communications/)
thread and the October owner in a
[thread on slow nozzle orders](https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/bondtech-nozzles-dont-ship/).

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
Prusa, and whether a cash refund returns to the original payment method.

!!! note "Store credit buys nozzles you may not be able to use yet"
    Worth knowing before you choose credit over cash: PrusaSlicer currently offers the
    INDX only a single nozzle variant, so other sizes have no profile to print with.
    One owner making exactly this decision put it plainly — they had never tried other
    sizes because there are no profiles for them, which makes credit-for-more-nozzles a
    weaker proposition than it looks — both INDX printer models declare a single nozzle
    variant in Prusa's published profile bundle, so no other size is selectable. See
    [missing slicer profiles](missing-slicer-profiles.md).

    Delivery has been slow and uneven as well. Two owners who ordered spare nozzles from
    the vendor's shop in mid-July report them shipping or arriving only in late
    September, in the
    [spare nozzles thread](https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/indx-nozzles/).
    Recent orders have gone both ways, according to a
    [later thread](https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/bondtech-nozzles-dont-ship/).
    In early October two owners there who had ordered in mid-September were still
    waiting, about three weeks on. The vendor told one that the nozzles still had to be
    assembled, and told the other, after a support ticket, that the order was queued to
    be picked and shipped within about a week. A third owner had received an order of
    plain-bore nozzles within three days, the week before posting. The first of the
    waiting owners warns that the shop can show nozzles in stock that are not ready to
    ship, and guesses that plain-bore nozzles are what is holding orders up. The
    second waiting order was also plain-bore, but so was the quick delivery, so no
    pattern by type is established. The vendor's explanations are each relayed by one
    owner.

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
compensation for kits already on order from Prusa, quoted from its August update to
those customers.

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
rests on one owner's notes from a trade-show conversation. Slow spare-nozzle delivery is
reported in two threads by four owners, but one of those threads also has a quick
delivery, and the vendor's reasons for the delays are each one owner's relay. The
"hardened" description on delivered spares comes from a single thread. That Prusa's
credit cannot buy INDX nozzles rests on two owners in separate threads, not on a
statement from Prusa; that Prusa did not sell them as of August is the August owner's
explanation alone.

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
