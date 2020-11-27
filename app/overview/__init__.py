from flask import Blueprint

bp = Blueprint('overview', __name__)

from app.overview import overviewRoutes