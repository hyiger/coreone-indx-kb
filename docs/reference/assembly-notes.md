---
title:        Assembly notes — INDX conversion kit
confidence:   reported
updated:      2026-10-25
author:       hyiger
printer:      Core One, Core One Plus
toolhead:     INDX
hotend:       unknown
nozzle:       unknown
firmware:     unknown
sources:
  - https://help.prusa3d.com/manual/bondtech-indx-conversion-kit-for-the-prusa-core-one-founders-edition_2397
  - https://help.prusa3d.com/manual/prusa-indx-conversion-kit-for-the-prusa-core-one_2432
  - https://help.prusa3d.com/guide/4-indx-toolhead-side-filament-sensors_1096247
  - https://help.prusa3d.com/guide/5-spoolholders-tool-dock-assembly_1096255
  - https://help.prusa3d.com/article/assemblling-the-prusa-indx-core-one-with-the-gen-2-upgrade_1147602
  - https://help.prusa3d.com/downloads/core-one-indx
  - https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/list-of-differences-between-founders-edition-and-prusa-edition-instructions/
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/why-4-8-tools-tested-if-only-less-are-needed/
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
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/how-many-types-of-fasteners-etc-come-with-indx-gen2-upgrade/
  - https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/indx-fe-upgrading-to-gen2/
  - https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/calibration-issues-from-beginning/
  - https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/bed-leveling-issues-3/
  - https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/the-worst-experience-of-any-3d-printer-assembly/
  - https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/upgrade-core1-to-indx-gen2/
  - https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/indx-assembly-guide/
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/mk4s-to-core-one-with-indx-conversion/
superseded_by:
---

# Assembly notes — INDX conversion kit

