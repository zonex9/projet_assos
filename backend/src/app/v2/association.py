
from flask import Blueprint, render_template, request, redirect, jsonify
from backend.src.app.extensions import db
from backend.src.app.models import Profil, Association

bp_associations = Blueprint("associations", __name__)

@bp_associations.route('/', methods=['GET'])

def index():
    """Page d'accueil des associations"""
    return render_template('association/index.html')


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
                "id": association.profil_id if association.profil else None,
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
    adresse = data.get('adresse')
    mail = data.get('mail')
    logo = data.get('logo')
    description = data.get('description')
    profil_id = data.get('profil_id')

    if not name or not ville or not adresse or not logo or not mail or not description or not profil_id:
        return jsonify({"Erreur": "Données incomplètes"}), 400

    profil = Profil.query.get(profil_id)
    if not profil:
        return jsonify({"Erreur": "Profil non trouvé"}), 404


    association = Association(
        name=name,
        description=description,
        logo=logo,
        mail=mail,
        ville=ville,
        addresse=adresse,
        profil_id=profil_id
    )

    db.session.add(association)
    db.session.commit()

    return jsonify({
        "message": "Association créée",
        "id": association.id
    }), 201

    
@bp_associations.route('/associations/<int:association_id>', methods=['DELETE'])
def delete_association(association_id):
    """Supprimer une association à travers son id"""
    association = Association.query.get(association_id)
    if not association:
        return jsonify({"Erreur": "Association non trouvée"}), 404

    db.session.delete(association)
    db.session.commit()

    return jsonify({"message": "association supprimée avec succès"}), 200