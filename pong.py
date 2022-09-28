import os
from flask import Flask, render_template, session, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy

import random

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    r = random.randint(1, 100)
    return str(r)
