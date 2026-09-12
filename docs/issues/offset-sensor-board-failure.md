---
title:        Tool offset calibration fails — contactless offset sensor
confidence:   reported
updated:      2026-09-12
author:       hyiger
printer:      Core One
toolhead:     INDX
hotend:       unknown
nozzle:       unknown
firmware:     6.9.0 for the calibration regression, addressed in 6.9.1-beta; the board fault is not version-specific
sources:
  - https://help.prusa3d.com/article/tool-offset-failed-36130-core-one-indx_1089016
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5442
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.9.1-beta
  - https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5473
  - https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/offset-sensor-failure/
  - https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/tool-offset-calibration-failing/
  - https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/a-summary-of-common-indx-problems/
superseded_by:
---

# Tool offset calibration fails — contactless offset sensor

## Summary

Tool Offset Calibration failing repeatedly, with an error message that tells you
nothing useful, is most often a faulty contactless offset sensor board rather than
anything you have assembled wrongly. Clean the sensor first, because a fleck of
filament on it produces exactly the same failure. If cleaning does not fix it, the
resolution reported by multiple owners is a replacement sensor board — and belt
tension, which support may suggest, has not fixed a single reported case.

!!! important "Before you suspect the board: are you on 6.9.0?"
    An open [bug report against the firmware](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5442) describes tool offset calibration
    failing repeatedly **after upgrading to 6.9.0**, on machines where it had been
    working. It is no longer a couple of accounts: the report has drawn a steady stream
    of owners across both four- and eight-tool machines, including new Gen 2 builds
    that passed every calibration during assembly. It affects multiple tools rather
    than one, and the calibration wizard often succeeds while the check at print start
    keeps failing.

    That matters here because it presents almost identically to the hardware fault
    this page is about, and the fix is completely different. If your calibration was
    fine before an update and started failing after one, you are more likely looking
    at this than at a failed sensor board — and replacing hardware will not help.

    **The strongest evidence that it is the firmware:** several owners report that
    going back to 6.6.3 restores reliable calibration, and that returning to 6.9.0
    brings the failure back.

    **But downgrading is not open to every machine.** Support for the newer 1.5 GT
    belts arrived *in* 6.9.0, so a printer fitted with them has no earlier firmware
    that knows their geometry. One owner in the thread could revert only because they
    had refitted the original belts first. If yours are the new ones, reverting is not
    the workaround — it trades a calibration failure for a motion system the firmware
    does not model.

    **Part of the cause is now confirmed by the vendor's own fix.** The beta release
    notes name two changes aimed at exactly this failure: tool offset calibration runs
    at a lower temperature, and the communication between the offset sensor and the
    main board was reconfigured to stop dropouts. The first is the ooze explanation
    owners had converged on — the nozzle oozes while it is heated for calibration and
    the deposit spoils the measurement, which is why the on-screen message asks you to
    check the nozzle is clean. The second is something the thread had not identified.
    The ooze half is the same mechanism as
    [oozing during probing](oozing-during-probing-and-calibration.md), with the
    difference noted there: the calibration temperature is fixed in firmware, so that
    page's slicer-side workarounds could never reach it. It needed a firmware change.

    **One configuration trap worth clearing first.** 6.9.0 added support for the newer
    1.5 GT belts. If your machine does not have them, that option must be off — it
    changes the geometry enough to matter. Several owners checked and found their
    settings already correct, so it is not the whole story, but it is free to rule out.

    **There is a vendor fix, in beta.** After investigating with input from owners on
    the report and tracking the fault internally, the vendor published
    [6.9.1-beta](https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.9.1-beta)
    for the Core One INDX on 10 September 2026. Alongside the temperature and
    communication changes it lets calibration retry
    its Z probing up to 10 times instead of 3, and lists a fix for tool offset recovery. The calibration
    temperatures themselves are in the release notes and are not repeated here. Several
    owners on the report say calibration now passes first time where it had been failing
    every time.

    It is a beta, and not yet clean for everyone. One owner reports a thermal runaway
    after the first filament change on it, which the developer asked to be filed as a
    separate bug; another finds calibration passing reliably but nozzles coming out
    noticeably dirtier. Neither is confirmed beyond its reporter.

    For owners with the newer belts it also removes the dilemma above: the beta is INDX
    firmware that keeps 1.5 GT support, so moving forward replaces downgrading as the
    way out. Check the report for whether a stable 6.9.1 has shipped before installing a
    beta. The firmware links an official help article for this error code, which owners
    say did not resolve it.

