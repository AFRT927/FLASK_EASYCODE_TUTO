from wtforms import Form 
from wtforms import StringField, SubmitField
from wtforms.fields import EmailField # para generar el correo

from wtforms import validators

class CommentForm(Form):
    username = StringField('username',
               [
                validators.DataRequired(message = 'este campo es requerido'), 
                validators.length(min=4, max=25, message='enter a valid username')                 
               ])
    email = EmailField('electronic email')
    comment = StringField('your comment')
    submit = SubmitField('send')
