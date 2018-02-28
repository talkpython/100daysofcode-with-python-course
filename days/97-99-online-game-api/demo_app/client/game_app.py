import random

from api import GameService


def main():
    svc = GameService()

    print("Game app! (client)")
    print()
    print()
    print("TOP SCORES")
    for s in svc.top_scores():
        print("{} scored {}".format(s.get('player').get('name'), s.get('score')))
    print()

    game_id = svc.create_game().get('game_id')
    rolls = svc.all_rolls()
    player = svc.find_user("Charles")

    is_over = False
    while not is_over:
        name = player.get('name')
        roll = random.choice(rolls)
        rnd = svc.play_round(game_id=game_id, user=name, roll=roll)
        is_over = rnd.get('is_final_round')
        print("Round {}".format(rnd.get('round_number')))
        print("{} rolls {}".format(name, roll))
        print("{} rolls {}".format(rnd.get('opponent').get('name'), rnd.get('computer_roll').get('name')))
        print("Resulting in {}".format(rnd.get('round_outcome')))
        print("")

    game_status = svc.game_status(game_id)
    print("Game is over, outcome: Winner: {}".format(game_status.get('winner').get('name')))


if __name__ == '__main__':
    main()