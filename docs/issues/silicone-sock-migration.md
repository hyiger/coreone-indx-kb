---
title:        Silicone sock migration over the temperature sensor
confidence:   provisional
updated:      2026-10-25
author:       hyiger
printer:      Core One
toolhead:     INDX
hotend:       unknown
nozzle:       unknown
firmware:     unknown
sources:
  - https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/indx-maintenance/
  - https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/nozzle-wiper-vs-indx-offset-sensor/
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/problems-with-nozzle-socks/
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/filament-blobs-can-tear-the-silicon-sock-on-indx-nozzles/
  - https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/missing-layers-5/
  - https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/bondtech-nozzles-dont-ship/
  - https://help.prusa3d.com/article/hotend-thermal-runaway-36204-indx_1088706
  - https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/core-1-indx-generic-petg-preset-hotend-thermal-runaway-error/
superseded_by:
---

# Silicone sock migration over the temperature sensor

!!! warning "A chain assembled from separate reports"
    Each link in this chain is reported by someone. The **chain as a whole** — sock
    migration causing overheating causing caking causing calibration failure — comes
    from a single account. Read the Verification section before treating it as
    established.

## Summary

The silicone sock on an INDX nozzle can creep upward from its seated position far
enough to partially cover the rectangular pad on the nozzle, evidently the target the
toolhead reads the nozzle's temperature from (Prusa's thermal runaway article has
owners keep a "measuring pad" clean, but does not tie that name to this rectangle
outright). With the pad
partially obscured the nozzle runs hotter than commanded. On the PET family, and in
this page author's experience PCTG in particular, the excess heat bakes filament onto
the nozzle tip, and the resulting deposit is enough to make tool offset calibration
fail.

The fix is trivial once you know to look: seat the sock back down. The reason to know
about it is that every symptom it produces points somewhere else — at the nozzle, at
the filament, or at the offset sensor.

## Not the offset sensor

**This is a temperature sensor, not the tool offset sensor.** They are different
components with different sensing principles, and the distinction matters because the
symptom — failed offset calibration — points at the wrong one.

This page's author has described the obscured part both as an IR window and as the
temperature sensor rectangle, in more than one thread. Both descriptions are thermal.
The tool offset sensor is separately documented as eddy-current based, and eddy-current
sensing has no optical window to obscure. See
[offset sensor board failure](offset-sensor-board-failure.md) for that component.

The maintenance thread's opening post, from another owner, independently calls the part
in front of the tool a temperature sensing window, though the cleaning advice under that
heading is relayed second-hand and the symptom it names for a dirty window is poor bed
probing rather than a temperature fault. This page is not alone in being unsure which
part is meant: on 25 September 2026 another owner asked in that thread whether the
small window its opening post says to keep clean is this same rectangle or some other
part, and the question was still unanswered that day.

