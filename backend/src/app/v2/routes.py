from flask import Blueprint, render_template, url_for, redirect,render_template_string
from backend.src.app.v2.profils import bp_profils
from backend.src.app.v2.associations import bp_associations
import threading

bp_v2 = Blueprint('v2', __name__)

bp_v2.register_blueprint(bp_profils)
bp_v2.register_blueprint(bp_associations)

@bp_v2.route('/')
def index():
    return render_template(
        'index.html',
        titre="Accueil | Notre Association",
        nom_association="Association Lyon : Gestion des matériels",
        slogan="Association Lyon, pour la gestion des matériels",
        description="L'association Lyon œuvre depuis pluisuers années pour gérer les entrées et les sorties des matériels",
        actions=[
            "Interface dédiée à la gestion des matériels",
            "Suivi de la commande depuis son compte principal 100% en ligne",
            "Prêt en ligne des matériels",
            "Accès au dashboard, reporting et autres fonctionnalité de suivi 100% en ligne"
        ]
    )


