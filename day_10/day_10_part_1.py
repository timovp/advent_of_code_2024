from helper_functions import Color, read_lines, clc
from hashlib import md5


class Map:
    def __init__(self, lines: list[list[str]]):
        self.lines = lines
        self.grid = [[0 for _ in row] for row in self.lines]
        self.colored = [[str(c) for c in line] for line in lines]
        self.nrows = len(lines)
        self.ncols = len(self.grid[0])
        for y, row in enumerate(self.lines):
            for x, c in enumerate(row):
                self.grid[y][x] = int(c)

    def print_grid(self, rating: int | None = None):
        clc()
        for line in self.colored:
            print("".join(str(c) for c in line))
        print("-" * self.ncols)
        print(f"{rating}")
        print("-" * self.ncols)

    def make_zero_green(self) -> "TrailLocation":
        for idy, line in enumerate(self.colored):
            for idx, c in enumerate(line):
                location = TrailLocation(idx, idy, int(c))
                if location.is_head():
                    self.colored[idy][idx] = Color.LIGHT_GREEN + c + Color.RESET
                    return location
        raise AssertionError("bad. ")

    def make_loc_blue(self, loc: "TrailLocation"):
        self.colored[loc.y][loc.x] = Color.LIGHT_BLUE + str(loc.height) + Color.RESET

    def make_loc_red(self, loc: "TrailLocation"):
        self.colored[loc.y][loc.x] = Color.LIGHT_RED + str(loc.height) + Color.RESET

    def make_loc_green(self, loc: "TrailLocation"):
        self.colored[loc.y][loc.x] = Color.LIGHT_GREEN + str(loc.height) + Color.RESET

    def color_loc(self, loc: "TrailLocation"):
        if loc.height == 9:
            self.make_loc_red(loc)
        elif loc.height == 0:
            self.make_loc_green(loc)
        else:
            self.make_loc_blue(loc)

    def zeros(self) -> list["TrailLocation"]:
        locs = []
        for y, row in enumerate(self.grid):
            for x, c in enumerate(row):
                if c == 0:
                    locs.append(TrailLocation(x, y, c))
        return locs

    def reset_colors(self):
        self.colored = [[str(c) for c in line] for line in self.lines]


class TrailLocation:
    def __init__(self, x: int, y: int, height: int) -> None:
        self.x = x
        self.y = y
        self.height = height

    def is_head(self) -> bool:
        return self.height == 0

    def is_right_trail(self, map: Map) -> bool:
        try:
            return self.height + 1 == map.grid[self.y][self.x + 1]
        except IndexError:
            return False

    def is_left_trail(self, map: Map) -> bool:
        if self.x - 1 < 0:
            return False
        try:
            return self.height + 1 == map.grid[self.y][self.x - 1]
        except IndexError:
            return False

    def is_up_trail(self, map: Map) -> bool:
        if self.y - 1 < 0:
            return False
        try:
            return self.height + 1 == map.grid[self.y - 1][self.x]
        except IndexError:
            return False

    def is_down_trail(self, map: Map) -> bool:
        try:
            return self.height + 1 == map.grid[self.y + 1][self.x]
        except IndexError:
            return False

    def is_dead_end(self, map: Map) -> bool:
        return not any(
            [
                self.is_down_trail(map),
                self.is_up_trail(map),
                self.is_right_trail(map),
                self.is_left_trail(map),
            ]
        )

    def get_left(self, map: Map) -> "TrailLocation":
        height = map.grid[self.y][self.x - 1]
        return TrailLocation(self.x - 1, self.y, height)

    def get_right(self, map: Map) -> "TrailLocation":
        height = map.grid[self.y][self.x + 1]
        return TrailLocation(self.x + 1, self.y, height)

    def get_down(self, map: Map) -> "TrailLocation":
        height = map.grid[self.y + 1][self.x]
        return TrailLocation(self.x, self.y + 1, height)

    def get_up(self, map: Map) -> "TrailLocation":
        height = map.grid[self.y - 1][self.x]
        return TrailLocation(self.x, self.y - 1, height)

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
    def __init__(self) -> None:
        self.locations: list[TrailLocation] = []
        self.rating = 0
        self.set_of_locs: set[TrailLocation] = set()

    def add(self, loc: TrailLocation) -> None:
        self.locations.append(loc)
        if loc not in self.set_of_locs:
            self.set_of_locs.add(loc)

    def look_for_new_locs(self, loc: TrailLocation, map: Map) -> Map:
        if loc.is_left_trail(map):
            go_left = loc.get_left(map)
            self.add(go_left)
            map.color_loc(go_left)
            if go_left.height == 9:
                self.rating += 1
        if loc.is_right_trail(map):
            go_right = loc.get_right(map)
            self.add(go_right)
            map.color_loc(go_right)
            if go_right.height == 9:
                self.rating += 1
        if loc.is_down_trail(map):
            go_down = loc.get_down(map)
            self.add(go_down)
            map.color_loc(go_down)
            if go_down.height == 9:
                self.rating += 1
        if loc.is_up_trail(map):
            go_up = loc.get_up(map)
            self.add(go_up)
            map.color_loc(go_up)
            if go_up.height == 9:
                self.rating += 1
        map.print_grid(self.rating)
        return map

    def deduplicate(self) -> set[tuple[int, int, int]]:
        set_of_locs = set()
        for loc in self.locations:
            set_of_locs.add((loc.x, loc.y, loc.height))
        return set_of_locs

    def get_number_nines(self) -> int:
        number = 0
        for loc in self.deduplicate():
            if loc[2] == 9:
                number += 1
        return number

    def __repr__(self) -> str:
        return "[" + ",".join([str(c) for c in self.locations]) + "]"


def color_trail(map: Map, zero: TrailLocation) -> tuple[int, int]:
    trail = Trail()
    trail.locations.append(zero)
    if zero.is_dead_end(map):
        print("first zero is a dead end, no trail possilbe.")
    map = trail.look_for_new_locs(zero, map)
    for loc in trail.locations:
        map = trail.look_for_new_locs(loc, map)
    return trail.get_number_nines(), trail.rating


lines = read_lines("./input_day_x_example.txt")
# lines = read_lines("./input_day_x.txt")
map = Map(lines)
map.colored = lines
trail_count = 0
total_rating = 0
map.reset_colors()
for zero in map.zeros():
    map.make_loc_green(zero)
    counter, rating = color_trail(map, zero)
    trail_count += counter
    total_rating += rating
    map.reset_colors()

print(f"{trail_count=}")
print(f"{total_rating=}")
print(f"{total_rating/2=}")
print("done")