Prusa's own documentation comes close to settling what the rectangle is for.
According to
[Prusa's article on the INDX hotend thermal runaway error](https://help.prusa3d.com/article/hotend-thermal-runaway-36204-indx_1088706),
the error's on-screen message sends the owner to the black rectangle on the tool, which
it calls the "heat block", to check it for contamination; and when the error is
confined to one nozzle, the article has them make sure the "measuring pad" is clean and
free of debris. Taken together, and from the name "measuring pad", the rectangle is
evidently the target the nozzle's temperature is read from, though the article does not
say so in as many words, nor say outright that the two names mean the same part. That
contamination on it can bring on a thermal runaway error, the on-screen message itself
implies. The article does not name the sensing principle and does not mention the sock.
Owners commenting under it, like this page's author elsewhere, call the sensor
infrared; the vendor does not say so there.

TODO(verify): whether the window the maintenance thread's opening post says to keep
clean is the measuring pad on the nozzle or some other part of the head, and what
sensing principle the toolhead's temperature sensor actually uses. Prusa's article
points to what the pad does but describes neither.

## Detail

### Sock migration

The sock is reported to slide upward from where it seats. This page's author found it
partially covering the temperature sensor and got a thermal runaway error as a direct
result — a first-hand account of the occlusion and its immediate consequence — and by
late August had reseated the sock on three nozzles on one machine. Another owner,
replying in the [thread](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/problems-with-nozzle-socks/) where the author reported those three nozzles, had to
reseat it on two tools after only a couple of test prints.

A third owner has since given the first account, other than the author's own, of a
displaced sock and a thermal runaway error together. In a comment of 23 October 2026
under [Prusa's article on that error](https://help.prusa3d.com/article/hotend-thermal-runaway-36204-indx_1088706),
they report two prints on their newly converted printer stopped by it, both times on the
same tool. On that tool they found the sock shifted so that it partly covered the pad,
and they nudged it back by hand. Whether that ended the errors they had not yet said.
A displaced sock over the pad has now been seen on three machines; this owner does not
say whether theirs moved in use or was never seated properly after the conversion. In a
[separate thread](https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/missing-layers-5/),
the author suggested a slipped sock as one possible cause of another owner's missing
layers; that owner checked, found the sock had not moved, and later traced the fault to
the slicer.

Why it migrates is not established. This page's author has since named scrubbing the
nozzle with a brass brush as one way the sock gets dragged up, in a
[thread on a thermal runaway error](https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/core-1-indx-generic-petg-preset-hotend-thermal-runaway-error/),
but no account ties a particular slip to it, and neither the vendor nor the community
has published a cause.

A thermal runaway error is not by itself evidence of a slipped sock. In that same
thread, an owner whose PETG prints were stopped by the error on more than one nozzle
judged from a photo they posted that their socks were properly seated. By their account,
Prusa's support put it down to the generic PETG profile. Drying the filament got one
small print through, but a larger one failed again, and the cause was still open on
24 October 2026.

### Overheating and caking

A partially covered thermal sensor reads low, so the heater drives harder to reach a
target the machine believes it has not met. The nozzle then runs above the commanded
temperature.

Filament caking on INDX nozzle tips is reported apart from this page's chain and does
not depend on the chain being right, though the support for it is thin: one other owner
describes PETG in particular as sticking to these nozzles readily, and this page's
author reports the same of PCTG. The author attributes that partly to the sock
geometry, noting that it extends nearly to the tip so deposits have something to cling
to. Earlier in the same thread, though, the author said that one PCTG they use, a single
brand and color, sticks to the nozzle and sheds small blobs on all of their printers,
not only the INDX; so, at least for that filament, the author's PCTG report does not
isolate the INDX nozzle or its sock. A
second owner in the same thread sees PETG blobbing too, but is not convinced it is
material sticking to the nozzle during a print, and puts it down to the wiper not being
left clean instead. Coated nozzles were put forward in the same thread as shedding
material better, but another owner there has seen no difference, with PETG building up
on coated nozzles as readily as on plain ones, so that contrast is disputed. Like
migration in use, the caking claim rests on one independent owner in one thread, so on
its own it is `provisional`.

Overheating making that worse is mechanistically plausible and is what the single
full-chain account describes, but it is inference rather than a measured relationship.

### Calibration failure

A deposit on the nozzle tip changes what the offset sensor sees. Tool offset
calibration then fails. This connects to the existing account of contamination
defeating calibration in
[oozing during probing](oozing-during-probing-and-calibration.md), by a
different route to the same place.

## What to do

**Check the sock before you chase anything else.** If offset calibration has started
failing on a tool that was previously fine, look at whether the sock has crept up over
the measuring pad before investigating the sensor, the nozzle or the filament. It costs
seconds and it is reversible. The same goes for a hotend thermal runaway error, where
Prusa's article draws a useful line: if the error stays with one nozzle, check that
nozzle's pad; if it follows the head from nozzle to nozzle, contact support.

**Seat it back down.** Every account of migration describes simply pushing the sock
back into position, and none needed a replacement part to do it.

**Running briefly without a sock is fine, per the vendor — but it is not a fix.** The
vendor's after-sales support, answering this page's author directly, says a tool can run
without its sock for a short while without any problem. That takes precedence over an
earlier warning on this page, which rested on the author's own reading of the firmware
source: that the nozzle's temperature measurement assumes a sock is fitted, so running
bare could push the reading far enough off to trip a thermal runaway error. The two are
not far apart. The vendor's answer covers a short while, and the concern was never
tested — so treat a missing sock as a stopgap until a replacement arrives, not as a way
to stop migration or a permanent state.

**Inspect the socks from time to time.** With no known trigger and no fix, looking is
the only defense. It is worth a look after a blob in particular: on the author's
machine a lump of PCTG stuck to a nozzle tip was dragged through the wiper hard enough
to tear the sock. In the author's view it is worth one after brushing the tip too, for
the reason given under "Sock migration" above.
Spares were not included in the kit. The vendor has since told this page's author
that socks will soon be sold on its store as a five-pack, at 4.90 USD when announced in
September 2026, and within days they were listed there, though on backorder as of 19
September. At least one order has since gone out: one owner reports socks they ordered there with
nozzles on 8 October 2026 shipping a week later. Another owner was told by Prusa's
support that socks will be stocked in Prusa's shop later too; Prusa's shop now lists INDX parts individually,
including a [tool holder with magnets](https://www.prusa3d.com/product/tool-holder-with-magnets-2/) and the
[INDX filament sensor cable](https://www.prusa3d.com/product/filament-sensor-cable-for-indx/), and sensor boards and silicone wipers are
reported there too. For this page's author, shipping and import
charges came to several times the price of the sock itself, so until a nearer source has
them a torn sock may still mean a wait and a bill.

**Clean the tip if material has already baked on.** See
[oozing during probing](oozing-during-probing-and-calibration.md) for the
cleaning caution — remove debris, do not polish the sensor face.

## Verification

`provisional` — the chain rests on one account.

What is corroborated by owners other than the author:

- **Sock migration, on two machines.** The first-hand report in the
  [maintenance thread](https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/indx-maintenance/)
  of a thermal runaway error caused by exactly this is the author's own, as is the
  three-nozzle account. The independent corroboration is a second owner in
  [a later thread](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/problems-with-nozzle-socks/) who had to reseat the sock on two tools. That thread was
  started by this page's author, but the corroborating account is another owner's, which
  is why it counts. One independent owner in one thread does not meet `reported`, so the
  migration claim taken alone is `provisional` too. Earlier versions of this page read
  the maintenance-thread report as a second owner's and rated migration `reported` on
  that basis; that was wrong.
- **A displaced sock over the pad, one further owner.** A third owner, commenting under
  [Prusa's thermal runaway article](https://help.prusa3d.com/article/hotend-thermal-runaway-36204-indx_1088706),
  found a shifted sock partly over the pad on the one tool that had stopped their prints
  twice. Their printer was newly converted, and they do not say whether the sock moved
  in use or was never seated properly, so this is displacement, not creep in use. A
  displaced sock over the pad, as distinct from migration, therefore now has two
  independent owners in two separate places, but the migration claim taken alone stays
  `provisional`. Prusa's article itself lists debris on the pad among the things to
  check for that error, but does not mention the sock; that the shifted sock caused
  those errors is this owner's own suspicion, with the outcome not yet posted, so that
  link is `provisional`.
- **PET-family caking onto INDX nozzle tips**, from one other owner in the
  [wiper thread](https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/nozzle-wiper-vs-indx-offset-sensor/);
  a second owner there sees the blobbing but attributes it to the wiper, not the nozzle.
  That is one independent owner in one thread, so the caking claim taken alone is
  `provisional`. The PCTG report and the observation that the sock geometry
  contributes are the author's own, in the same thread, where the author also says the
  one PCTG they named sticks on all of their printers, not only the INDX.

What is **not** corroborated is the causal chain joining them: that the occlusion is
what drives the caking, and that the caking is what fails the calibration. That is this
page author's own first-hand observation, repeated across three nozzles on one machine —
which is why the page exists, but it is still one machine and one observer, and no
temperature was measured. Both ends are individually supported; the join between them is
inferred.

The suggestion that the nozzle or sock needs a design revision is this author's
conclusion, not a vendor position, and is recorded as opinion rather than finding. So
are two later additions, the author's own and from a single machine: the sock torn by a
blob, and what spares cost to ship. So, too, is the author's suggestion that brushing
the tip drags the sock up. The PETG thermal runaway case in the same thread is one
owner's and unresolved. It is cited only as a caution against reading every such error
as a slipped sock, not as evidence about the sock.

The guidance on running without a sock, and the coming five-pack, are the vendor's —
but they arrived as a private reply to this page's author, so they are first-party yet
uncheckable by a reader, and are marked `provisional` here for that reason. They replace
an earlier warning against removing the sock that was the author's inference from
firmware source and never tested. What Prusa's support said about stocking socks is
relayed from another owner's replies in a [thread the author started](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/filament-blobs-can-tear-the-silicon-sock-on-indx-nozzles/), and is
not published by either company. That a sock order has since shipped from the vendor's
store rests on one owner's post in a
[thread about nozzle shipments](https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/bondtech-nozzles-dont-ship/).

What would move this to `reported`: a second owner describing the full sequence —
displaced sock, then overheating, then caking, then failed calibration — in a citable
venue. A measurement of actual versus commanded nozzle temperature with the sensor
partially covered would be better still, and would make the middle of the chain
`measured`.

## Related

- [Offset sensor board failure](offset-sensor-board-failure.md) — the
  eddy-current sensor this is often mistaken for
- [Oozing during probing](oozing-during-probing-and-calibration.md) —
  contamination defeating calibration by another route
- [Nozzle hardness](nozzle-hardness.md) — other nozzle-level defects
