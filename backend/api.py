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
from flask import Flask, jsonify, abort
from flask_restful import Api, Resource

from backend.db import NotFoundError, NotAuthorizedError, InternalServerError, login, some_function

app = Flask(__name__)
api = Api(app)


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
            return jsonify(some_function())
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
            return jsonify(some_function(user_id))
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


""" Setup for Api resource routing """
api.add_resource(LoginApi, '/api/login')
api.add_resource(RegisterApi, '/api/register')
api.add_resource(UsersApi, '/api/users')
api.add_resource(UserApi, '/api/users/<user_id>')
# api.add_resource(User, '/api/users/<user_id>')


if __name__ == '__main__':
    app.run(debug=True)
