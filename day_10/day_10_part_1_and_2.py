from time import sleep

from helper_functions import (
    Color,
    Cursor,
    clc,
    get_cursor_position,
    print_empty_lines,
    read_lines,
)


class Map:
    MAX_HEIGHT = 9

    def __init__(self, lines: list[list[str]]):
        self.lines = lines
        self.grid: list[list[TrailLocation]] = [
            [TrailLocation(0, 0, 0) for _ in row] for row in self.lines
        ]
        self.colored: list[list[str]] = [[str(c) for c in line] for line in lines]
        self.nrows = len(lines)
        self.ncols = len(self.grid[0])
        for y, row in enumerate(lines):
            for x, c in enumerate(row):
                self.grid[y][x] = TrailLocation(x, y, int(c))

    def print_grid(self, trail: "Trail"):
        clc()
        for line in self.colored:
            print("".join(str(c) for c in line))
        print("-" * self.ncols)
        print(f"{trail.rating}")
        print("-" * self.ncols)

    def make_loc_blue(self, loc: "TrailLocation") -> None:
        self.colored[loc.y][loc.x] = Color.LIGHT_BLUE + str(loc.height) + Color.RESET

    def make_loc_red(self, loc: "TrailLocation") -> None:
        self.colored[loc.y][loc.x] = Color.LIGHT_RED + str(loc.height) + Color.RESET

    def make_loc_green(self, loc: "TrailLocation") -> None:
        self.colored[loc.y][loc.x] = Color.LIGHT_GREEN + str(loc.height) + Color.RESET

    def colorize_traillocation(self, loc: "TrailLocation") -> None:
        if loc.height == self.MAX_HEIGHT:
            self.make_loc_red(loc)
        elif loc.height == 0:
            self.make_loc_green(loc)
        else:
            self.make_loc_blue(loc)

    def zeros(self) -> list["TrailLocation"]:
        locs = []
        for row in self.grid:
            for c in row:
                if c.height == 0:
                    locs.append(c)
        return locs


class TrailLocation:
    def __init__(self, x: int, y: int, height: int) -> None:
        self.x = x
        self.y = y
        self.height = height

    def is_head(self) -> bool:
        return self.height == 0

    def is_right_traillocation(self, trailmap: Map) -> bool:
        try:
            return self.height + 1 == trailmap.grid[self.y][self.x + 1].height
        except IndexError:
            return False

    def is_left_traillocation(self, trailmap: Map) -> bool:
        if self.x - 1 < 0:
            return False
        try:
            return self.height + 1 == trailmap.grid[self.y][self.x - 1].height

        except IndexError:
            return False

    def is_up_traillocation(self, trailmap: Map) -> bool:
        if self.y - 1 < 0:
            return False
        try:
            return self.height + 1 == trailmap.grid[self.y - 1][self.x].height

        except IndexError:
            return False

    def is_down_traillocation(self, trailmap: Map) -> bool:
        try:
            return self.height + 1 == trailmap.grid[self.y + 1][self.x].height
        except IndexError:
            return False

    def get_left(self, trailmap: Map) -> "TrailLocation":
        return trailmap.grid[self.y][self.x - 1]

    def get_right(self, trailmap: Map) -> "TrailLocation":
        return trailmap.grid[self.y][self.x + 1]

    def get_down(self, trailmap: Map) -> "TrailLocation":
        return trailmap.grid[self.y + 1][self.x]

    def get_up(self, trailmap: Map) -> "TrailLocation":
        return trailmap.grid[self.y - 1][self.x]

    def __repr__(self) -> str:
        return f"({self.x},{self.y}) = {self.height}"

    def __eq__(self, value: object, /) -> bool:
        if not isinstance(value, TrailLocation):
            return False
        return all([value.x == self.x, value.y == self.y, value.height == self.height])

    def __ne__(self, value: object, /) -> bool:
        return not self.__eq__(value)

    def __hash__(self) -> int:
        return hash(self.__repr__())


class Trail:
    MAX_HEIGHT = 9

    def __init__(self) -> None:
        self.locations: list[TrailLocation] = []
        self.rating = 0

    def add(self, loc: TrailLocation, trailmap: Map) -> None:
        self.locations.append(loc)
        if loc.height == self.MAX_HEIGHT:
            self.rating += 1
        trailmap.colorize_traillocation(loc)
        print(trailmap.colored[loc.y][loc.x], end="", flush=False)
        Cursor.left(flush=True)
        sleep(0.05)

    def look_for_new_locs(self, loc: TrailLocation, trailmap: Map) -> Map:
        if loc.is_left_traillocation(trailmap):
            left_loc = loc.get_left(trailmap)
            Cursor.position(left_loc.y + tzero_y, left_loc.x + tzero_x, True)
            self.add(left_loc, trailmap)
        if loc.is_right_traillocation(trailmap):
            right_loc = loc.get_right(trailmap)
            Cursor.position(right_loc.y + tzero_y, right_loc.x + tzero_x, True)
            self.add(right_loc, trailmap)
        if loc.is_down_traillocation(trailmap):
            down_loc = loc.get_down(trailmap)
            Cursor.position(down_loc.y + tzero_y, down_loc.x + tzero_x, True)
            self.add(down_loc, trailmap)
        if loc.is_up_traillocation(trailmap):
            up_loc = loc.get_up(trailmap)
            Cursor.position(up_loc.y + tzero_y, up_loc.x + tzero_x, True)
            self.add(up_loc, trailmap)
        return trailmap

    def deduplicate(self) -> set[TrailLocation]:
        set_of_locs = set()
        for loc in self.locations:
            set_of_locs.add((loc.x, loc.y, loc.height))
        return set(self.locations)

    def get_number_nines(self) -> int:
        number = 0
        for loc in self.deduplicate():
            if loc.height == self.MAX_HEIGHT:
                number += 1
        return number

    def __repr__(self) -> str:
        return "[" + ",".join([str(c) for c in self.locations]) + "]"


def color_trail(trailmap: Map, zero: TrailLocation) -> tuple[int, int]:
    trail = Trail()
    trail.locations.append(zero)
    trailmap = trail.look_for_new_locs(zero, trailmap)
    for loc in trail.locations:
        trailmap = trail.look_for_new_locs(loc, trailmap)
    return trail.get_number_nines(), trail.rating


trail_count = 0
total_rating = 0
lines = read_lines("./input_day_x_example.txt")
trailmap = Map(lines)
trail = Trail()
print_empty_lines(12)
Cursor.up(12, flush=True)
tzero_y, tzero_x = get_cursor_position()
for zero in trailmap.zeros():
    for line in trailmap.lines:
        print("".join(line), flush=False)
    print(end="", flush=True)
    trailmap = Map(lines)
    trailmap.make_loc_green(zero)
    Cursor.position(zero.y + tzero_y, zero.x + tzero_x, True)
    print(trailmap.colored[zero.y][zero.x], end="", flush=True)
    sleep(0.05)
    counter, rating = color_trail(trailmap, zero)
    trail_count += counter
    total_rating += rating
    Cursor.position(tzero_y, tzero_x, False)

Cursor.position(tzero_y + 12, 1, True)
sleep(1)
