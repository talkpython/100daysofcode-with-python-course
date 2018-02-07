{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## First day: list comprehensions and generators"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "> List comprehensions and generators are in my top 5 favorite Python features leading to clean, robust and Pythonic code. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "from collections import Counter\n",
    "import calendar\n",
    "import itertools\n",
    "import random\n",
    "import re\n",
    "import string\n",
    "\n",
    "import requests"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### List comprehensions"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's dive straight into a practical example. We all know how to use the classic for loop in Python, say I want to loop through a bunch of names title-casing each one:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['pybites', 'mike', 'bob', 'julian', 'tim', 'sara', 'guido']"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "names = 'pybites mike bob julian tim sara guido'.split()\n",
    "names"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Pybites\n",
      "Mike\n",
      "Bob\n",
      "Julian\n",
      "Tim\n",
      "Sara\n",
      "Guido\n"
     ]
    }
   ],
   "source": [
    "for name in names:\n",
    "    print(name.title())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Then I want to only keep the names that start with A-M, the `strings` module makes it easier (we love Python's standard library!):"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "first_half_alphabet = list(string.ascii_lowercase)[:13]\n",
    "first_half_alphabet"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Mike', 'Bob', 'Julian', 'Guido']"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "new_names = []\n",
    "for name in names:\n",
    "    if name[0] in first_half_alphabet:\n",
    "        new_names.append(name.title())\n",
    "new_names"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Feels verbose, not? \n",
    "\n",
    "If you don't know about list comprehensions you might start using them everywhere after seeing the next refactoring:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Mike', 'Bob', 'Julian', 'Guido']"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "new_names2 = [name.title() for name in names if name[0] in first_half_alphabet]\n",
    "new_names2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "assert new_names == new_names2"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "From 4 to 1 lines of code, and it reads pretty well too. That's why we love and stick with Python! \n",
    "\n",
    "Here is another example I used recently to do a most common word count on Harry Potter. I used some list comprehensions to clean up the words before counting them:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['the', 'boy', 'who', 'lived', 'mr.']"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "resp = requests.get('http://projects.bobbelderbos.com/pcc/harry.txt')\n",
    "words = resp.text.lower().split()\n",
    "words[:5]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[('the', 202), ('he', 136), ('a', 108), ('and', 100), ('to', 93)]"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "cnt = Counter(words)\n",
    "cnt.most_common(5)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Hmm should not count stopwords, also:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'-' in words"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's first clean up any non-alphabetic characters:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "words = [re.sub(r'\\W+', r'', word) for word in words]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'-' in words"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'the' in words"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Ok let's filter those stopwords out plus the empty strings caussed by the previous list comprehension:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['a', 'about', 'above', 'across', 'after']"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "resp = requests.get('http://projects.bobbelderbos.com/pcc/stopwords.txt')\n",
    "stopwords = resp.text.lower().split()\n",
    "stopwords[:5]  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['boy', 'lived', 'mr', 'mrs', 'dursley']"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "words = [word for word in words if word.strip() and word not in stopwords]\n",
    "words[:5]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'the' in words"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now it looks way better:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[('dursley', 45),\n",
       " ('dumbledore', 35),\n",
       " ('said', 32),\n",
       " ('mr', 30),\n",
       " ('professor', 30)]"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "cnt = Counter(words)\n",
    "cnt.most_common(5)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "What's interesting here is that the first bit of the list comprehension can be an expression like `re.sub`. The final bit can be a compound statement: here we checked for a non-empty word (' ' -> `strip()` -> '' = `False` in Python) `and` we checked `word not in stopwords`. \n",
    "\n",
    "Again, a lot is going on in one line of code, but the beauty of it is that it is totally fine, because it reads like plain English :)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Generators"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "A generator is a function that returns an iterator. It generates values using the `yield` keyword, when called with next() (a for loop does this implicitly), and it raises a `StopIteration` exception when there are no more values to generate. Let's see what this means with a very simple example:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "def num_gen():\n",
    "    for i in range(5):\n",
    "        yield i\n",
    "        \n",
    "gen = num_gen()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "next(gen)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "2\n",
      "3\n",
      "4\n"
     ]
    }
   ],
   "source": [
    "# note it takes off where we left it last statement\n",
    "for i in gen:\n",
    "    print(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "ename": "StopIteration",
     "evalue": "",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mStopIteration\u001b[0m                             Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-21-63d934b06ce9>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0;31m# no more values to generate\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 2\u001b[0;31m \u001b[0mnext\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mgen\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;31mStopIteration\u001b[0m: "
     ]
    }
   ],
   "source": [
    "# no more values to generate\n",
    "next(gen)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [],
   "source": [
    "# for catches the exception for us\n",
    "for i in gen:\n",
    "    print(i)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "> The `StopIteration` error appears because there are no more yield statements in the function. Calling next on the generator after this does not cause it to loop over and start again. - [Generators are Awesome, Learning by Example\n",
    "](https://pybit.es/generators.html)\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Since learning about generators, a common pattern I use is to build up my sequences:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['red', 'yellow', 'blue', 'white', 'black', 'green', 'purple']"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "options = 'red yellow blue white black green purple'.split()\n",
    "options"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "My older code:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [],
   "source": [
    "def create_select_options(options=options):\n",
    "    select_list = []\n",
    "    \n",
    "    for option in options:\n",
    "        select_list.append(f'<option value={option}>{option.title()}</option>')\n",
    "    \n",
    "    return select_list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['<option value=red>Red</option>',\n",
      " '<option value=yellow>Yellow</option>',\n",
      " '<option value=blue>Blue</option>',\n",
      " '<option value=white>White</option>',\n",
      " '<option value=black>Black</option>',\n",
      " '<option value=green>Green</option>',\n",
      " '<option value=purple>Purple</option>']\n"
     ]
    }
   ],
   "source": [
    "from pprint import pprint as pp\n",
    "pp(create_select_options())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Using a generator you can write this in 2 lines of code - my newer code:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [],
   "source": [
    "def create_select_options_gen(options=options):    \n",
    "    for option in options:\n",
    "        yield f'<option value={option}>{option.title()}</option>'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<generator object create_select_options_gen at 0x10afca570>\n"
     ]
    }
   ],
   "source": [
    "print(create_select_options_gen())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Note that generators are _lazy_ so you need to explicitly consume them by iterating over them, for example by looping over them. Another way is to pass them into the `list()` constructor:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['<option value=red>Red</option>',\n",
       " '<option value=yellow>Yellow</option>',\n",
       " '<option value=blue>Blue</option>',\n",
       " '<option value=white>White</option>',\n",
       " '<option value=black>Black</option>',\n",
       " '<option value=green>Green</option>',\n",
       " '<option value=purple>Purple</option>']"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list(create_select_options_gen())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Specially when working with large data sets you definitely want to use generators. Lists can only get as big as they fit memory size. Generators are lazily evaluated meaning that they only hold a certain amount of data in memory at once. Just for the sake of giving Python something to do, let's calculate leap years for a million years, and compare performance of list vs generator:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [],
   "source": [
    "# list\n",
    "def leap_years_lst(n=1000000):\n",
    "    leap_years = []\n",
    "    for year in range(1, n+1):\n",
    "        if calendar.isleap(year):\n",
    "            leap_years.append(year)\n",
    "    return leap_years\n",
    "\n",
    "# generator\n",
    "def leap_years_gen(n=1000000):\n",
    "    for year in range(1, n+1):\n",
    "        if calendar.isleap(year):\n",
    "            yield year"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "PRO  tip: [since Python 3.3](https://docs.python.org/3/whatsnew/3.3.html) you can use the `yield from` syntax."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "396 ms ± 14.9 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)\n"
     ]
    }
   ],
   "source": [
    "# this had me waiting for a few seconds\n",
    "%timeit -n1 leap_years_lst()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The slowest run took 4.72 times longer than the fastest. This could mean that an intermediate result is being cached.\n",
      "870 ns ± 682 ns per loop (mean ± std. dev. of 7 runs, 1 loop each)\n"
     ]
    }
   ],
   "source": [
    "# this was instant\n",
    "%timeit -n1 leap_years_gen()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "That is pretty impressive. This is an important concept to know about because Big Data is here to stay!"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Second day: practice"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Look at your code and see if you can refactor it to use list comprehensions. Same for generators. Are you building up a list somewhere where you could potentially use a generator?"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "And/or exercise here, take this list of names:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [],
   "source": [
    "NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',\n",
    "         'julian sequeira', 'sandra bullock', 'keanu reeves',\n",
    "         'julbob pybites', 'bob belderbos', 'julian sequeira',\n",
    "         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Can you write a simple list comprehension to convert these names to title case (brad pitt -> Brad Pitt). Or reverse the first and last name? "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Then use this same list and make a little generator, for example to randomly return a pair of names, try to make this work:\n",
    "\n",
    "    pairs = gen_pairs()\n",
    "    for _ in range(10):\n",
    "        next(pairs)\n",
    "\n",
    "Should print (values might change as random):\n",
    "\n",
    "    Arnold teams up with Brad\n",
    "    Alec teams up with Julian\n",
    "\n",
    "Have fun!"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Third day: solution / simulate unix pipelines"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "I hope yesterday's exercise was reasonably doable for you. Here are the answers in case you got stuck:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Arnold Schwarzenegger',\n",
       " 'Alec Baldwin',\n",
       " 'Bob Belderbos',\n",
       " 'Julian Sequeira',\n",
       " 'Sandra Bullock',\n",
       " 'Keanu Reeves',\n",
       " 'Julbob Pybites',\n",
       " 'Bob Belderbos',\n",
       " 'Julian Sequeira',\n",
       " 'Al Pacino',\n",
       " 'Brad Pitt',\n",
       " 'Matt Damon',\n",
       " 'Brad Pitt']"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# list comprehension to title case names\n",
    "[name.title() for name in NAMES]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['schwarzenegger arnold',\n",
       " 'baldwin alec',\n",
       " 'belderbos bob',\n",
       " 'sequeira julian',\n",
       " 'bullock sandra',\n",
       " 'reeves keanu',\n",
       " 'pybites julbob',\n",
       " 'belderbos bob',\n",
       " 'sequeira julian',\n",
       " 'pacino al',\n",
       " 'pitt brad',\n",
       " 'damon matt',\n",
       " 'pitt brad']"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# list comprehension to reverse first and last names\n",
    "# using a helper here to show you that list comprehensions can be passed in functions!\n",
    "\n",
    "def reverse_first_last_names(name):\n",
    "    first, last = name.split()\n",
    "    # ' '.join([last, first]) -- wait we have f-strings now (>= 3.6)\n",
    "    return f'{last} {first}'\n",
    "\n",
    "[reverse_first_last_names(name) for name in NAMES]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [],
   "source": [
    "def gen_pairs():\n",
    "    # again a list comprehension is great here to get the first names\n",
    "    # and title case them in just 1 line of code (this comment took 2)\n",
    "    first_names = [name.split()[0].title() for name in NAMES]\n",
    "    while True:\n",
    "        \n",
    "        # added this when I saw Julian teaming up with Julian (always test your code!)\n",
    "        first, second = None, None\n",
    "        while first == second: \n",
    "            first, second = random.sample(first_names, 2)\n",
    "        \n",
    "        yield f'{first} teams up with {second}'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Alec teams up with Julbob\n",
      "Keanu teams up with Bob\n",
      "Keanu teams up with Julbob\n",
      "Julian teams up with Arnold\n",
      "Bob teams up with Alec\n",
      "Matt teams up with Alec\n",
      "Julbob teams up with Brad\n",
      "Julian teams up with Alec\n",
      "Julian teams up with Julbob\n",
      "Julbob teams up with Julian\n"
     ]
    }
   ],
   "source": [
    "pairs = gen_pairs()\n",
    "for _ in range(10):\n",
    "    print(next(pairs))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Another way to get a slice of a generator is using `itertools.islice`:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<itertools.islice at 0x10b1002c8>"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "first_ten = itertools.islice(pairs, 10)\n",
    "first_ten"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Sandra teams up with Julian',\n",
       " 'Matt teams up with Julian',\n",
       " 'Al teams up with Julian',\n",
       " 'Brad teams up with Julian',\n",
       " 'Alec teams up with Arnold',\n",
       " 'Matt teams up with Bob',\n",
       " 'Matt teams up with Julian',\n",
       " 'Julbob teams up with Julian',\n",
       " 'Brad teams up with Julian',\n",
       " 'Julian teams up with Julbob']"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list(first_ten)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Further practice"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Read up on set and dict comprehensions, then try these two Bites:\n",
    "- [Bite 5. Parse a list of names](https://codechalleng.es/bites/5/) (use a set comprehension in first function)\n",
    "- [Bite 26. Dictionary comprehensions are awesome](https://codechalleng.es/bites/promo/awesome-dict-comprehensions)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Here is a more advanced generators exercise you can try: [Code Challenge 11 - Generators for Fun and Profit](https://codechalleng.es/challenges/11/)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Time to share what you've accomplished!\n",
    "\n",
    "Be sure to share your last couple of days work on Twitter or Facebook. Use the hashtag **#100DaysOfCode**. \n",
    "\n",
    "Here are [some examples](https://twitter.com/search?q=%23100DaysOfCode) to inspire you. Consider including [@talkpython](https://twitter.com/talkpython) and [@pybites](https://twitter.com/pybites) in your tweets.\n",
    "\n",
    "*See a mistake in these instructions? Please [submit a new issue](https://github.com/talkpython/100daysofcode-with-python-course/issues) or fix it and [submit a PR](https://github.com/talkpython/100daysofcode-with-python-course/pulls).*"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "venv",
   "language": "python",
   "name": "venv"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
