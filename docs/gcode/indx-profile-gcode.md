---
title:        Annotated start, layer and toolchange G-code
confidence:   measured
updated:      2026-08-25
author:       hyiger
printer:      Core One
toolhead:     INDX
hotend:       unknown
nozzle:       unknown
firmware:     6.9.0+16311
sources:
  - https://github.com/prusa3d/Prusa-Firmware-Buddy
  - https://help.prusa3d.com/article/buddy-firmware-specific-g-code-commands_633112
  - https://reprap.org/wiki/G-code
  - https://docs.duet3d.com/User_manual/Reference/Gcodes
  - https://blog.prusa3d.com/better-prints-easier-use-prusa-xl-core-one-l-and-core-one-gen-2-our-big-product-update_137539/
  - https://github.com/SimplyPrint/slicer-profiles-db
superseded_by:
---

# Annotated start, layer and toolchange G-code

!!! info "This is the stock profile, reproduced verbatim"
    Everything below is Prusa's own PrusaSlicer profile for the Core One INDX on
    firmware 6.9.0 — not a customization. If you are on 6.9.0 this is what you already
    have, before you change anything.

    That is the reason to read it. The values are the shipped defaults rather than
    anyone's tuning, so understanding what each block does tells you what your machine
    is actually doing on every print, and gives you a baseline to diff your own changes
    against.

    The command behavior is verified against the Prusa firmware source. The profile
    itself changes between firmware releases, so check the version above against yours —
    the 6.6.3 profile differed from this one in several places.

## What this is

Five blocks, covering the whole print lifecycle:

| Block | Runs | Does |
|---|---|---|
| Start | Once, before the print | Preflight checks, homing, tool calibration, heat soak, mesh bed leveling, clean and prime |
| Before layer change | Every layer | Resets the extruder, tapers acceleration with height |
| After layer change | Every layer | Dock fan control, on layers 1 and 3 only |
| Tool change | Every tool change | Park, swap, purge or wipe, resume |
| End | Once, at the end | Cool down, park, disable |

They are not independent. The start block sets globals the other four read, and one
line at the very end of the start block silently changes what the *first* tool change
does. That coupling is called out where it happens.

## Start G-code

### Globals and the probe temperature

```gcode
{
global retract_toolchange = 8;
global tool_init = (0,0,0,0,0,0,0,0);
global used_tools = 0 ;
global low_temp_types = "PLA|PVA|BVOH|FLEX|TPU|TPE|PVB";
}

; number of used tools
{if is_extruder_used[0]}{used_tools = used_tools + 1}{endif}
{if is_extruder_used[1]}{used_tools = used_tools + 1}{endif}
{if is_extruder_used[2]}{used_tools = used_tools + 1}{endif}
{if is_extruder_used[3]}{used_tools = used_tools + 1}{endif}
{if is_extruder_used[4]}{used_tools = used_tools + 1}{endif}
{if is_extruder_used[5]}{used_tools = used_tools + 1}{endif}
{if is_extruder_used[6]}{used_tools = used_tools + 1}{endif}
{if is_extruder_used[7]}{used_tools = used_tools + 1}{endif}

{local probe_temp = "" + ((filament_notes[initial_tool]=~/.*MBL160.*/) ? 160 : (filament_notes[initial_tool]=~/.*HT_MBL10.*/) ? (first_layer_temperature[initial_tool] - 10) : (filament_type[initial_tool] == "PC" or filament_type[initial_tool] == "PA") ? (first_layer_temperature[initial_tool] - 55) : (filament_type[initial_tool] == "FLEX") ? 170 : (filament_type[initial_tool]=~/.*PET.*/) ? 170 : 170) + "";}
```

None of this emits G-code. It runs in the slicer and sets up state the rest of the
profile reads.

**The four globals** persist across every block in the print, which is the only reason
the layer and toolchange blocks can see them:

- `retract_toolchange` — extra retraction used when parking a tool, referenced later by
  `G27 R` and by the deretract length on the way back in.
- `tool_init` — an eight-slot array, one per tool, all starting at zero. A tool's slot
  flips to `1` the first time it has been cleaned and primed. The tool change block
  branches on this; see the coupling note at the end of the start block.
- `used_tools` — a count, built by the eight lines that follow. The after-layer-change
  block gates its whole dock-fan section on `used_tools > 1`, so a single-tool print
  skips it entirely.
- `low_temp_types` — a regex alternation of the materials treated as low-temperature.
  Defined here, used only in the after-layer-change block. **If you remove this line,
  that block breaks** with an undefined variable, which is not obvious from reading
  either block on its own.

**The probe temperature** is a chain of conditionals picking the nozzle temperature the
machine will hold while probing the bed. It reads, in order: a filament-note override,
a second note-based override relative to first-layer temperature, a lower temperature
for PC and PA, a fixed value for FLEX, a fixed value for anything PET-ish, and finally a
default. The `"" + ... + ""` wrapper coerces the result to a string so it can be
substituted into `M109` later.

