# src/test/test_app.py

import unittest

from src.app.app import create_app


class TestApp(unittest.TestCase):
    """
    Test suite for the Flask application.
    """
    def setUp(self):
        """
        Set up the test client before each test.
        """
        app = create_app()
        self.app = app.test_client()
        self.app.testing = True


    def test_hello_world(self):
        """
        Test that the root URL returns "Hello, World!".
        """
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'Hello, World!')


if __name__ == '__main__':
    unittest.main()
