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
    
    def __repr__(self):
        return f'<Employer {self.id} {self.name} {self.description}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'username': self.username,
            'description': self.description
        }
    
    class Job(db.Model):
   
        __tablename__ = 'jobs'

        id = db.Column(db.Integer, primary_key=True) 
        title = db.Column(db.String)
        description = db.Column(db.Text)
        salary = db.Column(db.Integer)
        location = db.Column(db.String)
        type = db.Column(db.String)
        image = db.Column(db.String)
        employer_id = db.Column(db.Integer, db.ForeignKey('employers.id'))
        employer = db.relationship('Employer', backref='jobs')

        def __init__(self, title, description, salary, location, type, image, employer):
            self.title = title
            self.description = description
            self.salary = salary
            self.location = location
            self.type = type
            self.image = image
            self.employer = employer
        
        def __repr__(self):
            return f'<Job {self.id} {self.title}>'
    
        def to_dict(self):
            return {
                'id': self.id,
                'title': self.title,
                'description': self.description,
                'salary': self.salary,
                'location': self.location,
                'type': self.type,
                'employer': self.employer
                # 'image': self.image
            }

class Rating(db.Model):
    __tablename__ = 'ratings'

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'))
    employee = relationship('Employee', backref='given_ratings')

    employer_id = db.Column(db.Integer, db.ForeignKey('employers.id'))
    employer = relationship('Employer', backref='received_ratings')

    def __init__(self, rating, date, employee, employer):
        self.rating = rating
        self.date = date
        self.employee = employee
        self.employer = employer

    def __repr__(self):
        return f'<Rating {self.id} {self.rating}>'

    def to_dict(self):
        return {
            'id': self.id,
            'rating': self.rating,
            'date': self.date.strftime('%Y-%m-%d %H:%M:%S') if self.date else None
        }
    
class CompanyProfile(db.Model):
    __tablename__ = 'company_profiles'

    id = db.Column(db.Integer, primary_key=True)
    employer_id = db.Column(db.Integer, db.ForeignKey('employers.id'))
    employer = db.relationship('Employer', backref='company_profile')
    business_industry = db.Column(db.String)
    employee_size = db.Column(db.String)
    base_currency = db.Column(db.String)
    continent = db.Column(db.String)
    country = db.Column(db.String)
    city = db.Column(db.String)
    address = db.Column(db.Text)
    primary_contact_email = db.Column(db.String)
    primary_contact_phone = db.Column(db.String)
        
    
    