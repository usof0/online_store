from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from db import db

from models import ProductModel
from schemas import ProductSchema, ProductUpdateSchema
# from schemas ............

blp = Blueprint('Product', 'product', description='operations on product')


@blp.route('/product/<int:product_id>')
class Product(MethodView):
    @blp.response(200, ProductSchema)
    def get(self, product_id):
        product = ProductModel.query.get_or_404(product_id)
        return product

    def delete(self, product_id):
        product = ProductModel.query.get_or_404(product_id)
        db.session.delete(product)
        db.session.commit()
        return {'message': 'Product deleted.'}

    @blp.arguments(ProductUpdateSchema)
    @blp.response(200, ProductSchema)
    def put(self, product_data, product_id):
        product = ProductModel.query.get(product_id)

        if product:
            product.name = product_data['name']
            product.description = product_data['description']
            product.price = product_data['price']
            product.sku = product_data['sku']
            product.category_id = product_data['category_id']
            product.brand_id = product_data['brand_id']
            product.quantity = product_data['quantity']
            product.weight = product_data['weight']
            product.image_url = product_data['image_url']

        else:
            product = ProductModel(id=product_id, **product_data)
        
        db.session.add(product)
        db.session.commit()

        return product

# item list route.........


@blp.route('/product')
class ProductList(MethodView):
    @blp.response(200, ProductSchema(many=True))
    def get(self):
        return ProductModel.query.all()
    
    @blp.arguments(ProductSchema)
    @blp.response(200, ProductSchema)
    def post(self, product_data):
        product = ProductModel(**product_data)
        try:
            db.session.add(product)
            db.session.commit()
        except IntegrityError:
            abort(
                400,
                message='A product exists.......'
            )
        except SQLAlchemyError:
            abort(
                500,
                message='An error occurred creating the product...'
            )
        return product
