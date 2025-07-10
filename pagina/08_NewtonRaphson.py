import streamlit as st
import pandas as pd
import altair as alt
import time

from funciones import FuncionesUnimodales_19marzo2025 as funcionUnimodal
from algoritmos import FNewtonRaphson as newton

st.title("Método de Newton-Raphson")
st.write("Se utiliza una aproximación lineal a la primera derivada de la función, usando la expansión de Taylor. " 
"Esta se iguala a cero en el siguiente intento; así, si el punto actual en la iteración t es x en la posición t, la siguiente " 
"iteración se encuentra por la ecuación: ")

st.markdown('<div style="text-align: justify;"Se utiliza una aproximación lineal a la primera derivada de la función, usando la expansión de Taylor. ' \
'Esta se iguala a cero en el siguiente intento; así, si el punto actual en la iteración t es x en la posición t, la siguiente iteración se encuentra por la ecuación: </div>', unsafe_allow_html=True)

latext1 = r'''
$$ 
x_{t+1} = x_{t} - \frac{f'(x_{t})}{f''(x_{t})} 
$$  
'''
st.write(latext1)

st.latex(r"""
\begin{array}{l}
\textbf{Algoritmo: Método de Newton-Raphson} \\
\rule{14cm}{1pt}\\
\textbf{Definir: } x_{1} \text{ (Valor Inicial), } \epsilon \text{ (Error Aceptado), } k = 1, f'(x_{1}) \\[0.5 ex] 
         \\
\textbf{Paso 1: } \text{Realizar la derivada } f''(x_{k})  \\[0.5 ex] 
         
\textbf{Paso 2: } \text{Calcular } x_{k+1} = x_{k} -  \frac{f'(x_{k})}{f''(x_{k})} \text{. Encontrar la derivada } f'(x_{k+1}) \\[0.5 ex] 

\textbf{Paso 3: } \text{Si } f'(x_{k+1})  \lt \epsilon \text{, Terminar.  Si no, definir k = k + 1 y volver al Paso 1.} \\[0.5 ex] 
         
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
        delta = st.slider("Selección del valor de delta", 0.01, 1.00)

        if(option == "Lata"):
            limInf = st.number_input("Escriba el límite inferior", value=0.20)
            limSup = st.number_input("Escriba el límite superior", value=5.00)
            st.write("Función: 2πr² + (500 / r)")
            funcion = funcionUnimodal.lata(values)
            x1, px, py = newton.newtonRaphson(limInf, limSup, values, delta, funcionUnimodal.lata)

        elif(option == "Caja"):
            limInf = st.number_input("Escriba el límite inferior", value=2.00)
            limSup = st.number_input("Escriba el límite superior", value=3.00)
            st.write("Función: -(4l³ - 60l² + 200l)")
            funcion = funcionUnimodal.caja(values)
            x1, px, py = newton.newtonRaphson(limInf, limSup, values, delta, funcionUnimodal.caja)

        elif(option == "Función 1"):
            limInf = st.number_input("Escriba el límite inferior", value=-2.00)
            limSup = st.number_input("Escriba el límite superior", value=2.00)
            st.write("Función: x² + 3")
            funcion = funcionUnimodal.ej1(values) 
            x1, px, py = newton.newtonRaphson(limInf, limSup, values, delta, funcionUnimodal.ej1)

        elif(option == "Función 2"):
            limInf = st.number_input("Escriba el límite inferior", value=0.001)
            limSup = st.number_input("Escriba el límite superior", value=10.000)
            st.write("Función: x² + (54/x)")
            funcion = funcionUnimodal.ej4(values)
            x1, px, py = newton.newtonRaphson(limInf, limSup, values, delta, funcionUnimodal.ej4)

        elif(option == "Función 3"):
            limInf = st.number_input("Escriba el límite inferior", value=0.00)
            limSup = st.number_input("Escriba el límite superior", value=5.00)
            st.write("Función: x³ + 2x - 3")
            funcion = funcionUnimodal.ej5(values) 
            x1, px, py = newton.newtonRaphson(limInf, limSup, values, delta, funcionUnimodal.ej5)

        elif(option == "Función 4"):
            limInf = st.number_input("Escriba el límite inferior", value=-2.50)
            limSup = st.number_input("Escriba el límite superior", value=2.50)
            st.write("Función: x⁴ + x² - 33")
            funcion = funcionUnimodal.ej6(values)
            x1, px, py = newton.newtonRaphson(limInf, limSup, values, delta, funcionUnimodal.ej6)

        else:
            limInf = st.number_input("Escriba el límite inferior", value=-1.50)
            limSup = st.number_input("Escriba el límite superior", value=3.00)
            st.write("Función: 3x⁴ - 8x³ - 6x² - 12x") 
            funcion = funcionUnimodal.ej7(values)
            x1, px, py = newton.newtonRaphson(limInf, limSup, values, delta, funcionUnimodal.ej7)                   
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
            time.sleep(0.1)

        progress_bar.empty()

