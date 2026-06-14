# Project status

## Current version

v4C audit-driven engineering candidate.

## What changed in v4C

- LogicBoard footprint changed from wrong DIP-8 placeholder to URB ZP-style DIP24 populated-pin footprint.
- LogicBoard U1 pins now map to: 2,3 = GND_IN; 11 = NC; 14 = OUT_12V; 16 = GND_OUT; 22,23 = VIN_24V. Pin 9 is intentionally absent.
- LogicBoard input capacitor changed to 100uF/50V plus 1uF HF footprint per audit consensus.
- PowerBoard URF pin drills corrected: pins 1,2,3,5,6,7 use 1.5mm drill; pins 4 and 8 use 2.0mm drill.
- PowerBoard output terminal pads enlarged and marked as 30A-class footprint target.
- PowerBoard fuse label changed from 20A default to 10A slow/link candidate on input side.
- PowerBoard precharge block is marked SIZE_BY_C_BANK, not final electrical value.
- PowerBoard external bypass header added for relay/MOSFET bypass concept.
- PowerBoard TVS footprint changed to SELECT/DNP default because SMDJ7.0A is not sufficient as supercap over-voltage protection.
- BOM and manufacturing notes are in progress after audit ingestion.

## Current confidence

- LogicBoard: 70/100 as PCB architecture. Main remaining blockers: exact official footprint coordinate check, KiCad ERC/DRC, Gerber review.
- PowerBoard: 55/100 as PCB architecture. Main remaining blockers: supercap precharge design, official footprint coordinate check, thermal/current verification, KiCad ERC/DRC, Gerber review.

## Blocking items before fab-ready release

1. Physical or official footprint verification for both Mornsun modules.
2. KiCad ERC on real schematic, not text placeholders.
3. KiCad DRC on PCB with 0.30mm clearance and real fab constraints.
4. Gerber and Excellon export.
5. Independent Gerber viewer check.
6. Real supercap bank capacitance, ESR and allowed charge current.
7. Precharge resistor / relay / MOSFET sizing and thermal validation.
8. 20A output connector part number and current rating confirmation.
9. Human EE review before production order.

## Hard warning

Current v4C files are much closer to a responsible engineering candidate, but still not a blind-order manufacturing release. The largest remaining technical risk is the PowerBoard use case: charging supercapacitors from a 5V/20A module whose maximum capacitive load is reported by auditors as 6000uF. A supercapacitor bank is orders of magnitude larger and must be isolated by a controlled precharge stage.
