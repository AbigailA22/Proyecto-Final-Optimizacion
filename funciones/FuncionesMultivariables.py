#Funciones multivariadas
import streamlit as st
import math
import matplotlib.pyplot as plt 
import numpy as np

#from matplotlib import cm
#from matplotlib.ticker import LinearLocator

def RastriginFunction(x:list):
    suma = 0
    d = 0
    for element in x:
        suma = suma + (element**2 - 10 * math.cos(2 * math.pi * element))    
        d = d+1
    return 10*d + suma

def AckleyFunction(x:float, y:float):
    return -20 * math.exp(-0.2 * math.sqrt(0.5*(x**2 + y**2))) - math.exp(0.5*(math.cos(2*math.pi*x) + math.cos(2*math.pi*y))) + math.e + 20
def ackley(x:np.ndarray):
    return -20 * math.exp(-0.2 * math.sqrt(0.5*(x[0]**2 + x[1]**2))) - math.exp(0.5*(math.cos(2*math.pi*x[0]) + math.cos(2*math.pi*x[1]))) + math.e + 20

def SphereFunction(x:list):
    suma = 0
    for element in x:
        suma = suma + element**2 
    return suma

def RosenbrockFunction(x:list):
    suma = 0
    for i in range(len(x)-1):
        suma = suma + (100 * (x[i+1] - x[i]**2)**2 + (1 - x[i])**2 )
    return suma
    
def BealeFunction(x:float, y:float):
    return (1.5 - x + x*y)**2 + (2.25 - x + x* y**2)**2 + (2.625 - x + x * y**3)**2
def beale(x:np.ndarray)-> float:
    return (1.5 - x[0] + x[0]*x[1])**2 + (2.25 - x[0] + x[0]* x[1]**2)**2 + (2.625 - x[0] + x[0] * x[1]**3)**2


def BoothFunction(x:float, y:float):
    return (x + 2*y - 7)**2 + (2*x + y - 5)**2
def booth(x: np.ndarray) -> float:
    return (x[0] + 2*x[1] - 7)**2 + (2*x[0] + x[1] - 5)**2

def HimmelblausFunction(x:float, y:float):
    return (x**2 + y - 11)**2 + (x + y**2 - 7)**2
def himmelblaus(x:np.ndarray)-> float:
    return (x[0]**2 + x[1] - 11)**2 + (x[0] + x[1]**2 - 7)**2

def McCormickFunction(x:float, y:float):
    return math.sin(x + y) + (x - y)**2 - 1.5*x + 2.5*y + 1
def mccormick(x:np.ndarray)-> float:
    return math.sin(x[0] + x[1]) + (x[0] - x[1])**2 - 1.5*x[0] + 2.5*x[1] + 1


#RastriginFunction, SphereFunction, RosenbrockFunction
def plot2d_lista(function, a, b):
    x = np.linspace(a, b, 400)
    y = np.linspace(a, b, 400) 
    X, Y = np.meshgrid(x, y)
    Z = np.array([function([i, j]) for i, j in zip(np.ravel(X), np.ravel(Y))]).reshape(X.shape)

    fig = plt.figure()
    contour = plt.contourf(X, Y, Z, levels=50, cmap='viridis')
    plt.colorbar(contour)
    plt.title(f"Gráfica de Contornos de {function.__name__}")
    plt.xlabel("Eje X")
    plt.ylabel("Eje Y")
    st.pyplot(fig)
    #plt.show()

#AckleyFunction, BealeFunction, BoothFunction, HimmelblausFunction, McCormickFunction
def plot2d_tupla(function, ax, bx, ay, by):
    x = np.linspace(ax, bx, 400)  
    y = np.linspace(ay, by, 400) 
    X, Y = np.meshgrid(x, y)
    Z = np.array([function(i, j) for i, j in zip(np.ravel(X), np.ravel(Y))]).reshape(X.shape)

    fig = plt.figure()
    contour = plt.contourf(X, Y, Z, levels=50, cmap='viridis')
    plt.colorbar(contour)
    plt.title(f"Gráfica de Contornos de {function.__name__}")
    plt.xlabel("Eje X")
    plt.ylabel("Eje Y")
    st.pyplot(fig)
    #plt.show()


