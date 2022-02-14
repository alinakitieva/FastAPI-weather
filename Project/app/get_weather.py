import requests

from fastapi import HTTPException
from app.config import settings

API_KEY = settings.appid
if API_KEY is None:
    raise ValueError("Please provide API-key for OpenWeather")
# change maybe


def get_weather_by_params(city, country_code, date_time):
    def get_temperature_from_data(data):
        for obj in data['list']:
            if obj['dt_txt'] == date_time:
                temperature = obj['main']['temp']
                return temperature
    country_code = country_code.upper()
    url = 'http://api.openweathermap.org/data/2.5/forecast'
    params = {
        'q': (city, country_code),
        'appid': API_KEY,
        'units': 'metric',
        'lang': 'ru'
    }
    response = requests.get(url, params=params)
    if response.status_code == 404:
        raise HTTPException(status_code=404,
                            detail=f"Not found weather with params {(city,country_code)}")
    data = response.json()
    date_time = date_time.strftime('%Y-%m-%d %H:%M:%S')
    #
    try:
        return get_temperature_from_data(data)
    except KeyError:
        raise HTTPException(status_code=500,
                            detail="Impossible to retrieve data from OpenWeather API")
