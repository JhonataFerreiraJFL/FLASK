from flask import render_template
from app import app

from app.models.forms import LoginForm

@app.route('/index/')
@app.route('/')
def index():
    return render_template(
        'index.html',
        )
@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html',
                           form=form
                           )