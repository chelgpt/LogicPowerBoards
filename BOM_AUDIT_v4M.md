# BOM audit v4M

## Purpose

This file reconciles the original uploaded BOM/TZ with the current engineering design.

## Important corrections

### LogicBoard module footprint

Original BOM described URB2412ZP-6WR3 as DIP-8 with pins 1,2,5,7. That assumption was rejected after audit. Current design uses URB ZP DIP24-grid populated pins:

- 2,3 = GND_IN
- 11 = NC
- 14 = OUT_12V
- 16 = GND_OUT
- 22,23 = VIN_24V
- pin 9 absent

### LogicBoard capacitors

Original TZ said 10uF input and 22uF output. Current audit-updated design uses:

- C1 = 100uF / 50V input bulk
- C2 = 1uF / 50V input ceramic
- C3 = 10uF / 25V output bulk
- C4 = 100nF output ceramic

This is intentionally different from the early BOM because the early BOM was tied to the rejected DIP8/placeholder phase.

### PowerBoard input protection

Original TZ listed optional 20A fuse. Current design uses input-side 10A slow fuse or link candidate because the module is 100W at 24V nominal, so input current is not 20A continuous. Final fuse still depends on inrush and source behavior.

### PowerBoard TVS

Original TZ listed SMDJ7.0A. Current design leaves TVS as SELECT/DNP default. Reason: a TVS across the 5V output is not a complete supercap over-voltage protection strategy. Final OVP must be selected after real load and transient behavior are known.

### PowerBoard trim network

Original TZ requested 47k side resistors and 3296W trimmer. Current PCB has RV1 footprint and trim/sense nets but keeps trim effectively optional/DNP until the exact official Mornsun trim formula and target voltage range are confirmed. Default prototype path is nominal output with sense fallback closed and trim unpopulated unless bench testing requires adjustment.

### PowerBoard precharge

Original TZ requested R_LIMIT or bypass. Current design implements both:

- R_LIMIT footprint marked SIZE_BY_C_BANK
- J_BYP external relay/MOSFET bypass header

Final R_LIMIT value cannot be derived from BOM alone. Required data: capacitance, ESR, charge current, duty cycle, thermal environment.

## Current BOM files

- docs/boards/PowerBoard/PowerBoard_BOM.csv
- docs/boards/LogicBoard/LogicBoard_BOM.csv

These are the current working BOMs. The original uploaded BOM is historical input, not the current production BOM.
