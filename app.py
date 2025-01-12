from flask import Flask, jsonify
from flask_smorest import Api
from flask_jwt_extended import JWTManager

import models

from db import db
from resources.user import blp as UserBlueprint
from resources.product import blp as ProductBlueprint
from resources.brand import blp as BrandBlueprint
from resources.category import blp as CategoryBlueprint
from resources.media import blp as MediaBlueprint

def create_app(db_url=None):
    app = Flask(__name__)
    app.config['API_TITLE'] = 'Online store REST API'
    app.config["API_VERSION"] = '1.0.0'
    app.config['OPENAPI_VERSION'] = '3.0.3'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////data.db'

    db.init_app(app)
    api = Api(app)

    app.config["JWT_SECRET_KEY"] = 'temp_secret_key'
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = 3600
    app.config["JWT_TOKEN_LOCATION"] = ["headers"]
    app.config["JWT_HEADER_NAME"] = "Authorization"
    app.config["JWT_HEADER_TYPE"] = "Bearer"
    app.config["JWT_COOKIE_CSRF_PROTECT"] = True
    app.config["JWT_CSRF_CHECK_FORM"] = True 
    jwt = JWTManager(app)

    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        return (
            jsonify(
                {'message': 'The token has expired.', 'error': 'token_expired'}
            ),
            401,
        )

    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return (
            jsonify(
                {'message': 'Signature verification failed.', 'error': 'invalid_token'}
            ),
            401,
        )
    @jwt.unauthorized_loader
    def expired_token_callback(error):
        return (
            jsonify(
                {
                    'description': 'Request does not contain an access token.',
                    'error': 'authorization_required'
                }
            ),
            401,
        )

    with app.app_context():
        import models
        db.create_all()

    api.register_blueprint(UserBlueprint)
    api.register_blueprint(ProductBlueprint)
    api.register_blueprint(BrandBlueprint)
    api.register_blueprint(CategoryBlueprint)
    api.register_blueprint(MediaBlueprint)

    return app