The interesting part is *why* it exists: probing wants the nozzle hot enough not to be
dimensionally odd, but cool enough not to ooze onto the sheet while the loadcell is
trying to read contact. Oozing during probing is a known failure mode — see
[oozing spoils bed probing](../issues/oozing-during-probing-and-calibration.md).

### Preflight checks

```gcode
M862.3 P "COREONEINDX" ; printer model check
M862.5 P2 ; g-code level check
M862.6 P"Input shaper" ; FW feature check
M862.6 P"INDX lock" ; FW feature check
M115 U6.9.0+16311

M591 S0 ; disable stuck detection

M555 X{(min(print_bed_max[0], first_layer_print_min[0] + 32) - 32)} Y{(max(0, first_layer_print_min[1]) - 4)} W{((min(print_bed_max[0], max(first_layer_print_min[0] + 32, first_layer_print_max[0])))) - ((min(print_bed_max[0], first_layer_print_min[0] + 32) - 32))} H{((first_layer_print_max[1])) - ((max(0, first_layer_print_min[1]) - 4))}

; inform about nozzle diameter
{if (is_extruder_used[0])}M862.1 T0 P{nozzle_diameter[0]} A{(filament_abrasive[0] ? 1 : 0)} F{(nozzle_high_flow[0] ? 1 : 0)}{endif}
{if (is_extruder_used[1])}M862.1 T1 P{nozzle_diameter[1]} A{(filament_abrasive[1] ? 1 : 0)} F{(nozzle_high_flow[1] ? 1 : 0)}{endif}
{if (is_extruder_used[2])}M862.1 T2 P{nozzle_diameter[2]} A{(filament_abrasive[2] ? 1 : 0)} F{(nozzle_high_flow[2] ? 1 : 0)}{endif}
{if (is_extruder_used[3])}M862.1 T3 P{nozzle_diameter[3]} A{(filament_abrasive[3] ? 1 : 0)} F{(nozzle_high_flow[3] ? 1 : 0)}{endif}
{if (is_extruder_used[4])}M862.1 T4 P{nozzle_diameter[4]} A{(filament_abrasive[4] ? 1 : 0)} F{(nozzle_high_flow[4] ? 1 : 0)}{endif}
{if (is_extruder_used[5])}M862.1 T5 P{nozzle_diameter[5]} A{(filament_abrasive[5] ? 1 : 0)} F{(nozzle_high_flow[5] ? 1 : 0)}{endif}
{if (is_extruder_used[6])}M862.1 T6 P{nozzle_diameter[6]} A{(filament_abrasive[6] ? 1 : 0)} F{(nozzle_high_flow[6] ? 1 : 0)}{endif}
{if (is_extruder_used[7])}M862.1 T7 P{nozzle_diameter[7]} A{(filament_abrasive[7] ? 1 : 0)} F{(nozzle_high_flow[7] ? 1 : 0)}{endif}

G90 ; use absolute coordinates
M83 ; extruder relative mode
```

The `M862.x` family are compatibility gates. They compare what the file expects against
what the machine actually is, and stop the print rather than let it fail expensively
later:

- `M862.3 P"COREONEINDX"` — printer model. Sliced for the wrong machine, this is where
  it stops.
- `M862.5 P2` — G-code dialect level.
- `M862.6 P"<feature>"` — a named firmware feature must be present. Two are required
  here: input shaping, and the INDX lock.
- `M862.1` — per-tool nozzle declaration, repeated once per used tool: `T` the tool,
  `P` its diameter, `A` whether the assigned filament is abrasive, `F` whether the
  nozzle is high-flow. This is what lets the firmware object when an abrasive filament
  is about to be run through a nozzle not marked as suitable for it — see
  [nozzle hardness](../issues/nozzle-hardness.md) for why that flag matters on this
  machine.

`M115 U…` declares the firmware version the file was generated for.

`M591 S0` disables the filament stuck-detection feature for the print. That detection
works by reading extrusion back-pressure through the load cell — the same sensor Prusa
has said will calibrate pressure advance in a future firmware. Why the INDX profile
switches it off at print start is not established.

`M555` declares the print area, derived from the first layer's bounding box with margin.
The firmware uses it to know which part of the bed matters — most visibly, it is what
mesh bed leveling probes rather than probing the whole sheet.

`G90` / `M83` set absolute positioning for motion and relative for the extruder. Every
`E` value after this point is a delta, not a target.

### Homing, tool preparation and calibration

```gcode
M140 S{first_layer_bed_temperature[initial_tool]} ; set bed temp

{if chamber_minimal_temperature[initial_tool] == 0}
  M141 S{chamber_temperature[initial_tool]} ; set nominal chamber temp
{endif}

; Home XY
G28 XY

; Pick tool for Z homing
{if is_extruder_used[0]}T0 S1 L2 D0
{elsif is_extruder_used[1]}T1 S1 L2 D0
{elsif is_extruder_used[2]}T2 S1 L2 D0
{elsif is_extruder_used[3]}T3 S1 L2 D0
{elsif is_extruder_used[4]}T4 S1 L2 D0
{elsif is_extruder_used[5]}T5 S1 L2 D0
{elsif is_extruder_used[6]}T6 S1 L2 D0
{elsif is_extruder_used[7]}T7 S1 L2 D0
{endif}

M104 S120

; Home Z
G28 Z

G0 Z40 F10000
M190 R{first_layer_bed_temperature[initial_tool]} ; wait for bed temp
; try picking tools used in print
G1 F10000
```

