#API Keys:
#a1d13f8e215109d501c403227f68e3f6
#648e982872364f97bc4f3d40f32ba6c1

import pyowm

class sensorWeb():
        
    def __init__(self, localizacao): #INICIALIZA O OBJETO/CLASSE COM AS CONEXÕES COM O openweathermap.org   
        self.localizacao = localizacao #LOCALIZAÇÃO A SER DEFINIDA QUANDO CHAMAR A CLASSE, EXEMPLO: 'SaoPaulo,br'
        self.owm = pyowm.OWM('648e982872364f97bc4f3d40f32ba6c1') #UTILIZAR UMA DAS API KEYS QUE ESTA COMENTANDO NO INICIO DO CODIGO
        self.observation = self.owm.weather_at_place(self.localizacao)
        self.w = self.observation.get_weather()
        self.temperatura = self.w.get_temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0} - FORMATO DA BIBLIOTECA
        self.statusWeb = self.w.get_detailed_status()
        self.wind = self.w.get_wind()
        self.date = pyowm.utils.timeutils.now(timeformat='date')

    def getLocalizacao(self):
        return self.localizacao

    def getWind(self):
        self.vento = float(self.wind['speed'])
        self.vento = self.vento * 3.6
        return ("%.2f" % self.vento)
    
    def getTempValor(self): #EXIBE A TEMPERATURA ATUAL DO LOCAL
        self.temperaturaValor = self.temperatura['temp']
        return self.temperaturaValor
        
    def getTempMax(self): #EXIBE A TEMPERATURA MAXIMA DO LOCAL
        self.temperaturaMax = self.temperatura['temp_max']
        return self.temperaturaMax
        
    def getTempMin(self): #EXIBE A TEMPERATURA MINIMA DO LOCAL
        self.temperaturaMin = self.temperatura['temp_min']
        return self.temperaturaMin

    def getStatus(self):
        if (self.statusWeb == 'clear sky'):
            self.status = 'Céu limpo'
        elif (self.statusWeb == 'few clouds'):
            self.status = 'Algumas nuvens'
        elif (self.statusWeb == 'scattered clouds'):
            self.status = 'Nuvens dispersas'
        elif (self.statusWeb == 'broken clouds'):
            self.status = 'Nuvens precipitadas'
        elif (self.statusWeb == 'shower rain'):
            self.status = 'Pancadas de chuva'
        elif (self.statusWeb == 'rain'):
            self.status = 'Chuva'
        elif (self.statusWeb == 'thunderstorm'):
            self.status = 'Tempestade'
        elif (self.statusWeb == 'mist'):
            self.status = 'Névoa'
        return self.status
        
    def getUmidade(self): #EXIBE A UMIDADE DO LOCAL
        self.umidade = self.w.get_humidity()
        return self.umidade

    def getDate(self): #EXIBE O HORARIO E A DATA (NOW) - EXEMPLO: 2016-08-24 09:06:11.376690
        return self.date.replace(microsecond=0) #EXIBE O HORARIO COM OS MILISEGUNDOS = 0 - EXEMPLO: 2016-08-24 09:12:23

    def getHora(self): #EXIBE A HORA
        return self.date.strftime("%H")

    def getMinuto(self): #EXIBE O MINUTO
        return self.date.strftime("%M")
        
    def getSegundo(self): #EXIBE O SEGUNDO
        return self.date.strftime("%S")

    def getAno(self): #EXIBE O ANO
        return self.date.strftime("%Y")

    def getMes(self): #EXIBE O MES
        return self.date.strftime("%m")

    def getDia(self): #EXIBE O DIA
        return self.date.strftime("%d")


#REFERENCIAS
#https://github.com/csparpa/pyowm
#https://github.com/csparpa/pyowm/wiki/Usage-examples
