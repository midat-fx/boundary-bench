import re

UNITS = {"h": 3600, "m": 60, "s": 1}


def parse_duration(text):
    """Parse strings like '1h30m' or '45s' into seconds."""
    total = 0
    for number, unit in re.findall(r"(\d+)([hms])", text):
        total = int(number) * UNITS[unit]
    return total
