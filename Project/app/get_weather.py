import requests


def get(city, country_code, date_time):
    country_code = country_code.upper()
    url = 'http://api.openweathermap.org/data/2.5/forecast'
    params = {
        'q': (city, country_code),
        'appid': 'e8254b56019f6c404ceecd4e5415e511',
        'units': 'metric',
        'lang': 'ru'
    }
    data = requests.get(url, params=params).json()
    if data['cod'] == "404":
        return
    date_time = date_time.strftime('%Y-%m-%d %H:%M:%S')

    for i in data['list']:
        if i['dt_txt'] == date_time:
            temp = i['main']['temp']
            return temp

    return data
