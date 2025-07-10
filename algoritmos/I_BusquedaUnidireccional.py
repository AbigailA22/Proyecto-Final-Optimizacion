#Búsqueda Unidireccional
import streamlit as st
import numpy as np
from algoritmos import Z_IntervalHalvingCopy as Interval
from funciones import GRAFICAS_multi as graph

def puntoInicial(N, limIf, limSup):
  k = 0
  x0 = []
  s=[]
  while k < N:
    x0.append(np.random.uniform(limIf, limSup))
    s.append(np.random.uniform(limIf, limSup))
    k = k + 1
  return x0, s  


def busquedaUnidireccional(N,  limInf, limSup, epsilon, funcion):
  xk, s = puntoInicial(N, limInf, limSup)
  s = np.array(s)
  def funcionAlpha(alpha):
      return funcion(xk - alpha*s)

  alphaList = Interval.interval_halving(0.0, 1.0, epsilon, funcionAlpha)
  alpha = (sum(alphaList) / 2)
  return alpha, xk - alpha*s

def graficar(a_x, b_x, a_y, b_y, x_arreglo, s, funcion):
  X, Y, Z = graph.meshdata(a_x, b_x, a_y, b_y, funcion)
  fig, ax = graph.plotContour(X, Y, Z) 
  s = [1, 1]
  
  x = [x_arreglo[0], s[0]]
  y = [x_arreglo[1], s[1]]

  ax.scatter(x, y, color="red", marker='*')

  st.pyplot(fig)


