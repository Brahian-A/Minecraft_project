from app import db
from app.models.user import User
from app import app
import datetime

# Crear la instancia de la aplicación con el contexto adecuado
with app.app_context():
    # Crear un nuevo usuario
    user = User(
        username="Brahian", 
        email="brahian@example.com", 
        password_hash="hashed_password", 
        coins=0, 
        created_at=datetime.datetime.utcnow()
    )

    # Agregar el usuario a la sesión de la base de datos
    db.session.add(user)

    # Confirmar la transacción (guardar el usuario)
    db.session.commit()

    print(f"Usuario creado con ID: {user.id}")

    # Consultar el usuario recién creado
    user_from_db = User.query.filter_by(username="Brahian").first()
    print(f"Usuario consultado de la base de datos: {user_from_db.username} - {user_from_db.email}")
