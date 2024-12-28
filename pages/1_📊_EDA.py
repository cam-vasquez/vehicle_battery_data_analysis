import streamlit as st
import pandas as pd
from src.eda import grafico_correlacion, grafico_pares, plot_vehicle_charging_interactive

# Carga el DataFrame
@st.cache_data
def load_data():
     return pd.read_csv("data/ev_charging_patterns.csv")  # Asegúrate de que el archivo existe en esta ruta

# Cargar datos
df = load_data()

# Configuración de la página
st.title("Análisis Exploratorio de Datos (EDA)")

# Información básica del conjunto de datos
st.header("Aspectos Básicos del Conjunto de Datos")
with st.container():
     col1, col2, col3 = st.columns(3)
     with col1:
          st.metric(label="Número de Filas", value=df.shape[0], border=True)
     with col2:
          st.metric(label="Número de Columnas", value=df.shape[1], border=True)
     with col3:
          missing_values = df.isnull().any().sum()
          st.metric(label="Valores Perdidos", value="Sí" if missing_values > 0 else "No", border=True)

# Mostrar gráficos
st.header("Mapa de Calor de Correlaciones")
fig_corr = grafico_correlacion(df)
st.plotly_chart(fig_corr, use_container_width=True)

st.header("Gráfico de Pares para Variables Numéricas")
fig_pares = grafico_pares(df)
st.plotly_chart(fig_pares, use_container_width=True)


st.header("Gráfico Interactivo: Vehículos por Modelo y Estación")
# Selección interactiva de columnas
x_column = st.selectbox("Selecciona la columna X:", df.columns)
# Opciones para el eje Y excluyendo la seleccionada en X
y_options = [col for col in df.columns if col != x_column]
y_column = st.selectbox("Selecciona la columna Y:", y_options)

# Generar el gráfico basado en la selección del usuario
scatter_fig = plot_vehicle_charging_interactive(df, x_column, y_column)
st.plotly_chart(scatter_fig, use_container_width=True)