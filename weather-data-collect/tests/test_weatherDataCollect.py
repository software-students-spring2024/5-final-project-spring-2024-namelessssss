import unittest
from unittest.mock import patch
from weatherDataCollect import app, fetch_weather_data, convert_temperatures, store_weather_data
# to test coverage, run these:
# cd weather-data-collect
# docker build -t weather-data-collect .
# docker run --rm weather-data-collect sh -c "coverage run -m unittest discover tests && coverage report"

class TestWeatherDataCollect(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
    def test_fetch_weather_data(self):
        # Test the fetch_weather_data function
        with patch('requests.get') as mock_get:
            mock_get.return_value.status_code = 200
            mock_get.return_value.json.return_value = {'name': 'New York'}
            weather_data = fetch_weather_data('New York')
            self.assertIsNotNone(weather_data)
            self.assertEqual(weather_data['name'], 'New York')

    def test_convert_temperatures(self):
        # Test the convert_temperatures function
        weather_data = {
            'main': {
                'temp': 298.15
            }
        }
        converted_data = convert_temperatures(weather_data)
        self.assertIn('temp_kelvin', converted_data['main'])
        self.assertIn('temp_celsius', converted_data['main'])
        self.assertIn('temp_fahrenheit', converted_data['main'])

    @patch('weatherDataCollect.store_weather_data')
    def test_collect_weather_data(self, mock_store_weather_data):
        # Test the collect_weather_data route
        with patch('weatherDataCollect.fetch_weather_data') as mock_fetch_weather_data:
            mock_fetch_weather_data.return_value = {
                'name': 'New York',
                'main': {
                    'temp': 298.15
                }
            }
            response = self.app.post('/collect', json={'city': 'New York'})
            self.assertEqual(response.status_code, 200)
            mock_store_weather_data.assert_called_once()

if __name__ == '__main__':
    unittest.main()