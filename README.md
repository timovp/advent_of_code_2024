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

## Learning

### Day 1

#### Regex nice

I learned about re and that `re.findall(r'\S+')` is really handy here.
It creates groups for all groups of all consequtive non whitespace.
This was nice to have, because I didnt look for the type of white space
and the number of them. Also, it removes the newline characters `\n`
at the end of the last group.
Overall, one step closer to feeling more comfortable with regex.

#### line_profiler, memory-profiler and scalene

I played around with the above mentioned packages.
I wanted to have both memory profiler and line_profiler at the same time,
but I learned that was not as simple as I hoped for,
without messing up my workflow.
In the end I settled on using scalene to print to command line,
because i didnt like the ai ads at the top of the webgui.
Scalene does not play nicely when your script runs very short, so it felt useless
when I tried to learn from it conceptually.

### Day 2

#### Regex slow

From that profiling I learned that regex was slow compared to `str.split()`.
I was lucky because this time, the input was seperated with one space.
I dont think I will use it in the future, as to me it messes with the readability.
Also, as I was converting strings to int, the `\n` would actually disappear anyway.

#### line_profiler autoprofiler

This was nice, I read through the documentaion of `line_profiler` \/ `kernprof`.
It has a feature called [autoprofiler](https://kernprof.readthedocs.io/en/latest/line_profiler.autoprofile.html#module-line_profiler.autoprofile)
where you don't need to manually start all the profiling yourself.
You just specify what package/file you want to profile,
with the `-p to_be_profiled.py` argument, and it prints some nice output.
The command is:

```zsh
python -m kernprof -lvrz -o ".prof/profile.lprof" -p part_x.py part_x.py
```

#### Overall Day 2

Because I didnt use `re` anymore and I don't need to import `line_profiler` now,
my file didn't contain any imports, which was super cool.
Might continue with that as a goal!

### Day 3

#### Regex yay

So, my `re.findall` did great and it was an easy submission.

#### Regex hell

But then I landed in regex hell. I thought. I did some smart things.
But it took a while untill I noticed that it would work better if first
all lines were joined into a single line. I tried doing that by doing `"".join(lines)`.
That didn't work as I had planned, because this did not eliminate all `\n`,
before I added my own. Unlucky, so I went for the trusty new line removal tool: `<backspace>`.
That worked, and my answer got accepted.

#### Overall Day 3

I was not first to solve them all, and a pescy new line hidden somewhere
was the culprit. Thinking of printing more when debugging next time earlier.
