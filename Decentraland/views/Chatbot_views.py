from flask import Blueprint , render_template,url_for,request,flash,session,g

from werkzeug.utils import redirect

bp= Blueprint('chatbot',__name__,url_prefix='/')

@bp.route('/chatbot',methods=('GET',))
def chatbot():
    return render_template('chatbot/chatbot.html')