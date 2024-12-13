"""
This was my first try.
But I was making it slow, ugly and it warranted a from scratch retry.
Please see `day_9_part_1_try2.py`!
"""


def get_disk_blocks(lines) -> list[list[str]]:
    evens = [line for idx, line in enumerate(lines) if idx % 2 == 0]
    odds = [line for idx, line in enumerate(lines) if idx % 2 == 1]
    disk_space_blocks = []
    if len(odds) == len(evens) + 1:
        evens.append("")
    if len(odds) + 1 == len(evens):
        odds.append("")
    for idx, (even, odd) in enumerate(zip(evens, odds, strict=True)):
        # print(idx, even, odd)
        disk_space_blocks.append([str(idx) for _ in range(int(even))])
        disk_space_blocks.append(["." for _ in range(int(odd))] if odd != "" else [])

    return disk_space_blocks


def read_lines(path: str = "./input_day_x.txt"):
    with open(path) as f:
        lines = []
        lines = f.readlines()

        assert len(lines) > 0

    return [[c for c in line if c != "\n"] for line in lines][0]


def find_last_non_dot(
    disk_space_blocks: list[list[str]], start: int = 0
) -> tuple[int, int, str | int]:
    nums_and_dots_len = len(disk_space_blocks)
    for idx in range(nums_and_dots_len - 1 if start == 0 else start, 0, -1):
        for inner_idx, element in enumerate(disk_space_blocks[idx]):
            if element != ".":
                return idx, inner_idx, element

    raise ValueError("")


def find_first_dot(
    disk_space_blocks: list[list[str]], start: int = 0
) -> tuple[int, int, str | int]:
    nums_and_dots_len = len(disk_space_blocks)
    for idx in range(start - 1 if start > 0 else 0, nums_and_dots_len - 1):
        if "." not in set(disk_space_blocks[idx]):
            continue
        inner_idx = disk_space_blocks[idx].index(".")
        # for inner_idx, element in enumerate(disk_space_blocks[idx]):
        #     if element == ".":
        return idx, inner_idx, "."
    raise ValueError("")


def printd(disk_space_blocks: list[list[str]]) -> None:
    if file_name != "./input_day_x.txt":
        print("".join("".join(b) for b in disk_space_blocks))


file_name = "./input_day_x_example.txt"
file_name = "./input_day_x_example_2.txt"
# file_name = "./input_day_x.txt"
lines = read_lines(file_name)
disk_space_blocks = get_disk_blocks(lines)


disk_space_blocks = [[c] for c in "".join("".join(b) for b in disk_space_blocks)]


def main(disk_space_blocks):
    printd(disk_space_blocks)
    non_dot_idx, non_dot_inner_idx, non_dot = find_last_non_dot(disk_space_blocks)
    idx, inner_idx, dot = find_first_dot(disk_space_blocks)
    disk_space_blocks[non_dot_idx][non_dot_inner_idx] = dot
    disk_space_blocks[idx][inner_idx] = non_dot
    printd(disk_space_blocks)

    while True:
        non_dot_idx, non_dot_inner_idx, non_dot = find_last_non_dot(
            disk_space_blocks  # , non_dot_idx
        )
        idx, inner_idx, dot = find_first_dot(disk_space_blocks, idx)
        if idx > non_dot_idx:
            print(idx, non_dot_idx)
            break
        disk_space_blocks[non_dot_idx][non_dot_inner_idx] = dot
        disk_space_blocks[idx][inner_idx] = non_dot
        printd(disk_space_blocks)
    calc_check_sum = 0
    for idx, num in enumerate("".join("".join(b) for b in disk_space_blocks)):
        if num != ".":
            calc_check_sum += int(num) * idx
    print(calc_check_sum)
    assert calc_check_sum != 90375502912


main(disk_space_blocks)
print("done")
