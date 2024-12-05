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
for page in pages:
    applicable_ordering = []
    for ordering in orderings:
        if set(ordering).issubset(set(page)):
            print(f"{ordering=} in {page=}")
            applicable_ordering.append(ordering)

    print(f"{page=} update:")
    page_correct = True
    for page_num in page:
        print(f"{page_num=}, checking applicable orderings")
        for ordering in applicable_ordering:
            if page_num == ordering[0]:
                print(f"{page_num=} has {ordering=}")
                print(f"            must be before {ordering[1]}")
                if page.index(page_num) > page.index(ordering[1]):
                    print(f"{page}      not in the correct order")
                    page_correct = False
    if page_correct:
        correct_pages.append((pages.index(page), page))

print(correct_pages)
middle_sum_correct = 0
for correct_page in correct_pages:
    middle_index = int((len(correct_page[1]) - 1) / 2)
    middle_sum_correct += correct_page[1][middle_index]

print(middle_sum_correct)
print("done")
