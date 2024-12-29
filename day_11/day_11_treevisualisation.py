from collections import Counter
from functools import cache


def read_lines(path: str = "./input_day_x.txt") -> list[str]:
    with open(path) as f:
        lines = []
        lines = f.readlines()

        assert len(lines) > 0

    return [numb.replace("\n", "") for numb in lines[0].split(" ")]


@cache
def stone_calc(stone: str):
    len_stone = len(stone)
    if stone == "0":
        return ("1",)
    elif len_stone % 2 == 0:
        return (
            str(int(stone[0 : int(len_stone / 2)])),
            str(int(stone[int(len_stone / 2) :])),
        )
    else:
        return (str(int(stone) * 2024),)


def do_blinks(blinks: int):
    """In a blink of an eye..."""
    stones: list[str] = read_lines("./input_day_x_example.txt")
    stones: list[str] = read_lines("./input_day_x.txt")
    counter = Counter()
    for stone in stones:
        counter[stone] = 1
    for _ in range(blinks):
        new_counter = Counter()
        for stone, stone_count in counter.items():
            new_stones = stone_calc(stone)
            for new_stone in new_stones:
                new_counter.update({new_stone: stone_count})
        counter = new_counter
    return counter.total()


def do_blinks_visual(blinks: int):
    """In a blink of an eye..."""
    stones: list[str] = read_lines("./input_day_x_example.txt")
    # stones: list[str] = read_lines("./input_day_x.txt")
    counter = Counter()
    stone_set = set()
    for stone in stones:
        counter[stone] = 1
    for _ in range(blinks):
        new_counter = Counter()
        new_counter = new_counter + counter
        for stone, _ in counter.items():
            new_stones = stone_calc(stone)
            for new_stone in new_stones:
                if stone not in stone_set:
                    print(f"  {stone} -> {new_stone}")
                new_counter[new_stone] = 1
            stone_set.add(stone)
        counter = new_counter
    return counter.total()


BLINKS = 75
ans = do_blinks(BLINKS)
print("digraph d")
print("{")
ans = do_blinks_visual(BLINKS)
print("}")
# print(ans)
