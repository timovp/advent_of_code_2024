from part_2 import calc_similarity_score, count_nums_in_list, read_input_files


def test_count_nums_in_list():
    assert count_nums_in_list(3, [3, 3, 3, 3]) == 4


def test_calc_similarity_score_1():
    example_left, example_right = read_input_files("test_input.txt")

    assert calc_similarity_score(example_left[0], example_right) == 9
    assert calc_similarity_score(example_left[1], example_right) == 4
    assert calc_similarity_score(example_left[2], example_right) == 0
    assert calc_similarity_score(example_left[3], example_right) == 0
    assert calc_similarity_score(example_left[4], example_right) == 9
    assert calc_similarity_score(example_left[5], example_right) == 9


def test_calc_similarity_score_2():
    example_left, example_right = read_input_files("test_input.txt")
    total_similarity_score = 0
    for left in example_left:
        total_similarity_score += calc_similarity_score(left, example_right)

    assert total_similarity_score == 31


def test_read_input_files():
    """Just a sanity check."""
    example_left, example_right = read_input_files("test_input.txt")

    assert len(example_left) == len(example_right)
