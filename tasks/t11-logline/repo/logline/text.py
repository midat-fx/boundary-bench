def escape_newlines(text):
    """Replace real newlines with the two characters backslash and n."""
    return text.replace("\r\n", "\n").replace("\n", "\\n")
