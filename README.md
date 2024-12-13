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

### Day 6

#### Animations

Inspired by others I obviously wanted to make this look cool.
In essence the exercise was quite simple, given conditions let a guard walk over
a map with objects standing in the way. As the guard was moving one square at a
time, this was perfect to try to animate.

Two learnings here:

- One, dont always print the full example. It usually does not fit the terminal window.
- Two, use special ansi character combinations to clear the screen so everytime you
print a new frame of your video to the terminal it starts whit a fresh canvas.

```python
print(chr(27) + "[2J") # clears the terminal
```

#### Part 2: optimization

So I struggled way too long on this solution. In the end I stopped searching for
elegant solutions and just bruteforced it. My first solution that produced the
correct answer took something like 2m45s. Profiling made me realize there were
a lot of improvements to make. I created seperate first between the initial
solution that didnt work, and the 24 second and the 17 second solutions.

The main takeaway is that when you do only really basic operations in Python,
such as list operations or integer artihmetic, the small things start to matter too!
For example, I leaned that creating variables and doing function calls are
super expensive operations. I was able to reduce the 2m45s to 37 seconds by
just reducing the number of function calls. Then I kept one function helper function
which did the moving of the guard and the searching for new obstacle locations.
Inside that final function I reduced any unneeded variable creations and assignments.

Below are extracts of the relevant sections, comparing variable creation and
function calls. I think it gets very clear from it why this how relatively
expensive the operations are comperatively.

```text
Total time: 67.3261 s
File: day_6_part_2_24seconds.py
Function: determine_move at line 33
Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    33                                           def determine_move(direction: Direction, x: int, y: int, grid: Grid):
    34  78712874   10606834.0      0.1     15.8      if direction == "^" and y - 1 >= 0:
    35  18742823    2302728.4      0.1      3.4          y = y - 1
    36  18742823    3646125.8      0.2      5.4          if grid[y][x] == "#":
    37    568459     103359.0      0.2      0.2              y = y + 1
    38    568459      59302.6      0.1      0.1              direction = ">"
    39  18742823    6314459.4      0.3      9.4          return x, y, direction
    40  59970051    7348720.7      0.1     10.9      elif direction == ">":
    41  20002108    2534413.8      0.1      3.8          x = x + 1
    42  20002108    3246405.3      0.2      4.8          if grid[y][x] == "#":
    43    567340      85986.3      0.2      0.1              x = x - 1
    44    567340      59260.8      0.1      0.1              direction = "v"
    45  20001484    3148008.8      0.2      4.7          return x, y, direction
    46  39967943    4998198.0      0.1      7.4      elif direction == "v":
    47  19452295    2176258.4      0.1      3.2          y = y + 1
    48  19452295    3484941.1      0.2      5.2          if grid[y][x] == "#":
    49    553149      75794.3      0.1      0.1              y = y - 1
    50    553149      55586.9      0.1      0.1              direction = "<"
    51  19438410    4011168.3      0.2      6.0          return x, y, direction
    52  20515648    3283676.1      0.2      4.9      elif direction == "<" and x - 1 >= 0:
    53  20514944    2393408.8      0.1      3.6          x = x - 1
    54  20514944    3542918.3      0.2      5.3          if grid[y][x] == "#":
    55    552436      71488.3      0.1      0.1              x = x + 1
    56    552436      52663.7      0.1      0.1              direction = "^"
    57  20514944    3722037.9      0.2      5.5          return x, y, direction
    58                                               else:
    59       704       2345.2      3.3      0.0          raise IndexError("Out of bounds")
Total time: 279.632 s
File: day_6_part_2_24seconds.py
Function: move_guard_in_grid at line 62
Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    62                                           def move_guard_in_grid(
    63                                               grid: Grid,
    64                                               x: int,
    65                                               y: int,
    66                                               direction: Direction,
    67                                           ):
    68     16901      12468.1      0.7      0.0      prev_positions = set()
    69     16901       3734.5      0.2      0.0      try:
    70  78714562    6742524.0      0.1      2.4          while True:
    71  78714562   14811654.2      0.2      5.3              if (direction, x, y) in prev_positions:
    72      1688        243.3      0.1      0.0                  return (direction, x, y)
    73  78712874   18386215.4      0.2      6.6              prev_positions.add((direction, x, y))
    74  78712874  228227021.6      2.9     81.6              x, y, direction = determine_move(direction, x, y, grid)
    75  78697661   11415139.0      0.1      4.1              grid[y][x] = direction
    76     15213      19061.8      1.3      0.0      except IndexError:
    77     15213      14060.8      0.9      0.0          pass
```

Here we see that we spend while profiling about 80 of the time on line 74 and we call the determine_move function.
But comparing how much time we actually were in inside the function, it nicely and evenly distributed. (only 60s)
Now have a look at below where I basically placed the entire function inside the other function:

