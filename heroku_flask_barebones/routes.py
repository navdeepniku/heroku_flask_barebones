from flask import url_for
from flask import request, redirect

from heroku_flask_barebones import app

@app.route('/')
def home():
    redirect(url_for('home'))
    return "hi this is sample heroku flask app"
