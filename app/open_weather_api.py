import os
import requests

from fastapi import HTTPException

OPEN_WEATHER_API_KEY = os.getenv("OPEN_WEATHER_API_KEY")
if OPEN_WEATHER_API_KEY is None:
    raise ValueError('Please, provide API-key for OpenWeather')


def validate_params(city, country_code):
    def is_valid_by_data(data):
        for obj in data:
            if obj['name'] == city and obj['country'] == country_code:
                return True
        return False

    url = 'http://api.openweathermap.org/geo/1.0/direct'
    params = {
        'q': (city, country_code),
        'appid': OPEN_WEATHER_API_KEY,
        'lang': 'ru'
    }
    response = requests.get(url, params=params)
    if response.status_code == 404:
        raise HTTPException(status_code=400, detail=f'Not found weather with params: {(city, country_code)}')

    data = response.json()
    if not is_valid_by_data(data):
        raise HTTPException(status_code=400, detail=f'Invalid data: `city`={city}, `country_code`={country_code}')


def get_temperature_by_params(city, country_code, date_time):
    def get_temperature_from_data(data):
        """Find the closest temperature for city with country_code"""
        temperature = None
        if data['city']['name'] == city and data['city']['country'] == country_code:
            for obj in data['list']:
                if date_time <= obj['dt']:
                    temperature = obj['main']['temp']
        return temperature

    url = 'http://api.openweathermap.org/data/2.5/forecast'
    params = {
        'q': (city, country_code),
        'appid': OPEN_WEATHER_API_KEY,
        'units': 'metric',
    }
    response = requests.get(url, params=params)
    if response.status_code == 404:
        raise HTTPException(status_code=400, detail=f'Not found weather with params: {(city, country_code)}')

    data = response.json()
    date_time = date_time.timestamp()

    try:
        temperature = get_temperature_from_data(data)
    except KeyError:
        raise HTTPException(status_code=500, detail=f'Impossible to retrieve data from OpenWeather API')

    if temperature is None:
        raise HTTPException(status_code=400, detail=f'Invalid data: `city`={city}, `country_code`={country_code}')

    return temperature
