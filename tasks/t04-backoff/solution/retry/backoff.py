def backoff_delays(attempts, base, cap):
    """Exponential backoff delays in seconds: base, 2*base, 4*base, ... capped at cap."""
    return [min(base * 2**i, cap) for i in range(attempts)]


def jitter(delay, fraction, rand):
    return delay * (1 - fraction + 2 * fraction * rand())
