from sqlalchemy import Integer, Column, String

from model.entity.base import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(20), unique=True, nullable=False)
    password = Column(String(20), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password