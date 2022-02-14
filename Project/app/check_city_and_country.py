import requests
from fastapi import HTTPException
from app.config import settings

API_KEY = settings.appid


def check_city_and_country(city, country_code):
    country_code = country_code.upper()
    url = 'http://api.openweathermap.org/geo/1.0/direct'
    params = {
        'q': city,
        'appid': API_KEY,
    }
    response = requests.get(url, params=params)
    data = response.json()
    if data[0]["country"] == country_code:
        return True
    raise HTTPException(status_code=404,
                        detail=f"Not found weather with params {(city, country_code)}. Check the correctness of the entered data")

