#Fecha: 16 de marzo de 2025
import streamlit as st

st.title("Optimización")
st.markdown('<div style="text-align: justify;">Busca encontrar la <b>mejor solución</b> posible, modificando el valor de las variables controladas, a veces sujeto a restricciones. ' \
'Es aplicable en todos los dominios, ya que cualquier problema en el que se toma una decisión puede plantearse como un problema de optimización.</div>', unsafe_allow_html=True)


st.header("Métodos para abordar problemas")
st.markdown('<div style="text-align: justify;"> <b>1) Analítico: </b> Basado en cálculo diferencial. El mínimo o máximo de un criterio de rendimiento es determinado al encontrar los valores ' \
'de los parámetros que hacen que las derivadas respecto a estos tomen valores de 0. El problema debe ser descrito matemáticamente, por lo mismo ' \
'no puede ser aplicado a problemas altamente no lineales, o si el número de variables independientes es mayor a 3.</div>', unsafe_allow_html=True)

st.markdown('<div style="text-align: justify;"> </div>', unsafe_allow_html=True)

st.markdown('<div style="text-align: justify;"> <b>2) Gráfico: </b> Requiere hacer la figura de la función a optimizar, por lo que funciona si el número de variables independientes ' \
'no excede a 2. Es limitado por lo mismo, ya que la mayoría de las aplicaciones prácticas requiere más de 4 variables.</div>', unsafe_allow_html=True)

st.markdown('<div style="text-align: justify;"> </div>', unsafe_allow_html=True)

st.markdown('<div style="text-align: justify;"> <b>3) Experimental: </b> Las variables se ajustan una a la vez, en cada paso el criterio a optimizar siendo evaluado. Suele llegar al óptimo ' \
'o a valores muy cercanos. Como tiene una base empírica, puede llevar a inciertos, como la interacción de variables que deben ajustarse simultáneamente.</div>', unsafe_allow_html=True)

st.markdown('<div style="text-align: justify;"> </div>', unsafe_allow_html=True)

st.markdown('<div style="text-align: justify;"> <b>4) Numérico: </b> Es iterativo, genera una serie de soluciones que progresivamente mejoran, iniciando con una solución estimada. Termina ' \
'cuando un criterio de convergencia es alcanzado. Por ello sirve para problemas altamente complejos, que no pueden resolverse analíticamente. ' \
'Es estudiado por la programación matemática, que se divide en Lineal, Entera, Cuadrática, No lineal y Dinámica.</div>', unsafe_allow_html=True)

st.divider()

st.header("Elementos de los problemas de optimización")
st.markdown('<div style="text-align: justify;"> <b>1) Variables de diseño, decisión o parámetros: </b> Variables independientes que describen un sistema o problema, son representados ' \
'por un vector columna, donde la dimensión del problema es la cantidad de variables (n).</div>', unsafe_allow_html=True)

st.markdown('<div style="text-align: justify;"> </div>', unsafe_allow_html=True)

st.markdown('<div style="text-align: justify;"> <b>2) Límites o Fronteras de las variables: </b> Límites superiores o inferiores de cada variable de decisión. Confina el problema, guiando ' \
'al algoritmo de búsqueda.</div>', unsafe_allow_html=True)

st.markdown('<div style="text-align: justify;"> </div>', unsafe_allow_html=True)

st.markdown('<div style="text-align: justify;"> <b>3) Funciones objetivo: </b> Determina el valor donde el diseño es mejor. Es un valor escalar, calculado por el resto de variables de ' \
'decisión, por lo tanto es la variable dependiente. Puede ser 1 o más, además de minimizar o maximizar.</div>', unsafe_allow_html=True)

st.markdown('<div style="text-align: justify;"> </div>', unsafe_allow_html=True)

st.markdown('<div style="text-align: justify;"> <b>4) Restricciones: </b>Representan relaciones funcionales entre las variables de diseño y otros parámetros, como fenómenos físicos o ' \
'limitaciones de recursos. Para que unsa solución sea factible, debe de cumplir las restricciones.</div>', unsafe_allow_html=True)

st.divider()

