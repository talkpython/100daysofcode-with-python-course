import csv
from enum import Enum

from game_logic.models.roll import Roll
from data import db_folder

__winner_lookup = {}


class Decision(Enum):
    tie = 1
    win = 2
    lose = 3

    def reversed(self):
        if self == Decision.win:
            return Decision.lose
        if self == Decision.lose:
            return Decision.win

        return Decision.tie

    def __str__(self):
        if self == Decision.win:
            return 'win'
        if self == Decision.lose:
            return 'lose'
        if self == Decision.tie:
            return 'tie'

        return "UNKNOWN DECISION: {}".format(self)


def decide(roll1: Roll, roll2: Roll) -> Decision:
    __build_decisions()

    if roll1.name == roll2.name:
        return Decision.tie

    roll1_wins = roll2.name in __winner_lookup[roll1.name]

    if roll1_wins:
        return Decision.win
    else:
        return Decision.lose


def __build_decisions():
    if __winner_lookup:
        return

    file = db_folder.get_db_path('battle-table.csv')

    with open(file) as fin:
        reader = csv.DictReader(fin)
        for row in reader:
            __build_roll(row)


def __build_roll(row: dict):
    row = dict(row)
    name = row['Attacker']

    del row['Attacker']
    del row[name]

    __winner_lookup[name] = set()
    for k in row.keys():
        can_defeat = row[k].strip().lower() == 'win'
        if can_defeat:
            __winner_lookup[name].add(k)


def all_roll_names():
    __build_decisions()
    return [k for k, v in __winner_lookup.items()]
