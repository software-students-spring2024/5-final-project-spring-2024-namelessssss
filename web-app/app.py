import os
from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
from pymongo.server_api import ServerApi

app = Flask(__name__)

client = MongoClient(os.environ['MONGODB_URI'], tls=True, tlsCertificateKeyFile=os.environ['SSL_CERT_FILE'], server_api=ServerApi("1"))
db = client[os.environ['DB_NAME']]
collection = db[os.environ['DB_COLLECTION_NAME']]

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
        # Pass an empty dictionary as weather_data if it's a GET request
        return render_template('index.html', cities=cities, weather_data={})

@app.route('/weather')
def weather():
    location = request.args.get('location')
    weather_data = collection.find_one({'city': location})
    if weather_data:
        return jsonify(weather_data)
    else:
        return jsonify(error='Weather data not found for the selected location.'), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)
