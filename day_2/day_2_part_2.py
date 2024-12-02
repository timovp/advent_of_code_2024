def read_lines(path: str = "./input_day_2.txt"):
    with open(path) as f:
        lines = []
        lines = f.readlines()
        assert len(lines) > 0

    return [line.split(" ") for line in lines]


def make_diff_line(line: list[str]) -> list[int]:
    diff_line = []
    line_int = [int(el) for el in line]
    prev = line_int[0]
    for num in line_int[1:]:
        diff = num - prev
        diff_line.append(diff)
        prev = num
    return diff_line


def make_diff_lines(lines: list[list[str]]) -> list[list[int]]:
    return [make_diff_line(line) for line in lines]


def check_logic(diff_line: list[int]):
    if any(el > 3 or el < -3 for el in diff_line):
        return False
    if all(el < 0 for el in diff_line) or all(el > 0 for el in diff_line):
        return True
    return False


def check_popped(orig_line: list[str]):
    for idx, element in enumerate(orig_line):
        orig_line.pop(idx)
        popped_diffs = make_diff_line(orig_line)
        orig_line.insert(idx, element)
        if check_logic(popped_diffs):
            return True

    return False


def find_safe_reports(
    diff_lines: list[list[int]], orig_lines: list[list[str]]
) -> tuple[list[int], list[int]]:
    safe_with_dampener = []
    real_safe = []
    for row_num, diff_line in enumerate(diff_lines):
        if check_logic(diff_line):
            real_safe.append([orig_lines[row_num], diff_line])
        elif check_popped(orig_lines[row_num]):
            safe_with_dampener.append([orig_lines[row_num], diff_line])

    return real_safe, safe_with_dampener


def main():
    lines = read_lines()
    diff_lines = [make_diff_line(line) for line in lines]
    real_safe, with_dampener = find_safe_reports(diff_lines, lines)

    assert len(real_safe) == 314
    # assert len(with_dampener) == 59
    assert len(real_safe) + len(with_dampener) == 373
    test_lines = read_lines("./exmaple_day_2_part_2.txt")
    test_diff_files = [make_diff_line(line) for line in test_lines]
    test_safe, test_damp = find_safe_reports(test_diff_files, test_lines)
    assert len(test_safe) == 2
    assert len(test_damp) == 2


for _ in range(100):
    main()
