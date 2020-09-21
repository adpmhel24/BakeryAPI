from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_caching import Cache
from flask_httpauth import HTTPTokenAuth
from api_app.config import Config

db = SQLAlchemy()
bcrpyt = Bcrypt()
cache = Cache()
login_manager = LoginManager()
auth = HTTPTokenAuth(scheme='Bearer')

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    app.config['JSON_SORT_KEYS'] = False
    app.config['CACHE_TYPE'] = 'simple'

    
    db.init_app(app)
    bcrpyt.init_app(app)
    login_manager.init_app(app)
    cache.init_app(app)

    from api_app.users.routes import users
    from api_app.sap_b1.routes import sap_b1
    from api_app.ab_pos.routes import ab_pos

    app.register_blueprint(users)
    app.register_blueprint(sap_b1)
    app.register_blueprint(ab_pos)

    return app

