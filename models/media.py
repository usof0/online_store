from db import db
from datetime import datetime


# CREATE TABLE media (
#     media_id SERIAL PRIMARY KEY,
#     product_id INT REFERENCES Products(product_id) ON DELETE CASCADE,
#     media_url VARCHAR(255) NOT NULL,
#     media_type VARCHAR(50) CHECK (media_type IN ('image', 'video')),
#     alt_text VARCHAR(255),
#     created_at TIMESTAMP DEFAULT NOW()
# );

class MediaModel(db.Model):
    __tablename__ = 'media'

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(250), nullable=False)
    media_type = db.Column(db.String(50))
    alt_text = db.Column(db.String(250), default='Media can not laoded!')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id', ondelete='CASCADE'))

    product = db.relationship('ProductModel', back_populates='media')