TESTING = False
WTF_CSRF_ENABLED = False
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECURITY_REGISTERABLE = True
SECURITY_SEND_REGISTER_EMAIL = False

# MAIL SERVER CONFIGS
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
# MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = 'ejoy.noreply@gmail.com'
MAIL_PASSWORD = 'noreply-email-password'
# MAIL_DEFAULT_SENDER = None

# ADMIN STUFF
ADMIN_ADDRESSES = ['ejoy.main@gmail.com', 'szeka1994@gmail.com', 
				'dragosimbrea@yahoo.it', 'konatkalman@gmail.com']
# SERVER_NAME = 'https://packjoy.herokuapp.com'