from flask import Flask, jsonify, request, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource
from models import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your-secret-key' 
app.config['JWT_ALGORITHM'] = 'HS256'

with app.app_context():
  db.init_app(app)
  
migrate = Migrate(app,db)
api = Api(app)

################### EMPLOYEES ################
class EmployeeResource(Resource):

    def get(self):
        response_dict_list = [n.to_dict() for n in Employee.query.all()]
        response = make_response(
            jsonify(response_dict_list), 200)
        
        return response


    
    
    def post(self):
        data = request.get_json()
  
        new_employee = Employee(
            name = data['name'],
            email = data['email'],
            skills = data['skills'],
            experience = data['experience'],
            user_name = data['user_name'],
            password=data['password']
        )

        db.session.add(new_employee)
        db.session.commit()

        response_dict = new_employee.to_dict()

        response = make_response(
            jsonify(response_dict),
            201,
        )

        return response
   
api.add_resource(EmployeeResource, '/employees')  

class EmployeeByID(Resource):
      

    def get(self, id):
        employee = Employee.query.get(int(id))
        if employee is not None:
            response_dict = employee.to_dict()
            response = make_response(
                jsonify(response_dict),
                200,
            )
        else:
            response_dict = {'message': 'Employee not found'}
            response = make_response(
                jsonify(response_dict),
                404,
            )
        return response

     
    def patch(self,id):
        employee = Employee.query.get(int(id))
        for attr in request.json:
            setattr(employee, attr, request.json[attr])
        db.session.add(employee)
        db.session.commit()

        response_dict = employee.to_dict()

        response = make_response(
            jsonify(response_dict),
            200,
        )
        return response
api.add_resource(EmployeeByID, '/employees/<int:id>') 

################### EMPLOYERS ################
class EmployerResource(Resource):
    def get(self):
        response_dict_list = [n.to_dict() for n in Employer.query.all()]

        response = make_response(
            jsonify(response_dict_list),
            200,
        )

        return response
    
    def post(self):
        data = request.get_json()
        new_employer = Employer(
            name=data['name'],
            description=data['description'],
            user_name=data['user_name'], 
            password=data['password']
        )

        db.session.add(new_employer)
        db.session.commit()

        response_dict = new_employer.to_dict()

        response = make_response(
            jsonify(response_dict),
            201,
        )

        return response
   
api.add_resource(EmployerResource, '/employers')   

