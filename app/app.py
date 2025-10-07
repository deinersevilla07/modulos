
x = sp.Symbol('x')

import streamlit as st
import sympy as sp
from sympy.physics.continuum_mechanics.beam import Beam
import matplotlib.pyplot as plt

# Navegación multipágina
st.sidebar.title("Menú de navegación")
pagina = st.sidebar.selectbox(
    "Selecciona una página:",
    [
        "Introducción teórica",
        "Cálculo sencillo de viga",
        "Cálculo sencillo de amarre"
    ]
)

if pagina == "Introducción teórica":
    st.title("Introducción a SymPy y Mecánica Continua")
    st.markdown("""
    ## ¿Qué es SymPy?
    SymPy es una librería de Python para matemáticas simbólicas.
    
    ## Submódulo de Mecánica Continua
    El submódulo `continuum_mechanics` permite modelar vigas, cargas y apoyos de manera simbólica.
    
    Aquí puedes explicar conceptos teóricos, ejemplos y enlaces útiles.
    """)


elif pagina == "Cálculo sencillo de viga":
    st.title("Cálculo sencillo de viga")
    st.markdown("""
    Calculadora para una viga simplemente apoyada con carga puntual.
    """)
    L = st.number_input("Longitud de la viga (m)", min_value=1.0, max_value=20.0, value=10.0)
    P = st.number_input("Valor de la carga puntual (N)", min_value=1.0, max_value=1000.0, value=100.0)
    E = st.number_input("Módulo de Young E (Pa)", min_value=1e6, max_value=500e9, value=210e9, format="%.2e")
    I = st.number_input("Segundo momento de inercia I (m^4)", min_value=1e-8, max_value=1e-2, value=8.33e-6, format="%.2e")
    a = st.number_input("Posición de la carga puntual (m)", min_value=0.0, max_value=float(L), value=float(L)/2)

    try:
        viga = Beam(L, E, I, variable=x)
        viga.apply_load(P, a, -1)  # Carga puntual descendente en x=a
        viga.bc_deflection = [(0, 0), (L, 0)]  # Apoyos simples en ambos extremos
        viga.solve_for_reaction_loads()
        error = None
    except Exception as e:
        viga = None
        error = e

    if error:
        st.error(f"Error al crear la viga: {error}")
    elif viga:
        st.subheader("Reacciones en los apoyos:")
        for fuerza in viga.reaction_loads:
            st.latex(f"{sp.latex(fuerza)} = {sp.latex(viga.reaction_loads[fuerza])}")

        st.subheader("Diagrama de apoyos y carga:")
        fig, ax = plt.subplots(figsize=(6, 2))
        ax.hlines(0, 0, L, colors='black', linewidth=4, label='Viga')
        ax.plot([0, L], [0, 0], 'ko', markersize=10, label='Apoyos')
        ax.arrow(a, 0.2, 0, -0.15, head_width=0.3, head_length=0.1, fc='red', ec='red', label='Carga')
        ax.text(a, 0.25, f"P = {P} N", color='red', ha='center')
        ax.set_xlim(-1, L+1)
        ax.set_ylim(-0.5, 0.5)
        ax.axis('off')
        st.pyplot(fig)

elif pagina == "Cálculo sencillo de amarre":
    st.title("Cálculo sencillo de amarre")
    st.markdown("""
    Ejemplo básico de barra de amarre empotrada en un extremo y libre en el otro, sometida a una carga puntual en el extremo libre.
    """)
    L = st.number_input("Longitud de la barra (m)", min_value=1.0, max_value=20.0, value=5.0, key="L_amarre")
    P = st.number_input("Carga puntual en el extremo libre (N)", min_value=1.0, max_value=1000.0, value=50.0, key="P_amarre")
    E = st.number_input("Módulo de Young E (Pa)", min_value=1e6, max_value=500e9, value=200e9, format="%.2e", key="E_amarre")
    A = st.number_input("Área de la sección (m²)", min_value=1e-5, max_value=1e-1, value=1e-3, format="%.2e", key="A_amarre")

    # Deformación = P*L/(E*A)
    deformacion = P * L / (E * A)
    st.subheader("Deformación en el extremo libre:")
    st.latex(r"\delta = \frac{PL}{EA}")
    st.write(f"Deformación calculada: {deformacion:.4e} m")
