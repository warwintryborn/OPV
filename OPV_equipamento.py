class Equipamento():

    def __init__(self):
        self.nome = ""
        self.estado = 0
        self.MA = "Automatico"
        self.falha = 0
        self.comando = 0

    def setMA(self, MA):
        self.MA = MA

    def getMA(self):
        return self.MA


    def setComando(self, comando):
        self.comando = comando
        if self.falha == 1:
            self.estado = 0
        else:
            self.estado = self.comando
 
    def setFalha(self, falha):
        self.falha = falha

    def getEstado(self):
        return self.estado

    def getFalha(self):
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
