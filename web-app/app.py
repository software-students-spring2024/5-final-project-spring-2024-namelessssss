import os
import requests
from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
from pymongo.server_api import ServerApi

app = Flask(__name__)

client = MongoClient(os.environ['MONGODB_URI'], tls=True, tlsCertificateKeyFile=os.environ['SSL_CERT_FILE'], server_api=ServerApi("1"))
db = client[os.environ['DB_NAME']]
collection = db[os.environ['DB_COLLECTION_NAME']]

@app.route('/', methods=['GET', 'POST'])
def index():
    cities = ['New York', 'Boston', 'Washington, D.C.', 'Miami']
    temp_units = ['Kelvin', 'Celsius', 'Fahrenheit']
    selected_city = request.form.get('city', cities[0])
    selected_unit = request.form.get('temp_unit', temp_units[0])

    if request.method == 'POST':
        city = selected_city
        temp_unit = selected_unit

        response = requests.post('http://weather-data-collect:5030/collect', json={'city': city})

        weather_data = collection.find_one({'city': city}, sort=[('_id', -1)])
        if weather_data:
            return render_template('index.html', cities=cities, temp_units=temp_units, weather_data=weather_data, selected_unit=temp_unit, selected_city=selected_city)
        else:
            return render_template('index.html', cities=cities, temp_units=temp_units, error='Weather data not found for the selected city.', selected_unit=selected_unit, selected_city=selected_city)
    else:
        return render_template('index.html', cities=cities, temp_units=temp_units, selected_unit=selected_unit, selected_city=selected_city)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)