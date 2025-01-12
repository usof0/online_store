from db import db

# CREATE TABLE brand (
#     brand_id SERIAL PRIMARY KEY,
#     brand_name VARCHAR(100) NOT NULL UNIQUE,
#     brand_logo_url VARCHAR(255)
# );

class BrandModel(db.Model):
    __tablename__ = 'brand'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    logo_url = db.Column(db.String(250))

    products = db.relationship(
        'ProductModel', back_populates='brand', lazy='dynamic', cascade='all, delete'
    )