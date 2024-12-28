# ------------  AQUI VA EL CODIGO DEL EDA ---------------------------- #
import pandas as pd
import plotly.express as px

def grafico_correlacion(data):
     # Seleccionar solo columnas numéricas
     numeric_data = data.select_dtypes(include=['float64', 'int64'])
     # Calcular la matriz de correlación
     correlation_matrix = numeric_data.corr()
     # Crear el heatmap
     fig = px.imshow(
          correlation_matrix,
          text_auto=".2f",  # Mostrar valores con 2 decimales
          color_continuous_scale=["#8CC6E7", "#129d58", "#202124", "#4880FF", "#E15A51", "#E8EAED"],  # Paleta personalizada
          title="Matriz de Correlación con Escala Ajustada",
          labels=dict(color="Correlación"),
     )
     # Configuración adicional
     fig.update_layout(
          width=1000,  # Ancho del gráfico
          height=800,  # Altura del gráfico
          coloraxis_colorbar=dict(
               title="Correlación",  # Título de la barra de color
          ),
          plot_bgcolor='rgba(0, 0, 0, 0)',  # Fondo del gráfico transparente
          paper_bgcolor='rgba(0, 0, 0, 0)',  # Fondo del papel transparente
     )

     return fig

def grafico_pares(data):
     # Seleccionar columnas clave
     selected_columns = ['Battery Capacity (kWh)', 'Energy Consumed (kWh)', 'Charging Cost (USD)', 'Charging Duration (hours)']
     numeric_data = data[selected_columns]

     # Crear el gráfico de pares
     fig = px.scatter_matrix(
          numeric_data,
          dimensions=numeric_data.columns,  # Usar todas las columnas numéricas
          title="Gráfico de Pares para Variables Numéricas",
          labels={col: col for col in numeric_data.columns},  # Etiquetas de las columnas
          color_continuous_scale="Viridis",  # Paleta de colores para el fondo
     )

     # Configuración adicional
     fig.update_layout(
          width=1000,  # Ancho del gráfico
          height=1000,  # Altura del gráfico
          dragmode="select",  # Permitir selección de puntos
          plot_bgcolor='rgba(0, 0, 0, 0)',  # Fondo del gráfico transparente
          paper_bgcolor='rgba(0, 0, 0, 0)',  # Fondo del papel transparente
     )

     return fig

def plot_vehicle_charging_interactive(df, x_column, y_column):
     # Agrupar los datos para contar las ocurrencias
     grouped_data = df.groupby([x_column, y_column]).size().reset_index(name='Vehicle Count') 
     # Crear el gráfico de barras
     fig = px.bar(
          grouped_data,
          x=x_column,
          y='Vehicle Count',  
          color=y_column,
          title=f"Cantidad de Vehículos por {x_column} y {y_column}",
          labels={
               x_column: x_column,
               y_column: y_column,
               'Vehicle Count': 'Cantidad'
          },
          template="plotly_white"  # Tema claro por defecto
     )

     # Configuración adicional
     fig.update_layout(
          xaxis=dict(tickangle=45),  # Rotar etiquetas
          legend_title=y_column,
          plot_bgcolor='rgba(0, 0, 0, 0)',  # Fondo transparente
          paper_bgcolor='rgba(0, 0, 0, 0)'  # Fondo transparente
     )

     return fig