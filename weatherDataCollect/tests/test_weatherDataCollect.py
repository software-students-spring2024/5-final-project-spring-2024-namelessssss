import unittest
from weatherDataCollect import fetch_weather_data, store_weather_data

class TestWeatherDataCollect(unittest.TestCase):
    def test_fetch_weather_data(self):
        # Test the fetch_weather_data function
        lat = 40.7128
        lon = -74.0060
        weather_data = fetch_weather_data(lat, lon)
        self.assertIsNotNone(weather_data)
        self.assertIn('current', weather_data)
        self.assertIn('temp', weather_data['current'])

    def test_store_weather_data(self):
        # Test the store_weather_data function
        weather_data = {
            'city': 'New York',
            'current': {
                'temp': 25.5,
                'humidity': 60,
                'wind_speed': 5.2
            }
        }
        store_weather_data(weather_data)
        # Add assertions to check if the data is stored correctly in the database

if __name__ == '__main__':
    unittest.main()