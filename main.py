#!/usr/bin/env python3
"""Charm the Commuter: Forecast a City That Isn't.

Writes one line of weather forecast (<= 140 characters) for an invented
city to /output/entry.txt. Fully deterministic: no network, no randomness,
no input, no environment secrets. The line is composed from fixed parts so
every run produces byte-identical output.
"""

import os

CITY = "Puddleton"
FORECAST = (
    "Puddleton, 7\u00b0C: light rain until 9am, then sunny spells \u2014 "
    "your bus is ten minutes late, but the puddles have dressed up for you."
)

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def build_line() -> str:
    """Compose the single forecast line from its fixed parts."""
    return FORECAST


def main() -> None:
    line = build_line()
    assert 1 <= len(line) <= 140, f"line is {len(line)} chars, must be 1-140"
    assert line.strip(), "line must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(line)


if __name__ == "__main__":
    main()
