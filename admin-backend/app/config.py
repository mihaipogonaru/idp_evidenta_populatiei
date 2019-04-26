import os

class DBConfig:
    db_credentials_file = os.path.join(os.path.dirname(__file__), 'db_credentials')
    db_server = 'db'
    db_user = open(db_credentials_file, 'r').readline().split(' ')[0].strip()
    db_password = open(db_credentials_file, 'r').readline().split(' ')[1].strip()
    db_port = 3306
    db_name = 'idp'
    db_url = 'mysql://{}:{}@{}:{}/{}'.\
        format(db_user, db_password, db_server, db_port, db_name)
