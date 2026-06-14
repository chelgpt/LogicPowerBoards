# Fab readiness scorecard v4E

## Scoring model

100 means ready to generate Gerbers for a private prototype order after final visual review. Current score is lower because the project still lacks a verified real schematic and automated KiCad DRC/ERC results.

## LogicBoard

Current score: 76/100.

Closed:

- Corrected away from wrong DIP8 placeholder.
- Uses URB ZP DIP24 populated-pin map in PCB.
- Input/output capacitor values aligned to audit consensus.
- Net classes and 0.30mm clearance configured in project file.
- DRC rules and release gates documented.
- Browser review workflow works.

Remaining:

- Exact official Mornsun footprint coordinate check.
- Real schematic file with symbols/wires matching NETLIST_LOCK_v4E.
- KiCad ERC output.
- KiCad DRC output.
- Gerber and drill export.
- Independent Gerber viewer check.

## PowerBoard

Current score: 62/100.

Closed:

- URF pin drill sizes corrected.
- Output terminal enlarged to 30A-class target footprint.
- Input fuse candidate corrected to 10A slow/link class.
- Precharge block separated from final value selection.
- External bypass header added for relay or MOSFET bypass concept.
- TVS changed to selectable footprint rather than final wrong assumption.
- Net classes configured: power input, power output 20A, sense/trim/ctrl.
- DRC rules and precharge requirements documented.

Remaining:

- Exact official Mornsun footprint coordinate check.
- Real schematic file with symbols/wires matching NETLIST_LOCK_v4E.
- Real supercap data: capacitance, ESR, allowed charge current, cycle rate.
- R_LIMIT value and pulse rating.
- Bypass relay/MOSFET part selection and timing.
- Thermal check for 20A operation and module cooling.
- KiCad ERC output.
- KiCad DRC output.
- Gerber and drill export.
- Independent Gerber viewer check.

## Next gate

v4F should generate real KiCad schematics from NETLIST_LOCK_v4E and keep KiCanvas viewer stable.
