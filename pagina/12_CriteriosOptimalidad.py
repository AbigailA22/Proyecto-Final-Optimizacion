import streamlit as st

st.title("Criterios de Optimalidad")
st.markdown('<div style="text-align: justify;">Se mantiene muy similar a las funciones de una sola variable, solamente que ahora la gradiente ' \
'es una cantidad vectorial, por lo que el criterio de optimización puede ser derivado con la ayuda de las series de ' \
'Taylor. Con ello, se asume que la función objetivo es una función de N variables, donde las derivadas parciales de primer orden son calculadas con: </div>', unsafe_allow_html=True)

latext1 = r'''
$$ 
\bar{x} = \frac{x_{1} + x_{1}}{2} - \frac{a_{1}}{2a_{2}}
$$  
'''
st.write(latext1)

st.markdown('<div style="text-align: justify;">Mientras que las derivadas de segundo orden forman una matriz, conocida como Matriz Hessiana (∇²f(x̅) = Hf(x̅)), que está formada por ' \
'una matriz simétrica de N x N de segundas derivadas parciales de f(x) evaluadas en el vector de x. Con esto, se puede obtener el Determinante ' \
'Hessiano D de la siguiente manera: </div>', unsafe_allow_html=True)

st.latex(r"""
\begin{array}{l}
\textbf{Algoritmo: Criterios de Optimalidad} \\
\rule{14cm}{1pt}\\

\text{◇ Si } D \gt 0 \text{ y } fxx(a, b) \gt 0 \text{, entonces f(a, b) es un mínimo relativo.}\\[0.5 ex] 
\text{◇ Si } D \gt 0 \text{ y } fxx(a, b) \lt 0 \text{, entonces f(a, b) es un máximo relativo.}\\[0.5 ex] 
\text{◇ Si } D \lt 0 \text{, entonces f(a, b) es un punto de silla.}\\[0.5 ex]
\text{◇ Si } D = 0 \text{, entonces  no hay información suficiente.}\\[0.5 ex]
                 
\end{array}
""")