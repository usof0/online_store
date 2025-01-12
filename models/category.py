from db import db

# CREATE TABLE category (
#     category_id SERIAL PRIMARY KEY,
#     category_name VARCHAR(50) NOT NULL,
#     parent_category_id INT REFERENCES Category(category_id) ON DELETE SET NULL
# );

class CategoryModel(db.Model):
    __tablename__ = 'category'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    parent_category_id = db.Column(db.Integer, db.ForeignKey('category.id', ondelete='SET NULL'))

    products = db.relationship(
        'ProductModel', back_populates='category',lazy='dynamic'
    )