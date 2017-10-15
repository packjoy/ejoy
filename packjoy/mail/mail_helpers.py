from flask import render_template
from flask_mail import Message
from packjoy.mail import mail

def send_token_to_user(email=None, token=None):
    if email and token:
        try:
            msg = Message("Hello",
                sender="ejoy.main@gmail.com",
                recipients=[email])
            msg.body = "testing"
            msg.html = render_template('mail/token.html', email=email, token=token)
            mail.send(msg)
            return True;
        except Exception as e:
            print("Error happened: {}".format(str(e)))
            return str(e)
    return False;