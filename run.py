from app import create_app, db
from flask_migrate import Migrate
from dotenv import load_dotenv
from app import create_app, db

# Cargar variables de entorno
load_dotenv()

# Crear la aplicación Flask
app = create_app()

# Inicializar Flask-Migrate
migrate = Migrate(app, db)

# Importar modelos para que Flask-Migrate los detecte
from app.models.user import User
from app.models.game import Game
from app.models.match import Match
from app.models.MatchPlayer import MatchPlayer

if __name__ == '__main__':
    app.run(debug=True)