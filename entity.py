import sqlalchemy as sa

from db import db


class User(db.Model):
    id = sa.Column(sa.Integer, primary_key=True)
    username = sa.Column(sa.String(100), unique=True)
    password = sa.Column(sa.String(250))
