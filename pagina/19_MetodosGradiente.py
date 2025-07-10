import streamlit as st

st.title("Métodos Basados en Gradiente")
st.markdown('<div style="text-align: justify;">Usualmente los métodos directos requieren de muchas evaluaciones de la función para poder converger a un punto mínimo, lo cual puede llegar a ser tardado y costoso computacionalmente. ' \
'Así es donde surge la idea para los métodos basados en gradiente, que explotan la información de la derivada de la función, por lo que comúnmente son métodos más rápidos. Sin embargo, como muchos problemas ' \
'no son diferenciables, se debe de revisar la naturaleza para asegurarse que no es discreta, discontinua o si las variables son discretas (programación entera). Debido a que el concepto de gradientes es intricado, ' \
'se utilizan principalmente en problemas de diseño de ingeniería.</div>', unsafe_allow_html=True)

st.markdown('<div style="text-align: justify;"> </div>', unsafe_allow_html=True)

st.markdown('<div style="text-align: justify;">Las derivadas pueden obtenerse por el cálculo numérico de la función de dos o tres vecinos, aplicando la técnica de diferencia central.</div>', unsafe_allow_html=True)


latext1 = r'''
$$ 
\frac{\delta f(x)}{\delta x_{i}} \biggm| _{x^{(t)}} = \frac{ f(x_{i}^{(t)} + \Delta x_{i}^{(t)}) - f(x_{i}^{(t)} - \Delta x_{i}^{(t)}) } { 2\Delta x_{i}^{(t)} }
$$  
'''
latext2 = r'''
$$ 
\frac{\delta^{2} f(x)}{\delta^{2} x_{i}^{2}} \biggm| _{x^{(t)}} = \frac{ f(x_{i}^{(t)} + \Delta x_{i}^{(t)}) - 2f(x^{(t)}) + f(x_{i}^{(t)} - \Delta x_{i}^{(t)}) } { (\Delta x_{i}^{(t)})^{2} }
$$  
'''
latext3 = r'''
$$ 
\frac{\delta^{2} f(x)}{\delta x_{i} \delta x_{j}} \biggm| _{x^{(t)}} = 
\frac{f(x_{i}^{(t)} + \Delta x_{i}^{(t)}, x_{j}^{(t)} + \Delta x_{j}^{(t)}) 
- f(x_{i}^{(t)} + \Delta x_{i}^{(t)}, x_{j}^{(t)} - \Delta x_{j}^{(t)}) 
- f(x_{i}^{(t)} - \Delta x_{i}^{(t)}, x_{j}^{(t)} + \Delta x_{j}^{(t)})
+ f(x_{i}^{(t)} - \Delta x_{i}^{(t)}, x_{j}^{(t)} - \Delta x_{j}^{(t)}) }
{ 4 \Delta x_{i}^{(t)} \Delta x_{j}^{(t)} }
$$  
'''

st.write(latext1)
st.write(latext2)
st.write(latext3)