import streamlit as st
from funciones import FuncionesMultivariables as funMultivariable
from algoritmos import INelderMead_actividad as nelderMead

st.title("Nelder Mead (Simplex)")
st.markdown('<div style="text-align: justify;">Planteado por John A. Nelder y Roder Mead en 1965. Para funcionar, requiere de D+1 puntos iniciales (donde D es el número de ' \
'variables del problema), con estos se forma el simplex original, que no debe de formar un hipercubo del problema (debe tener dos dimensiones ' \
'o volumen). Básicamente, si en una función hay dos variables, los tres puntos no debe de estar en una línea, y si tiene tres variables, los cuatro puntos ' \
'no deben de estar en un plano. </div>', unsafe_allow_html=True)

st.markdown('<div style="text-align: justify;"> </div>', unsafe_allow_html=True)

st.markdown('<div style="text-align: justify;">En cada iteración, primero se busca el peor punto en el simplex, luego se genera uno nuevo al alejarse del peor punto (para ello se siguen las reglas ' \
'presentadas en el siguiente algoritmo). Esta búsqueda depende de las funciones relativas al simplex, siendo las más comunes: </div>', unsafe_allow_html=True)

st.image("pagina/simplex.png", caption="Ilustración del método Simplex, mostrando la reflexión, expansión y dos contracciones.")

st.markdown('<div style="text-align: justify;">A grandes rasgos, primero se determina el centroide (opuesto al peor punto), luego se refleja este peor punto, y dependiendo de un conjunto de funciones ' \
'se determina si se debe de expandir o contraer el área de búsqueda. Este proceso se repite hasta que la distancia entre puntos sea menor a un valor predeterminado.</div>', unsafe_allow_html=True)

st.latex(r"""
\begin{array}{l}
\textbf{Algoritmo: Nelder Mead (Simplex)} \\
\rule{14cm}{1pt}\\
\textbf{Definir: } \gamma \gt  1, \beta \in (0, 1), \epsilon \\[0.8 ex] 
\textbf{Nota: }  \text{Crear un simplex inicial.} \\[0.8 ex] 
         \\
\textbf{Paso 1: } \text{Encontrar el peor punto } x_{h} \text{,  el mejor punto } x_{l} \text{ y el siguiente peor punto } x_{g} \\[0.8 ex] 
         
\textbf{Paso 2: } \text{Calcular } x_{c} = \frac{1}{N} \sum_{i=1, i\neq h}^{N+1} x_{i} \\[0.8 ex] 

\textbf{Paso 3: } \text{Calcular el punto reflejado } x_{r} = 2 x_{c} - x_{k} \text{. Definir } x_{new} = x_{r} \\[0.8 ex]    
\quad \quad \text{Si } f(x_{r}) \lt f(x_{l}) \text{, definir } x_{new} =  (1 + \gamma)x_{c} - \gamma x_{h} \text{ (expansión).} \\[0.8 ex] 
\quad \quad \text{Si no, si } f(x_{r}) \ge f(x_{h}) \text{, definir } x_{new} =  (1 + \beta)x_{c} + \beta x_{h} \text{ (contracción 1).} \\[0.8 ex] 
\quad \quad \text{Si no, si } f(x_{g}) \lt f(x_{r}) \lt f(x_{h}) \text{, definir } x_{new} =  (1 + \beta)x_{c} - \beta x_{h} \text{ (contracción 2).} \\[0.8 ex] 
\quad \quad \text{Calcular } f(x_{new}) \text{ y  reemplazar } x_{h}  \text{ con } x_{new}\\[0.8 ex] 

\textbf{Paso 4: } \text{Si } \Bigg\{\sum_{i=1}^{N+1} \frac{(f(x_{i}) - f(x_{c}))^{2}}{N+1}\Bigg\}^{1/2} \le \epsilon \text{, Terminar. Si no, ir al paso 1.} \\[0.8 ex]             
\end{array}
""")

st.markdown('<div style="text-align: justify;">En realidad se puede usar cualquier otro criterio para la conlusión, considerando que el desempeño del algoritmo depende ' \
'de β y γ, ya que si se aplica un valor grande, se acercará al óptimo más rápidamente, pero su convergencia se complicará, mientras que con el caso contrario ' \
'requerirá de más evaluaciones de funciones para convergir al óptimo. Por ello, es recomendable usar los valores: γ cercano a 2.0 y |β| a 0.5 </div>', unsafe_allow_html=True)

st.header("Resolución de Problemas")
col1, col2 = st.columns(2)
with col1:
    with st.form("my_form"):
        option = st.selectbox(
            "¿Qué función desea?",
            ("Función de Rastrigin", "Función de Ackley", "Función Esfera", "Función de Rosenbrock", "Función de Beale", 
            "Función de Booth", "Función de Himmelblaus", "Función de McCormick")
        )
        
        alpha = st.slider("Selección del valor de alpha (α)", 0.10, 2.00, value=1.00)
        gamma =  st.slider("Selección del valor de gamma (γ)", 1.00, 5.00, value=1.20)
        beta = st.slider("Selección del valor de beta (β)", 0.01, 1.00, value=0.50)
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
            answer, best = nelderMead.NelderMead(Num, alpha, gamma, beta, epsilon, limInf, limSup, funMultivariable.RastriginFunction)
            
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
            answer, best = nelderMead.NelderMead(Num, alpha, gamma, beta, epsilon, limInf, limSup, funMultivariable.ackley)
            
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
            answer, best = nelderMead.NelderMead(Num, alpha, gamma, beta, epsilon, limInf, limSup, funMultivariable.SphereFunction)
            
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

            funcion = funMultivariable.RastriginFunction
            fun = funMultivariable.RastriginFunction
            answer, best = nelderMead.NelderMead(Num, alpha, gamma, beta, epsilon, limInf, limSup, funMultivariable.RastriginFunction)

            
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
            answer, best = nelderMead.NelderMead(Num, alpha, gamma, beta, epsilon, limInf, limSup, funMultivariable.beale) 
            
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
            answer, best = nelderMead.NelderMead(Num, alpha, gamma, beta, epsilon, limInf, limSup, funMultivariable.booth) 
            
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
            answer, best = nelderMead.NelderMead(Num, alpha, gamma, beta, epsilon, limInf, limSup,funMultivariable.himmelblaus) 
        
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
            answer, best = nelderMead.NelderMead(Num, alpha, gamma, beta, epsilon, limInf, limSup, funMultivariable.mccormick) 
            
        submitted = st.form_submit_button("Submit")

with col2:
    if submitted:
        nelderMead.graficar(limInf, limSup, limInf, limSup, answer, fun)
        st.write("Mejor punto: ", best)
        st.write("Resultado de la función: ", funcion)
