from flask import render_template, redirect, url_for,  request, flash, session
from flask_login import login_user
from . import auth
from .. models import User

@auth.route('/login')
def login():
    return render_template('pages/login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    print(email)
    remember = True if request.form.get('remember') else False
    user = User.query.filter_by(email=email).first()
    print(user.verify_password(password))
    if user is not None and  user.verify_password(password):
        login_user(user, remember)
        print(user)
        next = request.args.get('next')
        if next is None or not next.startswith('/'):
            next = url_for('.main.profile')
        return redirect(next)
    flash('Please check your login details and try again.')
    return render_template('pages/login.html')



