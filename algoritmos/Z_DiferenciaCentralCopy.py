#Diferencia Central
import numpy as np

def funcion(x:np.ndarray)-> float:
    return (x[0]**2 + x[1] - 11)**2 + (x[0] + x[1]**2 - 7)**2

def gradiente1(x:np.ndarray, delta:float, funcion:callable):
    r = []
    for i in range(len(x)):
        xp = x.copy()
        xn = x.copy()
        xp[i] = xp[i]+delta
        xn[i] = xn[i]-delta
        r.append( (funcion(xp) - funcion(xn)) / (2*delta) )
    return r    

def gradiente2(x:np.ndarray, delta:float, funcion:callable):
    r = []
    for i in range(len(x)):
        xp = x.copy()
        xn = x.copy()
        xp[i] = xp[i]+delta
        xn[i] = xn[i]-delta
        r.append( (funcion(xp) - 2*funcion(x) + funcion(xn))/ (delta*delta) )
    return r 

def derivadaTres(x:np.ndarray, delta:float, funcion:callable):
    H = []
    for i in range(len(x)):
        hi = []
        for j in range(len(x)):
            if i == j:
                xp = x.copy()
                xn = x.copy()
                xp[i] = xp[i]+delta
                xn[i] = xn[i]-delta
                hi.append( (funcion(xp) - 2*funcion(x) + funcion(xn)) / (delta*delta) )
            else:
                xpp = x.copy()
                xpn = x.copy()
                xnp = x.copy()
                xnn = x.copy()

                xpp[i] = xpp[i] + delta
                xpp[j] = xpp[j] + delta

                xpn[i] = xpn[i] + delta
                xpn[j] = xpn[j] - delta

                xnp[i] = xnp[i] - delta
                xnp[j] = xnp[j] + delta

                xnn[i] = xnn[i] - delta
                xnn[j] = xnn[j] - delta

                hi.append( (funcion(xpp)-funcion(xpn)-funcion(xnp)+funcion(xnn)) / (4*delta**2) )
        H.append(hi)
    return H



