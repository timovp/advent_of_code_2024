import re


def read_lines(path: str = "./input_day_3.txt"):
    with open(path) as f:
        lines = []
        lines = f.readlines()

        assert len(lines) > 0

    return [line for line in lines]


lines = read_lines("./input_day_3_example.txt")
# I removed newlines by hand from the input.
lines = read_lines()
big_line = "".join(lines)
# check if bigline now really is just one line with no hidden
# new line seperators:
assert len(big_line.splitlines()) == 1
sum_mul = 0
# add newline characters for each do and dont section (and a beginning section)
seperate_do_dont = big_line.replace("do()", "\ndo()").replace("don't()", "\ndon't()")
# now create a list of lines for each new line
# and filter out those that start with don't
do_lines = [
    dox_line
    for dox_line in seperate_do_dont.splitlines()
    if not dox_line.startswith("don't()")
]
# go through accepted lines and do the same as `day_1_part_1.py`
for do_line in do_lines:
    muls = re.findall(r"mul\(\d+\,\d+\)", do_line)
    for mul in muls:
        digits = mul.replace(")", "").split("(")[1].split(",")
        multiple = int(digits[0]) * int(digits[1])
        sum_mul = sum_mul + multiple

print(sum_mul)
assert sum_mul == 89349241
print("done")
