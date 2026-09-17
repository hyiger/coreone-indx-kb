---
title:        Silicone sock migration over the temperature sensor
confidence:   provisional
updated:      2026-09-16
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
enough to partially cover the toolhead's temperature sensor window. With the sensor
partially obscured the nozzle runs hotter than commanded. On the PET family, and
reportedly worst on PCTG, the excess heat bakes filament onto the nozzle tip, and the
resulting deposit is enough to make tool offset calibration fail.

The fix is trivial once you know to look: seat the sock back down. The reason to know
about it is that every symptom it produces points somewhere else — at the nozzle, at
the filament, or at the offset sensor.

## Not the offset sensor

**This is a temperature sensor, not the tool offset sensor.** They are different
components with different sensing principles, and the distinction matters because the
symptom — failed offset calibration — points at the wrong one.

One account describes the obscured part as an IR window; another describes it as the
temperature sensor rectangle. Both descriptions are thermal. The tool offset sensor is
separately documented as eddy-current based, and eddy-current sensing has no optical
window to obscure. See [offset sensor board failure](offset-sensor-board-failure.md)
for that component.

TODO(verify): whether the "IR window" and the "temperature sensor rectangle" are the
same physical feature, and what sensing principle the toolhead's temperature sensor
actually uses. Two owners describe it in different words and neither is confirmed
against a schematic or the vendor's documentation.

## Detail

### Sock migration

The sock is reported to slide upward from where it seats. One owner found it partially
covering the temperature sensor and got a thermal runaway error as a direct result —
that is a first-hand account of the occlusion and its immediate consequence. The author of this
page found the sock displaced on three separate nozzles on one machine, and another
owner, in a [separate thread](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/problems-with-nozzle-socks/), had to reseat it on two tools after only a
couple of test prints. The migration is no longer something seen on one machine.

Why it migrates is not established. None of the accounts identifies a trigger, and
neither the vendor nor the community has published a cause.

### Overheating and caking

A partially covered thermal sensor reads low, so the heater drives harder to reach a
target the machine believes it has not met. The nozzle then runs above the commanded
temperature.

Filament caking on INDX nozzle tips is independently reported and does not depend on
this page's chain being right: the PET family in general, and PCTG in particular, is
described as sticking to these nozzles readily. One owner attributes that partly to the
sock geometry, noting that it extends nearly to the tip so deposits have something to
cling to, and contrasts it with coated nozzles that shed material better.

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
the sensor window before investigating the sensor, the nozzle or the filament. It costs
seconds and it is reversible.

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
to tear the sock. Spares were not included in the kit. The vendor has since told this page's author
that socks will soon be sold on its store as a five-pack, at 4.90 USD when announced in
September 2026; another owner was told by Prusa's support that socks will be stocked
there later too; other INDX spares such as sensor boards and silicone
wipers are reportedly already in Prusa's shop. For this page's author, shipping and import
charges came to several times the price of the sock itself, so until a nearer source has
them a torn sock may still mean a wait and a bill.

**Clean the tip if material has already baked on.** See
[oozing during probing](oozing-during-probing-and-calibration.md) for the
cleaning caution — remove debris, do not polish the sensor face.

## Verification

`provisional` — the chain rests on one account.

What is corroborated, in different threads by different owners:

- **Sock migration, now in two threads.** One first-hand report in the
  [maintenance thread](https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/indx-maintenance/)
  describes a thermal runaway error caused by exactly this, and a second owner in
  [a later thread](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/problems-with-nozzle-socks/) had to reseat the sock on two tools. That later thread was
  started by this page's author, but the corroborating account is another owner's, which
  is why it counts. Taken alone, the migration claim now meets `reported`; the page as a
  whole stays `provisional` because the chain below it does not.
- **PET-family and PCTG caking onto INDX nozzle tips**, including the observation that
  the sock geometry contributes, in the
  [wiper thread](https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/nozzle-wiper-vs-indx-offset-sensor/).

What is **not** corroborated is the causal chain joining them: that the occlusion is
what drives the caking, and that the caking is what fails the calibration. That is this
page author's own first-hand observation, repeated across three nozzles on one machine —
which is why the page exists, but it is still one machine and one observer, and no
temperature was measured. Both ends are individually supported; the join between them is
inferred.

The suggestion that the nozzle or sock needs a design revision is this author's
conclusion, not a vendor position, and is recorded as opinion rather than finding. So
are two later additions, the author's own and from a single machine: the sock torn by a
blob, and what spares cost to ship.

The guidance on running without a sock, and the coming five-pack, are the vendor's —
but they arrived as a private reply to this page's author, so they are first-party yet
uncheckable by a reader, and are marked `provisional` here for that reason. They replace
an earlier warning against removing the sock that was the author's inference from
firmware source and never tested. What Prusa's support said about stocking socks is
relayed from another owner's replies in a [thread the author started](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/filament-blobs-can-tear-the-silicon-sock-on-indx-nozzles/), and is
not published by either company.

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
