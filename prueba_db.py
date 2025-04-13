from app import create_app, db
from app.models.user import User
import datetime

# Crear la aplicación Flask
app = create_app()

# Crear el contexto de la aplicación
with app.app_context():
    # Crear un nuevo usuario
    user = User(
        first_name="Brahian",
        last_name="Doe",
        username="Brahian",
        email="brahian@example.com",
        password="secure_password"
    )

    # Agregar el usuario a la sesión de la base de datos
    db.session.add(user)

    # Confirmar la transacción (guardar el usuario)
    db.session.commit()

    print(f"Usuario creado con ID: {user.id}")

    # Consultar el usuario recién creado
    user_from_db = User.query.filter_by(username="Brahian").first()
    print(f"Usuario consultado de la base de datos: {user_from_db.username} - {user_from_db.email}")