import os
import requests
from pymongo import MongoClient

API_KEY = os.environ['OPENWEATHERMAP_API_KEY']
BASE_URL = 'https://api.openweathermap.org/data/3.0/onecall'

MONGODB_URI = os.environ['MONGODB_URI']
DB_NAME = 'Project5'
COLLECTION_NAME = 'WeatherData'

def fetch_weather_data(lat, lon):
    params = {
        'lat': lat,
        'lon': lon,
        'appid': API_KEY,
        'units': 'metric'
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def store_weather_data(weather_data):
    client = MongoClient(MONGODB_URI)
    db = client[DB_NAME]
    collection = db[COLLECTION_NAME]
    collection.insert_one(weather_data)
    client.close()

if __name__ == '__main__':
    cities = [
        {'name': 'New York', 'lat': 40.7128, 'lon': -74.0060},
        {'name': 'Boston', 'lat': 42.3601, 'lon': -71.0589},
        {'name': 'Washington, D.C.', 'lat': 38.9072, 'lon': -77.0369},
        {'name': 'Miami', 'lat': 25.7617, 'lon': -80.1918}
    ]

    for city in cities:
        weather_data = fetch_weather_data(city['lat'], city['lon'])
        if weather_data:
            weather_data['city'] = city['name']
            store_weather_data(weather_data)
            print(f"Weather data for {city['name']} stored successfully.")
        else:
            print(f"Failed to fetch weather data for {city['name']}.")