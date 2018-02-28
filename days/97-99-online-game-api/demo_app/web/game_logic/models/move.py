import datetime
import sqlalchemy

# noinspection PyPackageRequirements
from game_logic.models.model_base import ModelBase


class Move(ModelBase):
    __tablename__ = 'moves'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    created = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now, index=True)
    roll_id = sqlalchemy.Column(sqlalchemy.Integer, index=True)
    game_id = sqlalchemy.Column(sqlalchemy.String, index=True)
    roll_number = sqlalchemy.Column(sqlalchemy.Integer, index=True)
    player_id = sqlalchemy.Column(sqlalchemy.Integer, index=True)
    is_winning_play = sqlalchemy.Column(sqlalchemy.Boolean, index=True, default=False)

    def to_json(self, roll: 'Roll', player: 'Player'):
        if self.roll_id != roll.id:
            raise Exception("Mismatched roll values")
        if self.player_id != player.id:
            raise Exception("Mismatched player values")

        return {
            'id': self.id,
            'created': self.created.isoformat(),
            'roll_id': self.roll_id,
            'roll': roll.name,
            'player_id': self.player_id,
            'player': player.name,
            'roll_number': self.roll_number,
            'is_winning_play': self.is_winning_play,
        }
