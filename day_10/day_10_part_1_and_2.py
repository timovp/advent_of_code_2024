from helper_functions import read_lines, clc, Color


class Map:
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
        if loc.height == 9:
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

    def is_right_traillocation(self, map: Map) -> bool:
        try:
            return self.height + 1 == map.grid[self.y][self.x + 1].height
        except IndexError:
            return False

    def is_left_traillocation(self, map: Map) -> bool:
        if self.x - 1 < 0:
            return False
        try:
            return self.height + 1 == map.grid[self.y][self.x - 1].height

        except IndexError:
            return False

    def is_up_traillocation(self, map: Map) -> bool:
        if self.y - 1 < 0:
            return False
        try:
            return self.height + 1 == map.grid[self.y - 1][self.x].height

        except IndexError:
            return False

    def is_down_traillocation(self, map: Map) -> bool:
        try:
            return self.height + 1 == map.grid[self.y + 1][self.x].height
        except IndexError:
            return False

    def get_left(self, map: Map) -> "TrailLocation":
        return map.grid[self.y][self.x - 1]

    def get_right(self, map: Map) -> "TrailLocation":
        return map.grid[self.y][self.x + 1]

    def get_down(self, map: Map) -> "TrailLocation":
        return map.grid[self.y + 1][self.x]

    def get_up(self, map: Map) -> "TrailLocation":
        return map.grid[self.y - 1][self.x]

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

    def add(self, loc: TrailLocation, map: Map) -> None:
        self.locations.append(loc)
        if loc.height == 9:
            self.rating += 1
        map.colorize_traillocation(loc)

    def look_for_new_locs(self, loc: TrailLocation, map: Map) -> Map:
        if loc.is_left_traillocation(map):
            self.add(loc.get_left(map), map)
        if loc.is_right_traillocation(map):
            self.add(loc.get_right(map), map)
        if loc.is_down_traillocation(map):
            self.add(loc.get_down(map), map)
        if loc.is_up_traillocation(map):
            self.add(loc.get_up(map), map)
        map.print_grid(self)
        return map

    def deduplicate(self) -> set[TrailLocation]:
        set_of_locs = set()
        for loc in self.locations:
            set_of_locs.add((loc.x, loc.y, loc.height))
        return set(self.locations)

    def get_number_nines(self) -> int:
        number = 0
        for loc in self.deduplicate():
            if loc.height == 9:
                number += 1
        return number

    def __repr__(self) -> str:
        return "[" + ",".join([str(c) for c in self.locations]) + "]"


def color_trail(map: Map, zero: TrailLocation) -> tuple[int, int]:
    trail = Trail()
    trail.locations.append(zero)
    map = trail.look_for_new_locs(zero, map)
    for loc in trail.locations:
        map = trail.look_for_new_locs(loc, map)
    return trail.get_number_nines(), trail.rating


lines = read_lines("./input_day_x_example.txt")
# lines = read_lines("./input_day_x.txt")
map = Map(lines)
trail_count = 0
total_rating = 0
for zero in map.zeros():
    map = Map(lines)
    map.make_loc_green(zero)
    counter, rating = color_trail(map, zero)
    trail_count += counter
    total_rating += rating

print(f"{trail_count=}")
print(f"{total_rating=}")
print(f"{total_rating/2=}")
print("done")
