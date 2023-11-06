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