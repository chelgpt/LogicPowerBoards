# Fab package manifest v4J

## Purpose

Defines the expected contents of a fabrication package once the manual KiCad CI export succeeds.

## Expected CI artifact

Artifact name: fabrication-output.

## Expected folders

- fabrication_output/reports
- fabrication_output/PowerBoard/gerbers
- fabrication_output/LogicBoard/gerbers

## Required report files

- reports/kicad_cli_version.txt
- reports/PowerBoard_erc.rpt
- reports/LogicBoard_erc.rpt
- reports/PowerBoard_drc.rpt
- reports/LogicBoard_drc.rpt

## Required board outputs

For each board:

- Top copper Gerber.
- Bottom copper Gerber.
- Top soldermask Gerber.
- Bottom soldermask Gerber.
- Top silkscreen Gerber.
- Bottom silkscreen Gerber if exported.
- Edge cuts / board outline Gerber.
- Excellon drill file.
- Drill map if exported.

## Factory order parameters

- PCB type: two-layer FR-4.
- Board thickness: 1.6mm.
- Copper: 2oz.
- Minimum clearance: 0.30mm or better.
- Surface finish: ENIG preferred; lead-free HASL acceptable for private prototype if budget constrained.
- Soldermask: green preferred for lowest manufacturing risk.
- Electrical test: yes.
- Controlled impedance: no.
- Castellated holes: no.
- Blind/buried vias: no.
- Panelization: no unless manufacturer requires it.

## Final no-order conditions

Do not order if any of the following is true:

- ERC report contains unresolved errors.
- DRC report contains unresolved errors.
- Gerber viewer shows broken outline.
- Drill file is missing.
- Input/output polarity marks are hidden or ambiguous.
- PowerBoard output connector current rating is still unknown.
- PowerBoard precharge sizing is still unknown for the real capacitive bank.
- Official Mornsun footprint coordinate check is not done.

## Private-use prototype order condition

The project may only move to private-use prototype order after:

1. Text validation passes.
2. KiCad ERC passes.
3. KiCad DRC passes.
4. Gerbers and drill files are generated.
5. Gerbers are visually reviewed.
6. Known PowerBoard precharge risks are accepted or closed.
