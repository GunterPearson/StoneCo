#!/usr/bin/python3
""" Starts a Flask Web Application """
from flask import Flask, render_template, redirect, request, flash, jsonify, url_for
from web_flask.database import Database
import os
from dotenv import load_dotenv
from flask_cors import CORS
from web_flask.forms import ContactForm, LoginForm, ChangeForm
from flask_mail import Message, Mail
import smtplib
app = Flask(__name__)
cors = CORS(app, resources={r"": {"origins": "*"}})

load_dotenv()
MAIL_USERNAME = os.getenv('MAIL_USERNAME')
MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
LOGIN_USERNAME = os.getenv('LOGIN_USERNAME')
LOGIN_PASSWORD = os.getenv('LOGIN_PASSWORD')

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_DEBUG'] = True
app.config['MAIL_USERNAME'] = MAIL_USERNAME
app.config['MAIL_PASSWORD'] = MAIL_PASSWORD
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
        # msg = Message(form.subject.data, sender=form.email.data, recipients=['stoneco.downflo@gmail.com'])
        msg = Message(form.subject.data, sender=form.email.data, recipients=['gunterpearson2000@gmail.com'])
        msg.body = form.name.data + "\n" + form.message.data + "\n\n" + form.email.data
        mail.send(msg)
        flash("Message is Sent!")
    return render_template("home.html", form=form)

@app.route('/change', strict_slashes=False, methods=['GET', 'POST'])
def change():
    """home route for html file"""
    db = Database()
    form = ChangeForm()
    if request.method == "POST":
        t1 = form.t1.data
        p1 = form.p1.data
        t2 = form.t2.data
        p2 = form.p2.data
        p2a = form.p2a.data
        t3 = form.t3.data
        p3 = form.p3.data
        p3a = form.p3a.data
        if t1:
            update = {'title': t1, 'name': 1}
            db.update_title_about(update)
        if p1:
            update = {'p1': p1, 'name': 1}
            db.update_p1_about(update)
        if t2:
            update = {'title': t2, 'name': 2}
            db.update_title_about(update)
        if p2:
            update = {'p1': p2, 'name': 2}
            db.update_p1_about(update)
        if p2a:
            update = {'p2': p2a, 'name': 2}
            db.update_p2_about(update)
        if t3:
            update = {'title': t3, 'name': 3}
            db.update_title_about(update)
        if p3:
            update = {'p1': p3, 'name': 3}
            db.update_p1_about(update)
        if p3a:
            update = {'p2': p3a, 'name': 3}
            db.update_p2_about(update)
        db.close()
        return redirect(url_for('about'))
    return render_template("change.html", form=form)

@app.route('/login', strict_slashes=False, methods=['GET', 'POST'])
def login():
    """home route for html file"""
    form = LoginForm()
    if request.method == "POST":
        if form.username.data == LOGIN_USERNAME and form.password.data == LOGIN_PASSWORD:
            return redirect(url_for('change'))
    return render_template("login.html", form=form)

@app.route('/contact', strict_slashes=False, methods=['GET', 'POST'])
def contact():
    """home route for html file"""
    return render_template("contact-us.html")

@app.route('/about', strict_slashes=False)
def about():
    db = Database()
    # db.create_about()
    # db.insert_about()
    jinja_tup = db.get_about()
    db.close()
    tup_1 = jinja_tup[0]
    tup_2 = jinja_tup[1]
    tup_3 = jinja_tup[2]
    """home route for html file"""
    return render_template("about-us.html", tup_1=tup_1, tup_2=tup_2, tup_3=tup_3)

@app.route('/projects', strict_slashes=False)
def projects():
    """home route for html file"""
    return render_template("projects.html")
