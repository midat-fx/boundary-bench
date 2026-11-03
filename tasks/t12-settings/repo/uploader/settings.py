import configparser
from pathlib import Path

DEFAULTS = {"retries": 3, "timeout_s": 10.0}


def load_settings(path=Path("config/settings.ini")):
    """Read the [upload] section; keys missing from the file keep their DEFAULTS value."""
    parser = configparser.ConfigParser()
    parser.read(path)
    section = parser["upload"] if parser.has_section("upload") else {}
    settings = dict(DEFAULTS)
    for key in DEFAULTS:
        if key in section:
            settings[key] = section[key]
    return settings
