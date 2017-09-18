from flask import Flask

app = Flask(__name__)

from packjoy.api.routes import api
from packjoy.site.routes import site
from packjoy.common import common

app.register_blueprint(api, url_prefix='/api')
app.register_blueprint(site)
app.register_blueprint(common)