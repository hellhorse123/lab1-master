import pyowm

print('OpenWeatherMap')

owm = pyowm.OWM('68b920e3e70b4296b634f879a4b7f1d2')
observation = owm.weather_at_place('Moscow,ru')
weather = observation.get_weather()
location = observation.get_location()
translate = {'Rostov-na-Donu': 'Ростов-на-Дону','Moscow':'Москва'}

print(owm)
print(observation)
print(weather)
print(location)


print('Страна:' + location.get_country())
print('Город:' + location.get_name())
print('Долгота:' + str(location.get_lon()))
print('Широта:' + str(location.get_lat()))
print('Облачность:' + str(weather.get_clouds()))
print('Статус:' + str(weather.get_detailed_status()))
print('Давление:' + str(weather.get_pressure()))
print('Дождь:' + str(weather.get_rain()))
print('Снег:' + str(weather.get_snow()))
print('Время:' + str(weather.get_reference_time('date')))
print('Статус:' + str(weather.get_status()))
print('Восход:' + str(weather.get_sunrise_time('iso')))
print('Закат:' + str(weather.get_sunset_time('iso')))
print('Температура :' + str(weather.get_temperature('celsius')))
print('видимость:' + str(weather.get_visibility_distance()))
print('Изображение:' + weather.get_weather_icon_name())
print('Ветер:' + str(weather.get_wind()))

def WhatIsCloudness():
    if 0 <= weather.get_clouds() <= 10:
        return 'ясная'
    if 10 <= weather.get_clouds() <= 30:
        return 'немного облачная'
    if 30 <= weather.get_clouds() <= 70:
        return 'пасмурная'
    if 70 <= weather.get_clouds() <= 100:
        return 'мрачная'

print('Погода в городе ' + translate[location.get_name()] + ' на сегодня  '+ str(observation.get_reception_time('date'))
 + ' '+ WhatIsCloudness() + ' ,облачность составляет  '+ str(weather.get_clouds()) + '%, давление ' + str(weather.get_pressure()['press']) +
'мм рт.ст.,температура ' + str(weather.get_temperature('celsius')['temp']) + ' градусов Цельсия ' +' Днем:'+
str(weather.get_temperature('celsius')['temp_max']) + ' Ночью:' +
str(weather.get_temperature('celsius')['temp_min'])  + ' скорость ветра ' + str(weather.get_wind()['speed']) + ' м/с. ')