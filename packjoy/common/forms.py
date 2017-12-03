from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Email
import wtforms_json

wtforms_json.init()

class EmailForm(FlaskForm):
    email = StringField('email', validators=[DataRequired(), Email()])

class ContactForm(FlaskForm):
    email = StringField('email', validators=[DataRequired(), Email()])
    name = StringField('name', validators=[DataRequired()])
    message = StringField('message', validators=[DataRequired()])