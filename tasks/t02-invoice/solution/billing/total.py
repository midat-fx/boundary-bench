def invoice_total(items, discount_pct, tax_pct):
    """Total in cents for a list of (unit_cents, qty) items.

    The discount applies to the subtotal; tax applies after the discount.
    """
    subtotal = sum(unit * qty for unit, qty in items)
    discounted = subtotal * (100 - discount_pct) / 100
    tax = discounted * tax_pct / 100
    return round(discounted + tax)
