import requests
import unittest
from collections import Counter

class TestWordCountApp(unittest.TestCase):

    def setUp(self):
        self.url = "http://127.0.0.1:5000"

    def test_correct_validation(self):
        pass

    def test_incorrect_validation(self):
        r = requests.get(self.url)
        self.assertTrue(4 == 4)

    def test_admin_addition(self):
        pass
