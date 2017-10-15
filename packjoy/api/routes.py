from flask import Blueprint, jsonify, request
from packjoy import db
from packjoy.common.models import Email
from packjoy.common.forms import EmailForm
from packjoy.common.helpers.moltin_helper import get_prods_by_slug, get_brand_by_slug
from packjoy.mail.mail_helpers import send_token_to_user


api = Blueprint('api', __name__)


@api.route('/email', methods=['POST'])
def adding_email_address():
    form = EmailForm()
    form.from_json(request.get_json())
    if form.validate():
        if Email.query.filter_by(email=form.email.data).first() is None:
            subscription = Email(email=form.data['email'])
            db.session.add(subscription)
            db.session.commit()
            send_token_to_user(email=subscription.email,
                                token=subscription.token)
            return jsonify({ 'message' : '10% discount in your inbox. Use this email address at checkout!' }), 200
        return jsonify({ 'message': 'This email has already joined.' }), 400
    return jsonify({ 'message' : form.errors['email'][0] }), 400


@api.route('/products/')
@api.route('/products/<slug>')
def get_products(slug=None):
    data = get_prods_by_slug(slug)
    return jsonify(data)

@api.route('/product/add_to_cart', methods=['POST'])
def add_to_cart():
    print(request.form['prod_id'])
    return jsonify({ 'message': 'Product added' })