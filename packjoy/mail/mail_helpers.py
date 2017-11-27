from flask import render_template
from flask_mail import Message
from packjoy.mail import mail
from packjoy.common.helpers.moltin_helper import get_prods_by_slug, get_brand_by_slug

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


'''
This functin will send an email
to the provided email address
The Campaign will provide additional
datas: template, products
'''
def send_email(email_address, campaign):
    products = None # We need get the products based on the campaign type
    pass