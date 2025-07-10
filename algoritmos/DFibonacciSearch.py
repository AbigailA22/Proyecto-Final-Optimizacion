#Fibonacci Search - ALL PROBLEMS
import math

def create_fibonacci(pos:int):
    phi = ( 1 + math.sqrt(5) ) / 2    
    return int((pow(phi, pos) - pow((1-phi), pos)) / math.sqrt(5))

def elimination_rules(x1:float, x2:float, a:float, b:float, funcion:callable):
    if (funcion(x1) > funcion(x2)):
        a = x1
    elif (funcion(x1) < funcion(x2)):   
        b = x2
    else:
        a = x1
        b = x2
    return a, b    

def fibonacci_search(a:float, b:float, n:float, funcion:callable) -> tuple[float, float]:
    """_summary_
    Args:
        a (float): limite inferior de la función
        b (float):limite superior de la función
        n (float): Número deseado de evaluaciones
        funcion (callable): Función a evaluar
    Returns:
        tuple[float, float]: Intervalo donde la función se hace mínima
    """
    L = b - a
    k = 2
    px = []
    py = []

    if(n<1):
        aux = (2 / n) * (b-a)
        a_aux = 0
        b_aux = 1
        c_aux = 1
        res = 1
        while (c_aux < aux) :
            c_aux = a_aux + b_aux
            res = res + 1
            a_aux = b_aux
            b_aux = c_aux
        n=res       
  
    while (k <= n):
        lk = (create_fibonacci(n-k+2) / create_fibonacci(n+2)) * L
        x1 = a + lk
        x2 = b - lk

        px.extend([x1, x2])
        py.extend([funcion(x1), funcion(x2)])        
        a, b = elimination_rules(x1, x2, a, b, funcion)
        k = k + 1
 
    return (a, b, px, py)




    
