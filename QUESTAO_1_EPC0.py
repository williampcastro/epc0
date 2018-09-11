# # QUESTÃO 1

import numpy as np

x = np.array([-1.3, np.sqrt(3), (1+2+3)*4/5])

print("=================================QUESTÃO 1=================================\n")
print("\nLETRA A")
print("x = ", x)

print("\nLETRA B")
x = np.insert(x,3,abs(x[1]))
print("x = ", x)

y = np.array([1,2,3,4])

print("\nLETRA C")
print("y = ",y)

print("\nLETRA D")
print("\ni")
print("x+y = ",x+y)

print("\nii")
print("x-y = ",x-y)

yTransp = y.transpose()
print("\niii")
print("y` = ", yTransp)

print("\niv")
print("x*y = ",x*y)

print("\nv")
print("x*y` = ",x*yTransp)

print("\nvi")
print("x.*y = ",np.dot(x,y))

print("\nvii")
print("x./y = ",np.divide(x,y))

print("\nviii")
print("x.^y = ",np.power(x, y))

print("\nx")
print(" [x y]= ",np.concatenate((x,y), axis=0))