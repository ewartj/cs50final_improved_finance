from flask import Blueprint

bp = Blueprint('stat', __name__)

from app.stat import stat_routes