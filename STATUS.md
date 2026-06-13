# Project status

## Current version

v4B engineering candidate.

## Current confidence

- LogicBoard: medium-high after official footprint/pinout verification and DRC/ERC.
- PowerBoard: medium only until official URF2405QB-100WR3 footprint/pinout, inrush strategy and 20A copper geometry are verified.

## Completed in current iteration

- GitHub Pages/KiCanvas review workflow is active.
- Main page has board tabs.
- v3 critique and remake plan added.
- PowerBoard PCB upgraded to functional v4A/v4B architecture.
- LogicBoard PCB upgraded to functional v4A/v4B architecture.
- BOM drafts added for both boards.
- Manufacturing notes and validation gates added.

## Blocking items before 90-100% fab-ready release

1. Official Mornsun datasheet and footprint verification for both modules.
2. KiCad ERC on real schematic.
3. KiCad DRC on PCB.
4. Gerber and Excellon export.
5. Independent Gerber viewer check.
6. Inrush/precharge resistor or bypass strategy calculation from actual supercap capacitance.
7. Connector current rating confirmation for 20A output.

## Next engineering iteration

v4C:

- Add/update full testpoint set on PowerBoard: Trim, Sense+, Sense-.
- Add trim resistors R_TRIM_L/R_TRIM_H explicitly to PCB.
- Add output HF capacitor footprint.
- Add mounting holes.
- Add clearer silkscreen polarity and warnings.
- Add stronger copper zone definitions if KiCanvas/KiCad parsing remains stable.
