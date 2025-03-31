from flask import render_template, request, redirect
from app import app, db
from app.models import Profil
from flask import jsonify


@app.route('/')
@app.route('/index')
def profils():
    profils = Profil.query.all()
    profils_data = [{"id": profil.id, "name": profil.name, "description": profil.description} for profil in profils]
    return jsonify(profils_data)

@app.route('/addProfil', methods=['GET', 'POST'])
def add_profil():

    data = request.get_json()
    
    if not data or 'name' not in data or 'description' not in data:
        return jsonify({"error": "Données invalides"}), 400

    profil = Profil(name=data['name'], description=data['description'])
 
    db.session.add(profil)
    db.session.commit()

    return jsonify({"message": "Profil ajouté avec succès", "id": profil.id}), 201

@app.route('/profil/details/<int:profil_id>', methods=['GET'])
def get_profil(profil_id):
    profil = Profil.query.get(profil_id)
    
    if not profil:
        return jsonify({"error": "Profil not found"}), 404
    
    profil_data = {
        "id": profil.id,
        "name": profil.name,
        "description": profil.description,
    }
  
    return jsonify(profil_data), 200

