from flask import Flask, request
from packjoy.common.logger import file_handler

import pprint
pp = pprint.PrettyPrinter(indent=2)

from flask_migrate import Migrate
migrate = Migrate()


def create_app(config_filename):
	app = Flask(__name__, static_folder=None)
	app.config.from_pyfile(config_filename)
	
	from packjoy.common.models import db
	db.init_app(app)

	if not app.debug:
		app.logger.addHandler(file_handler)

	from packjoy.admin.admin import admin
	admin.init_app(app)

	migrate.init_app(app, db)

	from packjoy.common.models import user_datastore, security
	security.init_app(app, datastore=user_datastore)

	from packjoy.mail import mail
	mail.init_app(app)
	
	'''
	Custom templating helper/filter
	it renders the file as plain text
	'''
	with app.app_context():
		from packjoy.common.helpers.utils import get_resource_as_string
		app.jinja_env.globals['get_resource_as_string'] = get_resource_as_string
		register_blueprints(app)

	return app
	

def register_blueprints(app):
	from packjoy.api.routes import api
	from packjoy.site.views import site
	from packjoy.mail import mail_service
	from packjoy.common import common

	app.register_blueprint(api, url_prefix='/api')
	app.register_blueprint(site)
	app.register_blueprint(mail_service, url_prefix='/mail')
	app.register_blueprint(common)
