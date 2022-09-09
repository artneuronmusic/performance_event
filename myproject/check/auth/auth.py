# from flask import Blueprint, render_template, redirect, url_for,  request, flash, session
# from werkzeug.security import generate_password_hash, check_password_hash
# from flask_login import login_user, login_required, logout_user
# from .models import User, Role, UserRoles
# from functools import wraps
# # from flask_user import current_user, login_required, roles_required, UserManager, UserMixin
# from .import db
# # from .import user_manager


# # from . import dbq

# auth = Blueprint('auth', __name__)

# @auth.route('/login')
# def login():
#     return render_template('pages/login.html')

# @auth.route('/login', methods=['POST'])
# def login_post():
#     email = request.form.get('email')
#     password = request.form.get('password')
  
#     remember = True if request.form.get('remember') else False
#     user = User.query.filter_by(email=email).first()
#     # if not user or not user_manager.verify_password(password, user.password):
#     if not user or not check_password_hash(user.password, password):
#         # print(check_password_hash(user.password, password))
#         flash('Please check your login details and try again.')
#         return redirect(url_for('auth.login'))


#     login_user(user, remember)
#     return redirect(url_for('main.profile'))

# @auth.route('/signup')
# def signup():
#     return render_template('pages/signup.html')

# @auth.route('/signup', methods=['POST'])
# def signup_post():
#     email = request.form.get('email')
#     name = request.form.get('name')
#     password = request.form.get('password')
#     account = request.form.get('radio-accounts')
#     print(type(account))
#     user = User.query.filter_by(email=email).first()
#     role = Role.query.filter_by(id=int(account)).first()

#     if user: 
#         flash('Email address already exists')
#         return redirect(url_for('auth.login'))
    
#     new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))
#     new_user.roles.append(role)
#     #new_user = User(email=email, name=name, password=user_manager.hash_password(password))   
#     db.session.add(new_user)
#     print(new_user)
#     db.session.commit()

#     return redirect(url_for('auth.login'))

# @auth.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     return redirect(url_for('main.index'))


# def role_required(roles):
#         """
#         see: https://flask.palletsprojects.com/en/2.1.x/patterns/viewdecorators/
#         """
#         def wrapper(fn):
#             @wraps(fn)
#             def decorated_view(*args, **kwargs):
#                 # if not current_user.is_authenticated():
#                 #     return redirect(url_for('auth.login', message="sorry, u are not logged in."))
#                 session_id=session['_user_id']
#                 print(session_id)
#                 new =[]  
#                 role_info = db.session.query(Role.name).select_from(UserRoles).join(Role).filter(UserRoles.user_id==session_id).all()
           
#                 for i in range(len(role_info)):
#                     new=role_info[i][0]
#                 print(str(new))
           
#                 if not new in roles:    
#                         flash('Sorry, this page requires permission') 
#                         return redirect(url_for('auth.login', message="sorry, you dont have right to access it."))
                
#                 return fn(*args, **kwargs)
#             return decorated_view
#         return wrapper
