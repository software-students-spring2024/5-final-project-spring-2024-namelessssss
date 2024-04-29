FROM python:3.12-slim

WORKDIR /weather-data-collect

COPY requirements.txt .
COPY X509-cert-4588623656805667932.pem .

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

ENV OPENWEATHERMAP_API_KEY=a8fb5351db81858ed5e57093a90b5a5d
ENV MONGODB_URI=mongodb+srv://nameless.wun5lpq.mongodb.net/?authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority&appName=Nameless
ENV DB_NAME=Project5
ENV DB_COLLECTION_NAME=WeatherData
ENV SSL_CERT_FILE=X509-cert-4588623656805667932.pem

EXPOSE 5030

CMD ["python", "weatherDataCollect.py"]