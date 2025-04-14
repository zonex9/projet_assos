from flask import Flask
from projet_assos.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from src.app.v1.routes import bp_v1
from src.app.v2.routes import bp_v2
from app import models

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Définir le préfixe de l'API à partir de la version dans la config
api_prefix = f"/api/{app.config['API_VERSION']}"

# Enregistrement des blueprints
app.register_blueprint(bp_v1, url_prefix='/v1')
app.register_blueprint(bp_v2, url_prefix='/v2')
