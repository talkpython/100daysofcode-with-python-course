import itertools
import sys
import time

symbols = itertools.cycle('-\|/')

while True:
    sys.stdout.write('\r' + next(symbols))
    sys.stdout.flush()
    time.sleep(0.1)
