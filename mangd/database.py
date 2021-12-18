# initialize user table using oop
from mangd import db
from flask import current_app
# todo related import
from datetime import datetime

# user token generator:
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer


class user(db.Model):
    # an ID that is automatically assigns to each user
    _id = db.Column("id", db.Integer, primary_key=True)
    # a user name: all usernames have a max of 20 characters
    username = db.Column(db.String(20), unique=True)
    # a password: all passwords have a max of 20
    password = db.Column(db.String(20), nullable=False)
    # user's email:
    email = db.Column(db.String, nullable=False, unique=True)

    # token generator for user to reset password or email
    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config["SECRET_KEY"], expires_sec)
        return s.dumps({"user_id": self._id}).decode("utf-8")

    # check user token
    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config["SECRET_KEY"])
        try:
            user_id = s.loads(token)["user_id"]
        except:
            return None
        return user.query.get(user_id)

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    def __repr__(self):
        return f"ID:{self.id}, username: {self.username}."


class todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    google_id = db.Column(db.Integer)
    title = db.Column(db.String(100), nullable=False)
    stat = db.Column(db.Boolean)
    creation = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    deadline = db.Column(db.DateTime)
    user = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def __init__(self, title, stat, deadline, user, google_id):
        self.title = title
        self.stat = stat
        self.deadline = deadline
        self.user = user
        self.google_id = google_id

db.create_all()