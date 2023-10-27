from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime

db = SQLAlchemy()

class Employee(db.Model):
    __tablename__ = 'employees'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    user_name = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(80), nullable=False)
    skills = db.Column(db.String(300))
    experience = db.Column(db.Integer)

    def __init__(self, name, email, user_name, password, skills, experience):
        self.name = name
        self.email = email
        self.user_name = user_name
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
            'user_name': self.user_name,
            'skills': self.skills,
            'experience': self.experience
        }
    
    @validates('name')
    def validate_name(self, key, name):
        if not name:
            raise AssertionError('Name required')
        return name

    @validates('email')
    def validate_email(self, key, email):
        if not email:
            raise AssertionError('Email required')
        return email

<<<<<<< HEAD
    @validates('username')
    def validate_user_name(self, key, user_name):
=======
    @validates('user_name')
    def validate_username(self, key, user_name):
>>>>>>> development
        if not user_name:
            raise AssertionError('Username required')
        return user_name

    @validates('password')
    def validate_password(self, key, password):
        if not password:
            raise AssertionError('Password required')
        return password


class Employer(db.Model):
    __tablename__ = 'employers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    user_name = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    description = db.Column(db.Text)

    def __init__(self, name, user_name, password, description):
        self.name = name
        self.user_name = user_name
        self.password = password
        self.description = description

    def __repr__(self):
        return f'<Employer {self.id} {self.name} {self.description}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'user_name': self.user_name,
            'description': self.description
        }
    
    @validates('name')
    def validate_name(self, key, name):
        if not name:
            raise AssertionError('Name required')
        return name

<<<<<<< HEAD
    @validates('username')
=======
    @validates('user_name')
>>>>>>> development
    def validate_user_name(self, key, user_name):
        if not user_name:
            raise AssertionError('Username required')
        return user_name

    @validates('password')
    def validate_password(self, key, password):
        if not password:
            raise AssertionError('Password required')
        return password


class Job(db.Model):
    __tablename__ = 'jobs'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.Text)
    salary = db.Column(db.Integer)
    location = db.Column(db.String)
    type = db.Column(db.String)
    image = db.Column(db.String)

    def __init__(self, title, description, salary, location, type, image):
        self.title = title
        self.description = description
        self.salary = salary
        self.location = location
        self.type = type
        self.image = image

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
            'image': self.image
        }


class Rating(db.Model):
    __tablename__ = 'ratings'

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, rating, date=None):
        self.rating = rating
        if date:
            self.date = date

    def __repr__(self):
        return f'<Rating {self.id} {self.rating}>'

    def to_dict(self):
        return {
            'id': self.id,
            'rating': self.rating,
            'date': self.date.strftime('%Y-%m-%d %H:%M:%S') if self.date else None
        }
