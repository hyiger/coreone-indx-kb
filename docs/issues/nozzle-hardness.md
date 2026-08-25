---
title:        Nozzle hardness and abrasive filaments
confidence:   reported
updated:      2026-08-25
author:       hyiger
printer:      Core One
toolhead:     INDX
hotend:       CHT high-flow, and plain-bore variants
nozzle:       0.4mm standard
firmware:     unknown
sources:
  - https://help.prusa3d.com/article/unknown-nozzle-36121-core-one-indx_1072730
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/nozzlegate-communications/
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/bondtech-nozzle-hardening-debacle-how-does-this-affect-prusa-indx-orders/
  - https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/a-summary-of-common-indx-problems/
  - https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/missing-profiles-in-slicer-for-non-0-4-nozzles-and-other-materials/
superseded_by:
---

# Nozzle hardness and abrasive filaments

## Summary

The INDX was marketed with hardened nozzles rated for carbon- and glass-filled
filaments. The shipped nozzles are surface-treated rather than through-hardened, at a
hardness well below what the trade normally means by "hardened". If you bought an
INDX expecting to run abrasive filament from day one, you cannot, and the vendor has
published a remediation offer that includes a full return. Treat abrasive filament on
the current nozzles as consuming them.

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
resistance sufficient for carbon fibre, glass fibre and glow-in-the-dark filaments
without meaningful wear, and listed hardened nozzles as standard equipment. That
wording was later removed from shop listings, and the vendor published an admission
that the shipped nozzles are nitrocarburised — a surface treatment — at roughly
30–32 HRC.

For context on why owners consider that a material difference rather than a quibble:
the community position, argued at length in the threads, is that "hardened" in this
industry conventionally implies something in the region of 50–60 HRC, and that a
buyer could reasonably have read the marketing that way. A surface treatment in the
low thirties is much closer to untreated stainless than to a hardened nozzle.

Compounding it, the high-flow insert is plain brass. So even setting the body
treatment aside, filled filaments will erode the flow geometry. And retail packaging
and product pages still carried the original hardened claim when this became public.

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

**How the claim goes, from owners who have filed one.** The contact form has no
category that obviously fits, and owners report submitting under the generic "other"
request type. Expect an automated acknowledgement immediately and then a wait — one
owner reports writing a week earlier, being acknowledged, and still having no substantive
reply. Another filed the day this was written and says much the same. So file early, keep
your own record of what you asked for, and do not read silence as refusal.

You can also ask for a **mix** of credit and cash rather than all of one. At least one
owner did, wanting enough credit to buy a genuinely hardened nozzle once one exists.

!!! note "Store credit buys nozzles you may not be able to use yet"
    Worth knowing before you choose credit over cash: PrusaSlicer currently offers the
    INDX only a single nozzle variant, so other sizes have no profile to print with.
    One owner making exactly this decision put it plainly — they had never tried other
    sizes because there are no profiles for them, which makes credit-for-more-nozzles a
    weaker proposition than it looks. A page on the profile gap is drafted and awaiting
    review; until it lands, the short version is that both INDX printer models declare a
    single nozzle variant in Prusa's published profile bundle, so no other size is
    selectable.

Be aware the adequacy of the compensation is disputed. At least one owner worked
through the arithmetic and found the offered credit represents a substantially
smaller uplift than the hardened-over-standard premium in the vendor's own store and
at other nozzle manufacturers. That is a community calculation, not a vendor figure,
but it is a reasonable thing to check for yourself before accepting an option.

### What is coming

A third-party diamond-nozzle manufacturer has confirmed an INDX-compatible variant.
Notably, the diamond is doped to keep it detectable by the eddy-current offset sensor
— a fully non-conductive tip would be invisible to that sensor, which is a real
design constraint on any replacement nozzle. Timing was described in months
rather than weeks.

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
material in the threads rather than as owner inference.

!!! note "Why hardness figures appear here when other numbers do not"
    This site withholds calibration values, temperatures and print settings until a
    human has verified them on hardware. A hardness rating is a different kind of
    number: it is a published material property, not a value anyone dials into a
    slicer or a drill, so being wrong about it misinforms rather than damages
    hardware. The lower figure is the vendor's own published admission; the higher
    one is the industry convention owners are measuring it against, not a
    specification of any shipped part. Both are cited. Please do not strip them —
    without them the central claim of this page cannot be checked.

Weaker: the hardness figure a buyer "should" have expected is a community norm rather
than a published standard. The compensation-adequacy arithmetic is one owner's
calculation. The diamond-nozzle timeline is a third-party statement of intent.

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
