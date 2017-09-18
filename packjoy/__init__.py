from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
# from flask_admin import Admin
from moltin.moltin import Moltin
from flask_migrate import Migrate
import pprint


app = Flask(__name__)
app.config.from_pyfile('../config_dev.py')
pp = pprint.PrettyPrinter(indent=2)


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
from packjoy.common import common

app.register_blueprint(api, url_prefix='/api')
app.register_blueprint(site, template_folder='templates')
app.register_blueprint(common)