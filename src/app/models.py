from app import db
from sqlalchemy import Column, DateTime

class Profil(db.Model):
    """Définit les profils"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15))
    description = db.Column(db.String(30))


class Association(db.Model):
    """Définir les associations"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15))
    description = db.Column(db.String(30))
    logo = db.Column(db.String(30))
    profil_id = db.Column(db.Integer, db.ForeignKey('profil.id'), nullable=True)


class ProfilManagement(db.Model):
    """donne les droits CRUD DB/site web entre 2 profils. Si pas défini => pas de droits """
    id = db.Column(db.Integer, primary_key=True)
    creation_right = db.Column(db.Boolean, default=False)
    update_right = db.Column(db.Boolean, default=False)
    read_right = db.Column(db.Boolean, default=False)
    delete_right = db.Column(db.Boolean, default=False)
    managed_profil_id = db.Column(db.Integer, db.ForeignKey('profil.id'), nullable=True)
    master_profil_id = db.Column(db.Integer, db.ForeignKey('profil.id'), nullable=True)

class ProfilResourceManagement(db.Model):
    """définit les droits de gestion des profils sur les ressources """
    id = db.Column(db.Integer, primary_key=True)
    creation_right = db.Column(db.Boolean, default=False)
    update_right = db.Column(db.Boolean, default=False)
    read_right = db.Column(db.Boolean, default=False)
    delete_right = db.Column(db.Boolean, default=False)
    profil_id = db.Column(db.Integer, db.ForeignKey('profil.id'), nullable=True)

class User(db.Model):
    """Table utilisateurs"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15))
    password = db.Column(db.String(15))
    date_creation = db.Column(db.DateTime, default=DateTime.utcnow)
    date_expiration = db.Column(db.DateTime, default=DateTime.utcnow)
    profil_id = db.Column(db.Integer, db.ForeignKey('profil.id'), nullable=True)

class ResourceCost(db.Model):
    """"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15))
    description = db.Column(db.String(15))
    time_cost = db.Column(db.Boolean, default=False)
    unit_time_reference = db.Column(db.Integer, default=0)
    unit_cost = db.Column(db.Float, default=0.0)

class ResourceType(db.Model):
    """ définit les types de ressources disponibles (emprunt gratuit/free_loan, service, récup/son/free_in_out) : par défaut livré avec material & tool"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15))
    type = db.Column(db.String(15))

class ResourceCategory(db.Model):
    """ (ex : bois) : définies des catégories utilisées dans l’appli. Récursif, seul l’ID de plus bas niveau est utilisé dans la table resources"""
    id = db.Column(db.Integer, primary_key=True)
    parent_id = db.Column(db.Integer, db.ForeignKey('resource_category.id'), nullable=True)
    name = db.Column(db.String(15))
    description = db.Column(db.String(15))

class Resource(db.Model):
    """Définie une ressource"""
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(15))
    qty_available = db.Column(db.Integer, default=0)
    resources_unit_cost = db.Column(db.Float, default=0.0)
    photo = db.Column(db.String(15))
    warning_nb = db.Column(db.Integer, default=0)
    resource_type_id = db.Column(db.Integer, db.ForeignKey('resource_type.id'), nullable=True)
    resource_category_id = db.Column(db.Integer, db.ForeignKey('resource_category.id'), nullable=True)
    resource_cost_id = db.Column(db.Integer, db.ForeignKey('resource_cost.id'), nullable=True)

class Loan(db.Model):
    """décrit les emprunts"""
    id = db.Column(db.Integer, primary_key=True)
    start_date = db.Column(db.DateTime, default=DateTime.utcnow)
    end_date = db.Column(db.DateTime, default=DateTime.utcnow)
    free = db.Column(db.Boolean, default=False)
    retire = db.Column(db.Boolean, default=False)
    rendu = db.Column(db.Boolean, default=False)
    note = db.Column(db.String(15))
    resource_id = db.Column(db.Integer, db.ForeignKey('resource.id'), nullable=True)

class ShopCart(db.Model):
    """ décrit les paniers en cours (expiration à 24h)"""
    id = db.Column(db.Integer, primary_key=True)
    creation_date = db.Column(db.DateTime, default=DateTime.utcnow)
    last_update_date = db.Column(db.DateTime, default=DateTime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)

class ShopCartDetail(db.Model):
    """décrit les lignes d’un panier """
    id = db.Column(db.Integer, primary_key=True)
    qty = db.Column(db.Integer, default=0)
    creation_date = db.Column(db.DateTime, default=DateTime.utcnow)
    last_update_date = db.Column(db.DateTime, default=DateTime.utcnow)
    shop_cart_id = db.Column(db.Integer, db.ForeignKey('shop_cart.id'), nullable=True)
    resource_id = db.Column(db.Integer, db.ForeignKey('resource.id'), nullable=True)

class i18n(db.Model):
    """table traduction"""
    id = db.Column(db.Integer, primary_key=True)
    en_text = db.Column(db.String(15))
    target = db.Column(db.String(15))
