
from model.entity import *


class Ticket(Base):
    __tablename__ = 'tickets'

    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _name = Column("name", String(30))
    _title = Column("title" ,String(30))
    _description = Column("description", String(50))
    _time = Column("time", String(30))
    _date = Column("date", Date)
    _state = Column("state", String(30))

    def __init__(self, name, title, description, time, date,state):
        self.id = None
        self.name = name
        self.title = title
        self.description = description
        self.time = time
        self.date = date
        self.state = state


    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = name_validator(value)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = name_validator(value)

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, value):
        self._time = time_validator(value)


    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = date_validator(value)

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = state_validator(value)



