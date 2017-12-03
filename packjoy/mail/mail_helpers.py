from flask import render_template
from flask_mail import Message
from packjoy.mail import mail
from packjoy.common.helpers.moltin_helper import get_prods_by_slug, get_brand_by_slug

mail_kalman = 'kkonat96@gmail.com'
mail_dragos = 'dragosimbrea@yahoo.com'
mail_szeka = 'szeka1994@gmail.com'
mail_ejoy = 'ejoy.main@gmail.com'


def send_token_to_user(email=None, token=None):
    if email and token:
        products = get_prods_by_slug(slug=None)
        brand = get_brand_by_slug(brand_slug='packjoy')
        print('Email {}'.format(email))
        print('Brand {}'.format(brand.banner))
        try:
            msg = Message("10 percent discount on your next purchase!",
                sender="ejoy.main@gmail.com",
                recipients=[email])
            msg.body = "testing"
            msg.html = render_template('mail/token.html',
                                    email=email,
                                    token=token,
                                    products = products,
                                    brand = brand)
            mail.send(msg)
            return True;
        except Exception as e:
            print("Error happened: {}".format(str(e)))
            return str(e)
    return False;


def send_contact_form_message(email=None, name=None, message=None):
    if email and name and message:
        try:
            msg = Message("Uj uzenet: Contact form",
                sender=email,
                recipients=[mail_ejoy, mail_kalman, mail_szeka, mail_dragos])
            msg.html = "<b>Uzenet</b>: {} <br /><br /><b>From {} : {}</b>".format(message, name, email)
            mail.send(msg)
            return True;
        except Exception as e:
            print("Error happened: {}".format(str(e)))
            return str(e)
    return False;





'''
This functin will send an email
to the provided email address
The Campaign will provide additional
datas: template, products
'''
def send_email(email_address, campaign):
    products = None # We need get the products based on the campaign type
    pass