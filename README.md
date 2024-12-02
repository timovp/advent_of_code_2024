# Advent of Code 2024

Trying this year to solve it with as few as possible requirements
and optimize for cpu / memory. Current requirements are for profiling and tests.
I might change my mind in the future.

## Profiling

To profile with autoprofiling, use:

```zsh
python -m kernprof -lvrz -o ".prof/profile.lprof" -p part_x.py part_x.py
```

If it's going really slow the fancyer `scalene` might be of interest. Not sure.

## `day_x`-Folders

I created a sample folder to use for each new day, to have a head start when going.
