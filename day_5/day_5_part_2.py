def determine_correct_ordering(
    applicable_ordering, page, page_correct, page_num
) -> tuple[bool, list[tuple]]:
    violated_orderings = []
    for ordering in applicable_ordering:
        if page_num == ordering[0]:
            # print(f"{page_num=} has {ordering=}")
            # print(f"            must be before {ordering[1]}")
            if page.index(page_num) > page.index(ordering[1]):
                # print(f"{page}      not in the correct order")
                page_correct = False
                violated_orderings.append(ordering)
    return page_correct, violated_orderings


def read_lines(path: str = "./input_day_5.txt"):
    with open(path) as f:
        lines = []
        lines = f.readlines()

        assert len(lines) > 0

    return [line.replace("\n", "") for line in lines]


def get_orderings_pages(lines: list[str]) -> tuple[list[list[int]], list[list[int]]]:
    orderings = [[int(el) for el in line.split("|")] for line in lines if "|" in line]
    pages = [[int(el) for el in line.split(",")] for line in lines if "," in line]

    return orderings, pages


lines = read_lines("./input_day_5.txt")


orderings, pages = get_orderings_pages(lines)


correct_pages = []
incorrect_pages = []
corrected_pages = []
for page in pages:
    # determine which of the orderings apply to the numbers on the "page"
    applicable_ordering = []
    for ordering in orderings:
        if set(ordering).issubset(set(page)):
            applicable_ordering.append(ordering)
    # if a page is correct, no changes are needed, and the determine fucntion
    # won't change it's value
    page_correct = True
    # we keep a sperate copy of the page, so we can make changes to it.
    # as lists are annoying and mutable.
    corrected_page = [p for p in page]
    for page_num in page:
        # checking the applicable orderings if any are violated for that page_num
        # we use corrected page, as we do alterations to it per page num,
        # and don't want override corrections.
        page_correct, violated_orderings = determine_correct_ordering(
            applicable_ordering, corrected_page, page_correct, page_num
        )
        # the page_correct applies to all numbers (needed for part1)
        # but the violated_orderings only applies to the current page_num
        while len(violated_orderings) != 0:
            # corrected_page is not correct for page_num and violated_orderings
            # so we move the page_num on place back in the corrected_page
            new_idx = corrected_page.index(page_num) - 1
            corrected_page.pop(corrected_page.index(page_num))
            corrected_page.insert(new_idx, page_num)
            # lets see if that solves it. if not we stay inside the while-loop.
            _, violated_orderings = determine_correct_ordering(
                applicable_ordering, corrected_page, page_correct, page_num
            )
        # once out of the while loop, we have a corrected_page, which does not create
        # any violations for page_num, and we can go on to the next page_num in this
        # for loop.

    # after completing all page_num's in the page, we see if none created violations:
    if page_correct:
        # if page was fully correct, epic, add it to the correct_pages list for part1 solution.
        correct_pages.append((pages.index(page), page))
    else:
        # if not, add the original version of the inccorect page to to the list
        # we keep these for comparison's sake.
        incorrect_pages.append((pages.index(page), page))
        # and add the adjusted page to a list, needed for the answer
        corrected_pages.append(corrected_page)

# to check if the spaghetti from above does not alter our original aswer to part 1
# we recalculate the result and assert
middle_sum_correct = 0
for correct_page in correct_pages:
    middle_index = int((len(correct_page[1]) - 1) / 2)
    middle_sum_correct += correct_page[1][middle_index]
# its a bit of a weak assertion, as we allow for both the example answer and my puzzle input.
# I think it's fair to assume i don't produce by accident the wrong-correct answer.
assert middle_sum_correct == 5713 or middle_sum_correct == 143


# now, just to be sure I didnt mess up, i'm checking if this full list of
# corrected pages, produces no new violations after all adjustments.
for corrected_page in corrected_pages:
    applicable_ordering = []
    for ordering in orderings:
        if set(ordering).issubset(set(corrected_page)):
            applicable_ordering.append(ordering)
    page_correct = True
    for page_num in corrected_page:
        page_correct, violated_orderings = determine_correct_ordering(
            applicable_ordering, corrected_page, page_correct, page_num
        )
        assert len(violated_orderings) == 0
# now do the part 2 recalculation.
middle_sum_corrected = 0
for corrected_page in corrected_pages:
    middle_index = int((len(corrected_page) - 1) / 2)
    middle_sum_corrected += corrected_page[middle_index]

assert middle_sum_corrected == 123 or middle_sum_corrected == 5180

print("done")
