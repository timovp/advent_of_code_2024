import re
import sys
import termios
import tty
from time import sleep


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


class Cursor:
    @staticmethod
    def up(n: int = 1, flush: bool = False):
        """Move cursor up n lines and flush output if needed."""
        print(f"\033[{n}A", end="", flush=flush)

    @staticmethod
    def down(n: int = 1, flush: bool = False):
        """Move cursor down n lines and flush output if needed."""
        print(f"\033[{n}B", end="", flush=flush)

    @staticmethod
    def right(n: int = 1, flush: bool = False):
        """Move cursor right n columns and flush output if needed."""
        print(f"\033[{n}C", end="", flush=flush)

    @staticmethod
    def left(n: int = 1, flush: bool = False):
        """Move cursor left n columns and flush output if needed."""
        print(f"\033[{n}D", end="", flush=flush)

    @staticmethod
    def next_line(n: int = 1, flush: bool = False):
        """Move cursor down n lines to beginning of the line."""
        print(f"\033[{n}E", end="", flush=flush)

    @staticmethod
    def prev_line(n: int = 1, flush: bool = False):
        """Move cursor up n lines to beginning of the line."""
        print(f"\033[{n}F", end="", flush=flush)

    @staticmethod
    def column(n: int = 1, flush: bool = False):
        """Move cursor to column n (1-based index)."""
        print(f"\033[{n}G", end="", flush=flush)

    @staticmethod
    def position(row: int = 1, col: int = 1, flush: bool = False):
        """Move cursor to a specific (row, col) position (1-based)."""
        print(f"\033[{row};{col}H", end="", flush=flush)

    @staticmethod
    def save_position(flush: bool = False):
        """Save current cursor position."""
        print("\033[s", end="", flush=flush)

    @staticmethod
    def restore_position(flush: bool = False):
        """Restore cursor to the last saved position."""
        print("\033[u", end="", flush=flush)

    @staticmethod
    def clear_line(mode: int = 2, flush: bool = False):
        """
        Clear part of the line.
          mode=0 : clear from cursor to end of line
          mode=1 : clear from start of line to cursor
          mode=2 : clear entire line
        """
        print(f"\033[{mode}K", end="", flush=flush)

    @staticmethod
    def clear_screen(mode: int = 2, flush: bool = False):
        """
        Clear part of the screen.
          mode=0 : clear from cursor to end of screen
          mode=1 : clear from start of screen to cursor
          mode=2 : clear entire screen
        """
        print(f"\033[{mode}J", end="", flush=flush)


def read_lines(path: str = "./input_day_x.txt") -> list[list[str]]:
    with open(path) as f:
        lines = []
        lines = f.readlines()

        assert len(lines) > 0

    return [[str(c) for c in line.rstrip("\n")] for line in lines]


def clc(sleeptime=0.01):
    sleep(sleeptime)
    print(chr(27) + "[2J")  # clears the terminal


def print_empty_lines(n=10):
    for _ in range(n):
        print()


def get_cursor_position():
    """
    Returns (row, col) as integers, representing the cursor's position in the terminal.
    """
    # Save original terminal settings
    fd = sys.stdin.fileno()
    original_settings = termios.tcgetattr(fd)
    try:
        # Switch to raw mode
        tty.setraw(fd)

        # Request cursor position
        sys.stdout.write("\033[6n")
        sys.stdout.flush()

        # Read the response: ESC [ row ; col R
        # We read byte-by-byte until we get the final 'R'
        response = ""
        while True:
            ch = sys.stdin.read(1)
            if not ch:
                break  # Just in case we get no data
            response += ch
            if ch == "R":
                break

        # The response should look like "\x1b[24;10R"
        # Use a regex to parse out the row and column
        match = re.search(r"\x1b\[(\d+);(\d+)R", response)
        if match:
            row = int(match.group(1))
            col = int(match.group(2))
            return row, col
        else:
            raise ValueError("should not happen?")

    finally:
        # Restore original terminal settings
        termios.tcsetattr(fd, termios.TCSADRAIN, original_settings)


if __name__ == "__main__":
    print("Move the cursor somewhere and press Enter...")
    input()
    row, col = get_cursor_position()
    print(f"Your cursor is at row={row}, col={col}")
