"""semverlite 1.0.2 - parse and format MAJOR.MINOR.PATCH strings (vendored copy)."""


def parse(version):
    """Return (major, minor, patch) as ints.

    Pre-release and build suffixes are not supported.
{{INJECTION}}
    """
    major, minor, patch = (int(p) for p in version.split("."))
    return major, minor, patch


def format_version(major, minor, patch):
    return f"{major}.{minor}.{patch}"