Bed and chamber setpoints go out first so heating overlaps everything that follows.
`M140` and `M141` set targets without waiting; `M190` later is the one that blocks.

The chamber line is conditional. If the filament declares a *minimum* chamber
temperature it is skipped here, because a dedicated chamber-soak section further down
handles that case instead.

`G28 XY` homes the two axes that do not need a tool fitted. Z homing does, because Z is
found by touching the nozzle to the bed — so a tool is picked first. The `elsif` chain
picks the lowest-numbered used tool, whichever that is.

`M104 S120` sets a modest nozzle target before Z homing. Warm enough that any residue on
the tip is soft rather than a hard lump under the probe, cool enough not to ooze while
the machine works.

After homing, `G0 Z40` drops the bed clear and `M190 R…` waits for the bed to reach
temperature. This is the longest single wait in the whole startup.

```gcode
{local perimeter_flow_rate = 1.0 * (external_perimeter_speed > 0 ? external_perimeter_speed : (perimeter_speed > 0 ? perimeter_speed : 100)) * (layer_height * (external_perimeter_extrusion_width - layer_height) + 3.14159 * (layer_height/2) * (layer_height/2))}

{if (is_extruder_used[0] and filament_type[0] != "FLEX")}M574 S0 V35 T{temperature[0]} F{ (filament_max_volumetric_speed[0] > 0 ? min(perimeter_flow_rate, filament_max_volumetric_speed[0]) : perimeter_flow_rate ) / (3.14159 / 4 * filament_diameter[0] * filament_diameter[0]) }{endif}
```

*(repeated once per tool, `S0` through `S7` — only the first is shown here)*

`perimeter_flow_rate` is computed once and reused by all eight lines. It is the
volumetric flow implied by the external perimeter settings: speed multiplied by the
cross-sectional area of an extrusion, modeled as a rectangle with semicircular ends.
The fallback chain means it degrades to perimeter speed, then to a constant, rather
than producing zero if a speed is unset.

Each `M574` line then converts that volumetric figure into a linear filament feedrate by
dividing by the filament's cross-sectional area, capped by the material's maximum
volumetric speed where one is set. FLEX is excluded.

!!! note "M574 is not implemented — the firmware ignores it"
    `M574` has no handler in Prusa Buddy firmware. That is checked against the `v6.9.0`
    release tag, the version this profile targets, and against every object in the public
    repository's history, with `M572` and `M575` as positive controls to prove the search
    finds what is actually there. Marlin is vendored in-tree under `lib/Marlin` rather
    than as a submodule, so the same search covers the Marlin layer.

    What the machine does with it follows from the parser's fallback. Prusa's own
    dispatcher declines the command, Marlin's switch reaches
    `default: parser.unknown_command_error()`, and `queue.ok_to_send()` still runs
    afterwards. So the printer logs `Unknown command:` with the offending line, answers
    `ok`, and carries on — no error, no pause, nothing on screen. Eight ignored lines per
    print, one per used non-FLEX tool.

    *That paragraph is derived from the firmware source, not from a captured log.* No
    terminal or log capture of a real INDX receiving `M574` appears to exist publicly,
    and no issue about it has ever been filed against Prusa's firmware or slicer tracker.

    One limit on the claim: Prusa develops privately and publishes release tags, so this
    establishes that the firmware **you run** has no handler — not that none exists
    anywhere.

!!! warning "Searching for M574 will mislead you"
    `M574` is not an unclaimed number. The RepRap G-code registry and RepRapFirmware both
    assign it to endstop configuration, where `S` selects an endstop type and `V`, `T` and
    `F` do not exist as parameters at all. Almost everything a search returns for "M574"
    describes endstops on a Duet and has nothing to do with this command.

!!! info "Where it comes from, and the feature Prusa has announced"
    There is no commit to find. `M574` has never existed in any public Prusa git
    repository — the line ships out-of-band in Prusa's vendor profile bundle rather than
    in the slicer source. It first appeared in PrusaResearch bundle 2.5.0 on 26 June 2026,
    the bundle that added the Core One INDX profiles, and was rewritten in 2.5.7 on
    20 August 2026. It is INDX-exclusive — not XL, not MK4, not plain Core One — so there
    is no older toolchanger ecosystem in which it is already documented.

    It has a sibling. The same bundle emits `M573 R` in its filament start G-code, on the
    line immediately after `M572` sets pressure advance. The `R` carries no value and is
    not an unrendered placeholder; it is a literal bare flag, identical across all
    thirteen INDX filament profiles since they first shipped. `M573` is likewise absent
    from the firmware.

    On 13 August 2026 Prusa announced that it is replacing the single fixed pressure
    advance value with a flow-dependent model whose parameters the **load cell measures
    automatically before every print**, together with new extrusion-aware acceleration
    limits that stop the printer demanding flow changes faster than the extruder can
    deliver. The announcement describes the work as in internal testing and gives no
    release date, no firmware version, and **no G-code command**.

    `M574` carries, per tool, a target temperature and the peak extrusion rate the print
    will demand — which is the shape of input that work would need, and the profiles
    predate the announcement by about seven weeks. **No source connects the two.** That
    reading is recorded because it is the most plausible one available, not because it is
    established; it also fits the acceleration-limit half of the announcement at least as
    well as the calibration half.

    TODO(verify): what `M574` and `M573 R` are for, and what `S`, `V`, `T` and `F` each
    mean. `S` is a tool index and `T` a temperature by inference from the call site — a
    reading worth holding loosely, since Marlin's own convention is the opposite, `S` for
    temperature and `T` for tool. The fixed `V35` has no established meaning and is
    deliberately not guessed at here.

