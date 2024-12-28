import streamlit as st
import os

# Configuración inicial
st.set_page_config(layout="wide")

# Página de inicio
st.title("Proyecto Final")

st.markdown("""
## Bienvenido
Este proyecto incluye las siguientes páginas:
""")

# Sección de páginas con título y imagenes
col1, col2 = st.columns([2, 2])

with col1:
    st.markdown('<div class="column">', unsafe_allow_html=True)
    #st.image("utils/exploration.png", width=250) 
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.subheader("EDA: Análisis exploratorio de datos")
    st.markdown("Examina los datos y descubre patrones interesantes.")

col3, col4 = st.columns([2, 2])

with col3:
    st.markdown('<div class="column">', unsafe_allow_html=True)
    #st.image("utils/idea.png", width=250)  
    st.markdown('</div>', unsafe_allow_html=True)

with col4:
    st.subheader("Hipótesis: Visualización de hipótesis propuestas")
    st.markdown("Evalúa diferentes hipótesis mediante gráficos interactivos.")

col5, col6 = st.columns([2, 2])

with col5:
    st.markdown('<div class="column">', unsafe_allow_html=True)
    # Asegúrate de que la ruta esté bien escrita
    #ruta_imagen = "utils/machinelearning.png"
    #if os.path.exists(ruta_imagen):
    #    st.image(ruta_imagen, width=250)
    #else:
    #    st.error(f"No se encontró el archivo en la ruta: {ruta_imagen}")  
    st.markdown('</div>', unsafe_allow_html=True) 

with col6:
    st.subheader("Modelo: Predicciones con un modelo de árbol de decisiones")
    st.markdown("Genera predicciones y evalúa el desempeño del modelo.")