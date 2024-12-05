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

### Day 4

#### Matrix things

Learning from yesterday, I was eager to do more printing and visualize
more of my results. Well, I did, and it worked. But it made me slow.
Pretty, but slow.

#### Visualizations

I started out example input and wanted to make the same output as they did replacing
the irrelevant characters with `.`. This resulted in a bit of spaghetti,
but I think acceptable for the prettyness.

```text
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX

....XXMAS. | ....XXMAS. ✅
.SAMXMS... | .SAMXMS... ✅
...S..A... | ...S..A... ✅
..A.A.MS.X | ..A.A.MS.X ✅
XMASAMX.MM | XMASAMX.MM ✅
X.....XA.A | X.....XA.A ✅
S.S.S.S.SS | S.S.S.S.SS ✅
.A.A.A.A.A | .A.A.A.A.A ✅
..M.M.M.MM | ..M.M.M.MM ✅
.X.X.XMASX | .X.X.XMASX ✅
```

I did the same for the big one, but there was less to compare obviously.
I used this idea of visualizations also to solve last years day_5 problem.

#### 2023 Day 5

##### They made me quit

Day 5 was the puzzle that was the hell that made me and most colleagues quit.  
It was a puzzle about hashmaps (dictionaries) chained, mapping ranges of numbers
to other ranges of numbers. You had to find the input that with the smallest result.
Conceptionally not so difficult, but, then done with multiple giant ranges per map,
made it almost impossible to bruteforce yourself through the map constructions.

##### The old appreach

In the end I went for a calculation instead of a dictionary loopup.
Saved a lot of time. But still, no luck when applying for such big ranges.

##### Making it visual again

Based on todays experiences I should just plot the input-output cominations.
Maybe it would give me some insight into a better solution.
I sampled every thousand-th element of a range, and plotted the overall
input and output ranges. Interesting results, but learned that this
still would be a huge undertaking.

##### Finding some local mininums

From the graphic it became clear to me that I could visually search for areas
around a local minimum. Doing this iteratively while making the sampled
ranges bigger (every 1000th, 100th, 10th, 5th etc), led me to smaller
attainable ranges to search for a minimum. After some iterations I
finally found a minimum and.... It was correct!

##### Plotting in the terminal

I used [termplotlib](https://github.com/nschloe/termplotlib),
which made plotting to the terminal easy, as it mimics matloblib a little.
In the end plotting ranges of 10^8 - 10^10 integers, was not considered fun,
and took longer than doing the calculations. But hey, it looks nice :-)

### Day 5

#### Lists and Mutable objects

Today was about ordering lists in such a way that they satisfie the given ordering-conditions.
Part 1 was about determining the correctly ordered lists.
In part 2 there the exercise was to correct those lists that were not
following the conditions.

For me there were to things nice to use / learn. Doing very basic list operations:

- `list.pop()`
- `list.insert()`
- `list.index()`

Which was very useful in this exercise.

I also used another basic Python type, which I rarely use effectively: `set`!
To determine if an ordering is applicable to an instruction (update / row) I use:

```python
ordering = {4,2}
instruction = {1,2,3,4}
ordering.issubset(instruction)
```

But I got bitten by the mutability of lists, so I want to learn more about that soon.
