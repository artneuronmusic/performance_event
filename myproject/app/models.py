import re
from . import db
from . import login_manager
from flask import current_app
from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from wtforms import ValidationError
# from werkzeug.security import generate_password_hash, check_password_hash

class Venue(db.Model):
    __tablename__ = 'venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(120), nullable=False)
    city = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(120), nullable=False)
    genres = db.Column(db.ARRAY(db.String(200)), nullable=False)
    website_link = db.Column(db.String(200))
    facebook_link = db.Column(db.String(120))
    seeking_talent = db.Column(db.Boolean())
    seeking_talent_description = db.Column(
        db.String(200))  # watch out the minor change
    image_link = db.Column(db.String(500))
    show_artist = db.relationship(
        'Artist', secondary='show', back_populates='show_venue',
        lazy='dynamic')

    def __repr__(self):
        return f"{self.name}, {self.id}"


class Artist(db.Model):
    __tablename__ = 'artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    city = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(120), nullable=False)
    genres = db.Column(db.ARRAY(db.String(200)), nullable=False)
    website_link = db.Column(db.String(200))
    facebook_link = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    seeking_venue = db.Column(db.Boolean())  # watch out the minor change
    seeking_venue_description = db.Column(db.String(200))
    show_venue = db.relationship(
        'Venue',
        secondary='show',
        back_populates='show_artist',
        lazy='dynamic')

    def __repr__(self):
        return f'{self.name}, {self.id}, {self.city}'

class Show(db.Model):
    __tablename__ = 'show'
    id = db.Column(db.Integer, primary_key=True)
    artist_id = db.Column(db.Integer(), db.ForeignKey('artist.id', ondelete='CASCADE'))
    venue_id = db.Column(db.Integer(), db.ForeignKey('venue.id', ondelete='CASCADE'))
    start_time = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'{self.artist_id}, {self.venue_id}, {self.start_time}'


class User(db.Model,UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True) 
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    roles = db.relationship('Role', secondary='user_roles', backref='user', lazy=True)
    confirmed = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'{self.email}, {self.password}, {self.name}'

    def generate_confirmation_token(self, expiration=60):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        print(self.id)
        return s.dumps({'confirm': self.id}).decode('utf-8')

    def confirm_account(self, token):
        s=Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token.encode('utf-8'))      
        except:
            return False
        if data.get('confirm') != self.id:
            return False
        self.confirmed = True
        db.session.add(self)
        return True

    # @property
    # def password(self):
    #     raise AttributeError('password is not a readable attribute')

    # @password.setter
    # def password(self, password):
    #     self.password_hash = generate_password_hash(password)

    # def verify_password(self, password):
    #     return check_password_hash(self.password_hash, password)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=True)
    #role_name = db.Column(db.String(50), unique=True)
    
    def __repr__(self):
        return f'{self.id}, {self.name}'


class UserRoles(db.Model):
        __tablename__ = 'user_roles'
        id = db.Column(db.Integer(), primary_key=True)
        user_id = db.Column(db.Integer(), db.ForeignKey('users.id', ondelete='CASCADE'))
        role_id = db.Column(db.Integer(), db.ForeignKey('roles.id', ondelete='CASCADE'))


