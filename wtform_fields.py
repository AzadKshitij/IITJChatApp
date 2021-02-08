from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, EqualTo, ValidationError


class RegistrationForm(FlaskForm):
    """Registration Form"""

    username = StringField('username_label', validators=[
                           InputRequired(message='Username is require'),
                           Length(min=4, max=25, message='Username can of size 4 to 25')])
    password = PasswordField('password_label', validators=[
        InputRequired(message='Password is require'),
        Length(min=4, max=25, message='Password can of size 4 to 25')])
    confirm_password = PasswordField('confirm_password_field', validators=[
        InputRequired(message='Confirm Password is require'),
        EqualTo('password', message='Password must match')])
    submit_button = SubmitField('Create')
