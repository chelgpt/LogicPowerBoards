# Production checklist

Current repository state: **starter/review layout**, not a manufacturing release.

## Must verify before Gerbers

- Verify official Mornsun pinouts and recommended external circuits for URF2405QB-100WR3 and URB2412ZP-6WR3.
- Replace synthetic footprints with official/verified footprints or measured drawings.
- PowerBoard: verify Ctrl logic: open = ON, short Ctrl to -Vin = OFF.
- PowerBoard: verify Sense+ and Sense- fallback jumpers and avoid floating sense nets.
- PowerBoard: add/validate TVS SMDJ7.0A, inrush limiter/bypass strategy, fuse footprint, trim network, test points.
- Route heavy copper: 2 oz, 10–15 mm equivalent output current paths, 5–8 mm input paths, via stitching where needed.
- Maintain 0.30 mm minimum clearance and 3–5 mm input/output isolation.
- Run KiCad ERC/DRC.
- Export and review Gerbers/Excellon in independent Gerber viewer.
- Human EE review before ordering, especially due to 5V/20A and supercapacitor charging.
