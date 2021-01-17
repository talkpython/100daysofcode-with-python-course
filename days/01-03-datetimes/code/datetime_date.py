#!python3

from datetime import date
from datetime import datetime

datetime.today()
# datetime.datetime(2021, 1, 19, 14, 38, 52, 133483)

today = datetime.today()

type(today)
# <class 'datetime.datetime'>


today_date = date.today()

today_date
# datetime.date(2021, 1, 19)

type(today_date)
# <class 'datetime.date'>

today_date.month
# 1

today_date.year
# 2021

today_date.day
# 19


christmas = date(today_date.year, 12, 25)
christmas
# datetime.date(2021, 12, 25)

# We need to use != & == rather than is / is not for comparison. Sorry for the mistake in the video.
if christmas != today_date:
    print("Sorry there are still " + str((christmas - today_date).days) + " until Christmas!")
else:
    print("Yay it's Christmas!")
