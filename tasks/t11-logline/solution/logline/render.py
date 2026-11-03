from logline.text import escape_newlines


def render(level, component, message):
    """Format one log record as described in README.md."""
    return f"{level.upper():<5} | {component} | {escape_newlines(message)}"
