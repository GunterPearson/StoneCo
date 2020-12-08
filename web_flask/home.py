#!/usr/bin/python3
""" Starts a Flask Web Application """
from flask import Flask, render_template, redirect, request, flash, jsonify
import os
from flask_cors import CORS
from web_flask.forms import ContactForm
from flask_mail import Message, Mail
import smtplib
app = Flask(__name__)
cors = CORS(app, resources={r"": {"origins": "*"}})
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SECRET_KEY'] = SECRET_KEY
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_DEBUG'] = True
app.config['MAIL_USERNAME'] = 'gunter10pearson@gmail.com'
app.config['MAIL_PASSWORD'] = 'StoneCo$$'
app.config['MAIL_DEFAULT_SENDER'] = None
app.config['MAIL_MAX_SEND'] = None
app.config['MAIL_SUPPRESS_SEND'] = False
app.config['MAIL_ASCII_ATTATCHMENTS'] = False
mail = Mail(app)


@app.route('/', strict_slashes=False, methods=['GET', 'POST'])
def home():
    """home route for html file"""
    form = ContactForm()
    if request.method == "POST":
        msg = Message(form.subject.data, sender=form.email.data, recipients=['howaj26162@hebgsw.com'])
        msg.body = form.name.data + "\n" + form.message.data + "\n\n" + form.email.data
        mail.send(msg)
        flash("Message is Sent!")
    return render_template("home.html", form=form)

@app.route('/contact', strict_slashes=False, methods=['GET', 'POST'])
def contact():
    """home route for html file"""
    return render_template("contact-us.html")

@app.route('/about', strict_slashes=False)
def about():
    """home route for html file"""
    return render_template("about-us.html")

@app.route('/projects', strict_slashes=False)
def projects():
    """home route for html file"""
    return render_template("projects.html")
