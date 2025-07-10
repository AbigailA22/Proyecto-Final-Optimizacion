import streamlit as st
import pandas as pd
import altair as alt
import time

from funciones import FuncionesUnimodales_19marzo2025 as funcionUnimodal
from algoritmos import DFibonacciSearch as fibonacci

st.title("Búsqueda por Fibonacci")
st.markdown('<div style="text-align: justify;">En este método el intervalo de búsqueda disminuye acorde a la secuencia de números de Fibonacci. La propiedad principal de esta secuencia ' \
'es que, dados dos números consecutivos, el siguiente se calcula al realizar la suma de los dos anteriores, es decir, ' \
'Fₙ = Fₙ₋₁ + Fₙ₋₂. La serie inicia de la siguiente manera: 0, 1, 1, 2, 3, 5, 8, 13, ... hasta el infinito..</div>', unsafe_allow_html=True)

st.markdown('<div style="text-align: justify;">Esta propiedad permite que solo sea necesario evaluar una función por cada iteración, debido a que uno de los valores siempre ' \
'se mantiene igual, mientras que el otro es nuevo, disminuyendo así la necesidad de procesamiento durante las evaluaciones.</div>', unsafe_allow_html=True)

st.latex(r"""
\begin{array}{l}
\textbf{Algoritmo: Búsqueda por Fibonacci} \\
\rule{14cm}{1pt}\\
\textbf{Definir: } a \text{ (Límite Inferior), } b \text{ (Límite Superior), } L = b - a, k = 2, n \text{ (Número de evaluaciones).}\\[0.5 ex] 
         \\
\textbf{Paso 1: } \text{Calcular } L_{k} = \frac{F_{n-k+1}}{F_{n+1}} \text{. Definir } x_{1} = a + L_{k}, x = b - L_{k} \\[0.5 ex] 
         
\textbf{Paso 2: } \text{Calcular } f(x_{1}) \text{ o } f(x_{2}) \text{, el que no se haya evaluado antes.} \\[0.5 ex] 
\quad \quad \text{Usar las reglas de Eliminación de Regiones para determinar nuevo a y b.} \\[0.5 ex] 
         
\textbf{Paso 3: } \text{Si } k \neq  n \text{, definir k = k + 1 e ir al Paso 1.}\\[0.5 ex] 
\quad \quad \text{Si no, Terminar.} \\[0.5 ex] 
\end{array}
""")

st.header("Resolución de Problemas")
col1, col2 = st.columns(2)
with col1:
    with st.form("my_form"):
        option = st.selectbox(
            "¿Qué función desea optimizar?",
            ("Lata", "Caja", "Función 1", "Función 2", "Función 3", "Función 4", "Función 5")
        )

        values = st.slider("Selección del valor de epsilon", 0.01, 1.00)

        if(option == "Lata"):
            limInf = st.number_input("Escriba el límite inferior", value=0.20)
            limSup = st.number_input("Escriba el límite superior", value=5.00)
            st.write("Función: 2πr² + (500 / r)")
            funcion = funcionUnimodal.lata(values)
            x1, x2, px, py = fibonacci.fibonacci_search(limInf, limSup, values, funcionUnimodal.lata)

        elif(option == "Caja"):
            limInf = st.number_input("Escriba el límite inferior", value=2.00)
            limSup = st.number_input("Escriba el límite superior", value=3.00)
            st.write("Función: -(4l³ - 60l² + 200l)")
            funcion = funcionUnimodal.caja(values)
            x1, x2, px, py = fibonacci.fibonacci_search(limInf, limSup, values, funcionUnimodal.caja)

        elif(option == "Función 1"):
            limInf = st.number_input("Escriba el límite inferior", value=-2.00)
            limSup = st.number_input("Escriba el límite superior", value=2.00)
            st.write("Función: x² + 3")
            funcion = funcionUnimodal.ej1(values) 
            x1, x2, px, py = fibonacci.fibonacci_search(limInf, limSup, values, funcionUnimodal.ej1)

        elif(option == "Función 2"):
            limInf = st.number_input("Escriba el límite inferior", value=0.001)
            limSup = st.number_input("Escriba el límite superior", value=10.000)
            st.write("Función: x² + (54/x)")
            funcion = funcionUnimodal.ej4(values)
            x1, x2, px, py = fibonacci.fibonacci_search(limInf, limSup, values, funcionUnimodal.ej4)

        elif(option == "Función 3"):
            limInf = st.number_input("Escriba el límite inferior", value=0.00)
            limSup = st.number_input("Escriba el límite superior", value=5.00)
            st.write("Función: x³ + 2x - 3")
            funcion = funcionUnimodal.ej5(values) 
            x1, x2, px, py = fibonacci.fibonacci_search(limInf, limSup, values, funcionUnimodal.ej5)

        elif(option == "Función 4"):
            limInf = st.number_input("Escriba el límite inferior", value=-2.50)
            limSup = st.number_input("Escriba el límite superior", value=2.50)
            st.write("Función: x⁴ + x² - 33")
            funcion = funcionUnimodal.ej6(values)
            x1, x2, px, py = fibonacci.fibonacci_search(limInf, limSup, values, funcionUnimodal.ej6)

        else:
            limInf = st.number_input("Escriba el límite inferior", value=-1.50)
            limSup = st.number_input("Escriba el límite superior", value=3.00)
            st.write("Función: 3x⁴ - 8x³ - 6x² - 12x") 
            funcion = funcionUnimodal.ej7(values)
            x1, x2, px, py = fibonacci.fibonacci_search(limInf, limSup, values, funcionUnimodal.ej7)                   
        st.write("Values: ", funcion)

        st.write("El mínimo está en el intervalo:", x1, x2)
        submitted = st.form_submit_button("Submit")

with col2:
    if submitted:
        df = pd.DataFrame({
            "x": px,
            "y": py,
        })

        chart_placeholder = st.empty()

        progress_bar = st.sidebar.progress(0)
        status_text = st.sidebar.empty()
        progressive_data = pd.DataFrame(columns=["x", "y"])

        for i in range(1, len(df) + 1):
            progressive_data = df.iloc[:i]
            
            line_chart = (
                alt.Chart(progressive_data).mark_line(point=True).encode(x="x", y="y")
            )
            chart_placeholder.altair_chart(line_chart, use_container_width=True)
            
            status_text.text(f"{i}/{len(df)} points added")
            progress_bar.progress(i / len(df))
            time.sleep(0.1)
        progress_bar.empty()


