import os
import requests
from flask import Flask, request, jsonify
from pymongo import MongoClient
from pymongo.server_api import ServerApi

app = Flask(__name__)

API_KEY = os.environ['OPENWEATHERMAP_API_KEY']
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather?'

def fetch_weather_data(city):
    url = BASE_URL + 'q=' + city + '&appid=' + API_KEY
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def convert_temperatures(weather_data):
    kelvin = weather_data['main']['temp']
    celsius = kelvin - 273.15
    fahrenheit = (kelvin - 273.15) * 9/5 + 32
    weather_data['main']['temp_kelvin'] = kelvin
    weather_data['main']['temp_celsius'] = round(celsius, 2)
    weather_data['main']['temp_fahrenheit'] = round(fahrenheit, 2)
    return weather_data

def store_weather_data(weather_data):
    client = MongoClient(os.environ['MONGODB_URI'], tls=True, tlsCertificateKeyFile=os.environ['SSL_CERT_FILE'], tlsAllowInvalidCertificates=True, server_api=ServerApi("1"))
    db = client[os.environ['DB_NAME']]
    collection = db[os.environ['DB_COLLECTION_NAME']]
    collection.insert_one(weather_data)
    client.close()

@app.route('/collect', methods=['POST'])
def collect_weather_data():
    city = request.json['city']
    weather_data = fetch_weather_data(city)
    if weather_data:
        weather_data = convert_temperatures(weather_data)
        weather_data['city'] = city
        store_weather_data(weather_data)
        return jsonify(status='success'), 200
    else:
        return jsonify(status='error'), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5030)