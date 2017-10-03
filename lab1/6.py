class p_anel_ex_6:
    def __init__(self, n):
        self.n = n

    def num(self):
        return self.n


p51 = p_anel_ex_6(0)
p52 = p_anel_ex_6(5)
p53 = p_anel_ex_6(50)


def agente_anel_ex_6(p):
    n = p.num()
    if(n == 0):
        print "esperar"
    else:
        print "andar"

agente_anel_ex_6(p51)
agente_anel_ex_6(p52)
agente_anel_ex_6(p53)