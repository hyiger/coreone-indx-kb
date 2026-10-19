---
title:        Probing fails or nozzle never touches the bed — loadcell noise
confidence:   reported
updated:      2026-10-18
author:       hyiger
printer:      Core One
toolhead:     INDX
hotend:       unknown
nozzle:       unknown
firmware:     unknown
sources:
  - https://help.prusa3d.com/article/loadcell-measure-failed-31526-core-one-35526-core-one-l-36526-core-one-indx-26526-mk4s-13526-mk4-27526-mk3-9s-21526-mk3-9-36526-core-one-indx_405741
  - https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/nozzle-not-touching-bed-during-probing/
  - https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/a-summary-of-common-indx-problems/
  - https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/tool-offset-calibration-failing/
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5468
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.9.1-beta
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.9.1
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/compare/v6.9.1-beta...v6.9.1
  - https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/bed-leveling-issues-3/
  - https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/loadcell-noise-and-mesh-bed-levelling/
  - https://forum.prusa3d.com/forum/ceske-forum-obecna-diskuze-oznameni-a-novinky/core-one-indx-tool-offset-out-of-bounds-36130-loadcell-test-issue/
  - https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/loadcell-test-tool-crash-on-calibration/
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5518
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/lib/Marlin/Marlin/src/module/probe.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/src/common/selftest/selftest_loadcell_indx.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.0/src/common/selftest/selftest_loadcell_indx.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/lib/Marlin/Marlin/src/module/prusa/toolchanger_indx.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5520
  - https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/homing-shows-early-endstop-detected-message/
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/lib/Marlin/Marlin/src/module/prusa/homing_corexy.cpp
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.9.2
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/compare/v6.9.1...v6.9.2
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5548
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5526
  - https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/gantry-squaring-failing/
  - https://help.prusa3d.com/downloads/core-one-indx
superseded_by:
---

# Probing fails or nozzle never touches the bed — loadcell noise

## Summary

If bed probing behaves as though the nozzle has already touched down while it is
still obviously well clear of the sheet, the likely cause is electrical
interference in the loadcell signal rather than anything mechanical. The vendor has
acknowledged interference from the heater as the working theory. The community fix,
which vendor support now also recommends, is a clamp-on ferrite core on the main
toolhead cable close to where it enters the controller board. Several owners report
this resolving the fault outright. Owners have since named further sources, the bed
heater wiring and the LED status strip among them; those are covered below and are
less well supported. A loadcell self-test that reports noise straight after a
toolchange (possibly also one the test makes itself) may be a different matter: noise
from the extruder motor, which one issue traced to the motor being left switched on
after a toolchange and a second measured on 7.0.0. See below before buying hardware
for that.

## Error codes that lead here

