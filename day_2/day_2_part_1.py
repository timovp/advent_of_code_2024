import os
import re
from line_profiler import profile


@profile
def read_lines(path: str = "./input_day_2.txt"):
    with open(path) as f:
        lines = []
        lines = f.readlines()

        assert len(lines) > 0

    return [re.findall(r"\S+", line) for line in lines]


lines = read_lines()
diff_lines = []
for line in lines:
    diff_line = []
    print(line)
    prev = int(line[0])
    for num in line[1:]:
        num_as_int = int(num)
        diff = prev - num_as_int
        diff_line.append(diff)
        prev = num_as_int
    diff_lines.append(diff_line)
potential_safe = []
for diff_line in diff_lines:
    if all(el < 0 for el in diff_line) or all(el > 0 for el in diff_line):
        potential_safe.append(diff_line)

print(potential_safe)
real_safe = []
for pot in potential_safe:
    if all(el <= 3 and el >= -3 for el in pot):
        real_safe.append(pot)

print(real_safe)
print(len(real_safe))
print("done")
