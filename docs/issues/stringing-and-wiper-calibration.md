---
title:        Blobs dragged into the print — nozzle wiper and purge
confidence:   reported
updated:      2026-11-10
author:       hyiger
printer:      Core One
toolhead:     INDX
hotend:       unknown
nozzle:       0.4mm reported
firmware:     6.9.0, re-checked against 6.9.1, 6.9.2, 7.0.0, 7.0.1 and 8.0.0 (notes and source); earlier behavior noted throughout
sources:
  - https://help.prusa3d.com/downloads/core-one-indx
  - https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/nozzle-cleaning-calibration-issues/
  - https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/nozzle-wiper-vs-indx-offset-sensor/
  - https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/a-summary-of-common-indx-problems/
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.9.1-beta
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.9.1
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/compare/v6.9.1-beta...v6.9.1
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5391
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5496
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5505
  - https://forum.prusa3d.com/forum/prusa-indx-how-do-i-print-this-printing-help/nozzle-cleaning-strange-results/
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/src/feature/indx_nozzle_cleaner_calibration/indx_nozzle_cleaner_calibration.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/src/feature/indx_nozzle_cleaner_calibration/screen_nozzle_cleaner_calibration.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/src/feature/tool_offset_calibration/tool_offset_calibration.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/src/feature/nozzle_cleaner/nozzle_cleaner.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/src/common/mapi/calibration_preamble.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5500
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5412
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5477
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.9.2
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/compare/v6.9.1...v6.9.2
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.10.1
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/cleaning-nozzle-2/
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/indx-review/
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5567
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5568
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5563
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/maybe-im-becoming-a-convert/
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v7.0.0
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v7.0.1
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v8.0.0
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/compare/v6.9.2...v8.0.0
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/src/feature/nozzle_cleaner/nozzle_cleaner.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/src/common/gcode/gcode_loader.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/src/feature/tool_offset_calibration/tool_offset_calibration.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/src/feature/indx_nozzle_cleaner_calibration/screen_nozzle_cleaner_calibration.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/src/common/mapi/parking.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/src/gui/MItem_hardware.hpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/ProjectOptions.cmake
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/src/feature/wastebin_watcher/wastebin_watcher.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.2/src/feature/wastebin_watcher/wastebin_watcher.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/commit/fcccaa10c62d0e399210bc7aabb14c868e3c5a33
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/commit/596d5330f3a5afde6b6eaefa6f60e9cb12882074
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5410
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5576
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/core-one-indx-blobs-at-color-change-layers-nozzle-wiper-dropping-filament-onto-print/
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/solved-tpu-tangling-at-the-extruder-after-indx-tool-changes-the-nozzle-was-too-cold-during-cleaning/
superseded_by:
---

# Blobs dragged into the print — nozzle wiper and purge

