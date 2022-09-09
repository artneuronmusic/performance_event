from flask import render_template
from . import main

@main.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404

@main.errorhandler(500)
def server_error(error):
    return render_template('errors/500.html'), 500
