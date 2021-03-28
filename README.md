# project_openweathermap_api

Проект основанный  на использование OpenWeatherMapApi.

Представляет из себя сайт при помощи которого вы можете узнать погоду в интересующем вас городе.
Проект открыт для доработки и является каркасом для дальнейшего дополнения функционала.

Чтобы начать начать свою работу с проектом вам нужно:

1. Открыть вашу рабочую директорию или создать ее.

- C:\Users\User> mkdir working_directory
- C:\Users\User> cd working_directory

2. Скопировать данный репозиторий при помощи команады git clone.

- git clone https://github.com/RoyalSam12/project_openweathermap_api.git

3. Перейти в папку с проектом и создать виртуальное окружение.

- C:\Users\User\working_directory> cd project_openweathermap_api
- C:\Users\User\ee\project_openweathermap_api>python -m venv env 

4. Активируем виртуальное окружение(venv/Scripts/activate) и устанавливаем нужные модули..

- C:\Users\User\ee\project_openweathermap_api> pip install -r requirements.txt

5. Делаем миграции и запускам сервер.

- C:\Users\User\ee\project_openweathermap_api> py manage.py makemigrations 
- C:\Users\User\ee\project_openweathermap_api> py manage.py migrate
- C:\Users\User\ee\project_openweathermap_api> py manage.py runserver
