from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
from app.db import db  # Importar db desde app.db
from app.models import user  # Importar todos los modelos

# Configuración de Alembic
config = context.config

# Configuración de logging
fileConfig(config.config_file_name)

# Añade aquí tus modelos
target_metadata = db.metadata  # Cambiar Base.metadata a db.metadata

def run_migrations_offline():
    """Ejecuta las migraciones en modo offline."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(url=url, target_metadata=target_metadata, literal_binds=True)

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """Ejecuta las migraciones en modo online."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()