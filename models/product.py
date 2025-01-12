from db import db
from datetime import datetime

# CREATE TABLE product (
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(100) NOT NULL,
#     description TEXT,
#     price DECIMAL(10, 2) NOT NULL,
#     sku VARCHAR(50) UNIQUE,
#     category_id INT REFERENCES Categories(category_id) ON DELETE SET NULL,
#     brand_id INT REFERENCES Brands(brand_id) ON DELETE SET NULL,
#     stock_quantity INT NOT NULL DEFAULT 0,
#     weight DECIMAL(5, 2),
#     image_url VARCHAR(255),
#     created_at TIMESTAMP DEFAULT NOW()
# );

class ProductModel(db.Model):
    __tablename__ = 'product'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Numeric(10, 2), nullable=False )
    sku = db.Column(db.String(50), unique=True)
    quantity = db.Column(db.Integer, nullable=False, default=0)
    weight = db.Column(db.Numeric(5, 2))
    image_url = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)\

    category_id = db.Column(db.Integer, db.ForeignKey('category.id', ondelete='SET NULL'))
    brand_id = db.Column(db.Integer, db.ForeignKey('brand.id'))

    category = db.relationship('CategoryModel', back_populates='products')
    brand = db.relationship('BrandModel', back_populates='products')
    media = db.relationship(
        'MediaModel', back_populates='product', lazy='dynamic', cascade='all, delete'
    )
