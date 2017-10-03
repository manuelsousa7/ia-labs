def agente_corredor_ex_9():
    def __init__(self):
        self.casaslimpas = 0
        self.cur = 1

    def invoca(self,p):
        if p == 0:
            if(self.cur == 0):
                return "fica parado"
        if(self.cur > p and self.cur > 1):
                self.cur = self.cur - 1
                return "andar-"
        if(self.cur < p and self.cur < 8):
                self.cur = self.cur + 1
                return "andar+"

a_e7 = agente_corredor_ex_9()
a_e7.invoca(4)
a_e7.invoca(8)
