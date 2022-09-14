import unittest
import os
os.path.join("..")
from app import create_app, db
from app.models import User, Role



class UserModelTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        # print(self.app.config.get('testing'))
        # self.app.config.update({
        #     'TESTING': True,
        # })
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.client = self.app.test_client(use_cookies=True)

    def tearDown(self):
        pass
        # db.session.remove()
        # db.drop_all()
        # self.app_context.pop()
#----------------------------------------------------------------------------#
# password
#----------------------------------------------------------------------------#

    def test_password_setter(self):
        new_password=User(password='ghjfWSDF')
        self.assertTrue(new_password.password_hash is not None)

    def test_no_password_getter(self):
        new_password=User(password='ghjfWSDF')
        with self.assertRaises(AttributeError):
            new_password.password

    def test_password_verification(self):
        new_password = User(password='ghjfWSDF')
        self.assertTrue(new_password.verify_password('ghjfWSDF'))
        self.assertFalse(new_password.verify_password('dfghg'))


        
        

        

