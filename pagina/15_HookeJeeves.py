import streamlit as st
from funciones import FuncionesMultivariables as funMultivariable
from algoritmos import JHookeJeeves as hookeJeeves

st.title("Hooke Jeeves")
st.markdown('<div style="text-align: justify;">Funciona al crear un conjunto de direcciones de búsqueda de manera iterativa, de forma en que se cubra completamente el espacio de búsqueda. Es decir, encontrándose en un punto ' \
'del espacio, se puede alcanzar cualquier otro atravesando solamente estas direcciones. Así, en un problema de dimensión N requiere al menos N direcciones de búsqueda linealmente ' \
'independientes. Por ejemplo, en una función de dos variables, requiere al menos dos direcciones de búsqueda para llegar de un punto a otro, de manera que algunas de estas combinaciones puede ' \
'que lleguen al destino con menos iteraciones, y otras requieran de más pruebas.</div>', unsafe_allow_html=True)

st.markdown('<div style="text-align: justify;"> </div>', unsafe_allow_html=True)

st.markdown('<div style="text-align: justify;">En este método se aplica una combinación de movimientos exploratorios y de patrón heurísticos, de forma que primero se realiza la exploración en el vecindario del ' \
'punto, buscando sistematicamente el mejor, y luego se eligen dos puntos para realizar el patrón, de la siguiente forma:</div>', unsafe_allow_html=True)

st.subheader("Movimiento Exploratorio")
latex_expr = "x^{c}"
latex_expr1 = "\mathrm{x}_{i}^{c}"
latex_expr2 = "\Delta_{i}"
st.write(f"Se asume que la solución actual, que sirve como punto base, está denotada por ${latex_expr}$, así como que ${latex_expr1}$ es perturbada por ${latex_expr2}$.")

st.latex(r"""
\begin{array}{l}
\textbf{Algoritmo: Movimiento Exploratorio} \\
\rule{14cm}{1pt}\\
\textbf{Definir: } i = 1, x = x^{c}\\[0.5 ex] 
         \\
\textbf{Paso 1: } \text{Calcular } f = f(x), f_{+} = f(x_{i} + \Delta_{i}), f_{-} = f(x_{i} - \Delta_{i}) \\[0.5 ex] 
         
\textbf{Paso 2: } \text{Encontrar } f_{min} = min(f, f_{+}, f_{-}) \text{. Declarar x que corresponda a la función mínima.} \\[0.5 ex] 

\textbf{Paso 3: } \text{Si i no es igual a N, sumarle 1 a i, y volver al Paso 1. Si lo es, ir al Paso 4.}\\[0.5 ex] 
         
\textbf{Paso 4: } \text{Si x es diferente de xᶜ, Éxito. Si no, Fallo. } \\[0.5 ex] 
         
\end{array}
""")

st.markdown('<div style="text-align: justify;">De esta forma, con el movimiento exploratorio se modifica el punto tanto en direcciones positivas como negativas para cada variable, una dirección a la vez, y se guarda el mejor punto. ' \
'El actual se modifica con lo obtenido en cada prueba, y si lo encontrado al final es diferente del original, se considera que el movimiento tuvo éxito, o en el caso contrario, es un fallo. En cualquiera de las dos formas, el mejor ' \
'punto es la salida de este movimiento exploratorio.</div>', unsafe_allow_html=True)

st.subheader("Movimiento de Patrón")

latex_expr = "x^{c}"
latex_expr1 = "x^{k-1}"
latex_expr2 = "\mathrm{x}_{p}^{(k+1)} = x^{(k)} + (x^{(k)} - x^{(k-1)})"
st.write(f"Se encuentra un nuevo punto al saltar desde el mejor punto actual ${latex_expr}$, en una dirección determinada, conectando con el mejor punto anterior ${latex_expr1}$ y la base actual ${latex_expr2}$.")

st.markdown('<div style="text-align: justify;">Así, este método incluye la aplicación iterativa de un movimiento exploratorio del punto actual y luego un salto con el de patrón. Por lo que si no lleva a una mejor región, ' \
'no es aceptado y se reduce el área para la exploración.</div>', unsafe_allow_html=True)

st.latex(r"""
\begin{array}{l}
\textbf{Algoritmo: Hooke Jeeves (Búsqueda de Patrón)} \\
\rule{14cm}{1pt}\\
\textbf{Definir: } x^{(0)}, \epsilon \\[0.5 ex] 
         \\
\textbf{Paso 1: } \text{Mientras } ||\Delta|| \text{ sea menor a } \epsilon \text{, hacer los siguientes pasos:}\\[0.5 ex] 
         
\quad \textbf{Paso 2: } \text{Realizar un movimiento exploratorio, basado en } x_{i} \\[0.5 ex] 

\quad \textbf{Paso 3: } \text{Si el movimiento de patrón es exitoso, entonces realizar movimiento de patrón.}\\[0.5 ex] 
\quad \quad \quad \quad\text{Si no, } \Delta  = \Delta \div \alpha         
         
\end{array}
""")

st.markdown('<div style="text-align: justify;">La estrategia es sencilla y directa, por lo que requiere de menos variables (solo el punto actual y el siguiente), además de que los cálculos son sencillos, pero esta naturaleza también lo lleva a ser impredecible, ya que ' \
'puede tomar alguna ruta equivocada al inicio, especialmente cuando las variables son no lineales, y solo termina al hacer una búsqueda exhaustiva del punto de convergencia.</div>', unsafe_allow_html=True)

st.header("Resolución de Problemas")
col1, col2 = st.columns(2)
with col1:
    with st.form("my_form"):
        option = st.selectbox(
            "¿Qué función desea?",
            ("Función de Rastrigin", "Función de Ackley", "Función Esfera", "Función de Rosenbrock", "Función de Beale", 
            "Función de Booth", "Función de Himmelblaus", "Función de McCormick")
        )
        
        alpha = st.slider("Seleccione el valor de alpha (α)", 0.01, 5.00, value=2.00)
        epsilon = st.slider("Seleccione el valor de epsilon", 0.01, 1.00)
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
            answer, best = hookeJeeves.HookeJeeves(Num, epsilon, alpha, limInf, limSup, funMultivariable.RastriginFunction)
            
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
            answer, best = hookeJeeves.HookeJeeves(Num, epsilon, alpha, limInf, limSup, funMultivariable.ackley)

            
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
            answer, best = hookeJeeves.HookeJeeves(Num, epsilon, alpha, limInf, limSup, funMultivariable.SphereFunction)

            
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
            answer, best = hookeJeeves.HookeJeeves(Num, epsilon, alpha, limInf, limSup, funMultivariable.RosenbrockFunction)


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
            answer, best = hookeJeeves.HookeJeeves(Num, epsilon, alpha, limInf, limSup, funMultivariable.beale)

            
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
            answer, best = hookeJeeves.HookeJeeves(Num, epsilon, alpha, limInf, limSup, funMultivariable.booth)

            
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
            answer, best = hookeJeeves.HookeJeeves(Num, epsilon, alpha, limInf, limSup, funMultivariable.himmelblaus) 
        
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
            answer, best = hookeJeeves.HookeJeeves(Num, epsilon, alpha, limInf, limSup, funMultivariable.mccormick)
            
        submitted = st.form_submit_button("Submit")

with col2:
    if submitted:
        hookeJeeves.graficar(limInf, limSup, limInf, limSup, answer, fun)
        st.write("Mejor punto: ", best)
        st.write("Resultado de la función: ", funcion)
