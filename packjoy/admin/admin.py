from flask import redirect, url_for, request, current_app
import flask_admin as admin
from flask_admin.contrib import sqla
from flask_security import current_user
from flask_admin import expose

from packjoy.common.models import Email, User, Role, db



class MyAdminIndexView(admin.AdminIndexView):
    @expose('/')
    def index(self):
        if not current_user.has_role('Admin'):
            return redirect(url_for('security.login'))
        return super(MyAdminIndexView, self).index()

class MyModelView(sqla.ModelView):
    def is_accessible(self):
        return current_user.has_role('Admin')

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for('security.login', next=request.url))

class UserView(MyModelView):
    column_auto_select_related = True
    inline_models = (Email,)
    column_list = ('name', 'email', 'emails', 'active')
 

admin = admin.Admin(name='ejoy', template_mode='bootstrap3', index_view=MyAdminIndexView())
admin.add_view(UserView(User, db.session))
admin.add_view(MyModelView(Role, db.session))
admin.add_view(MyModelView(Email, db.session))