!!! note "A lead: some offset sensor board failures may be a clock setting"
    `provisional` — one report, and its author says it is not yet proven.

    An owner who hit the sensor's first-sample failure on both 6.6.3 and 6.9.0 replaced
    nearly everything in the signal path without clearing it: two offset sensor boards,
    several cables including one run outside the printer, two main boards, the motors,
    the carriage and the power supply. What cleared it involved no hardware at all. A
    firmware build that doubled the reference clock divider on the offset sensor's LDC1612
    chip — taking its reference frequency from 40 MHz to 20 MHz — got all eight tools
    through calibration at the first try.

    The reasoning can be checked against the chip's datasheet, which caps the reference
    frequency at 35 MHz in the single-channel mode the INDX uses — below what the stock
    firmware sets. If that is the cause, units with a little less margin would fail
    intermittently while most carry on working, which would also account for a
    replacement board curing the same error for some owners without the fault ever
    being widespread.

    Treat it as a lead rather than a fix: one machine, a custom build, a result the
    reporter was still repeating, and a write-up they disclosed was drafted with an AI
    assistant. No source connects it to the communication fix in 6.9.1-beta, although
    both concern the same sensor link. See
    [firmware issue 5473](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5473).

## Error codes that lead here

| Code | What the printer shows |
|---|---|
| [`36130`](https://help.prusa3d.com/article/tool-offset-failed-36130-core-one-indx_1089016) | Tool offset failed |
| [`36136`](https://help.prusa3d.com/article/calibrate-dock-from-menu-17136-xl-36136-core-one-indx_1037195) | Calibrate dock from menu |

`36130` is this page. It is also the code the firmware links its own help
article for, which the owner reporting the 6.9.0 regression says did not resolve
their case.

## Detail

Two different sensors are involved in setting up an INDX, and knowing which one has
failed saves a great deal of wasted effort. The loadcell handles Z contact against
the bed. A separate contactless inductive sensor on its own small PCB handles tool
offsets. In this failure mode the loadcell Z-probe passes fine; it is the contactless
sensor that returns no readings at all, so calibration has nothing to work with.

The firmware log carries a distinctive fingerprint — an error naming the contactless
offset routine together with a failure to obtain a first sensor sample. That log line
is the single most useful thing you can capture, because the on-screen message is
generic and the on-screen suggestion to clean the nozzle is misleading.

What makes this fault confusing:

- **The tool number where it fails is not diagnostic.** Owners report failing on the
  first tool, and others report getting several tools in before failing, with the
  stopping point moving between attempts and no changes in between. Different
  stopping points do not mean different problems.
- **Swapping tools around does not help**, and neither does re-seating the tools.
  Several owners worked through permutations before concluding the sensor was at
  fault.
- **Belt tension is a red herring here.** It is a reasonable first guess and support
  has suggested it, but owners who squared and re-tensioned the gantry thoroughly
  report no change. Do not spend a night on it before capturing a log.
- **Cable continuity testing good does not clear the sensor.** One owner checked the
  cable, found it electrically fine, and the board was still the fault. Cable
  replacements on their own have not fixed reported cases.

### What to do, in order

1. **Clean the sensor itself**, not just the nozzle. A small piece of filament debris
   sitting on the sensor face causes an identical failure, and this is the one cause
   you can fix yourself in a minute.
2. **Capture a firmware log over the USB-C serial connection** and keep it. This is
   the evidence that gets a support case resolved quickly — at least one owner
   reports the vendor confirming the board as faulty specifically on the strength of
   submitted logs. TODO(verify): the serial baud rate to configure. It is stated in
   the summary thread, but a reader will type it into a terminal, so it needs
   checking first.
3. **Check the LED on the sensor PCB.** If it keeps blinking rapidly once a
   calibration has already failed, that points at the board itself — the rapid
   pattern is only meant to appear while the sensor's microcontroller is being
   flashed. Seeing it outside of a firmware update is a strong signal.
4. **Open a support case.** The reported route is diagnosis with Prusa first, then a
   Bondtech ticket for the replacement board, carrying Prusa's findings with it. A
   ticket that already says what Prusa identified moves faster than one starting from
   symptoms. Open it early even if you are not ready to act, so the date is on record
   — see [who to contact](support-and-warranty-path.md).

The sensor works on eddy currents, which is worth knowing for two reasons: it is why
a non-conductive nozzle tip is a design constraint for future nozzle variants, and it
is why surface contamination on the sensor matters as much as it does.

A board-to-board comparison reported in the summary found that a failing unit and a
working unit were the same hardware revision from the same production batch, so this
looks like unit-level variance rather than a bad batch you could identify from a
serial number.

!!! warning "One suggestion in the threads is not a repair"
    Reflow-oven reworking of the sensor board was floated by an owner as something
    they might try. There is no report of anyone doing it successfully, and it would
    almost certainly end any warranty claim on the part. Get the board replaced.

## Verification

`reported` — two independent threads, two different owners, both ending at board
replacement.

[Offset sensor failure](https://forum.prusa3d.com/forum/prusa-indx-general-discussion-announcements-and-releases/offset-sensor-failure/)
documents calibration failing on the first tool and establishes the support route
that owners converged on. [Tool offset calibration failing](https://forum.prusa3d.com/forum/prusa-indx-assembly-and-first-prints-troubleshooting/tool-offset-calibration-failing/)
is a separate owner with a different-looking presentation — failing partway through
the tool sequence, intermittently — who worked through belt tension and tool swaps
without improvement, verified cable continuity as good, and reports the vendor
confirming the PCB as the fault after reviewing submitted logs. That two dissimilar
symptom patterns resolve to the same component is the most useful thing on this page.

The log fingerprint, the LED diagnostic, the eddy-current mechanism, and the
same-batch comparison come from the
[common problems summary](https://forum.prusa3d.com/forum/prusa-indx-hardware-firmware-and-software-help/a-summary-of-common-indx-problems/),
a condensation of a now-offline community knowledge base. Those specifics are
single-source and have not been separately confirmed in the forum corpus.

Where the sources disagree: support's own first suggestions varied between cable and
board, and in one case belt tension was raised. Owner experience points consistently
at the board.

**Added since first publication.** The 6.9.0 calibration regression comes from the
[firmware issue tracker](https://github.com/prusa3d/Prusa-Firmware-Buddy/issues/5442),
which is a stronger class of source than the forum for firmware behavior — it is
first-party, versioned and reproducible. What began as two accounts has become a long
thread of independent reporters on both machine sizes, several of whom resolved it by
downgrading. That reciprocal test — fails on 6.9.0, works on 6.6.3, fails again on
6.9.0 — is what makes the regression itself well supported.

The *cause* is now partly established. Where this page previously had only owners
converging on ooze, the vendor's beta release notes name a lower calibration
temperature and a fix for offset sensor communication dropouts, and the developer on
the report said both mattered. That is the vendor naming contributing causes, not a
published root-cause analysis, and the fix is still a beta. Until a stable release
ships and the report closes, treat it as the vendor's current fix rather than a
settled one.

The LDC1612 reference-frequency lead is a separate single report from a different
owner, unconfirmed by the vendor, and is marked `provisional` where it appears.

## Related

- [Probing fails or nozzle never touches the bed](loadcell-emi-noise.md) — the other
  sensor, frequently confused with this one
- [Assembly notes](../reference/assembly-notes.md) — if this is failing on a
  freshly built machine that has never calibrated successfully, check the build
  first: this is one of the two selftest failures that recur on new conversions
- [Who to contact](support-and-warranty-path.md) — getting the replacement part:
  diagnosis from Prusa, hardware from Bondtech, and open the case early enough that
  the date falls inside your warranty window.
