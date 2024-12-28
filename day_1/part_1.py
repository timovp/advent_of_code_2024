import re

with open("input_part1.txt") as f:
    lines = f.readlines()

assert len(lines) > 0

left_side = []
right_side = []

for line in lines:
    # find all regex elements that are non-whitespace
    splits = re.findall(r"\S+", line)
    # dont be fooled by a timmie where you removed a newline...
    assert len(splits) == 2
    # now add them to a list
    left_side.append(int(splits[0]))
    right_side.append(int(splits[1]))

# sanity check
assert len(left_side) == len(right_side)

# sort from small to large
left_side.sort()
right_side.sort()

# calc differences
diffs = [abs(left - right) for left, right in zip(left_side, right_side, strict=False)]

print(sum(diffs))
