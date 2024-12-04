def read_lines(path: str = "./input_day_4.txt"):
    with open(path) as f:
        lines = []
        lines = f.readlines()

        assert len(lines) > 0

    return [[c for c in line.replace("\n", "")] for line in lines]


def check_for_xmas(x, y, lines):
    # if our middle point is not an A we dont care about it.
    if lines[y][x] != "A":
        return 0
    # first check for boundary conditions
    # we cannot catch this with below index error
    # because the -1 index is 'the last' of a list.
    # annoying. I know.
    if x < 1 or y < 1:
        return 0
    # In case we are beyond the boundaries of our 'lines'-matarix
    # we get an index error, and we don't care about it.
    try:
        up_left = lines[y - 1][x - 1]
        up_right = lines[y - 1][x + 1]
        down_left = lines[y + 1][x - 1]
        down_right = lines[y + 1][x + 1]
        # we make a set instead of list because checking for existance is faster.
        surrounds = {up_left, up_right, down_right, down_left}
    except IndexError:
        return 0
    # if any of the interesting surrounds is an X or an A, we dont care.
    if "X" in surrounds or "A" in surrounds:
        return 0
    # if across from the A the elements are equal, then its not an x mas.
    elif (up_left == down_right) or (up_right == down_left):
        return 0
    # but in the right order: side to side, we do want it!
    elif up_left == up_right and down_left == down_right:
        return 1
    elif up_left == down_left and up_right == down_right:
        return 1
    # profiling shows that we never actually reach this, but to make my
    # lsp not complain I just wrote it down.
    return 0


def do_day_4_part_2(lines: list[list[str]]):
    num_of_xmas = 0
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            num_of_xmas += check_for_xmas(x, y, lines)

    return num_of_xmas


lines = read_lines("input_day_4.txt")

num_of_xmas = do_day_4_part_2(lines)
assert num_of_xmas == 1900
print(num_of_xmas)
print("done")
