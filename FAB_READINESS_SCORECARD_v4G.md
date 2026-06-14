# Fab readiness scorecard v4G

## Scoring model

100 means ready to order private-use prototype boards from generated Gerbers after final visual review. v4G adds automated validation/export pipeline, but final score depends on CI results.

## LogicBoard

Current score: 84/100 before CI results.

Closed:

- Corrected away from wrong DIP8 placeholder.
- Uses URB ZP DIP24 populated-pin map in PCB.
- Input/output capacitor values aligned to audit consensus.
- Net classes and 0.30mm clearance configured in project file.
- DRC rules and release gates documented.
- Browser review workflow works.
- v4F component-level schematic generated from NETLIST_LOCK_v4E.
- v4G CI pipeline added for text validation, KiCad ERC, DRC, Gerber and drill export.

Remaining:

- GitHub Actions text validation result.
- KiCad ERC result.
- KiCad DRC result.
- Gerber/drill artifact review.
- Exact official Mornsun footprint coordinate check.

## PowerBoard

Current score: 70/100 before CI results.

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
- v4G CI pipeline added for text validation, KiCad ERC, DRC, Gerber and drill export.

Remaining:

- GitHub Actions text validation result.
- KiCad ERC result.
- KiCad DRC result.
- Gerber/drill artifact review.
- Exact official Mornsun footprint coordinate check.
- Real supercap data: capacitance, ESR, allowed charge current, cycle rate.
- R_LIMIT value and pulse rating.
- Bypass relay/MOSFET part selection and timing.
- Thermal check for 20A operation and module cooling.

## Next gate

v4H must read the GitHub Actions result. If text validation fails, fix repository-level contradictions. If KiCad ERC/DRC/export fails, fix the exact reported syntax/electrical/manufacturing errors. If CI passes, download fabrication-output and prepare a release package review.
