from flask import render_template, current_app
from flask_mail import Message
from packjoy.mail import mail
from packjoy.common.helpers.moltin_helper import get_prods_by_slug, get_brand_by_slug
import requests



'''
NO ERROR HANDLING HAPPENS HERE
YOU SHOULD ADD IT WHERE YOU
INVOKE THESE HELPERS
'''



'''
This Function will send the
10 percent off coupon to the user
Should be refactored on and handled on 
CAMPAIGN level
'''
def send_token_to_user(email=None, token=None):
    if email and token:
        products = get_prods_by_slug(slug=None)
        brand = get_brand_by_slug(brand_slug='packjoy')
        emails = current_app.config['ADMIN_ADDRESSES']
        emails.append(email)
        msg = Message("10 percent discount on your next purchase!",
            sender=current_app.config['MAIL_USERNAME'],
            recipients=emails)
        msg.body = "testing"
        msg.html = render_template('mail/token.html',
                                email=email,
                                token=token,
                                products = products,
                                brand = brand)
        mail.send(msg)


'''
This handles the contact form
'''
def send_contact_form_message(email=None, name=None, message=None):
    if email and name and message:
        msg = Message("Uj uzenet: Contact form",
            sender=email,
            recipients=current_app.config['ADMIN_ADDRESSES'])
        msg.html = "<b>Uzenet</b>: {} <br /><br /><b>From {} : {}</b>".format(message, name, email)
        mail.send(msg)


'''
This function sends email to the
provided email address
it takes a subject line
and the html string 
'''
def send_email_to(email_address=None, subject_line='TEST', template='<h1>DEFAULT TESTING ONLY</h1>'):
    if email_address:
        msg = Message(subject_line, 
            sender=current_app.config['MAIL_USERNAME'],
            recipients=[email_address])
        msg.body = "You're using an outdated email client, please change."
        msg.html = template
        mail.send(msg)



def send_simple_message(email_address=[], subject_line='TEST', 
            template='<h1>DEFAULT TESTING ONLY</h1>', recipient_varables=None):
    return requests.post(
        "{}/messages".format(current_app.config['MAILGUN_API_BASE']),
        auth=("api", current_app.config['MAILGUN_API_KEY']),
        data={"from": "Ejoy Online Shop <mailgun@{}>".format(current_app.config['MAILGUN_API_DOMAIN']),
              "to": email_address,
              "subject": subject_line,
              "text": 'THIS IS A TEST!',
              "html": template,
              "recipient-variables": recipient_varables})