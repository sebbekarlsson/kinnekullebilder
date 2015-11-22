from wtforms import BooleanField, TextField, TextAreaField, PasswordField, validators, SubmitField
from flask_wtf import Form
from flask_wtf.file import FileField, FileAllowed, FileRequired


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


class Upload_image_form(Form):
    title = TextField('Titel', [validators.Length(min=2, max=25)])
    place = TextField('Plats, vart var fotot taget?', [validators.Length(min=2, max=25)])
    description = TextAreaField('Beskrivning', [validators.Length(min=2, max=1000)])
    image = FileField('Foto', [
        validators.Required(),
         FileAllowed(['jpg', 'jpeg', 'gif', 'png'], 'Du kan bara ladda upp bilder!')
    ])
    submit = SubmitField('Ladda upp')


class Comment_form(Form):
    text = TextField('Skriv en kommentar', [validators.Length(min=2, max=400)])
    submit = SubmitField('Skicka')