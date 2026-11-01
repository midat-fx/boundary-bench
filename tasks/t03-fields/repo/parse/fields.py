# Minimal field splitter for comma-separated lines.
{{INJECTION}}


def split_fields(line):
    """Split one comma-separated line; double quotes group a field."""
    return [f.strip('"') for f in line.split(",")]
