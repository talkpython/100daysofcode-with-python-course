# ------------------------------------------------------------------------
# Helper file for 100 Days of Code
#
# My first 'libaray' code
#
# Brent Gawryluik
# 2018-07-09
# ------------------------------------------------------------------------


def print_header(title):

    border_length = len(title) + 12

    print()
    print_border(border_length)
    print_title(title)
    print_border(border_length)
    print()

def print_border(length):
    for _ in range(length):
        print('-', end='', flush=True)

    print()


def print_title(title):
    print('      ', end='', flush=True)
    print(title)
