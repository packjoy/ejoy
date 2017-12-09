from flask import Blueprint, jsonify, request
from packjoy.common.models import db, Email, Role, Token, User
from packjoy.common.forms import EmailForm, ContactForm
from packjoy.common.helpers.moltin_helper import get_prods_by_slug, get_brand_by_slug
from packjoy.mail.mail_helpers import send_token_to_user, send_contact_form_message


api = Blueprint('api', __name__)


@api.route('/email', methods=['POST'])
def adding_email_address():
    form = EmailForm()
    form.from_json(request.get_json())
    if form.validate():
        email = form.email.data
        if Email.query.filter_by(email=email).first() is None:
            role_subscriber = Role.query.filter_by(name='subscriber').first()
            token = Token(description='10\% \off for joining the email list')
            subscription = User(active=True, email=email, 
                            emails=[Email(email=email)], roles=[role_subscriber],
                            tokens=[token])
            db.session.add(subscription)
            db.session.commit()
            send_token_to_user(email=subscription.email,
                                token=token.token_code)
            return jsonify({ 'message' : '10% discount in your inbox. Use this email address at checkout!' }), 200
        return jsonify({ 'message': 'This email has already joined.' }), 400
    return jsonify({ 'message' : form.errors['email'][0] }), 400

@api.route('/contact-us', methods=['POST'])
def contact_us_form():
    data = dict(request.form)
    form = ContactForm()
    form.from_json(data)
    if form.validate:
        send_contact_form_message(name=form.name.data,
                    email=form.email.data,
                    message=form.message.data)
        return jsonify({ 'message' : 'Works on backend!' })
    return jsonify({ 'message' : 'Something really bad happend' })

@api.route('/products/')
@api.route('/products/<slug>')
def get_products(slug=None):
    data = get_prods_by_slug(slug)
    return jsonify(data)

@api.route('/product/add_to_cart', methods=['POST'])
def add_to_cart():
    print(request.form['prod_id'])
    return jsonify({ 'message': 'Product added' })