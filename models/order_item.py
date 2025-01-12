from db import db

# -- Create Order Items Table
# CREATE TABLE order_Item (
#     order_item_id SERIAL PRIMARY KEY,
#     order_id INT REFERENCES Orders(order_id) ON DELETE CASCADE,
#     product_id INT REFERENCES Products(product_id) ON DELETE CASCADE,
#     quantity INT NOT NULL,
#     price DECIMAL(10, 2) NOT NULL
# );

class OrderItemModel(db.Model):
    __tablename__ = 'order_item'

    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False, default=1)
    price = db.Column(db.Numeric(10, 2), nullable=False)

    order_id = db.Column(db.Integer, db.ForeignKey('order.id', ondelete='CASCADE'))
    product_id = db.Column(db.Integer, db.ForeignKey('product.id', ondelete='SET NULL'))

    order = db.relationship('OrderModel', back_populates='items')
    product = db.relationship('ProductModel')#, back_populates='orders')