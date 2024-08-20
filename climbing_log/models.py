from climbing_log import db
from flask_login import UserMixin


class Users(UserMixin, db.Model):
    # schema for the Users model
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    email = db.Column(db.String(75), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    sex = db.Column(db.String(1), nullable=False)
    height = db.Column(db.Float)
    weight = db.Column(db.Float)
    sessions = db.relationship(
        'Sessions', backref='users', cascade='all, delete', lazy=True)

    # set up flask-login to use primary key to track if user is logged in
    def get_id(self):
        return str(self.user_id)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return f'User {self.username}'


class Sessions(db.Model):
    # schema for the Sesssions model
    session_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(
        'users.user_id', ondelete='CASCADE'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    location = db.Column(db.String(50), nullable=False)
    length = db.Column(db.Float, nullable=False)
    time = db.Column(db.DateTime, nullable=False)
    climbs = db.relationship('Climb', backref='sessions',
                             cascade='all, delete', lazy=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return f'Session: {self.session_id} from user {self.user_id}'


class Climb(db.Model):
    # schema for the climb model
    climb_id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.Integer, db.ForeignKey(
        'sessions.session_id', ondelete='CASCADE'), nullable=False)
    difficulty = db.Column(db.String(3), nullable=False)
    length = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(50))
    completed = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string

        return f'Climb: {self.climb_id} from session {self.session_id}'