```text
Total time: 111.945 s
File: day_6_part_2_17seconds.py
Function: move_guard_in_grid at line 26
Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    26                                           def move_guard_in_grid(
    27                                               grid: Grid,
    28                                               x: int,
    29                                               y: int,
    30                                               direction: Direction,
    31                                           ):
    32                                               # we keep track of positions where we've been.
    33                                               # a set is nice and fast when doing 'element in' tests
    34     16900      11099.4      0.7      0.0      prev_positions = set()
    35     16900       2639.1      0.2      0.0      try:
    36  78709330    6901849.2      0.1      6.2          while True:
    37                                                       # first we check if we arrived in a loop
    38                                                       # we consider to be in a loop if we face the same direction
    39                                                       # at a location we've visited before
    40  78709330   15673192.9      0.2     14.0              if (direction, x, y) in prev_positions:
    41      1688        526.9      0.3      0.0                  return (direction, x, y)
    42                                                       # if we don't return, we add it to the list.
    43  78707642   22445828.3      0.3     20.1              prev_positions.add((direction, x, y))
    44                                                       # if our direction is "^" up. and we not at the top
    45  78707642   12213790.4      0.2     10.9              if direction == "^" and y - 1 >= 0:
    46                                                           # then we can move upward
    47  18741586    2394372.3      0.1      2.1                  y = y - 1
    48                                                           # however if we moved forward ontop of an object ("#")
    49  18741586    3798875.9      0.2      3.4                  if grid[y][x] == "#":
    50                                                               # then we move back and rotate
    51    568421      86937.7      0.2      0.1                      y = y + 1
    52    568421      61792.3      0.1      0.1                      direction = ">"
    53                                                       # similarly for if we are facing right, but now
    54                                                       # we don't have to fear an index of -1
    55  59966056    7324475.6      0.1      6.5              elif direction == ">":
    56  20000774    2480035.3      0.1      2.2                  x = x + 1
    57  20000774    3486051.8      0.2      3.1                  if grid[y][x] == "#":
    58    567302      84429.9      0.1      0.1                      x = x - 1
    59    567302      58932.7      0.1      0.1                      direction = "v"
    60  39965282    4833814.7      0.1      4.3              elif direction == "v":
    61  19451004    2538420.2      0.1      2.3                  y = y + 1
    62  19451004    4006223.8      0.2      3.6                  if grid[y][x] == "#":
    63    553112      83701.8      0.2      0.1                      y = y - 1
    64    553112      57803.9      0.1      0.1                      direction = "<"
    65  20514278    3932881.0      0.2      3.5              elif direction == "<" and x - 1 >= 0:
    66  20513574    2652180.7      0.1      2.4                  x = x - 1
    67  20513574    3592516.6      0.2      3.2                  if grid[y][x] == "#":
    68    552399      79425.8      0.1      0.1                      x = x + 1
    69    552399      58961.3      0.1      0.1                      direction = "^"
    70                                                       else:
    71                                                           # we only arrive here if we are actually out of bounds up or left
    72                                                           # so we never found a loop
    73       704        176.7      0.3      0.0                  break
    74                                                       # now that determined the new x and y and direction for our move
    75                                                       # we can do the actual move.
    76  78692430   13053155.0      0.2     11.7              grid[y][x] = direction
    77                                               # if at any moment we we're actually going out of bounds right or down,
    78                                               # an IndexError will be raised
    79     14508      20738.2      1.4      0.0      except IndexError:
    80     14508       9964.6      0.7      0.0          pass
```

Now you cannot 1 for 1 compare the 222 seconds with the 111 seconds. But more interestingly, other opeartions in the function, that have not changed 
take relative more time. So line 76, `grid[x][y] = direction` is taking 11.7% of the time while before only 4.1%. Which tells me, that whatever else there was taking up time, now is taking a hell of a lot shorter!
Please note that execution time is very slow compared to execution time without profiling, definitely when there are so many function calls we profile.
But that does not take away that we can see from just putting the function "inline-refactored" in the other function we get a 2-3x speed improvement.

#### Inline Refactor

If you never looked it up. It's a very convenient tool, well implemented in basically [any editor](https://www.jetbrains.com/help/pycharm/inline.html) except VS Code.
To be honest, it was one of the final nails in the coffin to try Neovim for me: that there was [an extension](https://github.com/ThePrimeagen/refactoring.nvim) that did this.
THe refactoring extension does not always work, but when it does, it feels like magic.

### Day 7

#### Evil Eval

This time I was quite prod of the elegance of my solution.  
But and there is a big butt.
I admit. I used `eval`. I know. Im really sorry. Please forgive me.

#### I made the right choice. For once

So this time I am not only proud of the elegance, I'm way more proud of the fact
that I was able to write part 1 in such a way that I needed to change practically
3 characters to get to the solution of part 2.
Finally, no major rewrites to get to the answer!

### Day 8

#### Colors
So day 8 was not super hard, but, but lended itself perfectly for another try at visuals. I need to figure out how to share videos or gifs here.
But, major learning, are more on the terminal printing side and those ansi keycodes. I made a class for it even, that contains all available keycodes

```python
string_to_print:str = Color.LIGHT_GREEN + "some_string" + Color.RESET
```

### Day 9

#### I dont want to talk about it

Well again I made my own visual debuger which was fun on its own so my solution looked like this, but then colors ring the 
free space and the piece that will move (so on the second line the `99` and the first `..`). Again, will look into embeddinges later.

```text
00...111...2...333.44.5555.6666.777.888899
00...111...2...333.44.5555.6666.777.88889️9
0099.111...2...333.44.5555.6666.777.8888..
0099.1117772...333.44.5555.6666.....8888..
0099.111777244.333....5555.6666.....8888..
```
