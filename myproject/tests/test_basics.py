import unittest
from flask import current_app
from app import create_app, db
from config import config


class BasicsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        # print(self.app.config.get('testing'))
        # self.app.config.update({
        #     'TESTING': True,
        # })
        print(self.app)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.client = self.app.test_client(use_cookies=True)

    def tearDown(self):
        
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_app_exists(self):
        self.assertFalse(current_app is None)

    def test_app_is_testing(self):
        self.assertTrue(current_app.config['TESTING'])
