from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
ma = Marshmallow()
migrate = Migrate(app, db)

from app import routes, models
# from flask import Flask, current_app
# from flask_sqlalchemy import SQLAlchemy
# from config import Config
# from flask_marshmallow import Marshmallow

# db = SQLAlchemy()
# ma = Marshmallow()

# def create_app(config_class=Config):
#     app = Flask(__name__)
#     app.config.from_object(config_class)
#     db.init_app(app)
#     ma.init_app(app)

#     from app.access import bp as access_bp
#     app.register_blueprint(access_bp)

#     from app.buy import bp as buy_bp
#     app.register_blueprint(buy_bp)

#     from app.overview import bp as overview_bp
#     app.register_blueprint(overview_bp)

#     from app.sell import bp as sell_bp
#     app.register_blueprint(sell_bp) 

#     from app.errors import bp as errors_bp
#     app.register_blueprint(errors_bp)

#     return app
