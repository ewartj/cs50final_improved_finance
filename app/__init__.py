# from flask import Flask
# from config import Config
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# from flask_marshmallow import Marshmallow


# app = Flask(__name__)
# app.config.from_object(Config)
# db = SQLAlchemy(app)
# ma = Marshmallow()
# migrate = Migrate(app, db)

# from app import routes, models
from flask import Flask, current_app
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    ma.init_app(app)

    from app.access import bp as access
    app.register_blueprint(access)

    from app.manage import bp as manage
    app.register_blueprint(manage)

    from app.overview import bp as overview
    app.register_blueprint(overview)

    # from app.error import bp as error
    # app.register_blueprint(error)

    return app
