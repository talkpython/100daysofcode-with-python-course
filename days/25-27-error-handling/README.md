# Days 25-27 Error handling

One of the key differentiators of professional programs and scripts thrown together by beginners is that the pro app does not crash. It anticipates all the error conditions and puts the proper error handling and user feedback to keep working. 

Ok, pro apps still crash, but they do so much less often. When they do, we have [logging](https://logbook.readthedocs.io) and other error monitoring such as [Rollbar](https://rollbar.com/?dr) so that we can get notified and fix these once we encounter them. This allows apps to grow stronger and more resilient over time.

Your goal during these three days is to solidify one of your apps you've already built.

## Day N: Pick your application

Today is mostly watching the corresponding videos from the course. Be sure to watch the videos first. 

Then look through the apps we've already built or other applications you may have created that could use some proper error handling. 

One example that comes to mind is the text games apps we built. What happens when you enter invalid input?

Once you picked your app, you'll be ready to improve it over the next two days. 

## Day N+1: Adding error handling to the demo app

Your goal today will be to consider all the error cases in your application. What might go wrong? How will you test or discover these?

Once you have a list of potential problems, run the app in ways that will trigger those errors. Make a list of the exception types so that you'll be able to handle them individually in the app.

## Day N+2: Add error handling to one of your applications

Now that you know the error conditions in your applications, it's time to add error handling.

Recall, this looks something like:

```python
try:
    method1()
    method2()
    method3()
except ExceptionType1 as x:
    # details with x
except ExceptionType2 as x:
    # details with x
except Exception:
    # general error fallback.
finally:
    # code that runs regardless of error or success.
```

Add the error handling to your app and verify that it's catching and handling errors as expected.

### Time to share what you've accomplished!

Be sure to share your last couple of days work on Twitter or Facebook. Use the hashtag **#100DaysOfCode**. 

Here are [some examples](https://twitter.com/search?q=%23100DaysOfCode) to inspire you. Consider including [@talkpython](https://twitter.com/talkpython) and [@pybites](https://twitter.com/pybites) in your tweets.

*See a mistake in these instructions? Please [submit a new issue](https://github.com/talkpython/100daysofcode-with-python-course/issues) or fix it and [submit a PR](https://github.com/talkpython/100daysofcode-with-python-course/pulls).*
