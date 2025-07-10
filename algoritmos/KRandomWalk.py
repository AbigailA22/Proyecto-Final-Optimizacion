import streamlit as st
import numpy as np
from funciones import GRAFICAS_multi as graph

def puntoInicial(N, limIf, limSup):
  k = 0
  x0 = []
  while k < N:
    x0.append(np.random.uniform(limIf, limSup))
    k = k + 1
  return x0   

def randomWalk (epsilon, N, a, b, funcion):
    x0 = puntoInicial(N, a, b)
    x_best = x0
    x = []
    x.append(x0)
    k=0
    while ((funcion(x_best) > epsilon) and (k < 100000)):
        i = 0
        y = []
        while i < N:
            y.append(np.random.uniform(a,b))
            i = i + 1
        x.append(y)

        if funcion(x[k+1]) < funcion(x_best):
            x_best = x[k+1]
            x.append(x_best)
        k=k+1

    return x, x_best

def graficar(a_x, b_x, a_y, b_y, x_arreglo, funcion):
    X, Y, Z = graph.meshdata(a_x, b_x, a_y, b_y, funcion)
    fig, ax = graph.plotContour(X, Y, Z) 

    for j in range(len(x_arreglo[-150:])):
        ax.scatter(x_arreglo[j][0], x_arreglo[j][1], color='red', marker='*')
    st.pyplot(fig)
