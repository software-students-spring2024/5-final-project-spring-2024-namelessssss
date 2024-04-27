document.getElementById('get-weather-btn').addEventListener('click', function() {
    var location = document.getElementById('location-input').value;

    // Check if the location is not empty
    if (!location) {
        alert('Please enter a location.');
        return;
    }
    fetch('/weather?location=' + location)
        .then(function(response) {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }

            return response.json();
        })
        .then(function(weatherData) {

            if (!weatherData || Object.keys(weatherData).length === 0) {
                throw new Error('No weather data available for this location');
            }

            document.getElementById('location').textContent = weatherData.location;
            document.getElementById('temperature').textContent = weatherData.temperature;
            document.getElementById('humidity').textContent = weatherData.humidity;
            document.getElementById('wind-speed').textContent = weatherData.windSpeed;
            document.getElementById('conditions').textContent = weatherData.conditions;

            document.getElementById('weather-box').style.display = 'block';
        })
        .catch(function(error) {

            console.error('There has been a problem with your fetch operation:', error);

            alert(error.message);
        });
});
