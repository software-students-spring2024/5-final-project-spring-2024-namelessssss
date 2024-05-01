FROM python:3.12-slim

WORKDIR /weather-data-collect

COPY requirements.txt .
COPY X509-cert-4588623656805667932.pem .

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5030

CMD ["python", "weatherDataCollect.py"]