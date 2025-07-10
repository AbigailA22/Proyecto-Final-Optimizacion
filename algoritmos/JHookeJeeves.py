import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from funciones import GRAFICAS_multi as graph

def movimiento_exploratorio(x, delta, funcion, N):
  xc = np.array(x)
  for i in range(N):
    x_plus = np.array(x)
    x_minus = np.array(x)
    x_plus[i] = x[i] + delta[i]
    x_minus[i] = x[i] - delta[i]
    xs = [x_minus, x, x_plus] #Ordenarlo
    fx = [funcion(x) for x in xs]
    indice_min = np.argmin(fx) #Indice que corresponda al de menor valor
    x = xs[indice_min] #x se vuelve el minimo

  if all(x == xc):
    return xc, False
  return x, True

def movimiento_patron(x_arreglo, k):
  return x_arreglo[k] + (x_arreglo[k] - x_arreglo[k-1])

def movimiento_exploratorio_grafica(x, delta, funcion, N):
  xc = np.array(x)
  for i in range(N):
    x_plus = np.array(x)
    x_minus = np.array(x)
    x_plus[i] = x[i] + delta[i]
    x_minus[i] = x[i] - delta[i]
    xs = [x_minus, x, x_plus] #Ordenarlo
    fx = [funcion(x) for data in xs]
    indice_min = np.argmin(fx) #Indice que corresponda al de menor valor
    x = xs[indice_min] #x se vuelve el minimo
  return xs

def puntoInicial(N, limInf, limSup):
  k = 0
  x0 = []
  delta = []
  while k < N:
    x0.append(np.random.uniform(limInf, limSup))
    delta.append(np.random.uniform(limInf, limSup))
    k = k + 1
  return x0, delta 

def HookeJeeves(N, epsilon, alpha, limInf, limSup, funcion):
  k = 0
  x0, delta = puntoInicial(N, limInf, limSup)
  #print(delta)
  #print(alpha)
  delta = np.array(delta)
  x_arreglo = [np.array(x0)]
  while np.linalg.norm(delta) > epsilon:
    x, exito = movimiento_exploratorio(x_arreglo[k], delta, funcion, N)
    #print("x: ", x, "exito ", exito)
    if exito:
      x_arreglo.append(x)
      k += 1
      xp = movimiento_patron(x_arreglo, k)
      if funcion(xp) < funcion(x):
        x_arreglo.append(xp)
        k += 1
    else:
      delta = delta / alpha
  return x_arreglo, xp

def graficar(a_x, b_x, a_y, b_y, x_arreglo, funcion):
  X, Y, Z = graph.meshdata(a_x, b_x, a_y, b_y, funcion)
  fig, ax = graph.plotContour(X, Y, Z)

  for j in range(len(x_arreglo[-100:])):
      ax.scatter(x_arreglo[j][0], x_arreglo[j][1], color='red', marker='*')
  st.pyplot(fig)    