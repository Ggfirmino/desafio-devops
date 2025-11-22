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

    def test_docs(self):
        response = self.tester.post('/swagger/')
        self.assertEqual(response.status_code, 200)

    def test_unauthorized_access_block(self):
        response = self.tester.get('/protected')
        self.assertEqual(response.status_code, 401)

if __name__ == '__main__':
    unittest.main()
