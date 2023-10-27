from flask import Flask, jsonify, request, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource
from models import *
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
# postgresql://povertyline1_user:YjDL4FXatowosyshHEXWL9way79WVy24@dpg-cl19hpas1bgc73eirco0-a.oregon-postgres.render.com/povertyline1
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your-secret-key' 
app.config['JWT_ALGORITHM'] = 'HS256'

CORS(app)

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

class EmployerByID(Resource):
    def get(self, id):
        employer = Employer.query.get(int(id))
        if employer is not None:
            response_dict = employer.to_dict()
            response = make_response(
                jsonify(response_dict),
                200,
            )
        else:
            response_dict = {'message': 'Employer not found'}
            response = make_response(
                jsonify(response_dict),
                404,
            )
        return response
     
    def patch(self,id):
        employer = Employer.query.get(int(id))
        for attr in request.json:
            setattr(employer, attr, request.json[attr])
        db.session.add(employer)
        db.session.commit()

        response_dict = employer.to_dict()

        response = make_response(
            jsonify(response_dict),
            200,
        )
        return response
api.add_resource(EmployerByID, '/employers/<int:id>')  

################### JOBS ################
class JobResource(Resource):
    def get(self):
        response_dict_list = [n.to_dict() for n in Job.query.all()]

        response = make_response(
            jsonify(response_dict_list),
            200,
        )

        return response
    
    def post(self):
        data = request.get_json()
  
        new_job = Job(
            title=data['title'],
            description=data['description'],
            location=data['location'],
            type=data['type']
        )

        db.session.add(new_job)
        db.session.commit()

        response_dict = new_job.to_dict()

        response = make_response(
            jsonify(response_dict),
            201,
        )

        return response
   
api.add_resource(JobResource, '/jobs')   

class JobByID(Resource):
    def get(self, id):

        job = Job.query.get(id)
  
        response_dict = job.to_dict()

        return make_response(jsonify(response_dict), 200)
    def patch(self,id):
        job = Job.query.get(int(id))
        for attr in request.json:
            setattr(job, attr, request.json[attr])
        db.session.add(job)
        db.session.commit()

        response_dict = job.to_dict()

        response = make_response(
            jsonify(response_dict),
            200,
        )
        return response
    
    def delete(self, id):
        job = Job.query.get(int(id))
        db.session.delete(job)
        db.session.commit()

        response_dict = {
            'message':'job succesfully deleted'
        }

        reponse = make_response(
            jsonify(response_dict),
            200,
        )

        return reponse
api.add_resource(JobByID, '/jobs/<int:id>')  

################### RATINGS ################
class RatingResource(Resource):
    def get(self):
        response_dict_list = [n.to_dict() for n in Rating.query.all()]

        response = make_response(
            jsonify(response_dict_list),
            200,
        )

        return response
    
    def post(self):
        data = request.get_json()

        new_rating = Rating(
            rating=data['rating']
           
        )

        db.session.add(new_rating)
        db.session.commit()

        response_dict = new_rating.to_dict()

        response = make_response(
            jsonify(response_dict),
            201,
        )

        return response
   
api.add_resource(RatingResource, '/ratings')  

class RatingByID(Resource):
    def get(self, id):
        rating = Rating.query.get(id)
  
        response_dict = rating.to_dict()

        return make_response(jsonify(response_dict), 200)

    def patch(self,id):
        rating = Rating.query.get(int(id))
        for attr in request.json:
            setattr(rating, attr, request.json[attr])
        db.session.add(rating)
        db.session.commit()

        response_dict = rating.to_dict()

        response = make_response(
            jsonify(response_dict),
            200,
        )
        return response
    
    def delete(self, id):
        rating = Rating.query.get(int(id))
        db.session.delete(rating)
        db.session.commit()

        response_dict = {
            'message':'rating succesfully deleted'
        }

        reponse = make_response(
            jsonify(response_dict),
            200,
        )

        return reponse
api.add_resource(RatingByID, '/ratings/<int:id>')  

if __name__ == '__main__':
    app.run()
