from typing import Literal
# from functools import cache

Direction = Literal["^", "<", ">", "v"]
Postition = tuple[int, int]
Grid = list[list[str]]


# @cache
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


def print_grid(grid):
    for line in grid:
        print("".join(line))


def determine_move(direction: Direction, x: int, y: int, grid: Grid):
    if direction == "^" and y - 1 >= 0:
        y = y - 1
        if grid[y][x] == "#":
            y = y + 1
            direction = ">"
        return x, y, direction
    elif direction == ">":
        x = x + 1
        if grid[y][x] == "#":
            x = x - 1
            direction = "v"
        return x, y, direction
    elif direction == "v":
        y = y + 1
        if grid[y][x] == "#":
            y = y - 1
            direction = "<"
        return x, y, direction
    elif direction == "<" and x - 1 >= 0:
        x = x - 1
        if grid[y][x] == "#":
            x = x + 1
            direction = "^"
        return x, y, direction
    else:
        raise IndexError("Out of bounds")


def move_guard_in_grid(
    grid: Grid,
    x: int,
    y: int,
    direction: Direction,
):
    prev_positions = set()
    try:
        while True:
            if (direction, x, y) in prev_positions:
                return (direction, x, y)
            prev_positions.add((direction, x, y))
            x, y, direction = determine_move(direction, x, y, grid)
            grid[y][x] = direction
    except IndexError:
        pass


lines = read_lines("./input_day_6.txt")
x, y, direction = find_guard(lines)
move_guard_in_grid(lines, x, y, direction)


def main():
    lines = read_lines("./input_day_6.txt")
    x, y, direction = find_guard(lines)
    max_line = len(lines[0])
    loop_locs = []
    for idy in range(len(lines)):
        for idx in range(max_line):
            lines = read_lines("./input_day_6.txt")
            lines[idy][idx] = "#"
            loc = move_guard_in_grid(lines, x, y, direction)
            if loc:
                loop_locs.append(loc)
    return len(loop_locs)


places_to_put_some_crap = main()
assert places_to_put_some_crap == 1688
print(places_to_put_some_crap)
