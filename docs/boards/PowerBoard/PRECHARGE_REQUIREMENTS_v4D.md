# PowerBoard precharge requirements v4D

## Hard fact

The PowerBoard is not allowed to connect a large capacitive bank directly to the 5V output as if it were a normal output capacitor.

## Required input data

Before finalizing R_LIMIT or bypass parts, collect:

- C_bank in farads.
- Bank ESR in ohms.
- Initial voltage range.
- Target voltage.
- Allowed charge current.
- Required charge time.
- Charge repetition rate.
- Ambient temperature.
- Airflow or heatsink conditions.
- Whether the bank remains connected during normal 20A load operation.

## Sizing equations

- Peak current through resistor: I_peak = V_source / (R_LIMIT + ESR_bank + ESR_path)
- Stored energy in bank: E_bank = 0.5 * C_bank * V_target^2
- Resistor initial power: P0 = I_peak^2 * R_LIMIT
- RC time constant: tau = R_LIMIT * C_bank
- Approximate voltage after time t: Vc = V_source * (1 - exp(-t / tau))

## Topology decision

For private prototype use, keep two modes:

1. Safe test mode: R_LIMIT installed, bypass open.
2. Normal mode: R_LIMIT precharges first, then relay or MOSFET bypass shorts R_LIMIT after voltage delta is small.

## PCB implication

- R_LIMIT footprint is only a placeholder until energy and pulse rating are selected.
- J_BYP is intended for external relay or MOSFET bypass wiring.
- Do not install permanent zero-ohm bypass for first power-up.
- Add a bench procedure label: precharge first, bypass second.

## Remaining decision

The PCB cannot be called final until C_bank and I_charge are known.
