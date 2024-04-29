import coverage
import unittest
from unittest.mock import patch
from flask import Flask
from pymongo import MongoClient
from app import app, db, collection

class TestWebApplication(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index_get(self):
        # Test GET request to the index route
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'New York', response.data)
        self.assertIn(b'Boston', response.data)
        self.assertIn(b'Washington, D.C.', response.data)
        self.assertIn(b'Miami', response.data)

    def test_index_post(self):
        # Test POST request to the index route
        with patch.object(collection, 'find_one', return_value={
            'city': 'New York',
            'main': {
                'temp_kelvin': 298.65,
                'temp_celsius': 25.5,
                'temp_fahrenheit': 77.9
            }
        }):
            response = self.app.post('/', data={'city': 'New York', 'temp_unit': 'Celsius'})
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'New York', response.data)
            self.assertIn(b'25.5', response.data)

    def test_index_post_not_found(self):
        # Test POST request to the index route when weather data is not found
        with patch.object(collection, 'find_one', return_value=None):
            response = self.app.post('/', data={'city': 'London', 'temp_unit': 'Celsius'})
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Weather data not found', response.data)

if __name__ == '__main__':
    unittest.main()