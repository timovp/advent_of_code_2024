import re


def read_lines(path: str = "./input_day_x.txt"):
    with open(path) as f:
        lines = []
        lines = f.readlines()

        assert len(lines) > 0

    return [line for line in lines]


lines = read_lines()
sum_mul = 0
for line in lines:
    muls = re.findall(r"mul\(\d+\,\d+\)", line)
    for mul in muls:
        digits = mul.replace(")", "").split("(")[1].split(",")
        multiple = int(digits[0]) * int(digits[1])
        sum_mul = sum_mul + multiple
print(sum_mul)
print("done")
