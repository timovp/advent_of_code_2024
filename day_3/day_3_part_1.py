import re


def read_lines(path: str = "./input_day_3.txt"):
    with open(path) as f:
        lines = []
        lines = f.readlines()

        assert len(lines) > 0

    return [line for line in lines]


lines = read_lines()
sum_mul = 0
for line in lines:
    # use our prized findall again to search for mul(123,456)
    # escaping the `,`, `(` and `)` and, more importantly
    # looking for any number of repeated digits in a line.
    muls = re.findall(r"mul\(\d+\,\d+\)", line)
    for mul in muls:
        # Now that I have a list of mul(123,456)'s time extract the digits
        # by splitting both "(" and "," leaving: "mul", "123" and "456)".
        # so I replace the ")" pre-emptively.
        # In hindsight using another `re.findall("\d+")` would have been more
        # straight forward.
        digits = mul.replace(")", "").split("(")[1].split(",")
        # now convert to string and get the multiplication.
        multiple = int(digits[0]) * int(digits[1])
        sum_mul = sum_mul + multiple

print(sum_mul)
assert sum_mul == 159833790
print("done")
