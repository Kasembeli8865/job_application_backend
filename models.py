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
    

    def _hash_password(self, password):
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode('utf-8'), salt)
    
    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password_hash)
    
    @validates('name')
    def validate_name(self, key, name):
        if not name:
            raise AssertionError('Name required')  
        return name

    @validates('email')
    def validate_email(self, key, email):
        if not email or not re.match(r'^[\w\.-]+@[\w\.-]+$', email):
            raise AssertionError('Invalid email')
        return email
    
    @validates('username')
    def validate_username(self, key, username):
        if not username:
            raise AssertionError('Username required')
        return username
  
    @validates('password')
    def validate_password(self, key, password):
        if not (8 <= len(password) <= 80):
            raise AssertionError('Password must be between 8 and 80 characters')
        return password
    
class Employer(db.Model):
   
    __tablename__ = 'employers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    username = db.Column(db.String)
    email = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String)
    password_hash = db.Column(db.String)
    description = db.Column(db.Text)

    def __init__(self, email, username, password, name=None, description=None):
        self.name = name
        self.username = username
        self.email = email
        self.description = description
        self.password = password
        self.password_hash = self._hash_password(password)

    def _hash_password(self, password):
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode('utf-8'), salt)
    
    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password_hash)