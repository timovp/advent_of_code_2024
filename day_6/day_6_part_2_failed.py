import time


def read_lines(path: str = "./input_day_6.txt"):
    with open(path) as f:
        lines = []
        lines = f.readlines()

        assert len(lines) > 0

    return [[c for c in line.replace("\n", "")] for line in lines]


lines = read_lines("./input_day_6.txt")
# lines = read_lines("./input_day_6_example.txt")

# for line in lines:
#     print("".join(line))
print("done")


def find_guard(lines):
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char in {"v", "^", "<", ">"}:
                starting_point = (x, y)
                return starting_point, char
    raise ValueError("oops")


def move_left(x, y):
    if x - 1 < 0:
        raise IndexError("out of bounds!")
    return x - 1, y


def move_right(x, y):
    return x + 1, y


def move_down(x, y):
    return x, y + 1


def move_up(x, y):
    if y - 1 < 0:
        raise IndexError("out of bounds!")
    return x, y - 1


def print_grid(grid):
    for y, line in enumerate(grid):
        print(f"{y:03} " + "".join(line))
        pass


O_COUNTER = 0


def determine_move(guard_direction, x, y, original_grid):
    if guard_direction == "^":
        new_xy = move_up(x, y)
        new_guard_direction = guard_direction
        if original_grid[new_xy[1]][new_xy[0]] == "#":
            new_xy = (x, y)
            new_guard_direction = ">"
        return new_xy, new_guard_direction
    elif guard_direction == ">":
        new_xy = move_right(x, y)
        new_guard_direction = guard_direction
        if original_grid[new_xy[1]][new_xy[0]] == "#":
            new_xy = (x, y)
            new_guard_direction = "v"
        return new_xy, new_guard_direction
    elif guard_direction == "v":
        new_xy = move_down(x, y)
        new_guard_direction = guard_direction
        if original_grid[new_xy[1]][new_xy[0]] == "#":
            new_xy = (x, y)
            new_guard_direction = "<"
        return new_xy, new_guard_direction
    elif guard_direction == "<":
        new_xy = move_left(x, y)
        new_guard_direction = guard_direction
        if original_grid[new_xy[1]][new_xy[0]] == "#":
            new_xy = (x, y)
            new_guard_direction = "^"
        return new_xy, new_guard_direction
    return (x, y), guard_direction


def look_for_loophole_right(original_grid, x, y):
    check_x, check_y = int(x), int(y)
    o_locations = []

    while True:
        try:
            check_x, check_y = move_right(check_x, check_y)

            if original_grid[check_y][check_x] == "#":
                break
            if original_grid[check_y][check_x] == ">":
                print("I found a loophole")
                original_grid[y - 1].pop(x)
                original_grid[y - 1].insert(x, "O")
                o_locations.append((x, y - 1))
                print_grid(original_grid)
                # raise RecursionError("HERE")
                break
            if (
                original_grid[check_y][check_x] == "v"
                and original_grid[check_y][check_x + 1] == "#"
            ):
                print("I found a loophole")
                original_grid[y - 1].pop(x)
                original_grid[y - 1].insert(x, "O")
                o_locations.append((x, y - 1))
                print_grid(original_grid)
                print(check_x, check_y)
                # raise RecursionError("HERE")
                break
        except IndexError:
            # print("No loop hole!")
            break
    return o_locations


def look_for_loophole_down(original_grid, x, y):
    check_x, check_y = int(x), int(y)
    o_locations = []
    while True:
        try:
            check_x, check_y = move_down(check_x, check_y)
            if original_grid[check_y][check_x] == "#":
                break
            if original_grid[check_y][check_x] == "v":
                print("I found a loophole")
                original_grid[y].pop(x + 1)
                original_grid[y].insert(x + 1, "O")
                o_locations.append((x + 1, y))
                print_grid(original_grid)
                # raise RecursionError("HERE")
                break
            if (
                original_grid[check_y][check_x] == "<"
                and original_grid[check_y + 1][check_x] == "#"
            ):
                print("I found a loophole")
                original_grid[y].pop(x + 1)
                original_grid[y].insert(x + 1, "O")
                o_locations.append((x + 1, y))
                print_grid(original_grid)
                print(check_x, check_y)
                # raise RecursionError("HERE")
                break
        except IndexError:
            # print("No loop hole!")
            break
    return o_locations


