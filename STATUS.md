# Project status

## Current version

v4M BOM and production gate pass.

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
- Stopped speculative layout churn until CI logs, generated Gerbers, official footprint coordinates or real PowerBoard load data are available.

## What changed in v4M

- Updated PowerBoard_BOM.csv to match the v4K PCB state and current engineering decisions.
- Updated LogicBoard_BOM.csv to match the v4K PCB state and reject the stale DIP8 assumption.
- Added BOM_AUDIT_v4M.md to reconcile the uploaded BOM/TZ with the current design.
- Added ASSEMBLY_AND_BRINGUP_v4M.md.
- Added PRODUCTION_GATE_v4M.md.
- Fixed validate_repo.py version matcher so v4L/v4M and later statuses do not break CI.

## Current confidence

- LogicBoard: 89/100 as PCB architecture before automated ERC/DRC. Close to private prototype candidate after clean ERC/DRC and footprint-coordinate check.
- PowerBoard: 78/100 as PCB architecture before automated ERC/DRC and precharge closure. Not blind-order production-ready until real capacitive-bank/precharge data are closed.

## Next objective

Continue toward validation output, not cosmetic layout churn:

1. Get text-validation to pass.
2. Run or inspect heavy KiCad ERC/DRC/Gerber workflow.
3. Fix actual reported errors.
4. Produce reviewed fabrication package.

## Hard warning

v4M improves BOM/assembly/readiness closure but is still not a production release. The remaining blockers are validation outputs and PowerBoard load/precharge data.
