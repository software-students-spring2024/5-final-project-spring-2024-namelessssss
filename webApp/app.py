import os
from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

MONGODB_URI = os.environ['MONGODB_URI']
DB_NAME = 'Project5'
COLLECTION_NAME = 'WeatherData'

client = MongoClient(MONGODB_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form['city']
        weather_data = collection.find_one({'city': city})
        if weather_data:
            return render_template('index.html', weather_data=weather_data)
        else:
            return render_template('index.html', error='Weather data not found for the selected city.')
    else:
        cities = collection.distinct('city')
        return render_template('index.html', cities=cities)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)