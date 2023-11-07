from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from faker import Faker
from models import Employee, Employer, Job, Rating
from random import randint
from datetime import datetime, timedelta
import json

app = Flask(__name__)

# Update your app.config with your database configuration here
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
fake= Faker()

def create_employees(num_employees):
    for _ in range(num_employees):
        employee = Employee(
            name=fake.name(),
            email=fake.email(),
            user_name=fake.user_name(),  # Change to user_name
            password=fake.password(),
            skills=json.dumps(fake.words(nb=randint(1, 5))),
            experience=randint(0, 10)
        )
        db.session.add(employee)

def create_employers(num_employers):
    for _ in range(num_employers):
        employer = Employer(
            name=fake.company(),
            description=fake.text(),
            user_name=fake.user_name(),  # Use the user_name() method
            password="your_custom_password_logic",  # Replace with your password logic
        )
        db.session.add(employer)
def create_jobs(num_jobs):
    for _ in range(num_jobs):
        job = Job(
            title=fake.job(),
            description=fake.text(),
            location=fake.city(),
            type=fake.random_element(elements=("Full-time", "Part-time", "Contract")),
            salary=fake.random_int(),
            image=fake.url()
        )
        db.session.add(job)

def create_ratings(num_ratings):
    for _ in range(num_ratings):
        rating = Rating(
            rating=randint(1, 5),
            date=fake.date_time_between(start_date="-2y", end_date="now", tzinfo=None)
        )
        db.session.add(rating)
        
if __name__ == "__main__":
    with app.app_context():
        num_employees = 10  # Change as needed
        num_employers = 5   # Change as needed
        num_jobs = 20       # Change as needed
        num_ratings = 15   # Change as needed

        create_employees(num_employees)
        create_employers(num_employers)
        create_jobs(num_jobs)
        create_ratings(num_ratings)

        db.session.commit()