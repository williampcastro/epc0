#  QUESTÃO 3

import numpy as np
import matplotlib.pyplot as plt
import math as m

v3 = np.random.rand(1000)
print("\nLETRA A")
print("v3 = ", v3)

md = np.average(v3)
dv = np.std(v3)
print("\nLETRA B")
print("Média de V3 = ", md)
print("Desvio Padrão de V3 = ", dv)

pi = m.pi
x = np.linspace(0.0, 2*pi)
print("\nLETRA C")
print("x = ", x)
y = np.sin(x)
print("y = ", y)

plt.show(plt.plot(x, y))

