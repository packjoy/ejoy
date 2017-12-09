import uuid 
from packjoy import pp
from flask import url_for
from flask_security import UserMixin, RoleMixin


from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

roles_users = db.Table('roles_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))


# User Model, with User Attributes
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(255), nullable=True)
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    # This is the register/login email
    email = db.Column(db.String(255), unique=True)
    city = db.Column(db.String(300), nullable=True)
    name = db.Column(db.String(124), unique=False, nullable=True)
    emails = db.relationship('Email', cascade='all, delete-orphan', backref='user', lazy='joined')
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))
    tokens = db.relationship('Token', cascade='all, delete-orphan', backref='user',lazy='joined')

    def __repr__(self):
        return 'User: {}'.format(self.emails[0])


# Roles a user can have
# Needs to be used beacause of
# the flask security
class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

    def __str__(self):
        return self.name

    # __hash__ is required to avoid the exception TypeError: unhashable type: 'Role' when saving a User
    def __hash__(self):
        return hash(self.name)

    def __repr__(self):
        return self.name 



# This needs to be moved somewhere else
class Email(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=False, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    active = db.Column(db.Boolean(), default=True)

    def __str__(self):
        return self.email

    def __repr__(self):
        return self.email 


class Token(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    token_code = db.Column(db.String(20), unique=True, nullable=False)
    description = db.Column(db.String(546))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)

    def __init__(self, description='', user_id=''):
        self.token_code = uuid.uuid4().hex[:10].upper()
        self.description = description
        self.user_id = user_id

    def __repr__(self):
        return '<User id %r>' % self.user_id


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


from flask_security import Security, SQLAlchemyUserDatastore
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security()