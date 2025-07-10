#Búsqueda Exhaustiva - ALL PROBLEMS
import matplotlib.pyplot as plt

def calculoN(a:float, b:float, dec:float):
    """Función que retorna el cálculo para N 
    Args:
        a (float): valor del límite inferior
        b (float): valor del límite superior
        dec (float): valor del decimal
    Returns:
        float: Valor requerido para n
    """
    return ((2*(b-a))/dec)


def busqueda_exhaustiva(a:float, b:float, n:int, funcion:callable): 
    """_summary_
    Args:
        a (float): limite inferior de la función
        b (float):limite superior de la función
        n (int): Cantidad de valores a evaluar
        funcion (callable): Función a evaluar
    Returns:
        tuple[float, float]: Intervalo donde la función se hace mínima
    """
    delta_x = (b-a)/n

    x1 = a
    x2 = x1 + delta_x
    x3 = x2 + delta_x

    px = [x1, x2, x3]
    py = [funcion(x1), funcion(x2), funcion(x3)]

    while ( (not(funcion(x1) >= funcion(x2) <= funcion(x3))) and (x3 <= b) ):
        x1 = x2
        x2 = x3
        x3 = x2 + delta_x

        px.extend([x1, x2, x3])
        py.extend([funcion(x1), funcion(x2), funcion(x3)]) 

    #print("El mínimo está en el intervalo: ", x1, x3) 
    return(x1, x3, px,py)




    
