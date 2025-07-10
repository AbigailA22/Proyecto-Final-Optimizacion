import streamlit as st

st.title("Métodos de Eliminación de Regiones")
st.markdown('<div style="text-align: justify;">Más que un procedimiento por si solo, es un conjunto de reglas que aplican todos los algoritmos ' \
'de Eliminación de Regiones para decidir cómo actuar frente a los valores presentados. Es útil para funciones unimodales y convexas. A continuación se ' \
'presentan de manera formal, considerando a x₁ y x₂ como dos valores en la recta, mientras que a es el límite inferior y b el límite superior.</div>', unsafe_allow_html=True)

st.latex(r"""
\begin{array}{l}
\textbf{Algoritmo: Reglas de Eliminación} \\
\rule{14cm}{1pt}\\

\text{◇ Si } f(x_{1}) \gt f(x_{2}) \text{ entonces el mínimo no se encuentra entre } (a, x_{1}) \\[0.5 ex] 
\text{◇ Si } f(x_{1}) \lt f(x_{2}) \text{ entonces el mínimo no se encuentra entre } (x_{2}, b) \\[0.5 ex] 
\text{◇ Si } f(x_{1}) == f(x_{2}) \text{ entonces el mínimo no se encuentra entre } (a, x_{1}) y (x_{2}, b)\\[0.5 ex] 
                 
\end{array}
""")

st.markdown('<div style="text-align: justify;">Como se observa, es necesario considerar las funciones de los valores, no estos por si mismos. Además, de manera más simple, se puede considerar ' \
'lo siguiente: Si f(x₁) > f(x₂), a = x₁; si f(x₁) < f(x₂), b = x₂; si f(x₁) == f(x₂), a = x₁ y b = x₂. Como se observa, se van desplazando los límites ' \
'reduciendo poco a poco las regiones externas.</div>', unsafe_allow_html=True)