def plot3d_lista(function, a, b):
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    x = np.linspace(a, b, 400)
    y = np.linspace(a, b, 400) 
    X, Y = np.meshgrid(x, y)
    Z = np.array([function([i, j]) for i, j in zip(np.ravel(X), np.ravel(Y))]).reshape(X.shape)

    surf = ax.plot_surface(X, Y, Z, cmap='viridis', linewidth=0, antialiased=False)
    plt.title(f"Gráfica 3D de {function.__name__}")
    plt.xlabel("Eje X")
    plt.ylabel("Eje Y")
    fig.colorbar(surf, shrink=0.5, aspect=5)
    #plt.show()
    st.pyplot(fig)

def plot3d_tupla(function, a, bx, ay, by):
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    x = np.arange(a, bx, 0.25)  
    y = np.arange(ay, by, 0.25) 
    X, Y = np.meshgrid(x, y)
    Z = np.array([function(i, j) for i, j in zip(np.ravel(X), np.ravel(Y))]).reshape(X.shape)

    surf = ax.plot_surface(X, Y, Z, cmap='viridis', linewidth=0, antialiased=False)
    plt.title(f"Gráfica 3D de {function.__name__}")
    plt.xlabel("Eje X")
    plt.ylabel("Eje Y")
    fig.colorbar(surf, shrink=0.5, aspect=5)
    #plt.show()
    st.pyplot(fig)    

def plotquiver_lista(function, a, b):
    x = np.arange(a, b, 1)
    y = np.arange(a, b, 1) 
    X, Y = np.meshgrid(x, y)
    M = np.hypot(X, Y)
    fig, ax = plt.subplots()

    q = ax.quiver(x, y, X, Y, M)

    plt.title(f"Gráfica de Campo Vectorial de {function.__name__}")
    plt.xlabel("Eje X")
    plt.ylabel("Eje Y")
    st.pyplot(fig)

def plotquiver_tupla(function, a, bx, ay, by):
    x = np.arange(a, bx, 0.25)  
    y = np.arange(ay, by, 0.25) 
    X, Y = np.meshgrid(x, y)
    M = np.hypot(X, Y)
    fig, ax = plt.subplots()

    q = ax.quiver(x, y, X, Y, M)
  
    plt.title(f"Gráfica de Campo Vectorial de {function.__name__}")
    plt.xlabel("Eje X")
    plt.ylabel("Eje Y")
    #plt.show()  
    st.pyplot(fig) 

"""
print(RastriginFunction([4.52299, 4.52299]))
print(AckleyFunction(-32.768, 32.768))
print(SphereFunction([-5.12, 5.12]))
print(RosenbrockFunction([1, 1, 1]))
print(BealeFunction(3, 0.5))
print(BoothFunction(1, 3))
print(HimmelblausFunction(3, 2))
print(McCormickFunction(-0.54719, -1.54719))

plot2d_lista(RastriginFunction, -5.12, 5.12)
plot2d_tupla(AckleyFunction, -5, 5, -5, 5)
plot2d_lista(SphereFunction, -100, 100)
plot2d_lista(RosenbrockFunction, -2.048, 2.048)
plot2d_tupla(BealeFunction, -4.5, 4.5, -4.5, 4.5)
plot2d_tupla(BoothFunction, -10, 10, -10, 10)
plot2d_tupla(HimmelblausFunction, -5, 5, -5, 5)
plot2d_tupla(McCormickFunction, -1.5, 4, -3, 4)

plot3d_lista(RastriginFunction, -5.12, 5.12)
plot3d_tupla(AckleyFunction, -5, 5, -5, 5)
plot3d_lista(SphereFunction, -100, 100)
plot3d_lista(RosenbrockFunction, -2.048, 2.048)
plot3d_tupla(BealeFunction, -4.5, 4.5, -4.5, 4.5)
plot3d_tupla(BoothFunction, -10, 10, -10, 10)
plot3d_tupla(HimmelblausFunction, -5, 5, -5, 5)
plot3d_tupla(McCormickFunction, -1.5, 4, -3, 4)

"""




