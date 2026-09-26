---
title:        Silicone sock migration over the temperature sensor
confidence:   provisional
updated:      2026-09-25
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

TODO(verify): whether the window the maintenance thread's opening post says to keep
clean is the same feature as the temperature sensor rectangle the sock covers, and what
sensing principle the toolhead's temperature sensor actually uses. None of these
descriptions is confirmed against a schematic or the vendor's documentation.

## Detail

### Sock migration

The sock is reported to slide upward from where it seats. This page's author found it
partially covering the temperature sensor and got a thermal runaway error as a direct
result — a first-hand account of the occlusion and its immediate consequence — and by
late August had reseated the sock on three nozzles on one machine. Another owner,
replying in the [thread](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/problems-with-nozzle-socks/) where the author reported those three nozzles, had to
reseat it on two tools after only a couple of test prints. The migration is no longer
something seen on one machine, but so far it has been seen on only two. In a
[separate thread](https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/missing-layers-5/),
the author suggested a slipped sock as one possible cause of another owner's missing
layers; that owner checked, found the sock had not moved, and later traced the fault to
the slicer.

Why it migrates is not established. None of the accounts identifies a trigger, and
neither the vendor nor the community has published a cause.

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
migration, the caking claim rests on one independent owner in one thread, so on its own
it is `provisional`.

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
September 2026, and within days they were listed there, though on backorder as of 19
September; another owner was told by Prusa's support that socks will be stocked
there later too; Prusa's shop now lists INDX parts individually,
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
  the maintenance-thread report as a second owner's and rated migration `reported`;
  that was wrong.
- **PET-family caking onto INDX nozzle tips**, from one other owner in the
  [wiper thread](https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/nozzle-wiper-vs-indx-offset-sensor/);
  a second owner there sees the blobbing but attributes it to the wiper, not the nozzle.
  Like migration, this is one independent owner in one thread, so the caking claim taken
  alone is `provisional`. The PCTG report and the observation that the sock geometry
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
