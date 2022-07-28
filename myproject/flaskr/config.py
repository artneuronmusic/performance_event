import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True
SQLALCHEMY_DATABASE_URI= "postgresql:///fyyur_database"
# SQLALCHEMY_DATABASE_URI= "postgresql://localhost:8000/fyyur_database"
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Connect to the database


# DATABASE_NAME = "fyyur_database"
# url = 'localhost:8000'
# SQLALCHEMY_DATABASE_URI = "postgres://{}/{}".format(
#     url, DATABASE_NAME)
# SQLALCHEMY_DATABASE_URI= "postgres://localhost:8000/fyyur_database"
# SQLALCHEMY_TRACK_MODIFICATIONS = False


