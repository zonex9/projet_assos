from flask import render_template, request, redirect
from app import app, db
from app.models import Profil, Association
from flask import jsonify

@app.route('/')
@app.route('/index')
def index():
    """Page principale"""
    return "Bienvenue sur le projet assos"


@app.route('/')
@app.route('/profils')
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


@app.route('/profil/<int:profil_id>', methods=['GET'])
def get_profil(profil_id):
    """Lister les détails d'un profil par id"""
    profil = Profil.query.get(profil_id)
    if profil is None:
        return jsonify({"Erreur": "Profil non trouvé"}), 404

    profil_data = {
        "id": profil.id,
        "name": profil.name,
        "description": profil.description
    }
    return jsonify(profil_data)


@app.route('/profil/update/<int:profil_id>', methods=['PUT'])
def update_profil(profil_id):
    """Modifier les informations d'un profil par id"""
    data = request.get_json()

    if not data or 'name' not in data or 'description' not in data:
        return jsonify({"Erreur": "Données invalides"}), 400

    profil = Profil.query.get(profil_id)

    if profil is None:
        return jsonify({"Erreur": "Profil non trouvé"}), 404

    profil.name = data['name']
    profil.description = data['description']

    db.session.commit()

    return jsonify({"message": "Profil mis à jour avec succès", "id": profil.id}), 200

@app.route('/profil/delete/<int:profil_id>', methods=['DELETE'])
def delete_profil(profil_id):
    """Supprimer un profil à travers son id"""
    profil = Profil.query.get(profil_id)

    if profil is None:
        return jsonify({"Erreur": "Profil non trouvé"}), 404

    db.session.delete(profil)
    db.session.commit()

    return jsonify({"message": "Profil supprimé avec succès"}), 200


@app.route('/association')
def get_association():
    """Afficher les informations d'une association"""
    associations = Association.query.all()

    associations_data = [
        {
            "id": association.id,
            "nom": association.nom,
            "ville": association.ville,
            "addressse": association.addresse,
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


@app.route('/addProfil', methods=['GET', 'POST'])
def add_profil():
    """Ajouter un profil"""
    if request.method == 'POST':
        data = request.get_json()

        if not data or 'name' not in data or 'description' not in data:
            return jsonify({"Erreur": "Données invalides"}), 400
        
        name = data['name']
        description = data['description']

        profil = Profil(
            name=name,
            description=description
        )

        db.session.add(profil)
        db.session.commit()

        return jsonify({"message": "Profil ajouté avec succès", "id": profil.id}), 201
    else:
        return jsonify({"Erreur": "Méthode non autorisée"}), 405
    
@app.route('/addassociation', methods=['POST'])
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

    association = Association(nom=nom, ville=ville, profil_id=profil_id)

    db.session.add(association)
    db.session.commit()

    return jsonify({
        "message": "Association créée",
        "id": association.id
    }), 201

