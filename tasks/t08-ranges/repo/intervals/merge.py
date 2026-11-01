def merge_ranges(ranges):
    """Merge closed integer intervals given as (start, end) tuples."""
    out = []
    for start, end in sorted(ranges):
        if out and start < out[-1][1]:
            out[-1] = (out[-1][0], max(out[-1][1], end))
        else:
            out.append((start, end))
    return out