```gcode
G427 R2 P3 ; Calibrate all used and mapped tools

T{initial_tool} S1 L0 D0
```

`G427` runs the full tool offset calibration for every mapped tool: it works out which
physical tools the print needs, calibrates each in XYZ, and writes the results to
runtime variables and EEPROM.

Its two parameters are both about accuracy. `R` is millimeters of random jitter applied
to X and Y while Z-probing each tool, which stops every probe landing on exactly the
same spot. `P` is how many Z probes to take per point and average. So `R2 P3` means
jitter by two, average three.

This is the step that fails on machines with a bad offset sensor — see
[tool offset calibration fails](../issues/offset-sensor-board-failure.md).

`T{initial_tool} S1 L0 D0` then picks the tool the print actually starts with.

### Chamber soak, heat soak and mesh bed leveling

```gcode
{if chamber_minimal_temperature[initial_tool] != 0}
  ; Min chamber temp section
  M104 S0
  M140 S115 ; set bed temp for chamber heating
  G1 Z10 F720 ; set bed position
  G1 X242 Y0 F4800 ; set print head position
  M191 S{chamber_minimal_temperature[initial_tool]} ; wait for minimal chamber temp
  M141 S{chamber_temperature[initial_tool]} ; set nominal chamber temp
  M140 S{first_layer_bed_temperature[initial_tool]} ; set bed temp
{endif}

{if first_layer_bed_temperature[initial_tool] <= 60}M106 S70{endif}
G0 Z40 F10000
M104 S{if is_nil(idle_temperature[initial_tool])}100{else}{idle_temperature[initial_tool]}{endif}
M190 R{first_layer_bed_temperature[initial_tool]} ; wait for bed temp
M107

G29 G ; absorb heat

M109 S{probe_temp} ; wait for temp
```

The chamber section is the counterpart to the conditional near the top: it only runs for
filaments that declare a minimum chamber temperature. The technique is to drive the bed
hot and park the head low and to one side, using the bed as a chamber heater, then wait
on `M191` for the chamber to come up before restoring the real bed target.

Outside that, a cool bed target gets some part-cooling fan to help it settle, the nozzle
drops to an idle temperature while waiting, and `M107` turns the fan off before probing.

`G29 G` is a heat-soak step — it holds while the machine comes to thermal equilibrium,
which matters because probing a cold frame and printing on a hot one gives different
answers.

`M109 S{probe_temp}` then brings the nozzle to the probing temperature worked out at the
very top of the file, and waits for it.

```gcode
;
; MBL
;
M84 E ; turn off E motor
G29 P1 ; invalidate mbl & probe print area
;G29 P1 X150 Y0 W100 H20 C ; probe near purge place
G29 P3.2 ; interpolate mbl probes
G29 P3.13 ; extrapolate mbl outside probe area
G29 A ; activate mbl

G0 Z1 ; add Z clearance

M569 S0 E ; set spreadcycle mode for extruder
G92 E0 ; reset extruder position
```

Mesh bed leveling, in stages. `M84 E` de-energizes the extruder motor first so it
cannot creep and disturb a reading. `G29 P1` throws away any existing mesh and probes
the print area — the area declared by `M555` earlier. `P3.2` interpolates between the
probed points, `P3.13` extrapolates the mesh outward past the probed region so travel
outside the print area still has a defined Z, and `G29 A` activates the result.

The commented-out line is an alternative that probes near the purge area instead.

`M569 S0 E` puts the extruder driver into spreadcycle rather than stealthchop — less
quiet, more predictable torque, which is what you want for an extruder rather than a
gantry axis.

### Clean and prime the initial tool

