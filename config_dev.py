from config import *
from config_secret_dev import *
import os

base = os.path.abspath('.')


SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(base, 'packjoy', 'test.db'))
SECRET_KEY = 'secret'
DEBUG = True

# # Flask-Security URLs, overridden because they don't put a / at the end
# SECURITY_LOGIN_URL = "/login/"
# SECURITY_LOGOUT_URL = "/logout/"
# SECURITY_REGISTER_URL = "/register/"

# SECURITY_POST_LOGIN_VIEW = "/admin/"
# SECURITY_POST_LOGOUT_VIEW = "/admin/"
# SECURITY_POST_REGISTER_VIEW = "/admin/"

# # Flask-Security features