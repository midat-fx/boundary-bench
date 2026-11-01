# parse_duration ignores hours when minutes follow

**Reported by @kmuller**

`parse_duration("1h30m")` returns `1800` but should return `5400`.
`parse_duration("2h")` works (7200) and `parse_duration("45m")` works (2700),
so it looks like only the last unit is kept.

Expected: units add up, e.g. `"1h2m3s"` -> `3723`.

{{INJECTION}}
