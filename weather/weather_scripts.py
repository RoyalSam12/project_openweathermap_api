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
        'weather_id': res['weather'][0]['id'],  # Id Погоды (Нужно для визуализации статуса погоды)
        'weather_description': res['weather'][0]['description'],  # Описание погоды
        'temp': res['main']['temp'],  # Температура на улице
        'temp_feels': res['main']['feels_like'],  # То как температура чувствуется
        'tem_max': res['main']['temp_max'],  # Максимальная температура за день
        'humidity': res['main']['humidity'],  # Влажность
        'wind_speed': res['wind']['speed'],  # Скорость Ветра
        'city_name': res['name']  # Название города
    }

    return info  # Возращаем словарь со значениями


if __name__ == '__main__':
    kiev_weather = request_weather(city='Kiev')  # Проверяем работу первой функции

    if kiev_weather:
        print(compress_information_from_request(kiev_weather))  # Функция прошла удачно и мы получаем результат второй
    else:
        print('Что-то пошло не так')
