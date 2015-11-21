from wtforms import BooleanField, TextField, PasswordField, validators, SubmitField
from flask_wtf import Form


class Register_form(Form):
    first_name = TextField('Förnamn', [validators.Length(min=2, max=25)])
    last_name = TextField('Efternamn', [validators.Length(min=2, max=25)])
    email = TextField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('Lösenord', [
        validators.Required(),
        validators.EqualTo('password_confirm', message='Lösenorden måste matcha')
    ])
    password_confirm = PasswordField('Lösenordet igen')
    submit = SubmitField('Registrera')


class Login_form(Form):
    email = TextField('Email Address', [validators.Required()])
    password = PasswordField('Lösenord', [validators.Required()])
    submit = SubmitField('Logga in')