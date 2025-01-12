from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import jwt_required
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from db import db
from models import CategoryModel, ProductModel
from schemas import CategorySchema

blp = Blueprint('Category', 'category', description='Oerations on categories.')

@blp.route('/category/<int:category_id>')
class Category(MethodView):
    @blp.response(200, CategorySchema)
    def get(self, category_id):
        category = CategoryModel.query.get_or_404(category_id)
        return category

    def delete(self, category_id):
        category = CategoryModel.query.get_or_404(category_id)
        db.session.delete(category)
        db.session.commit()
        return {'message': 'category deleted....'}, 200
    
    # @blp.argumnets(CategoriesUpdateShema)


@blp.route('/category')
class CategoryList(MethodView):
    @blp.response(200, CategorySchema(many=True))
    def get(self):
        return CategoryModel.query.all()

    # @jwt_required()
    @blp.arguments(CategorySchema)
    @blp.response(200, CategorySchema)
    def post(self, category_data):
        category = CategoryModel(**category_data)

        try:
            db.session.add(category)
            db.session.commit()
        except IntegrityError:
            abort(
                400,
                message='A category exists...'
            )
        except SQLAlchemyError:
            abort(
                500,
                message='An error accurred creating the category...'
            )
        return category
