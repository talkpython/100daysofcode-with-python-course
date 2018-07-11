# ------------------------------------------------------------------------
# 100 Days of Code
# Day 1-3
#
# Pomadaro Timer
#  - Playing with Datetimes...
#  - or time, anyway...
#
# Brent Gawryluik
# 2018-07-09
# ------------------------------------------------------------------------

import helpers
import progressbar
import time


def main():
    helpers.print_header('Pomadaro Timer')
    work_duration = get_duration_input("WORK")
    rest_duration = get_duration_input("REST")
    display_timer(work_duration, 'WORK')
    display_timer(rest_duration, 'REST')
    print()
    print('Exiting the Pomadaro timer process.')


def get_duration_input(activity):
    return int(input("Please enter a number for how many minutes you would like to {}: ".format(activity)))


def display_timer(duration, activity):

    print()
    print("Starting new {} task".format(activity))

    if duration == 1:
        print("Now displaying {} timer for {} minute...".format(activity, duration))
    elif duration > 1:
        print("Now displaying {} timer for {} minutes...".format(activity, duration))

    print ()

    bar = progressbar.ProgressBar(widgets=[
        progressbar.Bar(),
    ])

    for i in bar(range(duration *60)):
        time.sleep(1)

    print()
    print("{} task is done".format(activity))

if __name__ == '__main__':
    main()
