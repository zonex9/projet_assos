import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    API_VERSION = "0.1.1"
    SECRET_KEY = 'do-or-do-not-there-is-no-try'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'associations.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False