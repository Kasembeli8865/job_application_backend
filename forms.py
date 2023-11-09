from flask_wtf import FlaskForm 
from wtforms import StringField, TextAreaField, IntegerField, SelectField, DateField

class JobForm(FlaskForm):

  title = StringField('Title')
  description = TextAreaField('Description')
  salary = IntegerField('Salary')
  location = StringField('Location')
  type = SelectField('Type', choices=[('Full-time', 'Full-time'), ('Part-time', 'Part-time')])
  image = StringField('Image')
  employer_id = IntegerField('Employer ID')

class EmployeeApplicationForm(FlaskForm):

  name = StringField('Name')
  date_of_birth = DateField('Date of Birth') 
  nationality = StringField('Nationality')
  city = StringField('City')
  email = StringField('Email')
  mobile = StringField('Mobile')
  role = StringField('Role')
  work_duration = StringField('Work Duration')
  work_location = StringField('Work Location')
  work_description = TextAreaField('Work Description')
  school = StringField('School')
  major = StringField('Major')
  year_completed = IntegerField('Year Completed')