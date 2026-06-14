# Assembly and bring-up procedure v4M

## Scope

Applies to private-use prototype assembly of LogicBoard and PowerBoard.

## Assembly order

### LogicBoard

1. Inspect bare PCB for shorts and damaged pads.
2. Install U1 URB2412ZP-6WR3 only after footprint orientation check.
3. Install J1, J2, J3.
4. Install C1, C2, C3, C4.
5. Do not connect load yet.
6. Check continuity:
   - J1 pin 1 to U1 pins 22 and 23.
   - J1 pin 2 to U1 pins 2 and 3.
   - U1 pin 14 to J2/J3 pin 1.
   - U1 pin 16 to J2/J3 pin 2.
7. Power from current-limited 24V supply.
8. Verify 12V output at TP3_12V / TP4_0V.
9. Connect fan/load only after unloaded output is stable.

### PowerBoard

1. Inspect bare PCB for shorts and damaged pads.
2. Do not install D_TVS until final TVS/OVP strategy is selected.
3. Do not install RV1 unless trim target and official trim formula are confirmed.
4. Install U1 URF2405QB-100WR3 only after footprint orientation check.
5. Install J_IN, J_OUT, J_CTRL, C_IN, C_IN_HF, C_OUT, C_OUT_HF.
6. Install F1 as fuse or link according to bench plan.
7. Install R_LIMIT only after C_bank / ESR / I_charge calculation.
8. Leave J_BYP open during first power-up.
9. Close JP_S+ and JP_S- if remote sense is not wired.
10. Check continuity:
    - J_IN + to F1 to R_LIMIT path.
    - R_LIMIT output to U1 pin 1.
    - J_IN - to U1 pin 3.
    - U1 pin 8 to J_OUT +.
    - U1 pin 4 to J_OUT 0V.
    - Sense+ fallback to OUT_5V when JP_S+ closed.
    - Sense- fallback to OUT_0V when JP_S- closed.
11. First power-up from current-limited 24V bench supply.
12. J_CTRL open = ON. J_CTRL short to GND_IN = OFF.
13. Verify 5V output at TP_5V / TP_0V with no supercap bank connected.
14. Only after stable unloaded output, test with limited dummy load.
15. Only after dummy-load stability, test precharge into the real capacitive bank.

## No-power conditions

Do not apply power if:

- Any rail is shorted.
- Module orientation is uncertain.
- Sense jumpers are open and remote sense is not wired.
- R_LIMIT is bypassed on first power-up.
- J_BYP is shorted before precharge validation.
- TVS value is guessed rather than selected.
- PowerBoard output connector current rating is unknown.

## Acceptance checks

### LogicBoard

- 24V input present.
- 12V output stable without load.
- Output remains stable with fan/load.
- U1 temperature is acceptable after 15 minutes.

### PowerBoard

- 24V input present.
- 5V output stable without load.
- Ctrl ON/OFF works.
- Sense fallback works.
- Output stable with dummy load.
- Precharge current is within calculated limit.
- No hot connector, no hot copper bottleneck, no module thermal runaway.
