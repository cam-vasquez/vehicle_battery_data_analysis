# ------------------ AQUI VA A CONTENER LOS MODULOS DE HIPOTESIS -------------- #
import plotly.express as px
import pandas as pd

def hipotesis_1(data):
     fig = px.box(
          data_frame=data,
          x='Charger Type',
          y='Charging Duration (hours)',
          color='Charger Type',
          title='Duración de Carga por Tipo de Cargador',
          labels={
               'Charger Type': 'Tipo de Cargador',
               'Charging Duration (hours)': 'Duración de Carga (horas)'
          },
          template="plotly_dark"  # Tema oscuro para gráficos
     )
     fig.update_layout(
          plot_bgcolor='rgba(0, 0, 0, 0)',  # Fondo transparente
          paper_bgcolor='rgba(0, 0, 0, 0)'  # Fondo del papel transparente
     )

     return fig

def hipotesis_2(data):
     # Crear el gráfico 1
     fig_scatter = px.scatter(
          data_frame=data,
          x='Energy Consumed (kWh)',
          y='Charging Cost (USD)',
          color='Charger Type',
          symbol='Charger Type',
          title='Relación entre Energía Consumida y Costo de Carga por Tipo de Cargador',
          labels={
               'Energy Consumed (kWh)': 'Energía Consumida (kWh)',
               'Charging Cost (USD)': 'Costo de Carga (USD)',
               'Charger Type': 'Tipo de Cargador'
          },
          template="plotly_white"  # Tema claro por defecto
     )
     # Configuración dinámica para tema oscuro o claro
     fig_scatter.update_layout(
          legend=dict(
               title=dict(text='Tipo de Cargador', font=dict(size=14)),
               font=dict(size=12),  # Tamaño del texto de la leyenda
               bgcolor='rgba(0, 0, 0, 0)',  # Fondo transparente
          ),
          plot_bgcolor='rgba(0, 0, 0, 0)',  # Fondo del gráfico transparente
          paper_bgcolor='rgba(0, 0, 0, 0)'  # Fondo del papel transparente
     )

     # Crear el gráfico 2 (de barras)
     avg_data = data.groupby('Charger Type', as_index=False)['Charging Cost (USD)'].mean()
     fig_bar = px.bar(
          data_frame=avg_data,  # Usar los datos promediados
          x='Charger Type',
          y='Charging Cost (USD)',
          color='Charger Type',
          title='Costo de Carga Promedio según Tipo de Cargador',
          labels={
               'Charger Type': 'Tipo de Cargador',
               'Charging Cost (USD)': 'Costo de Carga Promedio (USD)'
          },
          template="plotly_white"  # Tema claro por defecto
     )
     # Configuración dinámica para tema oscuro o claro
     fig_bar.update_layout(
          xaxis=dict(tickangle=45),  # Rotación de las etiquetas en el eje X
          legend=dict(
               title=dict(text='Tipo de Cargador', font=dict(size=14)),
               font=dict(size=12),  # Tamaño del texto de la leyenda
               bgcolor='rgba(0, 0, 0, 0)',  # Fondo transparente
          ),
          plot_bgcolor='rgba(0, 0, 0, 0)',  # Fondo del gráfico transparente
          paper_bgcolor='rgba(0, 0, 0, 0)'  # Fondo del papel transparente
     )

     return fig_scatter, fig_bar

def hipotesis_3 (data):

     # Crear el gráfico 1 de barras
     avg_energy = data.groupby('Vehicle Model', as_index=False)['Energy Consumed (kWh)'].mean()
     fig_bar = px.bar(
          data_frame=avg_energy,
          x='Vehicle Model',
          y='Energy Consumed (kWh)',
          title='Consumo Promedio de Energía por Modelo de Vehículo',
          labels={
               'Vehicle Model': 'Modelo de Vehículo',
               'Energy Consumed (kWh)': 'Consumo Promedio de Energía (kWh)'
          },
          template="plotly_white",
          color='Energy Consumed (kWh)',  # Color dinámico por intensidad
     )
     # Configuración adicional
     fig_bar.update_layout(
          xaxis=dict(tickangle=45),  # Rotación de etiquetas en eje X
          plot_bgcolor='rgba(0, 0, 0, 0)',
          paper_bgcolor='rgba(0, 0, 0, 0)',
          legend=dict(
               bgcolor='rgba(0, 0, 0, 0)',
               title=dict(font=dict(size=14)),
          )
     )

     # Crear el boxplot 2
     fig_box = px.box(
          data_frame=data,
          x='Vehicle Model',
          y='Energy Consumed (kWh)',
          color='Vehicle Model',
          title='Distribución del Consumo de Energía por Modelo de Vehículo',
          labels={
               'Vehicle Model': 'Modelo de Vehículo',
               'Energy Consumed (kWh)': 'Consumo de Energía (kWh)'
          },
          template="plotly_white"
     )

     # Configuración adicional
     fig_box.update_layout(
          xaxis=dict(tickangle=45),  # Rotación de etiquetas en eje X
          plot_bgcolor='rgba(0, 0, 0, 0)',
          paper_bgcolor='rgba(0, 0, 0, 0)',
          showlegend=False  # Oculta la leyenda para reducir saturación visual
     )

     # Crear gráfico de dispersión 3
     fig_scatter = px.scatter(
          data_frame=data,
          x='Battery Capacity (kWh)',
          y='Energy Consumed (kWh)',
          color='Vehicle Model',
          title='Relación entre Capacidad de Batería y Consumo de Energía',
          labels={
               'Battery Capacity (kWh)': 'Capacidad de Batería (kWh)',
               'Energy Consumed (kWh)': 'Consumo de Energía (kWh)',
               'Vehicle Model': 'Modelo de Vehículo'
          },
          template="plotly_white",
          symbol='Vehicle Model',
     )

     # Configuración adicional
     fig_scatter.update_layout(
          legend=dict(
               title=dict(font=dict(size=14)),
               bgcolor='rgba(0, 0, 0, 0)'
          ),
          plot_bgcolor='rgba(0, 0, 0, 0)',
          paper_bgcolor='rgba(0, 0, 0, 0)'
     )

     return fig_bar, fig_box, fig_scatter

