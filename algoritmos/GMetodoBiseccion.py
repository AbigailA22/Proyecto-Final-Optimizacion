#Método de Bisección - ALL PROBLEMS

import math
from algoritmos import BOUNDINGPhase as BP

def derivadaUno(x:float, delta:float, funcion:callable):    
    return ((funcion(x+delta) - funcion(x-delta)) / (2*delta))

def biseccion(a:float, b:float, epsilon:float, funcion:callable):
    x1 = a
    x2 = b
    funcionZ = 1

    z = (x1 + x2)/2
    funcionZ = derivadaUno(z, epsilon, funcion)
    
    px = [z]
    py = [funcion(z)]
    
    while((abs(funcionZ) > epsilon) and (z>a) and (z<b)):
        if(funcionZ<0): 
            x1 = z
        if(funcionZ>0):
            x2 = z
            
        z = (x1 + x2)/2
        funcionZ = derivadaUno(z, epsilon, funcion)

        px.extend([z])
        py.extend([funcion(z)])

    
    return (z, px, py)    
