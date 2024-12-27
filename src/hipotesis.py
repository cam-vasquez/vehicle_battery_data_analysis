# ------------------ AQUI VA A CONTENER LOS MODULOS DE HIPOTESIS -------------- #
from matplotlib import pyplot as plt
import seaborn as sns
import plotly.express as px


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
    # Configuración de la figura con fondo transparente
    plt.figure(figsize=(12, 8), facecolor='none')  # Fondo transparente
    sns.scatterplot(
        data=data,
        x='Energy Consumed (kWh)',
        y='Charging Cost (USD)',
        hue='Charger Type',
        style='Charger Type',
        alpha=0.7  # Transparencia de los puntos
    )
    plt.title('Relación entre Energía Consumida y Costo de Carga por Tipo de Cargador', fontsize=14)
    plt.xlabel('Energía Consumida (kWh)', fontsize=12)
    plt.ylabel('Costo de Carga (USD)', fontsize=12)
    plt.grid(True, alpha=0.3)  # Grilla con baja opacidad
    plt.legend(title='Tipo de Cargador')
    plt.gca().set_facecolor('none')  # Fondo del gráfico transparente
    plt.tight_layout()  # Asegura que los elementos del gráfico no se recorten
    
    fig2 = plt.gcf()  # Obtiene la figura actual
    return fig2
