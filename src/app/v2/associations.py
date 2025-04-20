
from flask import Blueprint, render_template, request, redirect, jsonify
from src.app.extensions import db
from src.app.models import Profil, Association

bp_associations = Blueprint("associations", __name__)

@bp_associations.route('/associations', methods=['GET'])
def get_association():
    """Afficher les informations d'une association"""
    associations = Association.query.all()
    associations_data = [
        {
            "id": association.id,
            "name": association.name,
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

@bp_associations.route('/associations', methods=['POST'])
def add_association():
    """Ajouter une association"""
    data = request.get_json()
    name = data.get('name')
    ville = data.get('ville')
    addresse = data.get('adresse')
    logo = data.get('logo')
    mail = data.get('mail')
    profil_id = data.get('profil_id')

    if not name or not ville or not addresse or not logo or not mail or not profil_id:
        return jsonify({"Erreur": "Données incomplètes"}), 400

    profil = Profil.query.get(profil_id)
    if not profil:
        return jsonify({"Erreur": "Profil non trouvé"}), 404

    association = Association(
        name=name,

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
