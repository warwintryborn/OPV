import pyowm


#API Keys:
#a1d13f8e215109d501c403227f68e3f6
#648e982872364f97bc4f3d40f32ba6c1

owm = pyowm.OWM('a1d13f8e215109d501c403227f68e3f6')



observation = owm.weather_at_place('SaoPaulo,br')
w = observation.get_weather()
print(w)

b = w.get_wind()                  # {'speed': 4.6, 'deg': 330}
w.get_humidity()              # 87
a = w.get_temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}

print(a)
print("")
print(b)

#REFERENCIA:
#https://github.com/csparpa/pyowm
#https://github.com/csparpa/pyowm/wiki/Usage-examples
