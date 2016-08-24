class Equipamento():

    def __init__(self, nome):
        self.nome = nome
        self.estado = 0
        self.MA = "automatico"
        self.falha = 0

    def setMA(self, MA):
        self.MA = MA
        if self.MA == "automatico":
            print("{0} FOI CONFIGURADO(A) PARA O MODO AUTOMATICO".format(self.nome))
        elif self.MA == "manual":
            print("{0} FOI CONFIGURADO(A) PARA O MODO MANUAL".format(self.nome))

    def getEstado(self,estado):
        self.estado = estado
        if self.estado == 0:
            print("{0} ESTA DESLIGADO(A)".format(self.nome))
        elif self.estado == 1:
            print("{0} ESTA LIGADO(A)".format(self.nome))

    def getFalha(self,falha):
        self.falha = falha
        if self.falha == 0:
            print("{0} ESTA SEM FALHAS".format(self.nome))
        elif self.falha == 1:
            print("{0} ESTA COM FALHAS".format(self.nome))


class Bomba(Equipamento):

    def __init__(self,nome):
        self.nome = nome
        self.estado = 0
        self.MA = "automatico"
        self.falha = 0

class Chiller(Equipamento):

    def __init__(self,nome):
        self.nome = nome
        self.estado = 0
        self.MA = "automatico"
        self.falha = 0

class Valvula(Equipamento):

    def __init__(self,nome):
        self.nome = nome
        self.estado = 0
        self.MA = "automatico"
        self.falha = 0

class Fancoil(Equipamento):

    def __init__(self,nome):
        self.nome = nome
        self.estado = 0
        self.MA = "automatico"
        self.falha = 0
        self.temperatura = 0

    def getTemperatura(self,temperatura):
        self.temperatura = temperatura
        print("A TEMPERATURA DO {0} É {1}°C".format(self.nome,self.temperatura))

    def setTemperatura(self, temperatura):
        if self.MA == "manual":
            self.temperatura = temperatura
            print("A TEMPERATURA DO {0} FOI CONFIGURADA PARA {1}°C".format(self.nome,self.temperatura))
        elif self.MA == "automatico":
            self.temperatura = self.temperatura
            print("A TEMPERATURA NÃO PODE SER ALTERADA NO MODO AUTOMATICO")

#TESTED
#bomba1 = Chiller("Chiller 01")
#bomba1.setMA("automatico")
#bomba1.getEstado(0)
#bomba1.getFalha(1)

#bomba2 = Bomba("BAG02")
#bomba2.setMA("manual")
#bomba2.getEstado(1)
#bomba2.getFalha(0)
            
#fancoil1 = Fancoil("FAN01")
#fancoil1.getTemperatura(100)
#fancoil1.setMA("manual")
#fancoil1.setTemperatura(50)
