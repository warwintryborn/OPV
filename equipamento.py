class Equipamento():

    def __init__(self):
        self.nome = ""
        self.estado = 0
        self.MA = "automatico"
        self.falha = 0
        self.comando = 0

    def setMA(self, MA):
        self.MA = MA
        if self.MA == "automatico":
            print("{0} FOI CONFIGURADO(A) PARA O MODO AUTOMATICO".format(self.nome))
        elif self.MA == "manual":
            print("{0} FOI CONFIGURADO(A) PARA O MODO MANUAL".format(self.nome))

    def getMA(self):
        print(self.MA)
        return self.MA

    def setComando(self, comando):
        self.comando = comando
        self.estado = self.comando

    def getEstado(self):
        if self.estado == 0:
            print("{0} ESTA DESLIGADO(A)".format(self.nome))
        elif self.estado == 1:
            print("{0} ESTA LIGADO(A)".format(self.nome))
        return self.estado

    def getFalha(self):
        if self.falha == 0:
            print("{0} ESTA SEM FALHAS".format(self.nome))
        elif self.falha == 1:
            print("{0} ESTA COM FALHAS".format(self.nome))
        return self.falha


class Bomba(Equipamento):

    def __init__(self, nome):
        Equipamento.__init__(self)
        self.nome = nome
        
class Chiller(Equipamento):

    def __init__(self,nome):
        Equipamento.__init__(self)
        self.nome = nome

class Valvula(Equipamento):

    def __init__(self,nome):
        Equipamento.__init__(self)
        self.nome = nome

class Fancoil(Equipamento):

    def __init__(self,nome):
        Equipamento.__init__(self)
        self.nome = nome

    def setTemperatura(self, temperatura):
        self.temperatura = temperatura
        print("A TEMPERATURA DO {0} FOI CONFIGURADA PARA {1}°C".format(self.nome,self.temperatura))
        
    def getTemperatura(self):
        print("A TEMPERATURA DO {0} É {1}°C".format(self.nome,self.temperatura))
        return self.temperatura
