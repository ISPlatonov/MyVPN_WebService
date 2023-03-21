from flask_login import UserMixin
from app import db
from datetime import datetime, timedelta


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    lastname = db.Column(db.String(1000))
    # date until the user has paid
    date_until_paid = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
