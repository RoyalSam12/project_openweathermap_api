import json

import requests
from decouple import config


def request_weather(city):
    """Функция делает request и возращает response из API openweathermap.org
    в случае если ответом не будет ошибка 404"""

    params = {
        'q': city,  # Город
        'appid': str(config('API_KEY_OPEN_WEATHER')),  # API KEY необходимий для работы запроса на сервер
        'units': 'metric',  # Указываем что хотим получить измерение в Цельсиях
        'lang': 'ru'  # Язык
    }
    re = requests.get('http://api.openweathermap.org/data/2.5/weather', params=params)  # Запрос на сервер
    if re.status_code == '404':
        return False
    return re


def compress_information_from_request(response):
    """Функция возращает Словарь с необходимой информацией, информацию получаем через индексирование"""

    res = response.json()  # Используем метод json() для получения информации из response

    info = {
        'weather_id': res['weather'][0]['id'],
        'weather_description': res['weather'][0]['description'],
        'temp': res['main']['temp'],
        'temp_feels': res['main']['feels_like'],
        'tem_max': res['main']['temp_max'],
        'humidity': res['main']['humidity'],
        'wind_speed': res['wind']['speed'],
        'city_name': res['name']
    }

    return info  # Возращаем словарь со значениями


if __name__ == '__main__':
    kiev_weather = request_weather(city='Kiev')  # Проверяем работу первой функции

    if kiev_weather:
        print(compress_information_from_request(kiev_weather))  # Функция прошла удачно и мы получаем результат второй
    else:
        print('Что-то пошло не так')
