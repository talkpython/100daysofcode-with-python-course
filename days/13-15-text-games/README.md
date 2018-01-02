# 13-15 Text-based Games Challenges

Now that you have seen the videos from day 13 and have some experience with classes and objects, we are going to build another, slightly more complex (but fun!) game.

Perhaps you've heard of [**Rock Paper Scissors**](https://www.wikihow.com/Play-Rock,-Paper,-Scissors). This game is a popular kids game played with just your hands. Make a symbol (rock, paper, or scissors) and both players show their hand at the same time and there are rules about which symbols beat which others. Check out page for details.

[wikihow.com/Play-Rock,-Paper,-Scissors](https://www.wikihow.com/Play-Rock,-Paper,-Scissors)

We are going to build **Rock Paper Scissors**. First, in the simple 3 symbol form (rock, paper, scissors). That will be Day 14. The grand finale for Day 15 will be to build a more complex variant.

Behold **15-way Rock Paper Scissors**!

![](./rps15.jpg)

The way you read this graphic is if an arrow points from one item to another, that pointed-to item is defeated.

For example:

* Paper defeats rock (paper points to rock)
* Devil defeats human (devil points to human)

It turns out to be error prone and generally unfun to work this out. So I created a CSV score sheet representing these relationships. 

[`battle-table.csv`](data/battle-table.csv)

You can use that CSV data to hard code in the different scenarios, or you can read the CSV directly in Python and do it dynamically.

We haven't talked about CSV yet but if you're feeling adventurous, combine what is to follow with the little bit of code shown here that reads the rolls and inspects the wins and losses for each.

[`sample_reader.py`](data/sample_reader.py)

Now, to your challenges!

## Day 13: Learn about classes and get started

1. This day is mostly watching. Watch the corresponding video from the course (if you haven't already).
2. Create a starter project that will be the foundation of **Rock, Paper, Scissors**. All it needs to do is ask the player for their name and print some sort of header telling them the title of the application.

## Day 14: Write standard **Rock, Paper, Scissors**

You will model **Rock, Paper, Scissors** with classes and a game loop. Recall the three rolls (Rock, Paper, and Scissor). These can be just hard coded into your game.

### Classes

`Roll`

* name of roll
* rolls that can be defeated by self
* rolls that defeated self

`Player`

* name of player

### Basic program flow

Your game loop code should look a little like this. It's not exact code but hopefully enough to get you moving without spoiling the fun of creating it. (Not every detail is shown)

```python
def main():
    print_header()

    rolls = build_rolls()

    name = get_players_name()

    player1 = Player(name)
    player2 = Player("computer")

    game_loop(player1, player2, rolls)
```

Be careful of ties! And here is the game loop

```python
def game_loop(player1, player2, rolls):
    count = 1
    while count < 3:
        p2_roll = None # TODO: get random roll
        p1_roll = None # TODO: have player choose a roll

        outcome = p1_roll.can_defeat(p2_roll)

        # display throws
        # display winner for this round

        count += 1

    # Compute who won
```

## Day 15: Write standard **Rock, Paper, Scissors**

Modify the game you created above on Day 14. Use the data in [`battle-table.csv`](data/battle-table.csv) to extend this from just Rocks, Paper, and Scissors, to the 15-way version.

Remember if you want to try to parse the CSV, you can borrow code from [`sample_reader.py`](data/sample_reader.py). 

Alternatively, you could simply hard code the table into the creation of the classes by creating the 15 types and setting who they defeat or are defeated by manually when creating them.
