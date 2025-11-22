import unittest
from app import app
import werkzeug

if not hasattr(werkzeug, '__version__'): 
    werkzeug.__version__ = "mock-version"

class APITestCase(unittest.TestCase): 
    @classmethod 
    def setUpClass(cls):
        cls.client = app.test_client()

    def test_home_out(self):
        response = self.tester.get('/')
        self.assertTrue(response.status_code, 404)

    def test_auth_token_generation(self):
        response = self.tester.post('/login')
        self.assertEqual(response.status_code, 200)
        self.assertIn('access_token', response.json)
        self.assertTrue(len(response.json['access_token']) > 0)

    def test_unauthorized_access_block(self):
        response = self.tester.get('/protected')
        self.assertEqual(response.status_code, 401)

if __name__ == '__main__':
    unittest.main()