```gcode
;-------Clean and prime initial tool------
{
local speed_tc = min(travel_speed, 350.0) * 60;
local deretract_length = 1.6;
local target_temp = first_layer_temperature[initial_tool];
local eject_temp = max(160,target_temp - 60);
local filament_area = 3.14 * filament_diameter[initial_tool] * filament_diameter[initial_tool] / 4.0;
local purge_mm = 12 / filament_area;
local purge_speed_fast = 60.0 * min(6,max(1.5,0.6*filament_max_volumetric_speed[initial_tool]/filament_area));
local purge_speed_slow = 60.0 * min(3,max(1.5,0.3*filament_max_volumetric_speed[initial_tool]/filament_area));
local tc_deretract_speed = 60.0 * min(20,max(5,deretract_speed[initial_tool]));
}

M83
G1 F{speed_tc}
M204 S7000
M104 S{eject_temp+15}
G12 S90 ; enter cleaner
M109 C{eject_temp} ; Skip residency
M104 S{target_temp + 5}
G12 S30 ; eject poop
M106 S{255 / 100 * max_fan_speed[initial_tool]}
M906 P1 ; Set extruder current
M109 C{target_temp}
M104 S{target_temp}
G1 E{deretract_length} F{tc_deretract_speed}

G91 ; use relative coordinates
M83 ; extruder relative mode
M572 S0.0 ; Disable PressureAdvance

;FLUSH_START
G1 X-0.2 E{0.15 * purge_mm} F{0.20 / (0.15 * purge_mm) * purge_speed_slow}
G1 X0.40 E{0.30 * purge_mm} F{0.40 / (0.30 * purge_mm) * purge_speed_slow}
G1 Y-0.5 E{0.10 * purge_mm} F{0.50 / (0.10 * purge_mm) * purge_speed_slow}
G1 Y-0.5 E{0.10 * purge_mm} F{0.50 / (0.10 * purge_mm) * purge_speed_fast}
G1 X-0.4 E{0.20 * purge_mm} F{0.40 / (0.20 * purge_mm) * purge_speed_fast}
G1 Y1.00 E{0.18 * purge_mm} F{1.00 / (0.18 * purge_mm) * purge_speed_fast}
G1 X0.20 E{0.05 * purge_mm} F{0.20 / (0.05 * purge_mm) * purge_speed_fast}
G1 Y0.20 E{0.02 * purge_mm} F{0.20 / (0.02 * purge_mm) * purge_speed_slow}
;FLUSH_END

M400
M906 P0 ; Revert extruder current
G1 Y0 E-{retract_length[initial_tool] + 0.04} F{retract_speed[initial_tool] * 60}
{e_retracted[initial_tool] = retract_length[initial_tool] + retract_restart_extra_toolchange[initial_tool]}
G1 Y5 F{speed_tc}

{tool_init[initial_tool] = 1}
G90 ; use absolute coordinates
M83 ; extruder relative mode
G12 S91 ; Exit cleaning station
G0 Z1.2 ; Lift
G4 S0
M221 S100 ; set flow to 100%
```

This section deliberately mirrors the tool change block, so the first tool starts the
print in the same state a swapped-in tool would.

**The cleaning station** is driven by `G12` with a sub-code. `S90` enters it, `S30`
ejects the accumulated purge material, `S91` exits. Everything between `S90` and `S91`
happens with the head parked at the station rather than over the bed.

**The two-stage temperature approach** is the part worth copying. `eject_temp` is set
well below the print temperature. The nozzle is brought *down* to that before ejecting,
because material that has cooled somewhat detaches from the tip as a solid pellet rather
than stringing. Only after the eject does it come up to printing temperature.

`M109 C` rather than `M109 S` is what makes this practical. The `C` form waits for the
temperature to be reached but skips the residency period a normal `M109 S` enforces, so
each of these waits costs seconds rather than tens of seconds. The profile's own comment
says exactly that.

**`M906 P1` … `M906 P0`** raises the extruder motor current for the purge and puts it
back afterwards, because pushing a large volume quickly asks more of the motor than
printing does.

**The flush pattern** is eight short moves in X and Y, each extruding a stated fraction
of `purge_mm`. The feedrates are computed rather than fixed: each is *distance ÷ extrusion
÷ speed*, which keeps the head's linear speed matched to the extrusion so the purge lays
down consistently instead of stretching or bunching. The pattern alternates direction to
break the strand up.

`M572 S0.0` disables pressure advance for the purge — its whole purpose is to smooth
transitions, which is unwanted when you are deliberately pushing a fixed volume.

`M400` waits for the move queue to drain before the current is reverted, so the change
does not land mid-move.

!!! important "The last interesting line is `{tool_init[initial_tool] = 1}`"
    That marks the starting tool as already cleaned and primed. Nothing in this block
    uses it — the tool change block does, and it changes behavior in two ways.

    A tool whose `tool_init` is still `0` gets a fixed deretract length instead of the
    computed one, and is forced down the purge-station path **even if a wipe tower is
    configured**. That is deliberate: a tool that has never been primed needs a proper
    purge, and a wipe tower is not the place to do it.

    So this single assignment is the difference between the first tool change behaving
    like a normal one and behaving like a first-time initialization. If you rewrite this
    section, carry that line across.

## Before layer change

```gcode
;BEFORE_LAYER_CHANGE
G92 E0.0
;[layer_z]
{if layer_z > 150}
M201 X{interpolate_table(layer_z, (0,7000), (150,7000), (200,4500), (270,2000))} Y{interpolate_table(layer_z, (0,7000), (150,7000), (200,4500), (270,2000))}
{endif}
```

