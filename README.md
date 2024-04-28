[![Weater Data CI](https://github.com/software-students-spring2024/5-final-project-spring-2024-namelessssss/actions/workflows/weatherDataCollect.yml/badge.svg?branch=main)](https://github.com/software-students-spring2024/5-final-project-spring-2024-namelessssss/actions/workflows/weatherDataCollect.yml)
[![Web App CI](https://github.com/software-students-spring2024/5-final-project-spring-2024-namelessssss/actions/workflows/webApp.yml/badge.svg)](https://github.com/software-students-spring2024/5-final-project-spring-2024-namelessssss/actions/workflows/webApp.yml)

# Nameless Weather App

The Nameless Weather App is a web-based weather forecasting web-based application that utilizes OpenWeatherMap's API in order to collect real-time weather data.
Users may use the web application's user-friendly interface to select which major city they would like to retrieve weather information about and to select their preferred temperature unit.
The app then displays real-time information about the weather in that city, including its temperature, humidity, wind speed, and overall weather condition.

## Subsystems
The Nameless Weather App is made up of two main subsystems:

1. **Weather Data Collection Subsystem:** This subsystem is responsible for collecting real-time weather data from OpenWeatherMap's API. It fetches data such as temperature, humidity, wind speed, and weather condition. Then the data is stored in the MongoDB database.

2. **Web Application Subsystem:** This subsystem is a web application that displays the real-time weather data fetched by the first subsystem. Users can select their location to receive the current weather information.

delete below:

An exercise to put to practice software development teamwork, subsystem communication, containers, deployment, and CI/CD pipelines. See [instructions](./instructions.md) for details.

# Instructions

wait that might not be necessary... hold on.

## API Key Setup
1. Obtain an OpenWeatherMap API key by following these steps:
    - Log into your OpenWeatherMap API account and navigate to the [API keys](https://home.openweathermap.org/api_keys) page.
    -  Copy the generated API key
> *Note: the free tier is sufficient for this application*

2. Insert the API key into the `Dockerfile` in the `weather-data-collect` directory.
    - Replace `API_KEY_HERE` with your OpenWeatherMap API key.
    - Save the changes.


**instructions for how to configure and run all parts of your project for any developer on any platform - these instructions must work!**

**instructions for how to set up any environment variables and import any starter data into the database, as necessary, for the system to operate correctly when run.**

in the weather-data-collect dockerfile, eplace the "API KEY HERE" with your Open Weather Map API key. 
You can make 


** links to the container images for each custom subsystem hosted on dockerhub**


## Contributors

- [Hannah Horiuchi](https://github.com/hah8236)
- [Jiahua Liao](https://github.com/Jiahuita)
- [Kevin Lin](https://github.com/Kalados)
- [Nicole Luzuriaga](https://github.com/nicjluz)