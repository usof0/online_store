from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import jwt_required
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from db import db
from models import BrandModel
from schemas import BrandSchema, BrandUpdateSchema

blp = Blueprint('Brand', 'brand', description='Operations on brands')

@blp.route('/brand/<int:brand_id>')
class Brand(MethodView):
    @blp.response(200, BrandSchema)
    def get(self, brand_id):
        brand = BrandModel.query.get_or_404(brand_id)
        return brand

    # @jwt_required()
    def delete(self, brand_id):
        brand = BrandModel.query.get_or_404(brand_id)
        db.session.delete((brand))
        db.session.commit()
        return {'message': 'brand deleted.'}, 200
    
    # @jwt_required()
    @blp.arguments(BrandUpdateSchema)
    @blp.response(200, BrandSchema)
    def put(self, brand_data, brand_id):
        brand = BrandModel.query.get(brand_id)

        if brand:
            brand.name = brand_data['name']
            brand.logo_url = brand_data['logo_url']
        else:
            brand = BrandModel(id=brand_id, **brand_data)
        
        db.session.add(brand)
        db.session.commit()

        return brand


@blp.route('/brand')
class BrandList(MethodView):
    @blp.response(200, BrandSchema(many=True))
    def get(self):
        return BrandModel.query.all()

    # @jwt_required()
    @blp.arguments(BrandSchema)
    @blp.response(200, BrandSchema)
    def post(self, brand_data):
        brand = BrandModel(**brand_data)
        try:
            db.session.add(brand)
            db.session.commit()
        except IntegrityError:
            abort(
                400,
                message='A brand exists......'
            )
        except SQLAlchemyError:
            abort(
                500,
                message='An error occurred creating the brand...'
            )
        return brand