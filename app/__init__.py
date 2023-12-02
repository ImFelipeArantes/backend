from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS


db = SQLAlchemy()
DB_NAME = "database.db"
ma = Marshmallow()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "helloworld"
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
    ma.init_app(app)
    CORS(app)
    from .routes import routes
    
    app.register_blueprint(routes, url_prefix='/')

    with app.app_context():
        db.create_all()
        print('Create Database!!')

    return app