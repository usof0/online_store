from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from passlib.hash import pbkdf2_sha256
from flask_jwt_extended import create_access_token

from db import db
from models import UserModel
from schemas import UserSchema, LoginSchema

blp = Blueprint('User', 'user', description='Operations on users.')

@blp.route('/register')
class UserRegister(MethodView):
    @blp.arguments(UserSchema)
    def post(self, user_data):
        if UserModel.query.filter(UserModel.username == user_data['username']).first():
            abort(409, messate='User already exists...')
        user_data['password'] = pbkdf2_sha256.hash(user_data['password'])
        user = UserModel(**user_data)
        try:
            db.session.add(user)
            db.session.commit()
        except IntegrityError:
            abort(
                400,
                message='A user exists......'
            )
        except SQLAlchemyError:
            abort(
                500,
                message='An error occurred creating the user...'
            )
        return {'message': 'User created successfully...'}, 201

@blp.route('/login')
class UserLogin(MethodView):
    @blp.arguments(LoginSchema)
    def post(self, user_data):
        user = UserModel.query.filter(
            UserModel.username == user_data['username']
        ).first()

        if user and pbkdf2_sha256.verify(user_data['password'], user.password):
            access_toden = create_access_token(identity=user.id, fresh=True)
            return {'access_toden': access_toden}

        abort(401, messate='Invalid credentials...')

@blp.route('/user/<int:user_id>')
class User(MethodView):
    @blp.response(200, UserSchema)
    def get(self, user_id):
        user = UserModel.query.get_or_404(user_id)
        return user

    def delete(self, user_id):
        user = UserModel.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return {'message': 'User deleted...'}, 200