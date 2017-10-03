class p_aspirador_ex_5:
    def __init__(self, moeda, n_moedas):
        self.moeda1 = moeda
        self.n_moedas1 = n_moedas

    def moeda(self):
        return self.moeda1

    def n_moedas(self):
        return self.n_moedas1

p51 = p_aspirador_ex_5(False, 5)
p52 = p_aspirador_ex_5(True, 5)
p53 = p_aspirador_ex_5(True, 50)


def agente_ensacador_ex_5(p):
    moeda = p.moeda()
    n_moedas = p.n_moedas()
    if not(moeda):
        print "esperar"
    elif n_moedas == 50:
        print "troca-saco-e-ensaca"
    else:
        print "ensaca"

agente_ensacador_ex_5(p51)
agente_ensacador_ex_5(p52)
agente_ensacador_ex_5(p53)
