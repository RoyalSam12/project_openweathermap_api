from django.urls import path, include
from .views import index, weather_page

app_name = 'weather'
urlpatterns = [
    path('', index, name='index'),
    path('weather/<str:city>', weather_page, name='weather_page')
]