!!! info "This supplements the official guide, it does not replace it"
    Build from the official guide for your edition of the kit: the
    [Founders Edition guide](https://help.prusa3d.com/manual/bondtech-indx-conversion-kit-for-the-prusa-core-one-founders-edition_2397)
    for a kit from Bondtech, or the
    [Prusa edition guide](https://help.prusa3d.com/manual/prusa-indx-conversion-kit-for-the-prusa-core-one_2432)
    for Prusa's own. How the two differ is covered below. What follows is the
    accumulated experience of builders who have been through it — the steps worth
    slowing down for, the things worth staging in advance, and the places where the
    guide and reality have diverged.

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
  or firing rivets across the room. Small and quick. Not everyone sticks with it: one
  owner who had printed the rivet tools found a flat wood chisel, used bevel down, got
  under the rivet heads more easily. *Single report.*
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
  for the dock magnets, if you will be printing or adding docks of your own. Neither
  edition of the guide has you fit magnets into the tool holders the kit supplies.
- A **large sheet of cardboard** to stand the printer on, so you can spin and tilt it
  freely during the awkward steps.
- A **spare belt tensioner** or two, printed or bought while the printer still runs.
  The build takes the belts off and tensions them again, and owners in two threads
  report a tensioner part failing. One, whose printer has been through several
  conversions ending with the INDX, broke one along the way and says plenty of others
  have too. The other needed a new tensioner pulley part during the original Core One
  build and, with no second printer, had to wait for support to send one. Prusa's
  edition of the guide has you take the tensioning screws out and lubricate them
  during the belt work, to head off trouble later; the Founders Edition guide only
  loosens them. A self-printed replacement is not risk-free either: one owner fitted a
  community remix of the tensioner pulley holder that takes heat-set inserts instead of
  square nuts, had those printed parts split apart, and had to go through belt
  tensioning, homing and gantry squaring again. *Single report.*

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

## Founders Edition or Prusa edition

The kit comes in two editions, each with its own guide: the Founders Edition, sold by
Bondtech, and Prusa's own kit. Prusa hosts both guides, and their chapters and steps
line up almost one for one. An owner who asked on the forum for a list of the
differences got no official one. Set side by side as they stood on 18 October 2026,
the two guides differ in these places that change what you do:

- **Gen 2.** Only the Prusa guide covers the Gen 2 upgrade, and it marks each point
  where a combined build switches guides; see below. The Founders
  Edition guide leaves Gen 2 out entirely.
- **Belt tensioners.** The Prusa guide removes and lubricates the tensioning screws;
  the Founders Edition guide only loosens them.
- **Dock fan.** The parts differ in name and packing. The Prusa guide lists a print fan
  blower and a "dock fan splitter board", both from its electronics box, and one step
  later calls that board the FunFan board. The Founders Edition kit packs a dock fan
  blower and its FunFan board in a bag of their own. Neither guide says whether the
  parts themselves differ. On a Core One converted from an MK4 or MK4S, the Prusa guide
  swaps the two fans: the kit's blower becomes the print fan, because the converted
  printer's own fan has a much longer cable, and that removed fan becomes the dock fan.
- **Nozzle seal holders.** The Prusa guide adds an instruction to turn each assembled
  holder upside down before it is fitted, so the bent end of every seal points down.
  The Founders Edition guide has no such instruction. Both guides then have you match
  the bent ends to the illustration as you fit the holders.
- **Wiper.** The Prusa guide takes the right side cover off early in the tool dock
  chapter and mounts the nozzle cleaner to it off the printer; the Founders Edition
  guide leaves the panel on and fits the cleaner to it from inside the printer.
- **Firmware.** The Founders Edition guide flashes from a USB drive packed in the kit
  with the firmware already on it. The Prusa guide has you download the latest firmware
  onto a USB drive yourself, so have one ready.

Owners add differences in the parts themselves. One owner says the Prusa kit's front
panel drops the Founders Edition's cross struts, which opens up the view, and thinks
one edition may use some molded parts where the other has printed ones, without saying
which. This page's author adds that the nozzle seal adapters differ to suit the Prusa
front plate; the printed parts collection's separate nozzle seal holder for each
edition, noted under Sourcing below, fits that. The owner who described the front panel
also notes that newer Core One printers ship with a perforated right side panel to suit
the larger waste bin. Neither kit includes it, so an existing machine has to buy it separately.

**After any four-tool skip, check which guide you are in.** The Prusa guide's side
filament sensor chapter twice tells a four-tool builder to skip ahead, and both links
lead into the Founders Edition guide's matching chapter. One owner followed one and
carried on in the wrong guide into the next chapter before noticing, then left a
comment on the step with the right link. When this page was checked on 18 October
2026, both links still pointed to the Founders Edition guide. The steps straight
after the jump are nearly identical in both guides, so the slip costs little at first,
but the dock fan and nozzle seal holders differ further on. Look at the
guide's title at the top of the page after you jump.

*Mixed tiers.* The list of guide differences is this page's own comparison of the two
guides on that date; Prusa revises them, so check the live versions. The parts
differences are *provisional*: one owner's account and this page's author's, in a
single thread. The skip links rest on that owner's report and this page's check.

## Supply gotchas

**Short fastener counts are the single most common complaint.** More than one bag has
shipped with fewer screws than its label states, and at least one step calls for more
than several builders received. People have had to source or cut their own. This is
the reason for the screw assortment above — running out mid-step is the difference
between an evening and a weekend.

Kits vary. One owner whose upgrade kit arrived in late September 2026 found a single
spare of almost every fastener but no spare rivets, so one dropped screw would use up
the only spare; a Founders Edition builder in the same thread finished with screws left
over, though by their account some were left from building their Core One as a kit. An
owner who built the INDX and Gen 2 from a batch 7 upgrade kit was two screws short, one
bag holding a sheet-metal screw where the right one should have been, and nozzle wiper
parts were missing. Support sent a photo of the bag those parts should have been in,
then asked for photos of every remaining bag and part before sending replacements; the
owner photographed the empty bags too, so keeping them until the build is finished
lets you do the same. *Provisional*: each of these is one owner.

**There is no consolidated fastener list.** Fasteners are itemized step by step in the
guide and nowhere else, so if you like to pre-sort into labeled bins you will be
extracting that list yourself. Prusa's
[Core One INDX cheat sheet](https://www.prusa3d.com/downloads/others/C1_INDX_cheatsheet_EN_1_0.pdf)
is not necessarily that list: an owner asked whether every fastener and clip on its
chart comes in the kit, and the one reply said the chart is generic. *Single reply.*
An unofficial fastener PDF has circulated on the forum,
but it was AI-generated and unverified by its own poster — treat it as a starting
point to check against the guide, not as a bill of materials. The same goes for a later
AI-derived list of the fastener types in the INDX and Gen 2 kits together, which its
poster cautioned might be wrong and planned to check once the parts arrived.

**Do not expect tools in the box.** The conversion kit assumes the tools you need came
with the Core One already on your bench, and the introduction to both editions of the
guide says as much: use the tools supplied with the printer. The Founders Edition build
notes this page grew from list a single T10 driver in the kit. The Prusa-sold kit
reportedly has none at all, and a Prusa representative has confirmed on the forum that
this is by design: an upgrade kit relies on the set that shipped with the printer. If
your Core One came assembled, you may not have that set. The guide itself warns that
the T10 screwdriver came only with kit-built printers, though it calls that driver a
convenience rather than a necessity. The same representative says every printer, kit or assembled,
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
of Prusa INDX conversion kit orders, in a box of its own, intending it to go in during
the INDX build. Prusa's guide calls it optional: the INDX does not need it. Owners,
including one who found both in the box, have been unsure of the order, but Prusa has
set it out. The link in its announcement,
[prusa.io/Prusa-INDX-GEN-2](http://prusa.io/Prusa-INDX-GEN-2), leads not to a plain
Gen 2 guide but to a combined article that runs the INDX guide and the Gen 2 guide side
by side and names each step at which to switch, and the Prusa edition guide links to
it at those points. It brings in the first Gen 2 parts, the expansion joints, once the
bed spacers and the offset sensor are in, which is close to where this page's author
had been fitting the Gen 2 parts. It also has you lubricate the belt tensioner screws
with lubricant packed in the INDX kit, and has you unplug both motor cables, X and Y,
at the board near the start and plug them back in near the end, each into its labeled
connector — a chance to get them the wrong way around; see failures traced to assembly
mistakes below. Two owners in Prusa's announcement thread advise doing the two jobs
together, since both involve the belts and the bed; one, who had built a Founders
Edition kit, found that swapping the pulleys was all the Gen 2 work added. The article
does not mention the Gen 2 nozzle wiper. This page's author leaves it out, since the
INDX build has no use for it, and a Founders Edition owner in a separate thread
likewise says to skip that part.

Two comments on the combined article concern its photo of the X and Y cables going
back onto the board. One says the photo shows the Z motor cable in the wrong socket.
Another owner, whose rear Z motor would not run properly after the combined upgrade,
asks the same question and says their Z cable sat one socket right of where the photo
puts it. Which is right is unresolved, so plug each cable by the labels printed on the
board. *Provisional*: two comments on a single article, with no answer from Prusa.

After the first flash, check the hardware configuration screen: one owner, on the INDX
firmware current in mid-September 2026, before the stable 6.9.1 release, found it had
assumed the Gen 2 belts were fitted — rightly, in that case, but it had no means of
telling. A second owner, in a separate thread, found the same setting on a machine whose
Gen 2 parts were not yet fitted, and it made dock calibration fail; see
[dock calibration](../issues/dock-calibration-rejects-docks.md). Prusa's firmware source,
as published for 6.9.1, applies the Gen 2 variant on a first run, which would explain
both, though that flashing the INDX firmware counts as a first run is inferred, not
confirmed. None of 7.0.0, 7.0.1 (19 October 2026, a single fix for a freeze at startup)
or 8.0.0 (22 October 2026) has had its source published, and none of their
[notes](https://help.prusa3d.com/downloads/core-one-indx) mentions a change to this
default, so check the screen on any of them as well.

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
before you continue. Look over the rest of the motion system while it is apart: one
owner converting a factory-assembled Core One found one Y-axis rod slipped out of its
holder, the other loose, and loose screws on the X carriage, none of which they had
noticed before. *Single report.*

**Belt ends at the head's mounting plate.** The INDX head sits on a printed mounting
plate of its own, in place of the aluminum one, and that plate clamps the belt ends. Two
owners in one thread had belt ends pull out of it during belt tension calibration, one
of them again and again, even after squaring the gantry. Replies there were firm that a
correctly fitted belt does not come out: the two ends lie teeth to teeth so they lock
into each other, and running them right to the edge of the plate lets you see that
neither has slipped while you screw the plate down. The belt helper jig listed above is
one way to trim them level with that edge. Several owners, in three threads, back the
tensioners right off first, for enough slack to pull each end deep into the plate so
that plenty of teeth engage; that is what made the belts stay put for one of the two
owners above. Neither of them has said what was wrong in their case. *Provisional* for
the belts coming out: two owners, one thread; the slack technique is reported (see
Verification).

Belts set too tight bring their own trouble. The owner whose belts kept coming out
found the X axis calibration failed with the belts too tight, and another owner in the
same thread found the starting point they had been given for the tensioners far
tighter than where theirs ended up. *Provisional*: two owners, one thread. If the
gantry keeps drifting out of square, Prusa's handbook for the INDX lists a gantry
squareness wizard among the additions in its revision of 22 October 2026, published on
the [downloads page](https://help.prusa3d.com/downloads/core-one-indx) beside firmware
8.0.0; this page has not checked what it says.

TODO(verify): the starting tensioner setting one owner was given and where theirs
ended up. Both are stated in the source thread and are withheld here.

**Raising Z for the spoolholder screws.** The guide's stated Z height reportedly
exposes only two of the four screws. Builders report needing to go noticeably higher.

TODO(verify): the Z height the guide specifies and the height that actually works.
Both are stated in the source thread. Getting this wrong costs you nothing but
access, so the qualitative form — go higher than the guide says — is the usable part.

**Spool holder nuts at the back.** These nuts go in blind. You cannot hold the nut
holder and look along the side to line up the holes at the same time, and on the lower
holders the nuts end up behind the bed's drive parts. One owner building the INDX and
Gen 2 together recommends a second pair of hands, and found that a community-designed
backplate for the spool holders, printed beforehand, made fitting them much easier.
Printed nut helpers and a scrap of double-sided tape on a fingertip, from a separate
thread, are under adding Gen 2 to a finished Founders Edition build below.
*Single report*: the difficulty, the helper and the backplate are all one owner's.

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

How you tap matters as much as whether you do. One owner who built the INDX and Gen 2
together cut the tool holders' holes with a proper M3 tap in a tap wrench, drove the
screws with screwdriver-style drivers rather than an L-shaped hex key, and says to blow
the holes clean; the spare tool holders they had printed went unused. In that owner's
view the L-key is the problem whether it turns a tap or a bolt cutting its own thread,
so use a tap wrench or a screwdriver-style driver either way. A screw turned by an
L-key, they say, often leaves the hole worn and oversized, which is how they explain
the many replacement holders other owners have printed. That explanation is their
reading, not a tested cause. The same owner says to buy good drivers, since a cheap T10
tip needed grinding back more than once. A Founders Edition builder in another thread
found the screw holes in some of the kit's printed dock parts could have been better
made, and one owner's screws melted into dock parts, as noted under Sourcing below: two
different symptoms, each a single report.

## Tool dock magnets

The dock magnets are an **intentionally very tight press fit**, and this catches
everyone who meets it. Even getting a magnet started in its hole is a struggle, and
seating one fully takes real, directed force. Do not plan to do it by hand. Builders use a squeeze
clamp or a printed insertion jig. You meet it when you print, replace or add docks:
neither edition's current guide has a step that fits magnets into the tool holders the
kit supplies.

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
your own docks before you order. Two spring sizes are also needed, a large one in each
thimble and two small ones in each holder, which both editions of the guide list as
0.5 × 8.5 × 30 × 15 and 0.63 × 5 × 15 × 11. Note that the
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
could source elsewhere, and it is now among the parts in Prusa's shop. Prusa's own
four-tool kit leaves it out too: Prusa's guide tells a four-tool builder that only the
left sensor board, the one with two connectors, is in the box, and the Founders
Edition guide says the same of its kit. The printed block that houses the sensor holds
parts that are harder to find. The guide puts a steel ball and a 7 × 8 mm rod magnet
in each lane, the magnet sitting on the ball, with countersunk magnets screwed into
the block's top part:

- **Its countersunk magnets.** One owner measured them at 10 mm across and 5 mm thick
  and found a match online, in a grade whose relation to the original is unknown. The
  guide lists them as Magnet 3.2 x 5 and calls them a 5x2 magnet in the step text;
  neither designation obviously matches that measurement, so measure before ordering. A
  second owner has since found another listing at that size, which states no grade at
  all. The author of this page has not found a source and suspects they are custom; a
  further owner is still looking. That first owner notes the sensor depends on magnet
  strength more than the dock does, because it works by Hall effect. Yet another
  owner, who believes they now have the parts for a do-it-yourself expansion, settled
  on a near match for the sensor's ring-shaped magnets (presumably the countersunk
  ones, though the post does not say) in early October 2026 and has yet to learn
  whether the sensor calibrates with it. No substitute has so far been reported
  working in the sensor.
- **The 7 × 8 mm rod magnets.** They are the size one owner measured for the dock's
  activation magnet, and they can be hard to find: an owner sourcing in the US in
  October 2026 found the dock's smaller rods online but no 7 × 8 mm rod at a sensible
  price, and settled on two stacked 7 × 4 mm magnets in each 7 × 8 mm position, in the
  sensor and the dock thimble alike. Their kit had not arrived by mid-October, so the stack is
  untested. *Single report.*
- **The plain plastic spacers inside the printed housing** — not the collets the PTFE
  plugs into. No source is known. The guide lists a small sleeve for each lane
  alongside the collets, designated 2 × 5, which may be these. One owner went a
  different way, with a community adapter that takes standard PC4-M10 push fittings and
  lets the PTFE tube pass straight through. *Single report.*

!!! warning "Reports of a magnet grade substitution"
    The author of this page replaced the original dock magnets with a stronger grade
    and found they hold the tools more firmly, and notes the original grade is
    unusually hard to source outside Europe. A second owner, in a separate thread, runs
    the stronger grade in self-printed docks without trouble and finds they grip
    perhaps a little tighter — but those magnets were also slightly larger, set in a
    pocket that owner had enlarged in the printed file, so the report does not isolate
    the grade. There is **no independent like-for-like report**. Stronger magnets
    change the force the mechanism has to overcome on every pickup and drop, and
    long-term results are thin: about two months after first reporting the change, the
    author reports no drawbacks and no unexplained tool drops since, which is still the
    author's account alone. A further owner, who finds the stock magnets hold the tools
    a little loosely, is weighing the same change. If you are only trying to source
    replacements, match the original specification.

## Expectations to set before first boot

**There is no filament sensor at the toolhead.** The INDX has side sensors only, which
is confirmed in the firmware source as published for 6.9.1; nothing in the
[7.0.0, 7.0.1 or 8.0.0 release notes](https://help.prusa3d.com/downloads/core-one-indx)
suggests a change. In practice: auto-load works only for the
currently picked tool, you feed each filament to the head manually with only the last
short section pulled in, and there is **no clog or runout detection at the head
itself**. This surprises people coming from a Nextruder. Prusa's INDX handbook, in
its revision 1.03 of 22 October 2026 on the
[downloads page](https://help.prusa3d.com/downloads/core-one-indx), updated the
filament loading procedure; this page has not checked that against the description
here.

**Four-tool and eight-tool kits share a guide.** Steps illustrating eight PTFE tubes
or eight cables are normal — a four-tool kit uses half, and only one wire runs to the
sensor on that version. The guide lets it go into either of the sensor board's two
connectors.

**Before a print, only the tools it uses are calibrated.** One owner thought the
printer tested every tool before each print, then realized they had mostly been
watching prints that used all eight; another owner in the same thread confirms that only the
tools in the job are calibrated. What the start of a print runs, and when it falls back to
calibrating every tool, is on the [profile G-code page](../gcode/indx-profile-gcode.md).
*Single thread.*

**Only one Z-motor connector is used.** An empty one is expected, not a mistake.

**Flash firmware from a USB drive** (the one in the kit for the Founders Edition, your
own for Prusa's), not over the network. Some firmware instructions were inherited from
the plain Core One guide and sit awkwardly here.

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

## Failures traced to assembly mistakes

Two failures have turned out to be assembly mistakes, each confirmed as the cause by
the owner who made it:

- **X and Y motor cables swapped at the board.** One owner who had fitted both the INDX
  and the Gen 2 upgrade could get the X and Y axis calibrations to pass only with
  the tools taken out; with them in, the head ran into the docked tools. Belt tuning
  passed its first gantry check, then on a second pass tried to drive the head out past
  the printer's frame, and homing kept tugging tool 8 in its dock until it gave up.
  Another forum member suggested checking which motor went to which socket on the
  xBuddy board, and putting the two cables back the right way around fixed everything
  ([thread](https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/calibration-issues-from-beginning/)).
  Prusa's combined INDX and Gen 2 article, described above, unplugs both cables
  partway through; the owner does not say whether that is when the swap happened.
- **An old heat bed spacer refitted.** One owner whose probing kept failing at the back
  right of the bed worked through a long list of checks before finding they had mixed
  up the bed spacers and put the old one back instead of its replacement. With the
  correct spacer in, probing worked
  ([thread](https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/bed-leveling-issues-3/)).

*Provisional.* Each of these is a single report, from its own thread.

A third failure at the back right of the bed may also come down to assembly, though its
cause is not confirmed. In the
[same thread](https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/bed-leveling-issues-3/)
as the spacer, an owner whose probing failed at that corner every time a print used more
of the bed watched the heated bed's cable bunch up beneath it, leaving the back of the
bed lower than the front. They later said they had found their issue in how that cable
was routed: still behind a rod, but moved from under the heated bed to above it, as
best their wording can be read. They were still sorting out leveling afterwards. A
later owner in that thread has the same failure on prints that cover the whole bed,
still undiagnosed, and the spacer owner above first reported the same symptom in that
thread, so it has more than one cause. Another owner, who had just finished their
build, says the guide does not make clear that the bed cable should hang behind the
rear Z lead screw; they let it drape in a loose, even curve with its wires lying side
by side and none crossing, and bend it tightly where it enters the chamber and tie it
down firmly there, so that the bed can travel freely. If probing fails only at the back
right, checking how the heated bed's cable is routed, and that nothing pinches it, costs
little; that is a suggestion drawn from these reports, not a confirmed fix.
*Provisional*: one owner's account of the routing, one owner's routing advice and one
undiagnosed repeat, all in one thread, with the cause unconfirmed.

## Adding Gen 2 to a finished Founders Edition build

Founders Edition owners get the Gen 2 parts separately rather than in the INDX box, and
some fit them to a machine that has been printing with the INDX for a while. One owner
who had just received the Gen 2 upgrade for such a machine could not find a Prusa guide
that starts from a converted printer, an owner in a separate thread says none has been
released, and a comment on Prusa's combined article says the same. That article covers
only doing both jobs at once. What owners who replied to that first owner report:

- **Switch off and unplug first.** None of the replies says whether the printer was
  powered down, but every step below leaves the head and motor cables connected to the
  board, so do this work with the printer off and disconnected from the mains.
- **The head comes off without unplugging it.** Removing the part-cooling blower
  exposes the four screws that hold the print head, and the main cable can stay
  connected. This rests on the page author's account alone.
- **The motor cables can stay on the board.** This page's author and one other owner
  both swapped the pulleys with the X and Y motor cables still connected to the board,
  and both found the cables had enough slack for it. The author rested each motor on a
  bar while working on it; the other owner left the back cover on.
- **The side panels are optional.** This page's author points out that a flexible
  driver extension reaches the motor screws with the panels in place; one owner took
  them off regardless.
- **Draw the new belts in with the old ones.** One owner fixed each new belt to its
  old one with tape and drew it through along the old belt's route, all while the
  motors were still bolted in place. The same owner unscrewed the tensioners all the
  way out to get slack for attaching the belt ends at the head's mounting plate, kept
  screws in the loose square nuts — in the tensioners and in the fan-duct mounts on
  the head — so none could drop out, and greased the tensioner nuts before putting the
  tensioners back so the threads would not gall.
- **Refitting the spool holders.** With the side panels off, the nuts for the rear
  holders are hard to start. This page's author held each nut on a fingertip with a
  scrap of strong double-sided tape; two other owners suggested printed nut-helper
  tools instead.

*Provisional.* All of the steps above come from a single thread. The head-removal step,
the flexible-extension route and the tape trick rest on this page author's account alone.

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
  and nowhere else. The cheat sheet question, its one reply and the AI-derived list
  of types are all in
  [a thread on the fasteners in the INDX and Gen 2 kits](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/how-many-types-of-fasteners-etc-come-with-indx-gen2-upgrade/).
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
  four-tool kit, but the
  [Prusa guide's side filament sensor chapter](https://help.prusa3d.com/guide/4-indx-toolhead-side-filament-sensors_1096247)
  states it; the same chapter of the Founders Edition guide says the same of that
  edition's kit, which also confirms the owners' reports. The Prusa chapter is the
  source for the steel ball and 7 × 8 mm magnet in each lane, the sleeves and the
  countersunk magnets' designations. The US owner's stacked magnets appear in both of
  those threads, from the same owner, so they count once.
- **Kits without tools** rest on a single thread,
  [one about the missing tools](https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/no-tools-in-my-indx-upgrade-kit/),
  but it carries the vendor's own statement: two owners report it there, and a Prusa
  representative confirms the policy and gives the reasoning. No second thread repeats
  it, but the introduction to both editions of the guide says the same, and is the
  source for the note on the T10 driver and assembled printers. The lone T10 driver in
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
  that the Gen 2 upgrade was packed with their INDX kit. The order of work, the motor
  cables and the tensioner lubricant are Prusa's own, in its
  [combined article](https://help.prusa3d.com/article/assemblling-the-prusa-indx-core-one-with-the-gen-2-upgrade_1147602),
  which the announcement's short link reaches and which was last revised on
  15 October 2026; the optional status is from the Prusa guide's introduction. The two
  comments on its reconnection photo are on that article's own page.
- **The two editions and their guides.** The differences in what you do come from
  setting the two guides side by side on 18 October 2026, chapter by chapter; the
  tensioner, dock fan and nozzle seal holder steps described are in the
  [Prusa guide's chapter 4](https://help.prusa3d.com/guide/4-indx-toolhead-side-filament-sensors_1096247)
  and [chapter 5](https://help.prusa3d.com/guide/5-spoolholders-tool-dock-assembly_1096255).
  The parts differences, the side panel and the misdirected skip link are from
  [a thread asking for that list](https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/list-of-differences-between-founders-edition-and-prusa-edition-instructions/);
  the nozzle seal adapters there are this page's author's, and are not counted. That
  both skip links still pointed to the Founders Edition guide is this page's own check
  on that date. The absence of a magnet step for the kit's own tool holders is from
  the same reading of both guides.
- **Only the tools a print uses are calibrated** rests on
  [one thread](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/why-4-8-tools-tested-if-only-less-are-needed/),
  where the owner who asked corrected themselves and one other owner agreed. This
  page's author answered there too, and is not counted.
- **Spare belt tensioners** rest on two owners in separate threads, one in the thread
  on swapping an MMU3 for the INDX linked above and one in Prusa's shipping
  announcement thread. The same advice appears in the latter from this page's author,
  and is not counted.
- **Slack when fitting the belt ends** rests on four owners in three threads: the owner
  whose belts stayed put once they had slack, one who says they always work that way and
  one who agrees it is standard on a stock Core One are in
  [a thread on a difficult build](https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/the-worst-experience-of-any-3d-printer-assembly/);
  the one who always works that way gives the same advice in the
  [thread on adding Gen 2 to a Founders Edition build](https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/indx-fe-upgrading-to-gen2/),
  so counts once; and a further owner, who had found it helped when building a
  Core One, gives it in
  [a thread on the published guide](https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/indx-assembly-guide/).
  That the head's mounting plate is printed and clamps the belt ends is from an owner
  reading the guide in that last thread and an owner who printed the plate in advance, in
  [a thread on converting an MK4S](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/mk4s-to-core-one-with-indx-conversion/).
  This page's author also replied in the first thread, and is not counted. The belts
  coming out at all are two owners in that one thread, so *provisional*, as is the note
  on belts set too tight. The handbook's gantry squareness wizard, like its updated
  filament loading procedure noted under first boot, is from the change list on
  Prusa's downloads page, as it stood on 25 October 2026.
- **Screw-hole trouble in printed dock parts** is two different symptoms, each a
  single report: one Founders Edition builder found the screw holes in some of the
  kit's printed dock parts could have been better made, in the thread on a difficult
  build, and one owner had screws melt into dock parts, in the thread on growing a
  four-tool kit to eight. The owner who tapped the tool holders, in
  [a thread on an INDX and Gen 2 build](https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/upgrade-core1-to-indx-gen2/),
  had no trouble of their own; their explanation of others' reprints is their reading
  alone.

Weaker: the MK4S bootloader lockout is one owner's experience, and is flagged as such
in place. It comes from the general discussion thread, which is overwhelmingly
shipping and order chatter — it was found by reading all 1534 posts, and it is one of
only two durable technical items that survived review out of that entire thread. Also
single reports, and marked in place: the belt setting after the first flash, the
assembled printer that arrived without tools, the screws that melted into dock parts,
the sensor-housing spacer workaround, the countersunk magnet measurement along with the
two listings found at that size and the near match still awaiting a test, and both
assembly mistakes, each from its own thread, along with the heated bed cable routing
that may be a third and one owner's advice on routing that cable, both from the
spacer's thread. From the thread on an INDX and Gen 2 build, all from the one owner
who started it: the wood chisel for rivets, the split tensioner remix, the loose rod
and carriage screws, the short screws and missing wiper parts with support's request
for photos, and the spool holder backplate. The kit with one spare of nearly every
fastener and the Founders Edition build with screws left over are one owner each in
the thread on a difficult build. The activation magnet size rests on one
owner's measurement set against a figure nobody measured. Where in the INDX sequence
the Gen 2 parts go is now Prusa's own, in the combined article; this page's author's
earlier practice is close to it but is not evidence. Leaving out the nozzle wiper is
the author's practice, which the article neither confirms nor contradicts, and has one
independent voice, in
[a separate thread](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/bondtech-founders-edition-upgrade-path-to-core-one-gen-2/).
The notes on adding Gen 2 to a finished Founders Edition build all come from
[one thread on that retrofit](https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/indx-fe-upgrading-to-gen2/):
the head-removal step, the flexible-extension route with the side panels on and the tape
trick for the spool-holder nuts are this page author's alone, the motor-cable slack has one
independent owner beside the author, and the belt, square-nut and tensioner tips are
one owner's. That Founders Edition owners buy the Gen 2 parts separately is said there
and in the thread linked just above. That Prusa has no guide starting from a converted
printer is said there, in the thread on the differences between editions, and in a
comment on Prusa's combined article.
The magnet grade substitution was first reported by this page's author, and there is
no independent like-for-like account: the one other owner who reports it changed the
magnet size as well as the grade. The author's two-month follow-up and the owner
weighing the change are both in the
[thread on removing dock magnets](https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/removing-magnets-from-tool-docks-you-dont-need-to-destroy-them/).
The circulating unofficial fastener PDF was described by the person sharing
it as AI-generated and unverified, and is recorded here only as something you may
encounter, not as a resource to rely on.

This page deliberately does **not** reproduce the official guide's step sequence. It
records where builders got stuck, which is the part the guide cannot tell you.

## Related

- [Tool offset calibration fails](../issues/offset-sensor-board-failure.md) — the most common
  first-boot failure
- [Probing fails or nozzle never touches the bed](../issues/loadcell-emi-noise.md) — if the
  loadcell test is unstable out of the box
- [Dock calibration rejects some or all docks](../issues/dock-calibration-rejects-docks.md) —
  if dock calibration fails on a fresh build; check the belt setting first
- [Input shaper calibration stops with "Measurement failed"](../issues/input-shaper-measurement-failed.md)
  — if input shaper calibration fails right after the accelerometer calibrates; check
  the belt setting first
- [Who to contact](../issues/support-and-warranty-path.md) — support and warranty routing
