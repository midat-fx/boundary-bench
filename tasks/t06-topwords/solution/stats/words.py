from collections import Counter


def top_words(text, n):
    """The n most frequent lowercase words as (word, count); ties sorted alphabetically."""
    counts = Counter(text.lower().split())
    return sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))[:n]
