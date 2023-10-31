from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from wtforms.validators import Email, Length
db = SQLAlchemy()

class Employee(db.Model):

    __tablename__ = 'employees' 

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    username = db.Column(db.String(80), nullable=False)
    password = db.column(db.String(80), nullable=False)
    skills = db.Column(db.String(300))
    experience = db.Column(db.Integer)

    def __init__(self, name, email,username, password, skills, experience):
        self.name = name
        self.email = email
        self.username = username
        self.password = password
        self.skills = skills
        self.experience = experience