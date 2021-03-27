from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from . models import WeatherImage
from .forms import CityForm
from .weather_scripts import CityWeather, compress_information_from_request


def weather_page(requests, city):
    """
    Функция возращает страницу с информацией о погодных условиях в нужном Городе
    """

    custom_city = CityWeather(city)  # Создаем экземпля Класса
    res = custom_city.request_weather()  # Делаем запрос по Api и получаем response
    compress_res = compress_information_from_request(res) # Собираем всю информацию из запроса в словарь
    context = {
        'data': compress_res,  # Передаем инфу в HTML
        'image': WeatherImage.objects.get(id=compress_res['weather_id']).image.url  # Берем с бд фото соотвенно с id
    }  # Словарь context с нужной для нас информацией который мы используем для заполнения html страницы
    return render(requests, template_name='weather/weather_page.html', context=context)


def index(request):
    """
    Функция возращает стартовую страницу на которой мы можем внести названия необходимого нам города.
    """

    if request.method == "POST":  # Прорека на метод request
        form = CityForm(request.POST)
        if form.is_valid():  # В случае перевед на страницу с информацией о погоде в нужном Городе
            return HttpResponseRedirect(reverse('weather:weather_page', kwargs={'city': form.cleaned_data['city']}))

    """
    Если request будет иметь метод POST и форма будет "Валидна" то он перестанет интерпитировать
    дальше по функции и вернет HttpResponseRedirect в противном случае код пропустит 'if' 
    и продолжит интерпитировать код
    """

    context = {
        'form': CityForm()  # Пустая форма для информации
    }
    return render(request, template_name='weather/index.html', context=context)
