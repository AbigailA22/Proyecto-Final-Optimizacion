#Método de Secante - ALL PROBLEMS

import math
import matplotlib.pyplot as plt
from algoritmos import BOUNDINGPhase as BP

def derivadaUno(x:float, delta:float, funcion:callable):    
    return ((funcion(x+delta) - funcion(x-delta)) / (2*delta))

def secante(a:float, b:float, epsilon:float, funcion:callable):
    x1 = a
    x2 = b
    f1 = derivadaUno(x1, epsilon, funcion)
    f2 = derivadaUno(x2, epsilon, funcion)

    z = x2 - (f2 / ( (f2 - f1) / (x2 - x1) ))
    funcionZ = derivadaUno(z, epsilon, funcion)

    px = [z]
    py = [funcion(z)]
    
    while((abs(funcionZ) > epsilon) and (z>a) and (z<b)):
        if(funcionZ<0): 
            x1 = z
        if(funcionZ>0):
            x2 = z
            
        f1 = derivadaUno(x1, epsilon, funcion)
        f2 = derivadaUno(x2, epsilon, funcion)

        z = x2 - (f2 / ( (f2 - f1) / (x2 - x1) ))
        funcionZ = derivadaUno(z, epsilon, funcion)

        px.extend([z])
        py.extend([funcion(z)])

    return (z, px, py)    
