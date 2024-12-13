import sys


class Color:
    # Reset
    RESET = "\033[0m"

    # Standard Colors
    BLACK = "\033[0;30m"
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    BROWN = "\033[0;33m"
    BLUE = "\033[0;34m"
    PURPLE = "\033[0;35m"
    CYAN = "\033[0;36m"
    LIGHT_GRAY = "\033[0;37m"

    # Bright Colors
    DARK_GRAY = "\033[1;30m"
    LIGHT_RED = "\033[1;31m"
    LIGHT_GREEN = "\033[1;32m"
    YELLOW = "\033[1;33m"
    LIGHT_BLUE = "\033[1;34m"
    LIGHT_PURPLE = "\033[1;35m"
    LIGHT_CYAN = "\033[1;36m"
    WHITE = "\033[1;37m"


def read_lines(path: str = "./input_day_x.txt") -> str:
    with open(path) as f:
        line = f.read()

        assert len(line) > 0

    return line.rstrip()


def _str(c: str, idx: int, fp: int, rp: int, rear_space: int):
    if fp <= idx and rear_space + fp > idx:
        return Color.LIGHT_GREEN + str(c) + Color.RESET
    if rp - rear_space < idx and rp >= idx:
        return Color.LIGHT_CYAN + str(c) + Color.RESET

    else:
        return str(c)


def disk_printer(disk, fp, rp, rear_space):
    if file_name != "./input_day_x.txt":
        print("".join([_str(c, idx, fp, rp, rear_space) for idx, c in enumerate(disk)]))


def main():
    # get the map to expand
    diskmap = read_lines(file_name)
    file_id = 0
    file_blocksize = 0
    free_space_size = 0
    disk = []
    map_pointer = 0
    is_file = True
    # do expansion
    for _ in diskmap:
        if is_file:
            file_blocksize = diskmap[map_pointer]
            disk.extend([file_id for _ in range(int(file_blocksize))])
            file_id += 1
        else:
            free_space_size = diskmap[map_pointer]
            disk.extend(["." for _ in range(int(free_space_size))])
        is_file = not is_file
        map_pointer += 1

    if file_name != "./input_day_x.txt":
        print("".join(str(c) if str(c).isdigit() else "." for c in disk))
    rear_pointer = len(disk) - 1
    front_pointer = 0
    rear_pointer_next = 0
    while True:
        # look for first point that is free space
        # `while disk[front_pointer] != ".":`
        # `    front_pointer += 1`
        # after profiling I realized that I spent most time here
        # and decided I could try `list.index()`. It made it way faster
        # I think it's because you start over from 0.
        # and appearantly it's faster than +=1 operations
        front_pointer = disk.index(".")
        front_pointer_next = front_pointer

        # then look for how big the free space is
        while disk[front_pointer_next] == disk[front_pointer]:
            # as long as the next point is still ".", there is more
            # free space availabe
            front_pointer_next += 1
        # front_space is the room between front_pointer_next and front_pointer
        front_space = front_pointer_next - front_pointer

        # now do the same for the rear, so look for the first place it's not "."
        while disk[rear_pointer] == ".":
            rear_pointer -= 1
        rear_pointer_next = rear_pointer

        # I assumed I could also apply my list.index learnings here
        # but this made it slower, which is actually super logical
        # Normally you have to travel utmost 10 steps from rear pointer
        # the next file_id or free_space.
        # list.index() gives the first occurance of the file_id, so it
        # probably starts from index 0 and has to very often travel further
        # than 10 indexes, so it becomes slower than -=1 operations
        while disk[rear_pointer_next] == disk[rear_pointer]:
            rear_pointer_next -= 1
        # rear_pointer_next = disk.index(disk[rear_pointer])
        rear_space = rear_pointer - rear_pointer_next

        # if we have more than enough space for the file_id at the back
        # and we're not moving the thing backwarts
        if front_space >= rear_space and front_pointer < rear_pointer:
            # now get that rear block
            rear_block = disk[rear_pointer_next + 1 : rear_pointer + 1]
            # this prints the current state of the disk, before the move
            # and visualizes what we want to move.
            # visually debugger >>>> debugger.
            disk_printer(disk, front_pointer, rear_pointer, rear_space)
            # place the rear_block at the most front place
            disk[front_pointer : (front_pointer + rear_space)] = rear_block
            # just place "." for every element you move.
            disk[rear_pointer_next + 1 : rear_pointer + 1] = "." * rear_space
            # critical step: move back the front pointer to start over looking
            # for leftover space
            front_pointer = 1
        else:
            # if there isnt enough space for the rear_block, increment front pointer
            # and look for the next location where there's space
            front_pointer += 1
            while disk[front_pointer] != ".":
                front_pointer += 1
        # if we passed the rear_pointer with the front pointer when looking for
        # free space, then we move front pointer back and we place rear pointer
        # at the end of the rear_block.
        if front_pointer >= rear_pointer:
            front_pointer = 1
            front_pointer_next = 1
            rear_pointer = rear_pointer_next
        if rear_pointer <= 0:
            # if rear_pointer is at the beginning, quit the while loop:
            # we moved all files.
            break
    # calculate the checksum
    check_sum = sum([index * int(mem) for index, mem in enumerate(disk) if mem != "."])
    print(check_sum)
    return check_sum


file_name = "./input_day_x_example.txt"
file_name = "./input_day_x_example_2.txt"
file_name = "./input_day_x_example_3.txt"
file_name = "./input_day_x.txt"
if len(sys.argv) > 1:
    file_name = sys.argv[1]
check_sum = main()
if file_name == "./input_day_x.txt":
    assert check_sum < 7326657141239
print("done")
