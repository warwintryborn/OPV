import pyowm

owm = pyowm.OWM('a1d13f8e215109d501c403227f68e3f6')

#API Keys:
#a1d13f8e215109d501c403227f68e3f6
#648e982872364f97bc4f3d40f32ba6c1


observation = owm.weather_at_place('SaoPaulo,br')
w = observation.get_weather()
print(w)
print('')

print(w.get_reference_time(timeformat='iso'))
print(pyowm.utils.timeutils.now(timeformat='date'))

hora = pyowm.utils.timeutils.now(timeformat='date')

#pyowm.utils.timeutils.now(timeformat='date')

temperatura = w.get_temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
humidade = w.get_humidity()


temperaturaMax = temperatura['temp_max']
temperaturaMin = temperatura['temp_min']
temperaturaValor = temperatura['temp']

print(temperaturaMax)
print(temperaturaMin)
print(temperaturaValor)
print(humidade)

#{'temp_kf': None, 'temp': 17.11, 'temp_max': 26.11, 'temp_min': 12.78}

#REFERENCIA:
#https://github.com/csparpa/pyowm
#https://github.com/csparpa/pyowm/wiki/Usage-examples
