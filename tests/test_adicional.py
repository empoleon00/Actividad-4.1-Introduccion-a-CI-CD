import unittest
from src.app import app

class TestAdditionalRoutes(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_home_status(self):
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)

    def test_home_content(self):
        response = self.app.get("/")
        self.assertIn("Hello", response.data.decode())

    def test_404(self):
        response = self.app.get("/noexiste")
        self.assertEqual(response.status_code, 404)

if __name__ == "__main__":
    unittest.main()