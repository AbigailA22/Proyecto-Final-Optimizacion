#Golden Section Search - ALL PROBLEMS
import math

def elimination_rules(x1:float, x2:float, a:float, b:float, funcion:callable):
    if (funcion(x1) > funcion(x2)):
        a = x1
    elif (funcion(x1) < funcion(x2)):   
        b = x2
    else:
        a = x1
        b = x2
    return a, b    

def golden_section(a:float, b:float, epsilon:float, funcion:callable) -> tuple[float, float]:
    """_summary_
    Args:
        a (float): limite inferior de la función
        b (float):limite superior de la función
        epsilon (float): Número deseado de error
        funcion (callable): Función a evaluar
    Returns:
        tuple[float, float]: Intervalo donde la función se hace mínima
    """
    phi = ((1 + math.sqrt(5)) / 2) - 1
    aw = 0
    bw = 1
    Lw = 1
    k = 1
    px = []
    py = []
    
    while Lw > epsilon:
        w1 = aw + (phi) * Lw
        w2 = bw - (phi) * Lw
        aw, bw = elimination_rules((w1*(bw-aw)+aw), (w2*(bw-aw)+aw), aw, bw, funcion)

        px.extend([w1*(bw-aw)+aw, w2*(bw-aw)+aw])
        py.extend([funcion(w1*(bw-aw)+aw), funcion(w2*(bw-aw)+aw)])
        
        k = k + 1
        Lw = abs(bw - aw)       

    return (aw, bw)





    
