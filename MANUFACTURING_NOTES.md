# Manufacturing notes / release gates

## Current release state

Current design state: **v4B engineering candidate**, not yet final fab release.

The repo is now structured for browser review and contains functional PCB architecture for both boards, BOM drafts and production checklist. It is still blocked from a responsible 90-100% manufacturing release by official Mornsun footprint/pinout verification and KiCad DRC/ERC/Gerber export.

## Board build assumptions

- Board size: 50 x 100 mm.
- Layers: 2 copper layers.
- Material: FR-4.
- Copper: 2 oz / 70 um.
- Minimum general clearance target: 0.30 mm.
- Input/output isolation target: 3-5 mm or higher where geometry allows.
- PowerBoard output current: up to 20A at 5V.
- LogicBoard output current: about 0.5A at 12V.

## Fabricator order parameters

- FR-4, 1.6 mm thickness unless enclosure requires otherwise.
- 2-layer PCB.
- 2 oz copper.
- HASL lead-free or ENIG. ENIG preferred for reliability if budget allows.
- Soldermask: any; green is lowest risk.
- Silkscreen: white.
- Minimum drill: check against final DRC after official footprints.
- Electrical test: yes.

## PowerBoard critical notes

- 5V/20A routes must be copper pours/planes, not thin traces.
- Thermal relief must be disabled on high-current connector/module pads.
- Output connector must be rated for real 20A current and selected wire gauge.
- Supercapacitor charging requires controlled inrush. R_LIMIT is a placement strategy, not a final electrical solution until capacitance and pulse energy are known.
- Remote sense must not float. Either wire Sense+/Sense- to load, or close fallback jumpers.
- Trim range must be validated on bench before connecting supercapacitors.
- TVS SMDJ7.0A is placed across 5V/0V near output, but final clamping suitability must be checked against module behavior and load.

## LogicBoard critical notes

- Input and output domains must remain isolated.
- Fan connector must match actual harness polarity.
- Capacitors should be placed close to converter pins.

## Required final validation before ordering

1. Download official Mornsun datasheets and footprints for URF2405QB-100WR3 and URB2412ZP-6WR3.
2. Replace/verify current custom footprints.
3. Run KiCad ERC on real schematic.
4. Run KiCad DRC on PCB with 0.30 mm clearance and 2 oz process constraints.
5. Export Gerber + Excellon drill from KiCad.
6. Open Gerbers in independent viewer.
7. Verify drill holes, board outline, polarity marks, terminal orientation and silkscreen.
8. Perform human EE review before production order.

## Bring-up sequence

PowerBoard:

1. Inspect empty board for shorts between input and output domains.
2. Assemble only connectors, fuse/link, input caps, module, output caps and test points first.
3. Do not connect supercapacitors on first power-up.
4. Power from current-limited bench supply.
5. Verify input current, output voltage, Ctrl behavior, and trim range.
6. Verify Sense fallback jumpers before load test.
7. Load-test gradually: 1A, 5A, 10A, 15A, 20A with thermal monitoring.
8. Only then test precharge into actual supercapacitor bank.

LogicBoard:

1. Power from current-limited 24V source.
2. Verify isolated 12V output without load.
3. Test fan/load current.
4. Verify polarity at all terminals.
