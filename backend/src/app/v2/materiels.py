
from flask import Blueprint, render_template, request, redirect, jsonify
from backend.src.app.extensions import db
from backend.src.app.models import Profil, Association, Resource

bp_materiels= Blueprint("materiels", __name__)

    # id = db.Column(db.Integer, primary_key=True)
    # description = db.Column(db.String(15))
    # qty_available = db.Column(db.Integer, default=0)
    # resources_unit_cost = db.Column(db.Float, default=0.0)
    # photo = db.Column(db.String(15))
    # warning_nb = db.Column(db.Integer, default=0)
    # creation_date = db.Column(db.DateTime, default=datetime.utcnow)
 
    # # Clés étrangères
    # profil_id = db.Column(db.Integer, db.ForeignKey('profil.id'), nullable=True, index=True)
    # association_id = db.Column(db.Integer, db.ForeignKey('association.id'), nullable=True, index=True)

    # # Relations pour accéder aux objets liés
    # profil = db.relationship('Profil', backref='resources', lazy=True)
    # association = db.relationship('Association', backref='resources', lazy=True)
    
@bp_materiels.route('/materiels', methods=['GET'])
def get_materiel():
    """Afficher les informations d'un matériel, chaque matériel est lié à une association
       chaque matériel est lié à un profil, qu'on à déjà crée avant"""
    materiels = Resource.query.all()
    materiels_data = [
        {
            "id": materiel.id,
            "description": materiel.description,
            "qty_available": materiel.qty_available,
            "resources_unit_cost": materiel.resources_unit_cost,
            "photo": materiel.photo,
            "warning_nb": materiel.warning_nb,
            "profil": {
                "id": materiel.profil.id if materiel.profil else None,
                "name": materiel.profil.name if materiel.profil else None,
                "description": materiel.profil.description if materiel.profil else None
            },
            "association": {
                "id": materiel.association.id if materiel.association else None,
                "name": materiel.association.name if materiel.association else None,
                "ville": materiel.association.ville if materiel.association else None,
                "addresse": materiel.association.addresse if materiel.association else None,
                "logo": materiel.association.logo if materiel.association else None,
                "mail": materiel.association.mail if materiel.association else None,

            },    
            
        }
        for materiel in materiels
    ]
    return jsonify(materiels_data)

@bp_materiels.route('/materiels/add', methods=['POST'])
def add_materiel():
    """Ajouter un materiel"""
    data = request.get_json()
    description = data.get('description')
    qty_available = data.get('qty_available')
    resources_unit_cost = data.get('resources_unit_cost')
    photo = data.get('photo')
    warning_nb = data.get('warning_nb')
    creation_date = data.get('creation_date')
    profil_id = data.get('profil_id')
    association_id = data.get('association_id')
    
    if not description or not qty_available or not resources_unit_cost or not photo or not warning_nb or not profil_id or not association_id:
        return jsonify({"Erreur": "Données incomplètes"}), 400

    profil = Profil.query.get(profil_id)
    if not profil:
        return jsonify({"Erreur": "Profil non trouvé"}), 404
    
    association = Association.query.get(association_id)
    if not association:
        return jsonify({"Erreur": "Association non trouvée"}), 404

    materiel = Resource(
        description=description,
        qty_available=qty_available,
        resources_unit_cost=resources_unit_cost,
        photo=photo,
        warning_nb=warning_nb,
        creation_date=creation_date,
        profil_id=profil_id,
        association_id=association_id
    )

    db.session.add(materiel)
    db.session.commit()

    return jsonify({
        "message": "Matériel crée",
        "id": materiel.id
    }), 201
