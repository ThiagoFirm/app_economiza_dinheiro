from interface import *


def calcular(): 
    # obtendo renda mensal
    renda_mensal = float(entry1.get())
    
    obter50porcento = (50/100) * renda_mensal
    obter30porcento = (30/100) * renda_mensal
    obter20porcento = (20/100) * renda_mensal

    total_necessidades("R$: ", obter50porcento)
    total_gastos("R$: ", obter30porcento)
    total_lazer("R$: ", obter20porcento)
