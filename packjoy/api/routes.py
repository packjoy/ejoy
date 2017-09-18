from flask import Blueprint, jsonify, request
from packjoy import db
from packjoy.common.models import Email
from packjoy.common.forms import EmailForm
from packjoy.common.helpers.moltin_helper import get_prods_by_slug, get_brand_by_slug


api = Blueprint('api', __name__)


@api.route('/api/email', methods=['POST'])
def adding_email_address():
    form = EmailForm()
    form.from_json(request.get_json())
    if form.validate():
        if Email.query.filter_by(email=form.email.data).first() is None:
            newsletter_subs = Email(email=form.data['email'])
            db.session.add(newsletter_subs)
            db.session.commit()
            return jsonify({ 'message' : '10% discount in your inbox. Use this email address at checkout!' }), 200
        return jsonify({ 'message': 'This email has already joined.' }), 400
    return jsonify({ 'message' : form.errors }), 400


@api.route('/api/products/')
@api.route('/api/products/<slug>')
def get_products(slug=None):
    data = get_prods_by_slug(slug)
    return jsonify(data)

@api.route('/api/product/add_to_cart', methods=['POST'])
def add_to_cart():
    print(request.form['prod_id'])
    return jsonify({ 'message': 'Product added' })