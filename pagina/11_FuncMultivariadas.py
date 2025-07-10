import streamlit as st
from funciones import FuncionesMultivariables as funMultivariable

st.title("Funciones Multivariadas")
st.markdown('<div style="text-align: justify;">De la manera más general, su entrada consiste de varios números; en otras ocasiones, si la salida de la función consiste de varios números, también se le puede llamar ' \
'multivariable, pero usualmente son conocidas como funciones con valores vectoriales. Así, una función multivariable es una función cuya entrada o salida  ' \
'consiste de varios números. En contraste, una función con una entrada y una salida se llama función de una variable o univariable.</div>', unsafe_allow_html=True)

st.markdown("")

col1, col2, col3 = st.columns(3)

with col1:
    st.write("Tipos de Funciones")
    st.write("Salida de 1 número")
    st.write("Salida de varios números")

with col2:
    st.write("Entrada de un número")
    st.write("f(x) = x²")
    st.write("f(t) = (cos(t), sen(t))")

with col3:
    st.write("Entrada de varios números")
    st.write("f(x, y) = x² + y²")
    st.write("f(u, v) = (u² - v, v² + u)")

st.header("Gráficas")
option = st.selectbox(
    "¿Qué función desea?",
    ("Función de Rastrigin", "Función de Ackley", "Función Esfera", "Función de Rosenbrock", "Función de Beale", 
     "Función de Booth", "Función de Himmelblaus", "Función de McCormick")
)

if(option == "Función de Rastrigin"):
    limInf = st.number_input("Escriba el límite inferior", value=-5.12)
    limSup = st.number_input("Escriba el límite superior", value=5.12)
    st.write("Función:")
    latext1 = r'''
    $$ 
    f(\textbf{x}) = 10n + \sum_{i=1}^{n}[\mathrm{x}_{i}^{2} - 10cos(2\pi x_{i})]
    $$  
    '''
    st.write(latext1)

    funcion = funMultivariable.RastriginFunction([limInf, limSup])
    funMultivariable.plot2d_lista(funMultivariable.RastriginFunction, limInf, limSup)
    funMultivariable.plot3d_lista(funMultivariable.RastriginFunction, limInf, limSup)
    funMultivariable.plotquiver_lista(funMultivariable.RastriginFunction, limInf, limSup)

elif(option == "Función de Ackley"):
    limInfx = st.number_input("Escriba el límite inferior de x", value=-5.00)
    limSupx = st.number_input("Escriba el límite superior de x", value=5.00)
    limInfy = st.number_input("Escriba el límite inferior de y", value=-5.00)
    limSupy = st.number_input("Escriba el límite superior de y", value=5.00)
    st.write("Función:")
    latext1 = r'''
    $$ 
    f(x, y) = -20exp[-0.2\sqrt{0.5(x^{2}+y^{2})}] - exp[0.5(cos(2\pi x) + cos(2\pi y))] + e + 20
    $$  
    '''
    st.write(latext1)

    funcion = funMultivariable.AckleyFunction(limInfx, limSupx)
    funMultivariable.plot2d_tupla(funMultivariable.AckleyFunction, limInfx, limSupx, limInfy, limSupy)
    funMultivariable.plot3d_tupla(funMultivariable.AckleyFunction, limInfx, limSupx, limInfy, limSupy)
    funMultivariable.plotquiver_tupla(funMultivariable.AckleyFunction, limInfx, limSupx, limInfy, limSupy)

elif(option == "Función Esfera"):
    limInf = st.number_input("Escriba el límite inferior", value=-100.0)
    limSup = st.number_input("Escriba el límite superior", value=100.0)
    st.write("Función:")
    latext1 = r'''
    $$ 
    f(\textbf{x}) = \sum_{i=1}^{n}\mathrm{x}_{i}^{2}
    $$  
    '''
    st.write(latext1)

    funcion = funMultivariable.SphereFunction([limInf, limSup])
    funMultivariable.plot2d_lista(funMultivariable.SphereFunction, limInf, limSup)
    funMultivariable.plot3d_lista(funMultivariable.SphereFunction, limInf, limSup)
    funMultivariable.plotquiver_lista(funMultivariable.SphereFunction, limInf, limSup)

elif(option == "Función de Rosenbrock"):
    limInf = st.number_input("Escriba el límite inferior", value=-2.048)
    limSup = st.number_input("Escriba el límite superior", value=2.048)
    st.write("Función:")
    latext1 = r'''
    $$ 
    f(\textbf{x}) = \sum_{i=1}^{n-1}[100(x_{i+1}-\mathrm{x}_{i}^{2})^{2} + (1-x_{i})^{2}]
    $$  
    '''
    st.write(latext1)

    funcion = funMultivariable.RosenbrockFunction([limInf, limSup])
    funMultivariable.plot2d_lista(funMultivariable.RosenbrockFunction, limInf, limSup)
    funMultivariable.plot3d_lista(funMultivariable.RosenbrockFunction, limInf, limSup)
    funMultivariable.plotquiver_lista(funMultivariable.RosenbrockFunction, limInf, limSup)

