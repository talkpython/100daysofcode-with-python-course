import itertools
import sys
import time


def spinner(seconds):
    """Show an animated spinner while we sleep."""
    symbols = itertools.cycle('-\|/')
    tend = time.time() + seconds
    while time.time() < tend:
        # '\r' is carriage return: return cursor to the start of the line.
        sys.stdout.write('\rPlease wait... ' + next(symbols))  # no newline
        sys.stdout.flush()
        time.sleep(0.1)
    print()


if __name__ == "__main__":
    spinner(3)
