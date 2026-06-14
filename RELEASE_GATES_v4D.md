# Release gates v4D

## Purpose

This file defines the gates that must be closed before any factory order.

## Gate A - source truth

- Use official Mornsun datasheet for URF2405QB-100WR3.
- Use official Mornsun datasheet for URB2412ZP-6WR3.
- Import or manually match official mechanical footprints.
- Do not use generic DIP8 for URB ZP.
- Do not use undersized drills for URF QB.

## Gate B - KiCad integrity

- Real schematic must exist, not text-only placeholder.
- ERC must pass or every warning must be documented.
- PCB footprints must be linked to schematic references.
- PCB net names must match schematic net names.
- DRC minimum clearance: 0.30mm or tighter only if fab selected and accepted.
- Board outline: 50 x 100mm.
- Copper: two layers, 2oz.

## Gate C - PowerBoard electrical closure

- URF pin map: 1 +Vin, 2 Ctrl, 3 -Vin, 4 0V, 5 Sense-, 6 Trim, 7 Sense+, 8 +Vo.
- Sense+ must connect to +Vo when remote sense is not wired.
- Sense- must connect to 0V when remote sense is not wired.
- Ctrl is referenced to input GND.
- Ctrl open equals ON; Ctrl short to input GND equals OFF.
- Trim must be NC or populated only after bench target is defined.
- Input fuse candidate: 10A slow or validated equivalent.
- Output connector: continuous 20A capable, preferably 25-30A class.
- Output direct capacitive load must stay below module limit unless isolated by precharge stage.
- Precharge value and bypass timing must be calculated from real load data.

## Gate D - LogicBoard electrical closure

- URB ZP pin map: 2 and 3 GND_IN; 11 NC; 14 OUT_12V; 16 GND_OUT; 22 and 23 VIN_24V.
- Pin 9 absent, no pad required.
- No trim, sense or ctrl assumptions unless confirmed by exact datasheet revision.
- Input bulk capacitor 100uF/50V plus HF cap close to input pins.
- Output bulk capacitor within module capacitive load limit.

## Gate E - fabrication package

- Gerber top copper.
- Gerber bottom copper.
- Gerber solder masks.
- Gerber silkscreens.
- Edge cuts / board outline.
- Excellon drill file.
- Drill map.
- Fab notes.
- BOM.
- Optional pick/place if assembly is outsourced.

## Gate F - pre-power bench checks

- Bare PCB continuity test.
- Input to output isolation resistance check.
- No short between VIN_24V and GND_IN.
- No short between output rails.
- No short between primary and secondary domains.
- First power-up from current-limited bench supply.
- No final load on first power-up.
