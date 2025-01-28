from sqlalchemy import Column, Integer, String, Date, ForeignKey ,Time
from sqlalchemy.orm import relationship

from model.entity.base import Base
from model.tools.validation import *
from model.tools.logging import *

from model.entity.ticket import Ticket
