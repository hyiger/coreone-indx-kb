---
title:        Assembly notes — INDX conversion kit
confidence:   reported
updated:      2026-09-25
author:       hyiger
printer:      Core One, Core One Plus
toolhead:     INDX
hotend:       unknown
nozzle:       unknown
firmware:     unknown
sources:
  - https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/bondtech-indx-conversion-kit-assembly-pain-points-prep-notes/
  - https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/sourcing-tool-dock-hardware/
  - https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/removing-magnets-from-tool-docks-you-dont-need-to-destroy-them/
  - https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/parts-list-for-screws-and-bolts/
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/update-kind-of/
  - https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/no-tools-in-my-indx-upgrade-kit/
  - https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/core-one-to-core-onegen2-indx-upgrade-path/
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/prusa-indx-update-shipping-starts-this-week/
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/bondtech-founders-edition-upgrade-path-to-core-one-gen-2/
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/coreone-with-mmu-upgrade-to-indx/
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/update-kit-from-indx-4t-to-8t/
superseded_by:
---

# Assembly notes — INDX conversion kit

!!! info "This supplements the official guide, it does not replace it"
    Build from the
    [official Bondtech INDX conversion guide](https://help.prusa3d.com/manual/bondtech-indx-conversion-kit-for-the-prusa-core-one-founders-edition_2397).
    What follows is the accumulated experience of builders who have been through it —
    the steps worth slowing down for, the things worth staging in advance, and the
    places where the guide and reality have diverged.

    Prusa actively fixes reported problems in the guide, so some of what is recorded
    here may already have been corrected. Treat the live guide as authoritative and
    this page as the thing that warns you what is coming.

## Summary

Most of the pain in this build is avoidable with preparation. Print three things
first, stage a small screw assortment and an M3 tap, and know in advance which four
or five steps consistently catch people out. The build is long rather than difficult;
the frustrations come from running out of a fastener mid-step, or from discovering
that a printed part needed tapping after you have already started driving screws.

## Print these before you begin

- **A snap-rivet remover.** Disassembly means pulling a lot of nylon snap rivets, and
  this is the most-praised pre-print by a wide margin. It stops you scratching panels
  or firing rivets across the room. Small and quick.
- **A belt helper jig.** Community-made to the official mounting-plate geometry. It
  holds both belts together so they end up the same length under the same tension,
  lets you trim them level with the mounting plate, and lets you return them to the
  identical position afterwards. Belts and toolhead mounting are the fiddliest part of
  the build, and this takes much of the sting out. Building it takes heat-set inserts
  and a handful of M3 screws, so run it off and gather those parts before you get
  there.
- **Any structural parts you owe yourself.** Printed parts are version-lettered, and
  which ones ship with the kit depends on the series. Some are supplied by Prusa in
  the box; others are download-and-print-yourself and are identical to the factory
  parts. Check your part bags against the official collection *before* you start
  rather than discovering a gap mid-build.

Download a **fresh copy** of the official parts collection rather than reusing files
you grabbed earlier. It has been revised since release — the docking panel now
uses less material, and the silicone cleaner and waste bin are included — so older
downloads will not match the current guide.

## Stage these

- A small **M3 screw assortment**. See the fastener shortfalls below.
- An **M3 tap**, or a spare M3 bolt to hand-tap with.
- A **clamp** — a squeeze clamp of the quick-grip type — or a printed insertion jig,
  for the dock magnets.
- A **large sheet of cardboard** to stand the printer on, so you can spin and tilt it
  freely during the awkward steps.
- A **spare belt tensioner** or two, printed or bought while the printer still runs.
  The build takes the belts off and tensions them again, and owners in two threads
  report a tensioner part failing. One, whose printer has been through several
  conversions ending with the INDX, broke one along the way and says plenty of others
  have too. The other needed a new tensioner pulley part during the original Core One
  build and, with no second printer, had to wait for support to send one.

**Check your build plate now, not afterwards.** If you print on an oversized
third-party flex sheet, it may stop clearing the tool docks once they are installed —
even though it fits your machine perfectly well today. See
[build plate compatibility](build-plate-compatibility.md). Sorting this out before you
start beats finishing the build and finding your go-to sheet unusable.

!!! danger "Update the firmware *before* you take the old printer apart"
    If you are converting a machine that started life as an MK4S, bring its firmware
    up to the level the conversion requires **while it is still assembled and
    working**. One owner built the INDX kit onto an MK4S-to-Core One upgrade without
    ever running the Core One in its Nextruder form, and without raising the MK4S
    firmware first. The assembled machine came up to a red error screen on first power
    on, with no route forward from the screen itself.

    The recovery, if you are already in this position: refit the original Nextruder
    and disconnect the door sensor, so the bootloader identifies the machine as an
    MK4S again. That is enough to let the firmware updates run, after which you can
    reassemble the conversion.

    *Single report.* One owner, first-hand, who recovered the machine — but nobody
    has reproduced it, and the recovery involves partly undoing your build. Read it
    as a reason to update early rather than as a procedure you should expect to need.

## Supply gotchas

**Short fastener counts are the single most common complaint.** More than one bag has
shipped with fewer screws than its label states, and at least one step calls for more
than several builders received. People have had to source or cut their own. This is
the reason for the screw assortment above — running out mid-step is the difference
between an evening and a weekend.

**There is no consolidated fastener list.** Fasteners are itemized step by step in the
guide and nowhere else, so if you like to pre-sort into labeled bins you will be
extracting that list yourself. An unofficial fastener PDF has circulated on the forum,
but it was AI-generated and unverified by its own poster — treat it as a starting
point to check against the guide, not as a bill of materials.

**Do not expect tools in the box.** The conversion kit assumes the tools you need came
with the Core One already on your bench. The Founders Edition build notes this page
grew from list a single T10 driver in the kit. The Prusa-sold kit reportedly has none
at all, and a Prusa representative has confirmed on the forum that this is by design:
an upgrade kit relies on the set that shipped with the printer. If your Core One came
assembled, you may not have that set. The same representative says every printer, kit or assembled,
is meant to include tools, and that support will help if yours did not — yet one owner
of an assembled machine never received any. Check before you start, not at the first
screw.

**MMU3 owners:** it must come off first, and the guide barely covers removal. Plan it
as a separate task before you start the conversion proper. It is less work than the
guide's advice to reverse the MMU assembly suggests. One owner who converted from an
MMU3 points out that the whole extruder is replaced — nothing survives except a few
screws and the part-cooling fan — so there is no need to undo the MMU's changes to it
one by one; they lifted the unit out with its cables and tubes. Owners in a separate
thread describe the same conversion as straightforward.

**Some kits arrive with a second upgrade inside.** Prusa included its Core One+ (Gen 2)
upgrade — new belts, belt pulleys and thermal expansion joints — with the first batch
of Prusa INDX conversion kit orders, intending it to go in during the INDX build, and
pointed to its [Gen 2 upgrade guide](http://prusa.io/Prusa-INDX-GEN-2) for that.
Owners, including one who found both in the box, have still been unsure of the order.
Two owners in Prusa's announcement thread advise doing the two together, since both
jobs involve the belts and the bed; one, who had built a Founders Edition kit, found that swapping the pulleys
was all the Gen 2 work added. The exact point is this page author's own practice: the
Gen 2 parts go in straight after the heat bed spacers in the INDX sequence, and the
Gen 2 nozzle wiper stays out, since the INDX build has no use for it; a Founders
Edition owner in a separate thread likewise says to skip that part. After the first
flash, check the hardware configuration screen: one owner, on the INDX firmware
current in mid-September 2026, before the stable 6.9.1 release, found it had assumed
the Gen 2 belts were fitted — rightly, in that case, but it had no means of telling.
*Single report* for the belt setting, and whether 6.9.1 behaves the same way has not
been reported.

## Steps to slow down on

**Connecting the head cable.** The most-cursed step in the build. The technique that
works is to feed only a short length of the nylon pull-string through first, secure
the cable cover, and *then* feed the rest — otherwise tension keeps pulling the string
back out of its slot.

TODO(verify): the length of pull-string to feed before securing the cover.

**Aligning the linear rail.** Loosen the six rail screws **only two or three turns** —
Prusa confirmed this in the guide comments. Do not fully unscrew them: the center
block can drop out, and reassembling it is genuinely miserable. This is a good moment
to re-lubricate the rail while you have access. Tighten the bottom gantry screw again
before you continue.

**Raising Z for the spoolholder screws.** The guide's stated Z height reportedly
exposes only two of the four screws. Builders report needing to go noticeably higher.

TODO(verify): the Z height the guide specifies and the height that actually works.
Both are stated in the source thread. Getting this wrong costs you nothing but
access, so the qualitative form — go higher than the guide says — is the usable part.

**Offset sensor cabling.** Thread the offset sensor cable through the hole **first**,
then the thicker RGB LED cable. The other order does not fit. Watch the screw at that
location: it is a blind, awkward reach and the thread strips easily. One builder
fitted a heat-set insert rather than fight it.

**Filament sensor blocks.** The ball-detection screws want to be left slack — loose
enough that the steel ball drops back down on its own. Test each block before you
mount it; checking afterwards is much harder.

**Tapping printed parts.** Countersunk and self-tapping screws strip easily here and
the holes run tight. Pre-tap with a spare M3 bolt. The tool-holder front face alone
has upwards of two dozen holes to tap, so settle in and go slowly — slipping scars the
front panel.

## Tool dock magnets

The dock magnets are an **intentionally very tight press fit**, and this catches
everyone. Even the starter holes are hard to begin, and seating a magnet fully takes
real, directed force. Do not plan to do it by hand. Builders use a squeeze clamp or a
printed insertion jig.

### If you are reprinting docks and need the magnets back

You do not have to destroy the old docks. The technique reported with photographs is
to lay the dock face down on a cutting mat, place a straight mini-pick tip behind
where the magnet sits, and push it steadily through — PETG gives way with little
force — then draw the magnet out with pliers from the other side. Keep your free hand
clear in case the pick slips.

The alternative reported approach is simply to reprint the parts and buy fresh
magnets, treating the old ones as consumed.

### Sourcing

An owner adding docks to a four-tool kit compiled sources for the hardware. The dock
magnets are 3 × 8 mm neodymium rods. The activation magnet in the dock's thimble is
where accounts disagree. The size first circulated, an unusual 5 × 8.47 mm rod that
very few suppliers stock, came from a vendor chat channel rather than a measurement.
The owner who compiled the list later measured the magnet in an installed dock at
7 × 8 mm and settled on that size for the official printed parts, while a second owner
wondered whether the smaller figure belongs to a different kit. A community thimble
remix takes the 5 mm magnet, and worked in the compiling owner's dock. Measure one of
your own docks before you order. Two spring sizes are also needed. Note that the
printed parts collection contains **a separate nozzle seal holder for each edition**,
Founders Edition and Prusa, so check which you need before printing. The seal itself
has a known substitute: owners in two threads point to the Prusa XL's spare nozzle
seal, whose blade is slightly shorter, in a remixed holder that compensates.

Buying the parts has since become simpler. Prusa's shop now lists INDX components
individually — among them a [tool holder with magnets](https://www.prusa3d.com/product/tool-holder-with-magnets-2/), a side filament sensor,
and the [INDX filament sensor cable](https://www.prusa3d.com/product/filament-sensor-cable-for-indx/) — and passive tools have been reported in
stock in the vendor's shop. If you are adding docks, check the ready-made holder before
hunting down magnets separately; what exactly it includes is worth confirming on the
listing. Not everyone would buy it, though. One owner, who had two screws melt into the
kit-supplied dock parts despite pre-threading them by hand, recommends printing a
community variant that takes nyloc nuts and sourcing the magnets yourself. Whether the
holder now sold on its own shares that weakness has not been reported.

**Going from four tools to eight.** No dedicated upgrade kit has been announced.
Prusa's product listing describes the two kit sizes as sharing the Smart Head and
docking hardware and differing only in the number of passive tools, which can be added
later. Owners of four-tool Founders Edition kits report a further difference, from
their own machines: tools five to eight run through a second, right-hand side filament
sensor that their kit did not include, and adding them also takes its cable, more PTFE
tubing and — if you want them — spool holders. That sensor was the one part nobody
could source elsewhere, and it is now among the parts in Prusa's shop. That fits the
one statement so far about Prusa's own four-tool kit, that it lacks the sensor as well,
but does not confirm it: the statement is one owner's, second-hand, made before they
had added any tools. The printed block that houses the sensor holds parts that are
harder to find:

- **Its countersunk magnets.** One owner measured them at 10 mm across and 5 mm thick
  and found a match online, in a grade whose relation to the original is unknown; the
  author of this page has not found a source and suspects they are custom; a third
  owner is still looking. That first owner notes the sensor depends on magnet strength
  more than the dock does, because it works by Hall effect.
- **The plain plastic spacers inside the printed housing** — not the collets the PTFE
  plugs into. No source is known. One owner went a different way, with a community
  adapter that takes standard PC4-M10 push fittings and lets the PTFE tube pass
  straight through. *Single report.*

!!! warning "Reports of a magnet grade substitution"
    The author of this page replaced the original dock magnets with a stronger grade
    and found they hold the tools more firmly, and notes the original grade is
    unusually hard to source outside Europe. A second owner, in a separate thread, runs
    the stronger grade in self-printed docks without trouble and finds they grip
    perhaps a little tighter — but those magnets were also slightly larger, set in a
    pocket that owner had enlarged in the printed file, so the report does not isolate
    the grade. There is **no independent like-for-like report**. Stronger magnets
    change the force the mechanism has to overcome on every pickup and drop, and nobody
    has reported long-term results. If you are only trying to source replacements,
    match the original specification.

## Expectations to set before first boot

**There is no filament sensor at the toolhead.** The INDX has side sensors only, which
is confirmed in the firmware source. In practice: auto-load works only for the
currently picked tool, you feed each filament to the head manually with only the last
short section pulled in, and there is **no clog or runout detection at the head
itself**. This surprises people coming from a Nextruder.

**Four-tool and eight-tool kits share a guide.** Steps illustrating eight PTFE tubes
or eight cables are normal — a four-tool kit uses half, and only one wire runs to the
sensor on that version.

**Only one Z-motor connector is used.** An empty one is expected, not a mistake.

**Flash firmware from the USB drive**, not over the network. Some firmware
instructions were inherited from the plain Core One guide and sit awkwardly here.

## If the first selftest fails

Two calibration failures recur on builds that are otherwise fine, and both have their
own pages:

- A **heater test** failure reporting nozzle temperature out of range. One builder
  cleared it by running the calibration again with filament already loaded. It has the
  shape of a firmware issue rather than a build error.
- **Tool offset out of bounds**, sometimes alongside an unstable loadcell test. See
  [tool offset calibration](../issues/offset-sensor-board-failure.md) and
  [loadcell noise](../issues/loadcell-emi-noise.md).

TODO(verify): the temperature the heater test reports and the acceptance window it is
checked against. Both appear in the source thread and are withheld here.

The vendor's guidance is to be on current INDX firmware, run calibration with filament
loaded, and — if it still fails — to take the full log to support rather than finding a
fresh way around it each time. The machine depends on those calibrations being right,
so a workaround here only compounds later.

## Where files and help come from

Prusa publishes the official printed parts to Printables. Bondtech publishes the INDX
CAD to GitHub rather than to a Printables account, and most of the community jigs and
tools you will find are remixes of that CAD.

Founders Edition build and calibration help is handled by Bondtech, largely through
its Discord, rather than going to Prusa support directly. Several builders report the
Discord hard to navigate. Posting on the Prusa forum is also a valid route — a community manager
forwards threads to the developers — and a forum post is searchable later in a way a
chat message is not. Include your firmware version, tool count, and the exact failing
step. See [who to contact](../issues/support-and-warranty-path.md) for the split between
diagnosis and parts once you are past the build.

## Verification

`reported` — assembly experience is spread across several independent threads and
many builders.

The principal source is
[Assembly Pain Points & Prep Notes](https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/bondtech-indx-conversion-kit-assembly-pain-points-prep-notes/),
a 194-post thread whose opening post is a compilation drawn from several hundred
comments left on the official guide's own steps, plus forum reports. That compilation
is second-hand relative to the individual builders who reported each item, but it
aggregates a much larger body of experience than any single thread here contains.

The support for each claim, item by item:

- **The absent fastener list** is confirmed by
  [Parts list for screws and bolts?](https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/parts-list-for-screws-and-bolts/),
  where a builder asks for one and is told the guide itemizes fasteners step by step
  and nowhere else.
- **The magnet press fit and extraction** are covered first-hand with photographs in
  [Removing magnets from Tool docks](https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/removing-magnets-from-tool-docks-you-dont-need-to-destroy-them/),
  by a builder who did it, with two further owners describing alternative approaches.
- **Hardware sourcing** comes from
  [Sourcing tool dock hardware](https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/sourcing-tool-dock-hardware/),
  which is marked answered and compiled by an owner adding docks to a four-tool kit.
  The second side filament sensor missing from four-tool Founders Edition kits, and the
  XL nozzle seal as a stand-in, are both reported there and again in
  [a thread on growing a four-tool kit to eight](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/update-kit-from-indx-4t-to-8t/).
  Neither thread has a first-hand report of the sensor from an owner of Prusa's
  four-tool kit.
- **Kits without tools** rest on a single thread,
  [one about the missing tools](https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/no-tools-in-my-indx-upgrade-kit/),
  but it carries the vendor's own statement: two owners report it there, and a Prusa
  representative confirms the policy and gives the reasoning. No second thread repeats
  it. The lone T10 driver in
  the Founders Edition kit rests only on the compilation above, which this page's
  author wrote, so it adds no independent support.
- **The thin MMU3 removal step** is raised again in
  [a thread on combining Gen 2 with the INDX](https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/core-one-to-core-onegen2-indx-upgrade-path/),
  and owners in
  [another on swapping an MMU3 for the INDX](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/coreone-with-mmu-upgrade-to-indx/)
  describe that conversion as uneventful.
- **Gen 2 parts in the first kits** is Prusa's own statement, in its
  [shipping announcement](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/prusa-indx-update-shipping-starts-this-week/),
  which also says to fit them while installing the INDX. Two owners in the same thread
  independently advise doing the two jobs together. An owner confirms in a separate
  thread,
  [the one on combining Gen 2 with the INDX](https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/core-one-to-core-onegen2-indx-upgrade-path/),
  that the Gen 2 upgrade was packed with their INDX kit.
- **Spare belt tensioners** rest on two owners in separate threads, one in the thread
  on swapping an MMU3 for the INDX linked above and one in Prusa's shipping
  announcement thread. The same advice appears in the latter from this page's author,
  and is not counted.

Weaker: the MK4S bootloader lockout is one owner's experience, and is flagged as such
in place. It comes from the general discussion thread, which is overwhelmingly
shipping and order chatter — it was found by reading all 1534 posts, and it is one of
only two durable technical items that survived review out of that entire thread. Also
single reports, and marked in place: the belt setting after the first flash, the
assembled printer that arrived without tools, the screws that melted into dock parts,
the sensor-housing spacer workaround and the countersunk magnet measurement. The
activation magnet size rests on one owner's measurement set against a figure nobody
measured. The exact point in the INDX sequence where the Gen 2 parts go is this page
author's own practice; fitting them during the INDX build has the support noted above,
and leaving out the nozzle wiper has one independent voice, in
[a separate thread](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/bondtech-founders-edition-upgrade-path-to-core-one-gen-2/).
The magnet grade substitution was first reported by this page's author, and there is
no independent like-for-like account: the one other owner who reports it changed the
magnet size as well as the grade. The circulating unofficial fastener PDF was described by the person sharing
it as AI-generated and unverified, and is recorded here only as something you may
encounter, not as a resource to rely on.

This page deliberately does **not** reproduce the official guide's step sequence. It
records where builders got stuck, which is the part the guide cannot tell you.

## Related

- [Tool offset calibration fails](../issues/offset-sensor-board-failure.md) — the most common
  first-boot failure
- [Probing fails or nozzle never touches the bed](../issues/loadcell-emi-noise.md) — if the
  loadcell test is unstable out of the box
- [Who to contact](../issues/support-and-warranty-path.md) — support and warranty routing
