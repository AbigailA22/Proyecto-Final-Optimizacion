import streamlit as st
from funciones import FuncionesMultivariables as funMultivariable
from algoritmos import NMetodoCauchy as cauchy

st.title("Método de Cauchy (Descenso Más Pronunciado)")
st.markdown('<div style="text-align: justify;">Usa el gradiente negativo como la dirección de búsqueda desde un punto particular x⁽ᵗ⁾. Esto se representa con la siguiente fórmula.</div>', unsafe_allow_html=True)

latext1 = r'''
$$ 
s^{(k)} = - \nabla f(x^{(k)})
$$  
'''
st.write(latext1)

st.markdown('<div style="text-align: justify;">Debido a que esta dirección da el descenso máximo considerando los valores de las funciones, se conoce como el descenso más pronunciado. De esta forma, en cada iteración se ' \
'encuentra la derivada del punto actual, y se realiza una búsqueda unidireccional, considerando su negativo, para encontrar el punto mínimo en esa dirección. Una vez hallado, se vuelve el punto actual, ' \
'y la búsqueda continúa desde ese punto, repitiéndose hasta que se encuentre un punto con el gradiente lo suficientemente pequeño.</div>', unsafe_allow_html=True)

st.latex(r"""
\begin{array}{l}
\textbf{Algoritmo: Método de Cauchy (Descenso Más Pronunciado)} \\
\rule{14cm}{1pt}\\
\textbf{Definir: } M \text{ (Número máximo de iteraciones)}, x_{0}, \epsilon_{1}, \epsilon_{2}, k = 0\\[0.5 ex] 
         \\
\textbf{Paso 1: } \text{Calcular la gradiente de } x^{(0)} \text{, así como su primera derivada.} \\[0.5 ex] 
         
\textbf{Paso 2: }  \text{Si la magnitud de la gradiente es menor o igual a } \epsilon_{1} \text{, o } k \ge M \text{, Terminar}\\[0.5 ex] 
\quad \quad \text{Si no, ir al paso 3.}\\[0.5 ex] 
         
\textbf{Paso 3: } \text{Realizar una búsqueda unidireccional para encontrar }  \alpha^{(k)} \\[0.5 ex] 
\quad \quad \quad \quad \text{ usando ϵ₂ para minimizar } f(x^{k+1}) = f(x^{k} - \alpha \nabla f(x^{k})) \\[0.5 ex] 
         

\textbf{Paso 4: }  \text{Si } \frac{x^{(k+1)} - x^{(k)}}{|x^{(k)}|} \lt \epsilon_{1} \text{, Terminar.} \\[0.5 ex] 
\quad \quad \quad \quad \text{Si no, k = k + 1, e ir al paso 3.}  \\[0.5 ex]            
\end{array}
""")

st.markdown('<div style="text-align: justify;">Este algoritmo garantiza la mejora en cada iteración, además, funciona mejor cuando x⁽⁰⁾ se encuentra lejos del óptimo, ya que si el punto actual está muy cercano al buscado, el cambio en el gradiente es muy pequeño, ' \
'haciendo que la convergencia sea lenta. Por ello, si se desea volver más rápido, se pueden utilizar derivadas de segundo orden.</div>', unsafe_allow_html=True)

st.header("Resolución de Problemas")
col1, col2 = st.columns(2)
with col1:
    with st.form("my_form"):
        option = st.selectbox(
            "¿Qué función desea?",
            ("Función de Rastrigin", "Función de Ackley", "Función Esfera", "Función de Rosenbrock", "Función de Beale", 
            "Función de Booth", "Función de Himmelblaus", "Función de McCormick")
        )
        
        epsilon1 = st.slider("Selección del valor de epsilon 1", 0.01, 1.00)
        epsilon2 = st.slider("Selección del valor de epsilon 2", 0.01, 1.00)
        delta = st.slider("Selección del valor de delta", 0.01, 1.00)     
        Num = st.number_input("Escriba el número deseado de variables", value=2)
        M = st.number_input("Escriba el número máximo de iteraciones", value=100)

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
            answer, best = cauchy.cauchy(Num, epsilon1, epsilon2, delta, M, limInf, limSup, funMultivariable.RastriginFunction)


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
            answer, best = cauchy.cauchy(Num, epsilon1, epsilon2, delta, M, limInf, limSup, funMultivariable.ackley)


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
            answer, best = cauchy.cauchy(Num, epsilon1, epsilon2, delta, M, limInf, limSup, funMultivariable.SphereFunction)


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
            answer, best = cauchy.cauchy(Num, epsilon1, epsilon2, delta, M, limInf, limSup, funMultivariable.RosenbrockFunction)

            
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
            answer, best = cauchy.cauchy(Num, epsilon1, epsilon2, delta, M, limInf, limSup, funMultivariable.beale)


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
            answer, best = cauchy.cauchy(Num, epsilon1, epsilon2, delta, M, limInf, limSup, funMultivariable.booth)


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
            answer, best = cauchy.cauchy(Num, epsilon1, epsilon2, delta, M, limInf, limSup, funMultivariable.himmelblaus) 
        

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
            answer, best = cauchy.cauchy(Num, epsilon1, epsilon2, delta, M, limInf, limSup, funMultivariable.mccormick) 
            
        submitted = st.form_submit_button("Submit")

with col2:
    if submitted:
        cauchy.graficar(limInf, limSup, limInf, limSup, answer, fun)
        st.write("Mejor punto: ", best)
        st.write("Resultado de la función: ", funcion)