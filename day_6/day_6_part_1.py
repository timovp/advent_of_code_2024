def read_lines(path: str = "./input_day_6.txt"):
    with open(path) as f:
        lines = []
        lines = f.readlines()

        assert len(lines) > 0

    return [[c for c in line.replace("\n", "")] for line in lines]


lines = read_lines("./input_day_6_example.txt")
for line in lines:
    print("".join(line))


def find_guard(lines):
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char in {"v", "^", "<", ">"}:
                starting_point = (x, y)
                return starting_point, char
    raise ValueError("oops")


def move_left(x, y):
    return x - 1, y


def move_right(x, y):
    return x + 1, y


def move_down(x, y):
    return x, y + 1


def move_up(x, y):
    return x, y - 1


def print_grid(grid):
    for line in grid:
        print("".join(line))


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


def move_in_grid(current_grid: list[list[str]]):
    guard_position, guard_direction = find_guard(current_grid)
    try:
        while True:
            new_guard_position, new_guard_direction = determine_move(
                guard_direction, guard_position[0], guard_position[1], current_grid
            )
            current_grid[new_guard_position[1]].pop(new_guard_position[0])
            current_grid[new_guard_position[1]].insert(
                new_guard_position[0], new_guard_direction
            )
            print(chr(27) + "[2J")
            print_grid(current_grid)
            import time

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


move_in_grid(lines)
print("done")
