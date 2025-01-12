from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from db import db
from models import MediaModel
from schemas import MediaSchema

blp = Blueprint('Media', 'media', description='Operations on media')

@blp.route('/product/<int:product_id>/media')
class Media(MethodView):
    @blp.arguments(MediaSchema)
    @blp.response(200, MediaSchema)
    def post(self, media_data, product_id):
        media_data['product_id'] = product_id
        media = MediaModel(**media_data)
        try:
            db.session.add(media)
            db.session.commit()
        except IntegrityError:
            abort(
                400,
                message='A media exists...'
            )
        except SQLAlchemyError:
            abort(
                500,
                message='An error occurred creating the media...'
            )
        return media
    
    @blp.response(200, MediaSchema(many=True))
    def get(self, product_id):
        return MediaModel.query.filter_by(product_id=product_id).all()
        


@blp.route('/media/<int:media_id>')
class Media(MethodView):
    def delete(self, media_id):
        media = MediaModel.query.get_or_404(media_id)
        db.session.delete(media)
        db.session.commit()
        return {'message': 'media deleted....'}, 200
    
    # need to add update endpoint
    