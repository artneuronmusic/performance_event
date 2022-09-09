#defines the flask application instance, inc luding a few tasks that help manage the applicaton
import os
import click
from flask_migrate import Migrate
from app import create_app, db
from app.models import Venue, Artist, Show

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, Venue=Venue, Artist=Artist, Show=Show)


@app.cli.command()
# @click.argument('test_names', nargs=-1)
# def test(test_names):
def test():
    """Run the unit tests."""
    import unittest
   
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
# @app.cli.command()
# @click.argument('test_names', nargs=-1)
# def test(test_names):
#     """Run the unit tests."""
#     import unittest
#     if test_names:
#         tests = unittest.TestLoader().loadTestsFromNames(test_names)
#     else:
#         tests = unittest.TestLoader().discover('tests')
#     unittest.TextTestRunner(verbosity=2).run(tests)