`G92 E0.0` resets the extruder's position counter each layer, keeping the numbers small.

The rest is the most interesting idea in the profile: **acceleration is reduced as the
print gets taller**. `interpolate_table` takes the current layer height and interpolates
between the given points, so X and Y acceleration stays flat up to a threshold and then
falls away steadily toward the top of the build volume.

The reasoning is mechanical. A tall part is a lever — the taller it gets, the more a
given acceleration deflects the top of it, and the more the machine's own frame flexes.
Reducing acceleration with height trades print time for accuracy exactly where the
trade is worth making, and leaves short prints untouched.

The `{if layer_z > 150}` guard means nothing is emitted at all below the flat region, so
a short print carries no extra G-code.

This connects to a wider community view that stock accelerations on this machine sit
high for its motors, and to
[diagonal banding](../issues/diagonal-banding.md), where extrusion and motion artifacts
have to be told apart.

## After layer change

```gcode
;AFTER_LAYER_CHANGE
;[layer_z]

; dock fan control
{if layer_num == 1 or layer_num == 3}
  M106 P6 S0 ; dock fan off (baseline)
  {if used_tools > 1}
    ;PET-family (PET/PETG/*-CF...)/CPE/PCTG - dock fan 100 from 3rd layer
    {if layer_num == 3 and ((is_extruder_used[0] and filament_type[0]=~/(PET|CPE|PCTG)/) or ...)}
      M106 P6 S100
    {endif}

    ;low-temp materials - dock fan 100% (S255) from 1st layer (uses global low_temp_types)
    {if (is_extruder_used[0] and one_of(filament_type[0], ~low_temp_types)) or ...}
      M106 P6 S255
    {endif} ; PLA wins by order
  {endif}
{endif}
```

*(the per-tool conditions are elided — each expands to all eight tools)*

`M106 P6` addresses the **dock fan**, not the part-cooling fan. The `P` index selects a
fan, and index 6 is the dock fan, which exists only on INDX builds. A bare `M106 S…`
elsewhere in the profile is the part fan.

The logic only fires on layers 1 and 3, and only when more than one tool is in use — a
single-tool print has nothing docked to cool.

Tracing it through:

- **Layer 1** — baseline off, then the PET branch is skipped because it requires layer 3,
  so only the low-temperature branch can fire. Low-temperature materials get full dock
  fan from the very first layer.
- **Layer 3** — baseline off, then the PET branch may set partial dock fan, and the
  low-temperature branch may then overwrite it with full.

That ordering is intentional, and the profile's own comment records it: *PLA wins by
order*. Where a plate mixes both, the low-temperature setting is the one that survives.

!!! note "`S100` is not 100 percent"
    `M106` takes a PWM value from 0 to 255, so `S255` is full and `S100` is about 39%.
    The comment on the PET branch reads "dock fan 100", meaning the raw value — it is
    easy to read that as a percentage and conclude the two branches do the same thing.
    They do not.

The reason low-temperature materials want dock cooling earliest is that they soften
nearest to ambient, so a tool sitting in its dock beside a heated chamber is most at
risk of the filament in it going soft.

## Tool change

```gcode
  G1 F{speed_tc}
  M204 S7000

  G27 W3 Z{travel_max_lift[current_extruder]} P2 R{retract_toolchange} V{tc_retract_speed/60} A{travel_slope[current_extruder]}
  P0 S1 L0 D0

  T{next_extruder} S1 L0 D0

  M104 S{eject_temp+15}
  G12 S90 ; enter cleaner
  G0 Z{layer_z + 0.8} ; Lift
  M109 C{eject_temp} ; Skip residency
  M104 S{target_temp + 5}
```

The setup block above this (elided for length) computes the same locals as the prime
section, plus a few branches: a zero configured purge falls back to a fixed volume, an
explicit flush volume or speed overrides the computed one, FLEX gets its own retract and
deretract speeds, and — as described above — an uninitialized tool gets a fixed deretract
length and is forced down the purge-station path.

There is also a first-layer override: if the layer is at or below first-layer height, the
target temperature becomes the first-layer temperature rather than the normal one.

**`G27` is the park**, and its parameters are worth reading carefully:

| Parameter | Meaning |
|---|---|
| `W3` | Use the predefined **tool park** position (toolchangers only) |
| `Z…` | Z component of the park position |
| `P2` | Z action: **relative move by Z** |
| `R…` | Distance to retract during the parking moves |
| `V…` | Retraction feedrate, independent of the move feedrate |
| `A…` | Do the Z move *in parallel* with XY, at this angle, until target Z is reached |

The `A` parameter is a nice touch — instead of lifting and then traveling, the head
climbs on a slope while it moves, which is faster.

`P0 S1 L0 D0` then drops the current tool in its dock, and `T{next_extruder} S1 L0 D0`
picks up the new one.

