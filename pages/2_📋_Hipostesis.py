import streamlit as st
from src.hipotesis import hipotesis_1, hipotesis_2  # Importa tus funciones de hipótesis

# Carga el DataFrame
@st.cache_data
def load_data():
    return pd.read_csv("data/ev_charging_patterns.csv")  # Asegúrate de que el archivo existe en esta ruta

# Cargar datos
df = load_data()

# Título de la aplicación
st.title("Hipótesis del Proyecto")

# Hipótesis 1
st.header("Hipótesis 1: Relación entre tipo de cargador y tiempo empleado en completar la carga")
fig = hipotesis_1(df)  # Genera los gráficos llamando a la función hipotesis_1
st.plotly_chart(fig, use_container_width=True)  # Muestra el gráfico interactivo

# Hipótesis 2
st.header("Hipótesis 2:  Relación Costo de Carga y  Energía Consumida")
fig2 = hipotesis_2(df)  # Genera el gráfico llamando a la función
st.plotly_chart(fig2, use_container_width=True)  # Muestra el gráfico en Streamlit

# Hipótesis 3
st.header("Hipótesis 3: Rendimiento de batería según modelo de vehículo")

# Hipótesis 4
st.header("Hipótesis 4: Precio de carga según ubicación")

# Hipótesis 5
st.header("Hipótesis 5: Costos de sesiones de carga según usuario")