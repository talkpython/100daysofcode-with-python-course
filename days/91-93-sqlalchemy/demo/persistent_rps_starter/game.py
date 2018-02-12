import random
import uuid
from typing import List

import game_decider
import game_service
from models.roll import Roll


def game_loop(player1, player2, rolls):
    game_id = str(uuid.uuid4())
    count = 1
    p1_wins = 0
    p2_wins = 0
    while count <= 5 or (p1_wins == p2_wins and count > 5):
        print(" ------------- ROUND {} --------------".format(count))
        print()
        p1_roll = get_roll_choice(rolls)
        p2_roll = random.choice(rolls)

        outcome = game_decider.decide(p1_roll, p2_roll)
        if outcome == game_decider.Decision.tie:
            msg = "Tie!"
        elif outcome == game_decider.Decision.win:
            msg = player1.name + " wins!"
            p1_wins += 1
        else:
            msg = player1.name + " is defeated!"
            p2_wins += 1

        final_move = count >= 5 and p1_wins != p2_wins
        game_service.record_roll(player1, p1_roll, game_id,
                                 p1_wins > p2_wins and final_move, count)
        game_service.record_roll(player2, p2_roll, game_id,
                                 p2_wins > p1_wins and final_move, count)

        print()
        print(player1.name + " throws " + p1_roll.name)
        print(player2.name + " throws " + p2_roll.name)
        print(msg)
        print()
        print(" -------------------------------------")
        print()

        count += 1

    if p1_wins < p2_wins:
        print(player2.name + " wins {} to {}".format(p2_wins, p1_wins))
    else:
        print(player1.name + " wins {} to {}".format(p1_wins, p2_wins))

    show_history([player1, player2], rolls, game_id)


def show_history(players, rolls, game_id):
    pass
    # TODO: Show history


def get_roll_choice(rolls: List[Roll]):
    print("Rolls: ")
    for idx, r in enumerate(rolls):
        print("{}. {}".format(idx + 1, r.name))
    print()
    idx = int(input("What roll will you throw? "))
    return rolls[idx - 1]
