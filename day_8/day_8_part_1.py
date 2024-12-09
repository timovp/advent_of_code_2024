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


def coord_add(coord: tuple[int, int], diff: tuple[int, int]) -> tuple[int, int]:
    return (coord[0] + diff[0], coord[1] + diff[1])


def coord_sub(coord: tuple[int, int], diff: tuple[int, int]) -> tuple[int, int]:
    return (coord[0] - diff[0], coord[1] - diff[1])


def add_and_sub_diff_to_coords(
    diff: tuple[int, int], coord_pair: tuple[tuple[int, int], tuple[int, int]]
):
    new_coords = set()
    new_coords.add(coord_sub(coord_pair[0], diff))
    new_coords.add(coord_sub(coord_pair[1], diff))
    new_coords.add(coord_add(coord_pair[0], diff))
    new_coords.add(coord_add(coord_pair[1], diff))
    new_coords.discard(coord_pair[0])
    new_coords.discard(coord_pair[1])
    return new_coords


def find_anti_antennas(input_file_name: str):
    # read input
    lines = read_lines(input_file_name)
    # retreive another grid of input so we can overwrite those for visualization
    new_lines = read_lines(input_file_name)

    # collect all potential characters that could form antenna pairs
    list_of_sets_of_chars = [set(line) for line in lines]
    antenna_chars = set()
    # loop through that list of sets
    for set_of_chars_on_a_line in list_of_sets_of_chars:
        # put them all in one big set
        antenna_chars = antenna_chars.union(set_of_chars_on_a_line)
    # the empty space is denoted with a `"."`.
    antenna_chars.remove(".")
    # define overarching set of antennas
    all_antennas = set()
    # loop over each antenna option
    for antenna_char in antenna_chars:
        # look for this charachter in the grid and store the location
        char_locations = set()
        # loop through each row and column, while keeping track of the indexes
        for idy, line in enumerate(lines):
            for idx, char in enumerate(line):
                # if we find it
                if char == antenna_char:
                    # we store its location in char locations
                    char_locations.add((idx, idy))
        # No use itertools.product to create tuples of length two for all
        # locations, creating all possible pairs of locations.
        locations_from_product = product(char_locations, repeat=2)
        # all possible pairs include pairs with locations with themself, so we exclude those
        two_locations = set(two for two in locations_from_product if two[0] != two[1])

        # we again create a set of anti_antennas for our `current antenna_char`
        anti_antennas = set()
        # we loop through pairs of locations to define the two new locations
        for pair in two_locations:
            # we caluclate the difference in x and y coordinate for the pair
            diff_pair = (pair[1][0] - pair[0][0], pair[1][1] - pair[0][1])
            # finally, use that diff to determine the anti_antenna locations
            anti_antennas_for_pair = add_and_sub_diff_to_coords(diff_pair, pair)
            # add the anti-antennas for this pair to the anti-antenna for the antenna.
            anti_antennas = anti_antennas.union(anti_antennas_for_pair)
        # determine boundary (dont forget that 0 is also a boundary!)
        x_bound = len(lines[0])
        y_bound = len(lines)
        # now filter anti_antennas for out of bounds-locations
        anti_antennas_coords = {
            antenna
            for antenna in anti_antennas
            if antenna[0] >= 0
            and antenna[0] < x_bound
            and antenna[1] >= 0
            and antenna[1] < y_bound
        }
        # now add these anti_antennas to the overarching set of antennas
        all_antennas = all_antennas.union(anti_antennas_coords)
        # now do some visually cool stuff:
        # now place a hashtag on each location, when the location is a `'.'`
        for x, y in anti_antennas_coords:
            if new_lines[y][x] == ".":
                # use fancy color codes to print in green ...
                new_lines[y][x] = Color.LIGHT_GREEN + "#" + Color.RESET
            else:
                # ... or in cyan when its an antenna thats also an antinode
                new_lines[y][x] = Color.LIGHT_CYAN + new_lines[y][x] + Color.RESET
        # sleep a little so the previous visual looks nice
        sleep(0.2)
        # clear the screeen
        print(chr(27) + "[2J")
        # print the new visual (with added colors)
        print_grid(new_lines)
    return all_antennas


# define the input file name (uncomment the example name to do the example first)
input_file_name = "./input_day_x.txt"
# input_file_name = "./input_day_x_example.txt"

# unnescecary fancyness ...
# clear terminal window and print grid before any edit
print(chr(27) + "[2J")
print_grid(read_lines(input_file_name))
# sleep so the cool animations are more impressive
sleep(1)
# now do stuff
all_anti_antennas = find_anti_antennas(input_file_name)
# assertion to make sure any future edits don't break the code
assert len(all_anti_antennas) == 14 or len(all_anti_antennas) == 305
print(len(all_anti_antennas))
print("done")
