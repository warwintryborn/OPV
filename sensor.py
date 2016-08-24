#API Keys:
#a1d13f8e215109d501c403227f68e3f6
#648e982872364f97bc4f3d40f32ba6c1

import pyowm

class Sensor():
        
    def __init__(self, localizacao): #INICIALIZA O OBJETO/CLASSE COM AS CONEXÕES COM O openweathermap.org   
        self.localizacao = localizacao #LOCALIZAÇÃO A SER DEFINIDA QUANDO CHAMAR A CLASSE, EXEMPLO: 'SaoPaulo,br'
        self.owm = pyowm.OWM('a1d13f8e215109d501c403227f68e3f6') #UTILIZAR UMA DAS API KEYS QUE ESTA COMENTANDO NO INICIO DO CODIGO
        self.observation = self.owm.weather_at_place(self.localizacao)
        self.w = self.observation.get_weather()
        self.temperatura = self.w.get_temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0} - FORMATO DA BIBLIOTECA
        self.date = pyowm.utils.timeutils.now(timeformat='date')
        
    def tempValor(self): #EXIBE A TEMPERATURA ATUAL DO LOCAL
        self.temperaturaValor = self.temperatura['temp']
        print(self.temperaturaValor)
        
    def tempMax(self): #EXIBE A TEMPERATURA MAXIMA DO LOCAL
        self.temperaturaMax = self.temperatura['temp_max']
        print(self.temperaturaMax)
        
    def tempMin(self): #EXIBE A TEMPERATURA MINIMA DO LOCAL
        self.temperaturaMin = self.temperatura['temp_min']
        print(self.temperaturaMin)
        
    def humidade(self): #EXIBE A HUMIDADE DO LOCAL
        self.humidade = self.w.get_humidity()
        print(self.humidade)

    def horario(self): #EXIBE O HORARIO E A DATA (NOW) - EXEMPLO: 2016-08-24 09:06:11.376690
        print(self.date.replace(microsecond=0)) #EXIBE O HORARIO COM OS MILISEGUNDOS = 0 - EXEMPLO: 2016-08-24 09:12:23

    def hora(self): #EXIBE A HORA
        print(self.date.strftime("%H"))

    def minuto(self): #EXIBE O MINUTO
        print(self.date.strftime("%M"))
        
    def segundo(self): #EXIBE O SEGUNDO
        print(self.date.strftime("%S"))

    def ano(self): #EXIBE O ANO
        print(self.date.strftime("%Y"))

    def mes(self): #EXIBE O MES
        print(self.date.strftime("%m"))

    def dia(self): #EXIBE O DIA
        print(self.date.strftime("%d"))


#TESTES
#sensor1 = Sensor('SaoPaulo,br')
#sensor1.tempValor()
#sensor1.tempMax()
#sensor1.tempMin()
#sensor1.humidade()
#sensor1.horario()
#sensor1.hora()
#sensor1.minuto()
#sensor1.segundo()
#sensor1.ano()
#sensor1.mes()
#sensor1.dia()

#REFERENCIAS
#https://github.com/csparpa/pyowm
#https://github.com/csparpa/pyowm/wiki/Usage-examples
