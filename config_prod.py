import os
from config import *

SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
SECRET_KEY = os.environ['SECRET_KEY']
MOLTIN_CLIENT_ID = os.environ['MOLTIN_CLIENT_ID']
MOLTIN_CLIENT_SECRET = os.environ['MOLTIN_CLIENT_SECRET']
DEBUG = False
SECURITY_PASSWORD_HASH = os.environ['SECURITY_PASSWORD_HASH']
SECURITY_PASSWORD_SALT = os.environ['SECURITY_PASSWORD_SALT']
