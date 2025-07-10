#Bounding Phase Method - ALL PROBLEMS
import random

def bounding_phase(a:float, b:float, delta:float, funcion:callable) -> tuple[float, float]:
    """_summary_
    Args:
        a (float): limite inferior de la función
        b (float):limite superior de la función
        delta (float): Incremento de búsqueda
        funcion (callable): Función a evaluar
    Returns:
        tuple[float, float]: Intervalo donde la función se hace mínima
    """
    #x0 = random.uniform(a,b)
    x0 = (a+b)/2
    k = 0
    step2 = False

    while (step2 == False):
        if ( funcion(x0 - abs(delta)) >= funcion(x0) >= funcion(x0 + abs(delta))):
            step2 = True
        elif ( funcion(x0 - abs(delta)) <= funcion(x0) <= funcion(x0 + abs(delta))):
            delta = delta * -1
            step2 = True
        else:
            x0 = random.uniform(a,b)
    px = [x0]
    py = [funcion(x0)]

    x_kmenos = x0
    xk = x0
    x_kmas = xk + (pow(2, k) * delta)

    while((funcion(x_kmas) < funcion(xk)) and (x_kmas>a) and (x_kmenos>a) and (x_kmas<b) and (x_kmenos<b)):
          x_kmenos = xk
          xk = x_kmas
          k = k + 1
          x_kmas = xk + (pow(2, k) * delta)
          px.extend([x_kmenos, xk, x_kmas])
          py.extend([funcion(x_kmenos), funcion(xk), funcion(x_kmas)])

    if(x_kmas>x_kmenos):
        print("El mínimo está en el intervalo: ", x_kmenos, x_kmas)
    else:    
        print("El mínimo está en el intervalo: ", x_kmas, x_kmenos)

    return (x_kmenos, x_kmas, px, py)

