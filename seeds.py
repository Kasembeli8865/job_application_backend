from app import app, db, Employee, Employer, Job, Rating, CompanyProfile, EmployeeApplication
from datetime import datetime
from faker import Faker
import json  # Import the json module
from random import randint  # Import the randint function from the random module

# Create the Flask app
app = app

# Create an application context
with app.app_context():
    # Create a Faker instance to generate fake data
    fake = Faker()

    # Create sample employees
    for _ in range(2):
        employee = Employee(
            email=fake.email(),
            user_name=fake.user_name(),
            password=fake.password(),
            name=fake.name(),
            skills=fake.words(nb=5),
            experience=fake.random_int(min=0, max=10),
        )
        db.session.add(employee)

    # Create sample employers
    for _ in range(2):
        employer = Employer(
            email=fake.email(),
            user_name=fake.user_name(),
            password=fake.password(),
            name=fake.company(),
            description=fake.text(max_nb_chars=200),
        )
        db.session.add(employer)

    # Create sample jobs
    for _ in range(2):
        job = Job(
            title=fake.job(),
            description=fake.text(max_nb_chars=300),
            salary=fake.random_int(min=30000, max=100000),
            location=fake.city(),
            type=fake.random_element(elements=("Full-time", "Part-time")),
            image="job_image.jpg",
            employer=fake.random_element(elements=Employer.query.all()),
        )
        db.session.add(job)

    # Create sample ratings
    # Create sample employees
# Create sample employees
    for _ in range(2):
 
        employee = Employee(
            name=fake.name(),
            email=fake.email(),
            user_name=fake.user_name(),  # Change to user_name
            password=fake.password(),
            skills=json.dumps(fake.words(nb=randint(1, 5))),
            experience=randint(0, 10)
        )
        db.session.add(employee)




    # Create sample company profiles
    for employer in Employer.query.all():
        company_profile = CompanyProfile(
            employer=employer,
            business_industry=fake.bs(),
            employee_size=fake.random_element(elements=("Small", "Medium", "Large")),
            base_currency=fake.random_element(elements=("USD", "EUR", "GBP")),
            continent=fake.random_element(elements=("North America", "Europe", "Asia")),
            country=fake.country(),
            city=fake.city(),
            address=fake.address(),
            primary_contact_email=fake.company_email(),
            primary_contact_phone=fake.phone_number(),
        )
        db.session.add(company_profile)

    # Create sample employee applications
    for job in Job.query.all():
        employee = fake.random_element(elements=Employee.query.all())
        employee_application = EmployeeApplication(
            job=job,
            employee=employee,
            name=fake.name(),
            date_of_birth=fake.date_of_birth(),
            nationality=fake.country(),
            city=fake.city(),
            email=fake.email(),
            mobile=fake.phone_number(),
            role=fake.job(),
            work_duration=fake.random_element(elements=("1 year", "2 years", "3 years")),
            work_location=fake.city(),
            work_description=fake.text(max_nb_chars=300),
            school=fake.company(),
            major=fake.random_element(elements=("Computer Science", "Engineering", "Business")),
            year_completed=fake.random_int(min=2000, max=2022),
        )
        db.session.add(employee_application)

    # Commit changes to the database
    db.session.commit()

app.app_context().push()
