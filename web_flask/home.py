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


@app.route('/', strict_slashes=False, methods=['GET', 'POST'])
def home():
    """home route for html file"""
    form = ContactForm()
    if request.method == "POST":
        TO = "howaj26162@hebgsw.com"
        SUBJECT = form.subject.data
        TEXT = form.name.data + "\n" + form.message.data + "\n\n" + form.email.data
        # Gmail Sign In
        gmail_sender = 'gunter10pearson@gmail.com'
        gmail_passwd = 'Gunter$2000'
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_sender, gmail_passwd)
        BODY = '\r\n'.join(['To: %s' % TO,
                            'From: %s' % gmail_sender,
                            'Subject: %s' % SUBJECT,
                            '', TEXT])
        try:
            server.sendmail(gmail_sender, [TO], BODY)
        except:
            pass
        server.quit()
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