def look_for_loophole_left(original_grid, x, y):
    check_x, check_y = int(x), int(y)

    o_locations = []
    while True:
        try:
            check_x, check_y = move_left(check_x, check_y)

            if original_grid[check_y][check_x] == "#":
                break
            if original_grid[check_y][check_x] == "<":
                print("I found a loophole")
                original_grid[y + 1].pop(x)
                original_grid[y + 1].insert(x, "O")
                o_locations.append((x, y + 1))
                print_grid(original_grid)
                # raise RecursionError("HERE")
                break
            if (
                original_grid[check_y][check_x] == "^"
                and original_grid[check_y][check_x - 1] == "#"
            ):
                print("I found a loophole")
                original_grid[y + 1].pop(x)
                original_grid[y + 1].insert(x, "O")
                o_locations.append((x, y + 1))
                print_grid(original_grid)
                # raise RecursionError("HERE")
                break
        except IndexError:
            # print("No loop hole!")
            break
    return o_locations


def look_for_loophole_up(original_grid, x, y):
    check_x, check_y = int(x), int(y)
    o_locations = []
    while True:
        try:
            check_x, check_y = move_up(check_x, check_y)

            if original_grid[check_y][check_x] == "#":
                break
            if original_grid[check_y][check_x] == "^":
                print("I found a loophole")
                original_grid[y].pop(x - 1)
                original_grid[y].insert(x - 1, "O")
                o_locations.append((x - 1, y))
                print_grid(original_grid)
                # raise RecursionError("HERE")
                break
            if (
                original_grid[check_y][check_x] == ">"
                and original_grid[check_y - 1][check_x] == "#"
            ):
                print("I found a loophole")
                original_grid[y].pop(x - 1)
                original_grid[y].insert(x - 1, "O")
                o_locations.append((x - 1, y))
                print_grid(original_grid)
                print((check_x, check_y))
                # raise RecursionError("HERE")
                break
        except IndexError:
            # print("No loop hole!")
            break
    return o_locations


def determine_move_with_check(guard_direction, x, y, original_grid):
    o = []
    if guard_direction == "^":
        # check if to the right, or two to the right is already ">"
        # if thats the case, we can place an "extra O" o there and we will spiral
        # into a loop.
        new_xy = move_up(x, y)
        new_guard_direction = guard_direction
        o.append(look_for_loophole_right(original_grid, x, y))

        if original_grid[new_xy[1]][new_xy[0]] == "#":
            new_xy = (x, y)
            new_guard_direction = ">"
        return new_xy, new_guard_direction, o
    elif guard_direction == ">":
        new_xy = move_right(x, y)
        o.append(look_for_loophole_down(original_grid, x, y))
        new_guard_direction = guard_direction
        if original_grid[new_xy[1]][new_xy[0]] == "#":
            new_xy = (x, y)
            new_guard_direction = "v"
        return new_xy, new_guard_direction, o
    elif guard_direction == "v":
        new_xy = move_down(x, y)
        o.append(look_for_loophole_left(original_grid, x, y))
        new_guard_direction = guard_direction
        if original_grid[new_xy[1]][new_xy[0]] == "#":
            new_xy = (x, y)
            new_guard_direction = "<"
        return new_xy, new_guard_direction, o
    elif guard_direction == "<":
        new_xy = move_left(x, y)
        o.append(look_for_loophole_up(original_grid, x, y))
        new_guard_direction = guard_direction
        if original_grid[new_xy[1]][new_xy[0]] == "#":
            new_xy = (x, y)
            new_guard_direction = "^"
        return new_xy, new_guard_direction, o
    return (x, y), guard_direction, o


def move_in_grid(current_grid: list[list[str]]):
    guard_position, guard_direction = find_guard(current_grid)
    o = []
    try:
        while True:
            print(chr(27) + "[2J")
            new_guard_position, new_guard_direction, o_inc = determine_move_with_check(
                guard_direction, guard_position[0], guard_position[1], current_grid
            )
            o.append(o_inc)
            current_grid[new_guard_position[1]].pop(new_guard_position[0])
            current_grid[new_guard_position[1]].insert(
                new_guard_position[0], new_guard_direction
            )
            if guard_direction != new_guard_direction:
                print_grid(current_grid)

                time.sleep(0.1)
            guard_direction = new_guard_direction
            guard_position = new_guard_position
    except IndexError:
        positition_counter = 0
        for line in current_grid:
            for char in line:
                if char in {"v", "^", "<", ">"}:
                    positition_counter += 1
        print(positition_counter)
        o = [loc[0][0] for loc in o if loc != [[]]]

        print(f"{o=}")
        print(f"{len(set(o))=}")


move_in_grid(lines)
