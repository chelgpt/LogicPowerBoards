# Project status

## Current version

v4F schematic generation iteration.

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

## What changed in v4F

- Replaced LogicBoard text-only schematic placeholder with a component-level KiCad schematic generated from NETLIST_LOCK_v4E.
- Replaced PowerBoard text-only schematic placeholder with a component-level KiCad schematic generated from NETLIST_LOCK_v4E.
- LogicBoard schematic now shows J1, U1, C1, C2, C3, C4, J2 and J3 with corrected URB ZP pin naming.
- PowerBoard schematic now shows J_IN, F1, R_LIMIT, J_BYP, U1, C_IN, C_OUT, JP_S+, JP_S-, J_OUT and J_CTRL.

## Current confidence

- LogicBoard: 82/100 as PCB architecture. Main remaining blockers: exact official footprint coordinate check, automated KiCad ERC/DRC, Gerber review.
- PowerBoard: 68/100 as PCB architecture. Main remaining blockers: capacitive-load precharge design, official footprint coordinate check, thermal/current verification, automated KiCad ERC/DRC, Gerber review.

## Blocking items before fab-ready release

1. Physical or official footprint verification for both Mornsun modules.
2. Automated KiCad ERC on the v4F schematic.
3. Automated KiCad DRC on PCB with 0.30mm clearance and real fab constraints.
4. Gerber and Excellon export.
5. Independent Gerber viewer check.
6. Real capacitive-load data: capacitance, ESR and allowed charge current.
7. Precharge resistor / relay / MOSFET sizing and thermal validation.
8. 20A output connector part number and current rating confirmation.
9. Human EE review before production order.

## Hard warning

Current v4F files are no longer only PCB drawings: they now include component-level schematic files. The largest remaining technical risk is still the PowerBoard use case: charging a large capacitive bank from a 5V/20A module. That load must be isolated by a controlled precharge stage and verified on the bench.
