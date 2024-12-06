from typing import Literal

Direction = Literal["^", "<", ">", "v"]
Postition = tuple[int, int]
Grid = list[list[str]]


def read_lines(path: str = "./input_day_6.txt"):
    with open(path) as f:
        lines = []
        lines = f.readlines()

        assert len(lines) > 0

    return [[c for c in line.replace("\n", "")] for line in lines]


def find_guard(lines):
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char in {"v", "^", "<", ">"}:
                return x, y, char
    raise ValueError("oops")


def move_guard_in_grid(
    grid: Grid,
    x: int,
    y: int,
    direction: Direction,
):
    # we keep track of positions where we've been.
    # a set is nice and fast when doing 'element in' tests
    prev_positions = set()
    try:
        while True:
            # first we check if we arrived in a loop
            # we consider to be in a loop if we face the same direction
            # at a location we've visited before
            if (direction, x, y) in prev_positions:
                return (direction, x, y)
            # if we don't return, we add it to the list.
            prev_positions.add((direction, x, y))
            # if our direction is "^" up. and we not at the top
            if direction == "^" and y - 1 >= 0:
                # then we can move upward
                y = y - 1
                # however if we moved forward ontop of an object ("#")
                if grid[y][x] == "#":
                    # then we move back and rotate
                    y = y + 1
                    direction = ">"
            # similarly for if we are facing right, but now
            # we don't have to fear an index of -1
            elif direction == ">":
                x = x + 1
                if grid[y][x] == "#":
                    x = x - 1
                    direction = "v"
            elif direction == "v":
                y = y + 1
                if grid[y][x] == "#":
                    y = y - 1
                    direction = "<"
            elif direction == "<" and x - 1 >= 0:
                x = x - 1
                if grid[y][x] == "#":
                    x = x + 1
                    direction = "^"
            else:
                # we only arrive here if we are actually out of bounds up or left
                # so we never found a loop
                break
            # now that determined the new x and y and direction for our move
            # we can do the actual move.
            grid[y][x] = direction
    # if at any moment we we're actually going out of bounds right or down,
    # an IndexError will be raised
    except IndexError:
        pass


def main():
    # ok let's grab the input
    grid = read_lines("./input_day_6.txt")
    # and findout what our staring point is
    x, y, direction = find_guard(grid)
    # determine the column boundary
    max_line = len(grid[0])
    # and create our result list of locations that create a loop
    loop_locs = []
    # loop through rows
    for idy in range(len(grid)):
        # loop through columns
        for idx in range(max_line):
            # get yourself a fresh copy of input (and avoid the slow deepcopy)
            grid = read_lines("./input_day_6.txt")
            # place a # on the track
            grid[idy][idx] = "#"
            # now see if the move guard in grid fucntion ended in a loop
            loc = move_guard_in_grid(grid, x, y, direction)
            # if it does, it's going to return a tuple of the loop location.
            if isinstance(loc, tuple):
                loop_locs.append(loc)
    # return the result to be able to so an assert on results outside this function
    return len(loop_locs)


places_to_put_some_crap = main()
assert places_to_put_some_crap == 1688
print("done")
