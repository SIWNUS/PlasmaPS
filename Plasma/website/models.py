from . import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150),  nullable=False)
    blood_group = db.Column(db.Text, nullable=False) 
    age = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<User {}>'.format(self.project_name)

class Plasma(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    email = db.Column(db.String(150), nullable=False)
    reg_no = db.Column(db.Integer, nullable=False)
    blood_group = db.Column(db.Text, nullable=False) 
    date_details = db.Column(db.String, nullable=False)
    address = db.Column(db.TEXT(200), nullable=False)
    details = db.Column(db.TEXT(4000), nullable=False)

    def __repr__(self):
        return '<Plasma {}>'.format(self.project_name)
