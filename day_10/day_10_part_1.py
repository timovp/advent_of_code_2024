def read_lines(path: str = "./input_day_x.txt"):
    with open(path) as f:
        lines = []
        lines = f.readlines()

        assert len(lines) > 0

    return [[str(c) for c in line.rstrip("\n")] for line in lines]


class Color:
    # Reset
    RESET = "\033[0m"

    # Standard Colors
    BLACK = "\033[0;30m"
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    BROWN = "\033[0;33m"
    BLUE = "\033[0;34m"
    PURPLE = "\033[0;35m"
    CYAN = "\033[0;36m"
    LIGHT_GRAY = "\033[0;37m"

    # Bright Colors
    DARK_GRAY = "\033[1;30m"
    LIGHT_RED = "\033[1;31m"
    LIGHT_GREEN = "\033[1;32m"
    YELLOW = "\033[1;33m"
    LIGHT_BLUE = "\033[1;34m"
    LIGHT_PURPLE = "\033[1;35m"
    LIGHT_CYAN = "\033[1;36m"
    WHITE = "\033[1;37m"


class Map:
    def __init__(self, lines: list[list[str]]):
        self.lines = lines
        self.grid = [[0 for _ in row] for row in lines]
        self.colored = lines
        self.nrows = len(lines)
        self.ncols = len(self.grid[0])
        for y, row in enumerate(lines):
            for x, c in enumerate(row):
                self.grid[y][x] = int(c)

    def print_grid(self):
        for line in self.colored:
            print("".join(str(c) for c in line))

    def make_zero_green(self):
        for idy, line in enumerate(self.colored):
            for idx, c in enumerate(line):
                location = TrailLocation(idx, idy, int(c))
                if location.is_head():
                    self.colored[idy][idx] = Color.LIGHT_GREEN + c + Color.RESET
                    return location
        raise AssertionError("bad. ")


class TrailLocation:
    def __init__(self, x: int, y: int, height: int):
        self.x = x
        self.y = y
        self.height = height

    def is_head(self):
        return self.height == 0

    def is_right_trail(self, map: Map):
        return self.height + 1 == map.grid[self.y][self.x + 1]

    def is_left_trail(self, map: Map):
        return self.height + 1 == map.grid[self.y][self.x - 1]

    def is_up_trail(self, map: Map):
        return self.height + 1 == map.grid[self.y - 1][self.x]

    def is_down_trail(self, map: Map):
        return self.height + 1 == map.grid[self.y + 1][self.x]

    def is_dead_end(self, map: Map):
        return not any(
            [
                self.is_down_trail(map),
                self.is_up_trail(map),
                self.is_right_trail(map),
                self.is_left_trail(map),
            ]
        )


lines = read_lines("./input_day_x_example.txt")
map = Map(lines)
map.colored = lines
first_zero = map.make_zero_green()
map.print_grid()
print(f"{first_zero.is_dead_end(map)}")


print("done")
