class agente :
    

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
