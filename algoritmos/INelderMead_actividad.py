import streamlit as st
import numpy as np
from funciones import GRAFICAS_multi as graph

def createSimplex(x0: np.ndarray, alpha:float, N):
  delta1 = ( (np.sqrt(N+1) + N - 1)/N*np.sqrt(2) )*alpha
  delta2 = ( (np.sqrt(N+1) - 1)/N*np.sqrt(2) )*alpha

  xn = [ np.array([x0[i]+delta1 if i==j else x0[i]+delta2 for i in range(0, N)]) for j in range(0, N) ]
  xn.insert(0, x0)
  print(xn)
  return np.reshape(np.array(xn), (N+1, N))

# Centro, Reflexion, Expansion, Contraccion, Termino
centroide = lambda simplex, index_h, N: (np.sum(simplex, axis=0) - simplex[index_h])/N #suma por columnas
reflexion = lambda xc, xh,: 2*xc - xh
expansion = lambda xc, xh, gamma: (1+gamma)*xc - gamma*xh
contraccion1 = lambda xc, xh, beta: (1-beta)*xc + beta*xh
contraccion2 = lambda xc, xh, beta: (1+beta)*xc - beta*xh
terminar = lambda fx, fc, N, epsilon=0.001: np.sqrt(np.sum((fx-fc)**2)/(N+1)) <= epsilon

def puntoInicial(N, limInf, limSup):
  k = 0
  x0 = []
  while k < N:
    x0.append(np.random.uniform(limInf, limSup))
    k = k + 1
  return x0   

def NelderMead(N, alpha, gamma, beta, epsilon, limInf, limSup, funcion):
  x0 = puntoInicial(N, limInf, limSup)
  simplex = createSimplex(x0, alpha, N)
  a = False
  lista = []
  lista.append(x0)
  k=0
  #while (a == False or (k <=1)):
  while (k <= 1000):
    fx = [funcion(x) for x in simplex]

    #Determinar índices de los puntos clave (mejor, peor y segundo peor)
    indices = np.argsort(fx)
    i_xl = indices[0]
    i_xh = indices[-1]
    i_xg = indices[-2]

    xc = centroide(simplex, i_xh, N) #Calcular centroide
    xr = reflexion(xc, simplex[i_xh]) #Calcular punto de reflejo
    fxr = funcion(xr)
    fxc = funcion(xc)
    xnew = xr
  
    if fxr < fx[i_xl]:
      xnew = expansion(xc, simplex[i_xh], gamma) #Calcular expansión
    elif fxr >= fx[i_xh]:
      xnew = contraccion1(xc, simplex[i_xh], beta) #Calcular contracción 1
    elif fx[i_xg] < fxr < fx[i_xh]:
      xnew = contraccion2(xc, simplex[i_xh], beta) #Calcular contracción 2

    simplex[i_xh] = xnew
    lista.append(xnew)

    a = terminar(fx, fxc, N, epsilon)
    k = k + 1
  return lista, lista[-1]


def graficar(a_x, b_x, a_y, b_y, x_arreglo, funcion):
  X, Y, Z = graph.meshdata(a_x, b_x, a_y, b_y, funcion)
  fig, ax = graph.plotContour(X, Y, Z) 

  for j in range(len(x_arreglo[-150:])):
      ax.scatter(x_arreglo[j][0], x_arreglo[j][1], color='red', marker='*')
  st.pyplot(fig)