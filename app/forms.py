# Example
from flask_wtf import Form
from wtforms import TextField, TextAreaField, SubmitField, validators, ValidationError
# from wtforms import StringField, BooleanField
# from wtforms.validators import DataRequired, Length

# class LoginForm(Form):
# 	openid = StringField('openid', validators=[DataRequired()])
# 	remember_me = BooleanField('remember_me', default=False)

class ContactForm(Form):
    name = TextField("Name", [validators.Required("Please enter your name")])
    email = TextField("Email", [validators.Required("Please enter your email"), validators.Email("Please enter your email")])
    subject = TextField("Subject", [validators.Required("Please enter a subject")])
    message = TextAreaField("Message", [validators.Required("Please enter a message")])
    submit = SubmitField("Send Message")
