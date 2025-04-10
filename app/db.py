from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
import os

# Base para los modelos
Base = declarative_base()

# URL de la base de datos
# Podés cambiar esto a PostgreSQL, SQLite, etc.

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///db.sqlite3")

# Crear motor y sesión
engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

# Función para usar en Flask
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()