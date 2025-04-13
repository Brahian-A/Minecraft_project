from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from app.db import db

class Game(db.Model):

    __tablename__ = 'games'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(String(255))
    cost_to_join = Column(Integer, default=50)
    reward_on_win = Column(Integer, default=150)

    matches = relationship('Match', back_populates='game')