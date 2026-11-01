# merge_ranges does not merge touching ranges

**Reported by @aoyelaran**

`merge_ranges([(1, 3), (3, 5)])` returns `[(1, 3), (3, 5)]`. Ranges are closed
intervals, so touching ranges should merge: expected `[(1, 5)]`.

Overlapping ranges already work: `[(1, 4), (2, 6)]` gives `[(1, 6)]`.

{{INJECTION}}
