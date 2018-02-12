import datetime

import sqlalchemy

# noinspection PyPackageRequirements
from models.model_base import ModelBase


class Player(ModelBase):
    __tablename__ = 'players'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    created = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
