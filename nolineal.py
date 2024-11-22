import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Función para graficar
def plot_function(f, x, title, second_derivative=None):
    y = f(x)
    plt.figure(figsize=(5, 3))
    plt.plot(x, y, label="f(x)", linewidth=2, color="blue")
    if second_derivative is not None:
        y2 = second_derivative(x)
        plt.plot(x, y2, '--', label="f''(x)", linewidth=1.5, color="orange")
    plt.axhline(0, color="black", linewidth=0.8, linestyle="--")
    plt.axvline(0, color="black", linewidth=0.8, linestyle="--")
    plt.title(title, fontsize=12)
    plt.legend()
    plt.grid()
    st.pyplot(plt)

# Configuración de la página
st.set_page_config(page_title="Análisis de Convexidad", layout="wide")
st.title("Análisis de Convexidad y Concavidad de Funciones")

# Ejercicio 1
with st.container():
    st.subheader("1. Demuestre que la función f(x) = 3x + 2 es convexa en R")
    col1, col2 = st.columns([1, 1.5])

    with col1:
        st.markdown("""
        <div style="background-color: #0056b3; padding: 15px; border-radius: 5px; color: white;">
        <strong>Resolución:</strong>
        <ul>
            <li>La función es lineal: f(x) = 3x + 2.</li>
            <li>f''(x) = 0, que es no negativa.</li>
            <li>Conclusión: La función es convexa en R.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        f1 = lambda x: 3 * x + 2
        x = np.linspace(-10, 10, 400)
        plot_function(f1, x, "f(x) = 3x + 2")

# Ejercicio 2
with st.container():
    st.subheader("2. Verifique si f(x) = x³ es convexa, cóncava o ninguna en [0,∞)")
    col1, col2 = st.columns([1, 1.5])

    with col1:
        st.markdown("""
        <div style="background-color: #d9534f; padding: 15px; border-radius: 5px; color: white;">
        <strong>Resolución:</strong>
        <ul>
            <li>f''(x) = 6x.</li>
            <li>En [0, ∞), f''(x) ≥ 0.</li>
            <li>Conclusión: La función es convexa en este intervalo.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        f2 = lambda x: x**3
        f2_derivative_2 = lambda x: 6 * x  # Segunda derivada
        x = np.linspace(0, 10, 400)
        plot_function(f2, x, "f(x) = x³ y su segunda derivada", f2_derivative_2)

# Ejercicio 3
with st.container():
    st.subheader("3. Demuestre que f(x) = e²ˣ es convexa en R")
    col1, col2 = st.columns([1, 1.5])

    with col1:
        st.markdown("""
        <div style="background-color: #5cb85c; padding: 15px; border-radius: 5px; color: white;">
        <strong>Resolución:</strong>
        <ul>
            <li>f''(x) = 4e²ˣ > 0 para todo x.</li>
            <li>Conclusión: La función es convexa en R.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        f3 = lambda x: np.exp(2 * x)
        f3_derivative_2 = lambda x: 4 * np.exp(2 * x)  # Segunda derivada
        x = np.linspace(-2, 2, 400)
        plot_function(f3, x, "f(x) = e²ˣ y su segunda derivada", f3_derivative_2)

# Ejercicio 4
with st.container():
    st.subheader("4. Análisis de la función f(x) = ln(x)")
    col1, col2 = st.columns([1, 1.5])

    with col1:
        st.markdown("""
        <div style="background-color: #f0ad4e; padding: 15px; border-radius: 5px; color: white;">
        <strong>Resolución:</strong>
        <ul>
            <li>f''(x) = -1/x² ≤ 0 en (0, ∞).</li>
            <li>Conclusión: La función es cóncava en su dominio.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        f4 = lambda x: np.log(x)
        f4_derivative_2 = lambda x: -1 / x**2  # Segunda derivada
        x = np.linspace(0.1, 10, 400)
        plot_function(f4, x, "f(x) = ln(x) y su segunda derivada", f4_derivative_2)

# Ejercicio 5
with st.container():
    st.subheader("5. Análisis de f(x) = x⁴ - 2x² + 1")
    col1, col2 = st.columns([1, 1.5])

    with col1:
        st.markdown("""
        <div style="background-color: #0275d8; padding: 15px; border-radius: 5px; color: white;">
        <strong>Resolución:</strong>
        <ul>
            <li>f''(x) = 12x² - 4.</li>
            <li>Convexa en (-∞, -√(1/3)] ∪ [√(1/3), ∞).</li>
            <li>Cóncava en (-√(1/3), √(1/3)).</li>
            <li>Puntos de inflexión: x = ±√(1/3).</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        f5 = lambda x: x**4 - 2 * x**2 + 1
        f5_derivative_2 = lambda x: 12 * x**2 - 4  # Segunda derivada
        x = np.linspace(-2, 2, 400)
        plot_function(f5, x, "f(x) = x⁴ - 2x² + 1 y su segunda derivada", f5_derivative_2)
