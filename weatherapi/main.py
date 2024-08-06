import requests
from pprint import pprint

API_key = 'a610e52aebd3a900ef37bcc1241214d8'

city = input("Enter a city: ")

base_url = "http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}"

weather_data = requests.get(base_url).json()

pprint(weather_data)
