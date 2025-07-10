#Fecha: 16 de marzo de 2025
#Interval Halving - ALL PROBLEMS

import math

def interval_halving(a:float, b:float, epsilon:float, funcion:callable) -> tuple[float, float]:
    """_summary_
    Args:
        a (float): limite inferior de la función
        b (float):limite superior de la función
        epsilon (float): Error aceptado
        funcion (callable): Función a evaluar
    Returns:
        tuple[float, float]: Intervalo donde la función se hace mínima
    """
    xm = (a+b)/2
    L = b - a   
    
    while(L > epsilon):
        x1 = a + (L/4)
        x2 = b - (L/4)
        
        if (funcion(x1) < funcion(xm)):
            b = xm
            xm = x1
        elif (funcion(x2) < funcion(xm)):   
            a = xm
            xm = x2
        else:
            a = x1
            b = x2
  
        L = b - a   
  
    return (a, b)



    
