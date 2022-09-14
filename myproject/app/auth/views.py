from flask import (render_template, redirect, url_for,  request, flash, session)
from flask_login import login_user, logout_user, current_user
from werkzeug.security import check_password_hash, generate_password_hash
from . import auth
from .. models import User, Role
from app import db
from .check_validation import validate_password, validate_name, validate_email

@auth.route('/login')
def login():
    return render_template('pages/login.html')
    # return render_template('pages/login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False
    user = User.query.filter_by(email=email).first()
    if user is not None and check_password_hash(user.password, password):
        login_user(user, remember)
        next = request.args.get('next')
        if next is None or not next.startswith('/'):
            next = url_for('main.profile')
        return redirect(next)
    flash('Please check your login details and try again.')
    return redirect(url_for('auth.login'))

@auth.route('/signup')
def signup():    
      return render_template('pages/signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post():
   
    email = request.form.get('email')
    email_validation = validate_email(email)
    if email_validation != "valid":
        flash('please check email, its not valid')
        return redirect(url_for('auth.signup'))
    name = request.form.get('name')
    name_validation = validate_name(name)
    if name_validation != "valid":
        flash('please check name, its not valid')
        return redirect(url_for('auth.signup'))
    password = request.form.get('password')
    pw_validation = validate_password(password)
    if pw_validation != "valid":
        flash('please check password, its not valid')
        return redirect(url_for('auth.signup'))
    account = request.form.get('radio-accounts')
    user = User.query.filter_by(email=email).first()
    role = Role.query.filter_by(id=int(account)).first()
    if user: 
        flash('Email address already exists')
        return redirect(url_for('auth.signup'))
    new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))
    new_user.roles.append(role)
    db.session.add(new_user)
    db.session.commit()  
    return redirect(url_for('auth.login'))


@auth.route('/logout')
def logout():   
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('main.index'))
  



