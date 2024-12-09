"""For comments and explainers see part 2."""

from itertools import product


def read_lines(path: str = "./input_day_x.txt"):
    with open(path) as f:
        lines = []
        lines = f.readlines()

        assert len(lines) > 0

    return [line.split(" ") for line in lines]


lines = read_lines("./input_day_x.txt")
# lines = read_lines("./input_day_x_example.txt")

results = [[int(n.replace(":", "")) for n in line if ":" in n] for line in lines]
elements = [[n.replace("\n", "") for n in line if ":" not in n] for line in lines]

operators = ["*", "+"]

correct_results = []
for nums, ans in zip(elements, results):
    operator_options = product(operators, repeat=len(nums) - 1)
    for operator_option in operator_options:
        to_be_eval = nums[0]
        for num, operator_option in zip(nums[1:], operator_option):
            to_be_eval = to_be_eval + operator_option + num
            to_be_eval = str(eval(to_be_eval))
        res = eval(to_be_eval)
        if res == ans[0]:
            print(f"{to_be_eval} = {res} must be {ans[0]}")
            correct_results.append(res)
print(f"{sum(set(correct_results))=}")
print("done")
