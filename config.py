from flask import Flask
from flask_login import LoginManager, UserMixin
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__)) 
app.config.from_mapping(
    SECRET_KEY = 'CMPE-Group4',
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db'),
    SQLALCHEMY_TRACK_MODIFICATIONS = False
)
db = SQLAlchemy(app)
login = LoginManager(app)
login.init_app(app)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), nullable = False)
    password = db.Column(db.String(200), nullable = False)
    def __repr__(self):
        return '<User {}>'.format(self.username)
    def delete(self):
        db.session.delete(self)

