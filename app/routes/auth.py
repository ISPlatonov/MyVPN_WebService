from flask_login import login_user, logout_user
from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import User
from app import db


auth = Blueprint('auth', __name__)


@auth.route('/log-in')
def log_in():
    return render_template('log-in.html')


@auth.route('/log-in', methods=['POST'])
def log_in_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False
    next_url = request.args.get('next')

    user = User.query.filter_by(email=email).first()

    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.log_in')) # if the user doesn't exist or password is wrong, reload the page

    # if the above check passes, then we know the user has the right credentials
    login_user(user, remember=remember)
    if next_url != None:
        return redirect(next_url)
    else:
        return redirect(url_for('routes.index'))


@auth.route('/sign-up', methods=['GET'])
def sign_up():
    return render_template('sign-up.html')


@auth.route('/sign-up', methods=['POST'])
def sign_up_post():
    email = request.form.get('email')
    name = request.form.get('name')
    lastname = request.form.get('lastname')
    password = request.form.get('password')
    confirm_password = request.form.get('confirm-password')
    if password != confirm_password:
        flash('Passwords do not match')
        return redirect(url_for('auth.sign_up'))

    # if this returns a user, then the email already exists in database
    user = User.query.filter_by(email=email).first()

    # if a user is found, we want to redirect back to signup page so user can try again
    if user:
        flash('Email address already exists')
        return redirect(url_for('auth.sign_up'))

    # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    new_user = User(email=email,
                    name=name,
                    lastname=lastname,
                    date_until_paid=
                    password=generate_password_hash(password, method='sha256'))

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for('auth.profile'))


@auth.route('/forgot-password')
def forgot_password():
    return render_template('forgot-password.html')


@auth.route('/log-out')
def log_out():
    logout_user()
    return redirect(url_for('routes.index'))


@auth.route('/order')
def order():
    return render_template('order.html')
