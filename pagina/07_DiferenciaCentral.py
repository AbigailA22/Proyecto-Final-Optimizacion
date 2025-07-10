import streamlit as st

st.title("Método de Diferencia Central")
st.markdown('<div style="text-align: justify;">La convergencia del algoritmo depende del punto inicial y de la naturaleza de la función objetivo. De manera matemática, ' \
'esto es fácil de conseguir, sin embargo, numéricamente presenta más dificultades. Aquí entra este método, el cual ' \
'no es aplicado por si mismo, en realidad funciona más como un apoyo computacional para el cálculo de derivadas. </div>', unsafe_allow_html=True)

st.header("Cálculo de derivadas")
st.markdown('<div style="text-align: justify;">Para la Primera y Segunda derivada, se realizan las siguientes ecuaciones: </div>', unsafe_allow_html=True)

latext1 = r'''
$$ 
f'(x_{t}) = \frac{f(x_{t} + \Delta x_{t}) - f(x_{t} - \Delta x_{t} )}{2 \Delta x_{t}} 
$$  
'''

latext2 = r'''
$$ 
f''(x_{t}) = \frac{f(x_{t} + \Delta x_{t}) - 2 f(x_{t}) + f(x_{t} - \Delta x_{t} )}{(\Delta x_{t}) ^2} 
$$  
'''

st.write(latext1)
st.write(latext2)

st.markdown('<div style="text-align: justify;">Siendo el parámetro ∆xₜ un valor muy pequeño, útil para las operaciones.</div>', unsafe_allow_html=True)