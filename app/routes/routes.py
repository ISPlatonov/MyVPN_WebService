from flask import render_template, redirect, url_for, flash
from app import app
from flask import Blueprint
from flask_login import login_required, current_user
from app import db

routes = Blueprint('routes', __name__)


@routes.route('/')
@routes.route('/index')
def index():
    return render_template('index.html')


@routes.route('/learn-more')
def learn_more():
    return render_template('learn-more.html')


@routes.route('/profile')
@login_required
def profile():
    return render_template('profile.html')


@routes.route('/order')
def order():
    flash('You have to log in to order')
    return redirect(url_for('auth.log_in'), next=url_for('auth.order'))
