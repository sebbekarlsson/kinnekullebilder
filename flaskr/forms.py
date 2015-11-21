from wtforms import BooleanField, StringField, PasswordField, validators, SubmitField
from flask_wtf import Form


class Register_form(Form):
    first_name = StringField('Förnamn', [validators.Length(min=2, max=25)])
    last_name = StringField('Efternamn', [validators.Length(min=2, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('Lösenord', [
        validators.Required(),
        validators.EqualTo('password_confirm', message='Lösenorden måste matcha')
    ])
    password_confirm = PasswordField('Lösenordet igen')
    submit = SubmitField('Registrera')