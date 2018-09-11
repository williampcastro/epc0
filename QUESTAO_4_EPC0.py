#  QUESTÃO 4

import numpy as np
import matplotlib.pyplot as plt
import math as m

# Exemplo de arquivo tipo script
# script1: desenha o grafico f(x) = sin(x)*exp(x), -2*pi < x < 2*pi

print("=================================QUESTÃO 4=================================\n")
pi = m.pi
x = np.arange(-2*pi,2*pi,0.1) #CRIA UM VETOR NO INTERVALO DE -2PI A 2PI INCREMENTANDO 0.1 A CADA ITERAÇÃO
prod =  np.sin(x)*np.exp(x) # MULTIPLICAÇÃO PONTO A PONTO DOS VETORES
plt.title('Gráfico exemplo') #INSERE UM TÍTULO NO GRÁFICO
plt.show(plt.plot(x,prod)) #PLOTA O GRÁFICO
