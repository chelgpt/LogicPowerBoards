# Project status

## Current version

v4E netlist and DRC lock iteration.

## What changed in v4C

- LogicBoard footprint changed from wrong DIP-8 placeholder to URB ZP-style DIP24 populated-pin footprint.
- LogicBoard U1 pins now map to: 2,3 = GND_IN; 11 = NC; 14 = OUT_12V; 16 = GND_OUT; 22,23 = VIN_24V. Pin 9 is intentionally absent.
- LogicBoard input capacitor changed to 100uF/50V plus 1uF HF footprint per audit consensus.
- PowerBoard URF pin drills corrected: pins 1,2,3,5,6,7 use 1.5mm drill; pins 4 and 8 use 2.0mm drill.
- PowerBoard output terminal pads enlarged and marked as 30A-class footprint target.
- PowerBoard fuse label changed from 20A default to 10A slow/link candidate on input side.
- PowerBoard precharge block is marked SIZE_BY_C_BANK, not final electrical value.
- PowerBoard external bypass header added for relay/MOSFET bypass concept.
- PowerBoard TVS footprint changed to SELECT/DNP default because SMDJ7.0A is not sufficient as load over-voltage protection.

## What changed in v4D

- Added RELEASE_GATES_v4D.md.
- Added KICAD_DRC_RULES_v4D.md.
- Added PowerBoard PRECHARGE_REQUIREMENTS_v4D.md.
- Updated GitHub Pages index to show v4D review state and direct engineering-document links.
- Removed temporary connector test file.

## What changed in v4E

- PowerBoard.kicad_pro now has 0.30mm default clearance and explicit net classes: POWER_INPUT, POWER_OUTPUT_20A, SENSE_TRIM_CTRL.
- LogicBoard.kicad_pro now has 0.30mm default clearance and LOGIC_POWER net class.
- Added NETLIST_LOCK_v4E.md as the locked electrical connectivity reference.
- Added FAB_READINESS_SCORECARD_v4E.md.

## Current confidence

- LogicBoard: 76/100 as PCB architecture. Main remaining blockers: exact official footprint coordinate check, real KiCad schematic, ERC/DRC, Gerber review.
- PowerBoard: 62/100 as PCB architecture. Main remaining blockers: capacitive-load precharge design, official footprint coordinate check, thermal/current verification, real KiCad schematic, ERC/DRC, Gerber review.

## Blocking items before fab-ready release

1. Physical or official footprint verification for both Mornsun modules.
2. Real schematic, not text placeholders.
3. KiCad ERC on the real schematic.
4. KiCad DRC on PCB with 0.30mm clearance and real fab constraints.
5. Gerber and Excellon export.
6. Independent Gerber viewer check.
7. Real capacitive-load data: capacitance, ESR and allowed charge current.
8. Precharge resistor / relay / MOSFET sizing and thermal validation.
9. 20A output connector part number and current rating confirmation.
10. Human EE review before production order.

## Hard warning

Current v4E files are closer to a responsible engineering candidate, but still not a blind-order manufacturing release. The largest remaining technical risk is the PowerBoard use case: charging a large capacitive bank from a 5V/20A module. That load must be isolated by a controlled precharge stage and verified on the bench.
