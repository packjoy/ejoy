class BaseConfig(object):
	TESTING = False
	WTF_CSRF_ENABLED = False
	SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
	SQLALCHEMY_TRACK_MODIFICATIONS = True
	SECRET_KEY = 'secret'
	MOLTIN_CLIENT_ID = '6lI3pFVOxwB0CNRS5YJboKY7GXPHSgkMxD8QXmb7j3'
	MOLTIN_CLIENT_SECRET = 'PuVZIDGLP9ws0Nph07dRwVR99l2mJf5iqiX8A1fA0b'


class Development(BaseConfig):
	pass

class Production(BaseConfig):
	pass

class Testing(BaseConfig):
	TESTING = True
	SQLALCHEMY_DATABASE_URI = "sqlite://"