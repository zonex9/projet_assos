
from flask import Blueprint, render_template, request, redirect, jsonify
from app import app, db
from app.models import Profil, Association

bp_v2 = Blueprint('v2', __name__)

@bp_v2.route('/associations', methods=['GET'])
def get_association():
    """Afficher les informations d'une association"""
    associations = Association.query.all()
    associations_data = [
        {
            "id": association.id,
            "nom": association.nom,
            "ville": association.ville,
            "addresse": association.addresse,
            "logo": association.logo,
            "mail": association.mail,
            "profil": {
                "id": association.profil.id if association.profil else None,
                "name": association.profil.name if association.profil else None,
                "description": association.profil.description if association.profil else None
            }
        }
        for association in associations
    ]
    return jsonify(associations_data)

@bp_v2.route('/associations', methods=['POST'])
def add_association():
    """Ajouter une association"""
    data = request.get_json()

    nom = data.get('nom')
    ville = data.get('ville')
    addresse = data.get('addresse')
    logo = data.get('logo')
    mail = data.get('mail')
    profil_id = data.get('profil_id')

    if not nom or not ville or not addresse or not logo or not mail or not profil_id:
        return jsonify({"Erreur": "Données incomplètes"}), 400

    profil = Profil.query.get(profil_id)
    if not profil:
        return jsonify({"Erreur": "Profil non trouvé"}), 404

    association = Association(
        nom=nom,
        ville=ville,
        addresse=addresse,
        logo=logo,
        mail=mail,
        profil_id=profil_id
    )

    db.session.add(association)
    db.session.commit()

    return jsonify({
        "message": "Association créée",
        "id": association.id
    }), 201
