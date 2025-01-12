from db import db
from datetime import datetime


# CREATE TABLE user (
#     user_id SERIAL PRIMARY KEY,
#     username VARCHAR(50) NOT NULL,
#     email VARCHAR(100) NOT NULL UNIQUE,
#     password VARCHAR(255) NOT NULL,
#     first_name VARCHAR(50),
#     last_name VARCHAR(50),
#     street_address VARCHAR(255),
#     city VARCHAR(50),
#     state VARCHAR(50),
#     postal_code VARCHAR(20),
#     country VARCHAR(50),
#     phone_number VARCHAR(15),
#     created_at TIMESTAMP DEFAULT NOW()
# );


class UserModel(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    country = db.Column(db.String(50))
    state = db.Column(db.String(50))
    city = db.Column(db.String(50))
    phone_number = db.Column(db.String(15))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
