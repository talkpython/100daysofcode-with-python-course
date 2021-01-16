#!python3

from datetime import datetime
from datetime import date
from sys import intern

datetime.today()
#datetime.datetime(2018, 2, 19, 14, 38, 52, 133483)

today = datetime.today()


type(today)
#<class 'datetime.datetime'>


todaydate = date.today()

todaydate
#datetime.date(2018, 2, 19)

type(todaydate)
#<class 'datetime.date'>

todaydate.month
#2

todaydate.year
#2018

todaydate.day
#19


christmas = date(date.today().year, 12, 25)

# This function allows you to compare their memory addresses rather than comparing the strings character-by-character:
a = intern(str(todaydate))
b = intern(str(christmas))

if a is not b:
    print("Sorry there are still " + str((christmas - todaydate).days) + " until Christmas!")
else:
    print("Yay it's Christmas!")
