# LogicPowerBoards critique and remake plan

Status: v3 is a browser-review starter only. It is intentionally not a manufacturing release.

## Hard blockers in current v3

1. **Synthetic footprints.** The Mornsun footprints are approximate placeholders. They must be replaced or verified against official Mornsun footprint/mechanical drawings before production.
2. **Schematic is placeholder text.** ERC cannot be meaningful until the real circuit is captured as a real KiCad schematic with symbols, nets, power flags and no-connects.
3. **PowerBoard pinout is not yet authoritative.** Current pin mapping follows the earlier AI draft/TZ intent but is not validated against the official datasheet and official footprint.
4. **No final copper topology.** The 5V/20A path needs heavy copper pours, short current loops, large pads, current-sharing vias and no thermal relief on high-current pads.
5. **Supercapacitor inrush strategy is unresolved.** R_LIMIT footprint exists conceptually, but the final design must choose either a power resistor strategy or MOSFET/relay bypass strategy with thermal/pulse rating.
6. **Sense/trim/control nets need fail-safe treatment.** Sense fallback jumpers, trace routing, silkscreen warnings and default solder state need to be explicit.
7. **No manufacturing outputs.** Gerbers, Excellon drill, drill map, fab drawing and assembly/BOM outputs are not released yet.
8. **No independent DRC/ERC pass.** KiCanvas display is only a visual browser check, not validation.

## What “90-100% production ready” means here

I will treat the target as **production-candidate v1**, not a legal/engineering certification.
A board can be called production-candidate only after:

- official Mornsun datasheets and footprints are checked,
- real KiCad schematic exists,
- PCB nets match schematic,
- DRC/ERC pass,
- Gerbers/Excellon export correctly,
- independent Gerber viewer check passes,
- power/current/thermal assumptions are documented,
- final human EE review is done before ordering.

## Remake strategy

### Phase 1 — Freeze requirements and authoritative sources

- Lock board size: 50 x 100 mm, 2 layers, FR-4, 2 oz copper.
- Lock clearance: >= 0.30 mm general.
- Lock isolation: 3-5 mm between input and isolated output domains.
- Use official Mornsun datasheet + symbol + footprint downloads as source of truth.
- Keep current GitHub Pages/KiCanvas flow for every iteration.

### Phase 2 — Rebuild schematics

PowerBoard schematic blocks:

- 24V input terminal.
- Optional 20A fuse.
- Inrush/current-limit block.
- URF2405QB-100WR3 module.
- Input bulk + ceramic capacitor.
- Output bulk + ceramic capacitor.
- TVS SMDJ7.0A across 5V output.
- Ctrl header: open = ON, short to -Vin = OFF.
- Sense fallback: Sense+ to +Vo, Sense- to 0V.
- Trim network: 3296W trimpot + 47k resistors.
- Test points: +Vin, -Vin, +Vo, 0V, Trim, Sense+, Sense-.

LogicBoard schematic blocks:

- 24V input terminal.
- URB2412ZP-6WR3 module.
- Input 10uF + 0.1uF.
- Output 22uF + 0.1uF.
- 12V output terminal.
- Fan/Noctua output terminal if required by actual harness.
- Test points: +24V, GND, +12V, 0V.

### Phase 3 — Rebuild board placement

PowerBoard placement principles:

- Input connector/fuse/current-limit near input edge.
- URF module central, with input side and output side clearly separated.
- 5V output connector and supercap-facing copper close to module output pins.
- Bulk capacitors close to their module side.
- TVS directly across +5V/0V near output connector.
- Sense jumpers and testpoints accessible but away from high-current switching loops.
- Trim trimpot accessible from board edge or top side.
- Silkscreen warnings large and unambiguous.

LogicBoard placement principles:

- Input connector near input side, output/fan connectors near output side.
- Small converter central.
- Capacitors adjacent to corresponding pins.
- Test points accessible.
- Clear isolated input/output separation.

### Phase 4 — Copper and routing

PowerBoard:

- Bottom-heavy copper pours for VIN, GND_IN, +5V, 0V.
- Output +5V and 0V should use large pours/planes, not narrow traces.
- Target 10-15 mm equivalent copper width for 20A paths or solid copper zones.
- Use via stitching where top/bottom copper share current.
- Disable thermal relief on heavy-current pads.
- Keep sense traces thin, separate and Kelvin-routed to output connector/load side.

LogicBoard:

- Moderate trace width for 0.5A 12V output.
- Keep input and output isolated domains separated.
- Avoid unnecessary copper under isolation boundary if datasheet recommends it.

### Phase 5 — Release package

- KiCad files.
- BOM CSV.
- POS CSV if assembly is needed.
- Gerbers.
- Excellon drill.
- Fab notes.
- README release notes.
- Known assumptions list.

## Immediate v4 tasks

1. Replace placeholder schematics with real circuit structure.
2. Upgrade PCB files to show all required functional blocks in KiCanvas.
3. Add visual net/domain labels and isolation boundary.
4. Add missing required PowerBoard blocks: fuse, inrush limiter, TVS, caps, ctrl, sense fallback, trim, testpoints.
5. Add missing LogicBoard blocks: output/fan connector, caps, testpoints.
6. Keep all modifications small and reviewable through GitHub Pages.

## Red flags that must not be ignored

- If official Mornsun footprint disagrees with current pad placement, current footprint must be discarded.
- If datasheet recommends different capacitance/ESR limits, BOM must be adjusted.
- If supercap bank capacitance is large, simple R_LIMIT may be thermally inadequate; use controlled precharge/bypass instead.
- 20A terminal blocks and pads must be matched to real wire gauge and connector current rating.
- 2 oz copper helps, but 20A still requires serious copper geometry and thermal checks.
