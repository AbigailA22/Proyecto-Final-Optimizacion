import streamlit as st
st.set_page_config(page_title="Algoritmos de Optimización", 
                   layout='wide',
                   menu_items={
                       'About': "Proyecto final para la materia de Optimización. Autor: Sahallely Abigail Aguilar Landa"
    })

teoria = st.Page("info.py", title="Teoría", icon=":material/home:", default=True)

exhaustive_search = st.Page("pagina/01_BusquedaExhaustiva.py", title="Búsqueda Exhaustiva", icon=":material/double_arrow:")
bounding_phase = st.Page("pagina/02_FasesDeAcotamiento.py", title="Fase De Acotamiento", icon=":material/double_arrow:")
region_elimination = st.Page("pagina/03_EliminacionRegiones.py", title="Reglas de Eliminación", icon=":material/block:")
interval_halving = st.Page("pagina/04_IntervalosMitad.py", title="Intervalos por la Mitad", icon=":material/block:")
fibonacci_search = st.Page("pagina/05_FibonacciSearch.py", title="Búsqueda por Fibonacci", icon=":material/block:")
golden_section = st.Page("pagina/06_GoldenSection.py", title="Búsqueda por Sección Dorada", icon=":material/block:")

centralDifference = st.Page("pagina/07_DiferenciaCentral.py", title="Método de la Diferencia Central", icon=":material/elevation:")
newton_raphson = st.Page("pagina/08_NewtonRaphson.py", title="Búsqueda por Método de Newton-Raphson", icon=":material/elevation:")
biseccion = st.Page("pagina/09_Biseccion.py", title="Búsqueda por Método de Bisección", icon=":material/elevation:")
secante = st.Page("pagina/10_Secante.py", title="Búsqueda por Método de la Secante", icon=":material/elevation:")

funcMultivariadas = st.Page("pagina/11_FuncMultivariadas.py", title="Funciones Multivariadas", icon=":material/hive:")
criteriosOptimalidad = st.Page("pagina/12_CriteriosOptimalidad.py", title="Criterios de Optimalidad", icon=":material/hive:")
busqUnidireccional = st.Page("pagina/13_BusquedaUnidireccional.py", title="Búsqueda Unidireccional", icon=":material/hive:")
nelderMead = st.Page("pagina/14_NelderMead.py", title="Nelder Mead (Simplex)", icon=":material/hive:")
hookeJeeves = st.Page("pagina/15_HookeJeeves.py", title="Hooke Jeeves (Búsqueda de Patrón)", icon=":material/hive:")
randomWalk = st.Page("pagina/16_RandomWalk.py", title="Caminata Aleatoria (Random Walk)", icon=":material/hive:")
hillClimbing = st.Page("pagina/17_HillClimbing.py", title="Ascenso de la Colina (Hill Climbing)", icon=":material/hive:")
simulatedAnnealing = st.Page("pagina/18_SimulatedAnnealing.py", title="Recocido Simulado (Simulated Annealing)", icon=":material/hive:")
gradiente = st.Page("pagina/19_MetodosGradiente.py", title="Métodos basados en gradiente", icon=":material/manage_search:")
cauchy = st.Page("pagina/20_Cauchy.py", title="Método de Cauchy (Descenso Más Pronunciado)", icon=":material/manage_search:")
newton = st.Page("pagina/21_MetodoNewton.py", title="Método de Newton", icon=":material/manage_search:")

pg = st.navigation(
        {
            "Optimización": [teoria],
            "Métodos de Acotamiento": [exhaustive_search, bounding_phase],
            "Métodos de Eliminación de Regiones": [region_elimination, interval_halving, fibonacci_search, golden_section],
            "Método Basado en Gradiente": [centralDifference, newton_raphson, biseccion, secante],
            "Algoritmos de Optimización Multivariada": [funcMultivariadas, criteriosOptimalidad, busqUnidireccional, nelderMead, hookeJeeves, randomWalk, hillClimbing, simulatedAnnealing],
            "Métodos Basados en Gradiente": [gradiente, cauchy, newton]
        }
    )

pg.run()
