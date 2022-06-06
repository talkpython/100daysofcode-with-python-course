from datetime import datetime
from datetime import timedelta

import beepy as beep

import time
import argparse

# Instantiate the parser
parser = argparse.ArgumentParser(description='input the timer value in minutes')
parser.add_argument('-t', '--timer', type=int, dest='timer', action="store", help='input the timer value in minutes')
args = parser.parse_args()

timer_delta = timedelta(seconds=args.timer * 60)

actual_time = datetime.now()

five_minutes_window = timedelta(seconds=300)
print(actual_time.strftime('Today is  %d, %b %Y. Time: %H:%M:%S'))
print("The selected focus time period is: {} minutes".format(args.timer))

print("Press ENTER once you are ready to focus.\nType Q and press ENTER to stop.")
value = input()
while value.lower() != "q":
    print("Focusing...")
    while(timer_delta.seconds > 0):
        time.sleep(five_minutes_window.seconds)
        timer_delta = timedelta(seconds=timer_delta.seconds - five_minutes_window.seconds)
        print("Remaining focus time: {} minutes".format(timer_delta.seconds / 60))
    print("Focus time is over, now it's time to relax!")
    beep.beep(7)
    beep.beep(2)
    timer_delta = timedelta(seconds=args.timer * 60)

    print("Press ENTER once you are ready to focus.\nType Q and press ENTER to stop.")
    value = input()



