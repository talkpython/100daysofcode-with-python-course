# Days 10-12 Test your code with pytest

In this lesson I show you how to use `pytest` to test a simple guessing game. It might not be the easiest example for a beginner, but it allows me to show some real world issues you want to address in your test code. 

After pip installing the module, I quickly show you how to write a test with `pytest` and how it differs from the classic (more verbose) `unittest` syntax.

Next I show you some tactics to mock out user inputs and random data, because test data needs to be predictable. We also learn how we can capture/test standard output of our program. 

Finally I show you some TDD or _test driven development_ in action by implementing _Fizz Buzz_ by writing the tests first, in small incremental steps. You learn about the `pytest.mark.parametrize` decorator to elegantly handle repetitive tests.

The `pytest` framework is huge and this is just a subset of features. I hope this gives you a head start though to start writing (more) tests for your programs to produce more reliable software. 

Be warned: mastering `pytest` might feel like possessing a super power!

## Day N: Setup + Learn pytest

Today you will pip install `pytest` and `pytest-cov` (best practice is to use a [virtual environment](https://pybit.es/the-beauty-of-virtualenv.html)) and watch the video lectures. 

Start thinking about how you can write tests for your code ...

## Day N+1: Your Turn: Test your code

Head over to [PyBites Code Challenge 39 - Writing Tests With Pytest](https://codechalleng.es/challenges/39/) and start adding tests to your code or if you're already covered maybe you want to do that as contribution to an open source project? 

By the way, notice that we use `pytest` for [our Bites](https://codechalleng.es/bites/) too. Under the _TESTS_ tab of each Bite you can see how your code will be tested and when you hit _Save + verify_ you can look at its output. 

Lastly if you are serious about writing tests and `pytest` check out Brian Okken's [Test and Code](http://testandcode.com) podcast and his [Python Testing with pytest](https://pragprog.com/book/bopytest/python-testing-with-pytest) book which goes into much more depth.

## Day N+2: Your Turn: Write a fixture

You wrote some test code? Good, hope that felt good. I know it does because with a set of tests you have more confidence to make any changes in the future. Software systems become increasingly complex so it's paramount to have a suite of tests as your project grows to catch any regression bugs. 

On the topic of more complex code, one thing I did not cover are `pytest` fixtures:

> The purpose of test fixtures is to provide a fixed baseline upon which tests can reliably and repeatedly execute. pytest fixtures offer dramatic improvements over the classic xUnit style of setup/teardown functions - [pytest fixtures: explicit, modular, scalable](https://docs.pytest.org/en/latest/fixture.html)

A typical example is a database app that needs to setup and tear down its state before each test. Today try to come up with a use case to use `@pytest.fixture` after checking out our article: [All You Need to Know to Start Using Fixtures in Your pytest Code](https://pybit.es/pytest-fixtures.html).

Ready to become a `pytest` ninja? You can do it!

### Time to share what you've accomplished!

Be sure to share your last couple of days work on Twitter or Facebook. Use the hashtag **#100DaysOfCode**. 

Here are [some examples](https://twitter.com/search?q=%23100DaysOfCode) to inspire you. Consider including [@talkpython](https://twitter.com/talkpython) and [@pybites](https://twitter.com/pybites) in your tweets.

*See a mistake in these instructions? Please [submit a new issue](https://github.com/talkpython/100daysofcode-with-python-course/issues) or fix it and [submit a PR](https://github.com/talkpython/100daysofcode-with-python-course/pulls).*