st.header("Conceptos Clave")
st.markdown('<div style="text-align: justify;"> <b>◇ Función Convexa: </b> Al unir dos puntos en una gráfica, el segmento trazado queda por encima de esta gráfica.</div>', unsafe_allow_html=True)
st.markdown('<div style="text-align: justify;"> </div>', unsafe_allow_html=True)
st.markdown('<div style="text-align: justify;"> <b>◇ Función Cóncava: </b> Al unir dos puntos en una gráfica, el segmento trazado queda por debajo de la gráfica.</div>', unsafe_allow_html=True)
st.markdown('<div style="text-align: justify;"> </div>', unsafe_allow_html=True)
st.markdown('<div style="text-align: justify;"> <b>◇ Función No Convexa: </b> Presenta ambos comportamientos a lo largo de la gráfica, por lo que puede dividirse en más secciones.</div>', unsafe_allow_html=True)
st.markdown('<div style="text-align: justify;"> </div>', unsafe_allow_html=True)
st.markdown('<div style="text-align: justify;"> <b>◇ Pendiente: </b>  Relación de cambio de la variable y sobre x.</div>', unsafe_allow_html=True)

st.subheader("Puntos óptimos")
st.markdown('<div style="text-align: justify;"> <b>• Óptimo local: </b> Punto o solución del cual no existe ningún punto en su vecindario mejor que este.</div>', unsafe_allow_html=True)
st.markdown('<div style="text-align: justify;"> </div>', unsafe_allow_html=True)
st.markdown('<div style="text-align: justify;"> <b>• Óptimo Global: </b> Solución de la cual no existe ningún punto en todo el espacio de búsqueda que sea mejor.</div>', unsafe_allow_html=True)
st.markdown('<div style="text-align: justify;"> </div>', unsafe_allow_html=True)
st.markdown('<div style="text-align: justify;"> <b>• Punto de Inflexión: </b> Es donde la gráfica toma diferente dirección. Es decir, el valor de la función disminuye cuando x ' \
'se reduce y aumenta cuando x es incrementado.</div>', unsafe_allow_html=True)
st.markdown('<div style="text-align: justify;"> </div>', unsafe_allow_html=True)
st.markdown('<div style="text-align: justify;">• Se considera que son <b>unimodales</b> cuando tienen un solo mínimo, mientras que son <b>multimodales</b> cuando pueden tener varios ' \
'mínimos. Las multimodales siempre son no convexas, mientras que las unimodales no necesariamente son convexas.</div>', unsafe_allow_html=True)

st.divider()
st.header("Métodos de Resolución Analíticos")
st.subheader("Derivada y Puntos Críticos")
st.markdown('<div style="text-align: justify;"> Para resolver un problema con este método, es necesario contar con una función unimodal, es decir, que tenga una sola variable. Después, ' \
'se debe conseguir la primera derivada, así como resolverla mientras este igualada a 0. Al tener la respuesta, se evalúan si los valores obtenidos son máximos ' \
'o mínimos, al evaluar dos puntos muy cercanos al número. Si el valor previo es positivo y el siguiente negativo, es un máximo; por el contrario, si pasa de negativo a positivo, es un mínimo.</div>', unsafe_allow_html=True)


st.subheader("Condiciones Suficientes")
st.markdown('<div style="text-align: justify;"> Considerando un problema con una función determinada, se deben de considerar las siguientes condiciones: </div>', unsafe_allow_html=True)
st.markdown('<div style="text-align: justify;"> </div>', unsafe_allow_html=True)
st.markdown('<div style="text-align: justify;"> 1) Si la primera derivada de x es igual a 0, indica que el punto es un máximo, mínimo o punto de inflexión.</div>', unsafe_allow_html=True)
st.markdown('<div style="text-align: justify;"> </div>', unsafe_allow_html=True)
st.markdown('<div style="text-align: justify;">2) Se procede a seguir derivando hasta alcanzar el primer NO CERO. Así, la derivada de mayor orden denotada por n: </div>', unsafe_allow_html=True)
st.markdown('<div style="text-align: justify;"> </div>', unsafe_allow_html=True)
st.markdown('<div style="text-align: justify;"> a) Si n es impar,  x es un punto de inflexión. </div>', unsafe_allow_html=True)
st.markdown('<div style="text-align: justify;"> </div>', unsafe_allow_html=True)
st.markdown('<div style="text-align: justify;"> b) Si n es par, x es un óptimo local: Si la derivada es positiva, es un mínimo; si es negativa, es un máximo.</div>', unsafe_allow_html=True)
st.markdown('<div style="text-align: justify;"> </div>', unsafe_allow_html=True)
