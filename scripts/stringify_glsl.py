#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path


def escape(line: str) -> str:
    return line.replace("\\", "\\\\").replace('"', '\\"')


def main() -> int:
    if len(sys.argv) != 4:
        print("usage: stringify_glsl.py <input> <output> <symbol>", file=sys.stderr)
        return 1

    input_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2])
    symbol = sys.argv[3]

    lines = input_path.read_text(encoding="utf-8").splitlines()

    output = [f"const char *fallbackShader_{symbol} ="]
    for line in lines:
        output.append(f"  \"{escape(line)}\\n\"")
    output.append(";")
    output.append("")

    output_path.write_text("\n".join(output), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
