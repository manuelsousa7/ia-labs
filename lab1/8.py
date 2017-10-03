
def mod(a,b):
    return a%b

class p_objetivo_ex_8:
    def __init__(self, pos):
        self.posicao1 = pos

    def posicao(self):
        return self.posicao1


p1 = p_objetivo_ex_8(4)

pG = 0

def agente_anda_ex_8(p):
    global pG
    pp = p.posicao()
    if pG > pp:
        pG = mod(pG+11,10)
        return "anda-"
    elif pG < pp:
        pG = mod(pG+9,10)
        return "anda+"
    else:
        return "espera"


print agente_anda_ex_8(p1)
