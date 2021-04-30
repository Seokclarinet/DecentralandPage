from flask import Blueprint , render_template,url_for
from Decentraland import db
from datetime import datetime
from werkzeug.utils import redirect

bp = Blueprint('pricetrend', __name__, url_prefix='/')

@bp.route('/pricetrend')
def trend():
    return render_template('trend.html')