---
title:        Blobs dragged into the print — nozzle wiper and purge
confidence:   reported
updated:      2026-09-25
author:       hyiger
printer:      Core One
toolhead:     INDX
hotend:       unknown
nozzle:       0.4mm reported
firmware:     6.9.0, re-checked against 6.9.1; earlier behavior noted throughout
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
superseded_by:
---

# Blobs dragged into the print — nozzle wiper and purge

!!! tip "Update to 6.9.0 or later before doing anything else"
    Firmware 6.9.0 introduced **automatic calibration of the nozzle cleaner** — this
    is confirmed in Prusa's own release notes, not just inferred from owner reports.
    The same release moved the purge point in Y and made the nozzle reheat in the
    cleaner when a print resumes. Owners additionally describe a revised wiping path
    and changed purge amounts.

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

    The stable 6.9.1 notes name no change to the wiper or the purge. The beta did one
    thing for the cleaner: where appropriate, the bed now moves down during Nozzle
    Cleaner calibration, leaving room for a hand or a wrench. The stable notes do not
    repeat it, but the stable is built on the beta: in the firmware repository it adds
    [15 commits](https://github.com/prusa3d/Prusa-Firmware-Buddy/compare/v6.9.1-beta...v6.9.1)
    to the beta tag, none of them about the nozzle cleaner. That comes from the release
    history, not from the notes.
    On a 6.9.1 build, one owner found PLA drawn out into long strings and left clinging
    to the nozzle, after which nozzle probing failed; going back to 6.9.0 seemed better,
    though they suspected their own wiper setting or a load cell fault. A second owner,
    on the beta, found PETG left on the nozzle after the wipe, enough to fail bed
    leveling, while crediting the beta with fixing most of their PETG calibration
    trouble. Both are single reports. For probing failures in general, see
    [oozing during probing and calibration](oozing-during-probing-and-calibration.md).

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

    One later owner, firmware not stated, reports trouble from too little contact.
    Primed material was clinging to the back of their nozzle and dropping onto the
    bed mid-print; after they adjusted the wiper height until it definitely touched the
    nozzle, the priming at least went well, and each recalibration of the wiper left
    them with a different purge. Their wiper had not been reliably touching, which is
    not the same as one set to just touching, so this is a single report that more
    contact helps. It says nothing about whether the automatic routine stops short.

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
  ([#5391](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5391)). 6.9.0 now
  reheats the nozzle in the cleaner on resume, which may bear on it; nobody has said
  whether it does. Single report, `provisional`.

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
an 87-post thread with sixteen participants running from late July to mid-September
2026. It contains the symptom reports, the visibility complaints, the Tune-menu
adjustments, the wipe-tower experiment, the 6.9.0 outcome, and the later single reports
on wiper height and on 6.9.1. Much of its later traffic is about tool offset
calibration, which belongs to [its own page](offset-sensor-board-failure.md).

The 6.9.1 re-check: the
[stable notes](https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.9.1)
list a gantry squaring wizard, PVA and BVOH presets and a homing fix, none of which
touches the cleaner. The bed dropping during Nozzle Cleaner calibration comes from the
[beta notes](https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.9.1-beta)
only. Nothing on this page is contradicted by either.

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
Core One+ (Gen 2) with its own wiper accessory, on the non-INDX 6.8.1 firmware. It is
not evidence of a systematic Y error on the INDX, and the per-machine reading of the
Y offset stands.

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
