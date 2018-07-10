# ------------------------------------------------------------------------
# 100 Days of Code
# Day 1-3
#
# Pomadaro Timer
#  - Playing with Datetimes...
#
# Brent Gawryluik
# 2018-07-09
# ------------------------------------------------------------------------

import helpers


def main():
    helpers.print_header('Pomadaro Timer')
    work_duration = get_duration_input("WORK")
    rest_duration = get_duration_input("REST")


def get_duration_input(activity):
    return input("Please enter for how many minutes you would like to {}: ".format(activity))


if __name__ == '__main__':
    main()