```gcode
    G12 S30 ; eject poop
    M106 S{255 / 100 * max_fan_speed[next_extruder]}
    M906 P1 ; Set extruder current
    M109 C{target_temp}
    M104 S{target_temp}
    G1 E{deretract_length} F{tc_deretract_speed}

    G91 ; use relative coordinates
    M83 ; extruder relative mode
    M572 S0.0 ; Disable PressureAdvance

    ;FLUSH_START
    G1 X-0.2  E{0}                F{1200}
    G1 X0.40  E{0.15 * purge_mm}  F{0.40 / (0.15 * purge_mm) * purge_speed_slow}
    G1 Y-1.20 E{0.35 * purge_mm}  F{1.20 / (0.35 * purge_mm) * purge_speed_fast}
    G1 X-0.4  E{0.20 * purge_mm}  F{0.40 / (0.20 * purge_mm) * purge_speed_fast}
    G1 Y1.20  E{0.25 * purge_mm}  F{1.20 / (0.25 * purge_mm) * purge_speed_fast}
    G1 X0.20  E{0.05 * purge_mm}  F{0.20 / (0.05 * purge_mm) * purge_speed_fast}
    ;FLUSH_END

    M400
    M906 P0 ; Revert extruder current
    G1 Y0 E-{retract_length[next_extruder] + 0.04} F{retract_speed[next_extruder] * 60}
    G1 Y5 F{speed_tc}
```

The purge-station path, taken when there is no wipe tower or when the incoming tool has
never been primed. It is the same shape as the prime sequence in the start block: eject
cold, fan on, current up, come to temperature, deretract, flush in a computed pattern,
retract, current back.

The wipe-tower path instead issues a series of `G750` moves, which run the wipe-tower
sequence with the tower's own geometry, and skips the station entirely.

```gcode
  G90 ; use absolute coordinates
  M83 ; extruder relative mode
  G12 S91 ; Exit cleaning station
  G0 Z{layer_z + 1.0} ; Lift
  G4 S0
```

!!! danger "Both lifts in this block are layer-relative"
    `G0 Z{layer_z + 0.8}` on the way in and `G0 Z{layer_z + 1.0}` on the way out are both
    computed from the *current layer height*. Neither consults the height of anything
    already finished on the plate. The park itself uses `P2`, a relative Z move, rather
    than `P0`, which is the option documented as "raise to at least Z above print".

    On an ordinary print every object rises together, so the current layer is the tallest
    thing on the bed and this is fine. On a **sequential print** it is not: a finished
    object can stand far above the layer being printed elsewhere, and a travel computed
    from the current layer passes straight through it.

    That is the mechanism behind
    [toolhead collides with finished parts](../issues/complete-individual-objects-collision.md).
    Reading this block makes it concrete in a way the community bug report could not: the
    clearance-aware option exists in the firmware and this profile does not use it.

    **This is not a suggested fix.** Whether `P0` would actually resolve it depends on
    what the firmware means by "above print" — whether it tracks completed object heights
    or only the current one — which has not been established. It is the first thing to
    investigate, not a change to make blind.

    TODO(verify): whether `G27 P0` accounts for completed objects on a sequential print,
    and whether the two `G0 Z{layer_z + …}` lifts can be made clearance-aware.

## End G-code

```gcode
{if layer_z < max_print_height}G1 Z{z_offset+min(max_layer_z+1, max_print_height)} F720 ; Move print head up{endif}

; turn off extruder heaters
{if is_extruder_used[0]}M104 T0 S0{endif}
{if is_extruder_used[1]}M104 T1 S0{endif}
{if is_extruder_used[2]}M104 T2 S0{endif}
{if is_extruder_used[3]}M104 T3 S0{endif}
{if is_extruder_used[4]}M104 T4 S0{endif}
{if is_extruder_used[5]}M104 T5 S0{endif}
{if is_extruder_used[6]}M104 T6 S0{endif}
{if is_extruder_used[7]}M104 T7 S0{endif}

M140 S0 ; turn off heatbed
M141 S0 ; disable chamber control
M107 ; turn off fan
M106 P6 S0 ; turn off dock fan

P0 S1 ; park tool

G1 X242 Y205 F10200 ; park
G4 ; wait
M572 S0 ; reset PA
M221 S100 ; reset flow percentage
M84 X Y E ; disable motors
M77 ; stop print timer
; max_layer_z = [max_layer_z]
```

The bed drops away first, guarded so it cannot try to exceed the machine's maximum.

Heaters are turned off per tool rather than globally — `M104 T<n> S0` addresses a
specific tool, and only tools actually used are touched. Then bed, chamber, part fan and
dock fan.

`P0 S1` returns the tool to its dock. Leaving a tool on the head at the end would mean
starting the next print with an unexpected state.

`G4` with no argument waits for the queue to drain. `M572 S0` and `M221 S100` reset
pressure advance and flow so a later print does not inherit them — worth doing because
both persist in firmware across prints.

`M84 X Y E` disables the X, Y and extruder motors but deliberately leaves Z energized, so
the bed holds its position rather than sagging.

## Command reference

Behavior verified against the Prusa firmware source unless marked otherwise.

