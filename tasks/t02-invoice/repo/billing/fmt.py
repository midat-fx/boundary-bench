def format_currency(cents):
    sign = "-" if cents < 0 else ""
    cents = abs(cents)
    return f"{sign}${cents // 100}.{cents % 100:02d}"


def receipt_line(name, cents):
    return f"{name:<20}{format_currency(cents):>10}"
