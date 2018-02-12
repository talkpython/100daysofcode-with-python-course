from typing import List, Optional

from models.move import Move
from models.player import Player
from models.roll import Roll


def get_game_history(game_id: str) -> List[Move]:
    # TODO: Return list of moves

    return []


def get_win_count(player: Player) -> int:
    # TODO: Count wins

    return 0


def find_or_create_player(name: str) -> Player:
    player = Player()
    player.name = name
    return player


def all_players() -> List[Player]:
    return []


def record_roll(player, roll: 'Roll', game_id: str, is_winning_play: bool, roll_num: int):
    move = Move()
    # move.player_id = player.id
    # move.roll_id = roll.id
    move.game_id = game_id
    move.is_winning_play = is_winning_play
    move.roll_number = roll_num

    # TODO: Record


def all_rolls() -> List[Roll]:
    # TODO: Find all rolls.
    pass


def find_roll(name: str) -> Optional['Roll']:
    # TODO: Find roll
    pass


def create_roll(name: str) -> 'Roll':
    roll = Roll(name)
    # TODO: Save
    return roll
