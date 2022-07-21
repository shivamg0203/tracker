from flask import request
from flask_restful import Resource, Api, reqparse
from database import User, db

api = Api()

parser = reqparse.RequestParser()
parser.add_argument('username', type = str)
parser.add_argument('email', type = str)
parser.add_argument('course', type = str)
parser.add_argument('institute', type = str)
parser.add_argument('about', type = str)

class Userinfo(Resource):
	def get(self,name):
		curruser = User.query.filter_by(username = name).first()
		return {'username':curruser.username,
				'email':curruser.email,
				'course':curruser.course,
				'institute':curruser.institute,
				'about':curruser.about}, 200

	def post(self):
		args = parser.parse_args()
		username = args['username']
		email = args['email']
		course = args['course']
		institute = args['institute']
		about = args['about']
		new_user = User(username = username, email = email, course = course, institute = institute, about = about)
		db.session.add(new_user)
		db.session.commit()
		return {'message':'added successfully'}, 200


api.add_resource(Userinfo, '/api/user/<string:name>', '/api/user')

