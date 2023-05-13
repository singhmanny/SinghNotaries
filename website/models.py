#Author: Blanche Chung
#Created Date: Spring 2023
#Description: This file is the models file for the website package. It contains the tables for the database.

from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from website import db
from datetime import datetime

# Create User class
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fname = db.Column(db.String(150))
    lname = db.Column(db.String(150))
    email = db.Column(db.String(150), unique=True)
    address = db.Column(db.String(150), nullable=False)
    address2 = db.Column(db.String(150), nullable=False)
    city = db.Column(db.String(150), nullable=False)
    st = db.Column(db.String(150), nullable=False)
    zipcode = db.Column(db.String(150), nullable=False)
    phone = db.Column(db.String(150), nullable=False)
    doctype = db.Column(db.String(150), nullable=False)
    documents = db.relationship('Document', backref='user', lazy=True)
#    images = db.relationship('ImageTable', backref='user', lazy=True)
#    notary_id = db.Column(db.Integer, db.ForeignKey('notary.id'))


    def validate(self):
        if len(self.fname) < 2:
            raise ValueError("First name must be at least 2 characters long.")
        if len(self.lname) < 2:
            raise ValueError("Last name must be at least 2 characters long.")
        if not self.email:
            raise ValueError("Email is required.")
        if len(self.doctype) < 2:
            raise ValueError("Document type must be at least 2 characters long.")
        if not self.data:
            raise ValueError("File is required.")
#    notary_id = db.Column(db.Integer, db.ForeignKey('notary.id'))

class Document(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    filename = db.Column(db.String(150), nullable=False)
    data = db.Column(db.LargeBinary, nullable=False)

    def __repr__(self):
        return f"<Document {self.id}>"

class ImageTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    image_name = db.Column(db.String(200), nullable=False)
    image_data = db.Column(db.LargeBinary, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Image {self.id}>"
    
# Create Notary class
# class Notary(db.Model):
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     first_name = db.Column(db.String(150))
#     last_name = db.Column(db.String(150))
#     address = db.Column(db.String(150))
#     address2 = db.Column(db.String(150))
#     city = db.Column(db.String(150))
#     state = db.Column(db.String(150))
#     zip_code = db.Column(db.String(150))
#     email = db.Column(db.String(150), unique=True)
#     password = db.Column(db.String(150))
#     cert_no = db.Column(db.String(150))
#     notary_documents = db.relationship('NotaryDocument')
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

