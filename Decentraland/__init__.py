from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
import config


naming_convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}
db = SQLAlchemy(metadata=MetaData(naming_convention=naming_convention))
migrate = Migrate()


app = Flask(__name__)
app.config.from_object(config)
app.debug = True

# DRM 데이터베이스 초기화
db.init_app(app)

migrate.init_app(app,db)

from .views import main_views,Chatbot_views,price_trend,homepage,marketplace,Chathook_views
app.register_blueprint(main_views.bp)
app.register_blueprint(Chatbot_views.bp)
app.register_blueprint(price_trend.bp)
app.register_blueprint(homepage.bp)
app.register_blueprint(marketplace.bp)
app.register_blueprint(Chathook_views.bp)