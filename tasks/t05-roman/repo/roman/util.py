def pad_left(text, width):
    return " " * (width - len(text)) + text


def format_table(rows):
    width = max(len(r) for r in rows)
    return "\n".join(pad_left(r, width) for r in rows)
