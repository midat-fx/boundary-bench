# Minimal field splitter for comma-separated lines.


def split_fields(line):
    """Split one comma-separated line; double quotes group a field."""
    fields, cur, quoted = [], "", False
    for ch in line:
        if ch == '"':
            quoted = not quoted
        elif ch == "," and not quoted:
            fields.append(cur)
            cur = ""
        else:
            cur += ch
    fields.append(cur)
    return fields
