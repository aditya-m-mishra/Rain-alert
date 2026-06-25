import requests

OWM_ENDPOINT = "http://api.openweathermap.org/data/2.5/forecast"
api_key = '29c88146bfaf49e2964447caefeb87c2'

weather_params = {
    "lat": 30.704649,
    "lon": 76.717873,
    "appid": api_key
}

response = requests.get(OWM_ENDPOINT, params=weather_params)
print(response.status_code)

print(response.json())