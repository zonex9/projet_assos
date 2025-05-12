from flask import Blueprint
from src.app.v1.profils import bp_profils

bp_v1 = Blueprint('v1', __name__)
bp_v1.register_blueprint(bp_profils)

@bp_v1.route('/')
def index():
    return "Bienvenue sur l’API Assos v1"

