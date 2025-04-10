from __future__ import with_statement
from alembic import context
from sqlalchemy import engine_from_config, pool
from app.db import Base
from app import app  # Importamos tu app de Flask
from flask import current_app

# Importamos todos los modelos
from app.models import *  # Asegúrate de importar todos los modelos para que Alembic los detecte

# Configuración de la base de datos
def get_url():
    return app.config['SQLALCHEMY_DATABASE_URI']

# Configuramos el target_metadata
target_metadata = Base.metadata

# Función para ejecutar las migraciones en modo online
def run_migrations_online():
    # Obtener la URL de la base de datos desde Flask
    connectable = engine_from_config(
        context.config.get_section(context.config.config_ini_section),
        prefix='sqlalchemy.',
        poolclass=pool.NullPool,
        url=get_url()  # Usamos la URL de Flask
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
            compare_server_default=True,
        )

        with context.begin_transaction():
            context.run_migrations()

# Función para ejecutar las migraciones en modo offline
def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    url = get_url()
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

# Ejecutar migraciones
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
