# NETLIST LOCK v4E

This document is the locked electrical connectivity reference for the current engineering candidate. PCB and future schematic must match this file.

## PowerBoard nets

### VIN_24V

- J_IN pin 1
- F1 pin 1
- TP_VIN if populated

### GND_IN

- J_IN pin 2
- U1 pin 3 (-Vin)
- C_IN pin 2
- C_IN_HF pin 2
- J_CTRL pin 2
- TP_GNDIN if populated

### VIN_AFTER_F1

- F1 pin 2
- R_LIMIT pin 1
- J_BYP pin 1

### VIN_TO_MODULE

- R_LIMIT pin 2
- J_BYP pin 2
- U1 pin 1 (+Vin)
- C_IN pin 1
- C_IN_HF pin 1

### CTRL

- U1 pin 2
- J_CTRL pin 1

### OUT_0V

- U1 pin 4
- J_OUT pin 2
- C_OUT pin 2
- C_OUT_HF pin 2
- JP_S- pin 2
- D_TVS pin 2 if installed
- TP_0V if populated

### SENSE_N

- U1 pin 5
- JP_S- pin 1
- RV1 pin 1 if trim is populated
- TP_S- if populated

### TRIM

- U1 pin 6
- RV1 pin 2 if trim is populated
- TP_TRIM if populated

### SENSE_P

- U1 pin 7
- JP_S+ pin 1
- RV1 pin 3 if trim is populated
- TP_S+ if populated

### OUT_5V

- U1 pin 8
- J_OUT pin 1
- C_OUT pin 1
- C_OUT_HF pin 1
- JP_S+ pin 2
- D_TVS pin 1 if installed
- TP_5V if populated

## LogicBoard nets

### VIN_24V

- J1 pin 1
- U1 pins 22 and 23
- C1 pin 1
- C2 pin 1
- TP1_24V if populated

### GND_IN

- J1 pin 2
- U1 pins 2 and 3
- C1 pin 2
- C2 pin 2
- TP2_GND if populated

### OUT_12V

- U1 pin 14
- J2 pin 1
- J3 pin 1
- C3 pin 1
- C4 pin 1
- TP3_12V if populated

### GND_OUT

- U1 pin 16
- J2 pin 2
- J3 pin 2
- C3 pin 2
- C4 pin 2
- TP4_0V if populated

### NC / no pin

- U1 pin 11: NC, no copper connection.
- U1 pin 9: physically absent, no pad.

## Locked manufacturing assumptions

- Board size: 50 x 100mm.
- Layers: 2 copper layers.
- Copper: 2oz.
- General clearance: 0.30mm.
- PowerBoard output paths: copper pours or 10-15mm equivalent width.
- PowerBoard sense lines: Kelvin-style, separate from high-current copper.
