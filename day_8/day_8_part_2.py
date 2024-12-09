from itertools import product
from time import sleep


def read_lines(path: str = "./input_day_x.txt"):
    with open(path) as f:
        lines = []
        lines = f.readlines()

        assert len(lines) > 0

    return [[c for c in line if c != "\n"] for line in lines]


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


class Format:
    BOLD = "\033[1m"
    FAINT = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    NEGATIVE = "\033[7m"
    CROSSED = "\033[9m"


def print_grid(lines: list[list[str]]):
    for line in lines:
        print("".join(line))


def add_and_sub_diff_to_coords(
    diff: tuple[int, int], the_one: tuple[int, int], other: tuple[int, int]
):
    new_coords = set()
    # I wanted to pick a sensible amount. but fuck it.
    for multi in range(X_BOUNDARY + Y_BOUNDARY):
        # I wnated to use nice functions that would have add and substract
        # but then I saw the perfomance penalty. Oneliner functions are not
        # worth it...
        new_coords.add((the_one[0] - (diff[0] * multi), the_one[1] - diff[1] * multi))
        new_coords.add((other[0] - (diff[0] * multi), other[1] - diff[1] * multi))
        new_coords.add((the_one[0] + (diff[0] * multi), the_one[1] + diff[1] * multi))
        new_coords.add((other[0] + (diff[0] * multi), other[1] + diff[1] * multi))
    # for part 2 we actually do not want to discard the antenna's themselves
    # because of the introduced harmonic frequencies...
    return new_coords


def find_anti_antennas(input_file_name: str):
    # read input
    lines = read_lines(input_file_name)
    new_lines = read_lines(input_file_name)

    list_of_sets_of_chars = [set(line) for line in lines]
    # we also need a list of all elements so we can do a count later
    flat_list = [c for line in lines for c in line]

    antenna_chars = set()
    for set_of_chars_on_a_line in list_of_sets_of_chars:
        antenna_chars = antenna_chars.union(set_of_chars_on_a_line)

    antenna_chars.remove(".")
    all_antennas = set()
    for antenna_char in antenna_chars:
        # if there is only one of the char,
        if flat_list.count(antenna_char) <= 1:
            # then they also don't count as harmonic resonance antenna
            continue
        char_locations = set()
        for y_coord, line in enumerate(lines):
            for x_coord, char in enumerate(line):
                if char == antenna_char:
                    char_locations.add((x_coord, y_coord))

        locations_form_product = product(char_locations, repeat=2)
        two_locations = set(two for two in locations_form_product if two[0] != two[1])

        anti_antennas = set()
        for one, other in two_locations:
            diff_pair = (one[0] - other[0], one[1] - other[1])
            anti_antennas_for_pair = add_and_sub_diff_to_coords(diff_pair, one, other)
            anti_antennas = anti_antennas.union(anti_antennas_for_pair)

        x_bound = len(lines[0])
        y_bound = len(lines)
        anti_antennas = {
            antenna
            for antenna in anti_antennas
            if antenna[0] >= 0
            and antenna[0] < x_bound
            and antenna[1] >= 0
            and antenna[1] < y_bound
        }
        all_antennas = all_antennas.union(anti_antennas)
        for x, y in anti_antennas:
            if new_lines[y][x] == ".":
                new_lines[y][x] = Color.LIGHT_GREEN + "#" + Color.RESET
            else:
                new_lines[y][x] = Color.LIGHT_CYAN + new_lines[y][x] + Color.RESET
        # more to show, thus speeding the animation up
        sleep(0.05)
        print(chr(27) + "[2J")
        print_grid(new_lines)
    return all_antennas, new_lines


input_file_name = "./input_day_x.txt"
# input_file_name = "./input_day_x_example.txt"

# clear terminal input again
print(chr(27) + "[2J")
initial_lines = read_lines(input_file_name)
print_grid(initial_lines)
X_BOUNDARY = len(initial_lines[0])
Y_BOUNDARY = len(initial_lines)

# DO IT
all_anti_antennas, new_lines = find_anti_antennas(input_file_name)

print(len(all_anti_antennas))

# print a comparison when we run the example
if "example" in input_file_name:
    expected = """##....#....#
    .#.#....0...
    ..#.#0....#.
    ..##...0....
    ....0....#..
    .#...#A....#
    ...#..#.....
    #....#.#....
    ..#.....A...
    ....#....A..
    .#........#.
    ...#......##"""
    for line, expected_line in zip(expected.splitlines(), new_lines):
        print(f"{''.join(expected_line)} {line}")

    assert len(all_anti_antennas) == 34
else:
    # else just assert that we didnt mess up
    assert len(all_anti_antennas) == 1150
print("done")
