import os

BASE_DIR = os.path.dirname(__file__)

#SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR,'book.db'))
#SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:kp4453kp@localhost:3307/bookbot'
SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://hankyungedudb007:gksrud83783!@my8001.gabiadb.com:3306/hankyung007'
SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = 'dev'