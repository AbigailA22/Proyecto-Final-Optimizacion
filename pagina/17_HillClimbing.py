import streamlit as st
from funciones import FuncionesMultivariables as funMultivariable
from algoritmos import LHillClimbing as hill

st.title("Ascenso o Descenso de la Colina") 
st.markdown('<div style="text-align: justify;">En este algoritmo también se generan soluciones de manera aleatoria a partir de un punto determinado, pero la diferencia radica en que solo se cambia la ' \
'posición si es mejor que la anterior.</div>', unsafe_allow_html=True)

st.markdown('<div style="text-align: justify;"> </div>', unsafe_allow_html=True)

st.markdown('<div style="text-align: justify;">Su nombre surge de imaginarse que uno se encuentra en un punto determinado de una colina, y se desea llegar al punto más alto (máximo), o ir hacia la base (mínimo). Para ' \
'hacer este recorrido se debe de escoger un camino a seguir, el cual se va verificando conforme se avanza: solamente se continúa si los pasos que se han seguido han llevado a un acercamiento al punto deseado, ' \
'ya que de lo contrario no tiene sentido realizar el recorrido. Esta idea funciona todavía mejor porque las gráficas de las funciones 3D son similares a este movimiento en una colina.</div>', unsafe_allow_html=True)

st.latex(r"""
\begin{array}{l}
\textbf{Algoritmo: Ascenso o Descenso de la Colina} \\
\rule{14cm}{1pt}\\
\textbf{Definir: }  \text{Función Objetivo}, \epsilon, x_{0}\\[0.5 ex] 
\textbf{Nota: }  \text{Definir } x_{best} \text{ como la mejor solución hasta el momento. Inicia como } x_{0}\\[0.5 ex] 
         \\
\textbf{Paso 1: } \text{Mientras no se cumpla la función de paro, por ejemplo: } f(x_{best}) \ge  \epsilon \\[0.5 ex] 
         
\quad \textbf{Paso 2: } x_{k+1} = \text{ generación aleatoria de punto } x_{k}\\[0.5 ex] 

\quad \textbf{Paso 3: } \text{ Si }  f(x_{k+1}) \lt f(x_{best})  \\[0.5 ex] 
\quad \quad \quad \quad x_{best} = x_{k+1} \\[0.5 ex] 
             
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
            answer, best = hill.hillClimbing(epsilon, Num, limInf, limSup, funMultivariable.RastriginFunction)


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
            answer, best = hill.hillClimbing(epsilon, Num, limInf, limSup, funMultivariable.ackley)


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
            answer, best = hill.hillClimbing(epsilon, Num, limInf, limSup, funMultivariable.SphereFunction)


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
            answer, best = hill.hillClimbing(epsilon, Num, limInf, limSup, funMultivariable.RosenbrockFunction)

            
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
            answer, best = hill.hillClimbing(epsilon, Num, limInf, limSup, funMultivariable.beale)


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
            answer, best = hill.hillClimbing(epsilon, Num, limInf, limSup, funMultivariable.booth)


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
            answer, best = hill.hillClimbing(epsilon, Num, limInf, limSup, funMultivariable.himmelblaus) 
        

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
            answer, best = hill.hillClimbing(epsilon, Num, limInf, limSup, funMultivariable.mccormick) 

        submitted = st.form_submit_button("Submit")

with col2:
    if submitted:
        hill.graficar(limInf, limSup, limInf, limSup, answer, fun)
        st.write("Mejor punto: ", best)
        st.write("Resultado de la función: ", funcion)