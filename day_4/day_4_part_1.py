def read_lines(path: str = "./input_day_4.txt"):
    with open(path) as f:
        lines = []
        lines = f.readlines()

        assert len(lines) > 0

    return [line.replace("\n", "") for line in lines]


def find_horz(x: int, y: int, lines: list[str]):
    return lines[y][x : x + 4]


def find_vert(x: int, y: int, lines: list[str]):
    return "".join([line[x] for line in lines[y : y + 4]])


def find_diag(x, y, lines):
    try:
        one = lines[y][x]
        two = lines[y + 1][x + 1]
        three = lines[y + 2][x + 2]
        four = lines[y + 3][x + 3]
    except IndexError:
        return ""
    return "".join([one, two, three, four])


def find_other_diag(x, y, lines):
    if x <= 2:
        return ""
    try:
        one = lines[y][x]
        two = lines[y + 1][x - 1]
        three = lines[y + 2][x - 2]
        four = lines[y + 3][x - 3]
    except IndexError:
        return ""
    return "".join([one, two, three, four])


def empty_10x10():
    return [["." for _ in range(10)] for _ in range(10)]


def empty_x_by_y(x: int, y: int):
    return [["." for _ in range(x)] for _ in range(y)]


def is_xmas(x, y, lines, res):
    # finding the correct xmas stuff isnt that hard
    horz = find_horz(x, y, lines)
    vert = find_vert(x, y, lines)
    diag = find_diag(x, y, lines)
    diag_vert = find_other_diag(x, y, lines)
    counter = 0
    # but what is hard, is visualizing them as they are found
    # well also not really hard, but it took some rewriting
    # as i couldn't recycle the finding logic in this set up.
    if horz in {"XMAS", "SAMX"}:
        counter += 1
        res[y][x] = horz[0]
        res[y][x + 1] = horz[1]
        res[y][x + 2] = horz[2]
        res[y][x + 3] = horz[3]

    if vert in {"XMAS", "SAMX"}:
        counter += 1
        res[y][x] = vert[0]
        res[y + 1][x] = vert[1]
        res[y + 2][x] = vert[2]
        res[y + 3][x] = vert[3]

    if diag in {"XMAS", "SAMX"}:
        counter += 1
        res[y][x] = diag[0]
        res[y + 1][x + 1] = diag[1]
        res[y + 2][x + 2] = diag[2]
        res[y + 3][x + 3] = diag[3]

    if diag_vert in {"XMAS", "SAMX"}:
        counter += 1
        res[y][x] = diag_vert[0]
        res[y + 1][x - 1] = diag_vert[1]
        res[y + 2][x - 2] = diag_vert[2]
        res[y + 3][x - 3] = diag_vert[3]
    return counter, res


def do_example():
    lines = read_lines("./input_day_4_example.txt")
    print("---do the example------")
    print()
    for line in lines:
        print(line)

    res = empty_10x10()

    assert find_horz(5, 0, lines) == "XMAS"
    total = 0
    for y in range(0, len(lines)):
        for x in range(0, len(lines[0])):
            counter, res = is_xmas(x, y, lines, res)
            total += counter
    print()

    example_answer = [
        "....XXMAS.",
        ".SAMXMS...",
        "...S..A...",
        "..A.A.MS.X",
        "XMASAMX.MM",
        "X.....XA.A",
        "S.S.S.S.SS",
        ".A.A.A.A.A",
        "..M.M.M.MM",
        ".X.X.XMASX",
    ]
    for row, ex in zip(res, example_answer):
        # printing both next to each other and adding a checkmark if they are the same.
        # sounds silly, but looks super satisfying.
        print(f"{''.join(row)} | {ex} {'✅' if ''.join(row) == ex else '❌'}")

    print()
    print(f"{total=}")
    print()
    return total


def do_the_work():
    lines = read_lines()
    res = empty_x_by_y(len(lines[0]), len(lines))
    print("-----do the real work----")
    total = 0
    for y in range(0, len(lines)):
        for x in range(0, len(lines[0])):
            counter, res = is_xmas(x, y, lines, res)
            total += counter
    print()
    for row in res:
        print(f"{''.join(row)}")
    print()
    print(f"{total=}")
    print()
    return total


total = do_the_work()
assert total == 2427
total_example = do_example()
assert total_example == 18
print("done")
