from collections import defaultdict

from game_logic import game_service, game_decider
from game_logic.game_decider import Decision
from game_logic.models.player import Player
from game_logic.models.roll import Roll


class GameRound:

    def __init__(self, game_id: str, player1: Player, player2: Player,
                 p1_roll: Roll, p2_roll: Roll):
        self.p2_roll = p2_roll
        self.p1_roll = p1_roll
        self.game_id = game_id
        self.player1 = player1
        self.player2 = player2

        self.decision_p1_to_p2 = None
        history = game_service.get_game_history(game_id)
        self.round = len(history) // 2 + 1
        self.player1_wins = GameRound.count_wins(self.player1, history)
        self.player2_wins = GameRound.count_wins(self.player2, history)
        self.WIN_COUNT_MIN = 3
        self.PLAY_COUNT_MIN = 5
        self.is_over = game_service.is_game_over(game_id)

    def play(self):
        if self.is_over:
            raise Exception("Game is already over, cannot play further.")

        d = game_decider.decide(self.p1_roll, self.p2_roll)
        self.decision_p1_to_p2 = d

        self.record_roll(d, self.player1, self.p1_roll, self.player1_wins)
        self.record_roll(d.reversed(), self.player2, self.p2_roll, self.player2_wins)

        print("RECORDING ROUND")
        print("Player 1: {}, prior wins {}, outcome: {}".format(self.p1_roll.name, self.player1_wins, d))
        print("Player 2: {}, prior wins {}, outcome: {}".format(self.p2_roll.name, self.player2_wins, d.reversed()))
        print()

        self.is_over = game_service.is_game_over(self.game_id)

    def record_roll(self, decision: Decision, player: Player, roll: Roll, win_count: int):
        final_round_candidate = self.round >= self.PLAY_COUNT_MIN and win_count + 1 >= self.WIN_COUNT_MIN
        wins_game = final_round_candidate and decision == Decision.win

        game_service.record_roll(player, roll, self.game_id, wins_game, self.round)

    @staticmethod
    def count_wins(player, history):
        grouped_moves = defaultdict(list)

        for h in history:
            grouped_moves[h.roll_number].append(h)

        win_count = 0
        for rnd_data in grouped_moves.values():
            if len(rnd_data) != 2:
                continue

            player_move = [m for m in rnd_data if m.player_id == player.id][0]
            opponent_move = [m for m in rnd_data if m.player_id != player.id][0]

            player_roll = game_service.find_roll_by_id(player_move.roll_id)
            opponent_roll = game_service.find_roll_by_id(opponent_move.roll_id)

            if game_decider.decide(player_roll, opponent_roll) == Decision.win:
                win_count += 1

        return win_count
