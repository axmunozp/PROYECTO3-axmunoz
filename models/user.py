from flask_login import UserMixin
from db import db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(45), nullable=False)
    password = db.Column(db.String(45), nullable=False)
    #is_admin = db.Column(db.Boolean, nullable=False)
    
    def __init__(self, id, username, password, is_admin):
        self.id = id
        self.username = username
        self.password = password
        #self.is_admin = is_admin

#SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def autenticar_usuario(db_session, username, password):
    usuario = db_session.query(username).filter(Users.username == username, Users.password == password).first()
    return usuario is not None

