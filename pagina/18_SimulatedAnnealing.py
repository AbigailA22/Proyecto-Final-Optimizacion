import streamlit as st
from funciones import FuncionesMultivariables as funMultivariable
from algoritmos import MRecocidoSimulado as recocido

st.title("Recocido Simulado")
st.markdown('<div style="text-align: justify;">Desarrollado a mediados de la década de 1980, sin embargo, su inspiración remonta al Algoritmo de Metrópolis, que fue creado por los científicos ' \
'Nicholas Metrópolis, Ariana y Marshall Rosenblouth, Augusta y Edward Teller, participantes del Proyecto Manhattan de 1953. </div>', unsafe_allow_html=True)

st.markdown('<div style="text-align: justify;"> </div>', unsafe_allow_html=True)

st.markdown('<div style="text-align: justify;">Varía de los algoritmos presentados anteriormente respecto a cuando reemplazar su X, que es la solución original, con U, una variación recién modificada. De esta forma, si ' \
'U es mejor que X siempre se reemplaza, pero si es peor, solamente cambia cuando sigue la probabilidad mostrada por la siguiente fórmula:</div>', unsafe_allow_html=True)

latext1 = r'''
$$ 
P(t, U, X) = \frac{f(U)-f(X)}{t}
$$  
'''
st.write(latext1)

st.markdown('<div style="text-align: justify;">Donde t es una unidad de temperatura, U es el punto recién creado, y X es la solución original. De esta forma, si la temperatura es muy alta funciona como una caminata aleatoria, ' \
'mientras que si baja de un punto determinado, empieza a trabajar como descenso de la colina. Así, conforme aumenta el tiempo, disminuye la probabilidad, considerando como guía la de Boltzmann:</div>', unsafe_allow_html=True)

latext2 = r'''
$$ 
P(∆E, T) = e \frac{-f(s')-f(s)}{T}
$$  
'''
st.write(latext2)

st.latex(r"""
\begin{array}{l}
\textbf{Algoritmo: Recocido Simulado} \\
\rule{14cm}{1pt}\\
\textbf{Definir: }  x_{0}, x_{best}, x_{current}, \epsilon, T, k = 0\\[0.5 ex] 
\textbf{Nota: }  \text{T es la temperatura que se desea aplicar.}\\[0.5 ex] 
         \\
\textbf{Paso 1: } \text{Mientras } f(x_{best}) \ge  \epsilon \\[0.5 ex] 
         
\quad \textbf{Paso 2: }\text{Encontrar la temperatura correspondiente, al dividirla entre k + 1}\\[0.5 ex] 
         
\quad \textbf{Paso 3: }\text{Encontrar un nuevo candidato, buscando alrededor del punto actual.}\\[0.5 ex] 

\quad \textbf{Paso 4: } \text{Si }  f(x_{candidate}) \lt f(x_{best}) \text{ O } x_{random} \lt e \frac{-f(x_{current})-f(x_{candidate})}{T} \\[0.5 ex] 
\quad \quad \quad \quad \quad x_{current} = x_{candidate} \\[0.5 ex]
\quad \quad \quad \quad \quad \text{Si } f(x_{candidate}) \lt f(x_{best}\\[0.5 ex]  
\quad \quad \quad \quad \quad \quad \quad f(x_{best}) = f(x_{candidate}\\[0.5 ex]  

\quad \textbf{Paso 5: } k = k + 1\\[0.5 ex]                    
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
        Num = st.number_input("Escriba el número deseado de variables", value=2)
        temperatura = st.number_input("Escriba el valor para la temperatura", value=10.00)

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
            answer, best = recocido.recocidoSimulado(epsilon, Num, limInf, limSup, temperatura, funMultivariable.RastriginFunction)


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
            answer, best = recocido.recocidoSimulado(epsilon, Num, limInf, limSup, temperatura, funMultivariable.ackley)


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
            answer, best = recocido.recocidoSimulado(epsilon, Num, limInf, limSup, temperatura, funMultivariable.SphereFunction)


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
            answer, best = recocido.recocidoSimulado(epsilon, Num, limInf, limSup, temperatura, funMultivariable.RosenbrockFunction)

            
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
            answer, best = recocido.recocidoSimulado(epsilon, Num, limInf, limSup, temperatura, funMultivariable.beale)


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
            answer, best = recocido.recocidoSimulado(epsilon, Num, limInf, limSup, temperatura, funMultivariable.booth)


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
            answer, best = recocido.recocidoSimulado(epsilon, Num, limInf, limSup, temperatura, funMultivariable.himmelblaus) 
        

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
            answer, best = recocido.recocidoSimulado(epsilon, Num, limInf, limSup, temperatura, funMultivariable.mccormick) 

        submitted = st.form_submit_button("Submit")

with col2:
    if submitted:
        recocido.graficar(limInf, limSup, limInf, limSup, answer, fun)
        st.write("Mejor punto: ", best)
        st.write("Resultado de la función: ", funcion)
