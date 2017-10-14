from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from moltin.moltin import Moltin
from flask_migrate import Migrate
from packjoy.common.logger import file_handler
from flask_security import Security, SQLAlchemyUserDatastore
import pprint


app = Flask(__name__, static_folder=None)
app.config.from_pyfile('../config_prod.py')
pp = pprint.PrettyPrinter(indent=2)
if not app.debug:
	app.logger.addHandler(file_handler)

# Custom templating helper
# filters, renderers
def get_resource_as_string(name, charset='utf-8'):
    with app.open_resource(name) as f:
        return f.read().decode(charset)

app.jinja_env.globals['get_resource_as_string'] = get_resource_as_string

# Moove somewhere else
m = Moltin(app.config['MOLTIN_CLIENT_ID'], app.config['MOLTIN_CLIENT_SECRET'])
access_token = m.authenticate()

db = SQLAlchemy(app)
migrate = Migrate(app, db)


@app.after_request
def apply_cors_to_amp_cache(response):
    response.headers["Access-Control-Allow-Origin"] = '*.ampproject.org'
    response.headers["Access-Control-Allow-Origin"] = '*.amp.cloudflare.com'
    source_origin = request.args.get('__amp_source_origin', '')
    if source_origin:
        response.headers["AMP-Access-Control-Allow-Source-Origin"] = source_origin
    response.headers["Access-Control-Expose-Headers"] = 'Access-Control-Expose-Headers'
    return response


from packjoy.api.routes import api
from packjoy.site.views import site
from packjoy.mail import mail_service
from packjoy.common import common
from packjoy.common.models import User, Role

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)
# Importing admin stuff`@@@@"""""""

# define a context processor for merging flask-admin's template context into the
# flask-security views.
import packjoy.admin.admin

app.register_blueprint(api, url_prefix='/api')
app.register_blueprint(site)
app.register_blueprint(common)
app.register_blueprint(mail_service, url_prefix='/mail')