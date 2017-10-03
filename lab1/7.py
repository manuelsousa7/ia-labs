class p_aspirador_ex_7:

    def __init__(self, lixo):
        self.lixo = lixo

    def lixo(self):
        return self.lixo


p51 = p_aspirador_ex_7(True)
p52 = p_aspirador_ex_7(False)


def agente_aspirador_ex_7():
    def __init__(self):
        self.casaslimpas = 0

    def invoca(self,p):
        self.casaslimpas = 0
        if self.casaslimpas == 8:
            return "esperar"
        elif p.lixo():
            return "aspirar"
        else:
            self.casaslimpas = self.casaslimpas + 1
            return "andar"


a_e7 = agente_aspirador_ex_7()
a_e7.invoca(p51)
a_e7.invoca(p52)
