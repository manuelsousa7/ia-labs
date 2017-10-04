class agente_corredor_ex_9():
    def __init__(self):
        self.cur = 1

    def invoca(self,pos):
        if pos == 0:
            if(self.cur == 0):
                return "fica parado"
        if(self.cur > pos and self.cur > 1):
            self.cur = self.cur - 1
            return "andar-"
        if(self.cur < pos and self.cur < 8):
            self.cur = self.cur + 1
            return "andar+"
        return "espera"


asd = agente_corredor_ex_9()
print asd.invoca(5)
print asd.invoca(5)
print asd.invoca(5)
print asd.invoca(5)
print asd.invoca(5)
print asd.invoca(5)
print asd.invoca(5)
print asd.invoca(5)
print asd.invoca(5)
print asd.invoca(1)
print asd.invoca(5)
print asd.invoca(5)
print asd.invoca(5)