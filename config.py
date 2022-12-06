from flask import Flask
from flask_login import LoginManager, UserMixin
from flask_sqlalchemy import SQLAlchemy
import os
from sqlalchemy.sql import func

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config.from_mapping(
    SECRET_KEY = 'CMPE-Group4',
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db'),
    UPLOAD_FOLDER = 'static/css/images/',
    SQLALCHEMY_TRACK_MODIFICATIONS = False
)
db = SQLAlchemy(app)
login = LoginManager(app)
login.init_app(app)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), nullable = False)
    password = db.Column(db.String(200), nullable = False)
    profile_picture = db.Column(db.String(), nullable = True)
    posts = db.relationship('Posts', backref='user', passive_deletes=True)
    comments = db.relationship('Comment', backref='user', passive_deletes=True)
    def __repr__(self):
        return '<User {}>'.format(self.username)
    def delete(self):
        db.session.delete(self)

class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    date_posted = db.Column(db.DateTime(timezone=True), default=func.now())
    content = db.Column(db.Text)
    author = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    comments = db.relationship('Comment', backref='posts', passive_deletes=True)

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_posted = db.Column(db.DateTime(timezone=True), default=func.now())
    content = db.Column(db.String(200), nullable=False)
    author = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id', ondelete='CASCADE'), nullable=False)

