from flask import redirect, url_for, request
import flask_admin as admin
from flask_admin.contrib import sqla
from flask_security import current_user
from flask_admin import expose

from packjoy import app, db
from packjoy.common.models import Email, User, Role



class MyAdminIndexView(admin.AdminIndexView):
    @expose('/')
    def index(self):
        if not current_user.has_role('Admin'):
            return redirect(url_for('security.login'))
        return super(MyAdminIndexView, self).index()

class MyModelView(sqla.ModelView):
    def is_accessible(self):
        print(current_user.has_role('Admin'))
        print(current_user.is_authenticated)
        return current_user.has_role('Admin')

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for('security.login', next=request.url))

 
admin = admin.Admin(app, name='ejoy', template_mode='bootstrap3', index_view=MyAdminIndexView())
admin.add_view(MyModelView(User, db.session))
admin.add_view(MyModelView(Role, db.session))
admin.add_view(MyModelView(Email, db.session))