| Code | What the printer shows |
|---|---|
| [`36526`](https://help.prusa3d.com/article/loadcell-measure-failed-31526-core-one-35526-core-one-l-36526-core-one-indx-26526-mk4s-13526-mk4-27526-mk3-9s-21526-mk3-9-36526-core-one-indx_405741) | Loadcell measure failed |
| [`36527`](https://help.prusa3d.com/article/loadcell-bad-configuration-31527-core-one-35527-core-one-l-36527-core-one-indx-26527-mk4s-13527-mk4-27527-mk3-9s-21527-mk3-9_405749) | Loadcell bad configuration |
| [`36528`](https://help.prusa3d.com/article/loadcell-timeout-31528-core-one-35528-core-one-l-26528-mk4s-36528-core-one-indx-13528-mk4-27528-mk3-9s-21528-mk3-9_405757) | Loadcell timeout |

All three are loadcell faults. Interference tends to show as a failed
measurement or a timeout rather than a configuration error.

## Detail

The INDX senses bed contact through a loadcell, and the signal from it shares a
cable loom with the power that drives the heater. In that loom the power pair is
twisted, which cancels most of its radiated noise, but the loadcell's signal pair is
not — so it is comparatively exposed to whatever the heater is doing. When that
noise is large enough, the firmware reads it as a contact event.

The tell-tale is *how wrong* the behavior is. A mechanical or offset problem makes
the nozzle probe slightly too high or too low. Noise-driven false contact makes it
stop while the nozzle is plainly nowhere near the sheet — a gap you can see across
the room, not one you would measure with paper. If you are watching a probing pass
and thinking "it hasn't even got close", this page is probably your fault.

Symptoms reported in this family:

- Probing completes with the nozzle visibly clear of the sheet
- Loadcell self-test failures
- Z homing or probing that fails **only once the hotend is hot** — a strong hint,
  because it points at the heater as the noise source
- False Z-collision errors
- Tool offset calibration that fails as a print starts but passes when run on
  its own from the menu. Owners describe both the heaters and the LED status strip as
  off during the menu run, so this pattern fits more than one source; see the section
  on other sources below
- Repeated bed-leveling retries, and unusually long mesh times
- A first layer that does not stick, or that drags filament up into a blob, because
  the machine believes the bed is higher than it is

### A noisy self-test is not always interference

In one report
([#5468](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5468)), the loadcell
test in the first calibration after a C1 was upgraded to a C1+ (Gen 2) with INDX, on
6.9.0, never sounded its beeps and rejected the press, reporting either a premature
press or a noisy signal; once the owner aborted the wizard and started it again, it
passed straight away. The owner suspected that silent mode, set on the pre-INDX
firmware, had carried over. Prusa replied that, as far as it knew, the conversion
factory-resets the printer, and that it could not reproduce the fault. A second owner,
also on a Gen 2 upgrade, describes the same fail-then-pass-on-retry outcome in
[a forum thread](https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/bed-leveling-issues-3/):
the self-test kept flagging a noisy signal until they aborted it, homed the printer and
ran it again, and then it passed. Only that outcome is shared. The first report
concerned only the first run after the conversion, with the beeps missing; the second
owner's failure was not tied to a first run: it came both in the full calibration
sequence and when the test was started on its own from a cold machine, and they
describe a faint hum during the failing attempt.
Two reports in different places make the retry outcome `reported`, but neither
explains it. A retry costs nothing: if the self-test fails, abort and run it once more
before treating it as interference. The second owner also homed the printer before the
retry; that step comes from their report alone, `provisional`, though the report below
gives a reason it could matter.

A later report offers a firmware explanation that would fit both. In
[#5518](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5518), an owner with an
eight-tool Gen 2 upgrade on 6.9.1 found the self-test failing as noisy every time after
a toolchange and passing again after homing, with each of the four tools they tried.
They traced it to the extruder motor, which on the INDX also works the tool lock: a
toolchange leaves that motor switched on, and while it is on, the loadcell signal is
noisy enough to fail the test. Switching that motor on by itself, with no toolchange,
made the signal noisy; switching it off after a toolchange made it clean again without
homing. Homing clears it because homing Z is itself a probe of the bed, and probing
switches the extruder motor off first; homing only X and Y left the noise in place.
Moving cables, switching fans and heaters, and changing temperatures neither caused it
nor cleared it, which is what sets it apart from the heater interference on the rest of
this page.
Another owner, in the same issue, heard something from inside the head during the
failing test, found that aborting the test switched the motor off, and passed on the
retry. The firmware source fits the reporter's reading: in 6.9.1 the
[probing code](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/lib/Marlin/Marlin/src/module/probe.cpp)
switches the extruder motor off before probing, with a comment that this reduces noise
on the sensor; the
[INDX loadcell self-test](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/src/common/selftest/selftest_loadcell_indx.cpp)
does not; and the
[toolchange code](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/lib/Marlin/Marlin/src/module/prusa/toolchanger_indx.cpp)
puts back the motor's current and position after working the lock, but not whether it
was on.

That would account for the two earlier reports: an abort that switches the motor off, a
homing pass before the retry, and the faint hum the second owner heard. Neither of those
owners tested it, so the link is an inference. Neither says whether a tool had just been
changed, either. In 6.9.1, though, the self-test picks up a tool by itself when none is
held, and
[6.9.0](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.0/src/common/selftest/selftest_loadcell_indx.cpp),
which the first report was on, has the same step; that pickup would leave the motor on
in the same way. That too is a reading of the code, not a tested result.

A separate issue, [#5548](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5548),
reports the same effect on 7.0.0, from the owner of another eight-tool Gen 2 machine.
After an ordinary tool pickup their self-test often reports noise with nobody touching
the nozzle; retrying can leave it noisy for minutes, while aborting and starting a fresh
test can make it quiet. With the head standing still on a cold tool and no heater on,
they recorded the loadcell with the extruder motor commanded off, then on, then off
again: the noise was about three times as high while the motor was on.

Whether the same motor also upsets probing when a print starts is open. The probing
code switches the motor off first, yet owners in both issues have seen print-start
probing fail right after a tool pickup. The first reporter saw tool offset calibration
fail when a toolchange came before it, and got prints going by selecting the starting
tool and homing before printing. The owner who heard the head later had a replacement
head cable from Prusa support, which changed nothing; they now start prints by picking
up the first tool from the Control menu, running the loadcell test, aborting it once it
fails, and only then starting the print, so that no pickup comes just before homing. The
7.0.0 owner's prints stop on 36130 during the loadcell probe of the offset sensor; the
motor was off once nozzle cleaning had finished, but they could not record its state
during the failing probe. None of them has shown that the motor is the cause there, and the
first reporter says as much. The 7.0.0 owner replaced the nozzle-cleaning macro with
their own version on the USB stick, which switches the motor off before that probe, and
added start G-code lines that restore the driver afterwards; they report far fewer
failed starts, though not none. The macro writes the motor driver's configuration
directly, nobody else has checked it, and it is not reproduced here.

The effect on the self-test now rests on two separate issues, which makes it
`reported`. The code reading behind it is the first reporter's and this page's, not
Prusa's, and the link to print-start failures is `provisional`. Prusa had not answered
in either issue by the date above. 6.9.2 changes nothing that reaches an INDX beyond
filament presets, and the
[7.0.0 release notes](https://help.prusa3d.com/downloads/core-one-indx) list no change to
the loadcell self-test or to the extruder motor after a toolchange; the second issue
shows the effect on 7.0.0.
In practice: if the self-test reports noise after a toolchange, or when the test had to
pick up a tool first, home all axes, not only X and Y, or abort the test, and run it
again before suspecting interference or the loadcell.

Whether a noisy self-test means noisy probing is not settled. The second owner of the
two earlier reports and a third, in
[a separate thread](https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/loadcell-noise-and-mesh-bed-levelling/),
both linked the self-test's noise complaints to first-layer trouble and asked whether
one causes the other. The second owner has one area of the bed where the first layer
consistently fails to attach and suspects the loadcell, without a diagnosis. The third,
whose self-test often complains of noise, tried to check: they ran the same mesh bed
leveling twice in a row, changing nothing except cleaning the sheet between runs, and
read back the probed values. They found the two runs close at every point, judged that
within tolerance, and asked whether that meant the noise warnings were nothing to worry
about.
TODO(verify): the spread between the two runs, as given in the loadcell noise and mesh
bed leveling thread; no band separating a healthy repeat from a faulty one has been
established here. Each of these is a single report, `provisional`, and none of the
three owners fitted a ferrite, so they say nothing either way about the fix below. A
repeated mesh may still be a cheap check before buying hardware, but only if it is run
the way a print probes, with the hotend hot, because the working theory on this page
is interference from the heater. The thread does not say whether the nozzle was hot
during those runs. Two matching runs with a cold nozzle do not rule interference out. This is an
inference, not a tested rule. If the explanation in #5518 holds, there is a further
reason the two can disagree: probing switches the extruder motor off and the self-test
does not, so a self-test that fails for that reason does not by itself mean probing is
noisy, although the print-start reports above leave that open. Neither owner checked
whether that was their case.

### What to try

1. **Fit a clamp-on ferrite core to the main toolhead cable**, positioned near the
   controller board end. This is the fix with the most independent confirmation, and
   it is now what vendor support suggests. A plain clamp-on core over the outside of
   the cable has been enough for several machines.
2. **If a plain core is not enough**, stubborn cases have responded to routing the
   cable through a higher-grade toroid for several turns instead of a single pass.
   TODO(verify): the specific ferrite material grade and the number of turns.
   Reported in the common-problems summary thread; not independently confirmed here.
3. **Recalibrate or factory-reset afterwards.** On several machines the ferrite
   appeared to do nothing until the stored calibration data was discarded — by a
   factory reset or a full recalibration — because the printer was still working from
   figures it had captured while the signal was noisy. If you fit a core and nothing
   changes, do this before concluding the core did not help.
4. **Mind the placement.** At least one reported position — at the controller's
   extension-board connector rather than on the main cable — made the problem worse.
   If your first placement degrades things, move it rather than abandoning the idea.

### Other sources owners have found

A ferrite on the main toolhead cable treats one path for the noise. Owners in the
[tool offset calibration thread](https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/tool-offset-calibration-failing/)
and in [#5526](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5526) have since
found others. Each rests on a few owners, most of whom changed several things at once, so
all of them are `provisional`.

- **The bed heater wiring.** One owner, whose INDX failed tool offset calibration from
  its very first print, separated the two heater wires out of the main bundle in the
  wiring box at the back (from the routing they describe, apparently the bed
  heater's), twisted them together and fitted ferrite chokes where they meet the
  controller board, with chokes on the toolhead and offset sensor cables at the same
  time; it has worked since. Another owner, whose loadcell self-test sometimes
  reported noise, with sharp spikes on its bar graph, twisted the bed heater wires,
  fitted chokes to them and to the toolhead harness, and kept the cables apart and free
  of loops; after that the test settled and the failures stopped.
- **The toolhead power wires.** A third owner twisted the power and ground wires of the
  INDX toolhead harness into pairs along its whole length, which meant releasing the
  pins from the connector at the controller end one by one; that cleared most of their
  calibration failures. A pin put back in the wrong position can damage the
  electronics, so this is not a first step. The Detail section above says the power
  pair in the loom is twisted; this owner twisted the pairs themselves, implying theirs
  were not, while the second owner above describes theirs as already twisted, so
  harnesses may differ.
- **The LED status strip.** In
  [#5526](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5526), an owner on
  6.9.1 traced tool offset calibration failures during prints to the RGB status strip,
  the LED strip whose color follows the printer's state; they call it the bed LED. The
  loadcell noise rose whenever the strip was lit and fell back when it went dark. In
  that report, calibration failed inside a print, where the strip is lit, and passed
  when started from the menu, where it is not. Much of that owner's testing was done on
  firmware they had modified themselves, which this page does not rely on. The owner
  who twisted the toolhead power wires, on stock 6.9.2, still had an occasional
  failure after that; switching the strip off (the RGB Status Bar option, in the
  settings or under Tune > Lights during a print) stopped it, and they later fitted
  ferrite beads to both the bed LED and the chamber LED cables and have had no trouble
  since. A further owner switched the LEDs off and put ferrites on every cable they
  could reach at the same time, and their failures stopped too. Switching the strip off
  costs nothing and is easily undone, which makes it a cheap test before opening the
  wiring.

The pattern of failing in a print and passing from the menu fits both the heaters and
the strip, since owners describe both as off during the menu run; the owner who twisted
the power wires first read it as heater interference. Outside the strip owner's own
testing, nobody has told the two apart on one machine.

!!! tip "How to tell interference from a genuinely bad loadcell"
    A ferrite core treats electrical interference. It will not fix a failed loadcell,
    and the two present almost identically. One owner separated them cleanly: their
    probing fault **followed a replacement toolhead** across a swap while the original
    head homed perfectly every time, on a recent controller board. Interference is a
    property of the machine and its wiring; a fault that travels with the toolhead is
    in the toolhead. See [diagonal banding](diagonal-banding.md), where that swap is
    described. If your board is recent and the fault moves with the head, go to the
    vendor rather than buying ferrites.

    A report from another thread ended in a hardware fix rather than interference. An
    owner on 6.6.0 and 6.6.1 whose loadcell
    test kept warning of unstable readings, although a press on the nozzle still
    registered once the warning was dismissed, and whose prints stopped on a 36130 tool
    offset error, eventually
    [traced the problem to a faulty part](https://forum.prusa3d.com/forum/ceske-forum-obecna-diskuze-oznameni-a-novinky/core-one-indx-tool-offset-out-of-bounds-36130-loadcell-test-issue/)
    they call the tool holder, which they took up with the manufacturer under warranty;
    everything has worked since. The post does not come back to the loadcell warning;
    that it cleared too is implied by "everything", not stated. The post mentions no
    ferrite. It does not make clear
    which assembly they mean, so that one is `provisional`. The same case appears under
    [tool offset calibration fails](offset-sensor-board-failure.md).

!!! note "A third cause: homing that fails after the calibration passed"
    Firmware 6.9.1, released as stable on 2026-09-25, lists a homing fix for
    printers that passed their first homing calibration but failed when homing again
    later. The change Prusa describes is to motor currents; a Prusa developer later
    explained in [#5520](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5520)
    that it was meant to stop belts slipping during homing on some printers, where the
    motor holding position could not resist the one doing the bumping. The
    [release notes](https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.9.1)
    name no axis, but the only motor-current change in the firmware repository
    between the beta and the stable
    ([compare](https://github.com/prusa3d/Prusa-Firmware-Buddy/compare/v6.9.1-beta...v6.9.1))
    is to the diagonal XY homing, not to the loadcell's Z probing. The notes also say
    nothing about the loadcell or the heater, so this is a separate fault from the one
    on this page, not a fix for it. If your homing failures match that description
    rather than the pattern above — failing only once hot, the nozzle stopping visibly
    short of the sheet — update the firmware before fitting a ferrite, but read the
    next paragraph first. This rests on the vendor's release notes, its firmware
    repository and that explanation alone, `provisional`: no owner has yet reported the
    fix curing their homing failures.

    Owners report what looks like a side effect of the same change, in
    [#5520](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5520), in a
    [forum thread](https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/homing-shows-early-endstop-detected-message/)
    and in [another](https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/gantry-squaring-failing/):
    since 6.9.1, homing shows an `Endstop early trigger` message several times and
    takes longer. For some it still finishes and prints run normally; for others the
    homing calibration fails, which stops the setup. Calibrating homing again after the
    update, Prusa's first suggestion, did not help; going back to the 6.9.1 beta or to
    6.9.0 made it stop for every owner who reported trying it, and several ran the
    homing calibration again after going back. Prusa says it did not see this on the
    printers it tested the change on, has said it is looking into the reports, and has
    asked owners who see it to stay on the earlier firmware in the meantime; the
    comment names 6.9.1, while the owners had gone back to the 6.9.1 beta or to 6.9.0.
    Going back to either also gives up the gantry squareness wizard, which the
    comparison above shows arriving after the beta. Two owners say 7.0.0 behaves the
    same, and the
    [7.0.0 release notes](https://help.prusa3d.com/downloads/core-one-indx) list no
    change to homing currents. In the
    [6.9.1 source](https://github.com/prusa3d/Prusa-Firmware-Buddy/blob/v6.9.1/lib/Marlin/Marlin/src/module/prusa/homing_corexy.cpp)
    that message marks an X/Y homing bump that stopped short and is being repeated;
    the measurement gives up only if the repeats run out. It comes from the X/Y homing,
    not the loadcell, and is no sign of interference. Several owners, in the issue and
    in two separate forum threads, make the message and the effect of going back
    `reported`; that the lower current causes it is an inference.

If none of that helps, particularly if the failure happens only with the heater on
and you are on an early board revision, the path is hardware replacement through the
vendor. One owner reported success wrapping the wiring at the controller connector in
grounded shielding foil instead, which is consistent with the same root cause.

TODO(verify): the raw loadcell value ranges that distinguish a healthy machine from
an affected one. The summary thread quotes an idle-value band for each, and those
numbers would make this page far more diagnostic — but they need checking against
firmware before being published, because a reader will use them to decide whether
their machine is faulty.

!!! note "This is a mitigation, not a cure"
    The vendor has described the ferrite as a stopgap rather than a fix, and a
    firmware-side improvement to loadcell handling is reportedly in progress. Neither
    the 6.9.0 nor the 6.9.1 release notes describe any change to how the loadcell
    signal is filtered or judged. The
    [6.9.1-beta notes](https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.9.1-beta)
    do give tool offset calibration more Z probe attempts. The stable notes do not
    restate it, but the stable 6.9.1 is built on that beta: in the firmware repository
    it adds
    [15 commits](https://github.com/prusa3d/Prusa-Firmware-Buddy/compare/v6.9.1-beta...v6.9.1)
    to the beta tag, none of them in the tool offset calibration code. That comes from
    the release history, not from the notes. More retries give a noisy tap more
    chances to pass; they do nothing about the noise.
    [6.9.2](https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.9.2),
    released on 2026-10-07,
    adds the PVA and BVOH filament presets that 6.9.1 announced and left out, and
    nothing else that reaches an INDX
    ([compare](https://github.com/prusa3d/Prusa-Firmware-Buddy/compare/v6.9.1...v6.9.2)),
    so it changes nothing described on this page.
    [7.0.0](https://help.prusa3d.com/downloads/core-one-indx), published on
    2026-10-15, lists nothing on how the loadcell signal is filtered or judged, nor on
    the self-test, the extruder motor after a toolchange or the status strip. Prusa had
    not published its source on GitHub by the date above, so what it changes is known
    only from those notes and from owners: the extruder motor effect has been measured
    on it. If you are reading this well after the date above, check whether a newer
    firmware has addressed it before adding hardware.

## Verification

`reported` — independently described in more than one thread by different owners.

In [Nozzle not touching bed during probing](https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/nozzle-not-touching-bed-during-probing/)
an owner reports probing running with the nozzle far above the sheet on a machine
that had passed all its setup calibrations; after fitting a ferrite core to the main
cable they confirm probing began working correctly. A second owner in the same thread
reports one probe-too-high incident and fitted a core pre-emptively without
regression. The mechanism, the vendor's acknowledgment, and the toroid variant come
from the [common problems summary](https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/a-summary-of-common-indx-problems/),
which is a condensation of a now-offline community knowledge base.

Where the sources are weaker: the controlled A/B test described in the summary
(failing without a core, working with one, failing again on removal) is reported
second-hand there and is not separately visible in the forum corpus. The loadcell
value bands and ferrite specifications are single-source and withheld above. The
self-test that passes on a retry now has two reports in different places, and Prusa
could not reproduce the first. The extruder motor's effect on the self-test is now in
two separate issues, one of them on 7.0.0, with a further owner in the first confirming
the abort-and-retry part; the firmware source is consistent with it, but Prusa has not
confirmed it, neither earlier owner tested it, and its link to print-start failures is
unproven. Homing before the retry, the
repeated-mesh check, the warranty claim and the tool-detection case under Related are
one report each.
None of those owners fitted a ferrite, so they neither strengthen nor weaken the case
for it. The bed heater wiring and the toolhead power wires come from one forum thread,
and the status strip from one issue and that same thread, with the first owner's
testing partly on modified firmware; the owners mostly changed several things at once.
The early-trigger homing message is reported by several owners across one issue
and two forum threads. The homing fix rests on the vendor's release notes, its firmware
repository and a developer's explanation, not on owner reports.

## Related

- [Tool offset calibration fails](offset-sensor-board-failure.md) — separate
  sensor, separate fault, often confused with this one
- [Oozing spoils bed probing and tool calibration](oozing-during-probing-and-calibration.md)
  — a completely different cause with an overlapping symptom, worth ruling out. If
  material is accumulating on the nozzle before contact, that is the other one.
- [Tool offset calibration fails: bed not aligned in Z](tool-offset-bed-z-alignment.md)
  — a mechanical fault that was taken for loadcell noise on one machine; a ferrite
  core did nothing for it
- [Who to contact](support-and-warranty-path.md) — if it comes to a parts request:
  diagnosis from Prusa first, then the hardware from Bondtech.
- [Assembly notes](../reference/assembly-notes.md) — if the loadcell test has been
  unstable since the machine was built and never worked, treat it as a build
  question before an interference one.
- [Phantom tools, "tool not detected" and park failures](tool-detection-ringdown-decay.md)
  — how the head detects a fitted tool. A detection fault can also stop the loadcell
  test without being a loadcell fault: in
  [one report](https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/loadcell-test-tool-crash-on-calibration/)
  on 6.9.1, the test step picked a tool and drove it into the other docks, and the
  owner found the printer never registered a fitted tool (`provisional`). A check of
  the head's wiring found nothing, and the case was still open with Prusa support at
  the date above.
