import os
import unittest

from webscraper import app

class BasicTests(unittest.TestCase):

    ############################
    #### setup and teardown ####
    ############################
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = True
        self.app = app.test_client()
        self.assertEqual(app.debug,True)
    def tearDown(self):
        pass


        ###############
        #### tests ####
        ###############

    def test_main_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
