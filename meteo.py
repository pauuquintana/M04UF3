#!/usr/bin/python3

import requests

url = "https://api.open-meteo.com/v1/forecast?latitude=41.4&longitude=2.12&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"

weather_enti = requests.get(url)

temp = data['current']['temperature_2m']
units = data['current_units']['temperature_2m']


print(f"La temperatura en ENTI es de: \{temp} {units} ")




