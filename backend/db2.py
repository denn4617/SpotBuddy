from flask.json import jsonify
from api import app
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy(app)

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

def postUser(request):
    if request.is_json:
            data = request.get_json()
            new_user = UserModel(
                user_id=data['user_id'], 
                date_created="01-01-2001", 
                email=data['email'],
                username=data['username'],
                hashed_pw=data['hashed_pw']
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
            "hashed_pw" : user.hashed_pw
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
        "hashed_pw" : user.hashed_pw
    }