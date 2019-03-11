'''Extract datetimes from log entries and calculate the time
   between the first and last shutdown events'''
from datetime import datetime
import os
import urllib.request

SHUTDOWN_EVENT = 'Shutdown initiated'

# prep: read in the logfile
logfile = os.path.join('/tmp', 'log')
urllib.request.urlretrieve('http://bit.ly/2AKSIbf', logfile)

with open(logfile) as f:
    loglines = f.readlines()


# for you to code:

def convert_to_datetime(line):
    '''TODO 1:
       Given a log line extract its timestamp and convert it to a datetime object. 
       For example calling the function with:
       INFO 2014-07-03T23:27:51 supybot Shutdown complete.
       returns:
       datetime(2014, 7, 3, 23, 27, 51)'''
    
    timestamp = line.split()[1]  # type: str
    timestamp = datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S') # type: datetime
    return timestamp


def time_between_shutdowns(loglines):
    '''TODO 2:
       Extract shutdown events ("Shutdown initiated") from loglines and calculate the 
       timedelta between the first and last one. 
       Return this datetime.timedelta object.'''
    timestamps = []
    for line in loglines:
        if SHUTDOWN_EVENT in line:
            timestamps.append(line)
    first = convert_to_datetime(timestamps[0])
    last = convert_to_datetime(timestamps[len(timestamps) - 1])
    return last - first
