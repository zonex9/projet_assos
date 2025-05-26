from flask import Blueprint,redirect
from src.app.v2.profils import bp_profils
from src.app.v2.associations import bp_associations
bp_v2 = Blueprint('v2', __name__)

bp_v2.register_blueprint(bp_profils)
bp_v2.register_blueprint(bp_associations)

@bp_v2.route('/')
def index():
    """Page principale"""
    
    return "ienvenue sur l’API Assos v2"

