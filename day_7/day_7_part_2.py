from itertools import product


def read_lines(path: str = "./input_day_x.txt"):
    with open(path) as f:
        lines = []
        lines = f.readlines()

        assert len(lines) > 0

    return [line.split(" ") for line in lines]


def main():
    # Read input lines
    lines = read_lines("./input_day_x_example.txt")
    lines = read_lines("./input_day_x.txt")
    # Seperate expected answers from the numbers to make the answer with
    answers = [int(line[0].replace(":", "")) for line in lines]
    # Little hacky, but we need the numbers later to be strings, so they can be
    # concatenated efficiently.
    equation = [[n.replace("\n", "") for n in line if ":" not in n] for line in lines]
    # Allowed for operators
    # replaced the || operator by "" as we will abuse `eval` here
    operators = ["*", "+", ""]
    # list to store results in
    correct_results = set()
    # loop over each row, a combination of numbers and answers
    for numbers, answer in zip(equation, answers):
        # first find all combinations of operators
        operator_options = product(operators, repeat=len(numbers) - 1)
        # now loop through combination
        # it's actually a product, because we allow for duplicates
        for operator_option in operator_options:
            # as operators are in between numbers, and we have thus always one
            # more number then operators. We take the first number, before we
            # make pairs of numers and operators
            to_be_eval = numbers[0]
            # loop through numbers and operators that we "added" to the first element
            for number, operator_option in zip(numbers[1:], operator_option):
                # Now we combine our current result `to_be_eval`, which is a string
                # with the operator and the new number, also both strings.
                # We get a string in the from
                # `"result_of_previous_iteration " + "+" + "new_number"`
                # We put that string in the most evil of Python's built-in functions
                to_be_eval = eval(to_be_eval + operator_option + number)
                # We do this for the whole row of numbers, but maybe we are exploding
                # beyond the answer, so it makes sense to break out of the for loop
                # when we notice we're already too large.
                if to_be_eval > answer:
                    break
                # before we do the same thing again, we need to convert
                # the result back to string, as you put strings into eval.
                to_be_eval = str(to_be_eval)
            # We made it outside of the for loop. If we got out before the
            # string conversion...
            if isinstance(to_be_eval, int):
                # ... then we know that we came from the `break`, thus:
                # `to_be_eval > answer`
                # and we're not interested in the result and can go on to the
                # next "combintion" of operations
                continue
            # we made it out of the for-loop without break-ing out. Is it an answer?
            elif eval(str(to_be_eval)) == answer:
                # if we did, we add it to the results
                correct_results.add(eval(str(to_be_eval)))
                # Even better, we can stop looking for more ways of finding
                # the answers and can break out of this for-loop of
                # operator_options. This saves aa lot of computation time
                # as we only want to sum the answer once.
                break
    return sum(set(correct_results))


result = main()

assert result == 11387 or result == 223472064194845
print("done")
