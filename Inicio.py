import streamlit as st
import os

# Configuración inicial
st.set_page_config(page_title="Proyecto Final", layout="wide")

# Página de inicio
st.title("Bienvenido 👋🏻")

st.markdown("""
### ¿Qué hace esta aplicación?
Esta herramienta interactiva está diseñada específicamente para empresas del sector de **estaciones de carga de vehículos eléctricos**. 

### ¿A quién está dirigida?
La aplicación está orientada a:
- **Alta gerencia**: Para tomar decisiones basadas en datos procesados inteligentemente.
- **Departamentos de operaciones y análisis**: Para obtener análisis detallados y clasificaciones rápidas de métricas clave.
 
Su propósito es ofrecer insights estratégicos y analíticos mediante:   


""")

# 1. EDA: Análisis exploratorio de datos
col1, col2 = st.columns([2, 2])
with col1:
    ruta_imagen_eda = "utils/picture1.png"
    if os.path.exists(ruta_imagen_eda):
        st.markdown('<div style="text-align: center;">', unsafe_allow_html=True)
        st.image(ruta_imagen_eda, caption="Exploración de datos", width=250)
        st.markdown('</div>', unsafe_allow_html=True)    
    else:
        st.warning(f"No se encontró la imagen en la ruta: {ruta_imagen_eda}")
with col2:
    st.subheader("EDA")
    st.markdown("#### Análisis exploratorio de datos")
    st.markdown("Examina los datos y descubre patrones interesantes.")

# 2. Hipótesis: Visualización de hipótesis
col3, col4 = st.columns([2, 2])
with col3:
    ruta_imagen_hipotesis = "utils/picture2.png"
    if os.path.exists(ruta_imagen_hipotesis):
        st.image(ruta_imagen_hipotesis, caption="Hipótesis", width=250)
    else:
        st.warning(f"No se encontró la imagen en la ruta: {ruta_imagen_hipotesis}")
with col4:
    st.subheader("Hipótesis")
    st.markdown("#### Visualización de hipótesis propuestas")
    st.markdown("Evaluación de diferentes hipótesis mediante gráficos interactivos.")

# 3. Modelo: Predicciones con un modelo de árbol de decisiones
col5, col6 = st.columns([2, 2])
with col5:
    ruta_imagen_modelo = "utils/picture3.png" 
    if os.path.exists(ruta_imagen_modelo):
        st.image(ruta_imagen_modelo, caption="Modelo de Machine Learning", width=250)
    else:
        st.warning(f"No se encontró la imagen en la ruta: {ruta_imagen_modelo}")
with col6:
    st.subheader("Modelos")
    st.markdown("#### Uso de Means Clustering y Árbol de Decisioness")
    st.markdown("Modelos implementados con el fin de generar predicciones y evalúar el desempeño del modelo.")

# 4. Prompting: Interacción con OpenAI
col5, col6 = st.columns([2, 2])
with col5:
    ruta_imagen_modelo = "utils/picture4.png" 
    if os.path.exists(ruta_imagen_modelo):
        st.image(ruta_imagen_modelo, caption="Prompting", width=250)
    else:
        st.warning(f"No se encontró la imagen en la ruta: {ruta_imagen_modelo}")
with col6:
    st.subheader("Promptig")
    st.markdown("#### Uso de Few - Shots y Chain of Thought Promtings")
    st.markdown("Uso de differentes prompting approaches, con el fin de interactuar con OpenAI y el modelo de datos.")