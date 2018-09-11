#  QUESTÃO 6

import numpy as np
import matplotlib.pyplot as plt
import math as m

def FuzzySet(vmax,vrange,size,x):

    a = vmax - vrange
    b = vmax + vrange

    if x <= a:
        return 0
    if x > a and x <= vmax :    
        return (x-a)/(vmax-a)
    if x > vmax and x <= b:    
        return (b-x)/(b-vmax)
    if x > b and x <= size:    
        return 0 

print("=================================QUESTÃO 6=================================\n")
vmax = int(input("Max: "))
vrange = int(input("Range: "))
size = int(input("Size: "))

x = np.arange(0, size, 0.1)
y=[]

for num in x :
    y.append(FuzzySet(vmax,vrange,size,num))

plt.show(plt.plot(x,y))