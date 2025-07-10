import streamlit as st
import math
import numpy as np
from funciones import GRAFICAS_multi as graph

def puntoInicial(N, limIf, limSup):
  k = 0
  x0 = []
  while k < N:
    x0.append(np.random.uniform(limIf, limSup))
    k = k + 1
  return x0   

def recocidoSimulado(epsilon, N, a, b, temperatura, funcion):
    x0 = puntoInicial(N, a, b)
    x_best = x0
    x_current = x0
    x = []
    x.append(x0)
    k=0
    
    while ((funcion(x_best) > epsilon) and (k < 100000)):
        temp = temperatura / float(k + 1)
        i = 0
        candidato = []
        while i < N:
            candidato.append(x_current[i]+ np.random.uniform(-1,1))
            i = i + 1

        if(funcion(candidato) < funcion(x_best)) or np.random.random() < math.exp((funcion(x_current) - funcion(candidato)) / temp):
            x_current = candidato
            if(funcion(candidato) < funcion(x_best)):
                x_best = candidato
                x.append(x_best)
        k=k+1

    return x, x_best       

def graficar(a_x, b_x, a_y, b_y, x_arreglo, funcion):
    X, Y, Z = graph.meshdata(a_x, b_x, a_y, b_y, funcion)
    fig, ax = graph.plotContour(X, Y, Z)

    for j in range(len(x_arreglo)):
        ax.scatter(x_arreglo[j][0], x_arreglo[j][1], color='red', marker='*')
    st.pyplot(fig)

