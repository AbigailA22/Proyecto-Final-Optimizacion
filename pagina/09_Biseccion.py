import streamlit as st
import pandas as pd
import altair as alt
import time

from funciones import FuncionesUnimodales_19marzo2025 as funcionUnimodal
from algoritmos import GMetodoBiseccion as bis
from algoritmos import BOUNDINGPhase as BP

st.title("Método de Bisección")
st.markdown('<div style="text-align: justify;">A diferencia del método de Newton-Raphson, aquí se evita el cálculo de la segunda derivada. ' \
'En este método, se considera tanto el valor de la función como el signo de la primera derivada en dos puntos para eliminar ' \
'una región del espacio de búsqueda. Así, es similar al método de eliminación de regiones, solo que se usan las derivadas para decidir ' \
'que región eliminar. Por lo mismo, se puede usar un algoritmo de acotamiento para encontrar los límites.</div>', unsafe_allow_html=True)

st.latex(r"""
\begin{array}{l}
\textbf{Algoritmo: Método de Bisección} \\
\rule{14cm}{1pt}\\
\textbf{Definir: } a, b \text{, de forma que } f'(a) \lt  0 \text{ y } f'(b) \gt 0, \epsilon, x_{1} = a, x_{2} = b.\\[0.5 ex] 
         \\
\textbf{Paso 1: } \text{Calcular } z = \frac{x_{2} + x_{1}}{2} \text{ y evaluar } f'(z). \\[0.5 ex] 
         
\textbf{Paso 2: } \text{Si } |f'(z)| \le  \epsilon \text{, terminar.} \\[0.5 ex] 
\quad \quad \text{Si no,  si } f'(z) \lt 0 \text{ determinar que } x_{1} = z \text{ e ir al paso 1.} \\[0.5 ex] 
\quad \quad \text{Si no,  si } f'(z) \gt 0 \text{ determinar que } x_{2} = z \text{ e ir al paso 1.} \\[0.5 ex]          
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
            a, b, c, d = BP.bounding_phase(limInf, limSup, 0.1, funcionUnimodal.lata)
            x1, px, py = bis.biseccion(a, b, values, funcionUnimodal.lata)

        elif(option == "Caja"):
            limInf = st.number_input("Escriba el límite inferior", value=2.00)
            limSup = st.number_input("Escriba el límite superior", value=3.00)
            st.write("Función: -(4l³ - 60l² + 200l)")
            funcion = funcionUnimodal.caja(values)
            a, b, c, d = BP.bounding_phase(limInf, limSup, 0.1, funcionUnimodal.caja)
            x1, px, py = bis.biseccion(a, b, values, funcionUnimodal.caja)

        elif(option == "Función 1"):
            limInf = st.number_input("Escriba el límite inferior", value=-2.00)
            limSup = st.number_input("Escriba el límite superior", value=2.00)
            st.write("Función: x² + 3")
            funcion = funcionUnimodal.ej1(values)
            a, b, c, d = BP.bounding_phase(limInf, limSup, 0.1, funcionUnimodal.ej1) 
            x1, px, py = bis.biseccion(a, b, values, funcionUnimodal.ej1)

        elif(option == "Función 2"):
            limInf = st.number_input("Escriba el límite inferior", value=0.001)
            limSup = st.number_input("Escriba el límite superior", value=10.000)
            st.write("Función: x² + (54/x)")
            funcion = funcionUnimodal.ej4(values)
            a, b, c, d = BP.bounding_phase(limInf, limSup, 0.1, funcionUnimodal.ej4)
            x1, px, py = bis.biseccion(a, b, values, funcionUnimodal.ej4)

        elif(option == "Función 3"):
            limInf = st.number_input("Escriba el límite inferior", value=0.00)
            limSup = st.number_input("Escriba el límite superior", value=5.00)
            st.write("Función: x³ + 2x - 3")
            funcion = funcionUnimodal.ej5(values)
            a, b, c, d = BP.bounding_phase(limInf, limSup, 0.1, funcionUnimodal.ej5) 
            x1, px, py = bis.biseccion(a, b, values, funcionUnimodal.ej5)

        elif(option == "Función 4"):
            limInf = st.number_input("Escriba el límite inferior", value=-2.50)
            limSup = st.number_input("Escriba el límite superior", value=2.50)
            st.write("Función: x⁴ + x² - 33")
            funcion = funcionUnimodal.ej6(values)
            a, b, c, d = BP.bounding_phase(limInf, limSup, 0.1, funcionUnimodal.ej6)
            x1, px, py = bis.biseccion(a, b, values, funcionUnimodal.ej6)

        else:
            limInf = st.number_input("Escriba el límite inferior", value=-1.50)
            limSup = st.number_input("Escriba el límite superior", value=3.00)
            st.write("Función: 3x⁴ - 8x³ - 6x² - 12x") 
            funcion = funcionUnimodal.ej7(values)
            a, b, c, d = BP.bounding_phase(limInf, limSup, 0.1, funcionUnimodal.ej7)
            x1, px, py = bis.biseccion(a, b, values, funcionUnimodal.ej7)                   
        st.write("Values: ", funcion)

        st.write("El mínimo está en:", x1)
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
            time.sleep(0.2)

        progress_bar.empty()


