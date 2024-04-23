FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV OPENWEATHERMAP_API_KEY=YOUR_API_KEY
ENV MONGODB_URI=YOUR_MONGODB_URI

CMD ["python", "weatherDataCollect.py"]