from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from packjoy import app, db
from packjoy.common.models import Email


admin = Admin(app, name='ejoy', template_mode='bootstrap3')
admin.add_view(ModelView(Email, db.session))