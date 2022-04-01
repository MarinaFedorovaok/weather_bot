#!/usr/bin/python3
import requests

params = {
    'latitude': '52.52',
    'longitude': '13.41',
    'hourly': 'temperature_2m',
}

response = requests.get('https://api.open-meteo.com/v1/forecast', params=params)
data = response.json()

print(data["hourly"]['time'])
print(data["hourly"]['temperature_2m'])

