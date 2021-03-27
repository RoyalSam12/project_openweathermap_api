from django import template
from django.utils.safestring import mark_safe

register = template.Library()

CARD_HEAD = '''
            <div class="card bg-dark" style="width: 18rem;">
                <img src="{}" class="card-img-top">
                <div class="card-body">
                    <table class="table">
                        <tbody>
            '''

CARD_TAIL = '''     
                        <tbody>
                    </table>
                </div>
            </div>    
            '''

TABLE_CONTENT = """
                <tr>
                    <td class='text-white'>{name}</td>
                    <td class='text-white'>{value}</td>
                </tr>
                """

translate_info = {
    'weather_id': 'id',
    'weather_description': 'Описание',
    'temp': 'Температура',
    'temp_feels': 'Чувствуется',
    'tem_max': 'Максимальная температура',
    'humidity': 'Влажность',
    'wind_speed': 'Скорость ветра(км)',
    'city_name': 'Название города',
}

@register.filter
def weather_card(city_info):
    table_content = ''
    for key, value in city_info.items():
        table_content += TABLE_CONTENT.format(name=translate_info[key], value=value)
    return mark_safe(CARD_HEAD + table_content + CARD_TAIL)