!!! tip "Update to 6.9.0 or later before doing anything else"
    Firmware 6.9.0 introduced **automatic calibration of the nozzle cleaner** — this
    is confirmed in Prusa's own release notes, not just inferred from owner reports.
    The same release moved the purge point in Y and made the nozzle reheat in the
    cleaner when a print resumes. Owners additionally describe a revised wiping path
    and changed purge amounts. In the firmware source, "automatic" means the cleaner's
    position in X and Y, which the loadcell finds by touching it. The height of the
    silicone is still set by hand with a screw — see the warning under *Deeper than you
    would think*.

    Three owners independently report the difference as dramatic — clean tool changes
    across mixed-material prints, one no longer needing a brim to catch debris on the
    first layer, and — most tellingly — the owner who opened the original complaint
    thread reporting that 6.9.0 has largely settled both the oozing and the cleaning.
    That did not hold for good. Weeks later the same owner, still on 6.9.0, had a print
    fail on a different filament and then could not get tool calibration to pass, which
    was new for them; after resetting the machine and recalibrating every tool, they had
    the oozing back as well. They then reported every calibration passing on a 6.9.1
    build, without making clear which one; Prusa's 6.9.1 was at that point out only as a
    beta. See [tool offset calibration](offset-sensor-board-failure.md).

    Most of the manual procedure below exists because that calibration used to be
    done by hand, badly, with no way to see what you were doing. If you are on anything
    older than 6.9.0, update and re-test before investing any time in manual alignment.
    Height is the exception: it is still a manual step in every release through 8.0.0,
    whose wizard asks for the screw step in the same words as 6.9.0's did.

    The stable 6.9.1 notes name no change to the wiper or the purge. The beta did one
    thing for the cleaner: where appropriate, the bed now moves down during Nozzle
    Cleaner calibration, leaving room for a hand or a wrench. The stable notes do not
    repeat it, but the stable is built on the beta: in the firmware repository it adds
    [15 commits](https://github.com/prusa3d/Prusa-Firmware-Buddy/compare/v6.9.1-beta...v6.9.1)
    to the beta tag, none of them about the nozzle cleaner. That comes from the release
    history, not from the notes. 6.9.2, released 2026-10-07, leaves all of this as it
    was: it is 6.9.1 plus the PVA and BVOH filament presets that the 6.9.1 notes
    announced but left out, and nothing else that reaches an INDX
    ([compare](https://github.com/prusa3d/Prusa-Firmware-Buddy/compare/v6.9.1...v6.9.2)).

    Firmware 7.0.0, dated 15 October 2026 on
    [Prusa's downloads page](https://help.prusa3d.com/downloads/core-one-indx), has two
    lines on the cleaner. One promises improved Nozzle Wiper cleaning without saying what
    changed; the notes tag it as already shipped in
    [6.10.1](https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.10.1), which
    was firmware for the XL and XL+, not for the INDX. The source, which Prusa published
    on 3 November, shows that it does not reach an INDX at all: Nozzle Wiper is the
    firmware's name for the wiper accessory of printers without an INDX, its code is not
    built for the INDX, and that code is where the 7.0.0 work went. The INDX's own cleaning
    sequences are the same at the v6.9.2 and v8.0.0 tags. The other line moves filament
    loading and unloading to positions that take account of the calibrated cleaner offset;
    in the source both positions sit over the waste bin, where the park and purge points
    already used that offset. One INDX owner has since reported on the wipe under 7.0.0,
    and for PETG they find it worse than under 6.9.0, not better (see *Residue left by the
    clean before calibration* below). That is a single report, and the source has no 7.0.0
    change to the INDX wipe that would explain it; the cooler calibration of 6.9.1, which
    they blame, is the change that lies between.

    Firmware 8.0.0, dated 22 October 2026 on the same page, has two lines that come near
    the cleaner, and the fuller notes Prusa put on GitHub on 3 November add a third.
    Flexible filaments are now slowed down less while the nozzle is cleaned; the GitHub
    notes widen that to every extruder move the firmware makes with a filament marked
    flexible, from loading and purging to tool changes and cleaning. The bed drops further
    during calibrations that need a hand inside the printer, which reads as a continuation
    of the 6.9.1 beta change above, and the GitHub notes name them: Dock Calibration,
    Nozzle Cleaner Calibration and the Gantry Squareness check. The third line claims a
    more accurate nozzle cleaner calibration; in the source the wizard now homes precisely
    before the loadcell touches the cleaner, the same kind of homing the printer does when
    it later applies the stored offsets
    ([commit](https://github.com/prusa3d/Prusa-Firmware-Buddy/commit/fcccaa10c62d0e399210bc7aabb14c868e3c5a33)).
    None of them touches wiper height, the cleaning temperature, the order of purge,
    cool-down and wipe, or the amount purged, and the source bears that out (see
    *Verification*). The first INDX owners to describe the wipe on 8.0.0 saw purge carried
    onto the print; one of them, who believes they are on 8.0.0, thinks that lining the
    nozzle up differently during the calibration cured most of it. Their reports are under *Deeper than you would think*
    below.

    Several owners have found material still on the nozzle after the clean that runs as
    a print begins, mostly PETG and PCTG, and one finds it more often on 6.9.2 and 7.0.0
    than on 6.9.0. They put it down variously to the order of that clean and to its
    temperature, and neither has changed through 8.0.0. That is set out under *Residue
    left by the clean before calibration* below.

## Summary

On firmware before 6.9.0, the most common INDX print-quality complaint was filament
being dragged out of the purge area and deposited on the print — blobs, zits and
strings appearing at the start of a print and at tool changes. The cause is usually
not the filament: it is where the nozzle sits relative to the silicone wiper block
when it purges. Sitting *in* the purge material rather than clear of it is what lets
a blob stick to the nozzle and ride out onto the part.

## Detail

### What is actually happening

At a tool change the head purges into the bin, then retreats past the silicone block
at the front on its way to the part. Owners consistently describe the same sequence: the
purge happens, the nozzle drags some of it along on the way back, sits in it briefly,
and then carries it onto the sheet. It shows up on the first tool of a print and
again at subsequent changes.

It is material-dependent in a way that rules out a single simple cause. PLA prints
often come through clean while PETG and ABS do not. Ooze explains the PETG case
plausibly, but one owner specifically noted ABS blobbing too, which ooze alone does
not account for — stickiness of the purge material against the nozzle wall matters as
much as how much oozes.

### Read the pellets — this is the best diagnostic on this page

The shape of the discarded purge material tells you where you are, with no
measurement required:

- **Compact, rice-grain pellets** — the classic "good" result.
- **Long worms, tadpoles, or strands stuck together** — the purge is stretching
  rather than breaking cleanly.

A small change in the Y position flips between these two outcomes. That sensitivity
is the single most useful thing to know before you start adjusting, because it means
you are looking for a narrow window, not a broad one.

TODO(verify): the Y adjustment magnitude that one owner reported as the difference
between rice grains and worms. It is a small fraction of a millimeter and it is
machine-specific, so it is withheld here rather than published as a target.

!!! note "Which pellet shape is actually better is disputed"
    The community knowledge base recorded the 6.6.2-era shift from compact pellets to
    stringy tails as a regression. An owner in the forum thread later argued the
    opposite — that worms may have been deliberate, because a worm keeps the nozzle
    from nestling into the top of a blob, detaches more readily, and does less damage
    if it does reach the print. Both readings are in the sources. A later report adds a
    data point without settling it: the same owner cited in the warning box below found
    their purge coming out as worms joined end to end, some of which landed on the bed.
    Treat pellet shape as a *sensitive indicator that your alignment changed*, which it
    certainly is, rather than as a target to optimize toward.

### The real difficulty is that you cannot see it

Owners are unanimous that the hard part is visibility, not judgment. The wiper sits
where you cannot get eyes on it during a purge, and people resorted to dentists'
mirrors. Two techniques circulate:

- **Backlight it.** Put a light source behind the bin and adjust until the light just
  disappears behind the nozzle. This gives a repeatable visual reference where direct
  observation gives none.
- **Adjust during a print.** From 6.6.3 onward there is a *Nozzle Cleaner Y Offset*
  item in the printer's Tune menu, reachable while a print is running, so you can
  change position and immediately see the effect on the next pellet. Earlier firmware
  exposed X and Y cleaning offsets the same way. Note that these are only reachable
  mid-print, which is deliberate — you need a running print to have anything to judge.

TODO(verify): the direction and magnitude of a useful Nozzle Cleaner Y Offset. This
one is genuinely per-machine — the community knowledge base records owners reporting
success with offsets in **opposite directions**, so there is no correct value to
publish. Establish your own from the pellet shape.

### Deeper than you would think

The most useful pre-6.9.0 finding, and the one with the clearest first-hand
confirmation, concerns Z rather than Y. The working position is **deep** — the nozzle
genuinely down in the silicone rather than lightly grazing it.

One owner reasoned that burying the nozzle in the silicone would seal it and prevent
a final blob forming, tested it, and reported back that doing so **completely cured**
their ABS blobbing — on the opening tool and on every later change alike. The community
knowledge base independently records a systematic height test reaching the same
conclusion: the working position is deeper than the light-contact rule of thumb
people assume.

If you are calibrating by hand, err deep rather than shallow.

TODO(verify): the nominal gap figure that this finding contradicts, and any measured
depth. Neither is published here — the actionable form is directional ("deeper than
just touching"), which needs no number.

!!! warning "An open question about the automatic calibration"
    Before 6.9.0 shipped, an owner raised the concern that if an automated routine
    calibrates to *just touching*, it might reinstate exactly the blobbing that
    burying the nozzle cured. Early reports on 6.9.0 are good and do not show this,
    but nobody has confirmed what depth the automatic routine actually targets. If
    you update and blobbing returns having previously been fixed by going deep, this
    is the first thing to suspect.

    The firmware source narrows the question. The automatic part of the Nozzle Cleaner
    Calibration wizard measures where the cleaner sits in X and Y; it does not set the
    depth. Height is a one-time manual step in the same wizard, which asks you to rest
    the nozzle in the center of the silicone V-groove and then shows: "Turn the
    adjustment screw counterclockwise until it touches the silicone." The wizard's own
    steps are the same from 6.9.0 through 8.0.0, which changed only how it homes before
    measuring and how far it lowers the bed, so on all of them the depth is whatever that
    screw step leaves, and the criterion the wizard states is contact, not burial. That is a
    reading of the code; nobody has reported comparing the result against the deeper
    setting on hardware, so the question stays open.

    It matters because owners can read the 6.9.0 notes as meaning the cleaner now sets
    itself up entirely. One owner who mentioned 6.9.0, whose purge was not coming out as
    rice grains and was filling the bin fast, assumed just that and said calibration no
    longer asked about the wiper; a reply told them to raise the wiper pad with its screw
    ([thread](https://forum.prusa3d.com/forum/prusa-indx-how-do-i-print-this-printing-help/nozzle-cleaning-strange-results/)).
    The reply was unsure which way to turn it, and the direction it guessed does not
    obviously match the wizard's; go by the wizard and watch the block move. The owner has
    not reported back,
    and whether every setup path runs the wizard is not established.

    One later owner, firmware not stated, reports trouble from too little contact.
    Primed material was clinging to the back of their nozzle and dropping onto the
    bed mid-print; after they adjusted the wiper height until it definitely touched the
    nozzle, the priming at least went well, and each recalibration of the wiper left
    them with a different purge. Their wiper had not been reliably touching, which is
    not the same as one set to just touching, so this is a single report that more
    contact helps. It says nothing about whether the automatic routine stops short.

    A further owner, writing in mid-October on firmware they do not state but before
    they moved to 7.0.0, says their early stringing and blobs eased a great deal once they
    set the height so that the nozzle presses well down into the pad
    ([thread](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/indx-review/)).
    They also gave the earlier reply above about raising the pad, so this is not an
    independent second voice for it. A week later the same owner wrote that they had
    reset the pad well upward, as high as it would go, so that silicone surrounds the
    nozzle, and that a six-color PLA print in undried filament of several brands, on the
    generic profile, then came out with next to no stringing
    ([thread](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/maybe-im-becoming-a-convert/)).
    They are not sure the pad was the whole story, say the setting is judged by eye with
    no scale to read, and ask why the loadcell does not set it. That thread names no
    firmware; in the earlier thread they had said on 16 October that they had just
    installed 7.0.0. `provisional` — one owner across two threads, directional only,
    and like the last one it does not show whether the automatic routine stops short.

    Other owners have since pointed the same way, in a separate thread. In late October an
    INDX owner on 8.0.0, printing new PLA, found blobs on the outer surface at every layer
    with a tool change, and saw the cleaner now and then pick up a blob and leave it on or
    beside the part, although they had already run the wiper calibration
    ([thread](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/core-one-indx-blobs-at-color-change-layers-nozzle-wiper-dropping-filament-onto-print/)).
    Of the owners who replied, one only asked how to add purge lines; the other three
    point at the cleaner's height or pressure: raise the cleaner a little, because in
    one's experience its position is very sensitive; make sure the wiper presses on the
    nozzle hard enough to wipe it clean; and raise the cleaner, which together with a
    cooling change in the slicer gives the third reliable prints. The original poster has
    not reported back. So the advice to give the wiper more contact with the nozzle is now
    `reported`, from several owners across threads, but as advice: none of it is a
    before-and-after test, and none of it compares the wizard's touch criterion with a
    deeper setting on one machine.

    A newcomer on what they believe is 8.0.0, posting in November in the main thread,
    noticed notches for X and Y at the front of the waste bin and, for the calibration,
    lined the nozzle up on the X one rather than at the spot their photos label as Prusa's
    ([thread](https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/nozzle-cleaning-calibration-issues/)).
    Almost all of their cleaning trouble, purge carried onto prints included, went away,
    they write, ending the claim with a question mark; their photos show the purge
    changing. Which step of the wizard they mean is not stated. `provisional` — a single
    report.

### Workarounds that do not involve calibration

- **Print a skirt or brim.** Several owners report this catching the initial debris
  before it reaches the part. It is the cheapest mitigation and it worked for the
  owner who started the main thread. One notes brims can be awkward to remove from
  the sheet.
- **Use a wipe tower instead of the purge bin.** The tool-change G-code branches on
  whether a wipe tower is in use, so a wipe tower bypasses the purge-station sequence
  entirely. An owner reprinted a blob-spoiled ABS job with a minimal wipe tower and
  reported it came out very clean, for a small increase in print time.

    The trade-off is material-dependent, and worth getting right: a wipe tower is
    good for multiple colors of the **same** material, where the aim is only to
    stabilize flow. For **dissimilar** materials that do not bond to each other, the
    purge bin has the clear advantage, because a tower built from materials that will
    not stick together falls apart.

    TODO(verify): the reduced purge volume used for the minimal wipe tower, and the
    default it was reduced from. These are slicer settings and are withheld.

- **Add periodic wipes** for single-nozzle prints and sticky filaments.

### Residue left by the clean before calibration

Tool offset calibration runs as a print begins, and before it measures a tool it
cleans that tool's nozzle. In the firmware source the clean purges hot, cools with the
part fan on, then gives the nozzle its full wipe, in that order from 6.9.0 through 8.0.0
(see *Verification*). Whatever survives
that wipe is still on the nozzle when it is measured.

On a 6.9.1 build, one owner found PLA drawn out into long strings and left clinging
to the nozzle, after which nozzle probing failed; going back to 6.9.0 seemed better,
though they suspected their own wiper setting or a load cell fault. A second owner,
on the beta, found PETG left on the nozzle after the wipe, enough to fail bed
leveling, while crediting the beta with fixing most of their PETG calibration
trouble. Both are single reports.

An upstream report against the beta, also with PETG, blames the order of that clean
([#5505](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5505)): the nozzle is
cooled after its purge and before its main wipe, so the purge has time to firm up
and is not fully cleared, and calibration then fails on what is left. The reporter
asks for the wipe to come before the cool-down. The firmware source does run that
sequence, and the order is the same in 6.9.0 and at the v8.0.0 tag. What the beta
changed is how far the nozzle cools before that wipe: its notes lower the tool offset calibration temperature,
and the source applies that to this cool-down; stable 6.9.1 keeps it.

Whether that left more residue, or made the same residue matter more, is not settled.
One INDX owner now says both; theirs is a single report, filed in October against 6.9.2
and 7.0.0 ([#5567](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5567)). With
PETG and the stock start G-code, they found PETG left on the nozzle ahead of probing
now and then on 6.9.0 but often on 6.9.2 and 7.0.0, and on 7.0.0 photographed a large
lump of hardened PETG on the tip and side of the nozzle right after the cleaning
routine. Going back to 6.9.0 cut the problem a good deal without ending it. Their
explanation is that at the lower calibration temperature any leftover PETG is fully
solid, so it throws the measurement off further, and the Z offset comes out too high.
That is one owner's comparison on one machine, not a controlled test, and the
explanation is theirs.

A different owner, commenting on a separate issue
([#5500](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5500)), objects to
the same order as #5505: the nozzle should not sit in its purge while it cools, but be
cleaned as it cools, because by the time the wipe comes the material has set on the tip.
So the complaint about the order rests on two reports in two issues. It has not been
checked whether the #5505 reporter is independent of the PETG account above, and
whether wiping first would help is untested.

Others come at it from the temperature side. In October a forum owner observed that the
automatic clean runs far below printing temperature, too cool in their view to soften
PETG enough to wipe it off, and suggested running it at the temperature of the loaded
material instead
([thread](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/cleaning-nozzle-2/)).
The same owner then filed that suggestion upstream as an enhancement request
([#5568](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5568)), so the thread and
the request are one voice, not two. Neither the thread nor the request says which
firmware the owner is running. In the request they describe what they see the printer
do: heat to printing temperature, purge, move off, cool, then brush the nozzle in
several directions, which matches the source reading. They say that with sticky
materials such as PETG and PCTG, bits stay on the tip and come loose onto the print once
the nozzle is back at printing temperature, as lumps. They ask for a cleaning temperature
that follows the loaded material, or failing that a menu setting, and they add in the
thread that PETG did not always come off even at the warmer temperature earlier firmware
cleaned at. The #5567 reporter, separately, lists cleaning hotter as one possible fix,
beside cleaning the nozzle before the calibration and a calibration temperature that
follows the filament. One commenter on #5568 disagrees: the material should be soft, not
runny, and the lower temperature is closer to what they would choose.

Three later commenters on #5568 side with the request. One, an INDX owner who has filed
related requests of their own, finds PETG close to solid at the cleaning temperature and
would keep it below printing temperature only by enough to stop ooze. Another, whose
prints start with PETG, finds the nozzle badly cleaned before every print but clean after
the printer's filament-change routine, which by their account runs hotter; that compares
two different routines, not one clean at two temperatures. A third finds PLA cleans well
but PCTG does not: unless a lump is picked off the nozzle by hand before each print
begins, the Z offset check fails, on a fresh nozzle as well. The last two name neither machine nor
firmware, though the request is for the INDX.

So the residue itself is `reported`, and now by several owners: the reporters of #5567
and #5568 and two of these commenters find that the cool clean leaves sticky PETG or PCTG
behind, and the two complaints about the order describe the same thing. The causes they
offer are not established. That a hotter clean would cure it has not been tested on the
clean itself; one owner's comparison with the filament-change routine points that way,
and one commenter argues against it. Nothing in the firmware has moved: at the v8.0.0 tag
the clean still cools to the same capped temperature, in the same order, as at v6.9.2.

A forum thread whose title blames a nozzle too cold during cleaning is about a different
clean, and weighs less on #5568 than its title suggests. An INDX owner on 8.0.0 found
TPU tangling at the extruder whenever the print switched back to that tool after the
first layer, with almost nothing coming out in the purge
([thread](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/solved-tpu-tangling-at-the-extruder-after-indx-tool-changes-the-nozzle-was-too-cold-during-cleaning/)).
They traced it to the profile's own tool-change block, not to the firmware:
before the cleaner step that block brings the nozzle down to a lower eject temperature
(see *Tool change* on the [annotated profile G-code](../gcode/indx-profile-gcode.md)), and
the push that locks the filament in the incoming tool runs at that temperature, so soft
TPU buckled against plastic that had not yet melted. Raising that temperature for
flexible filament only, and adding a pause once the nozzle is back at printing
temperature, so the filament soaks before it is pushed back in, cured it, they report,
though they changed several other flexible-only settings at the same time
and did not try each on its own. It does not corroborate #5568: that request concerns
the clean inside tool offset calibration, which the firmware controls, while this one
sits in the profile where an owner can edit it, and the failure is filament buckling, not
residue left on the tip. What the two share is a clean that runs well below printing
temperature. `provisional` — one owner, several changes at once.

TODO(verify): the calibration and cleaning temperatures before and after 6.9.1, the
hotter cleaning temperatures proposed in #5567, #5568 and the forum thread, and the raised
eject temperature and the length of the pause the TPU owner used. None of them is
published here.

The #5567 reporter also points out that Prusa's start G-code runs the tool offset
calibration ahead of the print's own nozzle clean, and suggests cleaning first. The
start G-code this site reproduces has that order: `G427` comes ahead of bed leveling
and of the `G12` cleaning-station lines that prime the first tool (see
[annotated profile G-code](../gcode/indx-profile-gcode.md)). The calibration's own
per-tool clean, described above, still runs inside `G427`; the request is for a further
clean ahead of it.

An older request comes at it from the other end of the print
([#5410](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5410)): an INDX owner
asks for every tool to be heated and wiped once a print has finished, because PETG
nozzles get parked with residue around them. A second owner seconded it in August, and
in late October the INDX commenter on #5568 above suggested doing it while the bed
lowers at the end. That commenter has also asked for a way to clean a nozzle by hand
during a print ([#5576](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5576)):
a pause leaves the tools docked, cold and out of reach, so they want it to offer to pick
a tool, heat it and wait. Both requests are open, unanswered and untested.

The reporter of #5500 adds that 6.9.0 and 6.9.1 both purge more than they need to,
often leaving material on the nozzle after the wipe, and that the firmware takes no
notice of the slicer's purge volume. Two later commenters there say they have the same
issue, one on a four-tool Gen 2 and one who finds ASA sticks worse still, without saying
which of its complaints they mean. Owners in a forum thread from late October, who do
not cite the issue, describe much the same thing. One finds that a tool's first purge of
the print is large and partly stays on the nozzle, because the wiper cannot clear it, and
then lands on the first layer, so they print a short line with each tool first to catch
it; another agrees that the first purge spreads material all around the nozzle where it
cannot be cleaned reliably, and wonders why it is so large
([thread](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/core-one-indx-blobs-at-color-change-layers-nozzle-wiper-dropping-filament-onto-print/)).
Neither says whether they mean the purge inside the calibration or the one at a tool's
first change. The source settles part of it for the calibration: there the purge is the
firmware's own sequence, the same at the v6.9.2 and v8.0.0 tags, with a built-in amount
that no slicer setting feeds into (the firmware does let a macro file on the USB drive
replace the sequence; see *Verification*), whereas a tool change's purge is
worked out in the profile's tool-change G-code. Whether either amount is more than needed
is a judgment the source cannot make. So the complaint that an early purge leaves
material on the nozzle is `reported`, from owners in two separate sources; that the purge
is too large is their view. For probing failures in general, see
[oozing during probing and calibration](oozing-during-probing-and-calibration.md).

### Before you blame the wiper

- **Rule out oozing and probing faults first.** If material is accumulating during
  probing rather than at tool changes, see
  [oozing during probing and calibration](oozing-during-probing-and-calibration.md).
- **Check the silicone block is firmly mounted.** If it shifts slightly during
  cleaning, no amount of calibration will stay consistent.
- **If results are inconsistent between tools**, suspect tool offsets rather than the
  wiper — tools that come to rest at marginally different points with respect to the
  block produce exactly that symptom. See
  [tool offset calibration](offset-sensor-board-failure.md).
- **Dry the filament.** The INDX is reported to be more moisture-sensitive than the
  Nextruder it replaces.
- **A lone blob where a print resumed** has a different cause. One owner on 6.6.3
  traced blobs after a spool join to the nozzle oozing while the bed traveled back
  to printing height, and reported it upstream
  ([#5391](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5391)). The report was
  closed automatically for inactivity in late September 2026, with no reply from Prusa
  on it, so its closure says nothing about a fix. The same owner raised the same problem
  for an ordinary pause and resume, also on 6.6.3, asking for the purge and wipe to come
  after the bed is back in place
  ([#5412](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5412)). 6.9.0 now
  reheats the nozzle in the cleaner on resume. A second owner, filing after 6.9.0 was out
  ([#5477](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5477)), describes a
  resume that picks the tool and primes it over the silicone first and raises the bed
  only afterwards, so the primed nozzle oozes during that wait and the blob ends up on
  the part. They give no firmware version, so whether the 6.9.0 reheat helps is still
  not established. They ask for the bed to go up before the tool is picked and primed,
  and two more owners have added that they get blobs after a pause as well. In early
  October #5412 was flagged as stale, the same automatic step that preceded the closure
  of #5391; one of those two owners replied that it still affects them, and the flag was
  lifted. Both requests remain open with no reply from Prusa, and neither the 7.0.0 nor
  the 8.0.0 notes list a change to that sequence: the nearest 7.0.0 items fix an extra
  blob when resuming after a power failure, tagged as already in 6.9.0, resuming with a
  cold tool after a filament change on another tool, and a Z shift after a Spool Join on
  an instant runout. None of them changes the order of bed travel, pick and prime
  that #5412 and #5477 ask about. One flow keeps the requested order from 7.0.0: when the
  printer stops mid-print to empty the waste bin, it raises the bed over the bin, waits
  for the bed to get there, and only then reheats the nozzle and primes it over the
  cleaner before it travels back to the print. The fuller 7.0.0 notes on GitHub describe
  that stop, with dedicated screens, and the
  [source](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/src/feature/wastebin_watcher/wastebin_watcher.cpp)
  bears it out. At the
  [v6.9.2 tag](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.2/src/feature/wastebin_watcher/wastebin_watcher.cpp)
  the same stop already reheated over the bin, but it began the reheat while the bed was
  still rising and did not prime the nozzle at all. That covers only the stop to empty the bin;
  this page has not re-checked the order of an ordinary resume against the now-public
  source.
  No workaround is
  confirmed: one commenter suggested a small wipe tower for jobs with a pause, but had
  not tried it. `reported` —
  two owners, in separate issues, trace the blob to ooze while the bed travels.

### Temperatures, retraction and flow

Community consensus is that several stock profile values are not well suited to this
toolhead's high-flow nozzle geometry, which transfers heat more efficiently than what
many owners are coming from — so the general direction is cooler rather than hotter,
with retraction figures that are strongly machine-specific.

**No values appear on this page.** Every temperature, retraction distance, extrusion
multiplier and pressure-advance figure discussed in the sources is withheld pending
verification on hardware.

TODO(verify): stock versus community-preferred temperature ranges per material;
retraction ranges and the profile defaults they depart from; the reduced extrusion
multiplier reported for at least one filled material; and the per-nozzle-diameter
pressure advance table that circulates as a start-G-code snippet. These are exactly
the numbers that damage a stranger's printer when wrong, and they are the reason this
section is deliberately empty.

## Verification

`reported` — multiple independent owners, across two dedicated threads, over roughly
two months of firmware changes, with the firmware behavior itself confirmed first-party.

The 6.9.0 changes are documented in
[Prusa's own release notes](https://help.prusa3d.com/downloads/core-one-indx), which
name the automatic nozzle cleaner calibration, the shift in purge point, and the nozzle
reheat on resume. That upgrades the headline claim on this page from owner inference to
vendor-documented fact.

The primary source is
[Nozzle cleaning/calibration issues](https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/nozzle-cleaning-calibration-issues/),
an 88-post thread with seventeen participants, running from late July to mid-September
2026 with one further post in November. It contains the symptom reports, the visibility
complaints, the Tune-menu adjustments, the wipe-tower experiment, the 6.9.0 outcome, the
later single reports on wiper height and on 6.9.1, and the November report on aligning
the calibration on 8.0.0. Much of its later traffic is about tool offset
calibration, which belongs to [its own page](offset-sensor-board-failure.md).

The 6.9.1 re-check: the
[stable notes](https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.9.1)
list a gantry squaring wizard and a homing fix, and neither touches the cleaner. The bed dropping during Nozzle Cleaner calibration comes from the
[beta notes](https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.9.1-beta)
only. Nothing on this page is contradicted by either. The
[6.9.2 release](https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.9.2)
adds the PVA and BVOH presets and nothing else that reaches an INDX; none of the source
files cited below differs between the v6.9.1 and v6.9.2 tags, so the reading that
follows holds for 6.9.2 as well.

The 7.0.0 re-check began on the
[notes alone](https://help.prusa3d.com/downloads/core-one-indx) and now rests on the
source too: Prusa published the
[7.0.0 tag](https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v7.0.0), with
fuller notes, on 3 November. Of the two cleaner items described in the tip, the Nozzle
Wiper one does not reach the INDX. The firmware's
[build options](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/ProjectOptions.cmake)
give the INDX its own nozzle cleaner and the lighter wiper only to printers without an
INDX, and Nozzle Wiper is that lighter wiper's
[menu name](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/src/gui/MItem_hardware.hpp).
The other item is in the
[parking code](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/src/common/mapi/parking.cpp),
which from 7.0.0 applies the calibrated cleaner offset to the load and unload positions
over the waste bin. Neither the notes nor the source change wiper height or the order of
purge, cool-down and wipe. The notes name no change to the order of bed travel and
priming on an ordinary resume that #5412 and #5477 ask for; this page has not re-checked
that order in the source, and the waste-bin flow described under *Before you blame the
wiper* is the one place found that raises the bed first, and only from 7.0.0. One INDX
owner has since reported PETG left on the nozzle after the wipe on 7.0.0
([#5567](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5567)).

Firmware 7.0.1, published on 19 October 2026 on the same downloads page, lists a single
fix, for a hang at startup, and touches nothing on this page; its
[tag](https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v7.0.1) changes none
of the files read here.

The 8.0.0 re-check, too, began on the
[notes alone](https://help.prusa3d.com/downloads/core-one-indx) and now has the
[8.0.0 tag](https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v8.0.0) behind
it. Of its three lines near the cleaner, described in the tip, the lower bed comes from a
[commit](https://github.com/prusa3d/Prusa-Firmware-Buddy/commit/596d5330f3a5afde6b6eaefa6f60e9cb12882074)
that has the wizard ask the shared calibration preamble for a hand-access height, and
the more accurate calibration from the precise homing described there. None of the three
changes wiper height, the cleaning temperature, the order of purge, cool-down and wipe,
or the resume order.

What the automatic calibration does and does not cover, and the order of purge,
cool-down and wipe in the per-tool clean that runs as a print begins, are read from the
firmware source at the v6.9.1 tag: the
[calibration routine](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/src/feature/indx_nozzle_cleaner_calibration/indx_nozzle_cleaner_calibration.cpp),
its [screens](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/src/feature/indx_nozzle_cleaner_calibration/screen_nozzle_cleaner_calibration.cpp),
the [tool offset calibration](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/src/feature/tool_offset_calibration/tool_offset_calibration.cpp)
that runs the clean, and the [cleaner's sequences](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/src/feature/nozzle_cleaner/nozzle_cleaner.cpp).
The wizard's own steps, the screw step among them, and the cleaner's wipe and purge
moves are unchanged from the 6.9.0 tag. They are unchanged at the v8.0.0 tag as well
([compare](https://github.com/prusa3d/Prusa-Firmware-Buddy/compare/v6.9.2...v8.0.0)):
the INDX's
[cleaner sequences](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/src/feature/nozzle_cleaner/nozzle_cleaner.cpp)
differ from v6.9.2 only in a block for another printer, the
[screw step](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/src/feature/indx_nozzle_cleaner_calibration/screen_nozzle_cleaner_calibration.cpp)
reads as before, and the per-tool clean in the
[tool offset calibration](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/src/feature/tool_offset_calibration/tool_offset_calibration.cpp)
takes the same steps at the same temperatures. The purge inside that clean is a built-in
amount in the firmware's purge sequence, and no slicer setting reaches it. It is a
default rather than a fixed value: the firmware's
[G-code loader](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v8.0.0/src/common/gcode/gcode_loader.cpp)
first looks for a file named `purge_clean.gcode` in a `macros/nozzle_cleaner` folder on
the USB drive and runs that instead, as it does for each of the cleaner's sequences, and
falls back to the built-in one only when no such file is there. That path is the same at
the v6.9.2 tag; it is read from the source, not tried on a printer. The lower bed during the wizard that the beta
notes mention comes from a
[calibration preamble](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/src/common/mapi/calibration_preamble.cpp)
the wizard shares with other calibrations, not from the wizard itself. The tool offset
calibration did change: the beta lowered the temperature the per-tool clean cools to
before its main wipe, which is one of the two calibration temperatures its notes lower;
the other is for the XY scan. The source shows what the firmware does, not how well the
result works on any one machine.

The 6.9.0 improvement is **independently confirmed** by three owners: one reports clean
tool changes on a mixed TPU/PETG print and again on a four-color PETG print; a second
separately reports the result is much cleaner and that they no longer need a brim to
catch debris; and the owner who started the thread — the person with the worst of the
problem — has since confirmed that 6.9.0 has mostly resolved the oozing and cleaning
for them. The last of those is the strongest single data point on this page, because it
is the original complainant closing their own report. That is the strongest claim on this page.
It carries one qualification, set out in the tip at the top: weeks later, after a failed
print, the same owner hit tool calibration failures on 6.9.0 that were new to them, and
saw the oozing return once they had reset the machine and recalibrated every tool.

The "bury the nozzle" finding comes from
[Nozzle wiper vs. INDX offset sensor](https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/nozzle-wiper-vs-indx-offset-sensor/),
where an owner states the hypothesis, tests it, and reports the confirmed result in
the same thread — hypothesis and outcome from the same person, which is weaker than
two independent reports but stronger than an unbacked assertion. The
[common problems summary](https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/a-summary-of-common-indx-problems/)
records a separate systematic height test reaching the same conclusion.

Where the sources disagree: whether the change in pellet shape was a regression or an
intentional improvement, as noted in the body. The sources are directly in tension and
neither is confirmed.

Explicitly **not** carried onto this page: a claim in the thread that the wipe-tower
minimum purge setting also governs purge-bin volume despite its name. The owner who
posted it said plainly that they had traced it with an AI assistant rather than
reading the firmware, and told readers to take it with a pinch of salt. It is recorded
here as a lead for someone to verify, not as guidance.

Also not carried over: a dynamic overhang-fan profile issue described in the
community knowledge base. It appears in no other thread in the forum corpus, and it is
a cooling problem rather than a wiper one — it belongs on its own page, at
`provisional`, if someone can corroborate it.

Nor is an upstream report that the firmware's wipe path consistently lands off-center
in Y on the silicone pad
([#5496](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5496)). It reads like
the Nozzle Cleaner Y Offset question above, but it was filed against a non-INDX
Core One+ (Gen 2) with its own wiper accessory, on the non-INDX 6.8.1 firmware. A
second owner has since confirmed it, again on a non-INDX Gen 2. Prusa developers took
it up in October: the first to reply says that on that machine the wipe runs at a
position set by hand in the firmware, and another asked the owners to check the
printer's belt-type setting. After updating to 7.0.0 the reporter still found the wipe
off-center. No INDX owner has reported the same there. The INDX, by contrast, measures
where its cleaner sits (see the source reading above); that contrast is this page's
reason, not the developers', for not carrying the report over. The report is not
evidence of a systematic Y error on the INDX, and the per-machine reading of the Y
offset stands.

Also not carried over is a later Gen 2 report in which the wipe runs in the air, well
above the wiper ([#5563](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5563)),
because it comes from machines that have no INDX or do not say they have one, and no
INDX owner has reported it. Its reporter says the machine has no INDX. Five owners have
since added that they see it too, all on 8.0.0 and on a Gen 2, one of them since updating
from 6.8.1: one names Prusa's wiper accessory and an MMU3, the others do not mention an
INDX. In November the owner of a non-INDX Core One described the same wipe above the
wiper in a comment on #5567. In the source, those machines' wiper is the Nozzle Wiper
accessory, whose code 7.0.0 reworked and which is not built for the INDX (see the 7.0.0
re-check above); whether that rework lies behind these reports is not established.
One of the owners later found that keeping the hotend from heating while the printer
homes made the wipe land on the wiper again, a tip taken from a forum thread about a
non-INDX Core One that keeps detecting collisions, where owners suspect the loadcell or
its wiring. A second owner says the same change cured it for them. That would fit a
false loadcell trigger while the heater warms up, the pattern described under
[loadcell noise](loadcell-emi-noise.md), more than a misplaced wiper, but nobody in the
issue has tested that, and it still comes from Gen 2 machines without an INDX.

## Related

- [Oozing spoils bed probing and tool calibration](oozing-during-probing-and-calibration.md)
  — material in the wrong place, but during probing rather than tool changes
- [Tool offset calibration fails](offset-sensor-board-failure.md) — the cause to
  suspect when wiper results differ between tools
- [Phantom tools and park failures](tool-detection-ringdown-decay.md) — the other
  area 6.9.0 changed, in that case possibly for the worse
- [Diagonal banding across print walls](diagonal-banding.md) — the other print-quality
  page. If your defect is a regular pattern on the walls rather than discrete blobs
  landing on the part, it is the extruder, not the wiper.
- [Toolhead collides with finished parts](complete-individual-objects-collision.md) —
  also damage caused around a tool change, but mechanical rather than material. If parts
  are being knocked or gouged rather than dirtied, read that instead.