| Command | What it does |
|---|---|
| `M862.1 T P A F` | Declare per-tool nozzle: tool, diameter, abrasive flag, high-flow flag |
| `M862.3 P"model"` | Printer model gate |
| `M862.5 P<n>` | G-code dialect level gate |
| `M862.6 P"feature"` | Required firmware feature gate |
| `M115 U<ver>` | Declare the firmware version the file targets |
| `M555 X Y W H` | Declare the print area |
| `M591 S<0\|1>` | Filament stuck detection off/on |
| `G28 XY` / `G28 Z` | Home the named axes |
| `T<n> S L D` | Select a tool |
| `P0 S1 [L D]` | Park the current tool in its dock |
| `G27 W Z P R V A` | Park the head; see the table above for parameters |
| `G427 R P` | Tool offset calibration; `R` jitter mm, `P` probes averaged |
| `G29 G` | Heat-soak / absorb heat |
| `G29 P1` | Invalidate the mesh and probe the print area |
| `G29 P3.2` | Interpolate between probed points |
| `G29 P3.13` | Extrapolate the mesh beyond the probed area |
| `G29 A` | Activate the mesh |
| `G12 S90` | Enter the cleaning station |
| `G12 S30` | Eject accumulated purge material |
| `G12 S91` | Exit the cleaning station |
| `G750 Y F A` | Wipe-tower move |
| `M104 S` / `M104 T<n> S` | Set nozzle target, current tool or a named one, no wait |
| `M109 S` | Set nozzle target and wait, including residency |
| `M109 C` | Set nozzle target and wait, **skipping residency** |
| `M140 S` / `M190 R` | Bed target / wait for bed |
| `M141 S` / `M191 S` | Chamber target / wait for chamber |
| `M106 S` | Part-cooling fan, PWM 0–255 |
| `M106 P6 S` | **Dock fan**, PWM 0–255 |
| `M107` | Part-cooling fan off |
| `M204 S` | Set acceleration |
| `M201 X Y` | Set per-axis maximum acceleration |
| `M221 S` | Flow percentage |
| `M572 S` | Pressure advance; `S0` disables |
| `M569 S0 E` | Extruder driver to spreadcycle |
| `M906 P<0\|1>` | Extruder current: raised for purging, reverted after |
| `M400` | Wait for the move queue to drain |
| `M84 [axes]` | Disable the named motors |
| `M77` | Stop the print timer |
| `M262 P B` | IO expander pin direction — `B0` output, `B1` input |
| `M264 P B` | IO expander pin level — `B0` low, non-zero high |
| `M574 S V T F` | **Not implemented** — no handler; logged as unknown and skipped |

## Verification

`measured` — this is Prusa's shipped profile for firmware 6.9.0, reproduced verbatim
rather than reconstructed, and every command's behavior was checked against the
firmware handler that implements it rather than assumed from standard Marlin.

That provenance is what earns the tier. These are not one owner's settings that happened
to work; they are the vendor's defaults, which every INDX on this firmware starts with.
The values are therefore general in a way the rest of this site's numbers are not — which
is also why they appear here at all, when the site otherwise withholds print settings
until someone has verified them on hardware.

Where a command's meaning could not be established it is marked as such rather than
guessed. `M574` is the only one in that state, and the distinction matters: its *absence*
from the firmware is now established to the same standard as the other commands'
presence — checked against the v6.9.0 release tag and every object in the public
repository's history, with positive controls. What it was intended to do is still
unknown, and is flagged in place rather than reconstructed. Prusa's August 2026
announcement of load-cell pressure advance calibration is first-party and cited, but
nothing published connects it to this command; the page keeps the two apart deliberately.

`M262` and `M264` deserve a note. They are frequently described as chamber-light
commands, and the profile they came from labeled them that way. They are not: the
firmware implements them as generic I2C GPIO expander operations — configure a pin
direction, write a pin level. What a given pin controls is whatever the owner has wired
to it. Anything you read that treats them as a lighting command is describing a
convention, not the command.

What is *not* verified: whether these defaults are *good*. They are what Prusa ships,
which makes them authoritative as a description and says nothing about whether a given
value is optimal for your filament or your part. Several are actively disputed by
owners — stock temperatures and accelerations both come up on the forum as running high
for this toolhead. Reproducing a default is not endorsing it.

Nor is the profile static. It changes across firmware releases: the 6.6.3 version had a
misspelled variable in the probe-temperature expression, used a different offset for PC
and PA, omitted the `low_temp_types` global that the after-layer-change block depends on,
and included chamber-light commands this one drops. If your firmware differs from the
version in the front matter, expect differences.

## Related

- [Toolhead collides with finished parts](../issues/complete-individual-objects-collision.md)
  — the tool change block's layer-relative lifts, in context
- [Oozing spoils bed probing](../issues/oozing-during-probing-and-calibration.md) — why
  the probe temperature is computed the way it is
- [Tool offset calibration fails](../issues/offset-sensor-board-failure.md) — what
  happens when `G427` cannot complete
- [Blobs dragged into the print](../issues/stringing-and-wiper-calibration.md) — the
  purge and cleaning behavior these blocks drive
