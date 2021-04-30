from flask import Blueprint , render_template,url_for
from Decentraland import db
from datetime import datetime
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def index():
    return render_template('main.html')