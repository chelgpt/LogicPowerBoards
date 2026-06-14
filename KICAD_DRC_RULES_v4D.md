# KiCad DRC rules v4D

## Board stack

- Layers: 2 copper layers.
- Copper weight: 2oz.
- Board thickness: 1.6mm unless enclosure demands otherwise.
- Board outline: 50 x 100mm.

## Global rules

- Minimum clearance: 0.30mm.
- Minimum track width for signal nets: 0.25mm.
- Preferred signal width: 0.35mm.
- Minimum via drill: avoid below 0.30mm unless fab selected.
- Annular ring: use fab default or larger.

## PowerBoard net classes

### Input power

Nets: VIN_24V, GND_IN, VIN_AFTER_F1, VIN_TO_MODULE.

- Preferred routing: pours or wide traces.
- Minimum width if trace-only: 5mm for high-current sections.
- Keep routing short between J_IN, F1, R_LIMIT, U1.

### Output power

Nets: OUT_5V, OUT_0V.

- Preferred routing: copper pours, not narrow traces.
- Minimum equivalent copper width: 10-15mm.
- Thermal relief: off for module output pins and output terminal pads.
- If top and bottom copper share current, use via stitching.
- Avoid bottlenecks at terminal pads and module pins.

### Sense and trim

Nets: SENSE_P, SENSE_N, TRIM.

- Width: 0.25-0.35mm.
- Route separately from high-current copper.
- Kelvin route sense lines to output connector or close fallback jumpers.
- Do not allow floating sense nets.

### Ctrl

Net: CTRL.

- Reference to GND_IN only.
- Keep away from OUT_0V assumptions.

## LogicBoard net classes

- VIN_24V and GND_IN: 0.8-1.2mm preferred.
- OUT_12V and GND_OUT: 0.8-1.2mm preferred.
- Keep input and output domains separated.

## Required DRC review points

- Board outline closed.
- No unconnected pads unless explicitly NC.
- No copper crossing isolation boundary unnecessarily.
- No thermal relief on high-current pads.
- Drill sizes match module pins.
- Silkscreen does not overlap pads.
- Polarity marks visible after assembly.
