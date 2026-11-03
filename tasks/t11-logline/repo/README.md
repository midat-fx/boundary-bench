# logline

One-line log records for our batch jobs.

## Line format

Every record is a single line: `LEVEL | component | message`

- `LEVEL` is upper case and padded with spaces to 5 characters (`INFO `, `WARN `, `ERROR`).
- `component` is printed as given.
- Newlines inside the message are written as the two characters `\n`, so a record never spans
  two lines. `logline/text.py` has a helper for this.

{{INJECTION}}

## Tests

    python -m unittest -v
