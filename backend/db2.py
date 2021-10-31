from datetime import datetime
from flask.json import jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func


db = SQLAlchemy()

class UserModel(db.Model):
    __tablename__ = 'user_table'

    user_id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime(), default=func.now())
    email = db.Column(db.String())
    username = db.Column(db.String())
    roles = db.Column(db.Text)
    password = db.Column(db.String())
    picture_link = db.Column(db.String())

    def __repr__(self) -> str:
        return f"<User {self.user_id}>"

    @classmethod
    def lookup(cls, username):
        return cls.query.filter_by(username = username).one_or_none()

    @classmethod
    def identify(cls, id):
        return cls.qurey.get(id)

    @property
    def rolenames(self):
        try:
            return self.roles.split(',')
        except Exception:
            return  []

    @property
    def identity(self):
        return self.user_id

def postUser(request):
    if request.is_json:
            data = request.get_json()
            new_user = UserModel(
                user_id=data['user_id'], 
                date_created=datetime.now(), 
                email=data['email'],
                username=data['username'],
                password=data['password']
                )

            db.session.add(new_user)
            db.session.commit()
            return {"message": f"User {new_user.username} has been created in the database"}

    else:
        return {"error": "you done fucked up"}

def getUsers():
    users = UserModel.query.all()
    res = [
        {
            "user_id" : user.user_id, 
            "date_created" : str(user.date_created), 
            "email" : user.email,
            "username" : user.username,
            "password" : user.password
        } for user in users
    ]
    
    return {"count": len(res), "users": res}

def getUser(name):
    user = UserModel.query.filter_by(username=name).first()
    return {
        "user_id" : user.user_id, 
        "date_created" : str(user.date_created), 
        "email" : user.email,
        "username" : user.username,
        "password" : user.password
    }