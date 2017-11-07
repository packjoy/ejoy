import uuid 
from packjoy import db, pp
from flask import url_for
from flask_security import UserMixin, RoleMixin

# User Model, with User Attributes
class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))
    email = db.relationship('Email', backref='user', lazy='joined', nullable=False)
    token = db.relationship('Token', backref='user',lazy='joined', nullable=True)

    def __repr__(self):
        return '<User %s - %s>' % (self.email, self.roles)


# Roles a user can have
# Needs to be used beacause of
# the flask security
class Role(db.Model, RoleMixin):
    __tablename__ = 'roles'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

    def __str__(self):
        return self.name

    # __hash__ is required to avoid the exception TypeError: unhashable type: 'Role' when saving a User
    def __hash__(self):
        return hash(self.name)

    def __repr__(self):
        return '<Role %s>' % self.name 



# This needs to be moved somewhere else
class Email(db.Model):
    __tablename__ = 'emails'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)

class Token(db.Model):
    __tablename__ = 'tokens'
    id = db.Column(db.Integer, primary_key=True)
    token_code = db.Column(db.String(20), unique=True)
    description = db.Column(db.String(546))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)

    def __init__(self, description='', user_id=''):
        self.token_code = uuid.uuid4().hex[:10].upper()
        self.description = description
        self.user_id = user_id

    def __repr__(self):
        return '<Subscriber %r>' % self.email

# Define models
roles_users = db.Table('roles_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))



class Product(object):
    def __init__(self, data):
        self.created_at = data['created_at']
        self.description = data['description']
        self.id = data['id']
        self.images = [image['url']['https'] for image in data['images']]
        self.price = data['price']['value']
        self.slug = data['slug']
        self.stock_level = data['stock_level']
        self.title = data['title']
        self.brand = {
            'title': data['brand']['data']['title'],
            'slug': data['brand']['data']['slug'],
            'description': data['brand']['data']['description'],
            'banner': url_for('site.static', _external=True, filename='img/{}_banner.png'
                                                                .format(data['brand']['data']['title'].lower()))
        }
        self.category = [data['category']['data'][cat_id] for cat_id in data['category']['data']]

    def get_stock_status(self):
        if int(self.stock_level) <= 5:
            return '{} pieces left'.format(self.stock_level)
        elif int(self.stock_level) > 5 and int(self.stock_level) <=15:
            return 'Low Stock'
        else: 
            return 'In stock'

    def __repr__(self):
        return '<{} Product>'.format(self.title)


class Brand(object):
    def __init__(self, products=None):
        self.products = products
        self.title = self.products[0].brand['title']
        self.slug = self.products[0].brand['slug']
        self.description = self.products[0].brand['description']
        self.banner = url_for('site.static', _external=True, filename='img/{}_banner.png'.format(self.title.lower()))

    def __repr__(self):
        return '<{} Brand>'.format(self.title)