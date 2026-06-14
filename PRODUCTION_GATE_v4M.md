# Production gate v4M

## Gate result today

- LogicBoard: engineering prototype candidate, not final production release until ERC/DRC/Gerber pass.
- PowerBoard: engineering candidate, blocked by supercap/precharge/load data and ERC/DRC/Gerber pass.

## What can be considered ready

The repository is ready for automated validation and fabrication package generation attempts.

## What is not ready

The repository is not ready for blind PCB factory order.

## LogicBoard release path

LogicBoard can move to private prototype order after all of the following are true:

1. Text validation passes.
2. KiCad ERC passes.
3. KiCad DRC passes.
4. Gerber and drill files are generated.
5. Gerbers are reviewed.
6. Official URB2412ZP-6WR3 footprint coordinates are checked.

## PowerBoard release path

PowerBoard can move to private prototype order after all LogicBoard-style fabrication gates plus:

1. Real C_bank is known.
2. Real bank ESR is known.
3. Allowed charge current is known.
4. R_LIMIT value and pulse rating are selected.
5. Bypass relay/MOSFET strategy is selected.
6. Output connector part number and current rating are selected.
7. Thermal behavior is acceptable in bench test.

## Decision matrix

| Condition | LogicBoard | PowerBoard |
|---|---:|---:|
| Schematic exists | yes | yes |
| PCB exists | yes | yes |
| BOM current | yes | yes |
| Testpoints | yes | yes |
| Mounting holes | yes | yes |
| Text validator | present | present |
| ERC result | pending | pending |
| DRC result | pending | pending |
| Gerbers | pending | pending |
| Official footprint coordinates | pending | pending |
| Load/precharge closure | not needed | pending |

## Final instruction

Do not call this production-ready until pending rows are closed.
