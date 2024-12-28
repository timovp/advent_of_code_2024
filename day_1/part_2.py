import re

# from line_profiler import profile
# from memory_profiler import profile as mem_profile


def read_input_files(file_name: str) -> tuple[list[int], list[int]]:
    with open(file_name) as f:
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

    return left_side, right_side


def count_nums_in_list_functional(num: int, list_of_nums: list[int]):
    """Counts numbers of appearances in the list."""
    return list_of_nums.count(num)


def count_nums_in_list(num: int, list_of_nums: list[int]):
    """Counts numbers of appearances in the list."""
    only_nums = [nice_num for nice_num in list_of_nums if nice_num == num]
    return len(only_nums)


def calc_similarity_score_faster(num: int, list_of_nums: list[int]):
    """Calculates the similarity score as number of appearances * num."""

    return num * list_of_nums.count(num)


def calc_similarity_score(num: int, list_of_nums: list[int]):
    """Calculates the similarity score as number of appearances * num."""
    count_of_nums = count_nums_in_list(num, list_of_nums)
    return num * count_of_nums


# @profile
def overall_similarity_score_list_comp():
    left_side, right_side = read_input_files("input_part1.txt")
    sim_scores = [calc_similarity_score_faster(left, right_side) for left in left_side]
    total_sim_scores = sum(sim_scores)
    return total_sim_scores


# @profile
def overall_similarity_score():
    left_side, right_side = read_input_files("input_part1.txt")
    total_similarity_score = 0
    for left in left_side:
        total_similarity_score += calc_similarity_score(left, right_side)
    return total_similarity_score


total_similarity_score = "pizza"
total_similarity_score = overall_similarity_score()
assert total_similarity_score == 26593248
total_similarity_score = overall_similarity_score_list_comp()
assert total_similarity_score == 26593248
print(total_similarity_score)


if __name__ == "__main__":
    pass
