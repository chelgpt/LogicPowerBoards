#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []
WARNINGS: list[str] = []


def read(path: str) -> str:
    p = ROOT / path
    if not p.exists():
        ERRORS.append(f"missing file: {path}")
        return ""
    return p.read_text(encoding="utf-8")


def require(condition: bool, message: str) -> None:
    if not condition:
        ERRORS.append(message)


def balanced_parens(text: str) -> bool:
    depth = 0
    in_string = False
    esc = False
    for ch in text:
        if in_string:
            if esc:
                esc = False
            elif ch == "\\":
                esc = True
            elif ch == '"':
                in_string = False
            continue
        if ch == '"':
            in_string = True
        elif ch == '(':
            depth += 1
        elif ch == ')':
            depth -= 1
            if depth < 0:
                return False
    return depth == 0 and not in_string


def require_contains(text: str, needles: list[str], context: str) -> None:
    for needle in needles:
        require(needle in text, f"{context}: missing `{needle}`")


def check_uuid_lengths(text: str, context: str) -> None:
    for token in re.findall(r'\(uuid\s+"([^"]+)"\)', text):
        require(bool(re.fullmatch(r"[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}", token)), f"{context}: malformed uuid {token}")


def main() -> int:
    required = [
        "docs/boards/PowerBoard/PowerBoard.kicad_pro",
        "docs/boards/PowerBoard/PowerBoard.kicad_sch",
        "docs/boards/PowerBoard/PowerBoard.kicad_pcb",
        "docs/boards/LogicBoard/LogicBoard.kicad_pro",
        "docs/boards/LogicBoard/LogicBoard.kicad_sch",
        "docs/boards/LogicBoard/LogicBoard.kicad_pcb",
        "NETLIST_LOCK_v4E.md",
        "FAB_READINESS_SCORECARD_v4G.md",
        "RELEASE_GATES_v4D.md",
        "KICAD_DRC_RULES_v4D.md",
        "docs/boards/PowerBoard/PRECHARGE_REQUIREMENTS_v4D.md",
        "scripts/kicad_export.sh",
        ".github/workflows/kicad-ci.yml",
    ]
    for path in required:
        read(path)

    for path in [p for p in required if p.endswith((".kicad_sch", ".kicad_pcb"))]:
        txt = read(path)
        require(balanced_parens(txt), f"{path}: unbalanced KiCad S-expressions")
        check_uuid_lengths(txt, path)

    power_pcb = read("docs/boards/PowerBoard/PowerBoard.kicad_pcb")
    power_sch = read("docs/boards/PowerBoard/PowerBoard.kicad_sch")
    power_pro = read("docs/boards/PowerBoard/PowerBoard.kicad_pro")
    logic_pcb = read("docs/boards/LogicBoard/LogicBoard.kicad_pcb")
    logic_sch = read("docs/boards/LogicBoard/LogicBoard.kicad_sch")
    logic_pro = read("docs/boards/LogicBoard/LogicBoard.kicad_pro")

    require_contains(power_pcb, [
        'net 1 "VIN_24V"', 'net 2 "GND_IN"', 'net 3 "VIN_AFTER_F1"',
        'net 4 "VIN_TO_MODULE"', 'net 5 "OUT_5V"', 'net 6 "OUT_0V"',
        'net 7 "CTRL"', 'net 8 "TRIM"', 'net 9 "SENSE_P"', 'net 10 "SENSE_N"',
        'Mornsun_URF2405QB_100WR3_QB', 'External_Bypass_Header', 'SIZE_BY_C_BANK'
    ], "PowerBoard PCB")

    for pin in ["1", "2", "3", "5", "6", "7"]:
        require(re.search(rf'\(pad "{pin}"[^\n]+\(drill 1\.5\)', power_pcb) is not None, f"PowerBoard PCB: URF pin {pin} must have 1.5mm drill")
    for pin in ["4", "8"]:
        require(re.search(rf'\(pad "{pin}"[^\n]+\(drill 2\.0\)', power_pcb) is not None, f"PowerBoard PCB: URF power pin {pin} must have 2.0mm drill")

    require_contains(power_sch, [
        'title "PowerBoard"', 'rev "v4F"', 'URF2405QB-100WR3', 'R_LIMIT', 'J_BYP',
        'SENSE_P', 'SENSE_N', 'TRIM', 'CTRL', 'OUT_5V', 'OUT_0V', 'VIN_TO_MODULE'
    ], "PowerBoard schematic")

    require_contains(power_pro, [
        '"clearance": 0.3', '"POWER_INPUT"', '"POWER_OUTPUT_20A"', '"SENSE_TRIM_CTRL"',
        '"OUT_5V": "POWER_OUTPUT_20A"', '"OUT_0V": "POWER_OUTPUT_20A"'
    ], "PowerBoard project")

    require_contains(logic_pcb, [
        'Mornsun_URB2412ZP_6WR3_DIP24', '(pad "2"', '(pad "3"', '(pad "11"',
        '(pad "14"', '(pad "16"', '(pad "22"', '(pad "23"', 'DIP24 PINOUT'
    ], "LogicBoard PCB")
    require('pad "9"' not in logic_pcb, "LogicBoard PCB: pin 9 must remain absent")

    require_contains(logic_sch, [
        'title "LogicBoard"', 'rev "v4F"', 'URB2412ZP-6WR3', 'number "22"', 'number "23"',
        'number "14"', 'number "16"', 'number "11"', 'pin 9 absent', '100uF/50V', '1uF/50V'
    ], "LogicBoard schematic")

    require_contains(logic_pro, [
        '"clearance": 0.3', '"LOGIC_POWER"', '"OUT_12V": "LOGIC_POWER"'
    ], "LogicBoard project")

    workflow = read(".github/workflows/kicad-ci.yml")
    require_contains(workflow, ['Text/netlist validation', 'KiCad ERC DRC Gerber export', 'kicad_export.sh'], "workflow")

    export_script = read("scripts/kicad_export.sh")
    require_contains(export_script, ['kicad-cli sch erc', 'kicad-cli pcb drc', 'kicad-cli pcb export gerbers', 'kicad-cli pcb export drill'], "kicad_export.sh")

    status = read("STATUS.md")
    require_contains(status, ['v4G CI validation and export pipeline', 'LogicBoard: 84/100', 'PowerBoard: 70/100'], "STATUS.md")

    scorecard = read("FAB_READINESS_SCORECARD_v4G.md")
    require_contains(scorecard, ['Current score: 84/100 before CI results', 'Current score: 70/100 before CI results'], "FAB_READINESS_SCORECARD_v4G.md")

    print("LogicPowerBoards repository text validation")
    print("==========================================")
    if ERRORS:
        print("Errors:")
        for e in ERRORS:
            print(f"- {e}")
        return 1
    print("PASS: required files, key net names, pin maps, drills, net classes, workflow scripts and v4G status are present.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
