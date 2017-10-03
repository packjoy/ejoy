from flask import redirect, url_for, request
from flask_admin import Admin
from flask_admin.contrib import sqla
from flask_security import current_user

from packjoy import app, db
from packjoy.common.models import Email, User, Role

class MyModelView(sqla.ModelView):
    def is_accessible(self):
        print(current_user.has_role('Admin'))
        return current_user.has_role('Admin')


admin = Admin(app, name='ejoy', template_mode='bootstrap3')
admin.add_view(MyModelView(User, db.session))
admin.add_view(MyModelView(Role, db.session))
admin.add_view(MyModelView(Email, db.session))