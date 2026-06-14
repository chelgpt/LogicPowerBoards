# Project status

## Current version

v4L engineering freeze.

## What changed in v4K

- PowerBoard PCB includes M3 mounting holes.
- PowerBoard PCB includes testpoints: TP_VIN, TP_GNDIN, TP_5V, TP_0V, TP_TRIM, TP_S+, TP_S-.
- PowerBoard silkscreen includes stronger guards: no-copper-under-module, remote-sense warning, precharge-first warning, input/output labels.
- LogicBoard PCB includes M3 mounting holes.
- LogicBoard PCB includes testpoints: TP1_24V, TP2_GND, TP3_12V, TP4_0V.
- Validator requires v4K testpoints, mounting holes and board marks.
- Added FAB_READINESS_SCORECARD_v4K.md.

## What changed in v4L

- Added ENGINEERING_FREEZE_v4L.md.
- Stopped speculative repo churn until CI logs, generated Gerbers, official footprint coordinates or real PowerBoard load data are available.

## Current confidence

- LogicBoard: 88/100 as PCB architecture before automated ERC/DRC. Close to private prototype candidate after clean ERC/DRC and footprint-coordinate check.
- PowerBoard: 76/100 as PCB architecture before automated ERC/DRC and precharge closure. Not blind-order production-ready until real capacitive-bank/precharge data are closed.

## Stop condition

Do not continue layout iterations without one of these inputs:

1. GitHub Actions text-validation failure log.
2. GitHub Actions KiCad ERC/DRC/export failure log.
3. Generated fabrication-output artifact.
4. Official Mornsun footprint coordinate file or drawing extraction.
5. Real PowerBoard capacitive-bank data: capacitance, ESR, allowed charge current, duty cycle.
6. Selected 20A output connector part number.

## Hard warning

This is an engineering freeze, not a production release. Continuing blind edits now would be fake progress. The next meaningful move is validation, not more speculative changes.
