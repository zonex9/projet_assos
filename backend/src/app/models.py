from backend.src.app.extensions import db
from sqlalchemy import Column, DateTime
from datetime import datetime

class Profil(db.Model):
    """Définit les profils"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15), index=True)
    description = db.Column(db.String(30))


class Association(db.Model):
    """Définir les associations"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15), index=True)
    ville = db.Column(db.String(30))
    addresse = db.Column(db.String(50))
    description = db.Column(db.String(30))
    mail = db.Column(db.String(30))
    logo = db.Column(db.String(30))
    # Clé étrangère vers Profil
    profil_id = db.Column(db.Integer, db.ForeignKey('profil.id'))

    # Relationship vers Profil
    profil = db.relationship('Profil', backref='associations', lazy=True)


class Resource(db.Model):
    """Définie une ressource"""
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(15))
    qty_available = db.Column(db.Integer, default=0)
    resources_unit_cost = db.Column(db.Float, default=0.0)
    photo = db.Column(db.String(15))
    warning_nb = db.Column(db.Integer, default=0)
    creation_date = db.Column(db.DateTime, default=datetime.utcnow)
 
    # Clés étrangères
    profil_id = db.Column(db.Integer, db.ForeignKey('profil.id'), nullable=True, index=True)
    association_id = db.Column(db.Integer, db.ForeignKey('association.id'), nullable=True, index=True)

    # Relations pour accéder aux objets liés
    profil = db.relationship('Profil', backref='resources', lazy=True)
    association = db.relationship('Association', backref='resources', lazy=True)
    
class ShopCart(db.Model):
    """ décrit les paniers en cours (expiration à 24h)"""
    id = db.Column(db.Integer, primary_key=True)
    creation_date = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    last_update_date = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    
    # Clés étrangères
    profil_id = db.Column(db.Integer, db.ForeignKey('profil.id'), nullable=True, index=True)
    
    # Relations pour accéder aux objets liés
    profil = db.relationship('Profil', backref='shopcarts', lazy=True)
    


class ShopCartDetail(db.Model):
    """décrit les lignes d’un panier """
    id = db.Column(db.Integer, primary_key=True)
    qty = db.Column(db.Integer, default=0)
    creation_date = db.Column(db.DateTime, default=datetime.utcnow)
    last_update_date = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Clés étrangères
    shop_cart_id = db.Column(db.Integer, db.ForeignKey('shop_cart.id'), nullable=True, index=True)
    resource_id = db.Column(db.Integer, db.ForeignKey('resource.id'), nullable=True, index=True)
    profil_id = db.Column(db.Integer, db.ForeignKey('profil.id'), nullable=True, index=True)

     # Relations pour accéder aux objets liés
    shopcart = db.relationship('ShopCart', backref='shopcartdetails', lazy=True)
    resource = db.relationship('Resource', backref='shopcartdetails', lazy=True)
    profil = db.relationship('Profil', backref='shopcartdetails', lazy=True)
    
class Loan(db.Model):
    """décrit les emprunts"""
    id = db.Column(db.Integer, primary_key=True)
    start_date = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    end_date = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    free = db.Column(db.Boolean, default=False, index=True)
    retire = db.Column(db.Boolean, default=False, index=True)
    rendu = db.Column(db.Boolean, default=False, index=True)
    note = db.Column(db.String(15))
    
    # Clés étrangères
    profil_id = db.Column(db.Integer, db.ForeignKey('profil.id'), nullable=True, index=True)
    resource_id = db.Column(db.Integer, db.ForeignKey('resource.id'), nullable=True, index=True)
    
    # Relations pour accéder aux objets liés
    profil = db.relationship('Profil', backref='loans', lazy=True)
    resource = db.relationship('Resource', backref='loans', lazy=True)
    
# class ProfilManagement(db.Model):
#     """donne les droits CRUD DB/site web entre 2 profils. Si pas défini => pas de droits """
#     id = db.Column(db.Integer, primary_key=True)
#     creation_right = db.Column(db.Boolean, default=False, index=True)
#     update_right = db.Column(db.Boolean, default=False, index=True)
#     read_right = db.Column(db.Boolean, default=False, index=True)
#     delete_right = db.Column(db.Boolean, default=False, index=True)
#     managed_profil_id = db.Column(db.Integer, db.ForeignKey('profil.id'), nullable=True, index=True)
#     master_profil_id = db.Column(db.Integer, db.ForeignKey('profil.id'), nullable=True, index=True)

# class ProfilResourceManagement(db.Model):
#     """définit les droits de gestion des profils sur les ressources """
#     id = db.Column(db.Integer, primary_key=True)
#     creation_right = db.Column(db.Boolean, default=False, index=True)
#     update_right = db.Column(db.Boolean, default=False, index=True)
#     read_right = db.Column(db.Boolean, default=False, index=True)
#     delete_right = db.Column(db.Boolean, default=False, index=True)
#     profil_id = db.Column(db.Integer, db.ForeignKey('profil.id'), nullable=True, index=True)

# class User(db.Model):
#     """Table utilisateurs"""
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(15), index=True)
#     password = db.Column(db.String(15))
#     date_creation = db.Column(db.DateTime, default=datetime.utcnow)
#     date_expiration = db.Column(db.DateTime, default=datetime.utcnow)
#     profil_id = db.Column(db.Integer, db.ForeignKey('profil.id'), nullable=True, index=True)

# class ResourceCost(db.Model):
#     """"""
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(15), index = True)
#     description = db.Column(db.String(15))
#     time_cost = db.Column(db.Boolean, default=False, index=True)
#     unit_time_reference = db.Column(db.Integer, default=0)
#     unit_cost = db.Column(db.Float, default=0.0)

# class ResourceType(db.Model):
#     """ définit les types de ressources disponibles (emprunt gratuit/free_loan, service, récup/son/free_in_out) : par défaut livré avec material & tool"""
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(15), index=True)
#     type = db.Column(db.String(15))

# class ResourceCategory(db.Model):
#     """ (ex : bois) : définies des catégories utilisées dans l’appli. Récursif, seul l’ID de plus bas niveau est utilisé dans la table resources"""
#     id = db.Column(db.Integer, primary_key=True)
#     parent_id = db.Column(db.Integer, db.ForeignKey('resource_category.id'), nullable=True)
#     name = db.Column(db.String(15), index=True)
#     description = db.Column(db.String(15))


class i18n(db.Model):
    """table traduction"""
    id = db.Column(db.Integer, primary_key=True)
    en_text = db.Column(db.String(15))
    target = db.Column(db.String(15))
