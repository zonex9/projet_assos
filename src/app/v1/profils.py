from flask import Blueprint, render_template, request, redirect, jsonify
from src.app.extensions import db 
from src.app.models import Profil, Association

bp_profils = Blueprint("profils", __name__)

@bp_profils.route('/profils', methods=['GET'])
def get_profils():
    """Lister tous les profils"""
    profils = Profil.query.all()
    profils_data = [
        {
            "id": profil.id,
            "name": profil.name,
        }
        for profil in profils
    ]
    return jsonify(profils_data)

@bp_profils.route('/profils/<int:profil_id>', methods=['GET'])
def get_profil(profil_id):
    """Lister les détails d'un profil par id"""
    profil = Profil.query.get(profil_id)
    if not profil:
        return jsonify({"Erreur": "Profil non trouvé"}), 404

    profil_data = {
        "id": profil.id,
        "name": profil.name,
        "description": profil.description
    }
    return jsonify(profil_data)

@bp_profils.route('/profils/<int:profil_id>', methods=['PUT'])
def update_profil(profil_id):
    """Modifier les informations d'un profil par id"""
    data = request.get_json()

    if not data or not data.get('name') or not data.get('description'):
        return jsonify({"Erreur": "Données invalides"}), 400

    profil = Profil.query.get(profil_id)
    if not profil:
        return jsonify({"Erreur": "Profil non trouvé"}), 404

    profil.name = data['name']
    profil.description = data['description']
    db.session.commit()

    return jsonify({"message": "Profil mis à jour avec succès", "id": profil.id}), 200

@bp_profils.route('/profils/<int:profil_id>', methods=['DELETE'])
def delete_profil(profil_id):
    """Supprimer un profil à travers son id"""
    profil = Profil.query.get(profil_id)
    if not profil:
        return jsonify({"Erreur": "Profil non trouvé"}), 404

    db.session.delete(profil)
    db.session.commit()

    return jsonify({"message": "Profil supprimé avec succès"}), 200

@bp_profils.route('/profils', methods=['POST'])
def add_profil():
    """Ajouter un profil"""
    data = request.get_json()
    if not data or not data.get('name') or not data.get('description'):
        return jsonify({"Erreur": "Données invalides"}), 400

    profil = Profil(
        name=data['name'],
        description=data['description']
    )

    db.session.add(profil)
    db.session.commit()

    return jsonify({"message": "Profil ajouté avec succès", "id": profil.id}), 201
