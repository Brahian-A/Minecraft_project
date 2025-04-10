from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from app.db import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(32), unique=True, nullable=False)
    email = Column(String(120), unique=True)
    password_hash = Column(String(128), nullable=False)
    coins = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)

    
    #Relación con MatchPlayer (se agrega cuando lo tengamos creado)
    matches = relationship('MatchPlayer', back_populates='user', cascade="all, delete-orphan")

    def __repr__(self):
        return f"<User(username='{self.username}', coins={self.coins})>"