"""
/api/login
/api/register
/api/users          // returns all users, should search be implemented here?
/api/users/{id}
/api/spots           // all but less data, only long-lat
/api/spots/{id}      // all data from specific spot
/api/review
/api/follow/{id}
/api/get_foxy_image

"""

# ============ LOOK AT DB2 IF YOU FORGET WHERE YOU WERE ======= #

import re
from flask.json import JSONEncoder
from db import InternalServerError, NotAuthorizedError, NotFoundError
from flask import Flask, jsonify, abort, request
from flask_restful import Api, Resource, reqparse
from flask_sqlalchemy import SQLAlchemy
import flask_praetorian
import flask_cors
import decimal
from db import *
from db2 import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:Postgres@192.168.0.115:5432/postgres"
api = Api(app)
guard = flask_praetorian.Praetorian()
db = SQLAlchemy(app)


db_handler = DBHandler();

class UserModel(db.Model):
    __tablename__ = 'user_table'

    user_id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.Date())
    email = db.Column(db.String())
    username = db.Column(db.String())
    hashed_pw = db.Column(db.String())
    picture_link = db.Column(db.String())

    def __init__(self, user_id, date_created, email, username, hashed_pw):
        self.user_id = user_id
        self.date_created = date_created
        self.email = email
        self.username = username
        self.hashed_pw = hashed_pw

    def __repr__(self) -> str:
        return f"<User {self.user_id}>"

# For fixing JSON errors
class DecimalEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return str(o)
        return super(DecimalEncoder, self).default(o)

app.json_encoder = DecimalEncoder

class LoginApi(Resource):
    def get(self):
        try:
            # validate login.. requires more research
            return jsonify(login())
        except NotFoundError:
            abort(404, description="Resource not found")
        except NotAuthorizedError:
            abort(403, description="Access denied")
        except InternalServerError:
            abort(500, "How did you fuck this up..")


class RegisterApi(Resource):
    def put(self):
        try:
            # put request to add a new user
            return jsonify(some_function())
        except NotFoundError:
            abort(404, description="Resource not found")
        except NotAuthorizedError:
            abort(403, description="Access denied")
        except InternalServerError:
            abort(500, "How did you fuck this up..")


class UsersApi(Resource):
    def get(self):
        try:
            # get request to return list of users, should 'search' be implemented in conjunction with this?
            return jsonify((db_handler.get_all_users()))
        except NotFoundError:
            abort(404, description="Resource not found")
        except NotAuthorizedError:
            abort(403, description="Access denied")
        except InternalServerError:
            abort(500, "How did you fuck this up..")


class UserApi(Resource):
    def get(self, user_id):
        try:
            # get request to get a single user, as user_id is listed as an argument the id of the user is in the URL. is this right?
            return jsonify(db_handler.get_user_by_id(user_id))
        except NotFoundError:
            abort(404, description="Resource not found")
        except NotAuthorizedError:
            abort(403, description="Access denied")
        except InternalServerError:
            abort(500, "How did you fuck this up..")


    def delete(self, user_id):
        try:
            # delete request to remove user. should this be located in 'Register'?
            return jsonify(some_function(user_id))
        except NotFoundError:
            abort(404, description="Resource not found")
        except NotAuthorizedError:
            abort(403, description="Access denied")
        except InternalServerError:
            abort(500, "How did you fuck this up..")

class UserSpotAPI(Resource):
    def get(self, user_id):
        try:
            return jsonify(db_handler.get_all_spots_from_user_id(user_id))
        except NotFoundError:
            abort(404, description="Resource not found")
        except NotAuthorizedError:
            abort(403, description="Access denied")
        except InternalServerError:
            abort(500, "Bruh")

class SpotsAPI(Resource):
    def get(self):
        try:
            return jsonify(db_handler.get_all_spots())
        except NotFoundError:
            abort(404, description="Resource not found")
        except NotAuthorizedError:
            abort(403, description="Access denied")
        except InternalServerError:
            abort(500, "Bruh")

class SpotAPI(Resource):
    def get(self, spot_id):
        try:
            return jsonify(db_handler.get_all_spots_from_spot_id(spot_id))
        except NotFoundError:
            abort(404, description="Resource not found")
        except NotAuthorizedError:
            abort(403, description="Access denied")
        except InternalServerError:
            abort(500, "Bruh")

class TestResource(Resource):
    def post(self):
        return postUser(request)

    def get(self):
        return getUsers()

class TestResource2(Resource):
    def get (self, name):
        return getUser(name)


""" Setup for Api resource routing """
api.add_resource(LoginApi, '/api/login')
api.add_resource(RegisterApi, '/api/register')
api.add_resource(UsersApi, '/api/users')
api.add_resource(UserApi, '/api/users/<user_id>')
api.add_resource(UserSpotAPI, '/api/users/spots/<user_id>')
api.add_resource(SpotsAPI, "/api/spots")
api.add_resource(SpotAPI, "/api/spots/<spot_id>")
api.add_resource(TestResource, "/api/test/")
api.add_resource(TestResource2, "/api/test/<name>")

# api.add_resource(User, '/api/users/<user_id>')


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
