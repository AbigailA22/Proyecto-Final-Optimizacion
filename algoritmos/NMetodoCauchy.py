#Método de Cauchy
import streamlit as st
import numpy as np
from algoritmos import Z_IntervalHalvingCopy as Interval
from funciones import GRAFICAS_multi as graph

def gradiente1(x:np.ndarray, delta:float, funcion:callable):
    r = []
    for i in range(len(x)):
        xp = x.copy()
        xn = x.copy()
        xp[i] = xp[i]+delta
        xn[i] = xn[i]-delta
        r.append( (funcion(xp) - funcion(xn)) / (2*delta) )
    return r

def puntoInicial(N, limIf, limSup):
  k = 0
  x0 = []
  while k < N:
    x0.append(np.random.uniform(limIf, limSup))
    k = k + 1
  return x0   

def cauchy(N, epsilon1, epsilon2, delta, M, limInf, limSup, funcion):
    x0 = puntoInicial(N, limInf, limSup)
    terminar = False
    x = []
    xk = x0
    x.append(xk)
    k=0
    alpha = 0
    while terminar == False:
        gradiente = np.array(gradiente1(xk, delta, funcion))
        if (np.linalg.norm(gradiente) < epsilon1) or (k >= M):
            terminar = True
        else:
            def funcionAlpha(alpha):
                return funcion(xk - alpha*gradiente)
            
            alphaList = Interval.interval_halving(0.0, 1.0, epsilon2, funcionAlpha)
            alpha = (sum(alphaList) / 2)

            xk1 = xk - alpha*gradiente

            if ((np.linalg.norm(xk1 - xk)) / (np.linalg.norm(xk)+0.0000001)) <= epsilon2:
                terminar = True
            else:
                k = k + 1 
                xk = xk1
                x.append(xk)
    return x, xk             

def graficar(a_x, b_x, a_y, b_y, x_arreglo, funcion):
    X, Y, Z = graph.meshdata(a_x, b_x, a_y, b_y, funcion)
    fig, ax = graph.plotContour(X, Y, Z) 

    for j in range(len(x_arreglo[-150:])):
        ax.scatter(x_arreglo[j][0], x_arreglo[j][1], color='red', marker='*')
    st.pyplot(fig)



    
