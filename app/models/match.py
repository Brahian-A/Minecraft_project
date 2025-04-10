from datetime import datetime
from app.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship

class Match(Base):
    __tablename__ = 'matches'

    id = Column(Integer, primary_key=True)
    game_id = Column(Integer, ForeignKey('games.id'), nullable=False)
    host_server = Column(String(255))  # IP o identificador del servidor
    status = Column(String(20), default='waiting')  # waiting, playing, finished
    created_at = Column(DateTime, default=datetime.utcnow)

 # Relación con el modelo 'Game'
    game = relationship('Game', back_populates='matches')
# Relación con los jugadores (creado en 'MatchPlayer')
    players = relationship('MatchPlayer', back_populates='match')


def __repr__(self):
    return f"<Match(game_id={self.game_id}, status={self.status})>"