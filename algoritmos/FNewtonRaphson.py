#Método de Newton Raphson - ALL PROBLEMS

import math

def derivadaUno(x:float, delta:float, funcion:callable):    
    return ((funcion(x+delta) - funcion(x-delta)) / (2*delta))

def derivadaDos(x:float, delta:float, funcion:callable):    
    return ((funcion(x+delta) - (2 * funcion(x)) + funcion(x-delta)) / (delta*delta))

def newtonRaphson(a:float, b:float, epsilon:float, delta:float, funcion:callable):
    x = 0.5
    k = 1

    funcion1 = derivadaUno(x, delta, funcion)

    px = [x]
    py = [funcion(x)]
    
    while((abs(funcion1) >= epsilon) and (x>a) and (x<b)):
        funcion2 = derivadaDos(x, delta, funcion)

        x = x - (funcion1 / funcion2)
        funcion1 = derivadaUno(x, delta, funcion)
        
        k=k+1
        px.extend([x])
        py.extend([funcion(x)])

    return (x, px, py)