elif(option == "Función de Beale"):
    limInfx = st.number_input("Escriba el límite inferior de x", value=-4.50)
    limSupx = st.number_input("Escriba el límite superior de x", value=4.50)
    limInfy = st.number_input("Escriba el límite inferior de y", value=-4.50)
    limSupy = st.number_input("Escriba el límite superior de y", value=4.50)
    st.write("Función:")
    latext1 = r'''
    $$ 
    f(x, y) = (1.5−x+xy)^{2}+(2.25−x+xy^{2})^{2}+(2.625−x+xy^{3})^{2}
    $$  
    '''
    st.write(latext1)
    funcion = funMultivariable.BealeFunction(limInfx, limSupx) 
    funMultivariable.plot2d_tupla(funMultivariable.BealeFunction, limInfx, limSupx, limInfy, limSupy)
    funMultivariable.plot3d_tupla(funMultivariable.BealeFunction, limInfx, limSupx, limInfy, limSupy)
    funMultivariable.plotquiver_tupla(funMultivariable.BealeFunction, limInfx, limSupx, limInfy, limSupy)

elif(option == "Función de Booth"):
    limInfx = st.number_input("Escriba el límite inferior de x", value=-10.00)
    limSupx = st.number_input("Escriba el límite superior de x", value=10.00)
    limInfy = st.number_input("Escriba el límite inferior de y", value=-10.00)
    limSupy = st.number_input("Escriba el límite superior de y", value=10.00)
    st.write("Función:")
    latext1 = r'''
    $$ 
    f(x, y) = (x+2y-7)^{2}+(2x+y-5)^{2}
    $$  
    '''
    st.write(latext1)

    funcion = funMultivariable.BoothFunction(limInfx, limSupx)
    funMultivariable.plot2d_tupla(funMultivariable.BoothFunction, limInfx, limSupx, limInfy, limSupy)
    funMultivariable.plot3d_tupla(funMultivariable.BoothFunction, limInfx, limSupx, limInfy, limSupy)
    funMultivariable.plotquiver_tupla(funMultivariable.BoothFunction, limInfx, limSupx, limInfy, limSupy)

elif(option == "Función de Himmelblaus"):
    limInfx = st.number_input("Escriba el límite inferior de x", value=-5.00)
    limSupx = st.number_input("Escriba el límite superior de x", value=5.00)
    limInfy = st.number_input("Escriba el límite inferior de y", value=-5.00)
    limSupy = st.number_input("Escriba el límite superior de y", value=5.00)
    st.write("Función:")
    latext1 = r'''
    $$ 
    f(x, y) = (x^{2}+y-11)^{2}+(x+y^{2}-7)^{2}
    $$  
    '''
    st.write(latext1)

    funcion = funMultivariable.HimmelblausFunction(limInfx, limSupx) 
    funMultivariable.plot2d_tupla(funMultivariable.HimmelblausFunction, limInfx, limSupx, limInfy, limSupy)
    funMultivariable.plot3d_tupla(funMultivariable.HimmelblausFunction, limInfx, limSupx, limInfy, limSupy)
    funMultivariable.plotquiver_tupla(funMultivariable.HimmelblausFunction, limInfx, limSupx, limInfy, limSupy)

else:
    limInfx = st.number_input("Escriba el límite inferior de x", value=-1.50)
    limSupx = st.number_input("Escriba el límite superior de x", value=4.00)
    limInfy = st.number_input("Escriba el límite inferior de y", value=-3.00)
    limSupy = st.number_input("Escriba el límite superior de y", value=4.00)
    st.write("Función:")
    latext1 = r'''
    $$ 
    f(x, y) = sen(x+y)+(x-y)^{2}-1.5x + 2.5y + 1
    $$  
    '''
    st.write(latext1)

    funcion = funMultivariable.McCormickFunction(limInfx, limSupx) 
    funMultivariable.plot2d_tupla(funMultivariable.McCormickFunction, limInfx, limSupx, limInfy, limSupy)
    funMultivariable.plot3d_tupla(funMultivariable.McCormickFunction, limInfx, limSupx, limInfy, limSupy)
    funMultivariable.plotquiver_tupla(funMultivariable.McCormickFunction, limInfx, limSupx, limInfy, limSupy)


