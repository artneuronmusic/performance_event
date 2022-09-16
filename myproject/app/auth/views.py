from flask import (render_template, redirect, url_for,  request, flash, session)
from flask_login import login_user, logout_user, current_user, login_required
from functools import wraps
from werkzeug.security import check_password_hash, generate_password_hash
from . import auth
from .check_validation import validate_password, validate_name, validate_email
from ..email import send_email
from .. models import User, Role, UserRoles
from app import db


@auth.before_app_request
def before_request():
    if current_user.is_authenticated \
            and not current_user.confirmed \
            and request.endpoint \
            and request.blueprint != 'auth' \
            and request.endpoint != 'static':
        return redirect(url_for('auth.unconfirmed'))

@auth.route('/unconfirmed')
def unconfirmed():
    if current_user.is_anonymous or current_user.confirmed:
        flash('Your account is confirmed')
        return redirect(url_for('main.index'))
    return render_template('auth/unconfirmed.html')

@auth.route('/confirm')
@login_required
def resend_confirmation():
    token = current_user.generate_confirmation_token()
    send_email(current_user.email, 'Confirm Your Account',
               'auth/confirm', user=current_user, token=token)
    flash('A new confirmation email has been sent to you by email.')
    return redirect(url_for('main.index'))

@auth.route('/confirm/<token>')
@login_required
def confirm(token):
    if current_user.confirmed:
        return redirect(url_for('main.index'))
    elif current_user.confirm_account(token):
        db.session.commit()
        flash('Account confirmed. Thanks!')
    else:
        # TODO: Bug - Only works when logged in
        flash('The confirmation link is invalid or has expired.')
    return redirect(url_for('main.index'))

@auth.route('/logout')
@login_required
def logout():   
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('main.index'))
  
@auth.route('/login')
def login():
    return render_template('pages/login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False
    user = User.query.filter_by(email=email).first()
    if user is not None and check_password_hash(user.password, password):
        print(current_user)
        print(current_user.is_authenticated)
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
    # TODO: Clean up code for easier reading
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

    role = request.form.get('radio-accounts')
    email_check = User.query.filter_by(email=email).first()
    name_check = User.query.filter_by(name=name).first()
    role_check = Role.query.filter_by(id=int(role)).first()

    if email_check: 
        flash('Email address already exists')
        return redirect(url_for('auth.signup'))

    if name_check: 
        flash('Account name already exists')
        return redirect(url_for('auth.signup'))
    
    new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))
    new_user.roles.append(role_check)

    db.session.add(new_user)
    db.session.commit()  

    token = new_user.generate_confirmation_token()
    send_email(new_user.email, 'Confirm Your Account', 'auth/confirm', user=current_user, token=token)
    flash('A confirmation email has been sent to you by email.')
    return redirect(url_for('auth.login'))



def role_required(roles):
        """
        see: https://flask.palletsprojects.com/en/2.1.x/patterns/viewdecorators/
        """
        def wrapper(fn):
            @wraps(fn)
            def decorated_view(*args, **kwargs):
                # if not current_user.is_authenticated():
                #     return redirect(url_for('auth.login', message="sorry, u are not logged in."))
                session_id=session['_user_id']
                print(session_id)
                new =[]  
                role_info = db.session.query(Role.name).select_from(UserRoles).join(Role).filter(UserRoles.user_id==session_id).all()
           
                for i in range(len(role_info)):
                    new=role_info[i][0]
                print(str(new))
           
                if not new in roles:    
                        flash('Sorry, this page requires permission') 
                        return redirect(url_for('auth.login', message="sorry, you dont have right to access it."))
                
                return fn(*args, **kwargs)
            return decorated_view
        return wrapper






