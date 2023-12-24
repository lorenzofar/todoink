from flask import Blueprint
from flask_cors import CORS

bp = Blueprint('api', __name__)
CORS(bp, expose_headers=['Content-Disposition'])

from todoink.api import todoist