from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from app.db import db

# Inicializar extensiones
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Inicializar extensiones con la aplicación
    bcrypt.init_app(app)
    db.init_app(app)

    # Registrar blueprints o rutas si es necesario
    return app