def read_lines(path: str = "./input_day_x.txt") -> str:
    with open(path) as f:
        line = f.read()

        assert len(line) > 0

    return line.rstrip()


def main():
    diskmap = read_lines(file_name)
    file_id = 0
    file_blocksize = 0
    free_space_size = 0
    disk = []
    map_pointer = 0
    is_file = True

    # expand the diskmap to a real disk
    for _ in diskmap:
        if is_file:
            file_blocksize = diskmap[map_pointer]
            disk.extend([file_id for _ in range(int(file_blocksize))])
            file_id += 1
        else:
            free_space_size = diskmap[map_pointer]
            disk.extend(["." for _ in range(int(free_space_size))])
        # alternating is file for each element in the map for file or free space
        is_file = not is_file
        map_pointer += 1
    # create pointers that keep track of where we are
    rear_pointer = len(disk) - 1
    front_pointer = 0
    while True:
        # look for the first free space
        while disk[front_pointer] != ".":
            front_pointer += 1
        # look for the first block to move
        while disk[rear_pointer] == ".":
            rear_pointer -= 1
        # if we're looking for space beyond the rear pointer
        # we are technically trying to move it backwards.
        # we don't want that.
        if front_pointer > rear_pointer:
            break
        # printing only if it fits on the screen
        if file_name != "./input_day_x.txt":
            print("".join(str(c) if c else "." for c in disk))
            pass
        # now move the rear piece to the first free piece
        rear_block = disk[rear_pointer]
        disk[front_pointer] = rear_block
        disk[rear_pointer] = "."

    if file_name != "./input_day_x.txt":
        print("".join(str(c) if c else "." for c in disk))
        pass
    check_sum = sum([index * int(mem) for index, mem in enumerate(disk) if mem != "."])
    print(check_sum)
    return check_sum


file_name = "./input_day_x_example.txt"
file_name = "./input_day_x_example_2.txt"
file_name = "./input_day_x_example_3.txt"
file_name = "./input_day_x.txt"

check_sum = main()
print("done")
