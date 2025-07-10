import streamlit as st
import pandas as pd
import altair as alt
import time

from funciones import FuncionesUnimodales_19marzo2025 as funcionUnimodal
from algoritmos import CIntervalHalving as interval

st.title("Intervalos por Mitad")
st.markdown('<div style="text-align: justify;">Para este método se consideran tres puntos que dividen al espacio en cuatro regiones equitativas, ' \
'del límite inferior a x₁, de x₁ a la mitad (xₘ), del medio a x₂ y de esta al límite superior. Luego se aplican las reglas de eliminación de regiones para quitar una porción durante cada búsqueda, ' \
'basado en los valores de las funciones de los puntos escogidos.</div>', unsafe_allow_html=True)

st.latex(r"""
\begin{array}{l}
\textbf{Algoritmo: Intervalos por Mitad} \\
\rule{14cm}{1pt}\\
\textbf{Definir: } a \text{ (Límite Inferior), } b \text{ (Límite Superior), } \epsilon \text{ (Error Aceptado) }, x_{m} = \frac{a+b}{2}, L = b - a \\
         \\
\textbf{Paso 1: } \text{Determinar que} x_{1} = a + \frac{L}{4}, x_{2} = b - \frac{L}{4}\\[0.5 ex] 
         
\textbf{Paso 2: } \text{Si } f(x_{1}) \lt  f(x_{m}) \text{, definir } b = x_{m}, x_{m} = x_{1} \text{ e ir al Paso 4.}\\[0.5 ex] 
\quad \quad \quad \text{Si no, ir al Paso 3} \\

\textbf{Paso 3: } \text{Si } f(x_{2}) \lt  f(x_{m}) \text{, definir } a = x_{m}, x_{m} = x_{2} \text{ e ir al Paso 4.}\\[0.5 ex] 
\quad \quad \quad \text{Si no, } a = x_{1}, b = x_{2} \text{ e ir al Paso 4}\\[0.5 ex] 

\textbf{Paso 4: } \text{Calcular L = b - a. Si } |L| \lt \epsilon \text{, terminar.}\\[0.5 ex] 
\quad \quad \quad \text{Si no, ir al Paso 1.} \\[0.5 ex] 
                           
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
            x1, x2, px, py = interval.interval_halving(limInf, limSup, values, funcionUnimodal.lata)

        elif(option == "Caja"):
            limInf = st.number_input("Escriba el límite inferior", value=2.00)
            limSup = st.number_input("Escriba el límite superior", value=3.00)
            st.write("Función: -(4l³ - 60l² + 200l)")
            funcion = funcionUnimodal.caja(values)
            x1, x2, px, py = interval.interval_halving(limInf, limSup, values, funcionUnimodal.caja)

        elif(option == "Función 1"):
            limInf = st.number_input("Escriba el límite inferior", value=-2.00)
            limSup = st.number_input("Escriba el límite superior", value=2.00)
            st.write("Función: x² + 3")
            funcion = funcionUnimodal.ej1(values) 
            x1, x2, px, py = interval.interval_halving(limInf, limSup, values, funcionUnimodal.ej1)

        elif(option == "Función 2"):
            limInf = st.number_input("Escriba el límite inferior", value=0.001)
            limSup = st.number_input("Escriba el límite superior", value=10.000)
            st.write("Función: x² + (54/x)")
            funcion = funcionUnimodal.ej4(values)
            x1, x2, px, py = interval.interval_halving(limInf, limSup, values, funcionUnimodal.ej4)

        elif(option == "Función 3"):
            limInf = st.number_input("Escriba el límite inferior", value=0.00)
            limSup = st.number_input("Escriba el límite superior", value=5.00)
            st.write("Función: x³ + 2x - 3")
            funcion = funcionUnimodal.ej5(values) 
            x1, x2, px, py = interval.interval_halving(limInf, limSup, values, funcionUnimodal.ej5)

        elif(option == "Función 4"):
            limInf = st.number_input("Escriba el límite inferior", value=-2.50)
            limSup = st.number_input("Escriba el límite superior", value=2.50)
            st.write("Función: x⁴ + x² - 33")
            funcion = funcionUnimodal.ej6(values)
            x1, x2, px, py = interval.interval_halving(limInf, limSup, values, funcionUnimodal.ej6)

        else:
            limInf = st.number_input("Escriba el límite inferior", value=-1.50)
            limSup = st.number_input("Escriba el límite superior", value=3.00)
            st.write("Función: 3x⁴ - 8x³ - 6x² - 12x") 
            funcion = funcionUnimodal.ej7(values)
            x1, x2, px, py = interval.interval_halving(limInf, limSup, values, funcionUnimodal.ej7)                   
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
