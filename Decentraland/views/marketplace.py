from flask import Blueprint , render_template,url_for
from Decentraland import db
from datetime import datetime
from werkzeug.utils import redirect

bp = Blueprint('marketplace', __name__, url_prefix='/')

@bp.route('/marketplace')
def market():
    return redirect("https://market.decentraland.org/")
