# Letter formation data + printable name-tracing sheet generator

Two things that are genuinely hard to find in one place:

1. `data/letter-formation.csv` — for each of the 26 letters: the stroke order, where the
   stroke starts, the mistake that shows up most often, and the correction that fixes it.
   Ascenders and descenders are flagged so you can filter the set for a given hand.
2. `scripts/make_name_sheet.py` — a single-file, dependency-free script that turns a name
   into a printable three-line tracing sheet in SVG (Letter or A4, three letter sizes,
   dotted or solid letters, one to five trace rows with a blank row at the end).

## The data

| letter | uppercase_strokes | start_point | common_error | fix |
|---|---|---|---|---|
| b | vertical down, back up into the bowl | top of the stem | the bowl is drawn first, so the stem leans | straight down first, then come back up and out |
| g | circle, then the hook below the line | top of the circle | below the line a second full circle is drawn | a shadow hook, one dip, then back up |
| s | one reversing curve | top right | built as two separate curves, the join shows | one stroke that reverses direction |

26 rows, columns: `letter, uppercase_strokes, lowercase_strokes, start_point, common_error,
fix, is_descender, is_ascender`. Plain CSV, UTF-8, no licence restrictions beyond MIT.

## The generator

```bash
python scripts/make_name_sheet.py Emma > emma.svg
python scripts/make_name_sheet.py "Mary-Jane" --rows 2 --size preschool --paper a4 > mary.svg
```

Letter sizes are the ones used in print: 15 / 12 / 9.5 mm capital ink height with 26 / 22 / 18 mm
row pitch. Open the SVG in a browser and print at 100% — one page, no scaling.

`examples/emma.svg` is the output for `Emma` at the default settings.

## Why the numbers are what they are

The millimetres are capital ink height in Andika, measured in Chrome's print layout at 100%
with `canvas.measureText`. Change the typeface and the numbers move with it.

## Related

A browser version of the same idea, with the dotted letters rendered on the page and printed
straight from the browser: [tracecub.com](https://tracecub.com) — free, no account.

## Licence

MIT.
