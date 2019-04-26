import os

class Config:
    SECRET_KEY = "IDP_SUPER_!@#SA$W!@%^%$df12^5#s9d8%09@#SxC%*_SECRET_KEY"
    APP_DIR = os.path.abspath(os.path.dirname(__file__))  # This directory
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    BCRYPT_LOG_ROUNDS = 13
    ASSETS_DEBUG = False

class ServerConfig:
    host = '0.0.0.0'
    port = 8888
    threaded = True

class DBConfig:
    db_credentials_file = os.path.join(os.path.dirname(__file__), 'db_credentials')
    db_server = 'db'
    db_user = open(db_credentials_file, 'r').readline().split(' ')[0].strip()
    db_password = open(db_credentials_file, 'r').readline().split(' ')[1].strip()
    db_port = 3306
    db_name = 'idp'
    db_url = 'mysql://{}:{}@{}:{}/{}'.\
        format(db_user, db_password, db_server, db_port, db_name)
