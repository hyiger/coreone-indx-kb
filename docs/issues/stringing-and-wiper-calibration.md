---
title:        Blobs dragged into the print — nozzle wiper and purge
confidence:   reported
updated:      2026-08-24
author:       hyiger
printer:      Core One
toolhead:     INDX
hotend:       unknown
nozzle:       0.4mm reported
firmware:     6.9.0; earlier behaviour noted throughout
sources:
  - https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/nozzle-cleaning-calibration-issues/
  - https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/nozzle-wiper-vs-indx-offset-sensor/
  - https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/a-summary-of-common-indx-problems/
superseded_by:
---

# Blobs dragged into the print — nozzle wiper and purge

!!! tip "Update to 6.9.0 before doing anything else"
    Firmware 6.9.0 introduced **automatic loadcell-driven alignment of the wiper in
    both horizontal axes**, along with a changed purge location, a revised wiping
    path and different purge amounts. Two owners independently report the difference as
    dramatic — clean tool changes across mixed-material prints, and one no longer
    needing a brim to catch debris on the first layer.

    Most of the manual procedure below exists because that calibration used to be
    done by hand, badly, with no way to see what you were doing. If you are on 6.9.0
    or later, update and re-test before investing any time in manual alignment.

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
between rice grains and worms. It is a small fraction of a millimetre and it is
machine-specific, so it is withheld here rather than published as a target.

!!! note "Which pellet shape is actually better is disputed"
    The community knowledge base recorded the 6.6.2-era shift from compact pellets to
    stringy tails as a regression. An owner in the forum thread later argued the
    opposite — that worms may have been deliberate, because a worm keeps the nozzle
    from nestling into the top of a blob, detaches more readily, and does less damage
    if it does reach the print. Both readings are in the sources. Treat pellet shape
    as a *sensitive indicator that your alignment changed*, which it certainly is,
    rather than as a target to optimise toward.

### The real difficulty is that you cannot see it

Owners are unanimous that the hard part is visibility, not judgement. The wiper sits
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
    good for multiple colours of the **same** material, where the aim is only to
    stabilise flow. For **dissimilar** materials that do not bond to each other, the
    purge bin has the clear advantage, because a tower built from materials that will
    not stick together falls apart.

    TODO(verify): the reduced purge volume used for the minimal wipe tower, and the
    default it was reduced from. These are slicer settings and are withheld.

- **Add periodic wipes** for single-nozzle prints and sticky filaments.

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
a month of firmware changes.

The primary source is
[Nozzle cleaning/calibration issues](https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/nozzle-cleaning-calibration-issues/),
a 58-post thread with nine participants running from late July to late August 2026. It
contains the symptom reports, the visibility complaints, the Tune-menu adjustments,
the wipe-tower experiment, and the 6.9.0 outcome.

The 6.9.0 improvement is **independently confirmed**: one owner reports clean tool
changes on a mixed TPU/PETG print and again on a four-colour PETG print, and a second
owner separately reports the result is much cleaner and that they no longer need a
brim to catch debris. That is the strongest claim on this page.

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
