from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# app = Flask(__name__)
# db = SQLAlchemy(app, session_options={"expire_on_commit": False})
db = SQLAlchemy()
# TODO: connect to a local postgresql database
# migrate = Migrate(app, db)


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
    # city_index = Index(city_index, this.city)
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
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'))
    venue_id = db.Column(db.Integer, db.ForeignKey('venue.id'))
    start_time = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'{self.artist_id}, {self.venue_id}, {self.start_time}'

