#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

import os
from logging import Formatter, FileHandler
import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
# from flaskr.models import Venue, Artist, Show
# from flask_moment import Moment
import dateutil.parser
import babel

# from flask_migrate import Migrate

#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

db = SQLAlchemy()


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )
# Database settings
    app.config["SQLALCHEMY_DATABASE_URI"] =  "postgresql:///fyyur_database"
    db.init_app(app)
    with app.app_context():
        db.create_all()
        db.session.commit()
    migrate = Migrate(app, db)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User
    @login_manager.user_loader
    def load_user(user_id):
        #the user_id is the primary key from data
        return User.query.get(int(user_id))
  
    

 

    #blueprint for auth routes in app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    #blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    if test_config is None:
            app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    logging.basicConfig(filename='error.log', level=logging.INFO)

   

# #----------------------------------------------------------------------------#
# # Filters.
# #----------------------------------------------------------------------------#


    def format_datetime(value, format='medium'):
        date = dateutil.parser.parse(value)
        if format == 'full':
            format = "EEEE MMMM, d, y 'at' h:mma"
        elif format == 'medium':
            format = "EE MM, dd, y h:mma"
        return babel.dates.format_datetime(date, format, locale='en')


    app.jinja_env.filters['datetime'] = format_datetime

    if not app.debug:
        file_handler = FileHandler('error.log')
        file_handler.setFormatter(Formatter(
            '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
        app.logger.setLevel(logging.INFO)
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)
        app.logger.info('errors')

    return app

#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

# Default port:
# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=8000, debug=True)

# Or specify port manually:
'''
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
'''
