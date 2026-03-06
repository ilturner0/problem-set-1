'''
PART 1: EXTRACT WEATHER AND TRANSIT DATA

Pull in data from two dataset
1. Weather data from visualcrossing's weather API (https://www.visualcrossing.com/weather-api)
- You will need to sign up for a free account to get an API key
-- You only get 1000 rows free per day, so be careful to build your query correctly up front
-- Though not best practice, include your API key directly in your code for this assignment
- Write code below to get weather data for Chicago, IL for the date range 10/1/2024 - 10/31/2025
- The default data fields should be sufficient
2. Daily transit ridership data for the Chicago Transit Authority (CTA)
- Here is the URL: ttps://data.cityofchicago.org/api/views/6iiy-9s97/rows.csv?accessType=DOWNLOAD"

Load both as CSVs into /data
- Make sure your code is line with the standards we're using in this class 
'''

#Write your code below
import requests
import io
import pandas as pd


# Extract visual crossing weather data for Chicago, IL
def extract_weather_data():
    weather = requests.get('https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Chicago,IL/2024-10-01/2025-10-31?key=SC8HPQU85E2XPGK86BGW7U2TQ&contentType=csv&include=days')
    weatherStr = io.StringIO(weather.text, newline='')
    weatherTab = pd.read_csv(weatherStr)
    weatherTab.to_csv(r'src/data/weather.csv')
    return weatherTab



# Extract CTA transit ridership data
def extract_transit_data():
    transit = requests.get('https://data.cityofchicago.org/api/views/6iiy-9s97/rows.csv?accessType=DOWNLOAD')
    transitStr = io.StringIO(transit.text, newline='')
    transitTab = pd.read_csv(transitStr)
    transitTab.to_csv(r'src/data/transit.csv')
    return transitTab