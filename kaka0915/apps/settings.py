import os

# from secret_keys import CSRF_SECRET_KEY, SESSION_KEY


class Config(object):
    # Set secret keys for CSRF protection
    # SECRET_KEY = CSRF_SECRET_KEY
    # CSRF_SESSION_KEY = SESSION_KEY
    SECRET_KEY = "likelion-flaskr-secret-key"
    debug = False


class Production(Config):
    debug = True
    CSRF_ENABLED = False
    ADMIN = "dbsrud2669@gmail.com"
    SQLALCHEMY_DATABASE_URI = 'mysql+gaerdbms:///kakao?instance=gyeongtest:ysososns'
    migration_directory = 'migrations'