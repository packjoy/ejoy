from flask_admin.contrib.sqla import ModelView

from packjoy.app import admin, db
from packjoy.models import Email


admin.add_view(ModelView(Email, db.session))
