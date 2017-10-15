from packjoy import app
from flask_mail import Mail, Message
from flask import Blueprint

mail = Mail(app)
mail_service = Blueprint('mail_service', __name__, template_folder='templates')

@mail_service.route('/test')
def test_email():
    try:
        msg = Message("Hello",
            sender="ejoy.main@gmail.com",
            recipients=["szeka1994@gmail.com"])
        msg.body = "testing"
        msg.html = "<b>Hello there</b>"
        mail.send(msg)
        return 'Thank you'
    except Exception as e:
        return str(e)
