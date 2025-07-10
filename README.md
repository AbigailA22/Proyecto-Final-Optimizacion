### Proyecto Final de Optimización
Este proyecto es parte de la evaluación final para la materia de Optimización, basándose en los métodos presentados por el libro "Optimization for Engineering Design: Algorithms and Examples" del autor Kalyanmoy Deb.

Después de una breve introducción al tema, se incluye un apartado para cada uno de los métodos estudiados, considerando la teoría, el algoritmo que lo explica y una sección para realizar diferentes pruebas, variando los parámetros requeridos y la función a resolver. 

Los métodos considerados son para funciones tanto univariables como multivariables, tomando en cuenta los siguientes: 

##### Métodos univariables
* Búsqueda Exhaustiva
* Fase de Acotamiento
* Intervalos por Mitad
* Búsqueda por Fibonacci
* Búsqueda por Sección Dorada
* Método de Newton - Raphson
* Método de Bisección
* Método de la Secante

##### Métodos multivariables
* Método de Nelder Mead (Simplex)
* Método de Hooke - Jeeves
* Caminata Aleatoria (Random Walk)
* Ascenso de la Colina (Hill Climbing)
* Recocido Simulado (Simulated Annealing)
* Método de Cauchy
* Método de Newton

Además, para la resolución de los métodos multivariables, se puede probar con las funciones:
* Función de Rastrigin
* Función de Ackley
* Función de Esfera
* Función de Rosenbrock
* Función de Beale
* Función de Booth
* Función de Himmelblaus
* Función de McCormick

El trabajo se planeó como una página web, así que los resultados puede ser visualizados al seguir el siguiente [enlace](https://proyecto-tercer-parcial-6rozmy6lq3qbficc2hrqfe.streamlit.app/).

O puede ser descargado y ejecutado de la siguiente manera:
1. Clonar repositorio, o en sud efecto, descargar el archivo ZIP y descomprimirlo.
2. Ir al directorio del proyecto y ejecutar `py -m venv .venv`
3. Activar el ambiente creado, usando `.venv\Scripts\activate`
4. Instalar los requisitos (que se encuentran en el archivo correpondiente): `pip install -r requirements.txt`
5. Ejecutar el código `streamlit run Main.py`
Nota: Una vez que se han descargado los requisitos en el ambiente, para el resto de ejecuciones solo será necesario activar el ambiente y ejecitar el código, con los comandos especificados.  

