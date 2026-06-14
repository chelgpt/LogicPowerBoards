# Fab readiness scorecard v4K

## Scoring model

100 means ready to order private-use prototype boards from generated Gerbers after clean ERC/DRC and final visual review.

## LogicBoard

Current score: 88/100 before automated ERC/DRC.

Closed in v4K:

- Mounting holes added to PCB.
- Testpoints added: TP1_24V, TP2_GND, TP3_12V, TP4_0V.
- Polarity and board-version silkscreen strengthened.
- Validator updated to require LogicBoard testpoints, mounting holes and v4K mark.

Still open:

- Official footprint coordinate check against Mornsun mechanical drawing.
- KiCad ERC result.
- KiCad DRC result.
- Gerber/drill artifact review.

## PowerBoard

Current score: 76/100 before automated ERC/DRC and precharge closure.

Closed in v4K:

- Mounting holes added to PCB.
- Testpoints added: TP_VIN, TP_GNDIN, TP_5V, TP_0V, TP_TRIM, TP_S+, TP_S-.
- Silkscreen guards added: no copper under module, remote sense warning, precharge-first warning, input/output domain labels.
- Validator updated to require PowerBoard testpoints, mounting holes and v4K mark.

Still open:

- Official footprint coordinate check against Mornsun mechanical drawing.
- KiCad ERC result.
- KiCad DRC result.
- Gerber/drill artifact review.
- Real supercap data: capacitance, ESR, allowed charge current, cycle rate.
- R_LIMIT value and pulse rating.
- Bypass relay/MOSFET part selection and timing.
- Thermal check for 20A operation and module cooling.

## Next gate

v4L should focus on official-footprint coordinate closure and CI feedback. If automated text validation passes, run the manual KiCad export workflow and fix the first real ERC/DRC/export errors.
