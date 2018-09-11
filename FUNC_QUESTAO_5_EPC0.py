#  QUESTÃO 4

import numpy as np
import matplotlib.pyplot as plt
import math as m

def chart(start,end,interval):
    x = np.arange(start,end,interval) #CRIA UM VETOR NO INTERVALO DE -2PI A 2PI INCREMENTANDO 0.1 A CADA ITERAÇÃO
    prod =  np.sin(x)*np.exp(x) # MULTIPLICAÇÃO PONTO A PONTO DOS VETORES
    plt.title('Gráfico exemplo - II') #INSERE UM TÍTULO NO GRÁFICO
    plt.show(plt.plot(x,prod)) #PLOTA O GRÁFICO
