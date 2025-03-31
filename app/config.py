import os
basedir = os.path.abspath(os.path.dirname(__file__))
version = "0.1.0"

class Config(object):
    SECRET_KEY = 'do-or-do-not-there-is-no-try'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'associations.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False