import re


def slugify(text):
    """Lowercase ASCII slug: runs of non-alphanumerics become one dash."""
    text = text.lower()
    return re.sub(r"[^a-z0-9]+", "-", text).strip("-")
