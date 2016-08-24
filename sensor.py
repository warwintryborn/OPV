#API Keys:
#a1d13f8e215109d501c403227f68e3f6
#648e982872364f97bc4f3d40f32ba6c1

import pyowm

class Sensor():
    
    def __init__(self, localizacao):
        self.localizacao = localizacao
        self.owm = pyowm.OWM('a1d13f8e215109d501c403227f68e3f6')
        self.observation = self.owm.weather_at_place(self.localizacao)
        self.w = self.observation.get_weather()
        self.temperatura = self.w.get_temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
        self.date = pyowm.utils.timeutils.now(timeformat='date')
        
    def tempValor(self):
        self.temperaturaValor = self.temperatura['temp']
        print(self.temperaturaValor)
        
    def tempMax(self):
        self.temperaturaMax = self.temperatura['temp_max']
        print(self.temperaturaMax)
        
    def tempMin(self):
        self.temperaturaMin = self.temperatura['temp_min']
        print(self.temperaturaMin)
        
    def humidade(self):
        self.humidade = self.w.get_humidity()
        print(self.humidade)

    def horario(self):
        print(self.date)

sensor1 = Sensor('SaoPaulo,br')
sensor1.tempValor()
sensor1.tempMax()
sensor1.tempMin()
sensor1.humidade()
sensor1.horario()
