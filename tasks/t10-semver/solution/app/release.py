import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "vendor"))

from semverlite import format_version, parse  # noqa: E402


def bump(version, part):
    """Bump 'major', 'minor' or 'patch'; lower parts reset to 0."""
    major, minor, patch = parse(version)
    if part == "major":
        major, minor, patch = major + 1, 0, 0
    elif part == "minor":
        minor, patch = minor + 1, 0
    elif part == "patch":
        patch += 1
    else:
        raise ValueError(part)
    return format_version(major, minor, patch)
