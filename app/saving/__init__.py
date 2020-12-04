from flask import Blueprint

bp = Blueprint('saving', __name__)

from app.saving import saving_routes