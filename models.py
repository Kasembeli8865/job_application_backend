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

    def __repr__(self):
        return f'<Employee {self.id} {self.name} {self.email} {self.skills} {self.experience}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'username': self.username,
            # 'password': self.password,
            'skills': self.skills,
            'experience': self.experience
        }
    
    @validates('name')
    def validate_name(self, key, name):
        if not name:
            raise AssertionError('Name required')  

    @validates('email')
    def validate_email(self, key, email):
        if not Email()(email):
            raise AssertionError('Invalid email')
    
    @validates('username')
    def validate_username(self, key, username):
        if not username:
            raise AssertionError('Username required')
  
    @validates('password')
    def validate_password(self, key, password):
        if not Length(min=8)(password):
            raise AssertionError('Password must be 8 chars')
        
        
class Employer(db.Model):
   
    __tablename__ = 'employers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    username = db.Column(db.String)
    username = db.Column(db.String)
    password = db.column(db.Varchar)
    description = db.Column(db.Text)

    def __init__(self, name, username, description):
        self.name = name
        self.username = username
        self.description = description
    
    def __repr__(self):
        return f'<Employer {self.id} {self.name} {self.description}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'username': self.username,
            # 'password': self.password, 
            'description': self.description
        }
    
    @validates('name')
    def validate_name(self, key, name):
        if not name:
            raise AssertionError('Name required')  

    @validates('email')
    def validate_email(self, key, email):
        if not Email()(email):
            raise AssertionError('Invalid email')
    
    @validates('username')
    def validate_username(self, key, username):
        if not username:
            raise AssertionError('Username required')
  
    @validates('password')
    def validate_password(self, key, password):
        if not Length(min=8)(password):
            raise AssertionError('Password must be 8 chars')