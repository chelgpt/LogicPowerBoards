# Fab readiness scorecard v4F

## Scoring model

100 means ready to generate Gerbers for a private prototype order after final visual review and automated KiCad ERC/DRC results.

## LogicBoard

Current score: 82/100.

Closed:

- Corrected away from wrong DIP8 placeholder.
- Uses URB ZP DIP24 populated-pin map in PCB.
- Input/output capacitor values aligned to audit consensus.
- Net classes and 0.30mm clearance configured in project file.
- DRC rules and release gates documented.
- Browser review workflow works.
- v4F component-level schematic generated from NETLIST_LOCK_v4E.

Remaining:

- Exact official Mornsun footprint coordinate check.
- Automated KiCad ERC output.
- Automated KiCad DRC output.
- Gerber and drill export.
- Independent Gerber viewer check.

## PowerBoard

Current score: 68/100.

Closed:

- URF pin drill sizes corrected.
- Output terminal enlarged to 30A-class target footprint.
- Input fuse candidate corrected to 10A slow/link class.
- Precharge block separated from final value selection.
- External bypass header added for relay or MOSFET bypass concept.
- TVS changed to selectable footprint rather than final fixed assumption.
- Net classes configured: power input, power output 20A, sense/trim/ctrl.
- DRC rules and precharge requirements documented.
- v4F component-level schematic generated from NETLIST_LOCK_v4E.

Remaining:

- Exact official Mornsun footprint coordinate check.
- Real supercap data: capacitance, ESR, allowed charge current, cycle rate.
- R_LIMIT value and pulse rating.
- Bypass relay/MOSFET part selection and timing.
- Thermal check for 20A operation and module cooling.
- Automated KiCad ERC output.
- Automated KiCad DRC output.
- Gerber and drill export.
- Independent Gerber viewer check.

## Next gate

v4G should add an automated validation/export path. Preferred route: GitHub Actions job using kicad-cli to run ERC, DRC and plot fabrication outputs when KiCad CLI is available in the runner/container.
