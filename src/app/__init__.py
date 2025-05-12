from flask import Flask,redirect
from config import Config
from flask_sqlalchemy import SQLAlchemy
from src.app.extensions import db, migrate

def create_app():
    """Crée et configure l'application Flask principale."""
    
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    from src.app.v1.routes import bp_v1
    app.register_blueprint(bp_v1, url_prefix='/v1')

    from src.app.v2.routes import bp_v2
    app.register_blueprint(bp_v2, url_prefix='/v2')


    # Dernière version
    LATEST_VERSION = 'v2'

    @app.route('/latest')
    def redirect_to_latest_root():
        # Redirige vers /v2 -> ce qui déclenche la fonction index() de v2
        return redirect(f'/{LATEST_VERSION}', code=302)


    @app.route('/latest/profils/<int:profil_id>', methods=['GET'])
    def get_profil(profil_id):
        return redirect(f'/v2/profils/{profil_id}')
    
    
    return app
