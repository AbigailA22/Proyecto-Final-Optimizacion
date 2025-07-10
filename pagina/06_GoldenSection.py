import streamlit as st
import pandas as pd
import altair as alt
import time

from funciones import FuncionesUnimodales_19marzo2025 as funcionUnimodal
from algoritmos import EGoldenSection as golden

st.title("Búsqueda por Sección Dorada")
st.markdown('<div style="text-align: justify;">Muchas veces se considera una mejora del Método de Fibonacci, porque soluciona dos de sus principales problemas: ' \
'Fibonacci requiere de calcular y guardar todos los números necesarios de la serie (ocupando mucho espacio de memoria), ' \
'además de que en cada iteración la proporción de la región eliminada no es la misma. Por ello, en este algoritmo el espacio de ' \
'búsqueda se mapea para que tenga un intervalo de (0, 1). Luego, se mapean dos puntos de tamaño φ, para que en cada iteración ' \
'la región eliminada sea (1 - φ) de la eliminación previa.</div>', unsafe_allow_html=True)

st.write("Como nota, φ (phi) es el número dorado o de proporción aurea. Este es calculado con: ") 
st.latex(''' (1 + \sqrt{5}) \div{2} = 1.618033988 . ''') 

st.latex(r"""
\begin{array}{l}
\textbf{Algoritmo: Búsqueda por Sección Dorada} \\
\rule{14cm}{1pt}\\
\textbf{Definir: } a \text{ (Límite Inferior), } b \text{ (Límite Superior), } \epsilon \text{ (Error Aceptado), } k = 1 \\[0.5 ex] 
        \text{Normalizar la variable x con la ecuación: } w = \frac{x-a}{b-a} \text{. Así } a^{w} = 0, b^{w} = 1, L^{w} = 1\\[0.5 ex] 
         \\
\textbf{Paso 1: } \text{Definir } w_{1} = a^{w} + 0.618 \cdot L^{w},  w_{2} = b^{w} + 0.618 \cdot L^{w}\\[0.5 ex] 
         
\textbf{Paso 2: } \text{Calcular } f(w_{1}) \text{ o } f(w_{2}) \text{, el que no se haya evaluado antes.}\\[0.5 ex] 
\quad \quad \text{Usar las reglas de Eliminación de Regiones para determinar nuevo } a^{w} \text{ y } b^{w} \\[0.5 ex] 
         
\textbf{Paso 3: } \text{Calcular } L = b^{w} - a^{w}  \text{. Si } |L| \lt \epsilon \text{, Terminar.}\\[0.5 ex] 
\quad \quad \text{Si no, determinar k = k + 1, e ir al Paso 1.} \\[0.5 ex] 
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
            x1, x2, px, py = golden.golden_section(limInf, limSup, values, funcionUnimodal.lata)

        elif(option == "Caja"):
            limInf = st.number_input("Escriba el límite inferior", value=2.00)
            limSup = st.number_input("Escriba el límite superior", value=3.00)
            st.write("Función: -(4l³ - 60l² + 200l)")
            funcion = funcionUnimodal.caja(values)
            x1, x2, px, py = golden.golden_section(limInf, limSup, values, funcionUnimodal.caja)

        elif(option == "Función 1"):
            limInf = st.number_input("Escriba el límite inferior", value=-2.00)
            limSup = st.number_input("Escriba el límite superior", value=2.00)
            st.write("Función: x² + 3")
            funcion = funcionUnimodal.ej1(values) 
            x1, x2, px, py = golden.golden_section(limInf, limSup, values, funcionUnimodal.ej1)

        elif(option == "Función 2"):
            limInf = st.number_input("Escriba el límite inferior", value=0.001)
            limSup = st.number_input("Escriba el límite superior", value=10.000)
            st.write("Función: x² + (54/x)")
            funcion = funcionUnimodal.ej4(values)
            x1, x2, px, py = golden.golden_section(limInf, limSup, values, funcionUnimodal.ej4)

        elif(option == "Función 3"):
            limInf = st.number_input("Escriba el límite inferior", value=0.00)
            limSup = st.number_input("Escriba el límite superior", value=5.00)
            st.write("Función: x³ + 2x - 3")
            funcion = funcionUnimodal.ej5(values) 
            x1, x2, px, py = golden.golden_section(limInf, limSup, values, funcionUnimodal.ej5)

        elif(option == "Función 4"):
            limInf = st.number_input("Escriba el límite inferior", value=-2.50)
            limSup = st.number_input("Escriba el límite superior", value=2.50)
            st.write("Función: x⁴ + x² - 33")
            funcion = funcionUnimodal.ej6(values)
            x1, x2, px, py = golden.golden_section(limInf, limSup, values, funcionUnimodal.ej6)

        else:
            limInf = st.number_input("Escriba el límite inferior", value=-1.50)
            limSup = st.number_input("Escriba el límite superior", value=3.00)
            st.write("Función: 3x⁴ - 8x³ - 6x² - 12x") 
            funcion = funcionUnimodal.ej7(values)
            x1, x2, px, py = golden.golden_section(limInf, limSup, values, funcionUnimodal.ej7)                   
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

