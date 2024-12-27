import streamlit as st
import pandas as pd
from src.hipotesis import hipotesis_1, hipotesis_2, hipotesis_3, hipotesis_4, hipotesis_5  # Importa tus funciones de hipótesis

# Carga el DataFrame
@st.cache_data
def load_data():
    return pd.read_csv("data/ev_charging_patterns.csv")  # Asegúrate de que el archivo existe en esta ruta

# Cargar datos
df = load_data()

# Título de la aplicación
st.title("Hipótesis del Proyecto")

# Hipótesis 1
st.header("Hipótesis 1: Los vehiculos que utilizan el tipo de cargador DC Fast tardan menos tiempo en cargar (Charging Duration (hours)) que utilizando otro tipo de cargado")
st.write("Observamos que los cargadores DC Fast Charger tienen una mediana ligeramente menor en la duración de la carga, sin embargo esta diferencia no es significativa respecto a los otros tipos de cargadores.")
fig = hipotesis_1(df)  # Genera los gráficos llamando a la función hipotesis_1
st.plotly_chart(fig, use_container_width=True)  # Muestra el gráfico interactivo

# Hipótesis 2
st.header("Hipótesis 2: El costo de carga está directamente relacionado con la la energía consumida y el tipo de cargador utilizado.")
st.write("El tipo de cargador influye en el costo, con los cargadores DC Fast Charger mostrando costos más altos en general. Observamos que a medida aumenta la energía consumida, el costo de carga también tiende a aumentar.")
fig_scatter, fig_bar = hipotesis_2(df)  # Genera los gráficos llamando a la función
st.plotly_chart(fig_scatter, use_container_width=True)  
st.plotly_chart(fig_bar, use_container_width=True)

# Hipótesis 3
st.header("Hipótesis 3: El modelo de vehículo Tesla Model 3 es el que más consume energía.")
st.write("Confirmamos que el vehiculo Tesla Model 3 tiene el consumo promedio de energía más alto comparado con otros modelos.")
fig_bar, fig_box, fig_scatter = hipotesis_3(df)  
st.plotly_chart(fig_bar, use_container_width=True) # Gráfico 1: Consumo promedio de energía
st.plotly_chart(fig_box, use_container_width=True) # Gráfico 2: Distribución del consumo de energía
st.plotly_chart(fig_scatter, use_container_width=True) # Gráfico 3: Relación entre consumo de energía y capacidad de batería

# Hipótesis 4
st.header("Hipótesis 4: San Francisco es el estado donde los precios de carga son más elevados.")
st.write("La hipotesis planteada es rechazada, aunque San Francisco tiene costos de carga relativamente altos, no se destaca significativamente respecto a otras ubicaciones como Chicago o Houston.")
fig_bar, fig_box = hipotesis_4(df)
st.plotly_chart(fig_bar, use_container_width=True) # Gráfico 1: Costo promedio por ubicación geográfica
st.plotly_chart(fig_box, use_container_width=True) # Gráfico 2: Distribución del costo de carga por ubicación

# Hipótesis 5
st.header("Hipótesis 5: El Long Distance Traveler es el usuario con costos de sesión de carga más elevados.")
st.write("La hipotesis planteada no es respaldada por los datos, se observa que los Long Distance Travelers tienen algunos valores atípicos altos, pero su costo promedio y mediana es ligeramente inferior a los de otros tipos de usuarios.")
fig_bar, fig_box, fig_scatter = hipotesis_5(df)
st.plotly_chart(fig_bar, use_container_width=True) # Gráfico 1: Costo promedio por tipo de usuario
st.plotly_chart(fig_box, use_container_width=True) # Gráfico 2: Distribución del costo de carga por tipo de usuario
st.plotly_chart(fig_scatter, use_container_width=True) # Gráfico 3: Relación entre costo de carga y energía consumida por tipo de usuario


