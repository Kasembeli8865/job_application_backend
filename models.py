from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from wtforms import  fields, validators 
from wtforms.validators import Length, Email
from sqlalchemy.orm import relationship
from datetime import datetime
import bcrypt

import re 
db = SQLAlchemy()

class Employee(db.Model):

    __tablename__ = 'employees' 

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80))
    password_hash = db.Column(db.String)
    skills = db.Column(db.String(300))
    experience = db.Column(db.Integer)

    def __init__(self, email, username, password, name=None, skills=None, experience=None):
        self.name = name
        self.email = email
        self.username = username
        self.password = password
        self.password_hash = self._hash_password(password)
        self.skills = skills
        self.experience = experience

    def __repr__(self):
        return f'<Employee {self.id} {self.name} {self.username} {self.email} {self.skills} {self.password} {self.experience}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'username': self.username,
            'email': self.email,
            'skills': self.skills,
            'experience': self.experience,
        }