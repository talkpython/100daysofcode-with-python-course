from typing import List, Optional

# noinspection PyPackageRequirements
from data import session_factory
# noinspection PyPackageRequirements
from models.move import Move
# noinspection PyPackageRequirements
from models.player import Player
# noinspection PyPackageRequirements
from models.roll import Roll


def get_game_history(game_id: str) -> List[Move]:
    session = session_factory.create_session()

    query = session.query(Move)\
        .filter(Move.game_id == game_id)\
        .order_by(Move.roll_number)\
        .all()

    moves = list(query)

    session.close()

    return moves


def get_win_count(player: Player) -> int:
    session = session_factory.create_session()

    wins = session.query(Move) \
        .filter(Move.player_id == player.id). \
        filter(Move.is_winning_play) \
        .count()

    session.close()

    return wins


def find_or_create_player(name: str) -> Player:
    session = session_factory.create_session()

    player = session.query(Player).filter(Player.name == name).first()
    if player:
        session.close()
        return player

    player = Player()
    player.name = name
    session.add(player)
    session.commit()

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
    roll = session.query(Roll).filter(Roll.id == roll.id).first()
    return roll
