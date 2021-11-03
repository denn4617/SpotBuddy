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
from db2 import UserModel, getUser, getUsers, postUser
from flasgger import Swagger

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:Postgres@192.168.0.115:5432/postgres"
app.config['SECRET_KEY'] = 'SuperSecretKey'
app.config['JWT_ACCESS_LIFESPAN'] = {'hours': 24}
app.config['JWT_REFRESH_LIFESPAN'] = {'days': 30}

api = Api(app)
guard = flask_praetorian.Praetorian()
guard.init_app(app, UserModel)
db = SQLAlchemy(app)
swagger = Swagger(app)

db_handler = DBHandler();

# For fixing JSON errors
class DecimalEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return str(o)
        return super(DecimalEncoder, self).default(o)

app.json_encoder = DecimalEncoder

with app.app_context():
    db.create_all()
    if db.session.query(UserModel).filter_by(username='Tester').count() < 1:
        db.session.add(UserModel(
            username='Tester',
            email = 'tester@tester.com',
            password=guard.hash_password('Tester'),
            roles='admin'
        ))
        db.session.commit()

class LoginApi(Resource):
    
    def post(self):
        """
        file: api_documentation/login_api_post.yml
        """
        req = request.get_json(force=True)
        username = req.get('username', None)
        password = req.get('password', None)
        user = guard.authenticate(username, password)
        ret = {'access_token': guard.encode_jwt_token(user)}
        return ret,200


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

class RefreshApi(Resource):
    def post(self):
        old_token = request.get_data()
        new_token = guard.refresh_jwt_token(old_token)
        ret = {'access_token': new_token}
        return ret, 200

class RegisterApi(Resource):
    def post(self):
        req = request.get_json()
        username = req.get('username', None)
        password = req.get('password', None)
        email = req.get('email', None)
        db.session.add(UserModel(
            username=username,
            email = email,
            password=guard.hash_password(password),
            roles=''
        ))
        db.session.commit()


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
    @flask_praetorian.auth_required
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


""" Setup for Api resource routing """
api.add_resource(LoginApi, '/api/login')
api.add_resource(RegisterApi, '/api/register')
api.add_resource(UsersApi, '/api/users')
api.add_resource(UserApi, '/api/users/<user_id>')
api.add_resource(UserSpotAPI, '/api/users/spots/<user_id>')
api.add_resource(SpotsAPI, "/api/spots")
api.add_resource(SpotAPI, "/api/spots/<spot_id>")

# api.add_resource(User, '/api/users/<user_id>')


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
