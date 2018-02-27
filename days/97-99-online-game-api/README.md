# Days 97-99 Online Games via a JSON API

This one was a big one wasn't it? Hopefully the real-world nature made it well worth it! Your goal will be to create an online game for another simple game: Hi-lo.

The output looks something like this:

```
---------------------------------
   GUESS THAT NUMBER GAME
---------------------------------

Player what is your name? Michael
Guess a number between 0 and 100: 50
Sorry Michael, your guess of 50 was too HIGH.
Guess a number between 0 and 100: 30
Sorry Michael, your guess of 20 was too HIGH.
Guess a number between 0 and 100: 10
Sorry Michael, your guess of 10 was too LOW.
Guess a number between 0 and 100: 15
Sorry Michael, your guess of 15 was too LOW.
Guess a number between 0 and 100: 19
Excellent work Michael, you won, it was 19!
done
```

There is already an app you can use to get started from here:

**HI-LO GAME**: [`program.py`](https://github.com/mikeckennedy/python-jumpstart-course-demos/blob/master/apps/02-guess-number-app/final/program.py)

## Day N: Add database persistence to the game

On this first day, you already watched the videos. Now you'll need to design what data to store in the database and model that with SQLAlchemy.

Feel free to borrow heavily from our code we already wrote for the **[SQLAlchemy day](https://github.com/talkpython/100daysofcode-with-python-course/tree/master/days/91-93-sqlalchemy)**.

Note that you'll probably want a virtual environment for this one as it involves plenty of external packages.

## Day N+1: Create the web services

Today you'll create a Flask-based web app. For the general structure, feel free to copy from the demo code in this block of days.

You will need to determine the actions that need to happen on the server. For example:

* Create user
* Find user
* Game status
* Play round
* ... ?

Add a web method for each of these and consider the appropriate URLs and endpoints for the data exchange.

Once you have your methods written, test it with a simple tool like [**Postman**](https://www.getpostman.com/).

## Day N+2: Create the program / game app that users use

Final day! Today, write the `uplink` client (or just raw `request` code if you'd rather). Take each method you wrote yesterday for the API and create a client version. If you need a hint, just look at the client we wrote for this block of days.

Once it's working, then write the code for user interaction on the client. 

This python application is the stand-in for the full video game each person plays locally but works with data on the server.

Looking for a bonus? Try to deploy your web app somewhere like Heroku. Here's their quick start: 

**[github.com/heroku/python-getting-started](https://github.com/heroku/python-getting-started)**

### Time to share what you've accomplished!

Be sure to share your last couple of days work on Twitter or Facebook. Use the hashtag **#100DaysOfCode**. 

Here are [some examples](https://twitter.com/search?q=%23100DaysOfCode) to inspire you. Consider including [@talkpython](https://twitter.com/talkpython) and [@pybites](https://twitter.com/pybites) in your tweets.

*See a mistake in these instructions? Please [submit a new issue](https://github.com/talkpython/100daysofcode-with-python-course/issues) or fix it and [submit a PR](https://github.com/talkpython/100daysofcode-with-python-course/pulls).*
