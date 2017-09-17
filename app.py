from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from moltin.moltin import Moltin
from flask_migrate import Migrate
from packjoy import app
import pprint

pp = pprint.PrettyPrinter(indent=2)

app = Flask(__name__)
app.config.from_object('packjoy.config.Development')

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

admin = Admin(app, name='packjoy', template_mode='bootstrap3')
import packjoy.admin


@app.after_request
def apply_cors_to_amp_cache(response):
    response.headers["Access-Control-Allow-Origin"] = '*.ampproject.org'
    response.headers["Access-Control-Allow-Origin"] = '*.amp.cloudflare.com'
    source_origin = request.args.get('__amp_source_origin', '')
    if source_origin:
        response.headers["AMP-Access-Control-Allow-Source-Origin"] = source_origin
    response.headers["Access-Control-Expose-Headers"] = 'Access-Control-Expose-Headers'
    return response


import packjoy.routes

if __name__ == "__main__":
    app.run(debug=True) 