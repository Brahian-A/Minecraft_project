from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship, validates
from app.db import db
from app import bcrypt
from email_validator import validate_email, EmailNotValidError

class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(32), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password_hash = Column(String(128), nullable=False)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    coins = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relación con MatchPlayer
    matches = relationship('MatchPlayer', back_populates='user', cascade="all, delete-orphan")

    def __init__(self, first_name: str, last_name: str, username: str, email: str, password: str, is_admin: bool = False):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')
        self.is_admin = is_admin

    @validates('first_name')
    def validate_first_name(self, key, value):
        if not value or len(value) > 50:
            raise ValueError("First name is required and cannot exceed 50 characters")
        return value

    @validates('last_name')
    def validate_last_name(self, key, value):
        if not value or len(value) > 50:
            raise ValueError("Last name is required and cannot exceed 50 characters")
        return value

    @validates('email')
    def validate_email(self, key, value):
        try:
            email_info = validate_email(value, check_deliverability=False)
            return email_info.normalized
        except EmailNotValidError as e:
            raise ValueError(f"Invalid email: {e}")

    @validates('password_hash')
    def validate_password(self, key, value):
        if len(value) < 8:
            raise ValueError("La contraseña debe tener al menos 8 caracteres")
        return bcrypt.generate_password_hash(value).decode('utf-8')

    def verify_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"<User(username='{self.username}', coins={self.coins})>"