# Days 31-33 Logging

Logging allows you to know what has happened to your program. Imagine this situation. You have a web application or redistributable app. A user calls you up and says, "Every time I try to run this operation, the app just crashes!" (500 errors on the server, or it just vanishes on the desktop).

Now what? You ask for the steps and inputs. Following along closely, you do exactly what they did with exactly the same version. And it works perfectly -- no crash.

You're in a tough spot! These are very hard to diagnose. If you have a record, a log file, with enough info you can just read what happened. 

Your goal during these three days is to add logging to one of your apps you've already built.

## Day N: Pick your application

Today is mostly watching the corresponding videos from the course. Be sure to watch the videos first. 

Then look through the apps we've already built or other applications you may have created that could use some proper logging. 

Once you picked your app, you'll be ready to improve it over the next two days. 

## Day N+1: Adding logging to your app

Your goal today will be to consider all information flowing through and actions of your application. What might go wrong? What would you want a history of? What info needs to be saved at each step?

You'll add logging to record this the next day.

## Day N+2: Add logging to the applications

Now it's time to add logging. Remember, you'll need to install [Logbook](https://logbook.readthedocs.io/en/stable/).

In your fresh Python3 virtual environment:

`pip install logbook`

Then you have to register the logging. Recall, this looks something like:

```python
import logbook
level = logbook.TRACE
log_filename = ...

if not log_filename:
    logbook.StreamHandler(sys.stdout, level=level).push_application()
else:
    logbook.TimedRotatingFileHandler(log_filename, level=level).push_application()
   
```

Then to log something, you create a logbook instance like this:

```python
app_log = logbook.Logger('App')
# ...
app_log.notice("some message")

# actions are:
# notice / info / trace / warn / error / critical
```

Once you've got your app logging (either to the console or a file) and saving what you think is important, you're done!

### Time to share what you've accomplished!

Be sure to share your last couple of days work on Twitter or Facebook. Use the hashtag **#100DaysOfCode**. 

Here are [some examples](https://twitter.com/search?q=%23100DaysOfCode) to inspire you. Consider including [@talkpython](https://twitter.com/talkpython) and [@pybites](https://twitter.com/pybites) in your tweets.

*See a mistake in these instructions? Please [submit a new issue](https://github.com/talkpython/100daysofcode-with-python-course/issues) or fix it and [submit a PR](https://github.com/talkpython/100daysofcode-with-python-course/pulls).*
