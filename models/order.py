from db import db

# -- Create Orders Table
# CREATE TABLE order (
#     order_id SERIAL PRIMARY KEY,
#     user_id INT REFERENCES Users(user_id) ON DELETE CASCADE,
#     total_amount DECIMAL(10, 2) NOT NULL,
#     shipping_address TEXT NOT NULL,
#     payment_method VARCHAR(50) CHECK (payment_method IN ('Credit Card', 'PayPal', 'Other')),
#     order_status VARCHAR(20) CHECK (order_status IN ('Processing', 'Shipped', 'Delivered', 'Cancelled')),
#     created_at TIMESTAMP DEFAULT NOW()
# );

class OrderModel(db.Model):
    __tablename__ = 'order'

    id = db.Column(db.Integer,primary_key=True)
    total_amount = db.Column(cb.Numeric(10, 2), nullable=False)
    shipping_address = db.Column(db.Text)
    payment_method = db.Column(db.String(50))
    order_status = db.Column(db.String(20))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user_id = db.Calumn(db.Integer, db.ForeignKey('user.id', ondelete='SET NULL'))
    user = db.relationship('UserModel', backpopulates='orders')
    items = db.relationship('OrderItemModel', back_populates='order')



# -- Create Reviews Table
# CREATE TABLE review (
#     review_id SERIAL PRIMARY KEY,
#     product_id INT REFERENCES Products(product_id) ON DELETE CASCADE,
#     user_id INT REFERENCES Users(user_id) ON DELETE CASCADE,
#     rating TINYINT CHECK (rating BETWEEN 1 AND 5),
#     comment TEXT,
#     is_approved BOOLEAN DEFAULT FALSE,
#     created_at TIMESTAMP DEFAULT NOW()
# );