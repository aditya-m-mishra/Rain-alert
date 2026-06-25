import requests

OWM_ENDPOINT = "http://api.openweathermap.org/data/2.5/forecast"
api_key = '29c88146bfaf49e2964447caefeb87c2'

weather_params = {
    "lat": 30.704649,
    "lon": 76.717873,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWM_ENDPOINT, params=weather_params)


response.raise_for_status()
print(response.status_code)

weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = (hour_data["weather"][0]["id"])
    if int(condition_code)<700:
        will_rain = True

if will_rain:
    print("bring an umbrella")
