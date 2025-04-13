from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship
from app.db import db

class MatchPlayer(db.Model):
    __tablename__ = 'match_players'

    id = Column(Integer, primary_key=True)
    match_id = Column(Integer, ForeignKey('matches.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    is_winner = Column(Integer, default=0)  # 0 = no, 1 = sí

    match = relationship('Match', back_populates='players')
    user = relationship('User', back_populates='matches')