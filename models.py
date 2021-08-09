from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from app import db


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow())

    def __repr__(self):
        return '<Name %r>' % self.name
