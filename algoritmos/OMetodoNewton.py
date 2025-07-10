#Método de Newton
import streamlit as st
import numpy as np
from algoritmos import Z_GoldenSectionCopy as Golden
from funciones import GRAFICAS_multi as graph
from algoritmos import Z_DiferenciaCentralCopy as diferencia

def puntoInicial(N, limIf, limSup):
  k = 0
  x0 = []
  while k < N:
    x0.append(np.random.uniform(limIf, limSup))
    k = k + 1
  return x0   

def newton(N, epsilon1, epsilon2, delta, M, limInf, limSup, funcion):
    x0 = puntoInicial(N, limInf, limSup)
    terminar = False
    x = []
    xk = x0
    x.append(xk)
    k=0
    alpha = 0
    while terminar == False:
        gradiente = np.array(diferencia.gradiente1(xk, delta, funcion))
        hessian = diferencia.derivadaTres(xk, delta, funcion)
        
        if (np.linalg.norm(gradiente) < epsilon1) or (k >= M):
            terminar = True
        else:

            def funcionAlpha(alpha):
                return funcion(xk - alpha*gradiente)
            
            alphaList =  Golden.golden_section(0.0, 1.0, epsilon2, funcionAlpha)
            alpha = (sum(alphaList) / 2)

            xk1 = xk - alpha*np.dot(np.linalg.inv(hessian), gradiente)
            
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



    
