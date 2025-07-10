import math

def lata(r:float):
    """Función que retorna el área de una lata dado un radio y sujeto a 250ml de volumen
    Args:
        r (float): radio de la lata
    Returns:
        float: Área de la lata dado el radio
    """
    return 2*math.pi*r*r + (500 / r)

def caja(l:float):
    """Función que retorna el volumen de una caja dado una L 
    Args:
        l (float): valor del alto de la caja
    Returns:
        float: Volumen de la caja dado l
    """

    return -(4*pow(l, 3) - 60*l*l + 200*l)

def ej1(x:float):
    """Función que retorna el mínimo de la operación x^2 + 3 
    Args:
        x (float): valor de la variable
    Returns:
        float: Mínimo de la función
    """

    return x*x + 3

def ej4(x:float):
    """Función que retorna el mínimo de la operación x^2 + 54/x 
    Args:
        x (float): valor de la variable
    Returns:
        float: Mínimo de la función
    """

    return x*x + (54/x)

def ej5(x:float):
    """Función que retorna el mínimo de la operación x^3 + 2x - 3 
    Args:
        x (float): valor de la variable
    Returns:
        float: Mínimo de la función
    """

    return (pow(x, 3) + 2*x - 3)

def ej6(x:float):
    """Función que retorna el mínimo de la operación x^4 + x^2 - 33 
    Args:
        x (float): valor de la variable
    Returns:
        float: Mínimo de la función
    """

    return (pow(x, 4) + x*x - 33)

def ej7(x:float):
    """Función que retorna el mínimo de la operación 3x^4 - 8x^3 + 6x^2 + 12x 
    Args:
        x (float): valor de la variable
    Returns:
        float: Mínimo de la función
    """

    return (3*pow(x, 4) - 8*pow(x, 3) - 6*pow(x, 2) + 12*x)