def hipotesis_4 (data):

     # Crear el gráfico de barras
     mean_costs = data.groupby('Charging Station Location', as_index=False)['Charging Cost (USD)'].mean()
     fig_bar = px.bar(
          data_frame=mean_costs,
          x='Charging Station Location',
          y='Charging Cost (USD)',
          color='Charging Station Location',
          title='Costo Promedio por Ubicación Geográfica',
          labels={
               'Charging Station Location': 'Ubicación Geográfica',
               'Charging Cost (USD)': 'Costo Promedio de Carga (USD)'
          },
          template="plotly_white",
     )
     # Configuración adicional
     fig_bar.update_layout(
          xaxis=dict(tickangle=45),  # Rotación de etiquetas en eje X
          plot_bgcolor='rgba(0, 0, 0, 0)',
          paper_bgcolor='rgba(0, 0, 0, 0)',
          showlegend=False  # Oculta la leyenda
     )

     # Crear el boxplot
     fig_box = px.box(
          data_frame=data,
          x='Charging Station Location',
          y='Charging Cost (USD)',
          color='Charging Station Location',
          title='Distribución del Costo de Carga por Ubicación',
          labels={
               'Charging Station Location': 'Ubicación Geográfica',
               'Charging Cost (USD)': 'Costo de Carga (USD)'
          },
          template="plotly_white"
     )
     # Configuración adicional
     fig_box.update_layout(
          xaxis=dict(tickangle=45),  # Rotación de etiquetas en eje X
          plot_bgcolor='rgba(0, 0, 0, 0)',
          paper_bgcolor='rgba(0, 0, 0, 0)',
          showlegend=False  # Oculta la leyenda para evitar saturación
     )

     return fig_bar, fig_box

def hipotesis_5(data):

     # Crear el gráfico de barras
     avg_cost_user = data.groupby('User Type', as_index=False)['Charging Cost (USD)'].mean()
     fig_bar = px.bar(
          data_frame=avg_cost_user,
          x='User Type',
          y='Charging Cost (USD)',
          color='User Type',
          title='Costo Promedio de Carga por Tipo de Usuario',
          labels={
               'User Type': 'Tipo de Usuario',
               'Charging Cost (USD)': 'Costo Promedio de Carga (USD)'
          },
          template="plotly_white",
     )
     # Configuración adicional
     fig_bar.update_layout(
          xaxis=dict(tickangle=45),  # Rotación de etiquetas en eje X
          plot_bgcolor='rgba(0, 0, 0, 0)',
          paper_bgcolor='rgba(0, 0, 0, 0)',
          showlegend=False  # Oculta la leyenda para evitar saturación visual
     )

     # Crear el boxplot
     fig_box = px.box(
          data_frame=data,
          x='User Type',
          y='Charging Cost (USD)',
          color='User Type',
          title='Distribución del Costo de Carga por Tipo de Usuario',
          labels={
               'User Type': 'Tipo de Usuario',
               'Charging Cost (USD)': 'Costo de Carga (USD)'
          },
          template="plotly_white"
     )
     # Configuración adicional
     fig_box.update_layout(
          xaxis=dict(tickangle=45),  # Rotación de etiquetas en eje X
          plot_bgcolor='rgba(0, 0, 0, 0)',
          paper_bgcolor='rgba(0, 0, 0, 0)',
          showlegend=False  # Oculta la leyenda para simplificar
     )

     # Crear gráfico de dispersión
     fig_scatter = px.scatter(
          data_frame=data,
          x='Energy Consumed (kWh)',
          y='Charging Cost (USD)',
          color='User Type',
          title='Relación entre Energía Consumida y Costo de Carga por Tipo de Usuario',
          labels={
               'Energy Consumed (kWh)': 'Energía Consumida (kWh)',
               'Charging Cost (USD)': 'Costo de Carga (USD)',
               'User Type': 'Tipo de Usuario'
          },
          template="plotly_white",
          symbol='User Type'
     )

     # Configuración adicional
     fig_scatter.update_layout(
          legend=dict(
               title=dict(font=dict(size=14)),
               bgcolor='rgba(0, 0, 0, 0)'
          ),
          plot_bgcolor='rgba(0, 0, 0, 0)',
          paper_bgcolor='rgba(0, 0, 0, 0)'
     )


     return fig_bar, fig_box, fig_scatter