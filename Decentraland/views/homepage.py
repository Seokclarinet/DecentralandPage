from flask import Blueprint , render_template,url_for
from Decentraland import db
from datetime import datetime
from werkzeug.utils import redirect

bp = Blueprint('homepage', __name__, url_prefix='/')

@bp.route('/homepage')
def home():
    return redirect("https://decentraland.org/")

