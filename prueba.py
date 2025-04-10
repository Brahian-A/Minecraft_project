from app import db, app
from app.models.user import User
import datetime

with app.app_context():
    # Crear un nuevo usuario
    user = User(
        username="Brahian", 
        email="brahian@example.com", 
        password_hash="hashed_password", 
        coins=0, 
        created_at=datetime.datetime.now(datetime.timezone.utc)  # Usa timezone-aware
    )
    db.session.add(user)
    db.session.commit()

    print(f"Usuario creado con ID: {user.id}")

    # Consultar el usuario recién creado
    user_from_db = User.query.filter_by(username="Brahian").first()
    print(f"Usuario consultado de la base de datos: {user_from_db.username} - {user_from_db.email}")
