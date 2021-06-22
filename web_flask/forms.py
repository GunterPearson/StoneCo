#!/usr/bin/python3
"""Sign-up & log-in forms."""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Optional


class ContactForm(FlaskForm):
    """User Sign-up Form."""
    name = StringField('Name', validators=[DataRequired()])

    subject = StringField(
        'Subject',
        validators=[DataRequired()]
    )
    email = StringField(
        'Email',
        validators=[
            Length(min=6),
            Email(message='Enter a valid email.'),
            DataRequired()
        ]
    )
    message = StringField('Message', validators=[DataRequired()])
    submit = SubmitField('Submit')

class LoginForm(FlaskForm):
    """User Sign-up Form."""
    username = StringField('Username', validators=[DataRequired()])

    password = StringField(
        'Password',
        validators=[DataRequired()]
    )
    submit = SubmitField('Submit')

class ChangeForm(FlaskForm):
    """User Sign-up Form."""
    t1 = StringField('T1', validators=[DataRequired()])

    p1 = StringField(
        'P1',
        validators=[DataRequired()]
    )
    t2 = StringField('T2', validators=[DataRequired()])

    p2 = StringField(
        'P2',
        validators=[DataRequired()]
    )
    p2a = StringField(
        'P2a',
        validators=[DataRequired()]
    )
    t3 = StringField('T3', validators=[DataRequired()])

    p3 = StringField(
        'P3',
        validators=[DataRequired()]
    )
    p3a = StringField(
        'P3a',
        validators=[DataRequired()]
    )
    submit = SubmitField('Submit')
