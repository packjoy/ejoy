import uuid 
from packjoy import db, pp
from flask import url_for
from flask_security import UserMixin, RoleMixin


# This needs to be moved somewhere else
class Email(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    token = db.Column(db.String(20), unique=True)

    def __init__(self, email=''):
        self.email = email
        self.token = uuid.uuid4().hex[:8].upper()

    def __repr__(self):
        return '<Subscriber %r>' % self.email

# Define models
roles_users = db.Table('roles_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))

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
        return '<Role %s>' % self.name 

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))

    def __repr__(self):
        return '<User %s - %s>' % (self.email, self.roles)

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
            'banner': url_for('site.static', filename='img/{}_banner.jpg'
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
        self.banner = url_for('site.static', filename='img/{}_banner.jpg'.format(self.title.lower()))

    def __repr__(self):
        return '<{} Brand>'.format(self.title)