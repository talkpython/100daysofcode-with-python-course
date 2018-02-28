from collections import defaultdict
from typing import List, Optional

# noinspection PyPackageRequirements
from game_logic import session_factory, game_decider
# noinspection PyPackageRequirements
from game_logic.game_decider import Decision
from game_logic.models.move import Move
# noinspection PyPackageRequirements
from game_logic.models.player import Player
# noinspection PyPackageRequirements
from game_logic.models.roll import Roll


def get_game_history(game_id: str) -> List[Move]:
    session = session_factory.create_session()

    query = session.query(Move) \
        .filter(Move.game_id == game_id) \
        .order_by(Move.roll_number) \
        .all()

    moves = list(query)

    session.close()

    return moves


def is_game_over(game_id: str) -> bool:
    history = get_game_history(game_id)
    return any([h.is_winning_play for h in history])


def get_win_count(player: Player) -> int:
    session = session_factory.create_session()

    wins = session.query(Move) \
        .filter(Move.player_id == player.id). \
        filter(Move.is_winning_play) \
        .count()

    session.close()

    return wins


def find_player(name: str) -> Player:
    session = session_factory.create_session()

    player = session.query(Player).filter(Player.name == name).first()
    session.close()

    return player


def create_player(name: str) -> Player:
    session = session_factory.create_session()

    player = session.query(Player).filter(Player.name == name).first()
    if player:
        raise Exception("Player already exists")

    player = Player()
    player.name = name
    session.add(player)
    session.commit()
    session.close()

    player = session.query(Player).filter(Player.name == name).first()
    return player


def all_players() -> List[Player]:
    session = session_factory.create_session()

    players = list(session.query(Player).all())
    session.close()
    return players


def record_roll(player, roll: 'Roll', game_id: str, is_winning_play: bool, roll_num: int):
    session = session_factory.create_session()

    move = Move()
    move.player_id = player.id
    move.roll_id = roll.id
    move.game_id = game_id
    move.is_winning_play = is_winning_play
    move.roll_number = roll_num
    session.add(move)

    session.commit()
    session.close()


def all_rolls() -> List[Roll]:
    session = session_factory.create_session()

    query = session.query(Roll).order_by(Roll.name).all()
    rolls = list(query)

    session.close()

    return rolls


def init_rolls(rolls: List[str]):
    session = session_factory.create_session()
    roll_count = session.query(Roll).count()
    session.close()

    if roll_count:
        return

    for roll_name in rolls:
        create_roll(roll_name)


def find_roll(name: str) -> Optional['Roll']:
    session = session_factory.create_session()

    roll = session.query(Roll).filter(Roll.name == name).first()

    session.close()
    return roll


def create_roll(name: str) -> 'Roll':
    session = session_factory.create_session()

    roll = Roll()
    roll.name = name
    session.add(roll)

    session.commit()
    session.close()

    return find_roll(name)


def find_roll_by_id(roll_id):
    session = session_factory.create_session()
    roll = session.query(Roll).filter(Roll.id == roll_id).first()
    session.close()

    return roll


def find_player_by_id(player_id: int) -> Player:
    session = session_factory.create_session()
    player = session.query(Player).filter(Player.id == player_id).first()
    session.close()

    return player


def count_round_wins(player_id: int, game_id: str) -> int:
    history = get_game_history(game_id)
    wins = 0
    grouped_moves = defaultdict(list)

    for h in history:
        grouped_moves[h.roll_number].append(h)

    for rnd_num, moves in grouped_moves.items():
        player_move = [m for m in moves if m.player_id == player_id][0]
        opponent_move = [m for m in moves if m.player_id != player_id][0]

        player_roll = find_roll_by_id(player_move.roll_id)
        opponent_roll = find_roll_by_id(opponent_move.roll_id)

        outcome = game_decider.decide(player_roll, opponent_roll)
        if outcome == Decision.win:
            wins += 1

    return wins

