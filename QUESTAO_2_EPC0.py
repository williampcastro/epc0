# # QUESTÃO 2

import numpy as np

x = np.arange(0, 10, 2)

print("=================================QUESTÃO 2===============================\n")
print("\nLETRA A")
print("x = ", x)

y = np.arange(0, 5, 1)
print("\nLETRA B")
print("y = ", y)

v = np.concatenate((x,y), axis=0)
print("\nLETRA C")
print("v = ", v)
print("dimensions of v = ", v.shape)

v2 = np.linspace(0.,10.,6)
print("\nLETRA D")
print("v2 = ", v2)


