import streamlit as st
from funciones import FuncionesMultivariables as funMultivariable
from algoritmos import I_BusquedaUnidireccional as unidireccional

st.title("Búsqueda Unidireccional")
st.markdown('<div style="text-align: justify;">Este tipo de búsqueda está realizada en una sola dimensión, usualmente desde un punto xₜ hacia una dirección sₜ. Por ello, ' \
'solamente se consideran los puntos que se encuentran en la línea que se genera entre estos dos. Matemáticamente, se puede expresar como: </div>', unsafe_allow_html=True)

latext1 = r'''
$$ 
x(α) = x^{(t)} + αs^{(t)}
$$  
'''
st.write(latext1)
st.markdown('<div style="text-align: justify;">Donde α es un parámetro escalar, equivalente a la distancia desde el punto x(α) hasta xₜ. Por lo mismo, puede considerarse que este sea ' \
'negativo, positivo o 0, teniendo este último caso como resultado mantenerse en el punto inicial. Entonces, para encontrar el mínimo ' \
'de una línea específica, se debe encontrar el valor óptimo de α (para ello puede servir la ecuación previamente mostrada).</div>', unsafe_allow_html=True)

st.latex(r"""
\begin{array}{l}
\textbf{Algoritmo: Búsqueda Unidireccional} \\
\rule{14cm}{1pt}\\
\textbf{Definir: } x_{k} \text{ (Punto Inicial), } s \text{ (Punto Deseado), } \epsilon \\[0.5 ex] 
\textbf{Nota: }  \text{n es el número de puntos intermedios.} \\[0.5 ex] 
         \\
\textbf{Paso 1: } \text{Crear la función alfa donde se retorne } f(x_{k} - \alpha * s)  \\[0.5 ex] 
         
\textbf{Paso 2: } \text{Minimizar } \alpha \text{ usando una de las funciones unimodales vistas previamente.} \\[0.5 ex]         
\end{array}
""")

st.header("Resolución de Problemas")
col1, col2 = st.columns(2)
with col1:
    with st.form("my_form"):
        option = st.selectbox(
            "¿Qué función desea?",
            ("Función de Rastrigin", "Función de Ackley", "Función Esfera", "Función de Rosenbrock", "Función de Beale", 
            "Función de Booth", "Función de Himmelblaus", "Función de McCormick")
        )
        
        epsilon = st.slider("Selección del valor de epsilon", 0.01, 1.00)
        s = st.text_input("Escriba el punto para buscar", [1., 1.])   
        Num = st.number_input("Escriba el número deseado de variables", value=2)
        st.write("Nota: El valor inicial se generará aleatoriamente")

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
            fun = funMultivariable.RastriginFunction
            answer, best = unidireccional.busquedaUnidireccional(Num, limInf, limSup, epsilon, funMultivariable.RastriginFunction)


        elif(option == "Función de Ackley"):
            limInf = st.number_input("Escriba el límite inferior", value=-5.00)
            limSup = st.number_input("Escriba el límite superior", value=5.00)
            st.write("Función:")
            latext1 = r'''
            $$ 
            f(x, y) = -20exp[-0.2\sqrt{0.5(x^{2}+y^{2})}]
            $$  
            '''
            latext2 = r'''
            $$ 
            - exp[0.5(cos(2\pi x) + cos(2\pi y))] + e + 20
            $$  
            '''
            st.write(latext1, latext2)
            
            funcion = funMultivariable.ackley([limInf, limSup])
            fun = funMultivariable.ackley
            answer, best = unidireccional.busquedaUnidireccional(Num, limInf, limSup, epsilon, funMultivariable.ackley)


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
            fun = funMultivariable.SphereFunction
            answer, best = unidireccional.busquedaUnidireccional(Num, limInf, limSup, epsilon, funMultivariable.SphereFunction)


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
            fun = funMultivariable.RosenbrockFunction
            answer, best = unidireccional.busquedaUnidireccional(Num, limInf, limSup, epsilon, funMultivariable.RosenbrockFunction)

            
        elif(option == "Función de Beale"):
            limInf = st.number_input("Escriba el límite inferior", value=-4.50)
            limSup = st.number_input("Escriba el límite superior", value=4.50)
            st.write("Función:")
            latext1 = r'''
            $$ 
            f(x, y) = (1.5−x+xy)^{2}+(2.25−x+xy^{2})^{2}
            $$  
            '''
            latext2 = r'''
            $$ 
            +(2.625−x+xy^{3})^{2}
            $$  
            '''
            st.write(latext1, latext2)

            funcion = funMultivariable.beale([limInf, limSup])
            fun = funMultivariable.beale
            answer, best = unidireccional.busquedaUnidireccional(Num, limInf, limSup, epsilon, funMultivariable.beale)


        elif(option == "Función de Booth"):
            limInf = st.number_input("Escriba el límite inferior", value=-10.00)
            limSup = st.number_input("Escriba el límite superior", value=10.00)
            st.write("Función:")
            latext1 = r'''
            $$ 
            f(x, y) = (x+2y-7)^{2}+(2x+y-5)^{2}
            $$  
            '''
            st.write(latext1)

            funcion = funMultivariable.booth([limInf, limSup])
            fun = funMultivariable.booth
            answer, best = unidireccional.busquedaUnidireccional(Num, limInf, limSup, epsilon, funMultivariable.booth)


        elif(option == "Función de Himmelblaus"):
            limInf = st.number_input("Escriba el límite inferior", value=-5.00)
            limSup = st.number_input("Escriba el límite superior", value=5.00)
            st.write("Función:")
            latext1 = r'''
            $$ 
            f(x, y) = (x^{2}+y-11)^{2}+(x+y^{2}-7)^{2}
            $$  
            '''
            st.write(latext1)

            funcion = funMultivariable.himmelblaus([limInf, limSup])
            fun = funMultivariable.himmelblaus
            answer, best = unidireccional.busquedaUnidireccional(Num, limInf, limSup, epsilon, funMultivariable.himmelblaus) 
        

        else:
            limInf = st.number_input("Escriba el límite inferior", value=-3.00)
            limSup = st.number_input("Escriba el límite superior", value=4.00)
            st.write("Función:")
            latext1 = r'''
            $$ 
            f(x, y) = sen(x+y)+(x-y)^{2}-1.5x + 2.5y + 1
            $$  
            '''
            st.write(latext1)

            funcion = funMultivariable.mccormick([limInf, limSup])
            fun = funMultivariable.mccormick
            answer, best = unidireccional.busquedaUnidireccional(Num, limInf, limSup, epsilon, funMultivariable.mccormick) 
            
        submitted = st.form_submit_button("Submit")

with col2:
    if submitted:
        unidireccional.graficar(limInf, limSup, limInf, limSup, best, s, fun)
        st.write("Valor de alfa: ", answer)
        st.write("Mejor punto: ", best)
        st.write("Resultado de la función: ", funcion)
