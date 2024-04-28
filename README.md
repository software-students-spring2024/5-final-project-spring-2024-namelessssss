[![Weater Data CI](https://github.com/software-students-spring2024/5-final-project-spring-2024-namelessssss/actions/workflows/weatherDataCollect.yml/badge.svg?branch=main)](https://github.com/software-students-spring2024/5-final-project-spring-2024-namelessssss/actions/workflows/weatherDataCollect.yml)
[![Web App CI](https://github.com/software-students-spring2024/5-final-project-spring-2024-namelessssss/actions/workflows/webApp.yml/badge.svg)](https://github.com/software-students-spring2024/5-final-project-spring-2024-namelessssss/actions/workflows/webApp.yml)

# Nameless Weather App

The Nameless Weather App is a web-based weather forecasting web-based application that utilizes OpenWeatherMap's API in order to collect real-time weather data.
Users may use the web application's user-friendly interface to select which major city they would like to retrieve weather information about and to select their preferred temperature unit.
The app then displays real-time information about the weather in that city, including its temperature, humidity, wind speed, and overall weather condition.

## System Architecture
The Nameless Weather App is made up of **two major subsystems**:

1. **Weather Data Collection Subsystem:** This subsystem is responsible for collecting real-time weather data from OpenWeatherMap's API. It fetches data such as temperature, humidity, wind speed, and weather condition. Then the data is stored in the MongoDB database.
> **insert link to container image for this custom subsystem hosted on dockerhub**

2. **Web Application Subsystem:** This subsystem is a web application that displays the real-time weather data fetched by the first subsystem. Users can select their location to receive the current weather information.
> **insert link to container image for this custom subsystem hosted on dockerhub**

# Instructions

## API Key Setup
1. Obtain an OpenWeatherMap API key by following these steps:
    - Log into your OpenWeatherMap API account and navigate to the [API keys](https://home.openweathermap.org/api_keys) page.
    -  Copy the generated API key
> *Note: the free tier of the subscription is sufficient for this application*

2. Insert the API key into the `Dockerfile` in the `weather-data-collect` directory.
    - Replace `API_KEY_HERE` with your OpenWeatherMap API key.
    - Save the changes.

## Running the Application with Docker

1. Open a terminal and navigate to the root folder of the project.
2. Run the command `docker-compose up --build` to build and start the application containers.

### Accessing the Web Application

1. Open a web browser and visit *what is the local host again lol* to access the Nameless Weather App web application.
2. From the first dropdown, select which major city you would like to retrieve weather data from. Then from the second, select which unit of temperature you would like to recieve the data in.
3. Click the Check Weather button to submit your request.
4. The application will display the real-time weather data for the selected city, including it's current temperature, humidity level, wind speed, and overall weather condition.
5. To get information about another city or update the information you already have to represent the current time, repeat steps 2-3 as needed.

## Testing
AHHHHHHHHH

# Contributors

- [Hannah Horiuchi](https://github.com/hah8236)
- [Jiahua Liao](https://github.com/Jiahuita)
- [Kevin Lin](https://github.com/Kalados)
- [Nicole Luzuriaga](https://github.com/nicjluz)



delete below:

An exercise to put to practice software development teamwork, subsystem communication, containers, deployment, and CI/CD pipelines. See [instructions](./instructions.md) for details.