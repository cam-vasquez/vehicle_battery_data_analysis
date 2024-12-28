import streamlit as st
import os

# Configuración inicial
st.set_page_config(page_title="Proyecto Final", layout="wide")

# Página de inicio
st.title("Proyecto Final")
st.markdown("""
## Bienvenido
Este proyecto incluye las siguientes páginas:
Esta aplicación está diseñada para explorar, analizar y modelar datos relacionados con el uso de baterías en vehículos eléctricos. Proporciona herramientas interactivas para comprender los datos, evaluar hipótesis y generar predicciones con modelos avanzados.
A continuación, se presentan las secciones disponibles en el proyecto:
""")

# 1. EDA: Análisis exploratorio de datos
col1, col2 = st.columns([2, 2])
with col1:
    ruta_imagen_eda = "utils/picture1.png"
    if os.path.exists(ruta_imagen_eda):
        st.image(ruta_imagen_eda, caption="Exploración de datos", width=150)
    else:
        st.warning(f"No se encontró la imagen en la ruta: {ruta_imagen_eda}")
with col2:
    st.subheader("EDA: Análisis exploratorio de datos")
    st.markdown("Examina los datos y descubre patrones interesantes.")

# 2. Hipótesis: Visualización de hipótesis
col3, col4 = st.columns([2, 2])
with col3:
    ruta_imagen_hipotesis = "utils/picture2.png"
    if os.path.exists(ruta_imagen_hipotesis):
        st.image(ruta_imagen_hipotesis, caption="Hipótesis", width=150)
    else:
        st.warning(f"No se encontró la imagen en la ruta: {ruta_imagen_hipotesis}")
with col4:
    st.subheader("Hipótesis: Visualización de hipótesis propuestas")
    st.markdown("Evalúa diferentes hipótesis mediante gráficos interactivos.")

# 3. Modelo: Predicciones con un modelo de árbol de decisiones
col5, col6 = st.columns([2, 2])
with col5:
    ruta_imagen_modelo = "utils/picture3.png" 
    if os.path.exists(ruta_imagen_modelo):
        st.image(ruta_imagen_modelo, caption="Modelo de Machine Learning", width=150)
    else:
        st.warning(f"No se encontró la imagen en la ruta: {ruta_imagen_modelo}")
with col6:
    st.subheader("Modelo: K Means Clustering")
    st.markdown("Genera predicciones y evalúa el desempeño del modelo.")