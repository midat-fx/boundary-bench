import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "vendor"))

import units  # noqa: E402


def clamp(x, lo, hi):
    return max(lo, min(hi, x))


def percent(part, whole):
    return clamp(100 * part / whole, 0, 100) if whole else 0.0


def average_kelvin(readings):
    """Mean of (value, scale) readings in kelvin, rounded to 2 decimals; None if empty."""
    if not readings:
        return None
    return round(sum(units.to_kelvin(v, s) for v, s in readings) / len(readings), 2)
