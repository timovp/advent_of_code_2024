import re


def read_lines(path: str = "./input_day_x.txt"):
    with open(path) as f:
        lines = []
        lines = f.readlines()

        assert len(lines) > 0

    return [line for line in lines]


lines = read_lines("./input_day_x_example.txt")
lines = read_lines()
big_line = "".join(lines)
sum_mul = 0
seperate_do_dont = big_line.replace("do()", "\ndo()").replace("don't()", "\ndon't()")
do_lines = [
    dox_line
    for dox_line in seperate_do_dont.splitlines()
    if not dox_line.startswith("don't()")
]
for do_line in do_lines:
    muls = re.findall(r"mul\(\d+\,\d+\)", do_line)
    for mul in muls:
        digits = mul.replace(")", "").split("(")[1].split(",")
        multiple = int(digits[0]) * int(digits[1])
        sum_mul = sum_mul + multiple

print(sum_mul)
print("done")
